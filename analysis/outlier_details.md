# The 30 buildings removed as outliers

Rules from `analysis/outliers.py`; they use only the reference LCA and the features, never an LLM estimate. Inventory items are the enclosure A1–A3 rows of the reference LCA (`full_lca_results.xlsx`), largest first, per m² of the floor area the value is divided by.

| Rule | Definition | Buildings | Also extreme |
|---|---|---|---|
| R1 incomplete inventory | new construction with no window, glazing, curtain wall or storefront GWP | 10 | 3 |
| R2 out of scope | `lca_phys_scope` has no E: the source LCA did not assess the enclosure | 13 | 8 |
| R3 extreme value | log value outside Tukey's fences, below 11.6 or above 472 kgCO2e/m² | 18 | – |
| Any rule | (R1 and R2 do not overlap; 7 buildings are flagged by R3 alone) | **30** | |

## Who they are

- By project type: New Construction 11, Minor Renovation 9, Tenant Improvement 7, Major Renovation 3.
- Renovations and fit-outs are 19 of the 30 but only 49 of all 292: 39% of all renovations and fit-outs are flagged, against 4.5% of new buildings.
- Their enclosure inventories are sparse: a median of 28 material rows, against 156 for the other 262 buildings.
- 17 lie below the lower fence (11.6) and one (project 137) above the upper fence. Of the other 12, all but project 264 (141.4, flagged for its missing windows) lie between 11.6 and 42, in the bottom quarter of the distribution.

## R1: incomplete inventory (10 new buildings)

The reference model holds no glass at all. Seven of the ten are occupied buildings that would normally have windows (offices, a school, a hospital, an assembly building, an industrial building, a warehouse), and those with a window-to-wall ratio report a substantial one (WWR: 0.46 for project 66, 0.65 for project 74, 0.22 for project 217, 0.34 for project 264). The other three are parking garages (27, 35, 141), where an open structure without glass is plausible; they have no thermal envelope and are atypical rather than wrong. The enclosure value is then only the part that was modelled. Their whole-building values are ordinary, so the structure was modelled and the enclosure was not, or only in part. Project 264 is the exception at the high end: 104 kgCO2e/m² of aluminium sheet and no glass.

| Project | Type | Use | Storeys | Scope | Floor area, m² (basis) | Enclosure A1–A3, kgCO2e/m² | What the enclosure inventory holds (kgCO2e/m² floor) | Whole building A–C |
|---|---|---|---|---|---|---|---|---|
| 74 | new | Office | 2 to 5 | BSE | 45,000 (CFA) | **0.6** | 2 rows: Roll formed metal panel aluminum 0.5, Mineral wool high density 0.1 | 273 |
| 66 | new | Office | 2 to 5 | BSECF | 33,750 (CFA) | **7.0** | 17 rows: Roofing and waterproofing - other 1.4, Roll formed metal panel aluminum 1.3, Extruded polystyrene XPS 1.2, Insulation - other 1.0, ... | 415 |
| 80 | new | Industrial | 1 | BSE | 830 (CFA) | **9.4** | 3 rows: Roll formed metal panel aluminum 5.6, Extruded polystyrene XPS 3.3, Roofing and waterproofing - other 0.5 | 681 |
| 234 | new | Healthcare | 11 to 15 | BSE | 64,500 (CFA) | **15.5** | 4 rows: Ready mix unknown 11.3, Insulation - other 2.6, Polyisocyanurate PIR 1.4, Mineral wool low density 0.1 | 358 |
| 35 | new | Parking | 6 to 10 | BSE | 62,000 (CFA) | **17.2** | 4 rows: Steel - other 11.1, CMU 6.0 | 275 |
| 27 | new | Parking | 6 to 10 | BSE | 18,200 (CFA) | **24.9** | 97 rows: Ready mix NW 5000 10.3, Rebar and reinforcement 4.5, Mortar and grout 2.5, Steel sheet 2.0, ... | 383 |
| 217 | new | Education | 2 to 5 | BSECF | 7,950 (CFA) | **27.0** | 122 rows: Mineral wool high density 10.5, Extrusion 8.3, Terracotta units 3.5, Mineral wool low density 1.6, ... | 644 |
| 91 | new | Warehouse and Storage | 1 | BSE | 570 (CFA) | **29.2** | 6 rows: Cold formed steel framing 16.1, Coatings - other 6.7, Aluminum sheet 6.4 | 229 |
| 141 | new | Parking | 1 | BSE | 9,550 (CFA) | **41.7** | 4 rows: Ready mix unknown 28.8, CMU 7.5, Rebar and reinforcement 5.4 | 258 |
| 264 | new | Public Assembly | 2 to 5 | BSECF | 9,600 (CFA) | **141.4** | 182 rows: Aluminum sheet 103.6, Mineral wool high density 8.5, Polyisocyanurate PIR 6.8, Cold formed steel framing 5.6, ... | 480 |

## R2: enclosure not in the LCA's scope (13 renovations and fit-outs)

Their `lca_phys_scope` is interiors (CF), structure and interiors (SCF) or similar: the study did not set out to assess the enclosure. The dataset still classifies a few of their items as Shell – Enclosure: interior glazing and storefronts, steel studs, gypsum board, paint, a single insulation entry. The value measures what an interior or structural LCA happened to touch, not the building's enclosure.

| Project | Type | Use | Storeys | Scope | Floor area, m² (basis) | Enclosure A1–A3, kgCO2e/m² | What the enclosure inventory holds (kgCO2e/m² floor) | Whole building A–C |
|---|---|---|---|---|---|---|---|---|
| 134 | tenant impr. | Office | 2 to 5 | CF | 7,450 (renov.+added GFA) | **2.6** | 24 rows: Cold formed steel framing 1.8, Steel - other 0.3, Terracotta units 0.2, Insulated glass unit IGU 0.2, ... | 13 |
| 135 | minor renov. | Laboratory | 2 to 5 | SCF | 43,500 (renov.+added GFA) | **2.7** | 84 rows: Aluminum sheet 1.4, Fiberglass blanket 0.4, Steel - other 0.4, Mineral wool high density 0.2, ... | 36 |
| 163 | minor renov. | Office | 1 | CF | 1,270 (renov.+added GFA) | **3.1** | 23 rows: Glazing - other 1.2, Loose-fill cellulose 0.7, Extrusion 0.6, Insulated glass unit IGU 0.4, ... | 58 |
| 136 | tenant impr. | Public Assembly | 2 to 5 | CF | 250 (renov.+added GFA) | **4.3** | 16 rows: Insulated glass unit IGU 2.9, Fiberglass blanket 0.7, Other 0.5, Doors and frames - other 0.2 | 90 |
| 43 | minor renov. | Education | – | CF | 2,500 (renov.+added GFA) | **6.8** | 36 rows: Glazing - other 2.0, Fiberglass blanket 1.8, Insulated glass unit IGU 1.1, Cold formed steel framing 0.8, ... | 97 |
| 104 | tenant impr. | Office | 21 or more | CF | 36,250 (renov.+added GFA) | **7.6** | 6 rows: Mineral wool high density 5.6, Insulation - other 1.5, Glazing - other 0.5 | 186 |
| 122 | major renov. | Office | 2 to 5 | SCF | 5,850 (renov.+added GFA) | **10.0** | 76 rows: Mineral wool high density 2.7, Aluminum storefront or curtain wall 1.5, Cold formed steel framing 1.3, Fiberglass blanket 1.2, ... | 156 |
| 42 | minor renov. | Education | – | CF | 4,200 (renov.+added GFA) | **10.4** | 54 rows: Glazing - other 6.0, Extrusion 2.1, Fiberglass blanket 0.9, Steel door 0.6, ... | 219 |
| 101 | tenant impr. | Office | 21 or more | CF | 3,250 (renov.+added GFA) | **11.6** | 19 rows: Extrusion 8.1, Glazing - other 2.3, Doors and frames - other 0.6, Mineral wool low density 0.4, ... | 41 |
| 85 | tenant impr. | Office | 1 | CF | 430 (renov.+added GFA) | **12.9** | 57 rows: Cold formed steel framing 4.3, Aluminum storefront or curtain wall 2.6, Aluminum framed window 1.5, Doors and frames - other 1.2, ... | 75 |
| 205 | minor renov. | Lodging | 2 to 5 | SCF | 950 (renov.+added GFA) | **13.2** | 243 rows: Extruded polystyrene XPS 6.6, Air and vapor barriers 2.1, Rebar and reinforcement 1.9, Fiberglass blanket 1.7, ... | 115 |
| 10 | major renov. | Office | 2 to 5 | CF | 7,800 (renov.+added GFA) | **14.0** | 1 row: Mineral wool high density 14.0 | 126 |
| 228 | tenant impr. | Office | 11 to 15 | CF | 27,000 (renov.+added GFA) | **26.1** | 102 rows: Glazing - other 6.8, Gypsum board 6.5, Cold formed steel framing 5.6, Paint 1.9, ... | 131 |

## R3: extreme values flagged by this rule alone (7)

The other 11 extreme values are already caught by R1 or R2.

| Project | Type | Use | Storeys | Scope | Floor area, m² (basis) | Enclosure A1–A3, kgCO2e/m² | What the enclosure inventory holds (kgCO2e/m² floor) | Whole building A–C |
|---|---|---|---|---|---|---|---|---|
| 108 | minor renov. | Mercantile | 2 to 5 | SEC | 3,400 (renov.+added GFA) | **0.5** | 1 row: Fiberglass blanket 0.5 | 15 |
| 54 | major renov. | Residential: Multifamily (5 or more units) | 6 to 10 | BSE | 18,900 (renov.+added GFA) | **6.5** | 51 rows: Insulated glass unit IGU 3.7, Extruded polystyrene XPS 2.3, Roll formed metal panel aluminum 0.4, Coatings - other 0.1 | 72 |
| 99 | minor renov. | Mercantile | 2 to 5 | SEC | 5,100 (renov.+added GFA) | **6.5** | 14 rows: Fiberglass blanket 4.2, Ready mix unknown 0.6, Polyisocyanurate PIR 0.5, Stone masonry 0.5, ... | 32 |
| 103 | minor renov. | Laboratory | 2 to 5 | SECF | 24,750 (renov.+added GFA) | **10.1** | 61 rows: Insulated glass unit IGU 3.4, Extrusion 3.0, Polyisocyanurate PIR 2.3, Modified bitumen 0.9, ... | 29 |
| 56 | new | Office | 16 to 20 | BSEC | 67,500 (CFA) | **10.7** | 176 rows: Extrusion 3.6, Aluminum composite panel ACM 2.1, Insulation - other 1.4, Cold formed steel framing 1.1, ... | 237 |
| 146 | tenant impr. | Office | 1 | ECF | 3,450 (renov.+added GFA) | **11.3** | 31 rows: Aluminum storefront or curtain wall 4.3, Extrusion 3.6, Insulated glass unit IGU 1.6, Glazing - other 1.2, ... | 107 |
| 137 | minor renov. | Office | 16 to 20 | BSECF | 3,350 (renov.+added GFA) | **513.9** | 277 rows: Aluminum storefront or curtain wall 302.0, Insulated glass unit IGU 97.0, Aluminum sheet 39.9, Steel - other 31.8, ... | 1221 |

Project 137 is the only high extreme: its envelope area (7,660 m²) is 2.3 times the floor area its value is divided by (3,350 m² of renovated floor), against a median of 0.96 for all buildings. A full re-cladding of a 16–20 storey office is divided by a small renovated floor area.

## Effect on the results

| Prompt | inside ±20% among the 30 | median estimate / reference among the 30 | coverage, all 292 | coverage, cleaned 262 |
|---|---|---|---|---|
| v1 | 5 of 30 | 1.08 | 19.5% | 19.8% |
| v3 | 3 of 30 | 0.78 | 25.0% | 26.7% |
| v4 | 3 of 30 | 2.61 | 32.2% | 34.7% |
| v5 | 3 of 30 | 2.59 | 35.6% | 38.5% |

No prompt can estimate these values from the 48 features: the values describe the scope and completeness of the source study, not the building. Every result is reported on all 292 buildings and on the cleaned 262.
