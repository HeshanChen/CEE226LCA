# Run summary: 20261116_prompt-v5

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 71.3 | 42.2 | 130.3 | 31.3 | 1.07 | 35.6 | 5.0 | 78.0 | 76.1 |
| new construction only | 243 | 70.2 | 43.1 | 95.9 | 27.9 | 1.03 | 37.4 | 4.6 | 83.5 | 78.8 |
| excl. 10 incomplete ground truths | 282 | 71.7 | 41.8 | 91.8 | 30.9 | 1.02 | 36.5 | 5.0 | 79.5 | 76.4 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 85.9 | 45.6 | 61.6 | 31.9 | 1.05 | 37.0 | 4.7 | 76.8 | 76.0 |
| Zone 5A | 40 | 61.0 | 40.3 | 53.8 | 34.7 | 0.96 | 37.5 | 3.9 | 84.8 | 79.1 |
| Zone 3C | 33 | 52.1 | 36.1 | 381.1 | 26.5 | 1.39 | 42.4 | 4.6 | 64.9 | 73.4 |
| Zone 5B | 26 | 31.4 | 24.7 | 26.2 | 24.7 | 0.88 | 38.5 | 4.0 | 101.7 | 73.2 |
| Zone 3B | 23 | 28.3 | 21.5 | 68.0 | 29.8 | 1.29 | 39.1 | 6.9 | 50.5 | 57.2 |
| Zone 4A | 23 | 70.0 | 48.1 | 512.9 | 51.7 | 1.24 | 21.7 | 4.9 | 87.5 | 76.2 |
| Zone 1A | 12 | 81.3 | 53.8 | 48.8 | 33.4 | 0.82 | 25.0 | 3.6 | 80.6 | 79.8 |
| Other | 11 | 88.7 | 60.6 | 69.2 | 40.4 | 0.95 | 27.3 | 5.4 | 73.8 | 77.0 |
| Zone 3A | 10 | 95.7 | 57.2 | 80.2 | 36.3 | 1.23 | 30.0 | 9.4 | 56.0 | 67.5 |
| Zone 2A | 10 | 66.1 | 45.2 | 89.9 | 22.9 | 1.13 | 50.0 | 5.0 | 95.3 | 85.0 |
| Zone 2B | 7 | 107.7 | 62.4 | 55.9 | 32.1 | 0.92 | 28.6 | 5.5 | 101.5 | 81.5 |
| Zone 7 | 5 | 74.1 | 58.2 | 34.4 | 25.5 | 0.93 | 20.0 | 7.7 | 123.3 | 152.9 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 78.8 | 45.6 | 226.7 | 38.9 | 1.12 | 29.7 | 4.7 | 76.2 | 77.9 |
| Education | 55 | 64.4 | 37.8 | 45.6 | 22.7 | 0.97 | 43.6 | 5.4 | 85.6 | 81.7 |
| Residential: Multifamily (5 or more units) | 46 | 64.7 | 32.0 | 51.3 | 27.1 | 0.96 | 37.0 | 3.9 | 52.5 | 50.2 |
| Public Assembly | 31 | 98.5 | 68.3 | 70.7 | 40.9 | 1.11 | 22.6 | 8.1 | 95.8 | 102.2 |
| Laboratory | 23 | 38.1 | 28.6 | 53.2 | 32.1 | 1.10 | 43.5 | 4.0 | 86.4 | 85.8 |
| Warehouse and Storage | 21 | 57.9 | 33.5 | 48.2 | 27.1 | 1.00 | 42.9 | 3.9 | 64.4 | 64.6 |
| Healthcare | 13 | 41.5 | 30.2 | 86.4 | 31.7 | 1.36 | 38.5 | 3.4 | 70.5 | 63.4 |
| Public Order and Safety | 10 | 61.6 | 41.6 | 24.8 | 16.7 | 0.94 | 60.0 | 5.1 | 132.6 | 136.4 |
| Other | 10 | 63.0 | 49.7 | 136.6 | 41.2 | 1.15 | 20.0 | 4.6 | 80.1 | 74.4 |
| Transportation Hub | 9 | 45.0 | 36.3 | 32.0 | 25.5 | 1.13 | 44.4 | 5.4 | 157.2 | 164.5 |
| Lodging | 5 | 135.3 | 79.9 | 96.3 | 39.6 | 0.83 | 0.0 | 2.7 | 45.4 | 64.9 |
| Mercantile | 5 | 101.4 | 66.9 | 2147.9 | 66.6 | 3.31 | 20.0 | 9.4 | 43.5 | 66.0 |
