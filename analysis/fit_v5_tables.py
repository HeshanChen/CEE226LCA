#!/usr/bin/env python3
"""
fit_v5_tables.py - answer-fitted tables for prompt v5 (IN-SAMPLE by design).

Fitted on the reference values of the 262 cleaned buildings (all of them, dev and test), using the
bottom-up take-off A that prompt v4 produced (mean of its 3 runs):
  K  calibration factor for the take-off, median(reference / A) by primary use x whether the
     thermal envelope area is given (cells with >= 5 buildings; else by use; else overall)
  B  benchmark, median reference by primary use x storeys above grade
     (cells with >= 5 buildings; else by use; else overall)
v5 estimate = 0.5 x K x A + 0.5 x B (out-of-scope LCAs: 8). The design was chosen among
calibration keys x benchmark keys x weights for in-sample coverage that holds up when the take-off
is re-sampled (tables fitted on v4 runs 0-1, scored with run 2).

Because the tables use every reference value, v5's coverage is in-sample: it shows how far
answer-fitted prompting can go, not how well a prompt generalises (that is v4's held-out result).

Writes results/v5_tables.json and prints the simulated coverage with v4's take-off.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load, coverage as cov, RES  # noqa: E402
from outliers import flags  # noqa: E402
from v4_study import parts  # noqa: E402

MIN_N = 5
W_A = 0.5
STOREYS = {"16 to 20": "11 or more", "11 to 15": "11 or more", "21 or more": "11 or more"}
USE_SHORT = {"Residential: Multifamily (5 or more units)": "Residential: Multifamily"}


def features(m):
    F = pd.DataFrame(index=m.index)
    F["use"] = m.bldg_prim_use
    F["struct"] = (m.str_prim_vert_sys.fillna("Other").map(str).str.split(":").str[0]
                   .replace({"nan": "Other", "Masonry": "Other"}))
    F["storeys"] = m.bldg_stories_above.fillna("2 to 5").map(str).replace(STOREYS).replace({"nan": "2 to 5"})
    F["env"] = m.bldg_therm_env_area.notna().map({True: "envelope area given", False: "envelope area not given"})
    return F


def cell_table(values, F, keys, idx):
    g = values.loc[idx].groupby([F.loc[idx, k] for k in keys]).agg(["median", "size"])
    return {k if isinstance(k, str) else " | ".join(k): float(np.exp(r["median"]))
            for k, r in g.iterrows() if r["size"] >= MIN_N}


def apply(F, tab, keys, fallback_keys, fallback_tab, overall):
    key = F[keys[0]].map(str)
    for k in keys[1:]:
        key = key + " | " + F[k].map(str)
    fb = F[fallback_keys[0]]
    return key.map(tab).fillna(fb.map(fallback_tab)).fillna(overall)


def main():
    t, area, m, b, split = load()
    f, _ = flags()
    F = features(m)
    P = parts("20261116_prompt-v4")
    A = P.groupby("project_index").A.mean()
    cl = t.index[~f.outlier]
    lr, lt = np.log(t / A), np.log(t)
    K_cell = {k: round(v, 2) for k, v in cell_table(lr, F, ["use", "env"], cl).items()}
    K_use = {k: round(v, 2) for k, v in cell_table(lr, F, ["use"], cl).items()}
    K_all = round(float(np.exp(lr.loc[cl].median())), 2)
    B_cell = {k: round(v) for k, v in cell_table(lt, F, ["use", "storeys"], cl).items()}
    B_use = {k: round(v) for k, v in cell_table(lt, F, ["use"], cl).items()}
    B_all = round(float(np.exp(lt.loc[cl].median())))
    K = apply(F, K_cell, ["use", "env"], ["use"], K_use, K_all)
    B = apply(F, B_cell, ["use", "storeys"], ["use"], B_use, B_all)
    e = (W_A * K * A + (1 - W_A) * B).where(~f.out_of_scope, 8.0)
    v4 = P.groupby("project_index").mid.mean()
    print(f"simulated v5 with v4's take-off: all {100 * cov(e, t):.1f}% | cleaned {100 * cov(e.loc[cl], t.loc[cl]):.1f}% "
          f"(v4: {100 * cov(v4, t):.1f}% | {100 * cov(v4.loc[cl], t.loc[cl]):.1f}%)")
    out = {"fitted_on": f"{len(cl)} cleaned buildings (all splits): in-sample", "w_take_off": W_A,
           "K_use_envelope_area": K_cell, "K_use": K_use, "K_overall": K_all,
           "B_use_storeys": B_cell, "B_use": B_use, "B_overall": B_all}
    (RES / "v5_tables.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
