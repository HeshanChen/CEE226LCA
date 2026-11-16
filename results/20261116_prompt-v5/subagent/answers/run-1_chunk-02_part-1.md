===== KEY: project-110__run1 =====
Scope check: lca_phys_scope BSECF includes E, so the enclosure was modelled.

Step A. Areas: envelope 7,297 m2 given; about 18 storeys, so the roof is about 900 m2 and the ground slab about 900 m2, which leaves about 5,497 m2 of wall. WWR 0.84 gives about 4,617 m2 of glazing and 880 m2 of opaque wall.
Assemblies: a high-rise concrete residential tower in NY, so aluminum window wall with spandrel or metal-panel infill. The roof is a membrane over polyiso; NY banned HFC XPS from 2021, but tool data may lag, so I include it in the range.
Intensities: window wall 4,617 x 175 = 808 t; spandrel/metal panel 880 x 100 = 88 t; roof 900 x 25-100 (polyiso up to HFC XPS) = 23-90 t, mid 45 t; slab insulation 900 x 10 = 9 t. Total about 950 t.
Check: 950 t / 7,297 = 130 kgCO2e/m2 of envelope, which is consistent with a glazing-dominated facade.
Bottom-up: 950 t / 16,200 = 59; range 52-68, A = 60.
Calibration: Residential multifamily with envelope area given, K = 0.97, so CALIBRATED = 58.2.

Step B. Residential multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 58.2 + 0.5 x 71 = 64.6; range 0.8-1.2 x FINAL.
BOTTOM_UP_kgCO2e_per_m2: 60
CALIBRATED_kgCO2e_per_m2: 58.2
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 52 - 78

===== KEY: project-274__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 12,517 m2; about 4 storeys, so roof 3,750 m2 and ground slab 3,750 m2, which leaves walls of about 5,017 m2. WWR 0.18 gives 903 m2 of glazing and 4,114 m2 of opaque wall.
Assemblies: healthcare in Colorado (5B), R-22 walls and R-30 roof. Most likely brick veneer on steel stud with continuous insulation, aluminum windows, and a membrane roof over rigid insulation. Colorado banned HFC XPS from 2021, but Tally data of this period often lags, so legacy XPS is my high case.
Intensities: windows 903 x 130 = 117 t; brick/steel stud 4,114 x 105 = 432 t; roof 3,750 x 25 = 94 t (HFC XPS at 100 gives 375 t); slab insulation 3,750 x 5 = 19 t. Base total 662 t; high total 945 t.
Check: 53-75 kgCO2e/m2 of envelope, which is plausible for masonry with 18% glazing.
Bottom-up: 44 (base) to 63 (XPS) per m2 of floor; A = 54.
Calibration: Healthcare with envelope area given, K = 1.35, so CALIBRATED = 72.9.

Step B. Healthcare, 2 to 5 storeys: B = 68.

Step C. FINAL = 0.5 x 72.9 + 0.5 x 68 = 70.5; range 56-85.
BOTTOM_UP_kgCO2e_per_m2: 54
CALIBRATED_kgCO2e_per_m2: 72.9
BENCHMARK_kgCO2e_per_m2: 68
RANGE_kgCO2e_per_m2: 56 - 85

===== KEY: project-131__run1 =====
Scope check: BSE includes E.

Step A. Areas: envelope 7,804 m2; height 22.6-30 m suggests about 5 storeys, so roof 1,580 m2 and slab 1,580 m2, which leaves walls of about 4,644 m2. WWR 0.43 gives 1,997 m2 of glazing and 2,647 m2 of opaque wall.
Assemblies: a mass-timber school in Washington (4C), R-16 walls and R-50 roof. Likely stud backup with metal panel or fiber-cement rainscreen and aluminum windows or curtain wall. The roof is polyiso at R-50. WA banned HFC XPS in 2021 and the LCA is from 2021, so XPS is a minor risk.
Intensities: glazing 1,997 x 130 = 260 t; opaque 2,647 x 70 = 185 t; roof 1,580 x 40 (thick polyiso) = 63 t; slab insulation 1,580 x 4 = 6 t. Total 514 t.
Check: 66 kgCO2e/m2 of envelope, which is reasonable for 43% glazing with light cladding.
Bottom-up: 514 t / 7,900 = 65; range 58-75, A = 66.
Calibration: Education with envelope area given, K = 1.05, so CALIBRATED = 69.3.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 69.3 + 0.5 x 86 = 77.7; range 62-93.
BOTTOM_UP_kgCO2e_per_m2: 66
CALIBRATED_kgCO2e_per_m2: 69.3
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 62 - 93

===== KEY: project-2__run1 =====
Scope check: BSE includes E.

Step A. Areas: envelope 62,245 m2; a tower of over 90 m with about 40 storeys, so a footprint of about 5,000 m2. Roof 5,000 m2 and slab 5,000 m2 leave about 52,245 m2 of wall. WWR is missing, so I use 0.45 for a large office: 23,510 m2 of vision glass and 28,735 m2 of spandrel.
Assemblies: a high-rise office in a very cold climate (7B), so unitized aluminum curtain wall with insulated spandrels. The roof is a membrane over thick polyiso, with HFC XPS possible in One Click generic data.
Intensities: vision 23,510 x 180 = 4,232 t; spandrel 28,735 x 110 = 3,161 t; roof 5,000 x 35 = 175 t (XPS high around 500 t); slab insulation 5,000 x 5 = 25 t. Total about 7,590 t.
Check: 122 kgCO2e/m2 of envelope, which is consistent with all-curtain-wall facades.
Bottom-up: 7,590 t / 200,000 = 38; range 33-45, A = 39.
Calibration: Office with envelope area given, K = 1.23, so CALIBRATED = 48.0.

Step B. Office, 11 or more storeys: B = 72.

Step C. FINAL = 0.5 x 48.0 + 0.5 x 72 = 60.0; range 48-72.
BOTTOM_UP_kgCO2e_per_m2: 39
CALIBRATED_kgCO2e_per_m2: 48
BENCHMARK_kgCO2e_per_m2: 72
RANGE_kgCO2e_per_m2: 48 - 72

===== KEY: project-279__run1 =====
Scope check: BSECF includes E.

Step A. Areas: the reported envelope of 1,579 m2 is about equal to the floor area. Treating it as the total envelope with about 3 storeys gives a roof of about 527 m2, a slab of about 527 m2 and walls of about 525 m2. WWR 0.21 gives 110 m2 of glazing and 415 m2 of opaque wall. The wall figure looks low, so I widen the range upward.
Assemblies: a small steel-framed healthcare building in Zone 6A, so brick veneer on steel stud, aluminum windows and a membrane roof over thick rigid insulation. HFC XPS is plausible: the state is not a ban state and it is a cold climate.
Intensities: windows 110 x 120 = 13 t; brick/steel stud 415 x 105 = 44 t; roof 527 x 30 = 16 t (HFC XPS 527 x 100 = 53 t); slab insulation 527 x 6 = 3 t. Base 76 t; high case (XPS plus larger wall area) about 113 t.
Check: 48-72 kgCO2e/m2 of envelope.
Bottom-up: 76-113 t / 1,580 = 48-72; A = 60.
Calibration: Healthcare with envelope area given, K = 1.35, so CALIBRATED = 81.0.

Step B. Healthcare, 2 to 5 storeys: B = 68.

Step C. FINAL = 0.5 x 81 + 0.5 x 68 = 74.5; range 60-89.
BOTTOM_UP_kgCO2e_per_m2: 60
CALIBRATED_kgCO2e_per_m2: 81
BENCHMARK_kgCO2e_per_m2: 68
RANGE_kgCO2e_per_m2: 60 - 89

===== KEY: project-159__run1 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. The CFA is 40,000 m2 with about 6 tall storeys (22.6-30 m), so the footprint is about 6,667 m2. Long-span grids suggest a plan of about 140 x 48 m, a perimeter of about 376 m and walls of about 27 m, so gross wall area is about 10,150 m2; I use 11,000 m2. WWR is missing, so I assume 0.4 for a transit facility: 4,400 m2 of glazing and 6,600 m2 of opaque wall.
Assemblies: a steel-framed hub in Washington (4C), R-19 walls and R-30 roof. Likely aluminum curtain wall plus metal-panel rainscreen on steel stud, with a polyiso membrane roof.
Intensities: curtain wall 4,400 x 140 = 616 t; metal panel 6,600 x 90 = 594 t; roof 6,667 x 25 = 167 t; slab edge and under-slab insulation 6,667 x 3 = 20 t. Total 1,397 t.
Check: about 57 kgCO2e/m2 of envelope including roof and slab, which is acceptable.
Bottom-up: 1,397 t / 40,000 = 35; range 30-42, A = 36.
Calibration: Transportation Hub without envelope area, K = 1.44, so CALIBRATED = 51.8.

Step B. Transportation Hub, 6 to 10 storeys is not listed, so I use other storeys: B = 157.

Step C. FINAL = 0.5 x 51.8 + 0.5 x 157 = 104.4; range 84-125.
BOTTOM_UP_kgCO2e_per_m2: 36
CALIBRATED_kgCO2e_per_m2: 51.8
BENCHMARK_kgCO2e_per_m2: 157
RANGE_kgCO2e_per_m2: 84 - 125

===== KEY: project-228__run1 =====
Special case: lca_phys_scope is CF (interior construction and finishes only). It does not contain E, so the enclosure was not modelled and only incidental items are booked under it. Following the rule, I skip Steps A to C and report the fixed values for an unmodelled enclosure. This is consistent with a tenant improvement inside an existing office tower, where the enclosure is untouched and the low mass of the new work (about 89 kg/m2) reflects interior fit-out only.
BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-215__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 16,258 m2; about 3 storeys (7.6-15 m), so roof 6,267 m2 and slab 6,267 m2, which leaves walls of about 3,724 m2. WWR 0.25 gives 931 m2 of glazing and 2,793 m2 of opaque wall.
Assemblies: a steel-framed school in Massachusetts (5A), so brick veneer on steel stud with continuous insulation, aluminum windows and a large low-slope membrane roof over rigid insulation. Massachusetts is not an early HFC-ban state, and Tally data of this period often models XPS, so legacy XPS is my high case.
Intensities: windows 931 x 130 = 121 t; brick/steel stud 2,793 x 105 = 293 t; roof 6,267 x 25 = 157 t (HFC XPS at 100 gives 627 t); slab insulation 6,267 x 5 = 31 t. Base 602 t; high 1,072 t.
Check: 37-66 kgCO2e/m2 of envelope. The low end reflects a roof-dominated envelope with polyiso.
Bottom-up: 32-57 per m2 of floor; A = 45.
Calibration: Education with envelope area given, K = 1.05, so CALIBRATED = 47.3.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 47.3 + 0.5 x 86 = 66.6; range 53-80.
BOTTOM_UP_kgCO2e_per_m2: 45
CALIBRATED_kgCO2e_per_m2: 47.3
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 53 - 80

===== KEY: project-103__run1 =====
Scope check: SECF includes E, so new enclosure work was modelled.

Step A. Renovation evidence: a minor renovation of 24,750 m2 with a mass of only about 48 kg/m2, so new material is limited. The envelope work is likely re-roofing (roof R-42 is reported) and partial window replacement, not a full re-clad.
Areas: no envelope area is given. About 5 storeys (22.6-30 m) gives a roof of about 4,950 m2. Walls are about 0.4 x 24,750 = 9,900 m2, and WWR 0.36 gives 3,564 m2 of glazing, of which I assume about 30% (1,070 m2) is replaced.
Assemblies: new membrane roof over polyiso at R-42; new aluminum windows.
Intensities: roof 4,950 x 35 = 173 t; windows 1,070 x 130 = 139 t. Total about 312 t.
Check: this is not a full envelope, so the blended check does not apply. The low per-m2 value reflects partial scope.
Bottom-up: 312 t / 24,750 = 12.6; range 6-20 (from roof only up to more glazing and XPS), A = 13.
Calibration: Laboratory without envelope area, K = 1.33, so CALIBRATED = 17.3.

Step B. Laboratory, 2 to 5 storeys: B = 77.

Step C. FINAL = 0.5 x 17.3 + 0.5 x 77 = 47.2; range 38-57.
BOTTOM_UP_kgCO2e_per_m2: 13
CALIBRATED_kgCO2e_per_m2: 17.3
BENCHMARK_kgCO2e_per_m2: 77
RANGE_kgCO2e_per_m2: 38 - 57

===== KEY: project-53__run1 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 5,713 m2 for a 6,000 m2 above-grade building with about 4 storeys, so roof 1,500 m2 and slab 1,500 m2, which leaves walls of about 2,713 m2. WWR 0.27 gives 733 m2 of glazing and 1,980 m2 of opaque wall. The floor area for normalization is CFA 15,800 m2, which includes 9,800 m2 of below-grade parking.
Assemblies: a steel healthcare building in California (3B), R-19 walls. Likely steel stud with stucco or metal panel, aluminum windows and a polyiso membrane roof. California banned HFC XPS, and the climate needs only modest insulation.
Intensities: windows 733 x 130 = 95 t; opaque 1,980 x 85 = 168 t; roof 1,500 x 25 = 38 t; slab insulation 1,500 x 3 = 5 t; below-grade waterproofing and insulation about 20 t. Total 326 t.
Check: 57 kgCO2e/m2 of envelope, which is reasonable.
Bottom-up: 326 t / 15,800 = 20.6; range 17-26, A = 21.
Calibration: Healthcare with envelope area given, K = 1.35, so CALIBRATED = 28.4.

Step B. Healthcare, 2 to 5 storeys: B = 68.

Step C. FINAL = 0.5 x 28.4 + 0.5 x 68 = 48.2; range 39-58.
BOTTOM_UP_kgCO2e_per_m2: 21
CALIBRATED_kgCO2e_per_m2: 28.4
BENCHMARK_kgCO2e_per_m2: 68
RANGE_kgCO2e_per_m2: 39 - 58
