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
PROMPT_VERSION = "v2"         # "v1" = baseline prompt, "v2" = revised after the baseline error analysis
CONDITION = "prompt-v2"       # label written to the ontology_mode column of the runs CSVs

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

# v1: baseline (20261104_baseline-innate)
TASK_TEXT_V1 = (
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

# v2: revised after the baseline error analysis (report/report.md, section 5). Changes:
#   (1) scope written to match what the dataset classifies as Shell - Enclosure,
#   (2) a required component-by-component method (areas -> assemblies -> intensities -> total),
#   (3) high-impact materials (HFC-blown XPS, aluminum curtain wall) named explicitly,
#   (4) an instruction not to pull estimates toward a typical building,
#   (5) guidance for renovations, (6) a BEST line in addition to the RANGE line.
TASK_TEXT_V2 = """\
Scope. Estimate the embodied carbon of the building enclosure as classified in this dataset (OmniClass "Shell - Enclosure"), life cycle stages A1-A3 only (raw material supply, transport to the factory, manufacturing). Exclude A4, A5, B, C and D. The enclosure includes:
- exterior walls as complete assemblies: cladding, backup framing or studs, sheathing, cavity and continuous insulation, air and vapor barriers, and the interior gypsum layer of exterior walls; structural exterior walls (concrete, CMU, tilt-up) when they form the wall;
- fenestration: windows, curtain wall, storefront and skylights (frames and glass), and exterior doors;
- the roof assembly above the structural deck: insulation, cover board, membrane or roofing;
- insulation at slab edges, below grade and under slabs that belongs to the thermal envelope.
It excludes foundations, the structural frame, floor and roof decks or slabs, interior partitions and interior finishes.

Method. Work through these steps and show the key numbers:
1. Areas. If bldg_therm_env_area is given, use it as the total envelope area. Otherwise estimate the roof area (footprint = floor area / stories above grade), the above-grade wall area (perimeter x height) and the glazed area (bldg_wwr x wall area), plus any insulated ground-floor or below-grade area. State the resulting envelope-to-floor-area ratio; single-storey and low-rise buildings often exceed 1.
2. Assemblies. From the climate zone, R-values, building use, structure, region and construction type, choose the most likely wall, glazing and roof assemblies. Name the insulation type and estimate its thickness from the R-value.
3. Intensities. Give each component an A1-A3 intensity in kgCO2e per m2 of that component, using values typical of the North American whole-building LCA tools of the assessment year (Tally, One Click LCA). Account for these high-impact materials:
   - XPS insulation made with HFC blowing agents is common in these tools and carries roughly ten times or more the GWP of mineral wool, fiberglass or polyiso per unit of thermal resistance, so a thick XPS layer (for example roof or below-grade insulation in cold climates) can dominate the enclosure total.
   - Aluminum is carbon-intensive per kg (curtain wall and storefront framing, window frames, metal panels, ACM). Aluminum-framed curtain wall is about 100-200 kgCO2e per m2 of facade, and fully glazed curtain wall facades are among the highest-carbon enclosures.
   - Insulated glass units, precast concrete panels and masonry are also significant.
4. Total. Sum the components, divide by the floor area, and give a range that reflects your uncertainty about the assemblies. Do not pull the estimate toward a typical building: metal-clad, curtain-wall or thickly insulated enclosures can exceed 200 kgCO2e per m2 of floor area, and projects with little new enclosure work can fall below 10.
5. Renovations. For renovations and tenant improvements, count only new enclosure materials. Use bldg_proj_type, lca_phys_scope and mass_total per floor area to judge how much new envelope work was done. Major renovations often include new windows, cladding or roofing, and a high mass_total per floor area indicates substantial new material.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

End your answer with exactly two final lines in this format and nothing after them:
BEST_kgCO2e_per_m2: <value>
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on these lines)"""

TASK_TEXTS = {"v1": TASK_TEXT_V1, "v2": TASK_TEXT_V2}
TASK_TEXT = TASK_TEXTS[PROMPT_VERSION]

# Instructions given to each Claude Code subagent (the "LLM under test"). {placeholders} are
# filled by subagent_runs.py prepare. ANSWER_LENGTH and FINAL_LINES follow the prompt version.
ANSWER_LENGTH = {"v1": "briefly state your method and key assumptions (roughly 60-150 words)",
                 "v2": "work through its method steps with the key numbers (roughly 120-250 words)"}[PROMPT_VERSION]
FINAL_LINES = {"v1": "the final line `RANGE_kgCO2e_per_m2: <low> - <high>`",
               "v2": "the two final lines `BEST_kgCO2e_per_m2: <value>` and "
                     "`RANGE_kgCO2e_per_m2: <low> - <high>`"}[PROMPT_VERSION]
SUBAGENT_INSTRUCTIONS = """\
You are the language model being tested in a building life-cycle-assessment (LCA) experiment for a university course project. Your job is to answer a set of estimation prompts using only your own knowledge.

Input file: {task_file}
It is about {n_lines:,} lines, so read all of it with the Read tool, using offset/limit to page past line 2,000. It contains a System line, a shared context (a glossary of the feature names), and {n_buildings} building sections. Each section starts with a line like `===== KEY: {example_key} =====`, followed by the building's features and the question.

Rules. Breaking any of these invalidates the experiment:
- Read only that one task file. Do not open, list or search any other file or folder (especially nothing under results/, GWP-calculation/ or references/). Do not use web search or web fetch, and do not run code or shell commands. The only tools you may use are Read (on the task file) and Write (for your answer files).
- Treat each building as a separate, independent request, as if you were seeing it alone. Do not compare buildings, rank them, or adjust one estimate because of another.
- Follow each building's prompt exactly: {answer_length}, then end with {final_lines} containing plain numbers only.

Output: write your answers in parts of about 10 buildings each, using one new file per part and never overwriting an earlier part:
{answers_prefix}_part-1.md, then _part-2.md, and so on.
Inside each part file, every answer starts with its key line copied exactly from the task file, followed by the answer text, for example:

===== KEY: {example_key} =====
<answer>
{example_final}

Answer all {n_buildings} buildings, in the order they appear in the task file, with the key lines copied exactly.

When you are finished, reply with exactly one line: `done: <number of answers written> answers in <number of parts> parts`. Do not include the answers themselves in your reply."""
EXAMPLE_FINAL = {"v1": "RANGE_kgCO2e_per_m2: 40 - 75",
                 "v2": "BEST_kgCO2e_per_m2: 55\nRANGE_kgCO2e_per_m2: 40 - 75"}[PROMPT_VERSION]


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
        "prompt_version": PROMPT_VERSION,
        "include_papers": INCLUDE_PAPERS,
        "papers": [p.name for p in PAPER_PATHS] if INCLUDE_PAPERS else [],
        "include_practice_guide": INCLUDE_PRACTICE_GUIDE,
        "extra_context": [p.name for p in EXTRA_CONTEXT_PATHS],
        "features": FEATURES,
        "system_prompt": SYSTEM_PROMPT,
        "task_text": TASK_TEXT,
        "subagent_instructions": SUBAGENT_INSTRUCTIONS,
    }
