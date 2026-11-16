#!/usr/bin/env python3
"""
v4_study.py - results of prompt v4 (weighted evidence) against v1, v3 and a constant.

Reports, for all buildings and for the cleaned set (analysis/outliers.py), on all / dev / test:
  coverage (+/-20%), median |log error|, bias (geometric mean est/ref), RMSE;
  the two sources of evidence inside v4 (bottom-up A, benchmark B) and whether the model combined
  them as instructed; paired tests v4 vs v3; a weight sensitivity using v4's own A and B.

Usage:  python analysis/v4_study.py [v4 run name]
Writes analysis/v4_study.md and analysis/figures/v4_study.png.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, RES  # noqa: E402
from feature_study import estimates  # noqa: E402
from outliers import flags  # noqa: E402

RUNS = {"v1": "20261104_baseline-innate", "v3": "20261104_prompt-v3"}
DELTA = 0.2


def parts(run):
    """Per-building means of the v4 evidence lines (bottom_up, benchmark) and the range midpoint."""
    rows = []
    for fcsv in (RES / run).glob("project-*_runs.csv"):
        df = pd.read_csv(fcsv)
        df = df[df["parse_ok"].astype(str) == "True"]
        p = int(re.search(r"project-(\d+)_", fcsv.name).group(1))
        for _, r in df.iterrows():
            rows.append({"project_index": p, "run_idx": r["run_idx"], "mid": r["mid"],
                         "A": pd.to_numeric(r.get("bottom_up"), errors="coerce"),
                         "B": pd.to_numeric(r.get("benchmark"), errors="coerce")})
    return pd.DataFrame(rows)


def metrics(e, t):
    d = pd.DataFrame({"e": e, "t": t}).dropna()
    lr = np.log(d.e / d.t)
    k, n = int(((d.t >= d.e * (1 - DELTA)) & (d.t <= d.e * (1 + DELTA))).sum()), len(d)
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    return {"n": n, "cov": 100 * k / n, "lo": 100 * ci.low, "hi": 100 * ci.high, "abslog": float(lr.abs().median()),
            "bias": float(np.exp(lr.mean())), "rmse": float(np.sqrt(((d.e - d.t) ** 2).mean()))}


def paired(ea, eb, t, idx):
    a = (t.loc[idx] >= ea.loc[idx] * .8) & (t.loc[idx] <= ea.loc[idx] * 1.2)
    b = (t.loc[idx] >= eb.loc[idx] * .8) & (t.loc[idx] <= eb.loc[idx] * 1.2)
    oa, ob = int((a & ~b).sum()), int((~a & b).sum())
    p_mc = stats.binomtest(min(oa, ob), oa + ob).pvalue if oa + ob else 1.0
    la, lb = np.log(ea.loc[idx] / t.loc[idx]).abs(), np.log(eb.loc[idx] / t.loc[idx]).abs()
    return p_mc, float(stats.wilcoxon(la, lb).pvalue), 100 * float((lb < la).mean())


def main(run):
    t, area, m, b, split = load()
    f, _ = flags()
    est = {k: estimates(v) for k, v in RUNS.items()}
    est["v4"] = estimates(run)
    have = est["v4"].index
    P = parts(run)
    n_runs = int(P.run_idx.nunique())
    A, B = P.groupby("project_index").A.mean(), P.groupby("project_index").B.mean()
    dev_all = t.index[(split == "dev")].intersection(have)
    const = float(np.exp(np.log(t.loc[t.index[(split == "dev") & ~f.outlier]]).median()))
    est["constant"] = pd.Series(const, index=t.index)
    sets = {"all": have, "all, dev": dev_all, "all, test": t.index[split == "test"].intersection(have),
            "cleaned": t.index[~f.outlier].intersection(have),
            "cleaned, dev": t.index[~f.outlier & (split == "dev")].intersection(have),
            "cleaned, test": t.index[~f.outlier & (split == "test")].intersection(have)}
    out = [f"# Prompt v4 (weighted evidence): results (`{run}`, {n_runs} run(s), {len(have)} buildings answered)", "",
           f"Constant = {const:.0f} kgCO2e/m2 for every building (median of the cleaned development set).", ""]
    for metric, lab, fmt in [("cov", "Coverage (+/-20%), %", "{:.1f}"), ("abslog", "Median abs log error", "{:.3f}"),
                             ("bias", "Bias (geometric mean est/ref)", "{:.2f}"), ("rmse", "RMSE, kgCO2e/m2", "{:.1f}")]:
        out += [f"**{lab}**", "", "| Estimator | " + " | ".join(f"{k} ({len(v)})" for k, v in sets.items()) + " |",
                "|---|" + "---|" * len(sets)]
        for name in ["constant", "v1", "v3", "v4"]:
            out.append(f"| {name} | " + " | ".join(fmt.format(metrics(est[name].loc[i], t.loc[i])[metric]) for i in sets.values()) + " |")
        out.append("")
    ci = {k: metrics(est["v4"].loc[i], t.loc[i]) for k, i in sets.items()}
    out += ["v4 coverage with Wilson 95% CI: " + "; ".join(f"{k} {v['cov']:.1f}% ({v['lo']:.1f}-{v['hi']:.1f})" for k, v in ci.items()) + ".", ""]

    out += ["**Paired tests against v4**", "", "| Set | Baseline | McNemar p (coverage) | Wilcoxon p (abs log) | v4 closer, % of buildings |", "|---|---|---|---|---|"]
    for k in ["all", "cleaned", "all, test", "cleaned, test"]:
        for base in ["v3", "v1", "constant"]:
            pm, pw, closer = paired(est[base], est["v4"], t, sets[k])
            out.append(f"| {k} | {base} | {pm:.3g} | {pw:.3g} | {closer:.1f} |")
    out.append("")

    # the two sources inside v4
    ok = A.notna() & B.notna()
    comb = (0.5 * P.A + 0.5 * P.B)
    follow = ((P.mid - comb).abs() / comb < 0.03)[P.A.notna() & P.B.notna()]
    oos = f.out_of_scope.reindex(P.project_index).values
    rule = ((P.A == 8) & (P.B == 8))
    out += ["**Inside v4**", "",
            f"- Evidence lines parsed in {100 * (P.A.notna() & P.B.notna()).mean():.1f}% of answers.",
            f"- Reported range centred on 0.5 A + 0.5 B (within 3%) in {100 * follow.mean():.1f}% of those answers.",
            f"- Out-of-scope rule applied in {int(rule.sum())} answers; {int((rule & oos).sum())} of them are buildings whose "
            f"`lca_phys_scope` has no E ({int(oos.sum())} such answers in total).", "",
            "| Source (mean of runs) | " + " | ".join(sets) + " |", "|---|" + "---|" * len(sets)]
    src = {"A bottom-up only": A, "B benchmark only": B, "0.5 A + 0.5 B recomputed": 0.5 * A + 0.5 * B, "v4 as reported": est["v4"]}
    for name, e in src.items():
        out.append(f"| {name} | " + " | ".join(f"{metrics(e.reindex(i), t.loc[i])['cov']:.1f}" for i in sets.values()) + " |")
    out += ["", "**Weight sensitivity with v4's own A and B** (coverage %, estimate = w A + (1 - w) B)", "",
            "| w on bottom-up | " + " | ".join(sets) + " |", "|---|" + "---|" * len(sets)]
    for w in [0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
        e = w * A + (1 - w) * B
        out.append(f"| {w:.1f} | " + " | ".join(f"{metrics(e.reindex(i), t.loc[i])['cov']:.1f}" for i in sets.values()) + " |")
    if n_runs > 1:
        cvs = P.groupby("project_index").mid.agg(lambda x: x.std(ddof=1) / x.mean() if len(x) > 1 else np.nan)
        single = [metrics(P[P.run_idx == r].set_index("project_index").mid.reindex(sets["all"]), t.loc[sets["all"]])["cov"]
                  for r in sorted(P.run_idx.unique())]
        out += ["", f"Run-to-run CV of v4: {100 * cvs.mean():.1f}%. Coverage of single runs (all): "
                + ", ".join(f"{c:.1f}%" for c in single) + "."]
    (Path(__file__).resolve().parent / "v4_study.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261116_prompt-v4")
