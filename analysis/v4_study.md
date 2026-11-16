# Prompt v4 (weighted evidence): results (`20261116_prompt-v4`, 3 run(s), 292 buildings answered)

Constant = 85 kgCO2e/m2 for every building (median of the cleaned development set).

**Coverage (+/-20%), %**

| Estimator | all (292) | all, dev (204) | all, test (88) | cleaned (262) | cleaned, dev (181) | cleaned, test (81) |
|---|---|---|---|---|---|---|
| constant | 24.3 | 22.5 | 28.4 | 27.1 | 25.4 | 30.9 |
| v1 | 19.5 | 19.1 | 20.5 | 19.8 | 19.3 | 21.0 |
| v3 | 25.0 | 24.5 | 26.1 | 26.7 | 26.5 | 27.2 |
| v4 | 32.2 | 30.9 | 35.2 | 34.7 | 33.7 | 37.0 |

**Median abs log error**

| Estimator | all (292) | all, dev (204) | all, test (88) | cleaned (262) | cleaned, dev (181) | cleaned, test (81) |
|---|---|---|---|---|---|---|
| constant | 0.436 | 0.436 | 0.455 | 0.389 | 0.393 | 0.385 |
| v1 | 0.456 | 0.476 | 0.393 | 0.429 | 0.459 | 0.386 |
| v3 | 0.426 | 0.440 | 0.400 | 0.397 | 0.405 | 0.395 |
| v4 | 0.370 | 0.372 | 0.348 | 0.337 | 0.346 | 0.312 |

**Bias (geometric mean est/ref)**

| Estimator | all (292) | all, dev (204) | all, test (88) | cleaned (262) | cleaned, dev (181) | cleaned, test (81) |
|---|---|---|---|---|---|---|
| constant | 1.26 | 1.28 | 1.24 | 1.02 | 1.01 | 1.06 |
| v1 | 0.75 | 0.74 | 0.75 | 0.71 | 0.69 | 0.75 |
| v3 | 0.86 | 0.86 | 0.86 | 0.85 | 0.83 | 0.88 |
| v4 | 0.98 | 0.99 | 0.96 | 0.89 | 0.88 | 0.92 |

**RMSE, kgCO2e/m2**

| Estimator | all (292) | all, dev (204) | all, test (88) | cleaned (262) | cleaned, dev (181) | cleaned, test (81) |
|---|---|---|---|---|---|---|
| constant | 78.6 | 80.1 | 74.8 | 74.7 | 74.5 | 75.2 |
| v1 | 79.7 | 82.0 | 74.1 | 78.1 | 78.7 | 76.7 |
| v3 | 76.0 | 78.7 | 69.2 | 74.5 | 76.0 | 71.2 |
| v4 | 73.0 | 75.0 | 68.2 | 71.6 | 72.2 | 70.4 |

v4 coverage with Wilson 95% CI: all 32.2% (27.1-37.8); all, dev 30.9% (24.9-37.5); all, test 35.2% (26.1-45.6); cleaned 34.7% (29.2-40.7); cleaned, dev 33.7% (27.2-40.9); cleaned, test 37.0% (27.3-47.9).

**Paired tests against v4**

| Set | Baseline | McNemar p (coverage) | Wilcoxon p (abs log) | v4 closer, % of buildings |
|---|---|---|---|---|
| all | v3 | 0.0354 | 6.11e-05 | 61.3 |
| all | v1 | 0.000158 | 6.89e-07 | 62.7 |
| all | constant | 0.025 | 5.72e-06 | 57.5 |
| cleaned | v3 | 0.0295 | 1.29e-05 | 61.8 |
| cleaned | v1 | 2.77e-05 | 1.9e-09 | 65.6 |
| cleaned | constant | 0.0495 | 0.00706 | 54.2 |
| all, test | v3 | 0.243 | 0.0594 | 59.1 |
| all, test | v1 | 0.0351 | 0.0277 | 59.1 |
| all, test | constant | 0.345 | 0.00498 | 61.4 |
| cleaned, test | v3 | 0.229 | 0.096 | 58.0 |
| cleaned, test | v1 | 0.0294 | 0.00786 | 61.7 |
| cleaned, test | constant | 0.442 | 0.0343 | 59.3 |

**Inside v4**

- Evidence lines parsed in 100.0% of answers.
- Reported range centred on 0.5 A + 0.5 B (within 3%) in 100.0% of those answers.
- Out-of-scope rule applied in 40 answers; 38 of them are buildings whose `lca_phys_scope` has no E (38 such answers in total).

| Source (mean of runs) | all | all, dev | all, test | cleaned | cleaned, dev | cleaned, test |
|---|---|---|---|---|---|---|
| A bottom-up only | 22.6 | 21.6 | 25.0 | 24.4 | 23.2 | 27.2 |
| B benchmark only | 30.1 | 32.4 | 25.0 | 32.8 | 35.4 | 27.2 |
| 0.5 A + 0.5 B recomputed | 32.2 | 30.9 | 35.2 | 34.7 | 33.7 | 37.0 |
| v4 as reported | 32.2 | 30.9 | 35.2 | 34.7 | 33.7 | 37.0 |

**Weight sensitivity with v4's own A and B** (coverage %, estimate = w A + (1 - w) B)

| w on bottom-up | all | all, dev | all, test | cleaned | cleaned, dev | cleaned, test |
|---|---|---|---|---|---|---|
| 0.0 | 30.1 | 32.4 | 25.0 | 32.8 | 35.4 | 27.2 |
| 0.2 | 31.5 | 32.4 | 29.5 | 34.4 | 35.4 | 32.1 |
| 0.3 | 31.2 | 31.4 | 30.7 | 34.0 | 34.3 | 33.3 |
| 0.4 | 32.5 | 32.4 | 33.0 | 35.5 | 35.4 | 35.8 |
| 0.5 | 32.2 | 30.9 | 35.2 | 34.7 | 33.7 | 37.0 |
| 0.6 | 30.8 | 30.9 | 30.7 | 33.2 | 33.7 | 32.1 |
| 0.7 | 29.1 | 30.4 | 26.1 | 31.3 | 32.6 | 28.4 |
| 0.8 | 27.7 | 27.5 | 28.4 | 29.8 | 29.3 | 30.9 |
| 1.0 | 22.6 | 21.6 | 25.0 | 24.4 | 23.2 | 27.2 |

Run-to-run CV of v4: 5.3%. Coverage of single runs (all): 31.8%, 32.2%, 34.2%.
