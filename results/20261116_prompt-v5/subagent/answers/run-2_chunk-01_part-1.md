===== KEY: project-145__run2 =====
Scope check: lca_phys_scope BSE includes E, so the enclosure was modelled.

Step A. Areas: no envelope area is given. CFA 21,250 m2, 6-10 storeys (take 8), so the roof is about 2,660 m2. Wall area is about 0.45 x 21,250 = 9,560 m2. With WWR 0.30 (multifamily default), glazing is 2,870 m2 and opaque wall 6,690 m2. Assemblies: a concrete mid-rise in BC (4C), so aluminum window wall or windows at about 140 and steel stud with fiber cement or metal panel rainscreen at about 75. The roof is polyiso or low-GWP XPS at about 30, because HFC XPS was banned in Canada from 2021 and this is a 2023 One Click model. Below-grade insulation is about 10 per m2 of footprint. Totals: glazing 401,800 + opaque 501,750 + roof 79,700 + below grade 26,600 = about 1,010,000 kgCO2e. That is about 48 per m2 of floor and about 50 per m2 of envelope, which is plausible for 30% glazing. Bottom-up range 38-58, so A = 48.
Calibration: residential multifamily without envelope area, K = 1.60, gives 76.8.

Step B. Multifamily, 6-10 storeys: B = 48.

Step C. FINAL = 0.5 x 76.8 + 0.5 x 48 = 62.4. Range 49.9 - 74.9.

BOTTOM_UP_kgCO2e_per_m2: 48
CALIBRATED_kgCO2e_per_m2: 76.8
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 49.9 - 74.9

===== KEY: project-152__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 6,032 m2 on a CFA of 4,350 m2. Taking about 4 storeys, the roof is 1,090 m2 and the ground slab 1,090 m2, which leaves 3,856 m2 of wall. WWR 0.36 gives 1,388 m2 of glazing and 2,468 m2 of opaque wall. Assemblies: a Type II-A concrete school in Washington 4C, typically brick veneer or metal panel on a steel stud backup at about 95. Glazing is aluminum windows and storefront at about 130. The roof is polyiso membrane at about 30; WA banned HFC XPS from 2021, but Tally data lags, so XPS stays in the range. Slab-edge and under-slab insulation is about 5 per m2. Totals: opaque 234,500 + glazing 180,400 + roof 32,600 + slab 5,400 = 453,000 kgCO2e. That is 75 per m2 of envelope, which is consistent, and 104 per m2 of floor. Bottom-up range 90-120, so A = 104.
Calibration: education with envelope area, K = 1.05, gives 109.2.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 109.2 + 0.5 x 86 = 97.6. Range 78.1 - 117.1.

BOTTOM_UP_kgCO2e_per_m2: 104
CALIBRATED_kgCO2e_per_m2: 109.2
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 78.1 - 117.1

===== KEY: project-93__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 5,378 m2 and the CFA 4,650 m2, with about 3 storeys (7.6-15 m). Roof 1,550 m2 and slab 1,550 m2 leave 2,278 m2 of wall. WWR 0.68 gives 1,549 m2 of glazing and 729 m2 of opaque wall. Assemblies: a heavily glazed California 3C lab, so aluminum stick curtain wall at about 140 and metal panel on steel stud (R-23) at about 90. The roof is R-22 polyiso at about 24. This is a 2019 Tally model, before the California HFC ban, so HFC XPS at roughly +70 per m2 of roof is a plausible upper case. Slab insulation is about 3 per m2. Totals: glazing 216,900 + opaque 65,600 + roof 37,200 + slab 4,700 = 324,000 kgCO2e, which is 60 per m2 of envelope and 70 per m2 of floor. The HFC roof case reaches about 93. Bottom-up range 60-90, so A = 75.
Calibration: laboratory with envelope area, K = 1.81, gives 135.8.

Step B. Laboratory, 2-5 storeys: B = 77.

Step C. FINAL = 0.5 x 135.8 + 0.5 x 77 = 106.4. Range 85.1 - 127.7.

BOTTOM_UP_kgCO2e_per_m2: 75
CALIBRATED_kgCO2e_per_m2: 135.8
BENCHMARK_kgCO2e_per_m2: 77
RANGE_kgCO2e_per_m2: 85.1 - 127.7

===== KEY: project-2__run2 =====
Scope check: BSE includes E.

Step A. Areas: the envelope is 62,245 m2 and the CFA 200,000 m2. The building has 21 or more storeys and is over 90 m tall (take about 40 storeys), so the footprint is about 5,000 m2. Roof 5,000 m2 and slab 5,000 m2 leave 52,245 m2 of wall. WWR is missing, so I use 0.45 for a large office, giving 23,510 m2 of vision glazing and 28,735 m2 of spandrel and opaque wall. Assemblies: a high-rise office, so unitized aluminum curtain wall at about 180 and spandrel at about 100. The climate is very cold (7B), so the insulation is thick. The roof is polyiso at about 30, or about 100 with HFC XPS. Slab insulation is about 5 per m2. Totals: vision glazing 4,232,000 + spandrel 2,874,000 + roof 150,000 + slab 25,000 = 7,280,000 kgCO2e. That is 117 per m2 of envelope, consistent with curtain wall, and 36.4 per m2 of floor. With the HFC roof and higher aluminum data it is about 42. Bottom-up range 32-42, so A = 37.
Calibration: office with envelope area, K = 1.23, gives 45.5.

Step B. Office, 11 or more storeys: B = 72.

Step C. FINAL = 0.5 x 45.5 + 0.5 x 72 = 58.8. Range 47.0 - 70.5.

BOTTOM_UP_kgCO2e_per_m2: 37
CALIBRATED_kgCO2e_per_m2: 45.5
BENCHMARK_kgCO2e_per_m2: 72
RANGE_kgCO2e_per_m2: 47.0 - 70.5

===== KEY: project-63__run2 =====
Scope check: BSE includes E.

Step A. Areas: the envelope is 3,980 m2 for a single-storey building of 1,310 m2, a ratio of 3.0 that points to a tall, compact volume. Roof 1,310 m2 and slab 1,310 m2 leave 1,360 m2 of wall. WWR 0.12 gives 163 m2 of glazing and 1,197 m2 of opaque wall. Assemblies: a Type V-B wood light-frame building with concrete shear walls in California 3B. The walls are wood stud with stucco or fiber cement, partly concrete, at about 60. Glazing is aluminum storefront at about 145. The roof is R-38 polyiso or batt-insulated with membrane, at about 30. Slab insulation is about 3 per m2. Totals: walls 71,800 + glazing 23,600 + roof 39,300 + slab 3,900 = 138,700 kgCO2e. That is 35 per m2 of envelope, low but consistent with wood framing and little glazing, and 106 per m2 of floor. Allowing for missing trim, doors and the concrete wall share, the range is 95-135, so A = 115.
Calibration: public order and safety with envelope area, K = 1.07, gives 123.1.

Step B. Public order and safety, 1 storey is not listed, so I use the other-storeys value: B = 132.

Step C. FINAL = 0.5 x 123.1 + 0.5 x 132 = 127.5. Range 102.0 - 153.0.

BOTTOM_UP_kgCO2e_per_m2: 115
CALIBRATED_kgCO2e_per_m2: 123.1
BENCHMARK_kgCO2e_per_m2: 132
RANGE_kgCO2e_per_m2: 102.0 - 153.0

===== KEY: project-120__run2 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. This is a 1-storey warehouse of 33,250 m2, so the roof is 33,250 m2. Walls are about 0.4 x 33,250 = 13,300 m2. With WWR 0.05 that gives 665 m2 of glazing and doors and 12,635 m2 of opaque wall. Assemblies: steel frame with a concrete lateral system, which suggests tilt-up concrete walls at about 90, with light interior insulation in 4A. The roof is membrane over R-20 polyiso on bare metal deck at about 20. Glazing, storefront and doors are about 140. Totals: walls 1,137,000 + glazing 93,100 + roof 665,000 = 1,895,000 kgCO2e, or 57 per m2 of floor. Insulated metal panel walls would be lower and an HFC roof higher, so the range is 45-70 and A = 57.
Calibration: warehouse without envelope area, K = 1.22, gives 69.5.

Step B. Warehouse and storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 69.5 + 0.5 x 65 = 67.3. Range 53.8 - 80.7.

BOTTOM_UP_kgCO2e_per_m2: 57
CALIBRATED_kgCO2e_per_m2: 69.5
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 53.8 - 80.7

===== KEY: project-246__run2 =====
Scope check: BSE includes E.

Step A. Areas: the envelope is 12,033 m2 and the CFA 12,600 m2, with about 4 storeys. Roof 3,150 m2 and slab 3,150 m2 leave 5,733 m2 of wall. WWR 0.38 gives 2,179 m2 of glazing and 3,554 m2 of opaque wall. Assemblies: a Canadian school in 5A with R-24 walls and an R-45 roof. Walls are brick veneer on steel stud at about 105 and windows are aluminum at about 130. The roof is thick polyiso at about 35. HFC XPS has been banned in Canada since 2021, but tool lag keeps it in the range. Slab insulation is about 5 per m2. Totals: opaque 373,200 + glazing 283,300 + roof 110,300 + slab 15,800 = 782,600 kgCO2e. That is 65 per m2 of envelope, consistent, and 62 per m2 of floor. An HFC XPS roof would add about 37 per m2 of floor. Bottom-up range 55-85, so A = 70.
Calibration: education with envelope area, K = 1.05, gives 73.5.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 73.5 + 0.5 x 86 = 79.8. Range 63.8 - 95.7.

BOTTOM_UP_kgCO2e_per_m2: 70
CALIBRATED_kgCO2e_per_m2: 73.5
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 63.8 - 95.7

===== KEY: project-20__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 10,680 m2 on a CFA of 5,250 m2, a ratio of 2.0 that reflects tall assembly volumes. Taking 3 storeys, roof and slab are each 1,750 m2, leaving 7,180 m2 of wall. WWR 0.317 gives 2,276 m2 of glazing and 4,904 m2 of opaque wall. Assemblies: a steel-framed public assembly building in Texas 2A with R-20 walls. Walls are stone, brick or metal panel on steel stud at about 100. Glazing is curtain wall and storefront at about 140. The roof is R-33 polyiso at about 28. This is a 2021 Tally model in Texas, so HFC XPS at about +120 per m2 of roof is plausible. Slab insulation is about 3 per m2. Totals: opaque 490,400 + glazing 318,600 + roof 49,000 + slab 5,300 = 863,300 kgCO2e. That is 81 per m2 of envelope and 164 per m2 of floor; the HFC case is about 204. Bottom-up range 145-195, so A = 170.
Calibration: public assembly with envelope area, K = 1.37, gives 232.9.

Step B. Public assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 232.9 + 0.5 x 97 = 165.0. Range 132.0 - 197.9.

BOTTOM_UP_kgCO2e_per_m2: 170
CALIBRATED_kgCO2e_per_m2: 232.9
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 132.0 - 197.9

===== KEY: project-4__run2 =====
Scope check: BSE includes E.

Step A. Areas: the envelope is 12,637 m2 and the CFA 18,000 m2, including 3,400 m2 of parking, at about 9 storeys. Roof and slab are about 2,000 m2 each, leaving 8,637 m2 of wall. WWR 0.48 gives 4,146 m2 of glazing and 4,491 m2 of opaque wall. Assemblies: a concrete office in hot-humid 1A with 78 m/s wind, so impact-rated aluminum curtain wall or window wall at about 160. Opaque walls are stucco on concrete or CMU, or metal panel, at about 80. The parking floors are partly open. The roof is thin polyiso at about 25. Totals: glazing 663,400 + opaque 359,300 + roof 50,000 = 1,072,700 kgCO2e. That is 85 per m2 of envelope, consistent with heavy glazing, and 59.6 per m2 of floor. Bottom-up range 50-72, so A = 61.
Calibration: office with envelope area, K = 1.23, gives 75.0.

Step B. Office, 6-10 storeys: B = 79.

Step C. FINAL = 0.5 x 75.0 + 0.5 x 79 = 77.0. Range 61.6 - 92.4.

BOTTOM_UP_kgCO2e_per_m2: 61
CALIBRATED_kgCO2e_per_m2: 75.0
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 61.6 - 92.4

===== KEY: project-172__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 10,655 m2 and the CFA 18,900 m2, at about 13 storeys. Roof and slab are about 1,450 m2 each, leaving 7,747 m2 of wall. WWR 0.28 gives 2,169 m2 of glazing and 5,578 m2 of opaque wall. Assemblies: a Type IV-B mass-timber residential tower in BC 4C, typically prefabricated panelized walls with steel or wood studs and fiber cement or metal cladding at about 75. Windows are a vinyl or aluminum mix at about 110. The roof is polyiso or low-GWP XPS at about 30; HFC XPS was banned in Canada in 2021. Below-grade and slab insulation is about 5 per m2. Totals: opaque 418,400 + glazing 238,600 + roof 43,600 + slab 7,300 = 707,900 kgCO2e. That is 66 per m2 of envelope and 37.5 per m2 of floor. Bottom-up range 30-46, so A = 38.
Calibration: multifamily with envelope area, K = 0.97, gives 36.9.

Step B. Multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 36.9 + 0.5 x 71 = 53.9. Range 43.1 - 64.7.

BOTTOM_UP_kgCO2e_per_m2: 38
CALIBRATED_kgCO2e_per_m2: 36.9
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 43.1 - 64.7
