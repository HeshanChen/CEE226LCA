# Would a typical-range prompt (wb6-style) work for the enclosure?

Prompt v5's answers (`20261116_prompt-v5`, 3 runs, 292 buildings); no new LLM run. All fitted numbers are in-sample unless marked as a held-out check.

## 1. Where v5 over- and underestimates

| Reference decile, kgCO2e/m2 | n | median reference | median v5 | v5 / reference | inside ±20% | over | under |
|---|---|---|---|---|---|---|---|
| 0.5–22.5 | 30 | 10.5 | 45.6 | 3.27 | 7% | 73% | 20% |
| 22.5–39.0 | 29 | 29.2 | 60.4 | 1.89 | 7% | 90% | 3% |
| 39.0–53.5 | 29 | 46.5 | 57.2 | 1.26 | 48% | 52% | 0% |
| 53.5–66.2 | 29 | 60.6 | 67.6 | 1.13 | 59% | 38% | 3% |
| 66.2–78.0 | 29 | 71.4 | 78.6 | 1.06 | 66% | 24% | 10% |
| 78.0–89.9 | 29 | 83.9 | 75.9 | 0.90 | 62% | 14% | 24% |
| 89.9–107.7 | 29 | 97.4 | 84.6 | 0.85 | 45% | 10% | 45% |
| 107.7–130.6 | 29 | 116.8 | 95.0 | 0.78 | 34% | 7% | 59% |
| 130.6–190.0 | 29 | 150.3 | 91.8 | 0.60 | 21% | 0% | 79% |
| 190.0–513.9 | 30 | 256.3 | 113.2 | 0.39 | 10% | 0% | 90% |

The bottom 20% are overestimated 1.9–3.3 times and the top 20% reach only 0.39–0.60 of the reference. By contrast, the median v5 / reference of 22 of the 25 use, structure, storey and project-type groups with 9 or more buildings lies between 0.88 and 1.25; the exceptions are small groups (Other (12) 0.56; 21 or more (9) 0.69; Minor Renovation (17) 1.60). The extremes sit inside every group, not in particular groups.

## 2. What makes the extremes

| Material category (mean kgCO2e/m2 floor) | bottom 20% | middle 60% | top 20% | share of the top's excess |
|---|---|---|---|---|
| Insulation | 4.7 | 20.3 | 79.0 | 43% |
| XPS | 1.4 | 8.9 | 61.1 | 38% |
| Aluminum | 3.9 | 11.1 | 35.9 | 18% |
| Steel | 2.1 | 7.4 | 23.1 | 11% |
| Windows and frames | 1.3 | 6.5 | 14.9 | 6% |
| Cladding | 0.8 | 6.4 | 13.6 | 5% |

Mean total: bottom 20.4, middle 79.8, top 217.3. XPS is a sub-category of insulation, so the two overlap. The top is high mainly because of **HFC-blown XPS insulation** and **aluminium (curtain wall and frames)**. The bottom 20% (59 buildings) are mostly scope and data effects: 13 LCAs without the enclosure in scope, 8 flagged incomplete, 18 minor renovations or tenant improvements, 12 without any fenestration; 28 are complete new buildings.

## 3. Can any feature pick out the extremes?

AUC = chance that a building of the group ranks above one outside it (0.5 = no better than chance). Categorical AUCs use the group's own share, so they are in-sample and optimistic.

| Target | best five features (AUC) |
|---|---|
| Enclosure, top 20% | lca_ec_reduction_percent 0.69, bldg_prim_use 0.68, envelope area / floor area 0.68, bldg_cfa 0.67, str_sys_summary 0.66 |
| Enclosure, bottom 20% | bldg_ibc_type 0.73, bldg_cfa 0.72, bldg_prim_use 0.71, site_state_province 0.71, envelope area / floor area 0.70 |
| Enclosure, heavy XPS (> 20 kgCO2e/m2) | site_clim_zone 0.69, site_state_province 0.69, site_region 0.68, bldg_ibc_type 0.67, str_lat_sys 0.66 |
| *Whole building, for comparison* | mass_total / floor area: top 20% 0.86, bottom 20% 0.88 |

## 4. What typical-range designs would give (simulated with v5's evidence lines)

| Design (in-sample unless marked) | coverage | slope | bottom 20% inside | top 20% inside |
|---|---|---|---|---|
| v5 as run | 35.6% | 0.39 | 6.8% | 15.3% |
| v5 kept inside P10–P90 of use x climate zone (best of 84 clip designs) | 36.3% | 0.38 | 6.8% | 15.3% |
| 0.5 x calibrated take-off + 0.5 x typical value by use x storeys x structure (best of 220 triples) | 37.3% | 0.38 | 10.2% | 18.6% |
| v5 as run, test buildings only (88) | 38.6% | 0.47 | 0.0% | 22.2% |
| same best triple, cells fitted on the development set only, test buildings (held-out check) | 31.8% | 0.44 | 0.0% | 22.2% |

Clipping into a typical range never steepens the curve: the ranges are wide because the extremes lie inside every cell, so they hardly bind, and where they do they pull toward the middle. Replacing the benchmark with finer typical values adds at most about 2 points in-sample, does not change the slope, and loses on the held-out check.

## Verdict: not feasible, not run

- The whole building works because one feature, the inventory mass per m2, separates high from low buildings (AUC 0.86–0.88). For the enclosure no feature does (best 0.66–0.73), and the drivers of the top, HFC-blown XPS and aluminium curtain wall, are not predictable from the features (best AUC for heavy XPS 0.69).
- Every simulated typical-range design stays within about 2 points of v5 (in-sample) with the same slope, and the best one is worse than v5 on the held-out check. A new LLM run (about 2.4 million tokens for 3 runs) would not change the conclusion.
- The only small gain is the constant for LCAs without the enclosure in scope: 11.7 instead of 8 would cover 6 of these 13 buildings instead of 2 (+1.4 points, in-sample). It is not worth a run on its own.
- What would help is information the features lack: the insulation type (XPS or not) and the share of curtain wall, i.e. the assembly type.
