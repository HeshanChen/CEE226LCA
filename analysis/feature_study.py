#!/usr/bin/env python3
"""
feature_study.py - which input features matter? Prompt v3 with different feature sets.

Conditions (all prompt v3, same buildings, seeds and chunks):
  all      = 20261104_prompt-v3 (48 features)
  early, env, min                     = 20261105_feat-<set>  (run 0)
  no-<group> (leave-one-group-out)    = 20261105_ablate-no-<group>  (1 run)

Every condition is compared with "all" on run 0 only (the ablations have one run), as paired
differences per building: ±20% coverage (McNemar) and |log(est/true)| (Wilcoxon). The three main
conditions were run once (run 0) to limit token use. Results for all / dev / test (results/split.csv).

Writes: analysis/feature_study.md, analysis/figures/feature_study.png
"""

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import experiment_config as cfg  # noqa: E402

RES = ROOT / "results"
DELTA = 0.20
REF = "all"
CONDITIONS = {"all": "20261104_prompt-v3", "early": "20261105_feat-early", "env": "20261105_feat-env",
              "min": "20261105_feat-min",
              **{f"no-{g}": f"20261105_ablate-no-{g}" for g in cfg.FEATURE_GROUPS}}
INK, INK2, GRID, SURFACE, SERIES = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb", "#2a78d6"
# Run-to-run spread of median |log err| for prompt v3 itself (runs 0/1/2: 0.461, 0.436, 0.454)
NOISE = 0.025


def estimates(run: str, runs=None) -> pd.Series:
    """Per-building mean of parsed run midpoints, optionally restricted to some run indices."""
    out = {}
    for f in (RES / run).glob("project-*_runs.csv"):
        df = pd.read_csv(f)
        df = df[df["parse_ok"].astype(str) == "True"]
        if runs is not None:
            df = df[df["run_idx"].isin(runs)]
        mids = pd.to_numeric(df["mid"], errors="coerce").dropna()
        if len(mids):
            out[int(re.search(r"project-(\d+)_", f.name).group(1))] = mids.mean()
    return pd.Series(out, dtype=float)


def metrics(est, truth):
    d = pd.DataFrame({"e": est, "t": truth}).dropna()
    lr = np.log(d["e"] / d["t"])
    inside = (d["t"] >= d["e"] * (1 - DELTA)) & (d["t"] <= d["e"] * (1 + DELTA))
    return {"n": len(d), "coverage %": 100 * inside.mean(), "median |log err|": lr.abs().median(),
            "geo-mean est/true": float(np.exp(lr.mean())), "RMSE": float(np.sqrt(((d["e"] - d["t"]) ** 2).mean())),
            "_inside": inside, "_abslr": lr.abs()}


def paired(m_ref, m_x):
    i = m_ref["_inside"].index.intersection(m_x["_inside"].index)
    a, b = m_ref["_inside"].loc[i], m_x["_inside"].loc[i]
    oa, ob = int((a & ~b).sum()), int((~a & b).sum())
    p_mc = stats.binomtest(min(oa, ob), oa + ob).pvalue if oa + ob else 1.0
    ea, eb = m_ref["_abslr"].loc[i], m_x["_abslr"].loc[i]
    p_w = stats.wilcoxon(ea, eb).pvalue if (ea != eb).any() else 1.0
    return {"Δ coverage pp": 100 * (b.mean() - a.mean()), "Δ median |log err|": eb.median() - ea.median(),
            "McNemar p": p_mc, "Wilcoxon p": p_w, "closer than all %": 100 * (eb < ea).mean()}


def table(rows):
    cols = list(rows[0].keys())
    fmt = lambda v: f"{v:.3f}" if isinstance(v, float) and abs(v) < 1 else (f"{v:.1f}" if isinstance(v, float) else str(v))
    return "\n".join(["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)] +
                     ["| " + " | ".join(fmt(r[c]) for c in cols) + " |" for r in rows])


def main():
    gt = pd.read_csv(RES / "ground_truth.csv")
    truth = pd.Series(gt["ECI_true_kgCO2e_m2"].values, index=gt["Project Name"].str.extract(r"(\d+)")[0].astype(int))
    split = pd.read_csv(RES / "split.csv").set_index("project_index")["split"]
    avail = {k: v for k, v in CONDITIONS.items() if any((RES / v).glob("project-*_runs.csv"))}
    missing = sorted(set(CONDITIONS) - set(avail))
    n_feat = {k: (48 if cfg.FEATURE_SETS[k] == "all" else len(cfg.FEATURE_SETS[k])) for k in CONDITIONS}
    run0 = {k: estimates(v, runs=[0]) for k, v in avail.items()}
    lines = ["# Feature study (prompt v3)", "",
             "Paired with the full 48-feature set ('all') on run 0 of every condition. Δ < 0 in |log err| = better than all.",
             f"Missing conditions: {missing or 'none'}", ""]
    fig_rows = []
    for sp in ["all", "dev", "test"]:
        idx = truth.index if sp == "all" else split.index[split == sp]
        ref = metrics(run0[REF].reindex(idx), truth.reindex(idx))
        rows = []
        for k in avail:
            m = metrics(run0[k].reindex(idx), truth.reindex(idx))
            row = {"condition": k, "features": n_feat[k], "n": m["n"], "coverage %": m["coverage %"],
                   "median |log err|": m["median |log err|"], "geo-mean est/true": m["geo-mean est/true"],
                   "RMSE": m["RMSE"]}
            if k != REF:
                row.update(paired(ref, m))
            else:
                row.update({"Δ coverage pp": 0.0, "Δ median |log err|": 0.0, "McNemar p": 1.0, "Wilcoxon p": 1.0,
                            "closer than all %": 0.0})
            rows.append(row)
            if sp == "all":
                fig_rows.append(row)
        lines += [f"## {sp} split, run 0", "", table(rows), ""]
    out = ROOT / "analysis" / "feature_study.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

    # figure: Δ median |log err| vs all (run 0, all buildings), sorted
    fr = [r for r in fig_rows if r["condition"] != REF]
    if fr:
        fr.sort(key=lambda r: r["Δ median |log err|"])
        fig, ax = plt.subplots(figsize=(7.6, 0.45 * len(fr) + 1.6), facecolor=SURFACE)
        ax.set_facecolor(SURFACE)
        y = np.arange(len(fr))
        vals = [r["Δ median |log err|"] for r in fr]
        ax.axvspan(-NOISE, NOISE, color=GRID, alpha=0.6, zorder=0, linewidth=0)
        ax.barh(y, vals, color=SERIES, height=0.55, zorder=2)
        ax.axvline(0, color=INK2, linewidth=1)
        ax.set_xlim(-0.06, 0.06)
        ax.text(NOISE, len(fr) - 0.35, " run-to-run spread of v3 (±0.025)", fontsize=7.5, color=INK2, va="bottom")
        ax.set_yticks(y, [f"{r['condition']}  ({r['features']} features)" for r in fr], fontsize=8.5, color=INK)
        for yi, r in zip(y, fr):
            star = " *" if r["Wilcoxon p"] < 0.05 else ""
            v = r["Δ median |log err|"]
            ax.text(v + (0.002 if v >= 0 else -0.002), yi, f"{v:+.3f}{star}", va="center",
                    ha="left" if v >= 0 else "right", fontsize=8, color=INK2, zorder=3)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(colors=INK2, labelsize=8.5)
        ax.grid(axis="x", color=GRID, linewidth=0.6, zorder=0)
        ax.set_xlabel("Δ median |log(est/true)| vs all 48 features (run 0; right = worse)", color=INK, fontsize=9)
        ax.set_title("Which features matter? Prompt v3, 292 buildings", loc="left", color=INK, fontsize=11)
        fig.text(0.01, 0.01, "* Wilcoxon signed-rank p < 0.05 (paired by building)", fontsize=7.5, color=INK2)
        fig.tight_layout(rect=(0, 0.04, 1, 1))
        (ROOT / "analysis" / "figures").mkdir(exist_ok=True)
        fig.savefig(ROOT / "analysis" / "figures" / "feature_study.png", dpi=200, facecolor=SURFACE)
        plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
