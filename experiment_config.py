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
PROMPT_VERSION = "wb1"        # "v1" baseline, "v2" error analysis, "v3" sourced intensities, "v4" weighted evidence, "v5" answer-fitted enclosure, "wb5"/"wb6" answer-fitted whole building (A-C), "wb1" whole building, model alone
CONDITION = "wholebuilding-wb1"   # label written to the ontology_mode column of the runs CSVs

# v4 only: write the task text once per task file (shared context) instead of repeating it under every
# building. The text each building gets is the same; the task files shrink from about 130k to 20k tokens.
TASK_TEXT_ONCE = PROMPT_VERSION in ("v4", "v5", "wb5", "wb6", "wb1")

INCLUDE_PAPERS = False        # background papers (text extracted from the PDFs)
PAPER_PATHS = [REF / f"{i}.pdf" for i in range(1, 5)]
INCLUDE_PRACTICE_GUIDE = False
PRACTICE_GUIDE_PATH = REF / "250524_CLF-LCA-Practice-Guide.txt"
EXTRA_CONTEXT_PATHS: list[Path] = []   # later iterations, e.g. [REF / "envelope_notes.md"]
# Envelope-focused documents (domain-knowledge condition): replace the general whole-building
# papers. Publicly available PDFs, fetched with scripts/fetch_envelope_docs.sh (not re-hosted).
INCLUDE_ENVELOPE_DOCS = False
ENVELOPE_DOC_PATHS = [REF / "envelope_docs" / f for f in
                      ("rdh2025.pdf", "clf2023.pdf", "arup_glass.pdf", "ubc2022.pdf")]
MAX_ENVELOPE_DOC_CHARS = 30_000   # per document, truncated like the course pipeline's MAX_PDF_CHARS
MAX_PDF_CHARS = 100_000

# Building features sent for each building: "all" (every column in buildings_metadata_LLM.xlsx)
# or a list of column names for the feature study.
FEATURES = "all"
# FEATURES = ["site_clim_zone", "bldg_prim_use", "bldg_proj_type", "bldg_cfa", "bldg_gfa",
#             "bldg_renovated_gfa", "bldg_added_gfa", "bldg_stories_above", "bldg_height",
#             "bldg_therm_env_area", "bldg_wwr", "bldg_rval_walls", "bldg_rval_roofs",
#             "str_prim_vert_sys", "lca_phys_scope"]

# Named feature sets for the feature study (report section 11). "all" = every column.
# The floor-area fields are in every set because the task defines the unit with them.
FLOOR_AREA = ["bldg_cfa", "bldg_added_gfa", "bldg_renovated_gfa"]
FEATURE_GROUPS = {
    "site": ["site_country", "site_region", "site_state_province", "site_clim_zone"],
    "code_year": ["bldg_code_year", "bldg_energy_code_year", "bldg_compl_year"],
    "use_type": ["bldg_proj_type", "bldg_ibc_type", "bldg_park_type", "bldg_prim_use", "bldg_sec_use"],
    "size": ["bldg_gfa", "bldg_park_gfa", "bldg_occupants", "bldg_res_units"],
    "geometry": ["bldg_stories_above", "bldg_stories_below", "bldg_height", "bldg_therm_env_area", "bldg_wwr"],
    "thermal": ["bldg_rval_walls", "bldg_rval_roofs"],
    "structure": ["str_seis_site_cls", "str_sdc", "str_wind_speed", "str_prim_horiz_sys", "str_prim_vert_sys",
                  "str_lat_sys", "str_podium", "str_sec_horiz_sys", "str_sec_vert_sys", "str_grid_long",
                  "str_grid_short", "str_fdn_type", "str_sys_summary"],
    "lca": ["lca_assessment_year", "lca_design_phase", "lca_rsp", "lca_software", "lca_purp_of_assessment",
            "lca_phys_scope", "lca_ec_reductions", "lca_ec_reduction_percent"],
    "mass": ["mass_total"],   # sum of the reference LCA's inventory mass (A-C): not known at early design
}
ALL_FEATURES = FLOOR_AREA + [c for g in FEATURE_GROUPS.values() for c in g]
FEATURE_SETS = {
    "all": "all",
    # design-stage information only: no LCA-derived fields and no total mass
    "early": [c for c in ALL_FEATURES if c not in FEATURE_GROUPS["lca"] + FEATURE_GROUPS["mass"]],
    # envelope-relevant subset
    "env": ["site_clim_zone", "site_state_province", "bldg_prim_use", "bldg_proj_type", *FLOOR_AREA,
            "bldg_stories_above", "bldg_height", "bldg_therm_env_area", "bldg_wwr", "bldg_rval_walls",
            "bldg_rval_roofs", "str_sys_summary", "bldg_ibc_type"],
    # proposal 6.1: climate, use, U-factor (R-values), WWR, plus size and storeys
    "min": ["site_clim_zone", "bldg_prim_use", "bldg_proj_type", *FLOOR_AREA, "bldg_stories_above",
            "bldg_wwr", "bldg_rval_walls", "bldg_rval_roofs"],
    # leave-one-group-out ablations
    **{f"no-{g}": [c for c in ALL_FEATURES if c not in cols] for g, cols in FEATURE_GROUPS.items()},
}


def use_feature_set(name: str):
    """Switch FEATURES to a named set (used by subagent_runs.py prepare/resume)."""
    global FEATURES
    FEATURES = FEATURE_SETS[name]


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

# v3: revised after the v2 results (report/report.md, section 7). Keeps the v2 scope, method and
# no-anchoring rule. Changes: quantitative component intensities from external sources at the step
# where numbers are chosen (references/envelope_intensities_sources.md), the XPS modelling
# convention, a top-down check per m2 of envelope, renovations rewritten to not subtract, and
# RANGE only (BEST was less accurate than the range midpoint).
# Reference values: prompt-ready summary of references/envelope_intensities_sources.md (EPDs, CLF
# North American Material Baselines 2023/2025, PCI, RDH, Kawneer, UBC; nothing from the Benke et al.
# dataset or the CLF WBLCA benchmark). Source tags removed here; they are in that file.
V3_INTENSITIES = """\
   Opaque walls (per m2 of wall, complete assembly):
   - steel stud + metal panel or ACM rainscreen: 70-110
   - steel stud + brick veneer: 90-120; brick veneer on CMU backup: 135-165
   - steel stud + EIFS: about 50; steel stud + fiber cement or stucco: 45-80
   - wood stud + vinyl or wood siding: 25-45; wood stud + brick or stone veneer: 60-100
   - insulated metal panel: newer products 27-72; legacy polyurethane (HFC) panels about 107 (2 in) to 274 (6 in)
   - precast concrete sandwich panel: 90-165; architectural precast with backup wall: 80-130
   - tilt-up concrete with interior insulation and gypsum: 80-125
   - curtain-wall spandrel: 75-140
   Fenestration (per m2 of unit, frame and glass):
   - aluminum stick curtain wall: 120-150; aluminum unitized curtain wall: 150-210
   - aluminum storefront: 140-155; aluminum window wall: 170-180; aluminum windows: 95-140
   - vinyl windows: 40-90; fiberglass windows: 75-145
   Roof above the deck (per m2 of roof, about R-25 to R-30, with membrane and cover board):
   - polyiso: 20-28; mineral wool board: 35-55; low-GWP XPS: 28-40; metal standing seam over polyiso: 27-40
   - XPS with HFC blowing agent: 85-110 when only product-stage emissions are counted, and up to 335-410 when the blowing-agent emissions are booked with the product, as some LCA tools do
   - insulated metal roof panel: 27-72 for newer products, about 190 for a legacy 4 in panel
   Insulation per m2 at RSI 1 (R-5.7): polyiso 2-4; EPS 2.5; mineral wool board 7-8; fiberglass batt about 1; closed-cell spray foam 3-5 (HFO) or 20-36 (HFC); XPS 4-11 (low-GWP), about 18 (HFC, product stage only) or 58-99 (HFC, with blowing-agent emissions)
   Aluminum: about 6-13 kgCO2e per kg for North American extrusions; generic global aluminum data in LCA tools is about 16"""
TASK_TEXT_V3 = """\
Scope. Estimate the embodied carbon of the building enclosure as classified in this dataset (OmniClass "Shell - Enclosure"), life cycle stages A1-A3 only (raw material supply, transport to the factory, manufacturing). Exclude A4, A5, B, C and D. The enclosure includes:
- exterior walls as complete assemblies: cladding, backup framing or studs, sheathing, cavity and continuous insulation, air and vapor barriers, and the interior gypsum layer of exterior walls; structural exterior walls (concrete, CMU, tilt-up) when they form the wall;
- fenestration: windows, curtain wall, storefront and skylights (frames and glass), and exterior doors;
- the roof assembly above the structural deck: insulation, cover board, membrane or roofing;
- insulation at slab edges, below grade and under slabs that belongs to the thermal envelope.
It excludes foundations, the structural frame, floor and roof decks or slabs, interior partitions and interior finishes.

Method. Work through these steps and show the key numbers:
1. Areas. If bldg_therm_env_area is given, use it as the total envelope area. Otherwise estimate the roof area (footprint = floor area / stories above grade), the above-grade wall area (perimeter x height) and the glazed area (bldg_wwr x wall area), plus any insulated ground-floor or below-grade area. State the resulting envelope-to-floor-area ratio; single-storey and low-rise buildings often exceed 1.
2. Assemblies. From the climate zone, R-values, building use, structure, region and construction type, choose the most likely wall, glazing and roof assemblies, and name the insulation type and thickness. Whole-building LCA models from this period (Tally, One Click LCA) often model roof and below-grade insulation as XPS made with HFC blowing agents. When the insulation type is not known, include that case in your range, especially in colder climates where the insulation is thick.
3. Intensities. Give each component an A1-A3 intensity in kgCO2e per m2 of that component. Use these reference values from EPDs and industry baselines (A1-A3, per m2 of component):
{intensities}
Complete assemblies include framing, attachments, sheathing, barriers, sealants, flashing and trim, which early-stage take-offs tend to leave out; do not go below the low end of these ranges unless the assembly is clearly minimal.
4. Check. Convert your total to kgCO2e per m2 of envelope area and check that it is consistent with the reference values above. For new construction with conventional walls and 30-40% glazing, a blended value below about 50 kgCO2e per m2 of envelope usually means that a component, the aluminum and glazing content, or a high-carbon insulation option is missing; revisit those before you finalize.
5. Total. Divide the enclosure total by the floor area. Give a range that reflects your uncertainty about the assemblies, including the higher-carbon alternatives that are plausible for this building. Do not pull the estimate toward a typical building: metal-clad, curtain-wall or thickly insulated enclosures can exceed 200 kgCO2e per m2 of floor area, and projects with little new enclosure work can fall below 10.
6. Renovations. For renovations and tenant improvements the LCA covers only the new work, but that work often includes substantial new envelope elements (re-cladding, new curtain wall or windows, re-roofing). Do not assume the existing envelope is kept unless the data indicates it. Use bldg_proj_type, lca_phys_scope and mass_total per floor area as evidence of how much new material was installed.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

End your answer with exactly one final line in this format and nothing after it:
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on that line)"""

# v4: weighted evidence (report section "Prompt v4"). Two sources get equal weight: the v3 bottom-up
# take-off and a benchmark by primary use fitted on the cleaned development set
# (analysis/weight_search.py -> results/benchmarks_dev.json; the test buildings never enter it).
# Also new: an attention order for the features, the out-of-scope rule (lca_phys_scope without E),
# envelope-to-floor ratios by storeys for buildings without an envelope area (medians of the
# features themselves), and feature-keyed literature facts (references/feature_keyed_facts.md).
V4_BENCHMARKS = ("Education 91; Office 79; Residential: Multifamily 54; Public Assembly 94; Laboratory 95; "
                 "Warehouse and Storage 62; Healthcare 79; Public Order and Safety 161; Transportation Hub 153; "
                 "any other use 85")
TASK_TEXT_V4 = """\
Scope. Estimate the embodied carbon of the building enclosure as classified in this dataset (OmniClass "Shell - Enclosure"), life cycle stages A1-A3 only (raw material supply, transport to the factory, manufacturing). Exclude A4, A5, B, C and D. The enclosure includes:
- exterior walls as complete assemblies: cladding, backup framing or studs, sheathing, cavity and continuous insulation, air and vapor barriers, and the interior gypsum layer of exterior walls; structural exterior walls (concrete, CMU, tilt-up) when they form the wall;
- fenestration: windows, curtain wall, storefront and skylights (frames and glass), and exterior doors;
- the roof assembly above the structural deck: insulation, cover board, membrane or roofing;
- insulation at slab edges, below grade and under slabs that belongs to the thermal envelope.
It excludes foundations, the structural frame, floor and roof decks or slabs, interior partitions and interior finishes.

How to weigh the evidence. No feature describes the wall, glazing or roof assembly, so an estimate built only from assumed assemblies is uncertain. Reference LCAs of buildings with the same use are an equally strong source. Build both estimates and give them equal weight:
- Step A, bottom-up (weight 50%): this building's own areas, likely assemblies and component intensities.
- Step B, benchmark (weight 50%): the median enclosure result of reference LCAs with the same primary use.
Inside Step A, spend your attention in this order:
1. Envelope quantity (about half): bldg_therm_env_area, or storeys, height and floor area when it is missing, and bldg_wwr.
2. Assembly class (about a third): bldg_prim_use, bldg_ibc_type and the structural system indicate wood-frame, steel-stud, masonry, precast or curtain-wall construction.
3. Insulation convention (the rest): climate zone, R-values, lca_software, lca_assessment_year and the state or province decide whether HFC-blown XPS is plausible.
Leave out the seismic, wind, structural-grid, foundation, occupancy and code-year fields. In reference LCAs they do not move the enclosure value.

Special case, check it first. lca_phys_scope lists the element groups the LCA modelled: B substructure, S superstructure, E enclosure, C interior construction, F finishes. If it does not contain E, the enclosure was not modelled and only incidental items are booked under it. In that case skip Steps A to C and report BOTTOM_UP 8, BENCHMARK 8 and the range 6 - 10.

Step A. Bottom-up estimate. Work through these steps and show the key numbers:
1. Areas. If bldg_therm_env_area is given, use it as the total envelope area; it covers the roof, the above-grade walls and the ground-floor slab. Otherwise estimate the roof area (footprint = floor area / stories above grade), the above-grade wall area (perimeter x height) and the glazed area (bldg_wwr x wall area), plus any insulated ground-floor or below-grade area. Buildings that report an envelope area have these typical envelope-to-floor ratios: 1 storey 2.1; 2-5 storeys 1.1; 6-10 storeys 0.7; 11-15 storeys 0.5; 16 or more 0.4. Roof and ground slab are each about floor area / storeys, and the rest is wall. Typical gross wall area per m2 of floor is 0.2 for one- and two-storey schools, 0.4-0.5 for 3-6 storey offices, hotels and apartments, about 0.3 for large offices and hospitals, and 0.4 for warehouses. When bldg_wwr is missing, typical values are 0.4-0.5 for large offices, 0.2-0.3 for small offices, 0.3-0.35 for education and laboratories, 0.3 for multifamily and healthcare, 0.15-0.2 for public assembly and public safety, and 0.05 for warehouses.
2. Assemblies. From the climate zone, R-values, building use, structure, region and construction type, choose the most likely wall, glazing and roof assemblies, and name the insulation type and thickness. Facts about the North American stock:
   - Schools, hospitals and hotels are mostly brick, stone or stucco veneer (55-64% of wall area). Large offices are mostly precast or curtain wall, and offices above about 10 storeys usually have unitized curtain wall. Warehouses are metal panel or tilt-up concrete. High-rise residential is mostly aluminum window wall.
   - Roofs are low-slope membrane over rigid board insulation for offices, schools, hospitals and retail, and metal roofs for warehouses.
   - Whole-building LCA models from this period (Tally, One Click LCA) often model roof and below-grade insulation as XPS made with HFC blowing agents. HFC-blown XPS was banned from January 2021 in Canada and in WA, CA, CO, NY and VT, and US-wide only from 2025, and tool datasets lag behind the market. When the insulation type is not known, include that case in your range, especially in colder climates where the insulation is thick.
3. Intensities. Give each component an A1-A3 intensity in kgCO2e per m2 of that component. Use these reference values from EPDs and industry baselines (A1-A3, per m2 of component):
{intensities}
   - A facade of punched windows in panel or masonry cladding has roughly half the per-m2 intensity of an all-curtain-wall facade (74 against 138 in one same-tool comparison). At R-30, legacy HFC XPS is about 195 kgCO2e per m2 of roof against about 18 for low-GWP XPS.
Complete assemblies include framing, attachments, sheathing, barriers, sealants, flashing and trim, which early-stage take-offs tend to leave out; do not go below the low end of these ranges unless the assembly is clearly minimal.
4. Check. Convert your total to kgCO2e per m2 of envelope area and check that it is consistent with the reference values above. For new construction with conventional walls and 30-40% glazing, a blended value below about 50 kgCO2e per m2 of envelope usually means that a component, the aluminum and glazing content, or a high-carbon insulation option is missing; revisit those before you finalize.
5. Bottom-up result. Divide the enclosure total by the floor area and give a bottom-up range that reflects your uncertainty about the assemblies, including the higher-carbon alternatives that are plausible for this building. A is the midpoint of that range.
6. Renovations. For renovations and tenant improvements the LCA covers only the new work, but that work often includes substantial new envelope elements (re-cladding, new curtain wall or windows, re-roofing); a renovation that re-clads has about the enclosure of a new building. Do not assume the existing envelope is kept unless the data indicates it. Use bldg_proj_type, lca_phys_scope and mass_total per floor area as evidence of how much new material was installed.

Step B. Benchmark. Median enclosure A1-A3 in reference LCAs of North American buildings with the same primary use, in kgCO2e per m2 of floor area (181 buildings assessed 2019-2024 with Tally or One Click LCA):
{benchmarks}.
Take B from bldg_prim_use alone and do not adjust it.

Step C. Combine. FINAL = 0.5 x A + 0.5 x B. Report the range from 0.8 x FINAL to 1.2 x FINAL. The midpoint of your reported range is taken as your estimate, so keep it centred on FINAL.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

End your answer with exactly three final lines in this format and nothing after them:
BOTTOM_UP_kgCO2e_per_m2: <A>
BENCHMARK_kgCO2e_per_m2: <B>
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on these lines)"""


# v5: answer-fitted (IN-SAMPLE by design; report section "Prompt v5"). The course instruction is to fit
# the reference data. Same Step A as v4; then (A7) a calibration factor K for the take-off by primary use
# and whether the envelope area is given, and (B) a benchmark by primary use and storeys. K and B are fitted
# on the reference values of all 262 cleaned buildings (analysis/fit_v5_tables.py -> results/v5_tables.json),
# so v5's coverage is in-sample. Literature passages were selected because their numbers agree with the
# fitted values (references/answer_guided_passages.md).
V5_K_TABLE = """\
   - Education: 1.05 if bldg_therm_env_area is given, 1.46 if it is not given
   - Office: 1.23 if bldg_therm_env_area is given, 1.49 if it is not given
   - Residential: Multifamily (5 or more units): 0.97 if bldg_therm_env_area is given, 1.60 if it is not given
   - Public Assembly: 1.37 if bldg_therm_env_area is given, 1.29 if it is not given
   - Laboratory: 1.81 if bldg_therm_env_area is given, 1.33 if it is not given
   - Warehouse and Storage: 0.88 if bldg_therm_env_area is given, 1.22 if it is not given
   - Healthcare: 1.35 if bldg_therm_env_area is given, 1.34 if it is not given
   - Public Order and Safety: 1.07 if bldg_therm_env_area is given, 1.02 if it is not given
   - Transportation Hub: 1.32 if bldg_therm_env_area is given, 1.44 if it is not given
   - any other use: 1.31"""
V5_B_TABLE = """\
   - Education: 1 storey 104; 2 to 5 storeys 86; 6 to 10 storeys 85; other storeys 86
   - Office: 1 storey 131; 2 to 5 storeys 82; 6 to 10 storeys 79; 11 or more storeys 72; other storeys 84
   - Residential: Multifamily (5 or more units): 2 to 5 storeys 55; 6 to 10 storeys 48; 11 or more storeys 71; other storeys 54
   - Public Assembly: 1 storey 108; 2 to 5 storeys 97; other storeys 96
   - Laboratory: 2 to 5 storeys 77; 11 or more storeys 129; other storeys 92
   - Warehouse and Storage: 1 storey 65; other storeys 65
   - Healthcare: 2 to 5 storeys 68; other storeys 73
   - Public Order and Safety: 2 to 5 storeys 160; other storeys 132
   - Transportation Hub: 2 to 5 storeys 196; other storeys 157
   - any other use: 84"""
# Passages from references/answer_guided_passages.md (selected for agreement with the fitted values).
V5_PASSAGES_K = """\
   Supporting literature:
   - "Using the early design tool (scenario ED1) gives a higher impact of 18-42% for the whole building compared to the detailed LCA approach. This is due to the additional building elements, the conservative materials estimation and the completeness of inventory" (Zimmermann et al. 2019, IOP Conf. Ser.: Earth Environ. Sci. 323, 012118).
   - "Process LCAs thus tend to systematically underestimate the emissions ... the truncation error can be even as high as 50%" (Heinonen et al. 2016, Building and Environment 95).
   - A thermally broken cladding attachment system is 24-30% of the A1-A3 GWP of a steel-stud wall with metal cladding (RDH Building Science 2025, Embodied Carbon Analysis: Spray Foam Assemblies).
   - In the harmonized North American WBLCA data, assigning tool output that had no building element raised the average Shell - Enclosure GWP by 19% (Benke et al. 2025, Scientific Data).
"""
V5_PASSAGES_B = """\
   Supporting literature:
   - Average enclosure A1-A3 in North American whole-building LCAs is 108 kgCO2e/m2 for commercial buildings and 72 for multifamily residential (Carbon Leadership Forum, EC Policy Reduction Calculator documentation); these are means, so medians are lower.
   - "The IQRs of each physical scope ... included ... Enclosure (~80-170 kgCO2e/m2)", life-cycle stages A-C (Benke et al. 2025, The Embodied Carbon Benchmark Report, Carbon Leadership Forum).
   - Facades are 15% of an average 560 kgCO2e/m2 of upfront (A1-A5) carbon in office case studies, about 84 kgCO2e/m2 (WBCSD and Arup 2021, Net-zero buildings: Where do we stand?).
   - "To meet the TGS target of 350kgCO2e/m2, the average envelope ECI should not exceed 80.5 kgCO2e/m2" for Toronto multi-unit residential buildings (BDP Quadrangle 2024).
"""
TASK_TEXT_V5 = """\
Scope. Estimate the embodied carbon of the building enclosure as classified in this dataset (OmniClass "Shell - Enclosure"), life cycle stages A1-A3 only (raw material supply, transport to the factory, manufacturing). Exclude A4, A5, B, C and D. The enclosure includes:
- exterior walls as complete assemblies: cladding, backup framing or studs, sheathing, cavity and continuous insulation, air and vapor barriers, and the interior gypsum layer of exterior walls; structural exterior walls (concrete, CMU, tilt-up) when they form the wall;
- fenestration: windows, curtain wall, storefront and skylights (frames and glass), and exterior doors;
- the roof assembly above the structural deck: insulation, cover board, membrane or roofing;
- insulation at slab edges, below grade and under slabs that belongs to the thermal envelope.
It excludes foundations, the structural frame, floor and roof decks or slabs, interior partitions and interior finishes.

How to weigh the evidence. No feature describes the wall, glazing or roof assembly, so an estimate built only from assumed assemblies is uncertain. Reference LCAs are an equally strong source. Build both estimates and give them equal weight:
- Step A, calibrated bottom-up (weight 50%): this building's own areas, likely assemblies and component intensities, then the calibration factor of Step A7.
- Step B, benchmark (weight 50%): the median enclosure result of reference LCAs with the same primary use and number of storeys.
Inside Step A, spend your attention in this order:
1. Envelope quantity (about half): bldg_therm_env_area, or storeys, height and floor area when it is missing, and bldg_wwr.
2. Assembly class (about a third): bldg_prim_use, bldg_ibc_type and the structural system indicate wood-frame, steel-stud, masonry, precast or curtain-wall construction.
3. Insulation convention (the rest): climate zone, R-values, lca_software, lca_assessment_year and the state or province decide whether HFC-blown XPS is plausible.
Leave out the seismic, wind, structural-grid, foundation, occupancy and code-year fields. In reference LCAs they do not move the enclosure value.

Special case, check it first. lca_phys_scope lists the element groups the LCA modelled: B substructure, S superstructure, E enclosure, C interior construction, F finishes. If it does not contain E, the enclosure was not modelled and only incidental items are booked under it. In that case skip Steps A to C and report BOTTOM_UP 8, CALIBRATED 8, BENCHMARK 8 and the range 6 - 10.

Step A. Bottom-up estimate. Work through these steps and show the key numbers:
1. Areas. If bldg_therm_env_area is given, use it as the total envelope area; it covers the roof, the above-grade walls and the ground-floor slab. Otherwise estimate the roof area (footprint = floor area / stories above grade), the above-grade wall area (perimeter x height) and the glazed area (bldg_wwr x wall area), plus any insulated ground-floor or below-grade area. Buildings that report an envelope area have these typical envelope-to-floor ratios: 1 storey 2.1; 2-5 storeys 1.1; 6-10 storeys 0.7; 11-15 storeys 0.5; 16 or more 0.4. Roof and ground slab are each about floor area / storeys, and the rest is wall. Typical gross wall area per m2 of floor is 0.2 for one- and two-storey schools, 0.4-0.5 for 3-6 storey offices, hotels and apartments, about 0.3 for large offices and hospitals, and 0.4 for warehouses. When bldg_wwr is missing, typical values are 0.4-0.5 for large offices, 0.2-0.3 for small offices, 0.3-0.35 for education and laboratories, 0.3 for multifamily and healthcare, 0.15-0.2 for public assembly and public safety, and 0.05 for warehouses.
2. Assemblies. From the climate zone, R-values, building use, structure, region and construction type, choose the most likely wall, glazing and roof assemblies, and name the insulation type and thickness. Facts about the North American stock:
   - Schools, hospitals and hotels are mostly brick, stone or stucco veneer (55-64% of wall area). Large offices are mostly precast or curtain wall, and offices above about 10 storeys usually have unitized curtain wall. Warehouses are metal panel or tilt-up concrete. High-rise residential is mostly aluminum window wall.
   - Roofs are low-slope membrane over rigid board insulation for offices, schools, hospitals and retail, and metal roofs for warehouses.
   - Whole-building LCA models from this period (Tally, One Click LCA) often model roof and below-grade insulation as XPS made with HFC blowing agents. HFC-blown XPS was banned from January 2021 in Canada and in WA, CA, CO, NY and VT, and US-wide only from 2025, and tool datasets lag behind the market. When the insulation type is not known, include that case in your range, especially in colder climates where the insulation is thick.
3. Intensities. Give each component an A1-A3 intensity in kgCO2e per m2 of that component. Use these reference values from EPDs and industry baselines (A1-A3, per m2 of component):
{intensities}
   - A facade of punched windows in panel or masonry cladding has roughly half the per-m2 intensity of an all-curtain-wall facade (74 against 138 in one same-tool comparison). At R-30, legacy HFC XPS is about 195 kgCO2e per m2 of roof against about 18 for low-GWP XPS.
Complete assemblies include framing, attachments, sheathing, barriers, sealants, flashing and trim, which early-stage take-offs tend to leave out; do not go below the low end of these ranges unless the assembly is clearly minimal.
4. Check. Convert your total to kgCO2e per m2 of envelope area and check that it is consistent with the reference values above. For new construction with conventional walls and 30-40% glazing, a blended value below about 50 kgCO2e per m2 of envelope usually means that a component, the aluminum and glazing content, or a high-carbon insulation option is missing; revisit those before you finalize.
5. Bottom-up result. Divide the enclosure total by the floor area and give a bottom-up range that reflects your uncertainty about the assemblies, including the higher-carbon alternatives that are plausible for this building. A is the midpoint of that range.
6. Renovations. For renovations and tenant improvements the LCA covers only the new work, but that work often includes substantial new envelope elements (re-cladding, new curtain wall or windows, re-roofing); a renovation that re-clads has about the enclosure of a new building. Do not assume the existing envelope is kept unless the data indicates it. Use bldg_proj_type, lca_phys_scope and mass_total per floor area as evidence of how much new material was installed.
7. Calibration. Reference LCAs come out higher than component take-offs like the one above, because a full model counts attachments, clips, flashing, sealants, spandrels, framing and waste that early take-offs leave out, and because LCA tools of the period used conservative generic data. When bldg_therm_env_area is not given, take-offs also tend to underestimate the envelope area. Multiply A by the factor K for this building's primary use and for whether bldg_therm_env_area is given:
{k_table}
{k_passages}CALIBRATED = K x A. Do not change K.

Step B. Benchmark. Median enclosure A1-A3 in reference LCAs of North American buildings (262 buildings assessed 2019-2024 with Tally or One Click LCA), in kgCO2e per m2 of floor area, by primary use and stories above grade. "11 or more storeys" covers 11 to 15, 16 to 20 and 21 or more. Use the "other storeys" value when this building's band is not listed:
{b_table}
{b_passages}Take B from bldg_prim_use and bldg_stories_above alone and do not adjust it.

Step C. Combine. FINAL = 0.5 x CALIBRATED + 0.5 x B. Report the range from 0.8 x FINAL to 1.2 x FINAL. The midpoint of your reported range is taken as your estimate, so keep it centred on FINAL.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

End your answer with exactly four final lines in this format and nothing after them:
BOTTOM_UP_kgCO2e_per_m2: <A>
CALIBRATED_kgCO2e_per_m2: <K x A>
BENCHMARK_kgCO2e_per_m2: <B>
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on these lines)"""


# wb5: the same answer-fitted approach applied to the course's original target, whole-building A-C ECI
# (results/ground_truth_TA_wholebuilding_A-C.csv). IN-SAMPLE by design: tables from analysis/fit_wb_tables.py
# (results/wb_tables.json). Three sources: the model's own estimate (20%), a mass route using mass_total (50%)
# and a benchmark by use and structure (30%). Weights chosen with a simulated take-off.
WB5_B_TABLE = """\
     - Education: concrete 583, steel 506, wood 426, other structure 506
     - Office: concrete 394, steel 478, wood 415, other structure 422
     - Residential: Multifamily (5 or more units): concrete 455, wood 259, other structure 373
     - Public Assembly: concrete 342, steel 529, wood 560, other structure 490
     - Laboratory: concrete 643, steel 482, other structure 513
     - Warehouse and Storage: steel 281, other structure 287
     - Healthcare: steel 521, other structure 514
     - Public Order and Safety: steel 813, other structure 765
     - Transportation Hub: steel 452, other structure 452
     - any other use: 450"""
TASK_TEXT_WB5 = """\
Scope. Estimate the whole-building embodied carbon of the building below as its reference whole-building LCA reports it: life cycle stages A to C, for the element groups listed in lca_phys_scope (B substructure, S superstructure, E enclosure, C interior construction, F finishes), in kgCO2e per m2 of floor area.

How to weigh the evidence. Build three estimates and combine them with these weights:
- Step A, your own estimate (weight 20%).
- Step M, the mass route (weight 50%): mass_total is the total mass of materials in the reference LCA, so it fixes the scale of the result.
- Step B, a benchmark (weight 30%): the median result of reference LCAs of similar buildings.

Step A. Your own estimate. Estimate each element group in lca_phys_scope from the building's use, structural system, size, storeys, region and construction type, in kgCO2e per m2 of floor area for stages A-C, and add them up. Give a range; A is its midpoint.

Step M. Mass route. Compute the material mass per m2 of floor area, mass_total / floor area, and multiply it by F, the embodied carbon per kg of material in reference LCAs of North American buildings (stages A-C, kgCO2e per kg):
   - lca_phys_scope starts with BSE (substructure, structure and enclosure all modelled): concrete structure 0.37, steel structure 0.49, wood structure 0.47, any other structure 0.44. Take the structure from the text before the colon in str_prim_vert_sys.
   - lca_phys_scope contains S but does not start with BSE: 0.68.
   - lca_phys_scope does not contain S: 1.49.
M = mass_total / floor area x F.

Step B. Benchmark. Median whole-building A-C result of reference LCAs of North American buildings (279 buildings assessed 2019-2024 with Tally or One Click LCA), in kgCO2e per m2 of floor area:
   - lca_phys_scope starts with BSE, by primary use and structure:
{wb_b_table}
   - lca_phys_scope contains S but does not start with BSE: 195.
   - lca_phys_scope does not contain S: 156.
Take B from these values and do not adjust it.

Step C. Combine. FINAL = 0.2 x A + 0.5 x M + 0.3 x B. Report the range from 0.8 x FINAL to 1.2 x FINAL. The midpoint of your reported range is taken as your estimate, so keep it centred on FINAL.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

End your answer with exactly four final lines in this format and nothing after them:
BOTTOM_UP_kgCO2e_per_m2: <A>
MASS_ROUTE_kgCO2e_per_m2: <M>
BENCHMARK_kgCO2e_per_m2: <B>
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on these lines)"""


# wb6: whole building again, built to keep the head and tail of the band figure on the curve. wb5 pulled
# every building toward the average (log-log slope 0.59): its use x structure benchmark and the model's own
# estimate are compressed. wb6 drops the benchmark, calibrates the mass route with two tables (F by structural
# system x use, K by region), gives the typical range for the building's mass intensity band and keeps the
# estimate inside it. IN-SAMPLE by design: tables from analysis/fit_wb6_tables.py (results/wb6_tables.json).
WB6_F_TABLE = """\
     - Concrete: Education 0.41; Laboratory 0.45; Office 0.33; Residential: Multifamily (5 or more units) 0.33; any other use 0.37
     - Other: any use 0.59
     - Steel: Education 0.56; Healthcare 0.48; Laboratory 0.54; Office 0.59; Public Assembly 0.52; Transportation Hub 0.54; any other use 0.53
     - Steel/Concrete: Healthcare 0.39; Office 0.33; Warehouse and Storage 0.24; any other use 0.35
     - Steel/Masonry: any use 0.44
     - Wood: Light-frame: Office 0.49; Residential: Multifamily (5 or more units) 0.46; any other use 0.46
     - Wood: Mass Timber: Education 0.50; Office 0.48; Public Assembly 0.56; any other use 0.50
     - str_sys_summary missing or not listed: 0.44"""
WB6_K_TABLE = """\
     - Canada 1.00; Eastern 1.01; Great Lakes Midwest 0.84; North Central 1.00; Pacific Northwest 1.08; Pacific Southwest 0.91; Rocky Mountains 0.99; South Central 1.01; South Eastern 0.94; any other region 1.00"""
WB6_RANGES = """\
     - below 400 kg/m2: typical 229, range 126 to 504
     - 400 to 700 kg/m2: typical 310, range 207 to 494
     - 700 to 900 kg/m2: typical 375, range 235 to 609
     - 900 to 1,100 kg/m2: typical 452, range 288 to 662
     - 1,100 to 1,300 kg/m2: typical 552, range 259 to 821
     - 1,300 to 1,600 kg/m2: typical 484, range 359 to 958
     - 1,600 to 2,000 kg/m2: typical 656, range 315 to 896
     - 2,000 kg/m2 or more: typical 719, range 425 to 1349"""
TASK_TEXT_WB6 = """\
Scope. Estimate the whole-building embodied carbon of the building below as its reference whole-building LCA reports it: life cycle stages A to C, for the element groups listed in lca_phys_scope (B substructure, S superstructure, E enclosure, C interior construction, F finishes), in kgCO2e per m2 of floor area.

Aim. The estimate should follow this building, not the average building. Buildings with a lot of material per m2 of floor area have high results and buildings with little material have low results. Do not pull a heavy building down toward the average, and do not pull a light building up. The mass route (Step M) therefore carries 90% of the estimate, and the typical range (Step R) keeps the estimate from being far too low or far too high.

Floor area: use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa.

Step R. Typical range. Compute the mass intensity, mass_total / floor area, in kg per m2 (mass_total is the total mass of materials in the reference LCA). If lca_phys_scope starts with BSE (substructure, structure and enclosure all modelled), look up the typical whole-building A-C result of reference LCAs with that mass intensity, in kgCO2e per m2 of floor area (typical = median; range = 5th to 95th percentile of 268 North American buildings assessed 2019-2024 with Tally or One Click LCA):
{ranges}
If lca_phys_scope does not start with BSE, there is no typical range.

Step A. Your own estimate. Estimate each element group in lca_phys_scope from the building's use, structural system, size, storeys, region and construction type, in kgCO2e per m2 of floor area for stages A-C, and add them up. Compare the total with the typical range from Step R. A is your estimate.

Step M. Mass route. M = mass intensity x F x K.
   F is the embodied carbon per kg of material in reference LCAs of North American buildings (stages A-C, kgCO2e per kg).
   - lca_phys_scope starts with BSE: by str_sys_summary and primary use (bldg_prim_use):
{f_table}
   - lca_phys_scope contains S but does not start with BSE: F = 0.68 and K = 1.
   - lca_phys_scope does not contain S: F = 1.49 and K = 1.
   K is a regional factor by site_region, used when lca_phys_scope starts with BSE:
{k_table}

Step C. Combine and check. FINAL = 0.9 x M + 0.1 x A. If lca_phys_scope starts with BSE and FINAL is below the low end of the range from Step R, set FINAL to that low end; if FINAL is above the high end, set FINAL to that high end. Do not move FINAL in any other way. Report the range from 0.8 x FINAL to 1.2 x FINAL. The midpoint of your reported range is taken as your estimate, so keep it centred on FINAL.

End your answer with exactly three final lines in this format and nothing after them:
BOTTOM_UP_kgCO2e_per_m2: <A>
MASS_ROUTE_kgCO2e_per_m2: <M>
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on these lines)"""


# wb1: whole building A-C, the model alone ("innate"): the same target and scope sentence as wb5/wb6, but no
# mass route, no benchmark and no typical range. Same idea as the course's innate prompt; numeric examples are
# left out of the instructions so that nothing anchors the estimate.
TASK_TEXT_WB1 = """\
Scope. Estimate the whole-building embodied carbon of the building below as its reference whole-building LCA reports it: life cycle stages A to C, for the element groups listed in lca_phys_scope (B substructure, S superstructure, E enclosure, C interior construction, F finishes), in kgCO2e per m2 of floor area.

Provide a plausible range (a range, not a single value), using your own knowledge. For floor area, use bldg_cfa. If bldg_cfa is not provided, use bldg_renovated_gfa + bldg_added_gfa. Briefly state your method and key assumptions.

End your answer with exactly one final line in this format and nothing after it:
RANGE_kgCO2e_per_m2: <low> - <high>
(plain numbers only, no units or other text on that line)"""

TASK_TEXTS = {"v1": TASK_TEXT_V1, "v2": TASK_TEXT_V2,
              "v3": TASK_TEXT_V3.format(intensities=V3_INTENSITIES),
              "v4": TASK_TEXT_V4.format(intensities=V3_INTENSITIES, benchmarks=V4_BENCHMARKS),
              "v5": TASK_TEXT_V5.format(intensities=V3_INTENSITIES, k_table=V5_K_TABLE, b_table=V5_B_TABLE,
                                        k_passages=V5_PASSAGES_K, b_passages=V5_PASSAGES_B),
              "wb5": TASK_TEXT_WB5.format(wb_b_table=WB5_B_TABLE),
              "wb6": TASK_TEXT_WB6.format(ranges=WB6_RANGES, f_table=WB6_F_TABLE, k_table=WB6_K_TABLE),
              "wb1": TASK_TEXT_WB1}
TASK_TEXT = TASK_TEXTS[PROMPT_VERSION]

# Instructions given to each Claude Code subagent (the "LLM under test"). {placeholders} are
# filled by subagent_runs.py prepare. ANSWER_LENGTH and FINAL_LINES follow the prompt version.
ANSWER_LENGTH = {"v1": "briefly state your method and key assumptions (roughly 60-150 words)",
                 "v2": "work through its method steps with the key numbers (roughly 120-250 words)",
                 "v3": "work through its method steps with the key numbers (roughly 120-250 words)",
                 "v4": "work through Steps A, B and C with the key numbers (roughly 120-250 words)",
                 "v5": "work through Steps A, B and C with the key numbers (roughly 120-250 words)",
                 "wb5": "work through Steps A, M, B and C with the key numbers (roughly 100-200 words)",
                 "wb6": "work through Steps R, A, M and C with the key numbers (roughly 100-200 words)",
                 "wb1": "briefly state your method and key assumptions (roughly 60-150 words)"}[PROMPT_VERSION]
FINAL_LINES = {"v1": "the final line `RANGE_kgCO2e_per_m2: <low> - <high>`",
               "v2": "the two final lines `BEST_kgCO2e_per_m2: <value>` and "
                     "`RANGE_kgCO2e_per_m2: <low> - <high>`",
               "v3": "the final line `RANGE_kgCO2e_per_m2: <low> - <high>`",
               "v4": "the three final lines `BOTTOM_UP_kgCO2e_per_m2: <A>`, `BENCHMARK_kgCO2e_per_m2: <B>` and "
                     "`RANGE_kgCO2e_per_m2: <low> - <high>`",
               "v5": "the four final lines `BOTTOM_UP_kgCO2e_per_m2: <A>`, `CALIBRATED_kgCO2e_per_m2: <K x A>`, "
                     "`BENCHMARK_kgCO2e_per_m2: <B>` and `RANGE_kgCO2e_per_m2: <low> - <high>`",
               "wb5": "the four final lines `BOTTOM_UP_kgCO2e_per_m2: <A>`, `MASS_ROUTE_kgCO2e_per_m2: <M>`, "
                      "`BENCHMARK_kgCO2e_per_m2: <B>` and `RANGE_kgCO2e_per_m2: <low> - <high>`",
               "wb6": "the three final lines `BOTTOM_UP_kgCO2e_per_m2: <A>`, `MASS_ROUTE_kgCO2e_per_m2: <M>` and "
                      "`RANGE_kgCO2e_per_m2: <low> - <high>`",
               "wb1": "the final line `RANGE_kgCO2e_per_m2: <low> - <high>`"}[PROMPT_VERSION]
CONTEXT_DESC = ("a glossary of the feature names and four reference documents on enclosure embodied carbon"
                if INCLUDE_ENVELOPE_DOCS else
                "a glossary of the feature names and the task, which is the question asked for every building"
                if TASK_TEXT_ONCE else "a glossary of the feature names")
BLOCK_DESC = "the building's features" if TASK_TEXT_ONCE else "the building's features and the question"
KNOWLEDGE = ("your own knowledge and the reference documents included in the task file"
             if INCLUDE_ENVELOPE_DOCS or INCLUDE_PAPERS else
             "your own knowledge and the reference values given in the task" if PROMPT_VERSION in ("v4", "v5", "wb5", "wb6")
             else "your own knowledge")
SUBAGENT_INSTRUCTIONS = """\
You are the language model being tested in a building life-cycle-assessment (LCA) experiment for a university course project. Your job is to answer a set of estimation prompts using only {knowledge}.

Input file: {task_file}
It is about {n_lines:,} lines, so read all of it with the Read tool, using offset/limit to page past line 2,000. It contains a System line, a shared context ({context_desc}), and {n_buildings} building sections. Each section starts with a line like `===== KEY: {example_key} =====`, followed by {block_desc}.

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
                 "v2": "BEST_kgCO2e_per_m2: 55\nRANGE_kgCO2e_per_m2: 40 - 75",
                 "v3": "RANGE_kgCO2e_per_m2: 40 - 75",
                 "v4": "BOTTOM_UP_kgCO2e_per_m2: 60\nBENCHMARK_kgCO2e_per_m2: 79\nRANGE_kgCO2e_per_m2: 56 - 83",
                 "v5": "BOTTOM_UP_kgCO2e_per_m2: 60\nCALIBRATED_kgCO2e_per_m2: 80\nBENCHMARK_kgCO2e_per_m2: 86\n"
                       "RANGE_kgCO2e_per_m2: 66 - 100",
                 "wb5": "BOTTOM_UP_kgCO2e_per_m2: 420\nMASS_ROUTE_kgCO2e_per_m2: 470\nBENCHMARK_kgCO2e_per_m2: 456\n"
                        "RANGE_kgCO2e_per_m2: 362 - 543",
                 "wb6": "BOTTOM_UP_kgCO2e_per_m2: 430\nMASS_ROUTE_kgCO2e_per_m2: 512\nRANGE_kgCO2e_per_m2: 403 - 605",
                 "wb1": "RANGE_kgCO2e_per_m2: <low> - <high>"}[PROMPT_VERSION]


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
    if INCLUDE_ENVELOPE_DOCS:
        missing = [p.name for p in ENVELOPE_DOC_PATHS if not p.exists() or p.stat().st_size < 1000]
        if missing:
            raise SystemExit(f"Envelope documents missing: {missing}. Run scripts/fetch_envelope_docs.sh")
        docs = "\n\n".join(f"--- Document: {p.stem} ---\n{read_pdf(p, MAX_ENVELOPE_DOC_CHARS)}"
                            for p in ENVELOPE_DOC_PATHS)
        parts.append("These documents contain background information about the embodied carbon of "
                     "building enclosures (wall assemblies, insulation, glazing, windows and material "
                     f"baselines):\n\n{docs}")
    for p in EXTRA_CONTEXT_PATHS:
        parts.append(f"Additional reference ({p.name}):\n\n{p.read_text(encoding='utf-8')}")
    parts.append("Reference the given feature information above. Estimate the embodied carbon of "
                 "the building enclosure of the building below:")
    if TASK_TEXT_ONCE:
        parts.append("## Task (the same question is asked for every building below)\n\n" + TASK_TEXT)
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
    if TASK_TEXT_ONCE:
        return building_text
    return f"{building_text}\n\n{TASK_TEXT}"


def settings() -> dict:
    return {
        "condition": CONDITION,
        "prompt_version": PROMPT_VERSION,
        "task_text_once": TASK_TEXT_ONCE,
        "include_papers": INCLUDE_PAPERS,
        "papers": [p.name for p in PAPER_PATHS] if INCLUDE_PAPERS else [],
        "include_practice_guide": INCLUDE_PRACTICE_GUIDE,
        "extra_context": [p.name for p in EXTRA_CONTEXT_PATHS],
        "envelope_docs": ([p.name for p in ENVELOPE_DOC_PATHS] if INCLUDE_ENVELOPE_DOCS else []),
        "max_envelope_doc_chars": MAX_ENVELOPE_DOC_CHARS if INCLUDE_ENVELOPE_DOCS else None,
        "features": FEATURES,
        "feature_set": next((k for k, v in FEATURE_SETS.items() if v == FEATURES), "custom"),
        "system_prompt": SYSTEM_PROMPT,
        "task_text": TASK_TEXT,
        "subagent_instructions": SUBAGENT_INSTRUCTIONS,
    }
