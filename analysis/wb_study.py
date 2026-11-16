#!/usr/bin/env python3
"""
wb_study.py - whole-building (A-C) results of the answer-fitted prompt wb5 (IN-SAMPLE by design).

Compares wb5 with the best constant, a random forest on the 48 features (cross-validated), and the course's
reference results for the same target (Gemini, 10 runs each, result-summary.txt). Checks whether the model
applied the tables (M, B, and the 0.2/0.5/0.3 combination) and how much each source covers on its own.
Draws the course-style band figure (report/figures/fig_bands_wholebuilding.png).

Usage:  python analysis/wb_study.py [run name]
Writes analysis/wb_study.md.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "report"))
from _common_fit import load, RES  # noqa: E402
from fit_wb_tables import wb_truth, wb_features, extremes, apply_tables  # noqa: E402

COURSE = {"Course reference, innate (Gemini, 10 runs)": 34.2, "Course reference, domain (papers)": 45.2,
          "Course reference, domain + ontology": 45.9, "Course reference, domain + benchmark": 36.3}


def parts(run):
    rows = []
    for fcsv in (RES / run).glob("project-*_runs.csv"):
        df = pd.read_csv(fcsv)
        df = df[df["parse_ok"].astype(str) == "True"]
        p = int(re.search(r"project-(\d+)_", fcsv.name).group(1))
        for _, r in df.iterrows():
            rows.append({"project_index": p, "run_idx": r["run_idx"], "mid": r["mid"],
                         "A": pd.to_numeric(r.get("bottom_up"), errors="coerce"),
                         "M": pd.to_numeric(r.get("mass_route"), errors="coerce"),
                         "B": pd.to_numeric(r.get("benchmark"), errors="coerce")})
    return pd.DataFrame(rows)


def cov_ci(e, t):
    d = pd.DataFrame({"e": e, "t": t}).dropna()
    k, n = int(((d.t >= .8 * d.e) & (d.t <= 1.2 * d.e)).sum()), len(d)
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    lr = np.log(d.e / d.t)
    return {"k": k, "n": n, "cov": 100 * k / n, "lo": 100 * ci.low, "hi": 100 * ci.high,
            "abslog": float(lr.abs().median()), "bias": float(np.exp(lr.mean()))}


def main(run):
    import json
    t, area, m, b, split = load()
    W = wb_truth(t.index)
    F = wb_features(m)
    T = json.loads((RES / "wb_tables.json").read_text())
    M_exp, B_exp = apply_tables(F, T, m.mass_total / area)
    P = parts(run)
    n_runs = int(P.run_idx.nunique())
    g = P.groupby("project_index")
    est = g.mid.mean()
    A, M, B = g.A.mean(), g.M.mean(), g.B.mean()
    have = est.index
    fit = W.index[~extremes(W)].intersection(have)
    sets = {"all": have, "without extremes": fit}
    const = 414.0
    rows = [("Best constant (414 for every building)", pd.Series(const, index=W.index)),
            ("Model's own estimate only (Step A)", A), ("Mass route only (Step M)", M), ("Benchmark only (Step B)", B),
            ("wb5: 0.2 A + 0.5 M + 0.3 B (as reported)", est)]
    out = [f"# Whole building (A-C): answer-fitted prompt wb5 (`{run}`, {n_runs} run(s), {len(have)} buildings)", "",
           "**In-sample by design**: the mass factors and benchmarks were fitted on the reference values of the same "
           "buildings (all except 13 extreme values). The course reference results are from the course notes "
           "(Gemini, 10 runs, all 292 buildings) and are not in-sample.", "",
           "| Estimator | " + " | ".join(f"{k} ({len(v)})" for k, v in sets.items()) + " | median abs log (all) | bias (all) |",
           "|---|" + "---|" * (len(sets) + 2)]
    for name, e in rows:
        r = {k: cov_ci(e.reindex(i), W.loc[i]) for k, i in sets.items()}
        out.append(f"| {name} | " + " | ".join(f"{v['cov']:.1f}%" for v in r.values()) +
                   f" | {r['all']['abslog']:.3f} | {r['all']['bias']:.2f} |")
    for name, v in COURSE.items():
        out.append(f"| {name} | {v:.1f}% | – | – | – |")
    c = cov_ci(est, W.loc[have])
    out += ["", f"wb5 coverage, all buildings: {c['k']}/{c['n']} = {c['cov']:.1f}% (95% CI {c['lo']:.1f}-{c['hi']:.1f}).",
            "For comparison: a random forest on the 48 features reaches 57.2% (cross-validated) and 86.0% scored on "
            "its own training buildings (analysis/fit_wb_tables.py notes; scratch analysis).", ""]
    Q = P.dropna(subset=["A", "M", "B"]).copy()
    Q["M_exp"], Q["B_exp"] = M_exp.reindex(Q.project_index).values, B_exp.reindex(Q.project_index).values
    comb = 0.2 * Q.A + 0.5 * Q.M + 0.3 * Q.B
    out += ["**Did the model apply the tables?**", "",
            f"- All evidence lines parsed in {100 * P[['A', 'M', 'B']].notna().all(axis=1).mean():.1f}% of answers.",
            f"- M within 5% of mass_total / floor area x F: {100 * ((Q.M / Q.M_exp - 1).abs() < 0.05).mean():.1f}%.",
            f"- B equal to the table value: {100 * ((Q.B - Q.B_exp).abs() < 0.5).mean():.1f}%.",
            f"- Range centred on 0.2 A + 0.5 M + 0.3 B (within 3%): {100 * ((Q.mid - comb).abs() / comb < 0.03).mean():.1f}%."]
    (Path(__file__).resolve().parent / "wb_study.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))
    import make_figures as mf
    mf.fig_bands([("Model's own estimate only (Step A)", A), ("wb5: own estimate + mass route + benchmark", est)],
                 W.loc[have], "fig_bands_wholebuilding", unit="Whole building A–C, kgCO$_2$e/m$^2$")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261116_wholebuilding-wb5")
