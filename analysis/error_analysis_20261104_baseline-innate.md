# Error analysis: 20261104_baseline-innate

Enclosure A1–A3, kgCO2e/m² floor area; estimate = mean of run midpoints. est/true below 1 = underestimate.

## Accuracy

| diagnostic | 20261104_baseline-innate |
|---|---|
| ±20% coverage % | 19.5 |
| RMSE | 79.7 |
| median APE % | 37.9 |
| geo-mean est/true | 0.75 |
| mean CV across runs % | 19.0 |

## 1 Compression

| diagnostic | 20261104_baseline-innate |
|---|---|
| log-log slope est~truth (1 = none) | 0.46 |
| SD across buildings: estimate / truth | 0.39 |
| share of squared error from top 20 buildings % | 67.6 |
| median est/true, truth 0-25 | 1.58 |
| median est/true, truth 25-50 | 1.09 |
| median est/true, truth 50-100 | 0.76 |
| median est/true, truth 100-200 | 0.54 |
| median est/true, truth 200-max | 0.28 |

## 2 HFC-blown XPS

| diagnostic | 20261104_baseline-innate |
|---|---|
| median est/true, projects with XPS | 0.67 |
| median est/true, projects without XPS | 0.80 |
| median est/true, XPS > 30% of truth | 0.59 |
| median est/(truth - XPS) | 0.84 |

## 3 Climate

| diagnostic | 20261104_baseline-innate |
|---|---|
| median est/true, cold zones 5-8 | 0.65 |
| median est/true, warm zones 1-3 | 0.77 |
| median est/true, zone 4 | 0.76 |

## 4 Envelope area

| diagnostic | 20261104_baseline-innate |
|---|---|
| median est/true, bldg_therm_env_area given | 0.81 |
| median est/true, not given | 0.65 |

## 5 Project type

| diagnostic | 20261104_baseline-innate |
|---|---|
| median est/true, Major Renovation | 0.77 |
| median est/true, Minor Renovation | 0.85 |
| median est/true, New Construction | 0.71 |
| median est/true, Tenant Improvement | 0.24 |

## 6 Incomplete ground truth

| diagnostic | 20261104_baseline-innate |
|---|---|
| median est/true, flagged incomplete (n=10) | 3.09 |
| ±20% coverage %, excluding flagged | 20.2 |

## 7 Reasoning text (% of answers mentioning)

| diagnostic | 20261104_baseline-innate |
|---|---|
| XPS | 0.57 |
| HFC / blowing agent | 0.00 |
| curtain wall | 36.0 |
| envelope area | 54.9 |
| mass_total | 8.56 |
| XPS, among projects that have XPS | 0.67 |
