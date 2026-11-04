#!/usr/bin/env python3
"""
summarize_run.py - proposal metrics for one run folder, overall and by climate zone / building use.

Adds what LLM-data-cleaning.py and make_fig1_bands.py do not report:
  MAPE and median APE, geometric-mean bias (est/true), +/-20% coverage,
  within-project CV across repeated runs (consistency), and the same metrics per
  site_clim_zone and bldg_prim_use (RQ1: climate- and use-specific behaviour).

Reads:   results/<run>/project-#_runs.csv, results/ground_truth.csv,
         references/buildings_metadata_LLM.xlsx
Writes:  results/<run>/summary.md
         results/<run>/per_project.csv
         results/<run>/figures/fig2_estimate_vs_truth.png
         results/<run>/figures/fig3_ratio_by_group.png

Usage:   python summarize_run.py 20261104_baseline-innate
"""

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_ROOT = SCRIPT_DIR / "results"
GROUND_TRUTH = RESULTS_ROOT / "ground_truth.csv"
BREAKDOWN = RESULTS_ROOT / "ground_truth_breakdown.csv"   # from GWP-calculation/enclosure_breakdown.py
METADATA = SCRIPT_DIR / "references" / "buildings_metadata_LLM.xlsx"
DELTA = 0.20
MIN_GROUP_N = 5            # groups smaller than this are pooled into "Other" in the breakdowns

INK, INK2, GRID, SURFACE, SERIES = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb", "#2a78d6"
UNITS = r"kgCO$_2$e/m$^2$"


def load(run_dir: Path) -> pd.DataFrame:
    rows = []
    for f in run_dir.glob("project-*_runs.csv"):
        df = pd.read_csv(f)
        ok = df[df["parse_ok"].astype(str) == "True"]
        mids = pd.to_numeric(ok["mid"], errors="coerce").dropna()
        if mids.empty:
            continue
        best = pd.to_numeric(ok["best"], errors="coerce").dropna() if "best" in ok else pd.Series(dtype=float)
        rows.append({"project_index": int(re.search(r"project-(\d+)_", f.name).group(1)),
                     "estimate": mids.mean(), "sd_runs": mids.std(ddof=1) if len(mids) > 1 else np.nan,
                     "n_runs": len(mids), "estimate_best": best.mean() if len(best) else np.nan})
    if not rows:
        raise SystemExit(f"No parsed runs in {run_dir}")
    est = pd.DataFrame(rows)
    gt = pd.read_csv(GROUND_TRUTH)
    gt["project_index"] = gt["Project Name"].str.extract(r"(\d+)")[0].astype(int)
    meta = pd.read_excel(METADATA)[["project_index", "site_clim_zone", "bldg_prim_use", "bldg_proj_type"]]
    d = est.merge(gt[["project_index", "ECI_true_kgCO2e_m2"]], on="project_index").merge(meta, on="project_index")
    d = d.rename(columns={"ECI_true_kgCO2e_m2": "truth"}).dropna(subset=["truth"])
    d["cv_runs"] = d["sd_runs"] / d["estimate"]
    d["climate"] = d["site_clim_zone"].fillna("Unknown").str.replace(r"\s*\(.*\)", "", regex=True)
    d["flag_incomplete"] = False
    if BREAKDOWN.exists():
        fl = pd.read_csv(BREAKDOWN).set_index("project_index")["flag_incomplete"]
        d["flag_incomplete"] = d["project_index"].map(fl).fillna(False).astype(bool)
    return derive(d.sort_values("project_index"), "estimate")


def derive(d: pd.DataFrame, col: str) -> pd.DataFrame:
    """Error columns for the estimate in column `col` (run-mean midpoint or run-mean BEST)."""
    d = d.copy()
    d["estimate"] = d[col]
    d["ratio"] = d["estimate"] / d["truth"]
    d["ape"] = (d["estimate"] - d["truth"]).abs() / d["truth"]
    d["inside"] = (d["truth"] >= d["estimate"] * (1 - DELTA)) & (d["truth"] <= d["estimate"] * (1 + DELTA))
    return d


def metrics(d: pd.DataFrame) -> dict:
    e = d["estimate"] - d["truth"]
    return {"n": len(d),
            "RMSE": np.sqrt((e ** 2).mean()), "MAE": e.abs().mean(),
            "MAPE %": 100 * d["ape"].mean(), "median APE %": 100 * d["ape"].median(),
            "geo-mean est/true": float(np.exp(np.log(d["ratio"]).mean())),
            "±20% coverage %": 100 * d["inside"].mean(),
            "mean CV across runs %": 100 * d["cv_runs"].mean(),
            "median truth": d["truth"].median(), "median estimate": d["estimate"].median()}


def by_group(d: pd.DataFrame, col: str) -> pd.DataFrame:
    counts = d[col].value_counts()
    g = d[col].where(d[col].map(counts) >= MIN_GROUP_N, "Other")
    rows = [{col: k, **metrics(sub)} for k, sub in d.groupby(g)]
    return pd.DataFrame(rows).sort_values("n", ascending=False)


def fmt(df: pd.DataFrame) -> str:
    show = df.copy()
    for c in show.columns:
        if show[c].dtype.kind == "f":
            show[c] = show[c].map(lambda v: f"{v:.2f}" if "est/true" in c else f"{v:.1f}")
    head = "| " + " | ".join(map(str, show.columns)) + " |"
    sep = "|" + "---|" * len(show.columns)
    body = ["| " + " | ".join(map(str, r)) + " |" for r in show.itertuples(index=False)]
    return "\n".join([head, sep, *body])


def style(ax):
    ax.set_facecolor(SURFACE)
    ax.spines[["top", "right"]].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
    ax.tick_params(colors=INK2, labelsize=8.5)
    ax.grid(True, color=GRID, linewidth=0.6, zorder=0)


def fig_scatter(d: pd.DataFrame, run: str, out: Path):
    fig, ax = plt.subplots(figsize=(5.6, 5.2), facecolor=SURFACE)
    style(ax)
    lo = min(d["truth"].min(), d["estimate"].min()) * 0.8
    hi = max(d["truth"].max(), d["estimate"].max()) * 1.25
    x = np.array([lo, hi])
    ax.fill_between(x, x / (1 + DELTA), x / (1 - DELTA), color=SERIES, alpha=0.10, linewidth=0, zorder=1)
    ax.plot(x, x, color=INK2, linewidth=1.0, zorder=2)
    ax.scatter(d["truth"], d["estimate"], s=16, color=SERIES, edgecolor=SURFACE, linewidth=0.6, zorder=3)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
    ticks = [t for t in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000) if lo <= t <= hi]
    ax.set_xticks(ticks, [str(t) for t in ticks]); ax.set_yticks(ticks, [str(t) for t in ticks])
    ax.minorticks_off()
    ax.set_xlabel(f"Reference LCA, enclosure A1–A3 ({UNITS})", color=INK, fontsize=9.5)
    ax.set_ylabel(f"LLM estimate, mean of runs ({UNITS})", color=INK, fontsize=9.5)
    m = metrics(d)
    ax.set_title(f"Estimate vs. reference ({m['n']} buildings)", loc="left", color=INK, fontsize=11)
    ax.text(0.02, 0.97, f"line = 1:1, band = truth inside ±{DELTA:.0%} of estimate\n"
            f"coverage {m['±20% coverage %']:.1f}%, median APE {m['median APE %']:.0f}%, "
            f"RMSE {m['RMSE']:.1f}", transform=ax.transAxes, va="top", fontsize=8, color=INK2)
    fig.text(0.01, 0.005, run, fontsize=7, color=INK2)
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def fig_groups(d: pd.DataFrame, out: Path):
    panels = [("climate", "Climate zone"), ("bldg_prim_use", "Primary use")]
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), facecolor=SURFACE)
    for ax, (col, title) in zip(axes, panels):
        style(ax)
        counts = d[col].value_counts()
        g = d[col].where(d[col].map(counts) >= MIN_GROUP_N, "Other")
        stats = (d.assign(g=g).groupby("g")["ratio"]
                 .agg(med="median", q1=lambda s: s.quantile(.25), q3=lambda s: s.quantile(.75), n="size")
                 .sort_values("med"))
        y = np.arange(len(stats))
        ax.hlines(y, stats["q1"], stats["q3"], color=SERIES, linewidth=2, alpha=0.45, zorder=2)
        ax.scatter(stats["med"], y, s=36, color=SERIES, edgecolor=SURFACE, linewidth=1.2, zorder=3)
        ax.axvline(1, color=INK2, linewidth=1.0, zorder=1)
        ax.set_xscale("log")
        ax.set_yticks(y, [f"{k}  (n={n})" for k, n in zip(stats.index, stats["n"])], fontsize=8.5, color=INK)
        ticks = [0.25, 0.5, 1, 2, 4, 8]
        xmin, xmax = stats["q1"].min() * 0.8, stats["q3"].max() * 1.25
        ax.set_xticks([t for t in ticks if xmin <= t <= xmax] or [1])
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}×"))
        ax.minorticks_off()
        ax.set_xlabel("estimate / reference (median, IQR)", color=INK, fontsize=9)
        ax.set_title(title, loc="left", color=INK, fontsize=11)
    fig.text(0.01, 0.005, "Right of 1× = overestimate. Groups with fewer than "
             f"{MIN_GROUP_N} buildings pooled as Other.", fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    plt.close(fig)


def main(run: str):
    run_dir = RESULTS_ROOT / run
    d = load(run_dir)
    d.to_csv(run_dir / "per_project.csv", index=False)
    rows = [{"subset": "all projects", **metrics(d)},
            {"subset": "new construction only", **metrics(d[d["bldg_proj_type"] == "New Construction"])},
            {"subset": f"excl. {int(d['flag_incomplete'].sum())} incomplete ground truths",
             **metrics(d[~d["flag_incomplete"]])}]
    if d["estimate_best"].notna().all():
        b = derive(d, "estimate_best")
        rows += [{"subset": "all projects, BEST estimate", **metrics(b)},
                 {"subset": "excl. incomplete, BEST estimate", **metrics(b[~b["flag_incomplete"]])}]
    overall = pd.DataFrame(rows)
    lines = [f"# Run summary: {run}", "",
             "Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the "
             "parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). "
             "Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth "
             f"inside estimate ±{DELTA:.0%}. CV = SD / mean of a building's run midpoints.", "",
             "## Overall", "", fmt(overall), "",
             "## By climate zone", "", fmt(by_group(d, "climate")), "",
             "## By primary use", "", fmt(by_group(d, "bldg_prim_use")), ""]
    (run_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")
    fig_scatter(d, run, run_dir / "figures" / "fig2_estimate_vs_truth.png")
    fig_groups(d, run_dir / "figures" / "fig3_ratio_by_group.png")
    print("\n".join(lines[4:8]))
    print(f"Saved: {run_dir / 'summary.md'}, per_project.csv, figures/fig2_*.png, figures/fig3_*.png")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python summarize_run.py <run-name>")
    main(sys.argv[1])
