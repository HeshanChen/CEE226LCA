#!/usr/bin/env python3
"""
wb6_study.py - whole-building (A-C) results of prompt wb6 against wb5 (both IN-SAMPLE by design).

wb6 was built to keep the head and tail of the band figure on the curve (see analysis/fit_wb6_tables.py).
Reports coverage, the log-log slope of estimate on reference (1 = no compression), coverage of the lowest
and highest 15% of reference values, median abs log error and bias; whether the model applied the tables
(M = mass intensity x F x K, FINAL = 0.9 M + 0.1 A kept inside the typical range); and draws the band
figure wb5 vs wb6 (report/figures/fig_bands_wholebuilding_wb6.png).

Usage:  python analysis/wb6_study.py [wb6 run name]
Writes analysis/wb6_study.md.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "report"))
from _common_fit import load, RES  # noqa: E402
from fit_wb_tables import wb_truth, extremes  # noqa: E402
from fit_wb6_tables import wb6_features, apply  # noqa: E402
from wb_study import parts, COURSE  # noqa: E402

WB5_RUN = "20261116_wholebuilding-wb5"


def metrics(e, W):
    d = pd.DataFrame({"e": e, "t": W}).dropna()
    k, n = int(((d.t >= .8 * d.e) & (d.t <= 1.2 * d.e)).sum()), len(d)
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    lr = np.log(d.e / d.t)
    lo, hi = d.t <= W.quantile(.15), d.t >= W.quantile(.85)
    inside = (d.t >= .8 * d.e) & (d.t <= 1.2 * d.e)
    return {"k": k, "n": n, "cov": 100 * k / n, "lo": 100 * ci.low, "hi": 100 * ci.high,
            "slope": float(np.polyfit(np.log(d.t), np.log(d.e), 1)[0]),
            "low15": 100 * float(inside[lo].mean()), "high15": 100 * float(inside[hi].mean()),
            "under": int((d.t > 1.2 * d.e).sum()), "over": int((d.t < .8 * d.e).sum()),
            "abslog": float(lr.abs().median()), "bias": float(np.exp(lr.mean()))}


def main(run):
    t, area, m, b, split = load()
    W = wb_truth(t.index)
    F, mi = wb6_features(m, area)
    T = json.loads((RES / "wb6_tables.json").read_text())
    P = parts(run)
    n_runs = int(P.run_idx.nunique())
    g = P.groupby("project_index")
    E6, A6, M6 = g.mid.mean(), g.A.mean(), g.M.mean()
    E5 = parts(WB5_RUN).groupby("project_index").mid.mean()
    have = E6.index
    fit = W.index[~extremes(W)].intersection(have)
    test = W.index[split == "test"].intersection(have)
    sets = {"all": have, "without extremes": fit, "test split": test}
    rows = [("Best constant (414 for every building)", pd.Series(414.0, index=W.index)),
            ("wb5 (0.2 A + 0.5 M + 0.3 B)", E5),
            ("wb6: own estimate only (Step A)", A6), ("wb6: mass route only (Step M)", M6),
            ("wb6 (0.9 M + 0.1 A, kept inside the typical range)", E6)]
    out = [f"# Whole building (A-C): prompt wb6 (`{run}`, {n_runs} run(s), {len(have)} buildings)", "",
           "**In-sample by design**: the factors F and K and the typical ranges were fitted on the reference values "
           "of the same buildings (all except 13 extreme values). The test-split column is in-sample too.", "",
           "| Estimator | " + " | ".join(f"coverage, {k} ({len(v)})" for k, v in sets.items()) +
           " | slope | lowest 15% | highest 15% | median abs log | bias |",
           "|---|" + "---|" * (len(sets) + 5)]
    for name, e in rows:
        r = {k: metrics(e.reindex(i), W.loc[i]) for k, i in sets.items()}
        a = metrics(e.reindex(have), W.loc[have])
        out.append(f"| {name} | " + " | ".join(f"{v['cov']:.1f}%" for v in r.values()) +
                   f" | {a['slope']:.2f} | {a['low15']:.1f}% | {a['high15']:.1f}% | {a['abslog']:.3f} | {a['bias']:.2f} |")
    for name, v in COURSE.items():
        out.append(f"| {name} | {v:.1f}% | – | – | – | – | – | – | – |")
    c6, c5 = metrics(E6, W.loc[have]), metrics(E5.reindex(have), W.loc[have])
    out += ["", f"wb6 coverage, all buildings: {c6['k']}/{c6['n']} = {c6['cov']:.1f}% (95% CI {c6['lo']:.1f}-{c6['hi']:.1f}); "
            f"wb5: {c5['k']}/{c5['n']} = {c5['cov']:.1f}%.",
            f"Reference above the band (underestimated): wb5 {c5['under']}, wb6 {c6['under']}. "
            f"Reference below the band (overestimated): wb5 {c5['over']}, wb6 {c6['over']}.",
            "Slope = least-squares slope of log estimate on log reference; 1 means the estimates spread as much as the "
            "references, below 1 means they are pulled toward the average.", ""]
    # paired test wb6 vs wb5
    i5 = (W.loc[have] >= .8 * E5.reindex(have)) & (W.loc[have] <= 1.2 * E5.reindex(have))
    i6 = (W.loc[have] >= .8 * E6) & (W.loc[have] <= 1.2 * E6)
    o5, o6 = int((i5 & ~i6).sum()), int((~i5 & i6).sum())
    p = stats.binomtest(min(o5, o6), o5 + o6).pvalue if o5 + o6 else 1.0
    out += [f"Paired with wb5: {o6} buildings move inside the band, {o5} move outside (McNemar p = {p:.3g}).", ""]
    # did the model apply the tables?
    Q = P.dropna(subset=["A", "M"]).copy()
    M_exp, lo, hi, _ = apply(T, F, mi, pd.Series(0.0, index=F.index))
    Q["M_exp"] = M_exp.reindex(Q.project_index).values
    Q["lo"], Q["hi"] = lo.reindex(Q.project_index).values, hi.reindex(Q.project_index).values
    raw = 0.9 * Q.M + 0.1 * Q.A
    Q["final_exp"] = raw.clip(Q.lo.fillna(0), Q.hi.fillna(np.inf))
    clipped = (raw < Q.lo) | (raw > Q.hi)
    out += ["**Did the model apply the tables?**", "",
            f"- Both evidence lines parsed in {100 * P[['A', 'M']].notna().all(axis=1).mean():.1f}% of answers.",
            f"- M within 5% of mass intensity x F x K: {100 * ((Q.M / Q.M_exp - 1).abs() < 0.05).mean():.1f}%.",
            f"- Range centred on 0.9 M + 0.1 A, kept inside the typical range (within 3%): "
            f"{100 * ((Q.mid - Q.final_exp).abs() / Q.final_exp < 0.03).mean():.1f}%.",
            f"- 0.9 M + 0.1 A fell outside the typical range for {int(clipped.sum())} buildings; the reported estimate "
            f"sits at the range edge for {int((clipped & ((Q.mid - Q.final_exp).abs() / Q.final_exp < 0.03)).sum())} of them.",
            "", "**Median estimate / reference by reference band** (1.00 = no bias)", "",
            "| Reference, kgCO2e/m2 | n | wb5 | wb6 |", "|---|---|---|---|"]
    for a, bnd in [(0, 250), (250, 350), (350, 450), (450, 550), (550, 700), (700, 1e9)]:
        ix = W.loc[have][(W.loc[have] >= a) & (W.loc[have] < bnd)].index
        out.append(f"| {a}-{'' if bnd > 1e8 else int(bnd)} | {len(ix)} | {float(np.median(E5.reindex(ix) / W.loc[ix])):.2f} | "
                   f"{float(np.median(E6.reindex(ix) / W.loc[ix])):.2f} |")
    (Path(__file__).resolve().parent / "wb6_study.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))
    import make_figures as mf
    mf.fig_bands([(f"wb5 (slope {c5['slope']:.2f})", E5.reindex(have)), (f"wb6 / V6 (slope {c6['slope']:.2f})", E6)],
                 W.loc[have], "fig_bands_wholebuilding_wb6", unit="Whole building A–C, kgCO$_2$e/m$^2$")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261116_wholebuilding-wb6")
