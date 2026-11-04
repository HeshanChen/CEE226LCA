# Run summary: 20261104_prompt-v3

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 76.0 | 47.3 | 90.7 | 40.0 | 0.86 | 25.0 | 12.5 | 78.0 | 66.6 |
| new construction only | 243 | 74.1 | 49.1 | 90.9 | 38.0 | 0.91 | 26.3 | 10.9 | 83.5 | 74.3 |
| excl. 10 incomplete ground truths | 282 | 76.5 | 47.1 | 59.7 | 37.4 | 0.83 | 25.9 | 12.6 | 79.5 | 67.7 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 91.2 | 50.6 | 49.4 | 36.5 | 0.79 | 20.7 | 13.5 | 76.8 | 59.3 |
| Zone 5A | 40 | 68.1 | 51.7 | 70.0 | 45.2 | 0.83 | 20.0 | 10.2 | 84.8 | 69.9 |
| Zone 3C | 33 | 59.6 | 42.0 | 315.7 | 36.7 | 1.26 | 36.4 | 11.3 | 64.9 | 72.3 |
| Zone 5B | 26 | 40.8 | 32.4 | 33.4 | 30.6 | 0.79 | 38.5 | 9.0 | 101.7 | 73.7 |
| Zone 3B | 23 | 35.1 | 25.6 | 60.6 | 45.6 | 1.01 | 17.4 | 13.3 | 50.5 | 40.8 |
| Zone 4A | 23 | 71.1 | 50.5 | 127.6 | 53.3 | 0.81 | 8.7 | 15.7 | 87.5 | 67.3 |
| Zone 1A | 12 | 83.9 | 58.0 | 60.8 | 40.6 | 0.73 | 16.7 | 13.0 | 80.6 | 75.7 |
| Other | 11 | 106.0 | 69.3 | 68.0 | 49.6 | 0.75 | 27.3 | 9.2 | 73.8 | 55.0 |
| Zone 3A | 10 | 84.6 | 49.1 | 60.8 | 35.3 | 0.88 | 30.0 | 19.3 | 56.0 | 68.8 |
| Zone 2A | 10 | 70.7 | 43.4 | 96.1 | 20.0 | 1.19 | 50.0 | 9.5 | 95.3 | 92.2 |
| Zone 2B | 7 | 97.1 | 56.2 | 40.2 | 25.7 | 0.55 | 42.9 | 15.6 | 101.5 | 85.3 |
| Zone 7 | 5 | 83.0 | 64.9 | 37.6 | 37.2 | 0.87 | 40.0 | 16.8 | 123.3 | 120.0 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 83.4 | 47.2 | 171.2 | 46.6 | 0.79 | 26.6 | 13.3 | 76.2 | 67.8 |
| Education | 55 | 66.4 | 43.7 | 54.3 | 33.9 | 0.90 | 21.8 | 11.3 | 85.6 | 82.2 |
| Residential: Multifamily (5 or more units) | 46 | 68.2 | 36.8 | 55.8 | 42.2 | 0.86 | 23.9 | 9.0 | 52.5 | 45.5 |
| Public Assembly | 31 | 105.6 | 76.2 | 75.1 | 52.5 | 0.99 | 16.1 | 13.1 | 95.8 | 96.7 |
| Laboratory | 23 | 59.0 | 43.4 | 41.6 | 35.7 | 0.64 | 30.4 | 11.7 | 86.4 | 57.2 |
| Warehouse and Storage | 21 | 59.6 | 36.9 | 55.8 | 33.8 | 1.09 | 38.1 | 14.0 | 64.4 | 69.5 |
| Healthcare | 13 | 40.5 | 28.7 | 67.9 | 32.0 | 1.23 | 23.1 | 9.9 | 70.5 | 57.5 |
| Public Order and Safety | 10 | 66.4 | 52.0 | 34.1 | 25.8 | 0.98 | 50.0 | 16.4 | 132.6 | 150.4 |
| Other | 10 | 64.5 | 52.9 | 151.7 | 61.4 | 0.60 | 10.0 | 16.8 | 80.1 | 55.2 |
| Transportation Hub | 9 | 60.1 | 50.8 | 34.8 | 31.4 | 0.80 | 33.3 | 10.4 | 157.2 | 136.7 |
| Lodging | 5 | 147.1 | 83.9 | 78.3 | 56.8 | 0.56 | 20.0 | 13.7 | 45.4 | 41.2 |
| Mercantile | 5 | 85.1 | 50.6 | 412.8 | 58.8 | 1.32 | 0.0 | 36.1 | 43.5 | 27.7 |
