#!/usr/bin/env python3
"""climate_use.py - proposal RQ1 from the data: enclosure A1-A3 by climate group and building use.
New construction only, flagged incomplete references excluded. Writes analysis/climate_use.md."""
import re
from pathlib import Path

import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
b = pd.read_csv(ROOT / "results" / "ground_truth_breakdown.csv").set_index("project_index")
m = pd.read_excel(ROOT / "references" / "buildings_metadata_LLM.xlsx").set_index("project_index")
d = b.join(m[["site_clim_zone", "bldg_prim_use", "bldg_proj_type"]])
d = d[~d.flag_incomplete.astype(bool) & (d.bldg_proj_type == "New Construction")]


def clim(z):
    mm = re.search(r"Zone (\d)", str(z))
    if not mm:
        return None
    n = int(mm.group(1))
    return "Warm (zones 1-3)" if n <= 3 else ("Mixed (zone 4)" if n == 4 else "Cold (zones 5-8)")


d["climate"] = d.site_clim_zone.map(clim)
out = ["# Enclosure A1-A3 by climate and building use (RQ1, from the data)", "",
       f"New construction, flagged incomplete references excluded ({len(d)} projects). kgCO2e/m2 floor area.", ""]
for col, lab in [("climate", "Climate group"), ("bldg_prim_use", "Primary use (n >= 8)")]:
    g = d.groupby(col)["ECI_true_kgCO2e_m2"]
    t = pd.DataFrame({"n": g.size(), "median": g.median(), "q25": g.quantile(.25), "q75": g.quantile(.75)})
    t = t[t.n >= 8].sort_values("median")
    kw = stats.kruskal(*[d.loc[d[col] == k, "ECI_true_kgCO2e_m2"] for k in t.index])
    out += [f"| {lab} | n | Median | IQR |", "|---|---|---|---|"]
    out += [f"| {k} | {int(r.n)} | {r['median']:.1f} | {r.q25:.1f}-{r.q75:.1f} |" for k, r in t.iterrows()]
    out += ["", f"Kruskal-Wallis: H = {kw.statistic:.1f}, p = {kw.pvalue:.2g}", ""]
(ROOT / "analysis" / "climate_use.md").write_text("\n".join(out))
print("\n".join(out))
