#!/usr/bin/env python3
"""
outlier_details.py - the 30 buildings removed as outliers: what each one's reference data contains.

The rules are in analysis/outliers.py (they use only the reference LCA and the features). This script
looks inside the reference LCA of each flagged building: which enclosure items its inventory holds,
the floor area its value is divided by, its scope, and how the prompts did on it.

Reads the cached raw rows GWP-calculation/full_lca_results_breakdown.pkl (from enclosure_breakdown.py).
Writes analysis/outlier_details.md.
"""
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common_fit import load  # noqa: E402
from outliers import flags  # noqa: E402
from fit_wb_tables import wb_truth  # noqa: E402
from feature_study import estimates  # noqa: E402

RUNS = {"v1": "20261104_baseline-innate", "v3": "20261104_prompt-v3", "v4": "20261116_prompt-v4",
        "v5": "20261116_prompt-v5"}
SHORT = {"New Construction": "new", "Minor Renovation": "minor renov.", "Major Renovation": "major renov.",
         "Tenant Improvement": "tenant impr."}


def main():
    t, area, m, b, split = load()
    f, (lo, hi) = flags()
    W = wb_truth(t.index)
    raw = pd.read_pickle(ROOT / "GWP-calculation" / "full_lca_results_breakdown.pkl")
    enc = raw[(raw.omniclass_element == "Shell - Enclosure") & (raw.life_cycle_stage == "A1-A3")]
    rows_per = enc.groupby("project_index").size().reindex(t.index).fillna(0)
    O = t.index[f.outlier]

    def inventory(p, k=4):
        e = enc[enc.project_index == p]
        s = (e.groupby("mat_type").gwp.sum() / area[p]).sort_values(ascending=False)
        s = s[s >= 0.05]
        items = ", ".join(f"{name} {v:.1f}" for name, v in s.head(k).items())
        return f"{len(e)} row{'' if len(e) == 1 else 's'}: {items}" + (", ..." if len(s) > k else "")

    def basis(p):
        return "CFA" if pd.notna(m.bldg_cfa[p]) else "renov.+added GFA"

    def table(ix):
        out = ["| Project | Type | Use | Storeys | Scope | Floor area, m² (basis) | Enclosure A1–A3, kgCO2e/m² | "
               "What the enclosure inventory holds (kgCO2e/m² floor) | Whole building A–C |",
               "|---|---|---|---|---|---|---|---|---|"]
        for p in sorted(ix, key=lambda i: t[i]):
            out.append(f"| {p} | {SHORT.get(m.bldg_proj_type[p], m.bldg_proj_type[p])} | {m.bldg_prim_use[p]} | "
                       f"{m.bldg_stories_above[p] if pd.notna(m.bldg_stories_above[p]) else '–'} | {m.lca_phys_scope[p]} | "
                       f"{area[p]:,.0f} ({basis(p)}) | **{t[p]:.1f}** | {inventory(p)} | {W[p]:.0f} |")
        return out

    inc, oos, ext = f.incomplete, f.out_of_scope, f.extreme
    ext_only = ext & ~inc & ~oos
    out = ["# The 30 buildings removed as outliers", "",
           "Rules from `analysis/outliers.py`; they use only the reference LCA and the features, never an LLM estimate. "
           "Inventory items are the enclosure A1–A3 rows of the reference LCA (`full_lca_results.xlsx`), largest first, "
           "per m² of the floor area the value is divided by.", "",
           "| Rule | Definition | Buildings | Also extreme |", "|---|---|---|---|",
           f"| R1 incomplete inventory | new construction with no window, glazing, curtain wall or storefront GWP | {int(inc.sum())} | {int((inc & ext).sum())} |",
           f"| R2 out of scope | `lca_phys_scope` has no E: the source LCA did not assess the enclosure | {int(oos.sum())} | {int((oos & ext).sum())} |",
           f"| R3 extreme value | log value outside Tukey's fences, below {lo:.1f} or above {hi:.0f} kgCO2e/m² | {int(ext.sum())} | – |",
           f"| Any rule | (R1 and R2 do not overlap; {int(ext_only.sum())} buildings are flagged by R3 alone) | **{len(O)}** | |", ""]
    reno = m.bldg_proj_type != "New Construction"
    out += ["## Who they are", "",
            "- By project type: " + ", ".join(f"{k} {v}" for k, v in m.bldg_proj_type[O].value_counts().items()) + ".",
            f"- Renovations and fit-outs are {int(reno[O].sum())} of the 30 but only {int(reno.sum())} of all 292: "
            f"{100 * reno[O].sum() / reno.sum():.0f}% of all renovations and fit-outs are flagged, against "
            f"{100 * (~reno[O]).sum() / (~reno).sum():.1f}% of new buildings.",
            f"- Their enclosure inventories are sparse: a median of {rows_per[O].median():.0f} material rows, against "
            f"{rows_per[~f.outlier].median():.0f} for the other 262 buildings.",
            f"- {int((t[O] < lo).sum())} lie below the lower fence ({lo:.1f}) and one (project 137) above the upper fence. "
            f"Of the other {int(((t[O] >= lo) & (t[O] <= hi)).sum())}, all but project 264 (141.4, flagged for its missing "
            f"windows) lie between {lo:.1f} and {t[O][(t[O] >= lo) & (t[O] < 100)].max():.0f}, in the bottom quarter of the "
            "distribution.", ""]

    out += ["## R1: incomplete inventory (10 new buildings)", "",
            "The reference model holds no glass at all. Seven of the ten are occupied buildings that would normally have "
            "windows (offices, a school, a hospital, an assembly building, an industrial building, a warehouse), and those "
            "with a window-to-wall ratio report a substantial one (WWR: " +
            ", ".join(f"{m.bldg_wwr[p]:.2f} for project {p}" for p in sorted(t.index[inc & m.bldg_wwr.notna()])) +
            "). The other three are parking garages (27, 35, 141), where an open structure without glass is plausible; "
            "they have no thermal envelope and are atypical rather than wrong. The enclosure value is then only the part "
            "that was modelled. Their whole-building values are ordinary, so the structure was modelled and the enclosure "
            "was not, or only in part. Project 264 is the exception at the high end: 104 kgCO2e/m² of aluminium sheet "
            "and no glass.", "", *table(t.index[inc]), ""]
    out += ["## R2: enclosure not in the LCA's scope (13 renovations and fit-outs)", "",
            "Their `lca_phys_scope` is interiors (CF), structure and interiors (SCF) or similar: the study did not set out to "
            "assess the enclosure. The dataset still classifies a few of their items as Shell – Enclosure: interior glazing "
            "and storefronts, steel studs, gypsum board, paint, a single insulation entry. The value measures what an interior "
            "or structural LCA happened to touch, not the building's enclosure.", "", *table(t.index[oos]), ""]
    out += [f"## R3: extreme values flagged by this rule alone ({int(ext_only.sum())})", "",
            "The other 11 extreme values are already caught by R1 or R2.", "", *table(t.index[ext_only]), ""]
    env_ratio = m.bldg_therm_env_area / area
    out += [f"Project 137 is the only high extreme: its envelope area ({m.bldg_therm_env_area[137]:,.0f} m²) is "
            f"{env_ratio[137]:.1f} times the floor area its value is divided by ({area[137]:,.0f} m² of renovated floor), "
            f"against a median of {env_ratio.median():.2f} for all buildings. A full re-cladding of a 16–20 storey office "
            "is divided by a small renovated floor area.", ""]

    # effect on the results
    lines = ["| Prompt | inside ±20% among the 30 | median estimate / reference among the 30 | coverage, all 292 | "
             "coverage, cleaned 262 |", "|---|---|---|---|---|"]
    for name, run in RUNS.items():
        e = estimates(run).reindex(t.index)
        ins = (t >= .8 * e) & (t <= 1.2 * e)
        lines.append(f"| {name} | {int(ins[O].sum())} of 30 | {float(np.exp(np.log(e[O] / t[O]).median())):.2f} | "
                     f"{100 * ins.mean():.1f}% | {100 * ins[~f.outlier].mean():.1f}% |")
    out += ["## Effect on the results", "", *lines, "",
            "No prompt can estimate these values from the 48 features: the values describe the scope and completeness of "
            "the source study, not the building. Every result is reported on all 292 buildings and on the cleaned 262."]
    p = Path(__file__).resolve().parent / "outlier_details.md"
    p.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
