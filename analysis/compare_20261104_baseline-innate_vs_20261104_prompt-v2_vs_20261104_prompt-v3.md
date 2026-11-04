# Prompt comparison: 20261104_baseline-innate vs 20261104_prompt-v2 vs 20261104_prompt-v3

Enclosure A1–A3, kgCO2e/m² floor area. Estimate = mean of run midpoints. Split from analysis/make_split.py (seed 226, 30% test, assigned after the runs).

## all (n=292)

| run | ±20% coverage (95% CI) | RMSE | median APE | median abs log error | est/true geo-mean | CV across runs |
|---|---|---|---|---|---|---|
| 20261104_baseline-innate | 19.5% (15.4–24.5) | 79.7 | 37.9% | 0.456 | 0.75 | 19.0% |
| 20261104_prompt-v2 | 15.1% (11.4–19.6) | 81.0 | 44.3% | 0.563 | 0.67 | 13.8% |
| 20261104_prompt-v3 | 25.0% (20.4–30.3) | 76.0 | 40.0% | 0.426 | 0.86 | 12.5% |

| pair | inside only A / only B | McNemar p | median abs log error A → B | Wilcoxon p | B closer |
|---|---|---|---|---|---|
| A=20261104_baseline-innate, B=20261104_prompt-v2 | 31 / 18 | 0.085 | 0.456 → 0.563 | 0.0000 | 34% |
| A=20261104_baseline-innate, B=20261104_prompt-v3 | 30 / 46 | 0.085 | 0.456 → 0.426 | 0.0533 | 57% |
| A=20261104_prompt-v2, B=20261104_prompt-v3 | 28 / 57 | 0.002 | 0.563 → 0.426 | 0.0000 | 66% |

## dev (n=204)

| run | ±20% coverage (95% CI) | RMSE | median APE | median abs log error | est/true geo-mean | CV across runs |
|---|---|---|---|---|---|---|
| 20261104_baseline-innate | 19.1% (14.3–25.1) | 82.0 | 40.3% | 0.476 | 0.74 | 18.9% |
| 20261104_prompt-v2 | 13.7% (9.7–19.1) | 83.2 | 46.3% | 0.580 | 0.67 | 13.2% |
| 20261104_prompt-v3 | 24.5% (19.1–30.8) | 78.7 | 41.6% | 0.440 | 0.86 | 13.1% |

| pair | inside only A / only B | McNemar p | median abs log error A → B | Wilcoxon p | B closer |
|---|---|---|---|---|---|
| A=20261104_baseline-innate, B=20261104_prompt-v2 | 22 / 11 | 0.080 | 0.476 → 0.580 | 0.0000 | 33% |
| A=20261104_baseline-innate, B=20261104_prompt-v3 | 21 / 32 | 0.169 | 0.476 → 0.440 | 0.0818 | 57% |
| A=20261104_prompt-v2, B=20261104_prompt-v3 | 17 / 39 | 0.005 | 0.580 → 0.440 | 0.0000 | 68% |

## test (n=88)

| run | ±20% coverage (95% CI) | RMSE | median APE | median abs log error | est/true geo-mean | CV across runs |
|---|---|---|---|---|---|---|
| 20261104_baseline-innate | 20.5% (13.3–30.0) | 74.1 | 36.4% | 0.393 | 0.75 | 19.2% |
| 20261104_prompt-v2 | 18.2% (11.5–27.5) | 75.7 | 43.4% | 0.511 | 0.66 | 15.2% |
| 20261104_prompt-v3 | 26.1% (18.1–36.2) | 69.2 | 37.0% | 0.400 | 0.86 | 11.2% |

| pair | inside only A / only B | McNemar p | median abs log error A → B | Wilcoxon p | B closer |
|---|---|---|---|---|---|
| A=20261104_baseline-innate, B=20261104_prompt-v2 | 9 / 7 | 0.804 | 0.393 → 0.511 | 0.0002 | 34% |
| A=20261104_baseline-innate, B=20261104_prompt-v3 | 9 / 14 | 0.405 | 0.393 → 0.400 | 0.3787 | 55% |
| A=20261104_prompt-v2, B=20261104_prompt-v3 | 11 / 18 | 0.265 | 0.511 → 0.400 | 0.0018 | 62% |
