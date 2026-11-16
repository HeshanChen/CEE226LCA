#!/usr/bin/env python3
"""
make_figures.py - figures for the paper (report/latex) and the poster (report/poster).

Palette (validated with the dataviz palette checker; direct labels on every chart because the
v2 amber is below 3:1 contrast): v1 blue, v2 amber, v3 Stanford bright red.

Writes report/figures/*.png (and .pdf for LaTeX).
"""

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
sys.path.insert(0, str(ROOT / "analysis"))
import summarize_run as sr  # noqa: E402

OUT = ROOT / "report" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
RUNS = {"v1": "20261104_baseline-innate", "v2": "20261104_prompt-v2", "v3": "20261104_prompt-v3"}
V4_RUN = "20261116_prompt-v4"
COL = {"v1": "#2a78d6", "v2": "#eda100", "v3": "#B1040E"}
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
BINS = [(0, 25, "<25"), (25, 50, "25–50"), (50, 100, "50–100"), (100, 200, "100–200"), (200, 1e9, ">200")]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2,
                     "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2})


def style(ax):
    ax.set_facecolor(SURFACE)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, color=GRID, linewidth=0.6, zorder=0)


def save(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=300 if ext == "png" else None, facecolor=SURFACE,
                    bbox_inches="tight")
    plt.close(fig)


def load():
    d = {k: sr.load(sr.RESULTS_ROOT / v).set_index("project_index") for k, v in RUNS.items()}
    b = pd.read_csv(ROOT / "results" / "ground_truth_breakdown.csv").set_index("project_index")
    m = pd.read_excel(ROOT / "references" / "buildings_metadata_LLM.xlsx").set_index("project_index")
    split = pd.read_csv(ROOT / "results" / "split.csv").set_index("project_index")["split"]
    return d, b, m, split


def fig_bins(d):
    fig, ax = plt.subplots(figsize=(5.2, 3.3))
    style(ax)
    x = np.arange(len(BINS))
    for k, df in d.items():
        y = [df.loc[(df.truth >= a) & (df.truth < b_), "ratio"].median() for a, b_, _ in BINS]
        ax.plot(x, y, "-o", color=COL[k], linewidth=2, markersize=6, zorder=3,
                markeredgecolor=SURFACE, markeredgewidth=1.2)
        dy = {"v1": 6, "v2": -7, "v3": 0}[k]
        ax.annotate(f"{k}", (x[-1], y[-1]), xytext=(8, dy), textcoords="offset points", va="center",
                    fontsize=9, color=INK, fontweight="bold")
    ax.axhline(1, color=INK2, linewidth=1, zorder=2)
    ax.set_yscale("log")
    ax.set_yticks([0.25, 0.5, 1, 2], ["0.25×", "0.5×", "1×", "2×"])
    ax.minorticks_off()
    ax.set_xticks(x, [lab for *_, lab in BINS])
    ax.set_xlim(-0.3, len(BINS) - 0.4)
    ax.set_xlabel("Reference enclosure A1–A3 (kgCO$_2$e/m$^2$ floor area)")
    ax.set_ylabel("Median estimate / reference")
    ax.set_title("Compression: low values over-, high values underestimated", loc="left", fontsize=10, color=INK)
    save(fig, "fig_bins")


def fig_scatter(d):
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.5), sharey=True)
    lo, hi = 0.3, 700
    for ax, k in zip(axes, ["v1", "v3"]):
        style(ax)
        df = d[k]
        x = np.array([lo, hi])
        ax.fill_between(x, x / 1.2, x / 0.8, color=COL[k], alpha=0.10, linewidth=0, zorder=1)
        ax.plot(x, x, color=INK2, linewidth=1, zorder=2)
        ax.scatter(df.truth, df.estimate, s=10, color=COL[k], edgecolor=SURFACE, linewidth=0.4, zorder=3)
        ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
        t = [1, 10, 100]
        ax.set_xticks(t, [str(v) for v in t]); ax.set_yticks(t, [str(v) for v in t]); ax.minorticks_off()
        m = sr.metrics(df.reset_index())
        slope = np.polyfit(np.log(df.truth), np.log(df.estimate), 1)[0]
        ax.set_title(f"Prompt {k}", loc="left", fontsize=10, color=INK)
        ax.text(0.03, 0.97, f"±20% coverage {m['±20% coverage %']:.1f}%\nlog–log slope {slope:.2f}",
                transform=ax.transAxes, va="top", fontsize=8, color=INK2)
        ax.set_xlabel("Reference (kgCO$_2$e/m$^2$)")
    axes[0].set_ylabel("LLM estimate, mean of 3 runs")
    fig.tight_layout()
    save(fig, "fig_scatter_v1_v3")


def fig_prompts(d, split):
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7))
    groups = [("all", "All 292"), ("test", "Test 88")]
    for ax, metric in zip(axes, ["coverage", "logerr"]):
        style(ax)
        for gi, (g, glab) in enumerate(groups):
            idx = split.index if g == "all" else split.index[split == g]
            for ki, k in enumerate(["v1", "v2", "v3"]):
                df = d[k].loc[idx]
                y = gi * 4 + ki
                if metric == "coverage":
                    kk, n = int(df.inside.sum()), len(df)
                    ci = stats.binomtest(kk, n).proportion_ci(0.95, method="wilson")
                    v, l, h = 100 * kk / n, 100 * ci.low, 100 * ci.high
                    ax.hlines(y, l, h, color=COL[k], linewidth=2, alpha=0.5, zorder=2)
                    lab = f"{v:.1f}%"
                else:
                    v = np.log(df.ratio).abs().median()
                    lab = f"{v:.3f}"
                ax.scatter(v, y, s=40, color=COL[k], edgecolor=SURFACE, linewidth=1, zorder=3)
                ax.annotate(f"{k}  {lab}", (v, y), xytext=(0, 6), textcoords="offset points", ha="center",
                            fontsize=7.5, color=INK)
        ax.set_yticks([1, 5], [g[1] for g in groups])
        ax.set_ylim(-0.8, 7)
        ax.invert_yaxis()
        ax.set_title("±20% coverage (95% CI) — higher is better" if metric == "coverage"
                     else "Median |log(estimate/reference)| — lower is better", loc="left", fontsize=9, color=INK)
    axes[0].set_xlim(5, 40)
    axes[1].set_xlim(0.3, 0.62)
    fig.tight_layout()
    save(fig, "fig_prompts")


def fig_diagnostics(d, b, m):
    rows = [
        ("Projects with XPS", lambda df: df.index.isin(b.index[b["XPS [kgCO2e/m2]"] > 0])),
        ("Projects without XPS", lambda df: df.index.isin(b.index[b["XPS [kgCO2e/m2]"] == 0])),
        ("Cold zones 5–8", lambda df: df.climate.isin(["Zone 5A", "Zone 5B", "Zone 6A", "Zone 6B", "Zone 7", "Zone 8"])),
        ("Warm zones 1–3", lambda df: df.climate.str.match(r"Zone [123]")),
        ("Envelope area given", lambda df: df.index.isin(m.index[m.bldg_therm_env_area.notna()])),
        ("Envelope area not given", lambda df: df.index.isin(m.index[m.bldg_therm_env_area.isna()])),
        ("Major renovation", lambda df: df.bldg_proj_type == "Major Renovation"),
        ("Minor renovation", lambda df: df.bldg_proj_type == "Minor Renovation"),
    ]
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    style(ax)
    for ri, (lab, f) in enumerate(rows):
        vals = {k: df.loc[f(df), "ratio"].median() for k, df in d.items()}
        ax.hlines(ri, min(vals.values()), max(vals.values()), color=GRID, linewidth=3, zorder=1)
        for k, v in vals.items():
            ax.scatter(v, ri, s=42, color=COL[k], edgecolor=SURFACE, linewidth=1, zorder=3,
                       label=k if ri == 0 else None)
    ax.axvline(1, color=INK2, linewidth=1)
    ax.set_xscale("log")
    ax.set_xticks([0.4, 0.6, 0.8, 1, 1.25], ["0.4×", "0.6×", "0.8×", "1×", "1.25×"])
    ax.minorticks_off()
    ax.set_yticks(range(len(rows)), [r[0] for r in rows])
    ax.invert_yaxis()
    ax.set_xlabel("Median estimate / reference (1× = unbiased)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), frameon=False, fontsize=8, ncol=3,
              handletextpad=0.2, columnspacing=0.8)
    ax.set_title("Failure modes by prompt version", loc="left", fontsize=10, color=INK)
    save(fig, "fig_diagnostics")


def fig_composition(b):
    cols = {"Insulation": "Insulation [kgCO2e/m2]", "Aluminum": "Aluminum [kgCO2e/m2]",
            "Windows & frames": "Windows and frames [kgCO2e/m2]", "Concrete": "Concrete [kgCO2e/m2]",
            "Glazing": "Glazing [kgCO2e/m2]", "Steel": "Steel [kgCO2e/m2]", "Cladding": "Cladding [kgCO2e/m2]",
            "Masonry": "Masonry [kgCO2e/m2]"}
    gt = pd.read_csv(ROOT / "results" / "ground_truth.csv")
    area = gt.set_index(gt["Project Name"].str.extract(r"(\d+)")[0].astype(int))["floor_area_m2"]
    tot = (b["ECI_true_kgCO2e_m2"] * area).sum()
    shares = {k: 100 * (b[c] * area).sum() / tot for k, c in cols.items()}
    xps = 100 * (b["XPS [kgCO2e/m2]"] * area).sum() / tot
    fig, ax = plt.subplots(figsize=(5.0, 2.9))
    style(ax)
    names = list(shares)[::-1]
    vals = [shares[n] for n in names]
    ax.barh(names, vals, color="#8C1515", height=0.6, zorder=2)
    ax.barh(["Insulation"], [xps], color="#D9575F", height=0.6, zorder=3)
    for n, v in zip(names, vals):
        ax.text(v + 0.4, n, f"{v:.1f}%", va="center", fontsize=8, color=INK)
    ax.text(xps / 2, "Insulation", f"XPS {xps:.1f}%", va="center", ha="center", fontsize=7.5, color=INK,
            fontweight="bold", zorder=4)
    ax.set_xlim(0, 31)
    ax.set_xlabel("Share of enclosure A1–A3 GWP, 292 projects")
    ax.grid(axis="y", visible=False)
    ax.set_title("What enclosure carbon is made of", loc="left", fontsize=10, color=INK)
    save(fig, "fig_composition")


def fig_v4():
    """Left: coverage of constant / ML / prompts on all and cleaned buildings. Right: weight sensitivity."""
    sys.path.insert(0, str(ROOT / "analysis"))
    from _common_fit import load as load_fit, coverage as cov
    from feature_study import estimates
    from outliers import flags
    from v4_study import parts
    t, area, mm, bb, sp = load_fit()
    f, _ = flags()
    clean = t.index[~f.outlier]
    est = {"v1": estimates(RUNS["v1"]), "v3": estimates(RUNS["v3"]), "v4": estimates(V4_RUN)}
    V4C = "#175E54"
    col = {"v1": COL["v1"], "v3": COL["v3"], "v4": V4C}
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    style(ax)
    ax.grid(axis="y", visible=False)
    groups = [("All 292", t.index, 27.1, 28.4), ("Cleaned 262", clean, 30.2, 34.0)]
    for gi, (lab, idx, const, ml) in enumerate(groups):
        y0 = gi * 4.6
        ax.hlines([y0 - 0.55, y0 + 2.55], 0, 0, color="none")
        ax.axvspan(const, ml, ymin=1 - (y0 + 2.75 + 0.9) / 8.3, ymax=1 - (y0 - 0.55 + 0.9) / 8.3, color=GRID, zorder=0)
        for ki, k in enumerate(["v1", "v3", "v4"]):
            e = est[k].reindex(idx)
            kk, n = int(((t.loc[idx] >= 0.8 * e) & (t.loc[idx] <= 1.2 * e)).sum()), len(idx)
            ci = stats.binomtest(kk, n).proportion_ci(0.95, method="wilson")
            y = y0 + ki
            ax.hlines(y, 100 * ci.low, 100 * ci.high, color=col[k], linewidth=2, alpha=0.5, zorder=2)
            ax.scatter(100 * kk / n, y, s=46, color=col[k], edgecolor=SURFACE, linewidth=1, zorder=3)
            ax.annotate(f"{k}  {100 * kk / n:.1f}%", (max(100 * ci.high, ml), y), xytext=(6, 0), textcoords="offset points",
                        va="center", fontsize=8, color=INK, fontweight="bold" if k == "v4" else "normal")
        ax.text(const - 0.4, y0 + 2.62, "constant", ha="right", va="center", fontsize=6.5, color=INK2)
        ax.text(ml + 0.4, y0 + 2.62, "ML ceiling (CV)", ha="left", va="center", fontsize=6.5, color=INK2)
        ax.vlines([const, ml], y0 - 0.5, y0 + 2.75, color=INK2, linewidth=0.8, linestyles=["--", "-"], zorder=1)
    ax.set_yticks([1, 5.6], [g[0] for g in groups])
    ax.set_ylim(7.4, -0.9)
    ax.set_xlim(12, 47)
    ax.set_xlabel("±20% coverage, % (bars: 95% CI)")
    ax.set_title("v4 reaches what the features can support", loc="left", fontsize=9.5, color=INK)
    ax = axes[1]
    style(ax)
    P = parts(V4_RUN)
    A, B = P.groupby("project_index").A.mean(), P.groupby("project_index").B.mean()
    ws = np.linspace(0, 1, 11)
    for lab, idx, ls in [("cleaned, dev", t.index[~f.outlier & (sp == "dev")], "-"), ("cleaned, test", t.index[~f.outlier & (sp == "test")], "--")]:
        y = [100 * cov((w * A + (1 - w) * B).reindex(idx), t.loc[idx]) for w in ws]
        ax.plot(ws, y, ls, color=V4C, linewidth=2, zorder=3, label=lab)
    ax.axvline(0.5, color=INK2, linewidth=0.8, linestyle=":")
    ax.set_ylim(18, 40)
    ax.text(0.5, 18.5, " chosen", fontsize=7, color=INK2, va="bottom")
    ax.legend(loc="lower left", frameon=False, fontsize=7.5, handlelength=2.6)
    ax.set_xlabel("Weight on the bottom-up take-off (rest: use benchmark)")
    ax.set_ylabel("Coverage, %")
    ax.set_title("Weight sensitivity (v4's own A and B)", loc="left", fontsize=9.5, color=INK)
    fig.tight_layout()
    save(fig, "fig_v4")


def main():
    d, b, m, split = load()
    fig_bins(d)
    fig_scatter(d)
    fig_prompts(d, split)
    fig_diagnostics(d, b, m)
    fig_composition(b)
    fig_v4()
    for f in ["feature_study.png"]:
        src = ROOT / "analysis" / "figures" / f
        (OUT / f).write_bytes(src.read_bytes())
    print("Saved figures to", OUT)


if __name__ == "__main__":
    main()
