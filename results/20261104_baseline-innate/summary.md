# Run summary: 20261104_baseline-innate

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 79.7 | 48.6 | 96.0 | 37.9 | 0.75 | 19.5 | 19.0 | 78.0 | 56.0 |
| new construction only | 243 | 77.4 | 50.2 | 93.4 | 37.5 | 0.76 | 18.9 | 17.3 | 83.5 | 59.5 |
| excl. 10 incomplete ground truths | 282 | 80.5 | 48.7 | 57.8 | 37.3 | 0.72 | 20.2 | 19.1 | 79.5 | 55.8 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 95.4 | 50.8 | 42.7 | 34.8 | 0.71 | 22.8 | 20.3 | 76.8 | 51.7 |
| Zone 5A | 40 | 76.3 | 55.2 | 62.6 | 46.9 | 0.68 | 15.0 | 16.8 | 84.8 | 57.9 |
| Zone 3C | 33 | 53.6 | 38.2 | 372.7 | 37.2 | 1.10 | 27.3 | 18.5 | 64.9 | 64.7 |
| Zone 5B | 26 | 49.0 | 37.1 | 34.8 | 35.3 | 0.65 | 23.1 | 18.5 | 101.7 | 57.5 |
| Zone 3B | 23 | 29.8 | 23.2 | 62.8 | 37.6 | 0.94 | 17.4 | 18.9 | 50.5 | 41.5 |
| Zone 4A | 23 | 78.0 | 52.8 | 167.4 | 55.2 | 0.71 | 13.0 | 20.0 | 87.5 | 52.5 |
| Zone 1A | 12 | 94.3 | 62.5 | 55.0 | 38.2 | 0.68 | 16.7 | 22.3 | 80.6 | 69.3 |
| Other | 11 | 95.7 | 63.2 | 53.1 | 49.9 | 0.69 | 9.1 | 18.5 | 73.8 | 50.5 |
| Zone 3A | 10 | 79.1 | 42.2 | 40.1 | 39.8 | 0.77 | 20.0 | 17.0 | 56.0 | 50.2 |
| Zone 2A | 10 | 65.5 | 51.4 | 88.1 | 41.0 | 0.89 | 10.0 | 14.5 | 95.3 | 67.8 |
| Zone 2B | 7 | 108.3 | 73.9 | 51.6 | 47.3 | 0.45 | 0.0 | 21.5 | 101.5 | 60.8 |
| Zone 7 | 5 | 119.4 | 85.7 | 39.9 | 34.5 | 0.57 | 40.0 | 15.1 | 123.3 | 80.8 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 90.0 | 49.8 | 207.5 | 37.3 | 0.76 | 21.9 | 21.7 | 76.2 | 57.2 |
| Education | 55 | 70.3 | 44.5 | 48.4 | 33.9 | 0.76 | 23.6 | 17.0 | 85.6 | 65.0 |
| Residential: Multifamily (5 or more units) | 46 | 66.4 | 34.6 | 48.1 | 37.7 | 0.79 | 30.4 | 18.1 | 52.5 | 44.4 |
| Public Assembly | 31 | 98.5 | 64.9 | 52.3 | 48.8 | 0.78 | 9.7 | 17.6 | 95.8 | 77.5 |
| Laboratory | 23 | 56.5 | 43.3 | 43.1 | 44.1 | 0.64 | 17.4 | 21.2 | 86.4 | 52.5 |
| Warehouse and Storage | 21 | 63.8 | 41.1 | 47.4 | 35.6 | 0.66 | 14.3 | 15.8 | 64.4 | 42.0 |
| Healthcare | 13 | 28.9 | 24.4 | 65.8 | 26.1 | 1.14 | 23.1 | 17.4 | 70.5 | 59.2 |
| Public Order and Safety | 10 | 85.4 | 67.4 | 38.4 | 37.0 | 0.66 | 0.0 | 16.1 | 132.6 | 98.3 |
| Other | 10 | 90.7 | 69.3 | 127.0 | 62.5 | 0.49 | 0.0 | 18.2 | 80.1 | 44.6 |
| Transportation Hub | 9 | 89.2 | 76.8 | 43.2 | 47.5 | 0.56 | 11.1 | 19.8 | 157.2 | 84.2 |
| Lodging | 5 | 149.0 | 84.8 | 73.2 | 62.8 | 0.61 | 40.0 | 26.1 | 45.4 | 35.7 |
| Mercantile | 5 | 102.1 | 57.6 | 599.6 | 69.6 | 1.54 | 0.0 | 27.5 | 43.5 | 34.2 |
