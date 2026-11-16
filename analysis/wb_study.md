# Whole building (A-C): answer-fitted prompt wb5 (`20261116_wholebuilding-wb5`, 1 run(s), 292 buildings)

**In-sample by design**: the mass factors and benchmarks were fitted on the reference values of the same buildings (all except 13 extreme values). The course reference results are from the course notes (Gemini, 10 runs, all 292 buildings) and are not in-sample.

| Estimator | all (292) | without extremes (279) | median abs log (all) | bias (all) |
|---|---|---|---|---|
| Best constant (414 for every building) | 34.6% | 36.2% | 0.344 | 1.05 |
| Model's own estimate only (Step A) | 44.5% | 45.5% | 0.236 | 0.87 |
| Mass route only (Step M) | 50.3% | 51.6% | 0.196 | 1.03 |
| Benchmark only (Step B) | 45.5% | 47.7% | 0.231 | 1.05 |
| wb5: 0.2 A + 0.5 M + 0.3 B (as reported) | 53.4% | 55.9% | 0.182 | 1.04 |
| Course reference, innate (Gemini, 10 runs) | 34.2% | – | – | – |
| Course reference, domain (papers) | 45.2% | – | – | – |
| Course reference, domain + ontology | 45.9% | – | – | – |
| Course reference, domain + benchmark | 36.3% | – | – | – |

wb5 coverage, all buildings: 156/292 = 53.4% (95% CI 47.7-59.1).
For comparison: a random forest on the 48 features reaches 57.2% (cross-validated) and 86.0% scored on its own training buildings (analysis/fit_wb_tables.py notes; scratch analysis).

**Did the model apply the tables?**

- All evidence lines parsed in 100.0% of answers.
- M within 5% of mass_total / floor area x F: 100.0%.
- B equal to the table value: 100.0%.
- Range centred on 0.2 A + 0.5 M + 0.3 B (within 3%): 100.0%.
