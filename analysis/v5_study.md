# Prompt v5 (answer-fitted): results (`20261116_prompt-v5`, 1 run(s), 49 buildings answered)

**In-sample by design.** v5's calibration factors and benchmarks were fitted on the reference values of all 262 cleaned buildings, so every v5 number below is in-sample, including the test columns. Constant = 84 kgCO2e/m2 (median of the cleaned set).

**Coverage (+/-20%), %**

| Estimator | all (49) | cleaned (44) | all, test (13) | cleaned, test (12) |
|---|---|---|---|---|
| constant | 18.4 | 20.5 | 7.7 | 8.3 |
| v1 | 8.2 | 9.1 | 15.4 | 16.7 |
| v3 | 30.6 | 31.8 | 38.5 | 33.3 |
| v4 | 30.6 | 34.1 | 38.5 | 41.7 |
| v5 | 30.6 | 34.1 | 30.8 | 33.3 |

**Median abs log error**

| Estimator | all (49) | cleaned (44) | all, test (13) | cleaned, test (12) |
|---|---|---|---|---|
| constant | 0.453 | 0.389 | 0.491 | 0.438 |
| v1 | 0.465 | 0.464 | 0.422 | 0.442 |
| v3 | 0.388 | 0.382 | 0.320 | 0.325 |
| v4 | 0.393 | 0.357 | 0.295 | 0.279 |
| v5 | 0.333 | 0.329 | 0.255 | 0.251 |

**Bias (geometric mean est/ref)**

| Estimator | all (49) | cleaned (44) | all, test (13) | cleaned, test (12) |
|---|---|---|---|---|
| constant | 1.27 | 0.87 | 1.27 | 0.97 |
| v1 | 0.89 | 0.73 | 0.88 | 0.84 |
| v3 | 1.07 | 0.92 | 1.03 | 1.04 |
| v4 | 1.15 | 0.89 | 1.08 | 0.99 |
| v5 | 1.24 | 0.97 | 1.16 | 1.08 |

**RMSE, kgCO2e/m2**

| Estimator | all (49) | cleaned (44) | all, test (13) | cleaned, test (12) |
|---|---|---|---|---|
| constant | 75.2 | 74.7 | 65.6 | 64.1 |
| v1 | 67.6 | 70.6 | 57.1 | 59.4 |
| v3 | 60.6 | 63.4 | 50.8 | 52.9 |
| v4 | 60.9 | 62.9 | 52.3 | 54.4 |
| v5 | 57.7 | 59.4 | 50.6 | 52.6 |

**Log-log slope (1 = no compression)**

| Estimator | all (49) | cleaned (44) | all, test (13) | cleaned, test (12) |
|---|---|---|---|---|
| constant | -0.00 | 0.00 | 0.00 | 0.00 |
| v1 | 0.35 | 0.31 | 0.68 | 0.36 |
| v3 | 0.46 | 0.39 | 0.87 | 0.55 |
| v4 | 0.26 | 0.29 | 0.58 | 0.36 |
| v5 | 0.28 | 0.36 | 0.63 | 0.48 |

v5 coverage with Wilson 95% CI: all 30.6% (19.5-44.5); cleaned 34.1% (21.9-48.9); all, test 30.8% (12.7-57.6); cleaned, test 33.3% (13.8-60.9).

**Paired tests against v5**

| Set | Baseline | McNemar p (coverage) | Wilcoxon p (abs log) | v5 closer, % |
|---|---|---|---|---|
| all | v4 | 1 | 0.103 | 59.2 |
| all | v3 | 1 | 0.0438 | 65.3 |
| all | constant | 0.21 | 0.000563 | 73.5 |
| cleaned | v4 | 1 | 0.0852 | 63.6 |
| cleaned | v3 | 1 | 0.00202 | 70.5 |
| cleaned | constant | 0.21 | 0.00879 | 70.5 |

**Did the model apply the tables?** (answers for in-scope buildings)

- All four evidence lines parsed in 100.0% of answers.
- K used within 3% of the table value: 100.0%.
- B equal to the table value: 100.0%.
- Range centred on 0.5 x CALIBRATED + 0.5 x B (within 3%): 100.0%.
- Out-of-scope rule applied in 2 answers, 2 of them correctly (2 out-of-scope answers in total).

| Source (mean of runs) | all | cleaned | all, test | cleaned, test |
|---|---|---|---|---|
| A bottom-up only | 22.4 | 25.0 | 23.1 | 25.0 |
| K x A calibrated only | 24.5 | 27.3 | 30.8 | 33.3 |
| B benchmark only | 20.4 | 22.7 | 23.1 | 25.0 |
| tables applied exactly to v5's own A | 30.6 | 34.1 | 30.8 | 33.3 |
| v5 as reported | 30.6 | 34.1 | 30.8 | 33.3 |

**Median estimate/reference by reference bin**

| Bin | n | v3 | v4 | v5 |
|---|---|---|---|---|
| 0-25 | 8 | 3.69 | 3.35 | 3.54 |
| 25-50 | 2 | 1.16 | 1.38 | 1.26 |
| 50-100 | 15 | 0.90 | 1.05 | 1.11 |
| 100-200 | 20 | 0.85 | 0.72 | 0.81 |
| 200- | 4 | 0.54 | 0.48 | 0.54 |
