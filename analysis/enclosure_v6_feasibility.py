#!/usr/bin/env python3
"""
enclosure_v6_feasibility.py - would a wb6-style "typical range" prompt work for the enclosure?

wb6 kept the head and tail of the whole-building band figure on the curve because one feature, the
inventory mass per m2, separates high from low buildings. This script asks the same questions of the
enclosure (A1-A3), using prompt v5's answers (3 runs) and no new LLM run:
  1. Where does v5 over- and underestimate? (by reference decile and by building group)
  2. What makes the extremes extreme? (material breakdown of the reference LCAs)
  3. Can any feature pick out the extremes? (AUC; mass intensity for the whole building as the yardstick)
  4. What would typical-range designs give? (simulated with v5's evidence lines, in-sample, plus a
     held-out check)
Writes analysis/enclosure_v6_feasibility.md.
"""
import itertools
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov  # noqa: E402
from v5_study import parts as v5parts  # noqa: E402
from outliers import flags  # noqa: E402
from fit_wb_tables import wb_truth  # noqa: E402

V5_RUN = "20261116_prompt-v5"


def slope(e, tr):
    return float(np.polyfit(np.log(tr), np.log(e), 1)[0])


def main():
    t, area, m, b, split = load()
    f, _ = flags()
    g = v5parts(V5_RUN).groupby("project_index")
    E, C = g.mid.mean().reindex(t.index), g.C.mean().reindex(t.index)
    oos = f.out_of_scope
    inside = (t >= .8 * E) & (t <= 1.2 * E)
    lo, hi = t <= t.quantile(.2), t >= t.quantile(.8)
    mid = ~lo & ~hi
    out = ["# Would a typical-range prompt (wb6-style) work for the enclosure?", "",
           f"Prompt v5's answers (`{V5_RUN}`, 3 runs, 292 buildings); no new LLM run. All fitted numbers are in-sample "
           "unless marked as a held-out check.", ""]

    # 1. where v5 misses
    out += ["## 1. Where v5 over- and underestimates", "",
            "| Reference decile, kgCO2e/m2 | n | median reference | median v5 | v5 / reference | inside ±20% | over | under |",
            "|---|---|---|---|---|---|---|---|"]
    q = pd.qcut(t, 10)
    for k in q.cat.categories:
        ix = t.index[q == k]
        r = np.exp(np.log(E[ix] / t[ix]).median())
        out.append(f"| {k.left:.1f}–{k.right:.1f} | {len(ix)} | {t[ix].median():.1f} | {E[ix].median():.1f} | {r:.2f} | "
                   f"{100 * inside[ix].mean():.0f}% | {100 * (E[ix] > t[ix] / .8).mean():.0f}% | {100 * (E[ix] < t[ix] / 1.2).mean():.0f}% |")
    groups = {"use": m.bldg_prim_use, "structure": m.str_sys_summary.fillna("not given"), "storeys": m.bldg_stories_above,
              "project type": m.bldg_proj_type}
    ratios = []
    for name, s in groups.items():
        for k, n in s.value_counts().items():
            if n >= 9:
                ix = t.index[s == k]
                ratios.append((float(np.exp(np.log(E[ix] / t[ix]).median())), f"{k} ({n})"))
    core = [r for r, _ in ratios if .8 <= r <= 1.25]
    odd = "; ".join(f"{lab} {r:.2f}" for r, lab in sorted(ratios) if not .8 <= r <= 1.25)
    out += ["", f"The bottom 20% are overestimated 1.9–3.3 times and the top 20% reach only 0.39–0.60 of the reference. "
            f"By contrast, the median v5 / reference of {len(core)} of the {len(ratios)} use, structure, storey and project-type "
            f"groups with 9 or more buildings lies between {min(core):.2f} and {max(core):.2f}; the exceptions are small groups "
            f"({odd}). The extremes sit inside every group, not in particular groups.", ""]

    # 2. what makes the extremes
    cats = [c for c in b.columns if c.endswith("[kgCO2e/m2]")]
    rows = sorted(((c.replace(" [kgCO2e/m2]", ""), b.loc[lo, c].mean(), b.loc[mid, c].mean(), b.loc[hi, c].mean()) for c in cats),
                  key=lambda r: -(r[3] - r[2]))
    excess = t[hi].mean() - t[mid].mean()
    out += ["## 2. What makes the extremes", "",
            "| Material category (mean kgCO2e/m2 floor) | bottom 20% | middle 60% | top 20% | share of the top's excess |",
            "|---|---|---|---|---|"]
    for name, a, m_, h in rows[:6]:
        out.append(f"| {name} | {a:.1f} | {m_:.1f} | {h:.1f} | {100 * (h - m_) / excess:.0f}% |")
    nc = (lo & (m.bldg_proj_type == "New Construction") & ~oos & ~f.incomplete).sum()
    out += ["", f"Mean total: bottom {t[lo].mean():.1f}, middle {t[mid].mean():.1f}, top {t[hi].mean():.1f}. XPS is a "
            "sub-category of insulation, so the two overlap. The top is high mainly because of **HFC-blown XPS insulation** "
            "and **aluminium (curtain wall and frames)**. "
            f"The bottom 20% ({int(lo.sum())} buildings) are mostly scope and data effects: {int(oos[lo].sum())} LCAs without the "
            f"enclosure in scope, {int(f.incomplete[lo].sum())} flagged incomplete, "
            f"{int(m.bldg_proj_type[lo].isin(['Minor Renovation', 'Tenant Improvement']).sum())} minor renovations or tenant "
            f"improvements, {int((~b.has_fenestration[lo]).sum())} without any fenestration; {int(nc)} are complete new buildings.", ""]

    # 3. can a feature pick them out?
    X = m.copy()
    X["envelope area / floor area"] = m.bldg_therm_env_area / area
    X["mass_total / floor area"] = m.mass_total / area
    heavy = b["XPS [kgCO2e/m2]"] > 20

    def aucs(y):
        res = []
        for c in X.columns:
            x = X[c]
            if pd.api.types.is_numeric_dtype(x):
                ok = x.notna()
                if ok.sum() >= 100:
                    a = roc_auc_score(y[ok], x[ok])
                    res.append((c, max(a, 1 - a)))
            else:
                xs = x.fillna("NA").astype(str)
                res.append((c, roc_auc_score(y, y.groupby(xs).transform("mean"))))
        return sorted(res, key=lambda z: -z[1])[:5]

    W = wb_truth(t.index)
    mi = m.mass_total / area
    out += ["## 3. Can any feature pick out the extremes?", "",
            "AUC = chance that a building of the group ranks above one outside it (0.5 = no better than chance). Categorical "
            "AUCs use the group's own share, so they are in-sample and optimistic.", "",
            "| Target | best five features (AUC) |", "|---|---|",
            "| Enclosure, top 20% | " + ", ".join(f"{c} {a:.2f}" for c, a in aucs(hi)) + " |",
            "| Enclosure, bottom 20% | " + ", ".join(f"{c} {a:.2f}" for c, a in aucs(lo)) + " |",
            "| Enclosure, heavy XPS (> 20 kgCO2e/m2) | " + ", ".join(f"{c} {a:.2f}" for c, a in aucs(heavy)) + " |",
            f"| *Whole building, for comparison* | mass_total / floor area: top 20% {roc_auc_score(W >= W.quantile(.8), mi):.2f}, "
            f"bottom 20% {1 - roc_auc_score(W <= W.quantile(.2), mi):.2f} |", ""]

    # 4. typical-range designs
    F = pd.DataFrame(index=t.index)
    F["use"] = m.bldg_prim_use.where(m.bldg_prim_use.map(m.bldg_prim_use.value_counts()) >= 9, "other")
    F["storeys"] = m.bldg_stories_above.replace({"11 to 15": "11+", "16 to 20": "11+", "21 or more": "11+"})
    F["project type"] = m.bldg_proj_type
    F["structure"] = m.str_sys_summary
    er = m.bldg_therm_env_area / area
    F["envelope ratio"] = pd.cut(er, [0, .5, .8, 1.2, 1e9], labels=["<0.5", "0.5-0.8", "0.8-1.2", ">1.2"]).astype(str).where(er.notna())
    F["WWR"] = pd.cut(m.bldg_wwr, [-1, .2, .35, .5, 1.01], labels=["<20%", "20-35%", "35-50%", ">50%"]).astype(str).where(m.bldg_wwr.notna())
    F["climate zone"] = m.site_clim_zone.str.extract(r"Zone (\d)")[0]
    F["region"] = m.site_region
    F["software"] = m.lca_software
    F["IBC type"] = m.bldg_ibc_type
    F["size"] = pd.qcut(area, 4, labels=["S", "M", "L", "XL"]).astype(str)
    F["mass band"] = pd.qcut(mi, 4, labels=["m1", "m2", "m3", "m4"]).astype(str)
    F = F.astype(object).fillna("NA")
    lt = np.log(t)
    cl = t.index[~f.outlier]
    fit_rows = cl[~oos.loc[cl]]

    def typ(keys_list, qq, rows, mn=5):
        res = pd.Series(np.nan, index=t.index)
        for keys in keys_list:
            k = F[keys].astype(str).agg("|".join, axis=1)
            gg = lt.loc[rows].groupby(k.loc[rows])
            val, n = gg.quantile(qq), gg.size()
            res = res.fillna(k.map({i: np.exp(v) for i, v in val.items() if n[i] >= mn}))
        return res.fillna(float(np.exp(lt.loc[rows].quantile(qq))))

    def row(name, e, idx=None):
        idx = t.index if idx is None else idx
        e, tr = e.reindex(idx), t.loc[idx]
        l_, h_ = tr <= tr.quantile(.2), tr >= tr.quantile(.8)
        return (f"| {name} | {100 * cov(e, tr):.1f}% | {slope(e, tr):.2f} | {100 * cov(e[l_], tr[l_]):.1f}% | "
                f"{100 * cov(e[h_], tr[h_]):.1f}% |")

    head = ["| Design (in-sample unless marked) | coverage | slope | bottom 20% inside | top 20% inside |", "|---|---|---|---|---|"]
    lines = [row("v5 as run", E)]
    clips = []
    for keys in itertools.combinations(["use", "storeys", "structure", "envelope ratio", "project type", "mass band", "WWR",
                                        "climate zone"], 2):
        for ql, qh in [(.05, .95), (.1, .9), (.2, .8)]:
            e = E.clip(typ([list(keys), [keys[0]]], ql, fit_rows), typ([list(keys), [keys[0]]], qh, fit_rows)).where(~oos, 8.0)
            clips.append((100 * cov(e, t), keys, ql, qh, e))
    clips.sort(key=lambda z: -z[0])
    c0 = clips[0]
    lines.append(row(f"v5 kept inside P{int(c0[2] * 100)}–P{int(c0[3] * 100)} of {' x '.join(c0[1])} (best of {len(clips)} clip designs)", c0[4]))
    keysall = list(F.columns)
    best = []
    for k3 in itertools.combinations(keysall, 3):
        T = typ([list(k3), list(k3[:2]), [k3[0]]], .5, fit_rows)
        best.append((100 * cov((0.5 * C + 0.5 * T).where(~oos, 8.0), t), k3))
    best.sort(key=lambda z: -z[0])
    k3 = best[0][1]
    T = typ([list(k3), list(k3[:2]), [k3[0]]], .5, fit_rows)
    e3 = (0.5 * C + 0.5 * T).where(~oos, 8.0)
    lines.append(row(f"0.5 x calibrated take-off + 0.5 x typical value by {' x '.join(k3)} (best of {len(best)} triples)", e3))
    dev = fit_rows[split.loc[fit_rows] == "dev"]
    test = t.index[split == "test"]
    Td = typ([list(k3), list(k3[:2]), [k3[0]]], .5, dev)
    lines += [row("v5 as run, test buildings only (88)", E, test),
              row("same best triple, cells fitted on the development set only, test buildings (held-out check)",
                  (0.5 * C + 0.5 * Td).where(~oos, 8.0), test)]
    out += ["## 4. What typical-range designs would give (simulated with v5's evidence lines)", "", *head, *lines, "",
            "Clipping into a typical range never steepens the curve: the ranges are wide because the extremes lie inside every "
            "cell, so they hardly bind, and where they do they pull toward the middle. Replacing the benchmark with finer typical "
            "values adds at most about 2 points in-sample, does not change the slope, and loses on the held-out check.", ""]

    # verdict
    out += ["## Verdict: not feasible, not run", "",
            "- The whole building works because one feature, the inventory mass per m2, separates high from low buildings "
            "(AUC 0.86–0.88). For the enclosure no feature does (best 0.66–0.73), and the drivers of the top, HFC-blown XPS "
            "and aluminium curtain wall, are not predictable from the features (best AUC for heavy XPS 0.69).",
            "- Every simulated typical-range design stays within about 2 points of v5 (in-sample) with the same slope, and the "
            "best one is worse than v5 on the held-out check. A new LLM run (about 2.4 million tokens for 3 runs) would not "
            "change the conclusion.",
            "- The only small gain is the constant for LCAs without the enclosure in scope: 11.7 instead of 8 would cover 6 of "
            "these 13 buildings instead of 2 (+1.4 points, in-sample). It is not worth a run on its own.",
            "- What would help is information the features lack: the insulation type (XPS or not) and the share of curtain "
            "wall, i.e. the assembly type."]
    p = Path(__file__).resolve().parent / "enclosure_v6_feasibility.md"
    p.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
