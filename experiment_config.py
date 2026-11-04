"""
experiment_config.py - Group 8 experiment settings and prompt text. Edit this file only.

Scope of every estimate: building enclosure (OmniClass "Shell - Enclosure"), life cycle stages
A1-A3, kgCO2e per m2 of floor area. The ground truth for the same scope is made by
GWP-calculation/sum_gwp.py -> results/ground_truth.csv.

One experiment condition = one combination of the switches below. subagent_runs.py copies
these settings into results/<run-name>/subagent/manifest.json, so every run records what it used.
"""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
REF = BASE_DIR / "references"
METADATA_PATH = REF / "buildings_metadata_LLM.xlsx"
GLOSSARY_PATH = REF / "data_glossary_LLM.xlsx"

# --------------------------------------------------------------------------------------
# Condition - edit here
# --------------------------------------------------------------------------------------
CONDITION = "innate"          # label written to the ontology_mode column of the runs CSVs

INCLUDE_PAPERS = False        # background papers (text extracted from the PDFs)
PAPER_PATHS = [REF / f"{i}.pdf" for i in range(1, 5)]
INCLUDE_PRACTICE_GUIDE = False
PRACTICE_GUIDE_PATH = REF / "250524_CLF-LCA-Practice-Guide.txt"
EXTRA_CONTEXT_PATHS: list[Path] = []   # later iterations, e.g. [REF / "envelope_notes.md"]
MAX_PDF_CHARS = 100_000

# Building features sent for each building: "all" (every column in buildings_metadata_LLM.xlsx)
# or a list of column names for the feature study.
FEATURES = "all"
# FEATURES = ["site_clim_zone", "bldg_prim_use", "bldg_proj_type", "bldg_cfa", "bldg_gfa",
#             "bldg_renovated_gfa", "bldg_added_gfa", "bldg_stories_above", "bldg_height",
#             "bldg_therm_env_area", "bldg_wwr", "bldg_rval_walls", "bldg_rval_roofs",
#             "str_prim_vert_sys", "lca_phys_scope"]

# --------------------------------------------------------------------------------------
# Prompt text - edit here
# --------------------------------------------------------------------------------------
SYSTEM_PROMPT = "You are a building LCA expert."

TASK_TEXT = (
    "Scope: the building enclosure only, i.e. OmniClass \"Shell - Enclosure\" (exterior walls "
    "and cladding, exterior windows, curtain walls and storefronts, exterior doors, roofing, and "
    "their insulation). Exclude substructure, superstructure, interior construction and interior "
    "finishes. Life cycle stages: A1-A3 only (product stage: raw material supply, transport to "
    "the factory, manufacturing). Exclude A4, A5, B, C and D.\n\n"
    "Provide a plausible range of the enclosure's A1-A3 embodied carbon in units of kgCO2e per m2 "
    "of building floor area (a range, not a single value). For floor area, use bldg_cfa. If "
    "bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa. Briefly state your "
    "method and key assumptions.\n\n"
    "End your answer with exactly one final line in this format and nothing after it:\n"
    "RANGE_kgCO2e_per_m2: <low> - <high>\n"
    "(plain numbers only, no units or other text on that line)"
)


# --------------------------------------------------------------------------------------
# Builders (no need to edit)
# --------------------------------------------------------------------------------------
def read_pdf(path: Path, max_chars: int = MAX_PDF_CHARS) -> str:
    import PyPDF2
    with open(path, "rb") as f:
        text = "\n".join((p.extract_text() or "") for p in PyPDF2.PdfReader(f).pages)
    return text[:max_chars] + "...[truncated]" if len(text) > max_chars else text


def load_metadata() -> pd.DataFrame:
    meta = pd.read_excel(METADATA_PATH)
    if FEATURES != "all":
        bad = [c for c in FEATURES if c not in meta.columns]
        if bad:
            raise SystemExit(f"FEATURES has columns not in {METADATA_PATH.name}: {bad}")
        meta = meta[["project_index", *FEATURES]]
    return meta


def glossary_text() -> str:
    g = pd.read_excel(GLOSSARY_PATH)
    if FEATURES != "all":
        g = g[g["Feature Name"].isin(FEATURES)]
    # One line per feature (pandas' to_string pads every row to the longest description)
    return "\n".join(
        f"- {r['Feature Name']}"
        + (f" [{r['Units']}]" if pd.notna(r["Units"]) else "")
        + f": {' '.join(str(r['Description']).split())}"
        for _, r in g.iterrows())


def build_prefix() -> list[str]:
    """Shared context, identical for every building."""
    parts = [
        "Forget the information from previous sessions and calculate everything from the beginning.",
        f"data_glossary_LLM contains feature names and descriptions for the data:\n\n{glossary_text()}",
    ]
    if INCLUDE_PAPERS:
        missing = [p.name for p in PAPER_PATHS if not p.exists() or p.stat().st_size < 1000]
        if missing:
            raise SystemExit(f"Papers missing or empty: {missing}. Run scripts/fetch_reference_pdfs.sh")
        papers = "\n".join(read_pdf(p) for p in PAPER_PATHS)
        parts.append("These journal papers contain background information about the early building "
                     f"LCA process:\n\n{papers}")
    if INCLUDE_PRACTICE_GUIDE:
        parts.append("This document contains a detailed practice guide on life cycle assessment of "
                     "buildings focused on implementation. Use this guideline for LCA estimation:"
                     f"\n\n{PRACTICE_GUIDE_PATH.read_text(encoding='utf-8')}")
    for p in EXTRA_CONTEXT_PATHS:
        parts.append(f"Additional reference ({p.name}):\n\n{p.read_text(encoding='utf-8')}")
    parts.append("Reference the given feature information above. Estimate the embodied carbon of "
                 "the building enclosure of the building below:")
    return parts


def format_building(row: pd.Series) -> str:
    """One 'field: value' line per non-empty column. project_index is the ID, not a feature."""
    lines = []
    for col, val in row.items():
        if col == "project_index" or pd.isna(val):
            continue
        if isinstance(val, float) and val.is_integer():
            val = int(val)
        lines.append(f"{col}: {val}")
    return "\n".join(lines)


def build_building_prompt(building_text: str) -> str:
    return f"{building_text}\n\n{TASK_TEXT}"


def settings() -> dict:
    return {
        "condition": CONDITION,
        "include_papers": INCLUDE_PAPERS,
        "papers": [p.name for p in PAPER_PATHS] if INCLUDE_PAPERS else [],
        "include_practice_guide": INCLUDE_PRACTICE_GUIDE,
        "extra_context": [p.name for p in EXTRA_CONTEXT_PATHS],
        "features": FEATURES,
        "system_prompt": SYSTEM_PROMPT,
        "task_text": TASK_TEXT,
    }
