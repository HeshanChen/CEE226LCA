#!/usr/bin/env python3
"""
wb1_study.py - whole building (A-C), the model alone: prompt wb1 (no mass route, no benchmark, no tables).

wb1 is the "full model" version of the whole-building task: Claude Opus 5.5 estimates the whole-building A-C
intensity from the 48 features with its own knowledge only, like the course's "innate" condition. Nothing in it
is fitted to the reference data, so its numbers are not in-sample. Compares it with the course reference results
(Gemini, 10 runs), with the model's own estimate inside wb5 (Step A, written next to the mass route and the
benchmark) and with wb5 itself. Draws report/figures/fig_bands_wholebuilding_wb1.png (wb1 vs wb5).

Usage:  python analysis/wb1_study.py [wb1 run name]
Writes analysis/wb1_study.md.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "report"))
from _common_fit import load  # noqa: E402
from fit_wb_tables import wb_truth, extremes  # noqa: E402
from wb_study import parts, COURSE  # noqa: E402

WB5_RUN = "20261116_wholebuilding-wb5"


def metrics(e, W):
    d = pd.DataFrame({"e": e, "t": W}).dropna()
    inside = (d.t >= .8 * d.e) & (d.t <= 1.2 * d.e)
    k, n = int(inside.sum()), len(d)
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    lr = np.log(d.e / d.t)
    lo, hi = d.t <= W.quantile(.15), d.t >= W.quantile(.85)
    return {"k": k, "n": n, "cov": 100 * k / n, "lo": 100 * ci.low, "hi": 100 * ci.high,
            "slope": float(np.polyfit(np.log(d.t), np.log(d.e), 1)[0]), "low15": 100 * float(inside[lo].mean()),
            "high15": 100 * float(inside[hi].mean()), "abslog": float(lr.abs().median()), "bias": float(np.exp(lr.mean()))}


def main(run):
    t, area, m, b, split = load()
    W = wb_truth(t.index)
    P = parts(run)
    E1 = P.groupby("project_index").mid.mean()
    P5 = parts(WB5_RUN).groupby("project_index")
    E5, A5 = P5.mid.mean(), P5.A.mean()
    have = E1.index
    sets = {"all": have, "without extremes": W.index[~extremes(W)].intersection(have),
            "test split": W.index[split == "test"].intersection(have)}
    rows = [("Best constant (414 for every building)", pd.Series(414.0, index=W.index)),
            ("**wb1: the model alone (no tables)**", E1),
            ("wb5, Step A only (own estimate written next to the tables)", A5),
            ("wb5: 0.2 A + 0.5 mass route + 0.3 benchmark (tables fitted, in-sample)", E5)]
    out = [f"# Whole building (A-C): the model alone, prompt wb1 (`{run}`, {P.run_idx.nunique()} run, {len(have)} buildings)", "",
           "wb1 gives the model the 48 features and the target definition only: no mass route, no benchmark, no fitted "
           "table. Nothing in it is fitted to the reference data.", "",
           "| Estimator | " + " | ".join(f"coverage, {k} ({len(v)})" for k, v in sets.items()) +
           " | slope | lowest 15% | highest 15% | median abs log | bias |", "|---|" + "---|" * (len(sets) + 5)]
    for name, e in rows:
        r = {k: metrics(e.reindex(i), W.loc[i]) for k, i in sets.items()}
        a = r["all"]
        out.append(f"| {name} | " + " | ".join(f"{v['cov']:.1f}%" for v in r.values()) +
                   f" | {a['slope']:.2f} | {a['low15']:.1f}% | {a['high15']:.1f}% | {a['abslog']:.3f} | {a['bias']:.2f} |")
    for name, v in COURSE.items():
        out.append(f"| {name} | {v:.1f}% | – | – | – | – | – | – | – |")
    c = metrics(E1, W.loc[have])
    i1 = (W.loc[have] >= .8 * E1) & (W.loc[have] <= 1.2 * E1)
    i5 = (W.loc[have] >= .8 * E5.reindex(have)) & (W.loc[have] <= 1.2 * E5.reindex(have))
    o1, o5 = int((i1 & ~i5).sum()), int((~i1 & i5).sum())
    p = stats.binomtest(min(o1, o5), o1 + o5).pvalue if o1 + o5 else 1.0
    out += ["", f"wb1 coverage, all buildings: {c['k']}/{c['n']} = {c['cov']:.1f}% (95% CI {c['lo']:.1f}–{c['hi']:.1f}); "
            f"median estimate / reference {np.exp(np.median(np.log(E1 / W.loc[have]))):.2f}.",
            f"wb5 against wb1: {o5} buildings inside only with wb5, {o1} only with wb1 (McNemar p = {p:.3g})."]
    (Path(__file__).resolve().parent / "wb1_study.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))
    import make_figures as mf
    mf.fig_bands([(f"Model alone (wb1, slope {c['slope']:.2f})", E1),
                  (f"wb5: + mass route + benchmark (slope {metrics(E5.reindex(have), W.loc[have])['slope']:.2f})", E5.reindex(have))],
                 W.loc[have], "fig_bands_wholebuilding_wb1", unit="Whole building A–C, kgCO$_2$e/m$^2$")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261119_wholebuilding-wb1")
