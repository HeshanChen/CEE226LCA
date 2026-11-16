#!/usr/bin/env python3
"""
weight_search.py - how much weight should each source of evidence get?

Sources of evidence for one building's enclosure A1-A3 (kgCO2e per m2 floor):
  A  bottom-up   the LLM's own component take-off (areas x assemblies x intensities)
  B  use benchmark   median of the reference LCAs of buildings with the same primary use
  G  geometry benchmark   one intensity per m2 of envelope x envelope/floor ratio
Final estimate = k * (wA*A + wB*B + wG*G).

Everything is fitted on the cleaned development set (analysis/outliers.py, results/split.csv):
benchmarks and weights never see the test buildings. Weights are scored by repeated 5-fold
cross-validation inside the development set, then the chosen weights are applied once to the test set.

Usage:  python analysis/weight_search.py [bottom-up run, default 20261104_prompt-v3]
Writes analysis/weight_search.md and results/benchmarks_dev.json (the numbers quoted in prompt v4).
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, RES  # noqa: E402
from feature_study import estimates  # noqa: E402
from outliers import flags  # noqa: E402

MIN_N = 5          # a use needs at least this many development buildings to get its own benchmark
REPS = 4


def fit_parts(t, m, area, tr):
    """Benchmarks from the training buildings only."""
    lt = np.log(t.loc[tr])
    g = lt.groupby(m.bldg_prim_use.loc[tr]).agg(["median", "size"])
    overall = float(np.exp(lt.median()))
    use_bm = {u: float(np.exp(r["median"])) for u, r in g.iterrows() if r["size"] >= MIN_N}
    er = m.bldg_therm_env_area / area
    known = [i for i in tr if not np.isnan(er.loc[i])]
    c_env = float(np.exp(np.median(np.log(t.loc[known] / er.loc[known]))))
    er_by_storeys = er.loc[tr].groupby(m.bldg_stories_above.loc[tr]).median()
    return {"use": use_bm, "overall": overall, "c_env": c_env, "er_by_storeys": er_by_storeys,
            "er_overall": float(er.loc[tr].median())}


def sources(parts, m, area, A):
    B = m.bldg_prim_use.map(parts["use"]).fillna(parts["overall"])
    er = (m.bldg_therm_env_area / area)
    er = er.fillna(m.bldg_stories_above.map(parts["er_by_storeys"])).fillna(parts["er_overall"])
    return A, B, parts["c_env"] * er


def main(run):
    t, area, m, b, split = load()
    f, _ = flags()
    A_all = estimates(run)
    dev = t.index[(split == "dev") & ~f.outlier]
    test = t.index[(split == "test") & ~f.outlier]

    def blend(w, k, tr, te):
        A, B, G = sources(fit_parts(t, m, area, tr), m, area, A_all)
        return (k * (w[0] * A + w[1] * B + w[2] * G)).loc[te]

    def cv(w, k):
        p = pd.Series(0.0, index=dev)
        for r in range(REPS):
            for tr, te in KFold(5, shuffle=True, random_state=r).split(dev):
                p.loc[dev[te]] += blend(w, k, dev[tr], dev[te]) / REPS
        return p

    rows = []
    grid = [(a / 10, bb / 10, (10 - a - bb) / 10) for a in range(11) for bb in range(11 - a)]
    for w in grid:
        for k in (1.0, 1.05, 1.1):
            p = cv(w, k)
            rows.append({"wA bottom-up": w[0], "wB use benchmark": w[1], "wG geometry": w[2], "k": k,
                         "dev CV coverage %": 100 * cov(p, t.loc[dev]),
                         "dev CV median |log err|": float(np.log(p / t.loc[dev]).abs().median()),
                         "test coverage %": 100 * cov(blend(w, k, dev, test), t.loc[test])})
    R = pd.DataFrame(rows)
    R["score"] = R["dev CV coverage %"] / 100 - 0.15 * R["dev CV median |log err|"]

    def pick(mask):
        return R[mask].sort_values("score", ascending=False).iloc[0]

    def fmt(r):
        return (f"| {r['wA bottom-up']:.1f} | {r['wB use benchmark']:.1f} | {r['wG geometry']:.1f} | {r['k']:.2f} | "
                f"{r['dev CV coverage %']:.1f} | {r['dev CV median |log err|']:.3f} | {r['test coverage %']:.1f} |")

    head = ["| wA bottom-up | wB use benchmark | wG geometry | k | dev CV coverage % | dev CV median abs log err | test coverage % |",
            "|---|---|---|---|---|---|---|"]
    single = [pick((R["wA bottom-up"] == 1)), pick((R["wB use benchmark"] == 1)), pick((R["wG geometry"] == 1))]
    two = R[R["wG geometry"] == 0].sort_values("score", ascending=False).head(8)
    three = R[R["wG geometry"] > 0].sort_values("score", ascending=False).head(5)
    chosen = R[(R["wA bottom-up"] == 0.5) & (R["wB use benchmark"] == 0.5) & (R["k"] == 1.0)].iloc[0]
    out = [f"# Evidence-weight search (bottom-up run: `{run}`)", "",
           f"Cleaned development set: {len(dev)} buildings; cleaned test set: {len(test)}. "
           "Score used to rank = dev CV coverage - 0.15 x dev CV median abs log error. "
           "The test column is shown for information; it was not used to choose weights.", "",
           "## Round 1: one source at a time", "", *head, *[fmt(r) for r in single], "",
           "## Round 2: bottom-up + use benchmark (best 8 of 33)", "", *head, *[fmt(r) for _, r in two.iterrows()], "",
           "## Round 3: adding the geometry benchmark (best 5)", "", *head, *[fmt(r) for _, r in three.iterrows()], "",
           "## Chosen for prompt v4", "", *head, fmt(chosen), "",
           "Equal weights on the bottom-up estimate and the use benchmark, no extra factor. Coverage is flat for "
           "bottom-up weights between 0.3 and 0.6, so the choice within that range is not critical; the geometry "
           "benchmark adds nothing."]
    (Path(__file__).resolve().parent / "weight_search.md").write_text("\n".join(out) + "\n")
    R.to_csv(Path(__file__).resolve().parent / "weight_search.csv", index=False)

    parts = fit_parts(t, m, area, dev)
    n_use = m.bldg_prim_use.loc[dev].value_counts()
    all_dev = t.index[split == "dev"]
    oos = t.loc[[i for i in all_dev if f.out_of_scope.loc[i]]]
    rel = np.log(t / m.bldg_prim_use.map(parts["use"]).fillna(parts["overall"]))
    bench = {"fitted_on": f"{len(dev)} cleaned development buildings", "overall_median": round(parts["overall"]),
             "use_median": {u: round(v) for u, v in sorted(parts["use"].items(), key=lambda x: -n_use[x[0]])},
             "use_n": {u: int(n_use[u]) for u in parts["use"]},
             "minor_renovation_factor": round(float(np.exp(rel.loc[[i for i in dev if m.bldg_proj_type.loc[i] == 'Minor Renovation']].median())), 2),
             "out_of_scope_median": round(float(oos.median()), 1), "out_of_scope_n": int(len(oos)),
             "env_ratio_by_storeys": {k: round(float(v), 2) for k, v in parts["er_by_storeys"].items()},
             "c_env_kgCO2e_per_m2_envelope": round(parts["c_env"])}
    (RES / "benchmarks_dev.json").write_text(json.dumps(bench, indent=2))
    print("\n".join(out))
    print(json.dumps(bench, indent=2))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "20261104_prompt-v3")
