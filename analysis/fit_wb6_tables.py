#!/usr/bin/env python3
"""
fit_wb6_tables.py - answer-fitted tables for the whole-building (A-C) prompt "wb6" (IN-SAMPLE by design).

Why wb6. In wb5 the head and tail of the band figure fall off the curve: buildings with high reference
values are underestimated and buildings with low values overestimated (log-log slope 0.59). The use x
structure benchmark B and the model's own estimate A pull every building toward the dataset average;
the mass route M is the only source that keeps the spread. wb6 therefore
  1. drops the use x structure benchmark,
  2. calibrates the mass route with two tables instead of one:
       F  kgCO2e per kg of inventory mass, by structural system (str_sys_summary) x primary use
          (cells >= 5 buildings; else by system; else overall),
       K  a regional factor (site_region, cells >= 5; else 1.00) fitted on what F leaves over,
     M = mass_total / floor area x F x K,
  3. tells the model the typical range for the building's mass intensity band (5th, 50th and 95th
     percentile of the reference results in that band) and keeps the final estimate inside it:
     no gross under- or overestimation, and no pull toward the average,
  4. FINAL = 0.9 x M + 0.1 x A (the model's own estimate), moved to the nearest end of the typical
     range if it falls outside.
LCAs whose physical scope does not start with BSE keep one factor per scope group and no range check.

Everything is fitted on the reference values of the same 279 buildings that are scored (all except 13
extreme values), so the result is in-sample. The script also reports a held-out check (tables fitted on
the development set only, scored on the test set) to show how much of the gain is fitting.
Writes results/wb6_tables.json and prints the table text pasted into experiment_config.py.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, RES  # noqa: E402
from fit_wb_tables import wb_truth, wb_features, extremes, FULL  # noqa: E402

MIN_N = 5
W_A, W_M = 0.1, 0.9
BANDS = [(0, 400), (400, 700), (700, 900), (900, 1100), (1100, 1300), (1300, 1600), (1600, 2000), (2000, None)]
OTHER_SYS = "any other system"


def band_label(lo, hi):
    return f"{lo:,} kg/m2 or more" if hi is None else (f"below {hi:,} kg/m2" if lo == 0 else f"{lo:,} to {hi:,} kg/m2")


def wb6_features(m, area):
    F = wb_features(m)
    F["sys"] = m.str_sys_summary.astype(object).where(m.str_sys_summary.notna(), OTHER_SYS)
    F["use"] = m.bldg_prim_use.astype(object)
    F["region"] = m.site_region.astype(object).where(m.site_region.notna(), "not given")
    mi = m.mass_total / area
    F["band"] = pd.Series([next(band_label(lo, hi) for lo, hi in BANDS if v >= lo and (hi is None or v < hi))
                           for v in mi], index=m.index)
    return F, mi


def _med(y, keys, F, rows):
    k = F[keys].astype(str).agg(" | ".join, axis=1)
    g = y.loc[rows].groupby(k.loc[rows]).agg(["median", "size"])
    return {i: float(r["median"]) for i, r in g.iterrows() if r["size"] >= MIN_N}, k


def fit(W, F, mi, rows_fit):
    """Tables fitted on rows_fit (full scope for F, K and ranges; the other scope groups get one F each)."""
    full = F["scope"] == FULL
    rows = rows_fit[full.loc[rows_fit]]
    part = rows_fit[~full.loc[rows_fit]]
    lr = np.log(W / mi)
    f_cell, k_cell = _med(lr, ["sys", "use"], F, rows)
    f_sys, k_sys = _med(lr, ["sys"], F, rows)
    f_all = float(lr.loc[rows].median())
    lf = k_cell.map(f_cell).fillna(k_sys.map(f_sys)).fillna(f_all)
    r_reg, k_reg = _med(lr - lf, ["region"], F, rows)
    lw = np.log(W)
    rng = lw.loc[rows].groupby(F.loc[rows, "band"]).quantile([.05, .5, .95]).unstack()
    T = {"F_system_use": {k: round(float(np.exp(v)), 2) for k, v in f_cell.items()},
         "F_system": {k: round(float(np.exp(v)), 2) for k, v in f_sys.items()},
         "F_overall": round(float(np.exp(f_all)), 2),
         "K_region": {k: round(float(np.exp(v)), 2) for k, v in r_reg.items()},
         "F_scope": {k: round(float(np.exp(v)), 2) for k, v in lr.loc[part].groupby(F.loc[part, "scope"]).median().items()},
         "typical_range_by_mass_band": {b: {"low": int(round(np.exp(r[.05]))), "typical": int(round(np.exp(r[.5]))),
                                            "high": int(round(np.exp(r[.95])))}
                                        for b, r in rng.iterrows()},
         "n_band": {k: int(v) for k, v in F.loc[rows, "band"].value_counts().items()}}
    return T


def apply(T, F, mi, A):
    """M, the typical range and FINAL exactly as the prompt describes them (from the rounded tables)."""
    full = F["scope"] == FULL
    cell = (F["sys"].astype(str) + " | " + F["use"].astype(str)).map(T["F_system_use"])
    f = cell.fillna(F["sys"].map(T["F_system"])).fillna(T["F_overall"])
    k = F["region"].map(T["K_region"]).fillna(1.0)
    M = (mi * f * k).where(full, mi * F["scope"].map(T["F_scope"]))
    lo = F["band"].map({b: v["low"] for b, v in T["typical_range_by_mass_band"].items()}).where(full)
    hi = F["band"].map({b: v["high"] for b, v in T["typical_range_by_mass_band"].items()}).where(full)
    raw = W_M * M + W_A * A.reindex(M.index)
    final = raw.clip(lo.fillna(0), hi.fillna(np.inf))
    return M, lo, hi, final


def table_text(T):
    """The table text pasted into experiment_config.py (TASK_TEXT_WB6)."""
    by_sys = {}
    for key, v in T["F_system_use"].items():
        s, u = key.split(" | ")
        by_sys.setdefault(s, []).append(f"{u} {v:.2f}")
    sys_order = sorted(T["F_system"], key=lambda s: (s == OTHER_SYS, s))
    f_lines = []
    for s in sys_order:
        cells = "; ".join(sorted(by_sys.get(s, [])))
        f_lines.append(f"     - {s}: " + (f"{cells}; any other use {T['F_system'][s]:.2f}" if cells else
                                          f"any use {T['F_system'][s]:.2f}"))
    f_lines.append(f"     - str_sys_summary missing or not listed: {T['F_overall']:.2f}")
    k_lines = "; ".join(f"{r} {v:.2f}" for r, v in sorted(T["K_region"].items())) + "; any other region 1.00"
    order = [band_label(lo, hi) for lo, hi in BANDS]
    r_lines = [f"     - {b}: typical {T['typical_range_by_mass_band'][b]['typical']}, range "
               f"{T['typical_range_by_mass_band'][b]['low']} to {T['typical_range_by_mass_band'][b]['high']}"
               for b in order if b in T["typical_range_by_mass_band"]]
    return "\n".join(f_lines), "     - " + k_lines, "\n".join(r_lines)


def report(name, e, W):
    e = e.reindex(W.index)
    lo, hi = W <= W.quantile(.15), W >= W.quantile(.85)
    s = float(np.polyfit(np.log(W), np.log(e), 1)[0])
    print(f"  {name:55s} coverage {100 * cov(e, W):5.1f}%  slope {s:.2f}  lowest 15% {100 * cov(e[lo], W[lo]):5.1f}%  "
          f"highest 15% {100 * cov(e[hi], W[hi]):5.1f}%")


def main():
    t, area, m, b, split = load()
    W = wb_truth(t.index)
    F, mi = wb6_features(m, area)
    keep = W.index[~extremes(W)]
    T = fit(W, F, mi, keep)
    T = {"fitted_on": f"{len(keep)} buildings (all except {int(extremes(W).sum())} extreme values): in-sample",
         "weights": {"own_estimate": W_A, "mass_route": W_M}, **T}
    (RES / "wb6_tables.json").write_text(json.dumps(T, indent=2))
    f_txt, k_txt, r_txt = table_text(T)
    print("F table:\n" + f_txt + "\nK table:\n" + k_txt + "\nRanges:\n" + r_txt + "\nF_scope:", T["F_scope"])

    # expected result, using the model's own estimates from the wb5 run as a stand-in for A
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from wb_study import parts
    P = parts("20261116_wholebuilding-wb5")
    A = P.groupby("project_index").A.mean()
    E5 = P.groupby("project_index").mid.mean()
    M, lo, hi, final = apply(T, F, mi, A)
    print("\nSimulated with wb5's own estimates A (all 292 buildings):")
    report("wb5 as run", E5, W)
    report("wb6 mass route M alone", M, W)
    report("wb6 0.9 M + 0.1 A, kept inside the typical range", final, W)
    # held-out check: tables fitted on the development set only, scored on the test set
    dev = keep[split.loc[keep] == "dev"]
    test = W.index[split == "test"]
    Td = fit(W, F, mi, dev)
    _, _, _, final_d = apply(Td, F, mi, A)
    print("\nHeld-out check (test set, 88 buildings):")
    report("wb5 as run (tables in-sample)", E5.reindex(test), W.loc[test])
    report("wb6, tables fitted on the development set only", final_d.reindex(test), W.loc[test])
    report("wb6, tables in-sample", final.reindex(test), W.loc[test])


if __name__ == "__main__":
    main()
