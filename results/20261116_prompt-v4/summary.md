# Run summary: 20261116_prompt-v4

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 73.0 | 43.1 | 123.9 | 33.9 | 0.98 | 32.2 | 5.3 | 78.0 | 70.7 |
| new construction only | 243 | 71.7 | 44.3 | 89.5 | 32.5 | 0.94 | 34.6 | 4.9 | 83.5 | 73.7 |
| excl. 10 incomplete ground truths | 282 | 73.6 | 43.0 | 88.4 | 32.5 | 0.94 | 33.0 | 5.4 | 79.5 | 70.8 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 87.0 | 46.1 | 54.5 | 34.3 | 0.96 | 29.3 | 5.0 | 76.8 | 67.2 |
| Zone 5A | 40 | 66.6 | 43.7 | 52.8 | 37.7 | 0.88 | 40.0 | 4.8 | 84.8 | 75.5 |
| Zone 3C | 33 | 53.7 | 38.0 | 353.1 | 36.7 | 1.28 | 36.4 | 4.8 | 64.9 | 66.7 |
| Zone 5B | 26 | 35.0 | 27.5 | 27.9 | 27.8 | 0.82 | 30.8 | 5.7 | 101.7 | 67.8 |
| Zone 3B | 23 | 28.8 | 20.8 | 70.0 | 22.9 | 1.23 | 39.1 | 4.6 | 50.5 | 61.7 |
| Zone 4A | 23 | 74.3 | 49.9 | 516.4 | 45.4 | 1.11 | 17.4 | 8.2 | 87.5 | 70.8 |
| Zone 1A | 12 | 91.8 | 56.8 | 45.0 | 25.9 | 0.72 | 41.7 | 5.2 | 80.6 | 72.6 |
| Other | 11 | 89.4 | 60.0 | 63.6 | 45.6 | 0.87 | 18.2 | 6.1 | 73.8 | 74.2 |
| Zone 3A | 10 | 84.5 | 49.0 | 67.1 | 35.6 | 1.14 | 40.0 | 8.0 | 56.0 | 68.6 |
| Zone 2A | 10 | 55.2 | 40.7 | 72.4 | 23.2 | 1.01 | 40.0 | 5.8 | 95.3 | 77.2 |
| Zone 2B | 7 | 107.9 | 61.3 | 54.1 | 36.1 | 0.91 | 28.6 | 2.8 | 101.5 | 79.3 |
| Zone 7 | 5 | 86.6 | 67.4 | 35.6 | 42.6 | 0.78 | 20.0 | 4.3 | 123.3 | 117.8 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 84.1 | 47.6 | 205.6 | 40.3 | 0.99 | 23.4 | 5.7 | 76.2 | 68.6 |
| Education | 55 | 64.5 | 38.9 | 43.8 | 23.3 | 0.94 | 41.8 | 4.9 | 85.6 | 79.2 |
| Residential: Multifamily (5 or more units) | 46 | 66.4 | 33.6 | 53.0 | 32.3 | 0.91 | 32.6 | 4.9 | 52.5 | 48.2 |
| Public Assembly | 31 | 93.8 | 59.4 | 53.6 | 44.3 | 0.94 | 29.0 | 7.2 | 95.8 | 87.0 |
| Laboratory | 23 | 46.8 | 34.2 | 59.0 | 30.4 | 0.96 | 34.8 | 3.8 | 86.4 | 73.7 |
| Warehouse and Storage | 21 | 58.6 | 34.0 | 44.5 | 20.2 | 0.93 | 42.9 | 4.9 | 64.4 | 60.3 |
| Healthcare | 13 | 36.4 | 29.7 | 84.2 | 35.1 | 1.31 | 30.8 | 3.5 | 70.5 | 64.7 |
| Public Order and Safety | 10 | 61.3 | 43.8 | 28.3 | 19.4 | 1.00 | 60.0 | 4.4 | 132.6 | 141.6 |
| Other | 10 | 72.0 | 55.7 | 135.2 | 46.9 | 1.08 | 10.0 | 4.8 | 80.1 | 70.5 |
| Transportation Hub | 9 | 53.3 | 44.9 | 30.8 | 30.9 | 0.92 | 33.3 | 3.9 | 157.2 | 135.5 |
| Lodging | 5 | 135.1 | 79.3 | 91.8 | 39.3 | 0.81 | 0.0 | 3.6 | 45.4 | 61.2 |
| Mercantile | 5 | 104.3 | 66.3 | 2152.7 | 69.6 | 2.89 | 20.0 | 18.6 | 43.5 | 57.0 |
