# Climate- and Use-Specific Embodied Impacts of Exterior Wall Design

**A Comparative LCA and Implications for LEED v5 Embodied Carbon Credits.** CEE226 Group 8: George Zheng, Zixuan Zhao, Heshan Chen, Fei Cheng, Jamie Liu.

This repo tests how well an LLM can estimate the **embodied carbon of the building enclosure** from early-stage building metadata. It compares the estimates against the reference LCA results of the 292 buildings in the CLF harmonized dataset (Benke et al., 2025, *Scientific Data*, [doi:10.1038/s41597-025-05216-0](https://doi.org/10.1038/s41597-025-05216-0); data on [figshare](https://figshare.com/articles/dataset/28462145), CC BY 4.0).

It started from the course reference code, [eunicehjung/CEE226-BuildingLCA-LLM](https://github.com/eunicehjung/CEE226-BuildingLCA-LLM). That code covers the whole building over stages A–C. This repo narrows the scope as described below.

## Scope

| | Course reference | This project |
|---|---|---|
| Elements | all elements | **Shell - Enclosure** (OmniClass): exterior walls, cladding, windows, curtain wall, doors, roofing, insulation |
| Life cycle stages | A1–A3, A4, B4–B5, C2–C4 | **A1–A3** (cradle-to-gate) |
| Unit | kgCO2e / m² floor area | kgCO2e / m² floor area |
| Floor area | `bldg_cfa`, or renovated + added GFA | same (it matches the dataset's own `eci_a_to_c_cfa` for all 292 projects) |

Ground truth (`results/ground_truth.csv`, 292 projects): median 78.0, mean 95.6, range 0.49–513.9 kgCO2e/m². The enclosure share of the whole-building A–C value has a median of 19%.

## Pipeline

```bash
pip install pandas openpyxl PyPDF2 matplotlib scipy
```

**1. Ground truth**: needed only if the scope changes, because `results/ground_truth.csv` is already committed. Download `full_lca_results.xlsx` from figshare into `GWP-calculation/`, set `ELEMENTS` / `STAGES` in `GWP-calculation/sum_gwp.py`, then run:

```bash
python GWP-calculation/sum_gwp.py
```

It writes the per-project totals and `results/ground_truth.csv` (kgCO2e/m²).

**2. LLM estimates (Claude Code subagents).** Set the condition in `experiment_config.py`: papers on or off, extra context, feature subset, prompt text. Then run:

```bash
python subagent_runs.py prepare --run-name 20261104_baseline-innate --runs 3
```

This writes one task file per subagent to `results/<run>/subagent/tasks/`. Each task file holds the shared context and 48–49 buildings, and each run shuffles the buildings with its own seed. Claude Code then starts one subagent per task file. The subagent answers from its own knowledge only and writes its answers to `results/<run>/subagent/answers/`. To collect them:

```bash
python subagent_runs.py collect --run-name 20261104_baseline-innate
```

This parses every answer with the same `RANGE_kgCO2e_per_m2: low - high` parser as the Gemini scripts. It writes `results/<run>/project-#_runs.csv` in the course format.

**3. Data cleaning and figure**: unchanged course scripts.

```bash
python LLM-data-cleaning.py 20261104_baseline-innate
```

```bash
python make_fig1_bands.py 20261104_baseline-innate
```

## Files

| File | Purpose |
|---|---|
| `experiment_config.py` | **The only file to edit per condition**: knowledge switches, feature subset, prompt text |
| `subagent_runs.py` | `prepare` task files for subagents, `collect` their answers into `project-#_runs.csv` |
| `GWP-calculation/sum_gwp.py` | Filters `full_lca_results.xlsx` by element and stage, sums GWP, writes the ground truth |
| `LLM-data-cleaning.py` | Per-project mean estimate, error, RMSE (course script) |
| `make_fig1_bands.py` | ±20% band figure and inside/above/below counts (course script; ticks extended below 10) |
| `results/ground_truth.csv` | Enclosure A1–A3 ground truth (with total GWP and floor area columns) |
| `results/ground_truth_TA_wholebuilding_A-C.csv` | The course's whole-building A–C ground truth, kept for comparison |
| `references/` | Building metadata (49 features), glossary, CLF practice guide, A–C benchmarks |
| `scripts/fetch_reference_pdfs.sh` | Downloads the 4 background papers (not re-hosted here: publisher copyright) |
| `gemini_lca_batch.py`, `gemini_lca_project_runs.py` | Course Gemini runners. **Not used** in this project; they still carry the whole-building A–C prompt |

## Notes on the course reference repo

- `references/4.pdf` on its `main` branch is an empty 2-byte file. The intended paper (Rezaei et al., 2019) is in its history as `5.pdf`, and `scripts/fetch_reference_pdfs.sh` gets that one.
- `GWP-calculation/full_lca_results.pkl` there is also a 2-byte placeholder. If its timestamp is newer than the downloaded Excel file, `sum_gwp.py` tries to load it as a cache and fails. Delete it before running.
- The course prompt says "use bldg_renovated_cfa + bldg_renovated_gfa", but there is no `bldg_renovated_cfa` column. The dataset normalizes renovations by `bldg_renovated_gfa + bldg_added_gfa`, and the prompt here says that.
- The two course Gemini runners had drifted apart: batch sends papers + benchmarks, project-runs sends papers + practice guide. Here a single `experiment_config.py` defines the prompt.

## Experiment log

| Iteration | Condition | Runs | Status |
|---|---|---|---|
| 0 | Baseline: innate knowledge, all 49 features, no papers, no ontology | 292 × 3 | in progress |
| 1 | + envelope-focused papers in place of the whole-building PDFs | | planned |
| 2 | Feature study: full set vs. envelope-relevant subsets | | planned |
