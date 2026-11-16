#!/usr/bin/env python3
"""
ceiling.py - how much +/-20% coverage can the 48 features support at all?

Three reference points for the enclosure A1-A3 target (and the constant for the course's
whole-building A-C target, for comparison):
  constant     the same value for every building (the best constant, and the median)
  ML, CV       random forest / gradient boosting on all 48 features, 5-fold cross-validated
               (repeated): what a model trained on this very dataset can predict for unseen buildings
  ML, in-sample   the same forest scored on its own training buildings: memorisation, not prediction

Writes analysis/ceiling.md.
"""
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import KFold

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, design_matrix, RES  # noqa: E402
from outliers import flags  # noqa: E402


def best_constant(x):
    grid = np.exp(np.linspace(np.log(x.quantile(.05)), np.log(x.quantile(.95)), 400))
    c = [cov(pd.Series(e, index=x.index), x) for e in grid]
    return float(grid[int(np.argmax(c))]), float(max(c))


def cv_pred(fn, X, y, idx, reps=5):
    p = pd.Series(0.0, index=idx)
    for r in range(reps):
        for tr, te in KFold(5, shuffle=True, random_state=r).split(idx):
            p.loc[idx[te]] += fn(r).fit(X.loc[idx[tr]], y.loc[idx[tr]]).predict(X.loc[idx[te]]) / reps
    return np.exp(p)


def main():
    t, area, m, b, split = load()
    f, _ = flags()
    X = design_matrix(m, area)
    y = np.log(t)
    ta = pd.read_csv(RES / "ground_truth_TA_wholebuilding_A-C.csv")
    ta = pd.Series(ta["ECI_true_kgCO2e_m2"].values, index=ta["Project Name"].str.extract(r"(\d+)")[0].astype(int))
    rf = lambda r: RandomForestRegressor(400, min_samples_leaf=3, random_state=r)
    gb = lambda r: GradientBoostingRegressor(n_estimators=150, max_depth=3, learning_rate=0.05, subsample=0.8, random_state=r)
    out = ["# What coverage can the features support?", "",
           "Coverage = share of buildings whose reference value lies within the estimate +/-20%.", "",
           "| Target | Buildings | sd of log value | Median as constant | Best constant |", "|---|---|---|---|---|"]
    for name, x in [("Whole building A-C (course reference task)", ta), ("Enclosure A1-A3, all", t),
                    ("Enclosure A1-A3, cleaned", t[~f.outlier])]:
        e, c = best_constant(x)
        out.append(f"| {name} | {len(x)} | {np.log(x).std():.2f} | "
                   f"{100 * cov(pd.Series(x.median(), index=x.index), x):.1f}% | {100 * c:.1f}% (at {e:.0f}) |")
    out += ["", "| Enclosure A1-A3 | Buildings | Random forest, CV | Gradient boosting, CV | Random forest, in-sample |",
            "|---|---|---|---|---|"]
    for name, idx in [("all", t.index), ("cleaned", t.index[~f.outlier])]:
        p_rf, p_gb = cv_pred(rf, X, y, idx), cv_pred(gb, X, y, idx)
        ins = np.exp(pd.Series(rf(0).fit(X.loc[idx], y.loc[idx]).predict(X.loc[idx]), index=idx))
        out.append(f"| {name} | {len(idx)} | {100 * cov(p_rf, t.loc[idx]):.1f}% | {100 * cov(p_gb, t.loc[idx]):.1f}% | "
                   f"{100 * cov(ins, t.loc[idx]):.1f}% |")
    out += ["", "Reading: a model trained on this dataset itself, with all 48 features, predicts unseen buildings "
            "only a few points better than one constant. Coverage far above that on these buildings can only come "
            "from fitting the same buildings that are scored (the in-sample column)."]
    (Path(__file__).resolve().parent / "ceiling.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
