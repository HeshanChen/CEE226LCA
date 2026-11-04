#!/usr/bin/env python3
"""
make_split.py - fixed dev/test split of the 292 projects (70% dev, 30% test).

Stratified on input features only (never on the ground truth): new construction vs renovation
x climate group (cold zones 5-8, zone 4, warm zones 1-3, other/unknown). Seed 226.

The split was assigned after the v1-v3 runs (report/report.md, section 10). The dev split is
used to check that every finding behind the prompt revisions also holds on dev alone. The test
split is used for the final comparison of prompts v1, v2 and v3.

Writes: results/split.csv (project_index, split)
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SEED = 226
TEST_FRACTION = 0.30


def climate_group(z: str) -> str:
    z = str(z)
    if any(z.startswith(f"Zone {n}") for n in (5, 6, 7, 8)):
        return "cold"
    if z.startswith("Zone 4"):
        return "zone4"
    if any(z.startswith(f"Zone {n}") for n in (1, 2, 3)):
        return "warm"
    return "other"


def main():
    m = pd.read_excel(ROOT / "references" / "buildings_metadata_LLM.xlsx")
    strata = ((m["bldg_proj_type"] == "New Construction").map({True: "new", False: "reno"})
              + "_" + m["site_clim_zone"].map(climate_group))
    rng = np.random.default_rng(SEED)
    test = set()
    for _, idx in m.groupby(strata).groups.items():
        idx = list(m.loc[idx, "project_index"])
        k = int(round(TEST_FRACTION * len(idx)))
        test.update(rng.choice(idx, size=k, replace=False).tolist())
    out = pd.DataFrame({"project_index": m["project_index"],
                        "split": ["test" if p in test else "dev" for p in m["project_index"]],
                        "stratum": strata})
    out.to_csv(ROOT / "results" / "split.csv", index=False)
    print(out["split"].value_counts().to_string())
    print(pd.crosstab(out["stratum"], out["split"]).to_string())


if __name__ == "__main__":
    main()
