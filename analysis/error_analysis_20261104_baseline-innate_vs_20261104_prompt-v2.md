# Error analysis: 20261104_baseline-innate vs 20261104_prompt-v2

Enclosure A1–A3, kgCO2e/m² floor area; estimate = mean of run midpoints. est/true below 1 = underestimate.

## Accuracy

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| ±20% coverage % | 19.5 | 15.1 |
| RMSE | 79.7 | 81.0 |
| median APE % | 37.9 | 44.3 |
| geo-mean est/true | 0.75 | 0.67 |
| mean CV across runs % | 19.0 | 13.8 |

## 1 Compression

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| log-log slope est~truth (1 = none) | 0.46 | 0.55 |
| SD across buildings: estimate / truth | 0.39 | 0.47 |
| share of squared error from top 20 buildings % | 67.6 | 64.3 |
| median est/true, truth 0-25 | 1.58 | 1.27 |
| median est/true, truth 25-50 | 1.09 | 0.93 |
| median est/true, truth 50-100 | 0.76 | 0.71 |
| median est/true, truth 100-200 | 0.54 | 0.51 |
| median est/true, truth 200-max | 0.28 | 0.27 |

## 2 HFC-blown XPS

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| median est/true, projects with XPS | 0.67 | 0.58 |
| median est/true, projects without XPS | 0.80 | 0.71 |
| median est/true, XPS > 30% of truth | 0.59 | 0.50 |
| median est/(truth - XPS) | 0.84 | 0.77 |

## 3 Climate

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| median est/true, cold zones 5-8 | 0.65 | 0.61 |
| median est/true, warm zones 1-3 | 0.77 | 0.69 |
| median est/true, zone 4 | 0.76 | 0.65 |

## 4 Envelope area

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| median est/true, bldg_therm_env_area given | 0.81 | 0.75 |
| median est/true, not given | 0.65 | 0.57 |

## 5 Project type

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| median est/true, Major Renovation | 0.77 | 0.63 |
| median est/true, Minor Renovation | 0.85 | 0.56 |
| median est/true, New Construction | 0.71 | 0.65 |
| median est/true, Tenant Improvement | 0.24 | 0.26 |

## 6 Incomplete ground truth

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| median est/true, flagged incomplete (n=10) | 3.09 | 3.07 |
| ±20% coverage %, excluding flagged | 20.2 | 15.6 |

## 7 Reasoning text (% of answers mentioning)

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 |
|---|---|---|
| XPS | 0.57 | 29.7 |
| HFC / blowing agent | 0.00 | 4.00 |
| curtain wall | 36.0 | 42.7 |
| envelope area | 54.9 | 64.4 |
| mass_total | 8.56 | 14.4 |
| XPS, among projects that have XPS | 0.67 | 39.6 |
