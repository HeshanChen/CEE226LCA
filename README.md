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

```bash
python summarize_run.py 20261104_baseline-innate
```

## Files

| File | Purpose |
|---|---|
| `experiment_config.py` | **The only file to edit per condition**: knowledge switches, feature subset, prompt text |
| `subagent_runs.py` | `prepare` task files for subagents, `collect` their answers into `project-#_runs.csv` |
| `GWP-calculation/sum_gwp.py` | Filters `full_lca_results.xlsx` by element and stage, sums GWP, writes the ground truth |
| `LLM-data-cleaning.py` | Per-project mean estimate, error, RMSE (course script) |
| `make_fig1_bands.py` | ±20% band figure and inside/above/below counts (course script; ticks extended below 10) |
| `analysis/make_split.py`, `analysis/compare_runs.py` | Held-out dev/test split; metrics and paired tests (McNemar, Wilcoxon) per split |
| `summarize_run.py` | Proposal metrics (RMSE, MAPE, median APE, ±20% coverage, CV across runs), overall and by climate zone / primary use, plus `fig2_estimate_vs_truth.png` and `fig3_ratio_by_group.png` |
| `results/ground_truth.csv` | Enclosure A1–A3 ground truth (with total GWP and floor area columns) |
| `results/ground_truth_TA_wholebuilding_A-C.csv` | The course's whole-building A–C ground truth, kept for comparison |
| `references/` | Building metadata (48 features), glossary, CLF practice guide, A–C benchmarks |
| `scripts/fetch_reference_pdfs.sh` | Downloads the 4 background papers (not re-hosted here: publisher copyright) |
| `gemini_lca_batch.py`, `gemini_lca_project_runs.py` | Course Gemini runners. **Not used** in this project; they still carry the whole-building A–C prompt |

## Notes on the course reference repo

- `references/4.pdf` on its `main` branch is an empty 2-byte file. The intended paper (Rezaei et al., 2019) is in its history as `5.pdf`, and `scripts/fetch_reference_pdfs.sh` gets that one.
- `GWP-calculation/full_lca_results.pkl` there is also a 2-byte placeholder. If its timestamp is newer than the downloaded Excel file, `sum_gwp.py` tries to load it as a cache and fails. Delete it before running.
- The course prompt says "use bldg_renovated_cfa + bldg_renovated_gfa", but there is no `bldg_renovated_cfa` column. The dataset normalizes renovations by `bldg_renovated_gfa + bldg_added_gfa`, and the prompt here says that.
- The two course Gemini runners had drifted apart: batch sends papers + benchmarks, project-runs sends papers + practice guide. Here a single `experiment_config.py` defines the prompt.

## Report

**[`report/report.md`](report/report.md)** covers the data, setup, baseline, error analysis (why the model under- and overestimates), and the prompt v2 design and results. The final prompt is in [`report/appendix_prompts.md`](report/appendix_prompts.md), generated from `experiment_config.py`.

## Experiment log

| Iteration | Run folder | Condition | Runs | ±20% coverage | RMSE | median APE | CV across runs |
|---|---|---|---|---|---|---|---|
| pilot | `20261104_pilot-sonnet_run0-chunk01` | Sonnet 5.5 subagent, 49 buildings, pipeline test only | 49 × 1 | 36.7% | 62.2 | 31% | n/a |
| 0 | `20261104_baseline-innate` | **Baseline**: Opus 5.5 subagents (effort medium), innate knowledge, all 48 features, no papers, no ontology | 292 × 3 | **19.5%** (95% CI 15.4–24.5%) | **79.7** | **37.9%** | **19.0%** |
| 1 | `20261104_prompt-v2` | Prompt v2 (scope matching the dataset, component take-off, named high-impact materials, no anchoring, renovation rule, BEST line), same model and features | 292 × 3 | 15.1% (11.4–19.6%) | 81.0 | 44.3% | **13.8%** |
| 2 | `20261104_prompt-v3` | **Prompt v3 (final)**: v2 + external component-intensity table (`references/envelope_intensities_sources.md`), HFC-XPS modelling convention, per-envelope check, non-subtracting renovation rule, RANGE only | 292 × 3 | **25.0%** (20.4–30.3%) | **76.0** | 40.0% | **12.5%** |
| 3 | `20261105_feat-*`, `20261105_ablate-no-*` | Feature study with prompt v3 (run 0 only): early (39), env (15), min (10), no-lca (40), no-mass (47) vs all 48 | 292 × 1 each | 19.9–25.3% (all: 24.3%) | 77.3–81.2 | – | – |

### Feature study

Every feature set gives the same accuracy as all 48 features, within the run-to-run spread of prompt v3. The 10-feature early-design set (`min`) is as good as the full set, and removing `mass_total` or the LCA-derived fields does not hurt. See report Section 10, `analysis/feature_study.md` and `analysis/figures/feature_study.png`.

### Held-out test set

`analysis/make_split.py` (seed 226) holds out 88 of the 292 projects as a test set, stratified by project type × climate group. On test: v1 20.5% coverage / RMSE 74.1, v2 18.2% / 75.7, **v3 26.1% / 69.2** (bias 0.86, CV 11.2%). The v1–v3 difference is not significant at n = 88 (McNemar p = 0.41). The split was assigned after the runs, and every finding behind the prompt revisions replicates on the 204 dev projects alone. See report Section 9 and `analysis/compare_*.md`.

### Baseline findings (iteration 0)

All 876 answers parsed (292 buildings × 3 runs). Full tables are in `results/20261104_baseline-innate/summary.md`, and figures in `results/20261104_baseline-innate/figures/`.

- **Systematic underestimate.** The geometric mean of estimate/true is 0.75, and the median estimate is 56 against a true median of 78 kgCO2e/m². For 63% of buildings, the true value lies above the ±20% band.
- **Compressed range.** Estimates span 1.7–168 kgCO2e/m² (SD 30.7 across buildings), while true values span 0.5–514 (SD 78.0). The model pulls every building toward about 50–100, so it misses high-carbon enclosures.
- **Climate pattern.** Underestimation is larger in cold zones (5A 0.68×, 5B 0.65×, 7 0.57×, 2B 0.45×) than in warm marine and dry zones (3C 1.10×, 3B 0.94×). One hypothesis to test in iteration 1: insulation is the largest enclosure A1–A3 contributor in this dataset (26% of GWP, ahead of aluminum at 22%), and the model may underweight it.
- **Use pattern.** Healthcare (1.14×) and multifamily (0.79×) come closest. Transportation hubs (0.56×) and public order and safety (0.66×) are underestimated most.
- **Near-zero renovations are handled well.** Tenant fit-outs and minor renovations with a true value of 0.5–7 often received "0 – 5" style answers. See the parser note in `subagent_runs.py`.
- These numbers are **not comparable** to the course whole-building A–C results (34–46% coverage), because the scope (enclosure A1–A3) and the model differ.

### Method notes for the report

- The LLM is a Claude Code subagent, not an API call. Each subagent answers 48–49 buildings in one context, and buildings are shuffled with a different seed for each run. The prompt asks the model to treat every building independently and to read only its task file, with no web access or code. Separate API calls would be fully independent; this setup is not.
- The functional unit is per m² of **floor area** (the dataset's normalization), not per m² of wall as in the proposal. The enclosure element also includes windows, doors and roofing.
