# Run summary: 20261105_domain-envelope

Enclosure (Shell - Enclosure), A1–A3, kgCO2e per m² floor area. Estimate = mean of the parsed run midpoints per building (BEST rows: mean of the BEST lines, prompt v2). Incomplete ground truth = new construction with no fenestration GWP in the source LCA. APE = |estimate − truth| / truth. Coverage = truth inside estimate ±20%. CV = SD / mean of a building's run midpoints.

## Overall

| subset | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| all projects | 292 | 85.3 | 54.3 | 76.8 | 51.1 | 0.61 | 15.8 | nan | 78.0 | 45.0 |
| new construction only | 243 | 83.7 | 56.4 | 73.7 | 48.2 | 0.61 | 14.0 | nan | 83.5 | 49.0 |
| excl. 10 incomplete ground truths | 282 | 86.3 | 54.8 | 57.8 | 48.7 | 0.58 | 16.3 | nan | 79.5 | 45.0 |

## By climate zone

| climate | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Zone 4C | 92 | 100.2 | 56.1 | 46.6 | 50.0 | 0.59 | 26.1 | nan | 76.8 | 40.0 |
| Zone 5A | 40 | 84.4 | 64.0 | 65.9 | 62.1 | 0.51 | 10.0 | nan | 84.8 | 46.8 |
| Zone 3C | 33 | 60.2 | 43.9 | 208.1 | 47.6 | 0.87 | 12.1 | nan | 64.9 | 48.5 |
| Zone 5B | 26 | 56.5 | 45.8 | 43.7 | 42.0 | 0.53 | 7.7 | nan | 101.7 | 47.8 |
| Zone 3B | 23 | 34.1 | 24.9 | 58.8 | 42.8 | 0.79 | 13.0 | nan | 50.5 | 42.5 |
| Zone 4A | 23 | 84.3 | 55.6 | 128.5 | 62.8 | 0.58 | 17.4 | nan | 87.5 | 45.0 |
| Zone 1A | 12 | 97.2 | 67.5 | 55.3 | 45.4 | 0.61 | 16.7 | nan | 80.6 | 58.0 |
| Other | 11 | 91.8 | 63.6 | 50.4 | 65.5 | 0.53 | 9.1 | nan | 73.8 | 36.0 |
| Zone 3A | 10 | 86.4 | 49.7 | 48.6 | 47.2 | 0.59 | 10.0 | nan | 56.0 | 40.2 |
| Zone 2A | 10 | 71.2 | 58.9 | 85.2 | 47.2 | 0.72 | 0.0 | nan | 95.3 | 60.0 |
| Zone 2B | 7 | 124.4 | 82.0 | 55.8 | 43.8 | 0.38 | 0.0 | nan | 101.5 | 55.0 |
| Zone 7 | 5 | 128.0 | 95.5 | 48.0 | 45.3 | 0.46 | 20.0 | nan | 123.3 | 67.5 |

## By primary use

| bldg_prim_use | n | RMSE | MAE | MAPE % | median APE % | geo-mean est/true | ±20% coverage % | mean CV across runs % | median truth | median estimate |
|---|---|---|---|---|---|---|---|---|---|---|
| Office | 64 | 98.5 | 56.6 | 125.7 | 53.5 | 0.60 | 17.2 | nan | 76.2 | 44.2 |
| Education | 55 | 77.1 | 51.7 | 52.1 | 45.1 | 0.61 | 25.5 | nan | 85.6 | 50.0 |
| Residential: Multifamily (5 or more units) | 46 | 70.4 | 39.2 | 48.5 | 46.4 | 0.62 | 21.7 | nan | 52.5 | 33.5 |
| Public Assembly | 31 | 101.4 | 69.4 | 52.4 | 59.1 | 0.62 | 12.9 | nan | 95.8 | 51.5 |
| Laboratory | 23 | 65.2 | 51.9 | 49.6 | 46.1 | 0.49 | 13.0 | nan | 86.4 | 41.5 |
| Warehouse and Storage | 21 | 66.4 | 44.0 | 52.3 | 43.4 | 0.62 | 9.5 | nan | 64.4 | 42.5 |
| Healthcare | 13 | 35.8 | 29.7 | 56.4 | 46.3 | 0.88 | 7.7 | nan | 70.5 | 49.0 |
| Public Order and Safety | 10 | 88.3 | 71.5 | 41.9 | 40.7 | 0.61 | 0.0 | nan | 132.6 | 93.8 |
| Other | 10 | 98.5 | 75.9 | 138.9 | 68.6 | 0.44 | 0.0 | nan | 80.1 | 36.8 |
| Transportation Hub | 9 | 91.0 | 78.7 | 46.0 | 49.1 | 0.51 | 11.1 | nan | 157.2 | 82.5 |
| Lodging | 5 | 153.5 | 89.8 | 74.5 | 76.9 | 0.51 | 0.0 | nan | 45.4 | 27.5 |
| Mercantile | 5 | 104.7 | 60.6 | 417.3 | 70.6 | 1.16 | 0.0 | nan | 43.5 | 20.0 |
