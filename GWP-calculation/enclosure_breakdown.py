"""
enclosure_breakdown.py - per-project material breakdown of the enclosure A1-A3 ground truth,
plus data-quality flags. Used for the error analysis and the "clean subset" metrics.

Reads:   GWP-calculation/full_lca_results.xlsx (cached as full_lca_results_breakdown.pkl)
         results/ground_truth.csv (floor area per project, written by sum_gwp.py)
         references/buildings_metadata_LLM.xlsx (project type)
Writes:  results/ground_truth_breakdown.csv, one row per project:
           kgCO2e per m2 floor area by mat_group, XPS separately,
           has_fenestration / has_insulation,
           flag_incomplete = new construction whose enclosure inventory has no window,
                             glazing, curtain wall or storefront GWP at all (likely an
                             incomplete source LCA model, not a property of the building)

Run:     python GWP-calculation/enclosure_breakdown.py
"""

from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
INPUT = BASE / "full_lca_results.xlsx"
CACHE = BASE / "full_lca_results_breakdown.pkl"
ROOT = BASE.parent
GROUND_TRUTH = ROOT / "results" / "ground_truth.csv"
METADATA = ROOT / "references" / "buildings_metadata_LLM.xlsx"
OUT = ROOT / "results" / "ground_truth_breakdown.csv"
COLS = ["project_index", "omniclass_element", "life_cycle_stage", "mat_group", "mat_type", "gwp"]


def load() -> pd.DataFrame:
    if CACHE.exists() and CACHE.stat().st_mtime >= INPUT.stat().st_mtime:
        return pd.read_pickle(CACHE)
    print(f"Reading {INPUT.name} (slow once; caching to {CACHE.name}) ...")
    df = pd.read_excel(INPUT, usecols=COLS)
    df.to_pickle(CACHE)
    return df


def main():
    df = load()
    e = df[(df["omniclass_element"] == "Shell - Enclosure") & (df["life_cycle_stage"] == "A1-A3")].copy()
    gt = pd.read_csv(GROUND_TRUTH)
    gt["project_index"] = gt["Project Name"].str.extract(r"(\d+)")[0].astype(int)
    area = gt.set_index("project_index")["floor_area_m2"]
    e["kg_m2"] = e["gwp"] / e["project_index"].map(area)

    by_group = e.pivot_table(index="project_index", columns="mat_group", values="kg_m2",
                             aggfunc="sum", fill_value=0.0)
    by_group.columns = [f"{c} [kgCO2e/m2]" for c in by_group.columns]
    xps = e[e["mat_type"] == "Extruded polystyrene XPS"].groupby("project_index")["kg_m2"].sum()
    fen_mask = (e["mat_group"].isin(["Glazing", "Windows and frames"])
                | e["mat_type"].str.contains("curtain|storefront|window", case=False, na=False))
    fen = e[fen_mask].groupby("project_index")["gwp"].sum()
    ins = e[e["mat_group"] == "Insulation"].groupby("project_index")["gwp"].sum()

    meta = pd.read_excel(METADATA).set_index("project_index")
    out = pd.DataFrame(index=gt["project_index"].sort_values().values)
    out.index.name = "project_index"
    out["Project Name"] = "project-" + out.index.astype(str)
    out["ECI_true_kgCO2e_m2"] = gt.set_index("project_index")["ECI_true_kgCO2e_m2"]
    out["XPS [kgCO2e/m2]"] = xps.reindex(out.index).fillna(0).round(3)
    out["xps_share"] = (out["XPS [kgCO2e/m2]"] / out["ECI_true_kgCO2e_m2"]).round(3)
    out["has_fenestration"] = fen.reindex(out.index).fillna(0) > 0
    out["has_insulation"] = ins.reindex(out.index).fillna(0) > 0
    out["flag_incomplete"] = (meta["bldg_proj_type"].reindex(out.index) == "New Construction") & ~out["has_fenestration"]
    out = out.join(by_group.round(3))
    out.reset_index().to_csv(OUT, index=False)

    print(f"{len(out)} projects. With XPS: {(out['XPS [kgCO2e/m2]'] > 0).sum()}. "
          f"Flagged incomplete (new construction, no fenestration GWP): {out['flag_incomplete'].sum()} "
          f"-> {out.index[out['flag_incomplete']].tolist()}")
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
