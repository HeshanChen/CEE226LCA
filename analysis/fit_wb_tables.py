#!/usr/bin/env python3
"""
fit_wb_tables.py - answer-fitted tables for the whole-building (A-C) prompt "wb5" (IN-SAMPLE by design).

Target: the course's whole-building A-C ECI (results/ground_truth_TA_wholebuilding_A-C.csv).
Fitted on all buildings except the extreme values (Tukey's fences on the log value):
  F  embodied carbon per kg of inventory mass, median(ECI / (mass_total / floor area)): for LCAs whose
     physical scope covers substructure, structure and enclosure, by structural material; for the other
     scope groups, one value per group
  B  benchmark, median ECI: for full-scope LCAs by primary use x structural material (cells >= 5; else by
     use; else overall); for the other scope groups, one value per group
wb5 estimate = 0.2 x A (the model's own estimate) + 0.5 x M + 0.3 x B, with M = mass_total / floor area x F.
The weights were chosen with a simulated noisy take-off, because no LLM whole-building estimates existed yet.

mass_total is the total inventory mass of the reference LCA itself (stages A-C), so it is not known at
early design; it is one of the 48 features the course provides. Writes results/wb_tables.json.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, RES  # noqa: E402
from fit_v5_tables import features, cell_table  # noqa: E402

MIN_N = 5
W_A, W_M, W_B = 0.2, 0.5, 0.3


def wb_truth(index):
    ta = pd.read_csv(RES / "ground_truth_TA_wholebuilding_A-C.csv")
    return pd.Series(ta["ECI_true_kgCO2e_m2"].values,
                     index=ta["Project Name"].str.extract(r"(\d+)")[0].astype(int)).reindex(index)


def wb_features(m):
    F = features(m)
    sc = m.lca_phys_scope.fillna("").map(str)
    F["scope"] = np.select([sc.str.startswith("BSE"), sc.str.contains("S")],
                           ["substructure, structure and enclosure", "structure without substructure"],
                           "no structure")
    return F


def extremes(W):
    lw = np.log(W)
    q1, q3 = lw.quantile(.25), lw.quantile(.75)
    return (lw < q1 - 1.5 * (q3 - q1)) | (lw > q3 + 1.5 * (q3 - q1))


FULL = "substructure, structure and enclosure"


def apply_tables(F, T, mi):
    """F factor and benchmark B per building, exactly as the prompt describes them."""
    full = F["scope"] == FULL
    Fk = F["struct"].map(T["F_structure"]).fillna(T["F_overall"]).where(full, F["scope"].map(T["F_scope"]))
    B = lookup(F, T["B_use_structure"], ["use", "struct"], "use", T["B_use"], T["B_overall"]).where(
        full, F["scope"].map(T["B_scope"]))
    return mi * Fk, B


def lookup(F, tab, keys, fb_key, fb_tab, overall):
    key = F[keys[0]].map(str)
    for k in keys[1:]:
        key = key + " | " + F[k].map(str)
    return key.map(tab).fillna(F[fb_key].map(fb_tab)).fillna(overall)


def tables():
    t, area, m, b, split = load()
    W = wb_truth(t.index)
    F = wb_features(m)
    fit = W.index[~extremes(W)]
    mi = m.mass_total / area
    lf, lw = np.log(W / mi), np.log(W)
    full = fit[F.loc[fit, "scope"] == FULL]
    part = fit[F.loc[fit, "scope"] != FULL]
    T = {"fitted_on": f"{len(fit)} buildings (all except {int(extremes(W).sum())} extreme values): in-sample",
         "weights": {"own_estimate": W_A, "mass_route": W_M, "benchmark": W_B},
         "F_structure": {k: round(v, 2) for k, v in cell_table(lf, F, ["struct"], full).items()},
         "F_overall": round(float(np.exp(lf.loc[full].median())), 2),
         "F_scope": {k: round(float(np.exp(v)), 2) for k, v in lf.loc[part].groupby(F.loc[part, "scope"]).median().items()},
         "B_use_structure": {k: round(v) for k, v in cell_table(lw, F, ["use", "struct"], full).items()},
         "B_use": {k: round(v) for k, v in cell_table(lw, F, ["use"], full).items()},
         "B_overall": round(float(np.exp(lw.loc[full].median()))),
         "B_scope": {k: round(float(np.exp(v))) for k, v in lw.loc[part].groupby(F.loc[part, "scope"]).median().items()},
         "n_scope": {k: int(v) for k, v in F.loc[fit, "scope"].value_counts().items()}}
    return T, W, F, mi, fit


def main():
    T, W, F, mi, fit = tables()
    M, B = apply_tables(F, T, mi)
    e = (W_M * M + W_B * B) / (W_M + W_B)
    print(f"without the model's own estimate (M and B only, renormalised): all {100 * cov(e, W):.1f}% | "
          f"fit set {100 * cov(e.loc[fit], W.loc[fit]):.1f}%;  M alone {100 * cov(M, W):.1f}%;  B alone {100 * cov(B, W):.1f}%")
    (RES / "wb_tables.json").write_text(json.dumps(T, indent=2))
    print(json.dumps(T, indent=1))


if __name__ == "__main__":
    main()
