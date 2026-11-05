# Feature study (prompt v3)

Paired with the full 48-feature set ('all') on run 0 of every condition. Δ < 0 in |log err| = better than all.
Missing conditions: ['no-code_year', 'no-geometry', 'no-site', 'no-size', 'no-structure', 'no-thermal', 'no-use_type']

## all split, run 0

| condition | features | n | coverage % | median |log err| | geo-mean est/true | RMSE | Δ coverage pp | Δ median |log err| | McNemar p | Wilcoxon p | closer than all % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| all | 48 | 292 | 24.3 | 0.461 | 0.860 | 77.8 | 0.000 | 0.000 | 1.0 | 1.0 | 0.000 |
| early | 39 | 292 | 21.6 | 0.462 | 0.877 | 81.2 | -2.7 | 0.001 | 0.302 | 0.130 | 44.5 |
| env | 15 | 292 | 19.9 | 0.463 | 0.925 | 80.6 | -4.5 | 0.001 | 0.085 | 0.334 | 47.6 |
| min | 10 | 292 | 25.3 | 0.476 | 0.807 | 77.3 | 1.0 | 0.015 | 0.828 | 0.811 | 50.0 |
| no-lca | 40 | 292 | 25.3 | 0.441 | 0.900 | 78.6 | 1.0 | -0.020 | 0.771 | 0.571 | 52.4 |
| no-mass | 47 | 292 | 22.6 | 0.452 | 0.853 | 79.2 | -1.7 | -0.009 | 0.560 | 0.917 | 51.0 |

## dev split, run 0

| condition | features | n | coverage % | median |log err| | geo-mean est/true | RMSE | Δ coverage pp | Δ median |log err| | McNemar p | Wilcoxon p | closer than all % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| all | 48 | 204 | 22.5 | 0.485 | 0.858 | 80.8 | 0.000 | 0.000 | 1.0 | 1.0 | 0.000 |
| early | 39 | 204 | 22.1 | 0.492 | 0.875 | 84.6 | -0.490 | 0.006 | 1.0 | 0.495 | 46.6 |
| env | 15 | 204 | 20.6 | 0.467 | 0.924 | 84.1 | -2.0 | -0.018 | 0.597 | 0.937 | 50.5 |
| min | 10 | 204 | 23.0 | 0.489 | 0.801 | 79.5 | 0.490 | 0.004 | 1.0 | 0.717 | 48.5 |
| no-lca | 40 | 204 | 25.5 | 0.433 | 0.897 | 82.3 | 2.9 | -0.052 | 0.392 | 0.312 | 55.4 |
| no-mass | 47 | 204 | 22.1 | 0.462 | 0.852 | 83.2 | -0.490 | -0.023 | 1.0 | 0.863 | 52.0 |

## test split, run 0

| condition | features | n | coverage % | median |log err| | geo-mean est/true | RMSE | Δ coverage pp | Δ median |log err| | McNemar p | Wilcoxon p | closer than all % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| all | 48 | 88 | 28.4 | 0.422 | 0.865 | 70.3 | 0.000 | 0.000 | 1.0 | 1.0 | 0.000 |
| early | 39 | 88 | 20.5 | 0.448 | 0.881 | 72.7 | -8.0 | 0.026 | 0.065 | 0.084 | 39.8 |
| env | 15 | 88 | 18.2 | 0.424 | 0.927 | 71.9 | -10.2 | 0.002 | 0.049 | 0.112 | 40.9 |
| min | 10 | 88 | 30.7 | 0.411 | 0.822 | 72.0 | 2.3 | -0.011 | 0.851 | 0.323 | 53.4 |
| no-lca | 40 | 88 | 25.0 | 0.455 | 0.908 | 69.3 | -3.4 | 0.032 | 0.581 | 0.569 | 45.5 |
| no-mass | 47 | 88 | 23.9 | 0.397 | 0.854 | 69.2 | -4.5 | -0.025 | 0.424 | 0.941 | 48.9 |
