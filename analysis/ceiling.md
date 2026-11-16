# What coverage can the features support?

Coverage = share of buildings whose reference value lies within the estimate +/-20%.

| Target | Buildings | sd of log value | Median as constant | Best constant |
|---|---|---|---|---|
| Whole building A-C (course reference task) | 292 | 0.66 | 32.9% | 34.6% (at 414) |
| Enclosure A1-A3, all | 292 | 0.98 | 26.0% | 27.1% (at 80) |
| Enclosure A1-A3, cleaned | 262 | 0.65 | 28.6% | 30.2% (at 80) |

| Enclosure A1-A3 | Buildings | Random forest, CV | Gradient boosting, CV | Random forest, in-sample |
|---|---|---|---|---|
| all | 292 | 26.0% | 28.4% | 55.8% |
| cleaned | 262 | 34.0% | 34.0% | 60.7% |

Reading: a model trained on this dataset itself, with all 48 features, predicts unseen buildings only a few points better than one constant. Coverage far above that on these buildings can only come from fitting the same buildings that are scored (the in-sample column).
