#!/usr/bin/env python3
"""
outliers.py - rule-based outlier flags for the 292 reference values.

The rules use only the reference LCA and the building features, never an LLM estimate, so the
cleaned set does not depend on which buildings a prompt happens to get right.

  R1 incomplete      new construction with no fenestration GWP at all (flag_incomplete)
  R2 out_of_scope    the reference LCA's physical scope (lca_phys_scope) does not include the
                     Enclosure ("E"): its enclosure total is incidental, not a modelled enclosure
  R3 extreme         log(enclosure A1-A3 per m2) outside Tukey's fences (Q1 - 1.5 IQR, Q3 + 1.5 IQR)

Writes results/outliers.csv and analysis/outliers.md.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, RES  # noqa: E402


def flags():
    t, area, m, b, split = load()
    lt = np.log(t)
    q1, q3 = lt.quantile(.25), lt.quantile(.75)
    lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
    f = pd.DataFrame({
        "ECI_true_kgCO2e_m2": t, "bldg_proj_type": m.bldg_proj_type, "lca_phys_scope": m.lca_phys_scope,
        "incomplete": b.flag_incomplete.astype(bool),
        "out_of_scope": ~m.lca_phys_scope.astype(str).str.contains("E"),
        "extreme": (lt < lo) | (lt > hi), "split": split})
    f["outlier"] = f[["incomplete", "out_of_scope", "extreme"]].any(axis=1)
    return f, (float(np.exp(lo)), float(np.exp(hi)))


def main():
    f, (lo, hi) = flags()
    f.to_csv(RES / "outliers.csv")
    o = f[f.outlier]
    out = ["# Outlier rules", "",
           "Rules use only the reference LCA and the features, never an LLM estimate.", "",
           "| Rule | Definition | Buildings |", "|---|---|---|",
           f"| R1 incomplete | new construction with no fenestration GWP | {int(f.incomplete.sum())} |",
           f"| R2 out of scope | `lca_phys_scope` has no Enclosure (E) | {int(f.out_of_scope.sum())} |",
           f"| R3 extreme | log value outside Tukey's fences ({lo:.1f} to {hi:.0f} kgCO2e/m2) | {int(f.extreme.sum())} |",
           f"| Any rule | | **{len(o)}** ({100 * len(o) / len(f):.1f}%) |", "",
           f"Cleaned set: {int((~f.outlier).sum())} buildings "
           f"(dev {int(((~f.outlier) & (f.split == 'dev')).sum())}, test {int(((~f.outlier) & (f.split == 'test')).sum())}).", "",
           "Outliers by project type: " + ", ".join(f"{k} {v}" for k, v in o.bldg_proj_type.value_counts().items()) + ".", "",
           "| project | value | type | scope | incomplete | out of scope | extreme |", "|---|---|---|---|---|---|---|"]
    for p, r in o.sort_values("ECI_true_kgCO2e_m2").iterrows():
        out.append(f"| {p} | {r.ECI_true_kgCO2e_m2:.1f} | {r.bldg_proj_type} | {r.lca_phys_scope} | "
                   f"{'x' if r.incomplete else ''} | {'x' if r.out_of_scope else ''} | {'x' if r.extreme else ''} |")
    (Path(__file__).resolve().parent / "outliers.md").write_text("\n".join(out) + "\n")
    print("\n".join(out[:14]))


if __name__ == "__main__":
    main()
