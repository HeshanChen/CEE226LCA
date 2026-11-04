# Run summary: 20261104_prompt-v2

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 81.0 | 51.5 | 83.0 | 44.3 | 0.67 | 15.1 | 13.8 | 78.0 | 51.7 |
| new construction only | 243 | 79.8 | 53.5 | 81.7 | 44.2 | 0.70 | 16.5 | 11.8 | 83.5 | 55.7 |
| excl. 10 incomplete ground truths | 282 | 81.9 | 51.8 | 57.7 | 43.9 | 0.64 | 15.6 | 13.5 | 79.5 | 51.8 |
| all projects, BEST estimate | 292 | 83.2 | 53.4 | 81.4 | 49.4 | 0.59 | 14.4 | 13.8 | 78.0 | 48.0 |
| excl. incomplete, BEST estimate | 282 | 84.2 | 53.7 | 57.9 | 48.8 | 0.57 | 14.9 | 13.5 | 79.5 | 48.0 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 94.6 | 52.9 | 46.1 | 43.0 | 0.63 | 18.5 | 15.2 | 76.8 | 46.1 |
| Zone 5A | 40 | 76.8 | 56.4 | 63.8 | 52.0 | 0.64 | 15.0 | 11.8 | 84.8 | 55.2 |
| Zone 3C | 33 | 61.3 | 45.2 | 267.5 | 43.0 | 0.95 | 6.1 | 12.7 | 64.9 | 54.7 |
| Zone 5B | 26 | 50.8 | 42.3 | 42.5 | 44.3 | 0.58 | 7.7 | 11.2 | 101.7 | 51.2 |
| Zone 3B | 23 | 32.9 | 24.4 | 51.3 | 38.2 | 0.78 | 21.7 | 16.8 | 50.5 | 35.5 |
| Zone 4A | 23 | 82.0 | 53.9 | 125.4 | 49.0 | 0.64 | 21.7 | 12.5 | 87.5 | 53.7 |
| Zone 1A | 12 | 96.9 | 66.4 | 62.6 | 42.1 | 0.60 | 8.3 | 15.7 | 80.6 | 62.1 |
| Other | 11 | 102.7 | 68.6 | 59.1 | 60.9 | 0.60 | 27.3 | 13.1 | 73.8 | 42.3 |
| Zone 3A | 10 | 91.8 | 57.6 | 69.1 | 50.7 | 0.74 | 10.0 | 14.1 | 56.0 | 50.2 |
| Zone 2A | 10 | 64.6 | 50.4 | 77.1 | 42.2 | 0.82 | 10.0 | 11.2 | 95.3 | 61.2 |
| Zone 2B | 7 | 109.0 | 71.8 | 52.1 | 44.2 | 0.42 | 14.3 | 18.4 | 101.5 | 60.2 |
| Zone 7 | 5 | 98.6 | 78.6 | 41.8 | 39.2 | 0.63 | 0.0 | 10.5 | 123.3 | 75.0 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 89.2 | 52.8 | 150.5 | 44.1 | 0.65 | 14.1 | 15.6 | 76.2 | 51.7 |
| Education | 55 | 71.5 | 47.4 | 49.1 | 42.3 | 0.68 | 20.0 | 12.9 | 85.6 | 60.0 |
| Residential: Multifamily (5 or more units) | 46 | 71.5 | 39.7 | 53.1 | 44.7 | 0.66 | 17.4 | 11.0 | 52.5 | 36.0 |
| Public Assembly | 31 | 105.5 | 72.7 | 63.0 | 52.3 | 0.76 | 9.7 | 15.8 | 95.8 | 72.5 |
| Laboratory | 23 | 63.2 | 48.8 | 48.6 | 44.4 | 0.53 | 17.4 | 12.7 | 86.4 | 42.2 |
| Warehouse and Storage | 21 | 64.5 | 40.8 | 51.8 | 36.7 | 0.74 | 23.8 | 13.6 | 64.4 | 49.7 |
| Healthcare | 13 | 37.2 | 30.9 | 61.5 | 39.6 | 0.96 | 7.7 | 11.3 | 70.5 | 47.7 |
| Public Order and Safety | 10 | 83.3 | 61.8 | 35.1 | 35.1 | 0.66 | 20.0 | 11.2 | 132.6 | 101.2 |
| Other | 10 | 82.0 | 68.3 | 138.3 | 68.1 | 0.43 | 0.0 | 19.9 | 80.1 | 40.6 |
| Transportation Hub | 9 | 71.2 | 62.2 | 38.8 | 38.5 | 0.64 | 0.0 | 9.0 | 157.2 | 96.7 |
| Lodging | 5 | 151.8 | 86.1 | 64.3 | 66.9 | 0.51 | 0.0 | 21.8 | 45.4 | 31.5 |
| Mercantile | 5 | 101.2 | 60.7 | 417.3 | 67.8 | 0.97 | 20.0 | 17.8 | 43.5 | 17.3 |
