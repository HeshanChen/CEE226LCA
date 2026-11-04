# Error analysis: 20261104_baseline-innate vs 20261104_prompt-v2 vs 20261104_prompt-v3 (test split)

Enclosure A1–A3, kgCO2e/m² floor area; estimate = mean of run midpoints. est/true below 1 = underestimate.

## Accuracy

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| ±20% coverage % | 20.5 | 18.2 | 26.1 |
| RMSE | 74.1 | 75.7 | 69.2 |
| median APE % | 36.4 | 43.4 | 37.0 |
| geo-mean est/true | 0.75 | 0.66 | 0.86 |
| mean CV across runs % | 19.2 | 15.2 | 11.2 |

## 1 Compression

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| log-log slope est~truth (1 = none) | 0.52 | 0.63 | 0.68 |
| SD across buildings: estimate / truth | 0.42 | 0.48 | 0.65 |
| share of squared error from top 20 buildings % | 92.1 | 89.2 | 89.2 |
| median est/true, truth 0-25 | 1.57 | 1.15 | 1.76 |
| median est/true, truth 25-50 | 1.07 | 0.89 | 1.04 |
| median est/true, truth 50-100 | 0.77 | 0.66 | 0.92 |
| median est/true, truth 100-200 | 0.70 | 0.59 | 0.85 |
| median est/true, truth 200-max | 0.30 | 0.28 | 0.42 |

## 2 HFC-blown XPS

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, projects with XPS | 0.69 | 0.58 | 0.79 |
| median est/true, projects without XPS | 0.82 | 0.72 | 0.97 |
| median est/true, XPS > 30% of truth | 0.63 | 0.49 | 0.63 |
| median est/(truth - XPS) | 0.91 | 0.82 | 1.06 |

## 3 Climate

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, cold zones 5-8 | 0.76 | 0.69 | 0.91 |
| median est/true, warm zones 1-3 | 0.83 | 0.74 | 0.99 |
| median est/true, zone 4 | 0.69 | 0.56 | 0.73 |

## 4 Envelope area

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, bldg_therm_env_area given | 0.83 | 0.76 | 0.94 |
| median est/true, not given | 0.66 | 0.55 | 0.67 |

## 5 Project type

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, Major Renovation | 0.84 | 0.70 | 0.87 |
| median est/true, Minor Renovation | 0.92 | 0.61 | 0.77 |
| median est/true, New Construction | 0.77 | 0.65 | 0.88 |
| median est/true, Tenant Improvement | 0.09 | 0.09 | 0.09 |

## 6 Incomplete ground truth

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| median est/true, flagged incomplete (n=2) | 4.25 | 4.58 | 5.91 |
| ±20% coverage %, excluding flagged | 20.9 | 18.6 | 26.7 |

## 7 Reasoning text (% of answers mentioning)

| diagnostic | 20261104_baseline-innate | 20261104_prompt-v2 | 20261104_prompt-v3 |
|---|---|---|---|
| XPS | 0.76 | 26.9 | 89.8 |
| HFC / blowing agent | 0.00 | 5.30 | 86.4 |
| curtain wall | 32.6 | 39.8 | 40.5 |
| envelope area | 56.1 | 66.3 | 56.8 |
| mass_total | 7.95 | 14.8 | 12.5 |
| XPS, among projects that have XPS | 1.75 | 43.9 | 93.9 |
