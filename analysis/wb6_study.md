# Whole building (A-C): prompt wb6 (`20261116_wholebuilding-wb6`, 1 run(s), 292 buildings)

**In-sample by design**: the factors F and K and the typical ranges were fitted on the reference values of the same buildings (all except 13 extreme values). The test-split column is in-sample too.

| Estimator | coverage, all (292) | coverage, without extremes (279) | coverage, test split (88) | slope | lowest 15% | highest 15% | median abs log | bias |
|---|---|---|---|---|---|---|---|---|
| Best constant (414 for every building) | 34.6% | 36.2% | 42.0% | 0.00 | 0.0% | 0.0% | 0.344 | 1.05 |
| wb5 (0.2 A + 0.5 M + 0.3 B) | 53.4% | 55.9% | 61.4% | 0.59 | 29.5% | 31.8% | 0.182 | 1.04 |
| wb6: own estimate only (Step A) | 42.8% | 43.0% | 45.5% | 0.65 | 31.8% | 0.0% | 0.258 | 0.85 |
| wb6: mass route only (Step M) | 57.5% | 59.1% | 59.1% | 0.86 | 50.0% | 61.4% | 0.166 | 0.99 |
| wb6 (0.9 M + 0.1 A, kept inside the typical range) | 60.3% | 62.7% | 63.6% | 0.81 | 47.7% | 61.4% | 0.152 | 1.00 |
| Course reference, innate (Gemini, 10 runs) | 34.2% | – | – | – | – | – | – | – |
| Course reference, domain (papers) | 45.2% | – | – | – | – | – | – | – |
| Course reference, domain + ontology | 45.9% | – | – | – | – | – | – | – |
| Course reference, domain + benchmark | 36.3% | – | – | – | – | – | – | – |

wb6 coverage, all buildings: 176/292 = 60.3% (95% CI 54.6-65.7); wb5: 156/292 = 53.4%.
Reference above the band (underestimated): wb5 67, wb6 65. Reference below the band (overestimated): wb5 69, wb6 51.
Slope = least-squares slope of log estimate on log reference; 1 means the estimates spread as much as the references, below 1 means they are pulled toward the average.

Paired with wb5: 66 buildings move inside the band, 46 move outside (McNemar p = 0.0721).

**Did the model apply the tables?**

- Both evidence lines parsed in 100.0% of answers.
- M within 5% of mass intensity x F x K: 100.0%.
- Range centred on 0.9 M + 0.1 A, kept inside the typical range (within 3%): 100.0%.
- 0.9 M + 0.1 A fell outside the typical range for 27 buildings; the reported estimate sits at the range edge for 27 of them.

**Median estimate / reference by reference band** (1.00 = no bias)

| Reference, kgCO2e/m2 | n | wb5 | wb6 |
|---|---|---|---|
| 0-250 | 48 | 1.49 | 1.12 |
| 250-350 | 50 | 1.12 | 1.04 |
| 350-450 | 59 | 1.08 | 1.03 |
| 450-550 | 43 | 0.96 | 0.97 |
| 550-700 | 47 | 0.87 | 0.96 |
| 700- | 45 | 0.76 | 0.93 |
