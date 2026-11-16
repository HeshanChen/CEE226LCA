===== KEY: project-264__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 8,165 m2. With 3 storeys, roof plus slab would leave too little wall, so I use about 4 storeys: roof 2,400 m2 and slab 2,400 m2, which leaves walls of about 3,365 m2. WWR 0.34 gives 1,144 m2 of glazing and 2,221 m2 of opaque wall.
Assemblies: a mass-timber assembly building in Oregon (5B), R-19 walls and R-36 roof. Likely aluminum curtain wall or storefront, stud walls with metal panel or brick, and a polyiso membrane roof. Oregon is not an early-ban state, but the 2023 LCA has reductions, so polyiso is likely.
Intensities: glazing 1,144 x 140 = 160 t; opaque 2,221 x 85 = 189 t; roof 2,400 x 30 = 72 t (HFC XPS high about 240 t); slab insulation 2,400 x 4 = 10 t. Total 431 t.
Check: 53 kgCO2e/m2 of envelope.
Bottom-up: 431 t / 9,600 = 45; range 38-55, A = 46.
Calibration: Public Assembly with envelope area given, K = 1.37, so CALIBRATED = 63.0.

Step B. Public Assembly, 2 to 5 storeys: B = 97.

Step C. FINAL = 0.5 x 63.0 + 0.5 x 97 = 80.0; range 64-96.
BOTTOM_UP_kgCO2e_per_m2: 46
CALIBRATED_kgCO2e_per_m2: 63
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 64 - 96

===== KEY: project-195__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 14,882 m2 at about 13 storeys (46-60 m), so the footprint is about 1,885 m2. Roof 1,885 m2 and slab 1,885 m2 leave walls of about 11,112 m2. WWR 0.48 gives 5,334 m2 of vision glass and 5,778 m2 of opaque wall.
Assemblies: a steel office of more than 10 storeys in Washington (4C), so unitized aluminum curtain wall with spandrels or metal panel. The roof is membrane over polyiso (WA banned HFC XPS).
Intensities: curtain wall 5,334 x 180 = 960 t; spandrel/metal panel 5,778 x 100 = 578 t; roof 1,885 x 25 = 47 t; slab insulation 1,885 x 3 = 6 t. Total 1,591 t.
Check: 107 kgCO2e/m2 of envelope, which is consistent with curtain wall.
Bottom-up: 1,591 t / 24,500 = 65; range 56-74, A = 65.
Calibration: Office with envelope area given, K = 1.23, so CALIBRATED = 80.0.

Step B. Office, 11 or more storeys: B = 72.

Step C. FINAL = 0.5 x 80.0 + 0.5 x 72 = 76.0; range 61-91.
BOTTOM_UP_kgCO2e_per_m2: 65
CALIBRATED_kgCO2e_per_m2: 80
BENCHMARK_kgCO2e_per_m2: 72
RANGE_kgCO2e_per_m2: 61 - 91

===== KEY: project-235__run1 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area or height is given. Assuming 3 storeys, CFA 13,600 m2 gives a footprint of about 4,533 m2 (about 100 x 45 m), so a perimeter of about 290 m. At about 14 m high, the walls are about 4,060 m2. WWR is missing, so I use 0.33 for labs: 1,340 m2 of glazing and 2,720 m2 of opaque wall. The roof is 4,533 m2 and the slab 4,533 m2.
Assemblies: a steel-framed lab in the Eastern region (5A). Likely brick or metal panel on steel stud, aluminum windows or curtain wall, and a membrane roof over rigid insulation. The One Click LCA is from 2021 with no ban state given, so HFC XPS is a plausible high case.
Intensities: glazing 1,340 x 140 = 188 t; opaque 2,720 x 100 = 272 t; roof 4,533 x 25 = 113 t (HFC XPS at 100 gives 453 t); slab insulation 4,533 x 5 = 23 t. Base 596 t; high 936 t.
Check: 46-72 kgCO2e/m2 of envelope.
Bottom-up: 44-69 per m2 of floor; A = 56.
Calibration: Laboratory without envelope area, K = 1.33, so CALIBRATED = 74.5.

Step B. Laboratory, 2 to 5 storeys: B = 77.

Step C. FINAL = 0.5 x 74.5 + 0.5 x 77 = 75.7; range 61-91.
BOTTOM_UP_kgCO2e_per_m2: 56
CALIBRATED_kgCO2e_per_m2: 74.5
BENCHMARK_kgCO2e_per_m2: 77
RANGE_kgCO2e_per_m2: 61 - 91

===== KEY: project-134__run1 =====
Special case: lca_phys_scope is CF (interior construction and finishes). It does not contain E, so the enclosure was not modelled and only incidental items are booked under it. Following the rule, I skip Steps A to C and report the fixed values for an unmodelled enclosure. This fits a tenant improvement in an existing steel office, where the new mass is only about 22 kg/m2 of interior fit-out.
BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-58__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 13,904 m2 at about 8 storeys (22.6-30 m), so the footprint is about 2,488 m2. Roof 2,488 m2 and slab 2,488 m2 leave walls of about 8,928 m2. WWR 0.462 gives 4,125 m2 of glazing and 4,803 m2 of opaque wall.
Assemblies: a concrete residential building in California (3B), R-17 walls and R-21 roof. Likely aluminum windows or window wall, steel stud with stucco or metal panel, and a membrane roof over thin polyiso (no HFC XPS in California).
Intensities: glazing 4,125 x 150 = 619 t; opaque 4,803 x 70 = 336 t; roof 2,488 x 18 = 45 t; slab insulation 2,488 x 2 = 5 t. Total 1,005 t.
Check: 72 kgCO2e/m2 of envelope, which is consistent with about 46% aluminum glazing.
Bottom-up: 1,005 t / 19,900 = 50.5; range 42-60, A = 51.
Calibration: Residential multifamily with envelope area given, K = 0.97, so CALIBRATED = 49.5.

Step B. Residential multifamily, 6 to 10 storeys: B = 48.

Step C. FINAL = 0.5 x 49.5 + 0.5 x 48 = 48.7; range 39-58.
BOTTOM_UP_kgCO2e_per_m2: 51
CALIBRATED_kgCO2e_per_m2: 49.5
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 39 - 58

===== KEY: project-122__run1 =====
Special case: lca_phys_scope is SCF (superstructure, interior construction and finishes). It does not contain E, so the enclosure was not modelled in this major renovation and only incidental items are booked under it. Following the rule, I skip Steps A to C and report the fixed values for an unmodelled enclosure.
BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-15__run1 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. CFA 1,740 m2 at 2 storeys gives a footprint of about 870 m2 (about 30 x 29 m), so a perimeter of about 118 m. At 10 m high, the walls are about 1,180 m2. WWR 0.1115 gives 130 m2 of glazing and 1,050 m2 of opaque wall. The roof is 870 m2; the slab is uninsulated in this hot climate.
Assemblies: a steel industrial building in Texas (2A). Likely insulated metal panel or metal panel on steel stud, aluminum windows, and a membrane roof over thin polyiso. Newer IMP products are likely; a legacy HFC panel would be the high case.
Intensities: windows 130 x 120 = 16 t; opaque 1,050 x 80 = 84 t; roof 870 x 22 = 19 t. Total 119 t; with a legacy IMP, up to about 150 t.
Check: 58 kgCO2e/m2 of envelope.
Bottom-up: 119 t / 1,740 = 68; range 55-85, A = 70.
Calibration: Industrial is "any other use", K = 1.31, so CALIBRATED = 91.7.

Step B. Any other use: B = 84.

Step C. FINAL = 0.5 x 91.7 + 0.5 x 84 = 87.9; range 70-105.
BOTTOM_UP_kgCO2e_per_m2: 70
CALIBRATED_kgCO2e_per_m2: 91.7
BENCHMARK_kgCO2e_per_m2: 84
RANGE_kgCO2e_per_m2: 70 - 105

===== KEY: project-6__run1 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. A one-storey footprint of 1,600 m2 (about 40 x 40 m) has a perimeter of about 160 m; at 5 m high, the walls are about 800 m2. WWR is missing, so I use 0.25 for a small office: 200 m2 of glazing and 600 m2 of opaque wall. The roof is 1,600 m2; the slab is uninsulated in Zone 1A.
Assemblies: the vertical system is precast concrete with a wood roof, so precast or tilt-up concrete wall panels with interior insulation and gypsum, aluminum storefront, and a membrane roof over thin polyiso.
Intensities: storefront 200 x 145 = 29 t; precast walls 600 x 110 = 66 t; roof 1,600 x 22 = 35 t. Total 130 t.
Check: 54 kgCO2e/m2 of envelope (walls plus roof).
Bottom-up: 130 t / 1,600 = 81; range 68-95, A = 81.
Calibration: Office without envelope area, K = 1.49, so CALIBRATED = 120.7.

Step B. Office, 1 storey: B = 131.

Step C. FINAL = 0.5 x 120.7 + 0.5 x 131 = 125.9; range 101-151.
BOTTOM_UP_kgCO2e_per_m2: 81
CALIBRATED_kgCO2e_per_m2: 120.7
BENCHMARK_kgCO2e_per_m2: 131
RANGE_kgCO2e_per_m2: 101 - 151

===== KEY: project-23__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 38,392 m2 for a tower of over 90 m (about 30 storeys) on an above-grade parking podium. The roof is about 2,500 m2 including the podium roof, and the slab about 2,500 m2, which leaves walls of about 33,392 m2. WWR 0.3 gives 10,018 m2 of glazing and 23,374 m2 of opaque wall, including the parking screens.
Assemblies: a concrete residential tower in Texas (2A), R-19 walls and R-25 roof. Likely aluminum window wall or windows, steel stud with stucco or metal panel, and a polyiso membrane roof. The insulation is thin, so XPS risk is small.
Intensities: glazing 10,018 x 175 = 1,753 t; opaque 23,374 x 70 = 1,636 t; roof 2,500 x 22 = 55 t. Total 3,444 t.
Check: 90 kgCO2e/m2 of envelope, which is consistent.
Bottom-up: 3,444 t / CFA 70,000 = 49; range 42-58, A = 50.
Calibration: Residential multifamily with envelope area given, K = 0.97, so CALIBRATED = 48.5.

Step B. Residential multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 48.5 + 0.5 x 71 = 59.8; range 48-72.
BOTTOM_UP_kgCO2e_per_m2: 50
CALIBRATED_kgCO2e_per_m2: 48.5
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 48 - 72

===== KEY: project-91__run1 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. A one-storey footprint of 570 m2 (about 24 x 24 m) has a perimeter of about 96 m; at about 8 m high, the walls are about 768 m2. The warehouse WWR of 0.05 gives about 38 m2 of glazing and doors, and 730 m2 of opaque wall. The roof is 570 m2.
Assemblies: masonry shear walls in California (3C), so structural CMU exterior walls, probably with furring and insulation, a few aluminum windows and doors, and a membrane or metal roof over polyiso.
Intensities: glazing and doors 38 x 150 = 6 t; CMU walls 730 x 100 = 73 t; roof 570 x 27 = 15 t. Total 94 t.
Check: 70 kgCO2e/m2 of envelope (walls plus roof), which is reasonable for CMU.
Bottom-up: 94 t / 570 = 165; the small building has a high wall-to-floor ratio. Range 130-190, A = 160.
Calibration: Warehouse without envelope area, K = 1.22, so CALIBRATED = 195.2.

Step B. Warehouse and Storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 195.2 + 0.5 x 65 = 130.1; range 104-156.
BOTTOM_UP_kgCO2e_per_m2: 160
CALIBRATED_kgCO2e_per_m2: 195.2
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 104 - 156
