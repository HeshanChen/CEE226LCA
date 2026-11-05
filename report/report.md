# Can an LLM Estimate the Embodied Carbon of a Building Enclosure? Error Analysis and Prompt Design

CEE226 Group 8: George Zheng, Zixuan Zhao, Heshan Chen, Fei Cheng, Jamie Liu.
Part of the project *Climate- and Use-Specific Embodied Impacts of Exterior Wall Design: A Comparative LCA and Implications for LEED v5 Embodied Carbon Credits*.

> 中文版：[`report_zh.md`](report_zh.md). Both versions have the same content; the final prompt is the English text in Appendix A.
>
> Status: complete. Prompts v1–v3 were run 3 times on each of the 292 buildings, with a held-out evaluation on 88 test buildings (Section 9) and a feature study (Section 10). The final prompt is v3 (Appendix A, section E).
> Every number in this report can be regenerated with the commands in Appendix B.

## 1. Summary

The LLM in this study is Claude Opus 5.5, run as a Claude Code subagent with medium reasoning effort. Given the 48 early-stage features of each of the 292 buildings in the CLF harmonized WBLCA dataset, it estimated the **cradle-to-gate (A1–A3) embodied carbon of the building enclosure**, in kgCO2e per m² of floor area.

With a plain prompt (v1, innate knowledge), only **19.5%** of the estimates land within ±20% of the reference LCA. RMSE is 79.7 kgCO2e/m² and the median absolute percentage error is 37.9%.

The error is not random. The model:

1. compresses every building toward a "typical" value of about 50–60 kgCO2e/m²;
2. misses the single largest material driver in the data, HFC-blown XPS insulation;
3. underestimates envelope area when it is not given;
4. misjudges renovations.

Its largest overestimates are mostly cases where the reference LCA itself is incomplete.

From this analysis we wrote prompt v2. It defines the enclosure the way the dataset classifies it, requires a component-by-component take-off, names the high-impact materials, forbids anchoring on a typical value, adds renovation guidance, and asks for a best estimate. The prompt is described in Section 6 and given in full in Appendix A.

Prompt v2 made the model **more consistent** (CV 19.0% → 13.8%) and **less compressed** (slope 0.46 → 0.55), but **less accurate**: coverage fell to 15.1% (McNemar p = 0.085), the median APE rose to 44.3%, and the bias went from 0.75 to 0.67. The model named XPS but kept assuming polyiso roofs, its bottom-up component intensities were low, and the renovation rule pushed estimates down (Section 7). In short, qualitative knowledge in a prompt is acknowledged but not applied; changing the numbers requires quantitative anchors at the step where each number is chosen.

Prompt v3 does exactly that (Section 8):
- an externally sourced table of component intensities at the step where intensities are chosen;
- the HFC-XPS modelling convention;
- a per-envelope sanity check;
- a renovation rule that no longer subtracts.

**v3 is the final prompt.** On all 292 buildings, coverage is **25.0%** (v1 19.5%), RMSE 76.0, bias 0.86 and CV 12.5%. The improvement over v1 is consistent but borderline significant (McNemar p = 0.085, Wilcoxon p = 0.053); over v2 it is clearly significant (p = 0.002). The non-XPS part of the enclosure is now estimated without bias (0.99), and so are buildings whose envelope area is given (0.99). What remains is compression at the high end (buildings above 200 are at 0.38), more overestimation of light enclosures, and renovations.

**Held-out test set** (88 buildings, stratified split; Section 9). v3 reaches 26.1% coverage against 20.5% for v1, with RMSE 69.2 against 74.1, bias 0.86 against 0.75 and CV 11.2% against 19.2%. Its median log error is the same as v1's, and the v1–v3 difference is not significant at this size (McNemar p = 0.41). Every finding that motivated v2 and v3 replicates on the 204 dev buildings alone.

**Feature study** (Section 10). With prompt v3, a 10-feature early-design input set is as accurate as all 48 features, and removing `mass_total` or the LCA-derived fields does not hurt. Every difference between feature sets lies within the run-to-run spread. The limiting information is the assembly type, which no feature provides.

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
- **Inputs.** All 48 features of `references/buildings_metadata_LLM.xlsx` (49 columns including `project_index`), plus the feature glossary. No papers, no benchmark tables and no ontology, i.e. the innate-knowledge condition.
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

The model leans on geometry more than the data justifies. The envelope-to-floor-area ratio correlates 0.62 with the log estimate but only 0.39 with the log truth, and mass per floor area 0.68 against 0.53. What it misses is the intensity per m² of envelope. In the truth this ranges from 19 to 278 kgCO2e per m² of envelope (5th–95th percentile); in the estimates, from 20 to 144. This intensity alone correlates −0.79 with the log error. It is set by material and assembly choice, and **none of the 48 features describes the wall assembly**.

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

**On fitting to this dataset.** The error analysis that motivated v2 used the same 292 buildings that v2 is evaluated on. The goal of this project is a prompt that transfers to other projects, not a calibration to these 292. We therefore kept v2 to statements that hold outside this dataset: scope definitions, method steps, and literature-backed material facts. It contains no dataset statistics such as medians or fitted factors. A held-out evaluation on another dataset would be the clean test (Section 9).

## 7. Results: prompt v2 vs v1

All 876 v2 answers parsed (`results/20261104_prompt-v2/`). The same buildings, seeds and chunks were used as for v1.

| Subset | Prompt | ±20% coverage | RMSE | median APE | MAPE | est/true (geo-mean) | CV across runs |
|---|---|---|---|---|---|---|---|
| All projects (292) | v1 | **19.5%** | **79.7** | **37.9%** | 96.0% | **0.75** | 19.0% |
| | v2 midpoint | 15.1% | 81.0 | 44.3% | **83.0%** | 0.67 | **13.8%** |
| | v2 BEST | 14.4% | 83.2 | 49.4% | 81.4% | 0.59 | 13.8% |
| New construction (243) | v1 | 18.9% | 77.4 | 37.5% | 93.4% | 0.76 | 17.3% |
| | v2 midpoint | 16.5% | 79.8 | 44.2% | 81.7% | 0.70 | 11.8% |
| Excl. 10 incomplete (282) | v1 | 20.2% | 80.5 | 37.3% | 57.8% | 0.72 | 19.1% |
| | v2 midpoint | 15.6% | 81.9 | 43.9% | 57.7% | 0.64 | 13.5% |

**Paired tests (same 292 buildings).**
- v2 errors are larger (Wilcoxon signed-rank on |log(est/true)|, p < 0.0001). v2 is closer to the truth for only 34% of buildings.
- The drop in coverage is not significant (McNemar p = 0.085): 31 buildings were inside the band only with v1, and 18 only with v2.

**Prompt v2 did not improve accuracy.** It improved consistency and reduced compression, but it made the underestimate worse. Diagnostics side by side are in `analysis/error_analysis_20261104_baseline-innate_vs_20261104_prompt-v2.md`.

| Failure mode (Section 5) | v1 | v2 | Effect of v2 |
|---|---|---|---|
| Compression: log–log slope (1 = none) | 0.46 | 0.55 | better |
| Compression: SD of estimates / SD of truth | 0.39 | 0.47 | better |
| Low-end overestimate (truth < 25): est/true | 1.58 | 1.27 | better |
| Consistency: mean CV across runs | 19.0% | 13.8% | better |
| XPS mentioned, among projects that have XPS | 0.7% | 39.6% | the model now names it |
| Projects with XPS: est/true | 0.67 | 0.58 | worse |
| Envelope area not given: est/true | 0.65 | 0.57 | worse |
| Cold zones 5–8 / warm zones 1–3: est/true | 0.65 / 0.77 | 0.61 / 0.69 | worse (gap similar) |
| Minor renovation / major renovation: est/true | 0.85 / 0.77 | 0.56 / 0.63 | worse |
| Flagged incomplete ground truth: est/true | 3.09 | 3.07 | unchanged (not an LLM error) |

### 7.1 Why v2 underestimates more

1. **Knowing a fact is not the same as applying it.**
   - v2 answers name XPS 50 times more often, but 89% of them still assume **polyiso** roof insulation.
   - XPS is mostly placed below grade or at slab edges: 274 mentions in that context against 114 at the roof.
   - In the reference LCAs, most XPS sits at roof or floor level (54.5% of XPS GWP was tagged "Superstructure" in Tally). The model's assumption matches common practice, but not how these LCA models were built.
   - As a result, the median roof intensity in the v2 take-offs is **35 kgCO2e/m²** (IQR 30–40), and projects with XPS got worse rather than better.
2. **The bottom-up intensities are biased low.**
   - Median component intensities in the v2 take-offs are 80 kgCO2e/m² for opaque walls (IQR 65–110), 35 for roofs, and 145 for glazing and curtain wall (IQR 126–320).
   - Converted to per m² of envelope (160 projects with envelope area), the median is 66.8 for v2 against 72.4 for v1 and **86.7 for the truth**.
   - An explicit take-off from early-stage information leaves out items that the reference LCA includes. The prompt's curtain-wall range (100–200 kgCO2e/m²) became the default value (median 145).
3. **The renovation rule backfired.** "Count only new enclosure materials" moved minor renovations from 0.85 to 0.56 and major renovations from 0.77 to 0.63. For a model that already underestimates, a rule that subtracts makes things worse.
4. **BEST is below the range midpoint** (median 0.93× the midpoint). The model's uncertainty is right-skewed, so its stated best estimate is the worse estimator here.

### 7.2 Lessons for prompt design

These lessons transfer beyond this dataset:

- A **structured, step-by-step method** makes the model more consistent (CV −27%) and less anchored on a typical value. It also exposes the model's component-level priors: if those are biased, the structure carries the bias straight into the total.
- **Qualitative knowledge** ("XPS is about 10× higher") gets repeated in the reasoning but does not change the numbers. To move an estimate, the prompt has to supply a **quantitative anchor at the step where the number is chosen**, together with the condition under which it applies (e.g. which insulation the LCA tool is likely to have modelled).
- **Instructions that subtract** (exclusions, "only new materials") should be paired with what to include, otherwise they amplify an existing low bias.
- Report the **range midpoint**, not a self-reported best value.

## 8. Prompt v3

v3 keeps what worked in v2: the scope definition, the step-by-step method, and the rule against anchoring on a typical value. It changes what Section 7 showed did not work. Full text: Appendix A, section E.

| v2 result (Section 7.1) | Prompt v3 change |
|---|---|
| XPS named but not applied; polyiso roofs assumed | Step 2 states the tool modelling convention: whole-building LCA models of this period (Tally, One Click LCA) often model roof and below-grade insulation as HFC-blown XPS. When the insulation type is unknown, the range must include that case, especially in colder climates |
| Low bottom-up component intensities | Step 3 gives a reference table of A1–A3 intensities per m² of component: 8 wall types, 3 fenestration groups, roof assemblies by insulation type (HFC XPS: 85–110 counting the product stage only, up to 335–410 when blowing-agent emissions are booked with the product), insulation per m²·RSI, and aluminum per kg. The model is told that complete assemblies include framing, attachments, barriers, sealants and trim, and not to go below the low end unless the assembly is clearly minimal |
| No sanity check on the total | Step 4: convert the total to per m² of envelope. For new construction with conventional walls and 30–40% glazing, a blended value below about 50 kgCO2e/m² of envelope signals a missing component or a missing high-carbon option |
| Ranges did not include high-carbon alternatives | Step 5: the range must include the plausible higher-carbon alternatives (the midpoint is the estimate) |
| The renovation rule subtracted | Step 6 is rewritten: renovations often include substantial new envelope work (re-cladding, new curtain wall or windows, re-roofing), so the model should not assume the existing envelope is kept unless the data says so |
| BEST less accurate than the midpoint | Back to a single `RANGE` line |

**Sources.** The reference values were compiled by a separate research subagent with web access into [`references/envelope_intensities_sources.md`](../references/envelope_intensities_sources.md), with source links, system boundaries and unit conversions. The sources include:
- CLF North American Material Baselines 2023 and 2025;
- PCI industry-average precast EPDs (2025);
- Kawneer curtain wall, storefront and window EPDs (2021);
- RDH Building Science wall assembly studies;
- the UBC fenestration study;
- SPRI, NAIMA and AEC industry EPDs (as reported in the CLF baselines);
- the Arup/Saint-Gobain facade study.

The research brief excluded the Benke et al. dataset and anything derived from it. The subagent also left out the CLF WBLCA Benchmark v2 results, because they probably share source models with the ground truth. Several wall values are assembly sums by the subagent and are marked as uncertain in that file. The "below about 50 per m² of envelope" threshold in step 4 is our own derivation from those component ranges, not a published benchmark.

### 8.1 Results: prompt v3 vs v2 and v1

All 876 v3 answers parsed (`results/20261104_prompt-v3/`). The model, effort, features, buildings, seeds and chunks are the same as for v1 and v2.

During run 2 a container restart interrupted the six subagents after 130 of the run's 292 answers. The remaining 162 buildings were answered by six continuation subagents, using the same prompt and only the missing buildings (`subagent_runs.py resume`, recorded in the run manifest). Those 162 buildings therefore shared a context with different neighbours than planned.

| Subset | Prompt | ±20% coverage | RMSE | median APE | est/true (geo-mean) | CV across runs |
|---|---|---|---|---|---|---|
| All projects (292) | v1 | 19.5% (15.4–24.5) | 79.7 | **37.9%** | 0.75 | 19.0% |
| | v2 | 15.1% (11.4–19.6) | 81.0 | 44.3% | 0.67 | 13.8% |
| | **v3** | **25.0% (20.4–30.3)** | **76.0** | 40.0% | **0.86** | **12.5%** |
| New construction (243) | v1 | 18.9% | 77.4 | 37.5% | 0.76 | 17.3% |
| | **v3** | **26.3%** | **74.1** | 38.0% | **0.91** | **10.9%** |
| Excl. 10 incomplete (282) | v1 | 20.2% | 80.5 | 37.3% | 0.72 | 19.1% |
| | **v3** | **25.9%** | **76.5** | 37.4% | **0.83** | **12.6%** |

**Paired tests (same 292 buildings).**
- **v3 vs v1:** 46 buildings are inside the band only with v3, and 30 only with v1 (McNemar p = 0.085). The median |log(est/true)| falls from 0.456 to 0.426 (Wilcoxon p = 0.053), and v3 is closer to the truth for 57% of buildings. The improvement is consistent but only borderline significant at 3 runs × 292 buildings.
- **v3 vs v2:** the improvement is significant (McNemar p = 0.002; Wilcoxon p < 0.0001), and v3 is closer for 66% of buildings.
- **Median APE:** v3 is slightly worse than v1 (40.0% against 37.9%) even though its log error is lower. This is because v3 moves estimates up, and APE penalises overestimates more than underestimates.
- **Over/underestimates:** with v1, 58% of buildings were underestimated by more than 20% and 18% overestimated by more than 20%. With v3 the figures are 46% and 29%. The bias is smaller and the errors are more balanced.

| Failure mode (Section 5) | v1 | v2 | v3 |
|---|---|---|---|
| Overall bias, est/true (geo-mean) | 0.75 | 0.67 | **0.86** |
| Compression: log–log slope (1 = none) | 0.46 | 0.55 | **0.59** |
| Compression: SD of estimates / SD of truth | 0.39 | 0.47 | **0.63** |
| Truth 50–100: est/true | 0.76 | 0.71 | **0.91** |
| Truth 100–200 / > 200: est/true | 0.54 / 0.28 | 0.51 / 0.27 | **0.69 / 0.38** |
| Truth < 25 / 25–50: est/true | 1.58 / 1.09 | **1.27 / 0.93** | 1.53 / 1.31 |
| XPS mentioned among projects that have XPS | 0.7% | 39.6% | **96.0%** |
| HFC / blowing agent mentioned | 0% | 4% | **88%** |
| Projects with XPS: est/true | 0.67 | 0.58 | **0.75** |
| Est/(truth − XPS) | 0.84 | 0.77 | **0.99** |
| Cold zones 5–8 / warm zones 1–3: est/true | 0.65 / 0.77 | 0.61 / 0.69 | **0.82 / 0.98** |
| Envelope area given / not given: est/true | 0.81 / 0.65 | 0.75 / 0.57 | **0.99 / 0.73** |
| Minor / major renovation: est/true | **0.85 / 0.77** | 0.56 / 0.63 | 0.74 / 0.71 |
| Tenant improvement: est/true | 0.24 | 0.26 | 0.26 |

**What worked.**
- **Quantitative anchors at the decision step.** XPS (with its blowing agent) is now named in 96% of answers for projects that contain XPS.
- **The non-XPS part of the enclosure is now unbiased.** est/(truth − XPS) went from 0.84 to 0.99.
- **When the envelope area is given, the estimate is unbiased overall** (0.99). The per-component reference values and the per-envelope check are what fixed the low bottom-up totals.
- **The climate gap closed for warm zones.** Warm zones are now at 0.98. Cold zones (0.82) remain underestimated because of thick HFC-XPS layers: projects where XPS is more than 30% of the truth are still at 0.61.

**What is left.**
1. **Compression is reduced but not removed** (slope 0.59). Buildings above 200 kgCO2e/m² are still at 0.38, and their extreme values (e.g. 300+ kgCO2e/m² of curtain wall or XPS) are not predictable from the features.
2. **Low-carbon buildings are now overestimated more.** In the truth 25–50 bin, est/true rose from 1.09 to 1.31. The "do not go below the low end" instruction and the per-envelope check push light enclosures up, which is the price of correcting the low bias.
3. **When the envelope area is missing, buildings are still underestimated** (0.73).
4. **Renovations still fall short of v1.** They recovered from v2 but not to v1's level, and tenant improvements are unchanged at 0.26.

**Final prompt.** v3 is the best of the three prompts by coverage, RMSE, bias, log error and consistency, and is the final prompt of this study (Appendix A, section E).

## 9. Held-out evaluation

**No suitable external dataset.** We looked for an independent dataset with the same structure (element-level enclosure A1–A3 results plus early-stage features for North American buildings) and found none:
- The CLF WBLCA Benchmark v2 results probably share source models with the Benke et al. dataset.
- The open CarbEnMats / Global Buildings Database ([Zenodo](https://zenodo.org/records/8363895)) has more than 1,200 case studies, but only 172 of them report an envelope A1–A3 value, and all of those are European (Belgium 105, Netherlands 47, Finland 19, UK 1). Its "envelope" covers only openings and finishes; exterior walls and roofs are counted under structure. For those 172 buildings the envelope area, WWR and U-values are empty, and the number of storeys is given for only 12%. We checked the data and decided not to map it.
- The Mendeley "virtual building database" ([link](https://data.mendeley.com/datasets/znbp3szd75/1)) is synthetic.

We therefore held out part of this dataset.

**Split.** `analysis/make_split.py` (seed 226) assigns 30% of the projects to a test set (88) and 70% to a dev set (204). It is stratified on input features only: new construction vs renovation × climate group (cold zones 5–8, zone 4, warm zones 1–3, other). The two sets are similar in median truth (78.8 / 74.6 kgCO2e/m²). The test set has fewer projects with XPS (43% against 54%) and 2 of the 10 flagged incomplete ground truths.

**The split was assigned after the v1–v3 runs.** The error analysis behind v2 and v3 had therefore looked at aggregate patterns across all 292 buildings, including the test buildings. To check that this did not drive the prompt design, we re-ran every diagnostic on the dev set alone (`analysis/error_analysis_…_dev.md`). Every finding used to revise the prompt replicates on dev:

| Finding behind a prompt change | All 292 | Dev only (204) |
|---|---|---|
| v1 compression: log–log slope | 0.46 | 0.44 |
| v1 est/true for truth > 200 / < 25 | 0.28 / 1.58 | 0.28 / 1.59 |
| XPS share of enclosure A1–A3 GWP | 15.5% | 14.7% |
| v1 est/true, projects with XPS vs without | 0.67 vs 0.80 | 0.66 vs 0.77 |
| v1 est/(truth − XPS) | 0.84 | 0.80 |
| v1 cold zones vs warm zones | 0.65 vs 0.77 | 0.64 vs 0.71 |
| v1 envelope area given vs not | 0.81 vs 0.65 | 0.79 vs 0.65 |
| v1 answers mentioning XPS | 0.6% | 0.5% |
| Flagged incomplete ground truths, v1 est/true | 3.09 | 3.09 |
| v2 answers naming polyiso for the roof; median roof intensity | 89%; 35 | 89%; 35 |
| v2 per m² envelope estimate vs truth | 66.8 vs 86.7 | 68.1 vs 85.5 |
| v2 minor renovation est/true (v1 → v2) | 0.85 → 0.56 | 0.79 → 0.40 |

The same prompt revisions would therefore have followed from the dev set alone. Neither prompt contains per-building information or statistics computed from this dataset. The v3 reference values come from external EPDs and baselines.

**Test-set results (88 buildings, never used to choose between prompts):** `analysis/compare_…md`

| Prompt | ±20% coverage (95% CI) | RMSE | median APE | median abs log error | est/true geo-mean | CV across runs |
|---|---|---|---|---|---|---|
| v1 | 20.5% (13.3–30.0) | 74.1 | **36.4%** | **0.393** | 0.75 | 19.2% |
| v2 | 18.2% (11.5–27.5) | 75.7 | 43.4% | 0.511 | 0.66 | 15.2% |
| **v3** | **26.1% (18.1–36.2)** | **69.2** | 37.0% | 0.400 | **0.86** | **11.2%** |

| Test-set pair | Inside only first / only second | McNemar p | abs log error (Wilcoxon p) | Second closer |
|---|---|---|---|---|
| v1 vs v3 | 9 / 14 | 0.41 | 0.393 → 0.400 (p = 0.38) | 55% |
| v2 vs v3 | 11 / 18 | 0.27 | 0.511 → 0.400 (p = 0.002) | 62% |
| v1 vs v2 | 9 / 7 | 0.80 | 0.393 → 0.511 (p = 0.0002) | 34% |

**Reading the held-out results.**
- On the test set, v3 improves coverage by 5.6 points, RMSE by 4.9 kgCO2e/m², the bias (0.75 → 0.86) and consistency (CV 19.2% → 11.2%).
- Its typical error (median |log error|) is the same as v1's, and none of the v1–v3 differences is significant at n = 88.
- v3 is clearly better than v2 (Wilcoxon p = 0.002), and v2's regression against v1 also replicates on the test set (p = 0.0002).
- The test set has fewer XPS projects, which is where v3 gains most. v1 also happens to do better on test than on dev (0.393 against 0.476 median abs log error).

**Conclusion.** v3 is the best prompt on all, dev and test buildings for coverage, RMSE, bias and consistency. Its advantage in typical error over the plain baseline is small and is not statistically established on the held-out set. A larger or external test set is needed to settle it.

## 10. Feature study: which inputs does the model need?

**Question.** The baseline analysis showed that the error comes from assembly and material choices, which none of the inputs describe (Section 5.1). Does the model need all 48 features, or would early-design information be enough? This is the feature-study iteration suggested by the course team: the full input set against smaller envelope-relevant subsets.

**Design.** Prompt v3 is kept fixed. The buildings, seeds, chunks, model (Opus 5.5) and effort (medium) are the same as before; only the feature list changes, and the glossary is filtered to match. The three floor-area fields are in every set, because the task defines the unit with them. To limit token use, each condition was run **once (run 0)** and compared building by building with run 0 of v3 on all 48 features (`analysis/feature_study.py`, `analysis/feature_study.md`).

| Condition | Features | Contents |
|---|---|---|
| all (= v3) | 48 | every column of `buildings_metadata_LLM.xlsx` |
| early | 39 | all minus the LCA-derived fields (`lca_*`) and `mass_total`, i.e. design-stage information only |
| env | 15 | climate zone, state, use, project type, floor area, storeys, height, envelope area, WWR, wall and roof R-values, structure summary, IBC type |
| min | 10 | climate zone, use, project type, floor area, storeys, WWR, wall and roof R-values (proposal 6.1) |
| no-lca | 40 | all minus the 8 `lca_*` fields |
| no-mass | 47 | all minus `mass_total` |

`mass_total` is the sum of the reference LCA's own inventory mass (stages A–C), so it is not known at early design and partly encodes the answer. It correlates 0.53 with the true value. Prompts v2 and v3 also suggested using it for renovations.

Leave-one-group-out ablations for the other seven groups (site, code year, use type, size, geometry, thermal, structure) were prepared (`FEATURE_SETS`), but we stopped them to limit token use. 50 answers of `no-geometry` exist but are not analysed.

**Results (run 0, all 292 buildings; paired with "all").**

| Condition | Features | ±20% coverage | median abs log error | est/true geo-mean | RMSE | Δ abs log error vs all | Wilcoxon p | McNemar p |
|---|---|---|---|---|---|---|---|---|
| all | 48 | 24.3% | 0.461 | 0.86 | 77.8 | – | – | – |
| early | 39 | 21.6% | 0.462 | 0.88 | 81.2 | +0.001 | 0.13 | 0.30 |
| env | 15 | 19.9% | 0.463 | 0.93 | 80.6 | +0.001 | 0.33 | 0.085 |
| min | 10 | **25.3%** | 0.476 | 0.81 | **77.3** | +0.015 | 0.81 | 0.83 |
| no-lca | 40 | **25.3%** | **0.441** | 0.90 | 78.6 | −0.020 | 0.57 | 0.77 |
| no-mass | 47 | 22.6% | 0.452 | 0.85 | 79.2 | −0.009 | 0.92 | 0.56 |

On the test split (88 buildings), the same picture holds: min has 30.7% coverage against 28.4% for all, and no difference in log error is significant. Two coverage drops on test, early −8.0 points (p = 0.065) and env −10.2 points (p = 0.049), do not survive the multiple comparisons (5 conditions × 3 splits). Their log errors do not differ (p = 0.08 and 0.11).

**How large is the noise?** Running the same prompt again changes the result by about as much as any feature set does. Across the three v3 runs, single-run coverage was 24.3 / 24.3 / 22.3% and the median abs log error 0.461 / 0.436 / 0.454 (spread 0.025). For v1 the spreads were 3.4 points and 0.048. Every feature-set difference above lies within this run-to-run spread (`analysis/figures/feature_study.png`).

**Conclusions.**
1. **Ten early-design inputs are as good as all 48.** Climate zone, use, project type, floor area, storeys, WWR and the R-values give the same accuracy as the full set. The other 38 features add nothing measurable, which is consistent with Section 5.1: the missing information is the assembly, and no subset provides it. For the proposal's question this is the practical result. An LLM estimate at schematic design needs only the information a designer already has.
2. **The model does not depend on the leakage-prone fields.** Removing `mass_total`, or all LCA-derived fields, does not make the estimates worse; the no-lca condition is in fact marginally better. The v1–v3 results are therefore not an artefact of features that encode the reference LCA.
3. **Prompt content matters more than feature selection.** Moving from v2 to v3 changed the median abs log error by 0.137 and coverage by 10 points (Section 8.1). No feature set changed either by more than 0.020 or 4.5 points.

## 11. Limitations and next steps

- **Missing assembly information.** No feature describes the wall assembly, so a ceiling on accuracy remains whatever the prompt says. Adding assembly type to the inputs, as the proposal intended (section 6.1), is the most promising change.
- **Subagents vs. API calls.** Answers within one task file share a context, so they are not as independent as separate API calls. In v3 run 2, 162 buildings were answered in continuation tasks after a container restart (Section 8.1).
- **Held-out split assigned after the runs.** The dev-only replication (Section 9) shows that the prompt design did not depend on the test buildings. Even so, only a dataset the prompts have never been checked against can fully rule out overfitting.
- **Statistical power.** With 3 runs, the v3-vs-v1 gain is borderline on all 292 buildings (McNemar p = 0.085) and not significant on the 88 test buildings (p = 0.41). More runs per building or more buildings would settle it.
- **Feature study with one run.** Each feature condition was run once, and 7 of the 9 leave-one-group-out ablations were stopped to limit token use. The conclusion "no feature set matters" rests on differences that lie within the run-to-run spread; it is a null result, not proof that the features are irrelevant.
- **Functional unit.** Results are per m² of floor area, not per m² of wall, and the enclosure includes windows, doors and roofs.
- **Ground-truth quality.** It is uneven: 10 projects are flagged, and tool data vintages differ (HFC XPS).
- **Model dependence.** Results depend on the model and its version (Claude Opus 5.5, effort medium).
- **Next steps:**
  - evaluate the final prompt on an external dataset or a new project set (e.g. map the CarbEnMats/GBDB enclosure fields to this feature set);
  - add assembly-type inputs (cladding, insulation type, glazing system), the information the feature study shows is missing;
  - finish the remaining leave-one-group-out ablations (`FEATURE_SETS` in `experiment_config.py`, already prepared);
  - test domain context with CLF Material Baselines and EPDs;
  - extend to 10 runs per building (the proposal protocol), with seeds 1003–1009.

## Appendix A. Prompts

See [`appendix_prompts.md`](appendix_prompts.md): system prompt, shared context, task texts v1 and v2, **task text v3 (final)**, an example building block, and the subagent instruction template.

## Appendix B. Reproduction

```bash
python GWP-calculation/sum_gwp.py
```

```bash
python GWP-calculation/enclosure_breakdown.py
```

```bash
python subagent_runs.py prepare --run-name 20261104_prompt-v3 --runs 3 --model-label "claude-opus-5-5 (Claude Code subagent)" --effort medium
```

Then start one Claude Code subagent per `results/<run>/subagent/tasks/*.instructions.txt` (model Opus, effort medium), and collect the answers:

```bash
python subagent_runs.py collect --run-name 20261104_prompt-v3
```

```bash
python LLM-data-cleaning.py 20261104_prompt-v3
```

```bash
python make_fig1_bands.py 20261104_prompt-v3
```

```bash
python summarize_run.py 20261104_prompt-v3
```

```bash
python analysis/error_analysis.py 20261104_baseline-innate 20261104_prompt-v2 20261104_prompt-v3
```

```bash
python analysis/make_split.py
```

```bash
python analysis/compare_runs.py 20261104_baseline-innate 20261104_prompt-v2 20261104_prompt-v3
```

```bash
python analysis/error_analysis.py --split dev 20261104_baseline-innate 20261104_prompt-v2 20261104_prompt-v3
```

```bash
python analysis/feature_study.py
```

```bash
python report/make_prompt_appendix.py
```

Feature-study runs are prepared with `--feature-set <name> --runs 1`. Interrupted runs can be continued with `python subagent_runs.py resume --run-name <run> [--runs 0]`.
