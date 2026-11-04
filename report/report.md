# Can an LLM Estimate the Embodied Carbon of a Building Enclosure? Error Analysis and Prompt Design

CEE226 Group 8: George Zheng, Zixuan Zhao, Heshan Chen, Fei Cheng, Jamie Liu.
Part of the project *Climate- and Use-Specific Embodied Impacts of Exterior Wall Design: A Comparative LCA and Implications for LEED v5 Embodied Carbon Credits*.

> Status: draft. Sections 1–6 are complete. Section 7 (prompt v2 results) is filled in when the v2 run finishes.
> Every number in this report can be regenerated with the commands in Appendix B.

## 1. Summary

The LLM in this study is Claude Opus 5.5, run as a Claude Code subagent with medium reasoning effort. Given the 49 early-stage features of each of the 292 buildings in the CLF harmonized WBLCA dataset, it estimated the **cradle-to-gate (A1–A3) embodied carbon of the building enclosure**, in kgCO2e per m² of floor area.

With a plain prompt (v1, innate knowledge), only **19.5%** of the estimates land within ±20% of the reference LCA. RMSE is 79.7 kgCO2e/m² and the median absolute percentage error is 37.9%.

The error is not random. The model:

1. compresses every building toward a "typical" value of about 50–60 kgCO2e/m²;
2. misses the single largest material driver in the data, HFC-blown XPS insulation;
3. underestimates envelope area when it is not given;
4. misjudges renovations.

Its largest overestimates are mostly cases where the reference LCA itself is incomplete.

From this analysis we wrote prompt v2. It defines the enclosure the way the dataset classifies it, requires a component-by-component take-off, names the high-impact materials, forbids anchoring on a typical value, adds renovation guidance, and asks for a best estimate. The final prompt is in Section 6 and Appendix A. Its results are in Section 7.

## 2. Data and ground truth

**Source.** Benke et al. (2025), *A Harmonized Dataset of High-Resolution Embodied Life Cycle Assessment Results for Buildings in North America*, Scientific Data ([doi:10.1038/s41597-025-05216-0](https://doi.org/10.1038/s41597-025-05216-0); data on [figshare](https://figshare.com/articles/dataset/28462145), CC BY 4.0). The `full_lca_results.xlsx` file has 927,950 rows, one per material, element and life cycle stage, covering 292 projects.

**Scope.** We kept OmniClass element `Shell - Enclosure` and stage `A1-A3` (`GWP-calculation/sum_gwp.py`). That leaves 55,807 rows.

**Normalization.** The total GWP is divided by floor area: `bldg_cfa` for new construction, and `bldg_renovated_gfa + bldg_added_gfa` for the 49 renovations. This matches the dataset's own `eci_a_to_c_cfa` for all 292 projects. Note the difference from the proposal's functional unit (1 m² of wall): the dataset gives no wall area for most projects, and its enclosure element also includes windows, doors and roofs.

**Distribution.** The ground truth (`results/ground_truth.csv`) has a median of 78.0 kgCO2e/m², a mean of 95.6, and a range of 0.49–513.9. The 5th–95th percentile range is 10.5–255.7. The enclosure is a median 19% of the whole-building A–C total.

**What the enclosure carbon is made of** (share of all enclosure A1–A3 GWP; `GWP-calculation/enclosure_breakdown.py`):

| Material group | Share | Largest item |
|---|---|---|
| Insulation | 26.4% | XPS 15.5% of the enclosure total (59% of insulation) |
| Aluminum | 22.0% | extrusions 17.4% |
| Windows and frames | 9.7% | aluminum storefront / curtain wall 7.3% |
| Concrete | 8.9% | precast 3.4% |
| Glazing | 7.8% | IGU 4.0% |
| Steel | 6.6% | cold-formed framing 2.9% |
| Cladding | 6.5% | ACM 2.3% |
| Masonry | 5.0% | brick 1.9% |

XPS in this dataset carries **43.6 kgCO2e/kg**, against 1.2 for high-density mineral wool, 2.4 for fiberglass and 3.1 for polyiso. This is consistent with XPS made with HFC blowing agents, which the LCA tools of the assessment years (Tally, One Click LCA) modelled. 149 of the 292 projects contain XPS.

**Data-quality flag.** 10 new-construction projects (27, 35, 66, 74, 80, 91, 141, 217, 234, 264) have **no window, glazing, curtain wall or storefront GWP at all** in their enclosure inventory. Some of them report a WWR of 0.5–0.7. Project 74, for example, has WWR 0.65 and a true value of 0.64 kgCO2e/m². These look like incomplete source LCA models rather than real buildings with glass-free envelopes. They are kept in every headline metric, for comparability, and also reported separately ("excl. incomplete").

## 3. LLM experiment setup

- **Model.** Claude Opus 5.5, run as Claude Code subagents with reasoning effort *medium*. The course reference code uses the Gemini API, which we did not use. A pilot with Sonnet 5.5 (49 buildings, 1 run) only tested the pipeline.
- **Inputs.** All 49 features of `references/buildings_metadata_LLM.xlsx`, plus the feature glossary. No papers, no benchmark tables and no ontology, i.e. the innate-knowledge condition.
- **Protocol.** 292 buildings × 3 runs = 876 estimates per prompt version. Each subagent answers one task file: the shared context plus 48–49 buildings. For each run, the buildings are shuffled with a fixed seed (1000 + run index) and split into 6 chunks. v1 and v2 use identical chunks, so results can be compared building by building.
- **Isolation.** A subagent may read only its task file and write only its answer files. It may not use web search, run code, or open any other file, so it cannot see the ground truth. Unlike separate API calls, the buildings in one task file share a context. The instructions ask the model to treat each building independently, and the per-run shuffle changes each building's neighbours from run to run.
- **Parsing.** We use the course parser (`RANGE_kgCO2e_per_m2: low - high`, last match wins), with one change: a lower bound of 0 is accepted. In v1, 11 answers for renovations and tenant fit-outs had a lower bound of 0 (for example "0 – 5"). These projects have true values of 2.6–26 kgCO2e/m², 10 of them below 14, so the course parser would have discarded exactly the low-carbon cases. Prompt v2 adds a `BEST_kgCO2e_per_m2` line.
- **Metrics.** The estimate for a building is the mean of its run midpoints. Accuracy is measured by ±20% coverage (truth within estimate ±20%, Wilson 95% CI), RMSE, MAE, MAPE, median APE, and the geometric mean of estimate/true (bias). Consistency is the coefficient of variation across runs. Results are also broken down by climate zone and primary use (RQ1). Scripts: `LLM-data-cleaning.py`, `make_fig1_bands.py`, `summarize_run.py`, `analysis/error_analysis.py`.

## 4. Baseline results (prompt v1)

All 876 answers parsed (`results/20261104_baseline-innate/`).

| Subset | n | ±20% coverage | RMSE | median APE | est/true (geo-mean) | CV across runs |
|---|---|---|---|---|---|---|
| All projects | 292 | 19.5% (CI 15.4–24.5%) | 79.7 | 37.9% | 0.75 | 19.0% |
| New construction | 243 | 18.9% | 77.4 | 37.5% | 0.76 | 17.3% |
| Excl. 10 incomplete ground truths | 282 | 20.2% | 80.5 | 37.3% | 0.72 | 19.1% |

For 63% of buildings the truth lies above the ±20% band (underestimate), and for 17.5% below it.

Figures: `results/20261104_baseline-innate/figures/fig1_bands_sorted.png` (bands), `fig2_estimate_vs_truth.png` (scatter), `fig3_ratio_by_group.png` (climate and use).

These results cannot be compared with the course's whole-building A–C results (34–46% coverage with Gemini). The scope, the model and the ground truth all differ.

## 5. Error analysis: why the model under- and overestimates

Source: `analysis/error_analysis_20261104_baseline-innate.md`, plus the per-material ground truth and the 876 reasoning texts.

### 5.1 The dominant pattern is compression, not uniform underestimation

| True value (kgCO2e/m²) | n | median est/true |
|---|---|---|
| < 25 | 36 | 1.58 (overestimate) |
| 25–50 | 43 | 1.09 |
| 50–100 | 114 | 0.76 |
| 100–200 | 72 | 0.54 |
| > 200 | 27 | 0.28 |

- The log–log slope of estimate on truth is **0.46**. A doubling of the true value raises the estimate by only about 37%.
- The SD of the estimates across buildings is 0.39 of the SD of the truth.
- The estimates span 1.7–168 kgCO2e/m²; the truth spans 0.5–514.
- Midpoints cluster at 42–62 kgCO2e/m².
- The 20 buildings with the largest errors contribute 68% of the squared error, and all 20 are underestimates.

The model leans on geometry more than the data justifies. The envelope-to-floor-area ratio correlates 0.62 with the log estimate but only 0.39 with the log truth, and mass per floor area 0.68 against 0.53. What it misses is the intensity per m² of envelope. In the truth this ranges from 19 to 278 kgCO2e per m² of envelope (5th–95th percentile); in the estimates, from 20 to 144. This intensity alone correlates −0.79 with the log error. It is set by material and assembly choice, and **none of the 49 features describes the wall assembly**.

### 5.2 Why the model underestimates

1. **HFC-blown XPS is the largest single cause, and the model never considers it.**
   - XPS is 15.5% of all enclosure carbon and appears in 149 projects. Yet the model mentions XPS in 0.6% of its answers (0.7% for projects that contain XPS), and HFC blowing agents in none.
   - Median est/true is 0.67 for projects with XPS against 0.80 without, and 0.59 where XPS is more than 30% of the truth.
   - With XPS removed from the truth, the median est/(truth − XPS) rises from 0.72 to 0.84. **XPS explains roughly half of the systematic underestimate.**
   - Example, project-198 (lodging, zone 4C): the true value is 361.8, of which XPS is 325.9. The model's take-off assumed a ~30 kgCO2e/m² roof and estimated 22–36.

2. **XPS also explains the climate pattern.**
   - Median est/true is 0.65 in cold zones (5–8) against 0.77 in warm zones (1–3).
   - XPS is present in 65–68% of projects in zones 5A and 5B (est/true 0.64–0.65), but in only 26–33% in zones 3B and 3C (0.83–0.86). Cold climates need more insulation, so an HFC-blown XPS layer weighs more.
   - The climate signal is therefore an insulation-material effect, not evidence that the model ignores climate.

3. **When the envelope area is missing, the model's own take-off is too small.**
   - `bldg_therm_env_area` is given for 160 projects. With it, median est/true is 0.81; without it, 0.65.
   - The gap is largest for tall buildings: 0.24 against 0.67 for 21+ storeys.
   - Example, project-198: the model assumed an envelope-to-floor ratio of about 0.6 for a 2–5 storey building. The median in the data for 2–5 storeys is 1.07, probably because the dataset's thermal envelope area includes the ground floor.

4. **Aluminum curtain wall has a heavy tail.**
   - Aluminum is 22% of the total. Single projects reach 300 kgCO2e/m² of floor area from curtain wall alone.
   - Example, project-137 (office, minor renovation): the true value is 513.9, of which 302 is new curtain wall. The model reasoned that a minor renovation keeps the existing curtain wall and estimated 35.

5. **Renovations are scoped too narrowly.**
   - 60% of major renovations are underestimated, and tenant improvements reach est/true 0.24. The model tends to assume the existing envelope stays.
   - The feature that measures how much new material was installed, `mass_total` per floor area (correlation 0.53 with the truth), is used in only 8.6% of answers.

6. **The v1 scope text was narrower than the dataset's enclosure.**
   - In the harmonized data, 11% of enclosure GWP was tagged "Superstructure" in the source tool (mostly roof XPS/PIR and roofing), and 9.6% "Undefined".
   - Exterior-wall framing, sheathing, interior gypsum on exterior walls, and slab-edge and below-grade insulation are also in the enclosure.
   - The v1 scope ("exterior walls and cladding, windows, curtain walls, doors, roofing, and their insulation") left much of this to interpretation.

### 5.3 Why the model overestimates

1. **Incomplete reference LCAs.** The 10 flagged new-construction projects with no fenestration GWP have a median est/true of 3.09. The model's answers for them are reasonable buildings; the reference is not. Project-74, for example, has WWR 0.65, a model estimate of 62, and a truth of 0.64.
2. **Little new enclosure work.** Below a truth of 25 kgCO2e/m² (median est/true 1.58), most projects are tenant improvements and minor renovations. The features do not say how much of the envelope was replaced.

### 5.4 Ruled out

R-values, WWR, building size, completion year and `lca_ec_reductions` each correlate weakly with the error (|r| ≤ 0.26). Consistency across runs is acceptable: the median CV is 17%, the mean 19%.

## 6. Prompt v2

The v2 task text replaces v1. The system prompt and the shared context (glossary) are unchanged, and so are the model, effort, features, seeds and chunks. Full text: Appendix A, section D.

| Baseline finding (Section 5) | Prompt v2 change |
|---|---|
| 5.2.6: scope narrower than the dataset's enclosure | Scope written out to match the dataset: complete wall assemblies (cladding, framing, sheathing, insulation, barriers, interior gypsum), fenestration, the roof assembly above the deck, slab-edge and below-grade insulation; explicit exclusions |
| 5.1: geometry used, intensity guessed; 5.2.3: envelope area underestimated | Required method: (1) areas from `bldg_therm_env_area`, or a take-off with the envelope-to-floor ratio stated; (2) assemblies with insulation type and thickness; (3) a component intensity per m²; (4) sum and divide |
| 5.2.1–5.2.2: XPS missed, climate pattern; 5.2.4: curtain wall tail | Named high-impact materials: HFC-blown XPS (about 10× or more the GWP of mineral wool, fiberglass or polyiso per unit of thermal resistance), aluminum curtain wall (about 100–200 kgCO2e/m² of facade), IGU, precast, masonry |
| 5.1: compression toward a typical value | "Do not pull the estimate toward a typical building", with both tails named (> 200 and < 10 kgCO2e/m²) |
| 5.2.5, 5.3.2: renovations | Count only new materials; judge the extent of work from `bldg_proj_type`, `lca_phys_scope` and `mass_total` per floor area |
| Midpoint of a wide range used as the estimate (median relative range width 0.75) | `BEST_kgCO2e_per_m2` line before the `RANGE` line (RANGE stays last, so the course parser still works) |

**Sources for the material statements.** The XPS statement is qualitative and supported by external sources:
- The Alberta *PERSIST* insulation guide reports that XPS has the highest embodied GWP of common board insulations because of its HFC blowing agent ([alberta.ca](https://www.alberta.ca/system/files/custom_downloaded_images/tr-dtseries06insul2016.pdf)).
- Vermont's draft R408 embodied-carbon table lists XPS (HFC) at 55.5, against 1.7 for mineral wool batt and 4.1 for polyiso board ([publicservice.vermont.gov](https://publicservice.vermont.gov/sites/dps/files/documents/SECTION%20R408%20Insulation%20Embodied%20Carbon%20Calculation_DRAFT.pdf)).

The curtain wall range rests on aluminum-framed curtain wall EPDs, which report 117–134 kgCO2e/m² for A1–A3 ([One Click LCA EPD library](https://materials.oneclicklca.com/en/material/aluminium-framed-curtain-wall-system-double-glazed/661cc76cdc501e436af96490)). Arup's facade study reports 160–520 kgCO2e/m² over a wider boundary, A1–A5, B4 and C ([Arup](https://arup.com/globalassets/downloads/insights/the-carbon-foot-print-of-facades-the-significance-of-glass.pdf)).

**On fitting to this dataset.** The error analysis that motivated v2 used the same 292 buildings that v2 is evaluated on. The goal of this project is a prompt that transfers to other projects, not a calibration to these 292. We therefore kept v2 to statements that hold outside this dataset: scope definitions, method steps, and literature-backed material facts. It contains no dataset statistics such as medians or fitted factors. A held-out evaluation on another dataset would be the clean test (Section 8).

## 7. Results: prompt v2 vs v1

*To be filled in when the run `20261104_prompt-v2` finishes: the same tables as Section 4, the failure-mode diagnostics side by side (`analysis/error_analysis_20261104_baseline-innate_vs_20261104_prompt-v2.md`), and the BEST vs RANGE-midpoint comparison.*

## 8. Limitations and next steps

- **Missing assembly information.** No feature describes the wall assembly, so a ceiling on accuracy remains whatever the prompt says. Adding assembly type to the inputs, as the proposal intended (section 6.1), is the most promising change.
- **Subagents vs. API calls.** Answers within one task file share a context, so they are not as independent as separate API calls.
- **Functional unit.** Results are per m² of floor area, not per m² of wall, and the enclosure includes windows, doors and roofs.
- **Ground-truth quality.** It is uneven: 10 projects are flagged, and tool data vintages differ (HFC XPS).
- **Model dependence.** Results depend on the model and its version (Claude Opus 5.5, effort medium).
- **Next steps:**
  - evaluate the final prompt on a held-out dataset or a new project set;
  - run a feature study with envelope-relevant subsets (`FEATURES` in `experiment_config.py`);
  - test domain context with CLF Material Baselines and EPDs;
  - extend to 10 runs per building (the proposal protocol), with seeds 1003–1009.

## Appendix A. Prompts

See [`appendix_prompts.md`](appendix_prompts.md): system prompt, shared context, task text v1, **task text v2 (final)**, an example building block, and the subagent instruction template.

## Appendix B. Reproduction

```bash
python GWP-calculation/sum_gwp.py
```

```bash
python GWP-calculation/enclosure_breakdown.py
```

```bash
python subagent_runs.py prepare --run-name 20261104_prompt-v2 --runs 3 --model-label "claude-opus-5-5 (Claude Code subagent)" --effort medium
```

Then start one Claude Code subagent per `results/<run>/subagent/tasks/*.instructions.txt` (model Opus, effort medium), and collect the answers:

```bash
python subagent_runs.py collect --run-name 20261104_prompt-v2
```

```bash
python LLM-data-cleaning.py 20261104_prompt-v2
```

```bash
python make_fig1_bands.py 20261104_prompt-v2
```

```bash
python summarize_run.py 20261104_prompt-v2
```

```bash
python analysis/error_analysis.py 20261104_baseline-innate 20261104_prompt-v2
```

```bash
python report/make_prompt_appendix.py
```
