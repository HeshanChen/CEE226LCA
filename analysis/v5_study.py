#!/usr/bin/env python3
"""
v5_study.py - results of prompt v5 (answer-fitted, IN-SAMPLE by design) against v1, v3, v4 and a constant.

v5's tables were fitted on the reference values of all 262 cleaned buildings, so every v5 number here is
in-sample, including the "test" columns. v4 (benchmark fitted on the development set only) remains the
held-out result.

Also checks whether the model applied the tables: K = CALIBRATED / BOTTOM_UP against the K table,
B against the benchmark table, and the range centred on 0.5 x CALIBRATED + 0.5 x B.

Usage:  python analysis/v5_study.py [v5 run name]
Writes analysis/v5_study.md.
"""
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, RES  # noqa: E402
from feature_study import estimates  # noqa: E402
from fit_v5_tables import features, apply  # noqa: E402
from outliers import flags  # noqa: E402

RUNS = {"v1": "20261104_baseline-innate", "v3": "20261104_prompt-v3", "v4": "20261116_prompt-v4"}


def parts(run):
    rows = []
    for fcsv in (RES / run).glob("project-*_runs.csv"):
        df = pd.read_csv(fcsv)
        df = df[df["parse_ok"].astype(str) == "True"]
        p = int(re.search(r"project-(\d+)_", fcsv.name).group(1))
        for _, r in df.iterrows():
            rows.append({"project_index": p, "run_idx": r["run_idx"], "mid": r["mid"],
                         "A": pd.to_numeric(r.get("bottom_up"), errors="coerce"),
                         "C": pd.to_numeric(r.get("calibrated"), errors="coerce"),
                         "B": pd.to_numeric(r.get("benchmark"), errors="coerce")})
    return pd.DataFrame(rows)


def metrics(e, t):
    d = pd.DataFrame({"e": e, "t": t}).dropna()
    lr = np.log(d.e / d.t)
    k, n = int(((d.t >= d.e * .8) & (d.t <= d.e * 1.2)).sum()), len(d)
    ci = stats.binomtest(k, n).proportion_ci(0.95, method="wilson")
    return {"n": n, "cov": 100 * k / n, "lo": 100 * ci.low, "hi": 100 * ci.high, "abslog": float(lr.abs().median()),
            "bias": float(np.exp(lr.mean())), "rmse": float(np.sqrt(((d.e - d.t) ** 2).mean())),
            "slope": float(np.polyfit(np.log(d.t), np.log(d.e), 1)[0])}


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
    F = features(m)
    T = json.loads((RES / "v5_tables.json").read_text())
    K_exp = apply(F, T["K_use_envelope_area"], ["use", "env"], ["use"], T["K_use"], T["K_overall"])
    B_exp = apply(F, T["B_use_storeys"], ["use", "storeys"], ["use"], T["B_use"], T["B_overall"])
    P = parts(run)
    have = sorted(P.project_index.unique())
    n_runs = int(P.run_idx.nunique())
    est = {k: estimates(v).reindex(t.index) for k, v in RUNS.items()}
    est["v5"] = estimates(run).reindex(t.index)
    cl = t.index[~f.outlier]
    const = float(np.exp(np.log(t.loc[cl]).median()))
    est["constant"] = pd.Series(const, index=t.index)
    sets = {"all": pd.Index(have), "cleaned": cl.intersection(have),
            "all, test": t.index[split == "test"].intersection(have),
            "cleaned, test": cl[split.loc[cl] == "test"].intersection(have)}
    out = [f"# Prompt v5 (answer-fitted): results (`{run}`, {n_runs} run(s), {len(have)} buildings answered)", "",
           "**In-sample by design.** v5's calibration factors and benchmarks were fitted on the reference values of all "
           "262 cleaned buildings, so every v5 number below is in-sample, including the test columns. "
           f"Constant = {const:.0f} kgCO2e/m2 (median of the cleaned set).", ""]
    for metric, lab, fmt in [("cov", "Coverage (+/-20%), %", "{:.1f}"), ("abslog", "Median abs log error", "{:.3f}"),
                             ("bias", "Bias (geometric mean est/ref)", "{:.2f}"), ("rmse", "RMSE, kgCO2e/m2", "{:.1f}"),
                             ("slope", "Log-log slope (1 = no compression)", "{:.2f}")]:
        out += [f"**{lab}**", "", "| Estimator | " + " | ".join(f"{k} ({len(v)})" for k, v in sets.items()) + " |",
                "|---|" + "---|" * len(sets)]
        for name in ["constant", "v1", "v3", "v4", "v5"]:
            out.append(f"| {name} | " + " | ".join(fmt.format(metrics(est[name].loc[i], t.loc[i])[metric]) for i in sets.values()) + " |")
        out.append("")
    ci = {k: metrics(est["v5"].loc[i], t.loc[i]) for k, i in sets.items()}
    out += ["v5 coverage with Wilson 95% CI: " + "; ".join(f"{k} {v['cov']:.1f}% ({v['lo']:.1f}-{v['hi']:.1f})" for k, v in ci.items()) + ".", ""]
    out += ["**Paired tests against v5**", "", "| Set | Baseline | McNemar p (coverage) | Wilcoxon p (abs log) | v5 closer, % |", "|---|---|---|---|---|"]
    for k in ["all", "cleaned"]:
        for base in ["v4", "v3", "constant"]:
            pm, pw, closer = paired(est[base], est["v5"], t, sets[k])
            out.append(f"| {k} | {base} | {pm:.3g} | {pw:.3g} | {closer:.1f} |")
    out.append("")

    # did the model apply the tables?
    Q = P.dropna(subset=["A", "C", "B"]).copy()
    Q = Q[~f.out_of_scope.reindex(Q.project_index).values]
    Q["K_used"] = Q.C / Q.A
    Q["K_exp"] = K_exp.reindex(Q.project_index).values
    Q["B_exp"] = B_exp.reindex(Q.project_index).values
    comb = 0.5 * Q.C + 0.5 * Q.B
    oos = f.out_of_scope.reindex(P.project_index).values
    rule = (P.A == 8) & (P.B == 8)
    out += ["**Did the model apply the tables?** (answers for in-scope buildings)", "",
            f"- All four evidence lines parsed in {100 * P[['A', 'C', 'B']].notna().all(axis=1).mean():.1f}% of answers.",
            f"- K used within 3% of the table value: {100 * ((Q.K_used / Q.K_exp - 1).abs() < 0.03).mean():.1f}%.",
            f"- B equal to the table value: {100 * ((Q.B - Q.B_exp).abs() < 0.5).mean():.1f}%.",
            f"- Range centred on 0.5 x CALIBRATED + 0.5 x B (within 3%): {100 * ((Q.mid - comb).abs() / comb < 0.03).mean():.1f}%.",
            f"- Out-of-scope rule applied in {int(rule.sum())} answers, {int((rule & oos).sum())} of them correctly "
            f"({int(oos.sum())} out-of-scope answers in total).", ""]
    A = P.groupby("project_index").A.mean()
    exact = (0.5 * K_exp.reindex(A.index) * A + 0.5 * B_exp.reindex(A.index)).where(~f.out_of_scope.reindex(A.index), 8.0)
    out += ["| Source (mean of runs) | " + " | ".join(sets) + " |", "|---|" + "---|" * len(sets)]
    src = {"A bottom-up only": A, "K x A calibrated only": P.groupby("project_index").C.mean(),
           "B benchmark only": P.groupby("project_index").B.mean(), "tables applied exactly to v5's own A": exact,
           "v5 as reported": est["v5"]}
    for name, e in src.items():
        out.append(f"| {name} | " + " | ".join(f"{metrics(e.reindex(i), t.loc[i])['cov']:.1f}" for i in sets.values()) + " |")
    if n_runs > 1:
        cvs = P.groupby("project_index").mid.agg(lambda x: x.std(ddof=1) / x.mean() if len(x) > 1 else np.nan)
        single = [metrics(P[P.run_idx == r].set_index("project_index").mid.reindex(sets["all"]), t.loc[sets["all"]])["cov"]
                  for r in sorted(P.run_idx.unique())]
        out += ["", f"Run-to-run CV of v5: {100 * cvs.mean():.1f}%. Coverage of single runs (all): "
                + ", ".join(f"{c:.1f}%" for c in single) + "."]
    bins = [(0, 25), (25, 50), (50, 100), (100, 200), (200, 1e9)]
    out += ["", "**Median estimate/reference by reference bin**", "", "| Bin | n | v3 | v4 | v5 |", "|---|---|---|---|---|"]
    for lo, hi in bins:
        ix = t.index[(t >= lo) & (t < hi)].intersection(have)
        out.append(f"| {lo}-{'' if hi > 1e8 else int(hi)} | {len(ix)} | " +
                   " | ".join(f"{float(np.median(est[k].loc[ix] / t.loc[ix])):.2f}" for k in ["v3", "v4", "v5"]) + " |")
    (Path(__file__).resolve().parent / "v5_study.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261116_prompt-v5")
