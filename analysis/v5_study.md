# Prompt v5 (answer-fitted): results (`20261116_prompt-v5`, 3 run(s), 292 buildings answered)

**In-sample by design.** v5's calibration factors and benchmarks were fitted on the reference values of all 262 cleaned buildings, so every v5 number below is in-sample, including the test columns. Constant = 84 kgCO2e/m2 (median of the cleaned set).

**Coverage (+/-20%), %**

| Estimator | all (292) | cleaned (262) | all, test (88) | cleaned, test (81) |
|---|---|---|---|---|
| constant | 25.7 | 28.6 | 31.8 | 34.6 |
| v1 | 19.5 | 19.8 | 20.5 | 21.0 |
| v3 | 25.0 | 26.7 | 26.1 | 27.2 |
| v4 | 32.2 | 34.7 | 35.2 | 37.0 |
| v5 | 35.6 | 38.5 | 38.6 | 40.7 |

**Median abs log error**

| Estimator | all (292) | cleaned (262) | all, test (88) | cleaned, test (81) |
|---|---|---|---|---|
| constant | 0.446 | 0.389 | 0.455 | 0.391 |
| v1 | 0.456 | 0.429 | 0.393 | 0.386 |
| v3 | 0.426 | 0.397 | 0.400 | 0.395 |
| v4 | 0.370 | 0.337 | 0.348 | 0.312 |
| v5 | 0.320 | 0.286 | 0.304 | 0.275 |

**Bias (geometric mean est/ref)**

| Estimator | all (292) | cleaned (262) | all, test (88) | cleaned, test (81) |
|---|---|---|---|---|
| constant | 1.24 | 1.01 | 1.22 | 1.04 |
| v1 | 0.75 | 0.71 | 0.75 | 0.75 |
| v3 | 0.86 | 0.85 | 0.86 | 0.88 |
| v4 | 0.98 | 0.89 | 0.96 | 0.92 |
| v5 | 1.07 | 0.98 | 1.05 | 1.01 |

**RMSE, kgCO2e/m2**

| Estimator | all (292) | cleaned (262) | all, test (88) | cleaned, test (81) |
|---|---|---|---|---|
| constant | 78.8 | 75.1 | 75.0 | 75.5 |
| v1 | 79.7 | 78.1 | 74.1 | 76.7 |
| v3 | 76.0 | 74.5 | 69.2 | 71.2 |
| v4 | 73.0 | 71.6 | 68.2 | 70.4 |
| v5 | 71.3 | 69.9 | 64.1 | 65.9 |

**Log-log slope (1 = no compression)**

| Estimator | all (292) | cleaned (262) | all, test (88) | cleaned, test (81) |
|---|---|---|---|---|
| constant | -0.00 | -0.00 | 0.00 | 0.00 |
| v1 | 0.46 | 0.30 | 0.52 | 0.34 |
| v3 | 0.59 | 0.37 | 0.68 | 0.45 |
| v4 | 0.36 | 0.24 | 0.42 | 0.25 |
| v5 | 0.39 | 0.27 | 0.47 | 0.34 |

v5 coverage with Wilson 95% CI: all 35.6% (30.3-41.3); cleaned 38.5% (32.9-44.6); all, test 38.6% (29.1-49.1); cleaned, test 40.7% (30.7-51.6).

**Paired tests against v5**

| Set | Baseline | McNemar p (coverage) | Wilcoxon p (abs log) | v5 closer, % |
|---|---|---|---|---|
| all | v4 | 0.174 | 0.00355 | 56.5 |
| all | v3 | 0.00102 | 3.6e-07 | 63.4 |
| all | constant | 0.00346 | 5.89e-09 | 65.8 |
| cleaned | v4 | 0.174 | 0.0017 | 60.3 |
| cleaned | v3 | 0.000639 | 1.89e-08 | 64.1 |
| cleaned | constant | 0.00805 | 2.36e-05 | 63.4 |

**Did the model apply the tables?** (answers for in-scope buildings)

- All four evidence lines parsed in 100.0% of answers.
- K used within 3% of the table value: 99.8%.
- B equal to the table value: 99.9%.
- Range centred on 0.5 x CALIBRATED + 0.5 x B (within 3%): 100.0%.
- Out-of-scope rule applied in 40 answers, 39 of them correctly (39 out-of-scope answers in total).

| Source (mean of runs) | all | cleaned | all, test | cleaned, test |
|---|---|---|---|---|
| A bottom-up only | 19.5 | 20.6 | 19.3 | 21.0 |
| K x A calibrated only | 31.2 | 34.0 | 31.8 | 34.6 |
| B benchmark only | 30.5 | 33.2 | 34.1 | 37.0 |
| tables applied exactly to v5's own A | 35.6 | 38.5 | 38.6 | 40.7 |
| v5 as reported | 35.6 | 38.5 | 38.6 | 40.7 |

Run-to-run CV of v5: 5.0%. Coverage of single runs (all): 36.0%, 36.0%, 34.2%.

**Median estimate/reference by reference bin**

| Bin | n | v3 | v4 | v5 |
|---|---|---|---|---|
| 0-25 | 36 | 1.53 | 2.74 | 2.94 |
| 25-50 | 43 | 1.31 | 1.46 | 1.58 |
| 50-100 | 114 | 0.91 | 0.97 | 1.02 |
| 100-200 | 72 | 0.69 | 0.67 | 0.75 |
| 200- | 27 | 0.38 | 0.32 | 0.36 |
