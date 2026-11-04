#!/usr/bin/env python3
"""
compare_runs.py - headline metrics and paired tests for prompt versions on the same buildings.

For each split (all, dev, test from results/split.csv): coverage (Wilson CI), RMSE, median APE,
median |log(est/true)|, geometric-mean bias, CV across runs; and for every pair of runs a McNemar
test on ±20% coverage and a Wilcoxon signed-rank test on |log(est/true)|.

Usage:  python analysis/compare_runs.py 20261104_baseline-innate 20261104_prompt-v2 20261104_prompt-v3
Writes: analysis/compare_<runs>.md
"""

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import summarize_run as sr  # noqa: E402


def wilson(k, n):
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    return ci.low, ci.high


def main(runs):
    split = pd.read_csv(ROOT / "results" / "split.csv").set_index("project_index")["split"]
    data = {r: sr.load(sr.RESULTS_ROOT / r).set_index("project_index") for r in runs}
    lines = [f"# Prompt comparison: {' vs '.join(runs)}", "",
             "Enclosure A1–A3, kgCO2e/m² floor area. Estimate = mean of run midpoints. "
             "Split from analysis/make_split.py (seed 226, 30% test, assigned after the runs).", ""]
    for name in ["all", "dev", "test"]:
        idx = split.index if name == "all" else split.index[split == name]
        lines += [f"## {name} (n={len(idx)})", "",
                  "| run | ±20% coverage (95% CI) | RMSE | median APE | median abs log error | est/true geo-mean | CV across runs |",
                  "|---|---|---|---|---|---|---|"]
        for r in runs:
            d = data[r].loc[idx]
            k, n = int(d["inside"].sum()), len(d)
            lo, hi = wilson(k, n)
            e = d["estimate"] - d["truth"]
            lr = np.log(d["ratio"])
            lines.append(f"| {r} | {100*k/n:.1f}% ({100*lo:.1f}–{100*hi:.1f}) | {np.sqrt((e**2).mean()):.1f} | "
                         f"{100*d['ape'].median():.1f}% | {lr.abs().median():.3f} | {np.exp(lr.mean()):.2f} | "
                         f"{100*d['cv_runs'].mean():.1f}% |")
        lines += ["", "| pair | inside only A / only B | McNemar p | median abs log error A → B | Wilcoxon p | B closer |",
                  "|---|---|---|---|---|---|"]
        for a, b in itertools.combinations(runs, 2):
            A, B = data[a].loc[idx], data[b].loc[idx]
            oa, ob = int((A["inside"] & ~B["inside"]).sum()), int((~A["inside"] & B["inside"]).sum())
            p_mc = stats.binomtest(min(oa, ob), oa + ob).pvalue if oa + ob else 1.0
            ea, eb = np.log(A["ratio"]).abs(), np.log(B["ratio"]).abs()
            p_w = stats.wilcoxon(ea, eb).pvalue
            lines.append(f"| A={a}, B={b} | {oa} / {ob} | {p_mc:.3f} | {ea.median():.3f} → {eb.median():.3f} | "
                         f"{p_w:.4f} | {100*(eb < ea).mean():.0f}% |")
        lines.append("")
    text = "\n".join(lines)
    out = ROOT / "analysis" / f"compare_{'_vs_'.join(runs)}.md"
    out.write_text(text, encoding="utf-8")
    print(text)
    print(f"Saved {out}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Usage: python analysis/compare_runs.py <run1> <run2> [...]")
    main(sys.argv[1:])
