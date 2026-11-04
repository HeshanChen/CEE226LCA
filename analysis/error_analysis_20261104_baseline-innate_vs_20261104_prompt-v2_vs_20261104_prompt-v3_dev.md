# Error analysis: 20261104_baseline-innate vs 20261104_prompt-v2 vs 20261104_prompt-v3 (dev split)

Enclosure A1–A3, kgCO2e/m² floor area; estimate = mean of run midpoints. est/true below 1 = underestimate.

## Accuracy

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| ±20% coverage % | 19.1 | 13.7 | 24.5 |
| RMSE | 82.0 | 83.2 | 78.7 |
| median APE % | 40.3 | 46.3 | 41.6 |
| geo-mean est/true | 0.74 | 0.67 | 0.86 |
| mean CV across runs % | 18.9 | 13.2 | 13.1 |

## 1 Compression

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| log-log slope est~truth (1 = none) | 0.44 | 0.52 | 0.56 |
| SD across buildings: estimate / truth | 0.38 | 0.46 | 0.62 |
| share of squared error from top 20 buildings % | 75.8 | 72.6 | 74.9 |
| median est/true, truth 0-25 | 1.59 | 1.27 | 1.31 |
| median est/true, truth 25-50 | 1.11 | 1.08 | 1.38 |
| median est/true, truth 50-100 | 0.75 | 0.72 | 0.89 |
| median est/true, truth 100-200 | 0.52 | 0.48 | 0.64 |
| median est/true, truth 200-max | 0.28 | 0.26 | 0.33 |

## 2 HFC-blown XPS

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, projects with XPS | 0.66 | 0.58 | 0.73 |
| median est/true, projects without XPS | 0.77 | 0.69 | 0.97 |
| median est/true, XPS > 30% of truth | 0.54 | 0.51 | 0.57 |
| median est/(truth - XPS) | 0.80 | 0.74 | 0.95 |

## 3 Climate

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, cold zones 5-8 | 0.64 | 0.56 | 0.76 |
| median est/true, warm zones 1-3 | 0.71 | 0.68 | 0.95 |
| median est/true, zone 4 | 0.78 | 0.68 | 0.81 |

## 4 Envelope area

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, bldg_therm_env_area given | 0.79 | 0.75 | 1.02 |
| median est/true, not given | 0.65 | 0.57 | 0.75 |

## 5 Project type

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, Major Renovation | 0.68 | 0.62 | 0.65 |
| median est/true, Minor Renovation | 0.79 | 0.40 | 0.67 |
| median est/true, New Construction | 0.69 | 0.65 | 0.87 |
| median est/true, Tenant Improvement | 0.53 | 0.42 | 0.48 |

## 6 Incomplete ground truth

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, flagged incomplete (n=8) | 3.09 | 3.07 | 3.67 |
| ±20% coverage %, excluding flagged | 19.9 | 14.3 | 25.5 |

## 7 Reasoning text (% of answers mentioning)

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| XPS | 0.49 | 30.9 | 90.2 |
| HFC / blowing agent | 0.00 | 3.43 | 88.6 |
| curtain wall | 37.4 | 44.0 | 48.9 |
| envelope area | 54.4 | 63.6 | 60.5 |
| mass_total | 8.82 | 14.2 | 13.7 |
| XPS, among projects that have XPS | 0.30 | 38.1 | 96.7 |
