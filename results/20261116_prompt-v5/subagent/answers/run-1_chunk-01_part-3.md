===== KEY: project-210__run1 =====
Scope check: BSECF includes E.

Step A. CFA 4,900 m2 (GFA 4,360 m2 plus 540 m2 of parking). Multifamily, wood light-frame over a concrete podium, 6-10 storeys (I assume 7), height 22.6-30 m, no envelope area given. Washington 4C. WWR 0.145, walls R-21, roof R-38.
Areas: footprint and roof about 620 m2. Wall at about 0.45 x 4,360 gives about 1,960 m2: glazing about 285 m2 and opaque wall about 1,675 m2.
Assemblies: walls are wood stud with fiber cement or a metal-panel rainscreen at about 45. Glazing is mostly vinyl windows with aluminum storefront at the retail level, a blend of about 90. Roof: membrane over polyiso at about 28. Washington banned HFC XPS in 2021, but this LCA is from 2022 and tool data lags, so I allow some upside.
Totals: opaque 1,675 x 45 = 75,400; glazing 285 x 90 = 25,650; roof 620 x 28 = 17,360. Sum about 118,400 kgCO2e, about 46 kgCO2e/m2 of walls and roof. That is acceptable for wood frame with 15% glazing.
Per CFA: 24.2. Range 20-30, so A = 25.
Calibration: Multifamily, no envelope area given, K = 1.60, giving 40.

Step B. Multifamily, 6-10 storeys: B = 48.

Step C. FINAL = 0.5 x 40 + 0.5 x 48 = 44. Range 35.2-52.8.

BOTTOM_UP_kgCO2e_per_m2: 25
CALIBRATED_kgCO2e_per_m2: 40
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 35.2 - 52.8

===== KEY: project-117__run1 =====
Scope check: BSEF includes E.

Step A. CFA 10,700 m2. Education, mass timber, 6-10 storeys (I assume 7), height 22.6-30 m, no envelope area given. Pennsylvania 4A.
Areas: footprint and roof about 1,530 m2. Wall at about 0.4 x 10,700 gives 4,280 m2. WWR missing, so I use 0.33: glazing about 1,412 m2 and opaque wall about 2,868 m2.
Assemblies: brick veneer or metal panel on stud backup with continuous insulation at about 90. Aluminum windows and curtain wall at about 135. Roof: membrane over polyiso at about 28. HFC XPS at grade or on the roof is plausible in Pennsylvania (no state ban) and widens the upper bound.
Totals: opaque 2,868 x 90 = 258,100; glazing 1,412 x 135 = 190,600; roof 1,530 x 28 = 42,800. Sum about 491,500 kgCO2e, about 84 kgCO2e/m2 of walls and roof, which is consistent.
Per floor area: 45.9. The project reports a 55% reduction, but most of it is likely structural. Range 38-56, so A = 47.
Calibration: Education, no envelope area given, K = 1.46, giving 68.6.

Step B. Education, 6-10 storeys: B = 85.

Step C. FINAL = 0.5 x 68.6 + 0.5 x 85 = 76.8. Range 61.4-92.2.

BOTTOM_UP_kgCO2e_per_m2: 47
CALIBRATED_kgCO2e_per_m2: 68.6
BENCHMARK_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 61.4 - 92.2

===== KEY: project-292__run1 =====
Scope check: BSECF includes E.

Step A. Major renovation. Floor area = renovated GFA = 930 m2. Public assembly, 1 storey, zone 8 (subarctic). The envelope area given is 1,937 m2. WWR 0.48.
Areas: roof about 930 m2 and walls about 1,007 m2. Glazing is about 483 m2 and opaque wall about 524 m2.
A full new enclosure would be: glazing 483 x 140 = 67,600; opaque steel stud or CMU with thick insulation 524 x 90 = 47,200; roof with thick polyiso 930 x 35 = 32,600. Sum about 147,000 kgCO2e, which is 158 kgCO2e/m2 of floor.
Renovation evidence: mass_total is only about 76.5 t, or 82 kg/m2 across all scopes. That is far below new construction, so only limited new envelope work was installed, probably new storefront, windows and some insulation or re-roofing. I take about 30% of the full enclosure, with a wide range.
Per floor area: about 45. Range 25-65, so A = 45.
Calibration: Public Assembly, envelope area given, K = 1.37, giving 61.7.

Step B. Public Assembly, 1 storey: B = 108.

Step C. FINAL = 0.5 x 61.7 + 0.5 x 108 = 84.8. Range 67.9-101.8.

BOTTOM_UP_kgCO2e_per_m2: 45
CALIBRATED_kgCO2e_per_m2: 61.7
BENCHMARK_kgCO2e_per_m2: 108
RANGE_kgCO2e_per_m2: 67.9 - 101.8

===== KEY: project-227__run1 =====
Scope check: BSE includes E.

Step A. CFA 78,500 m2. Large public assembly building (about 31,800 occupants, likely an arena), 2-5 storeys, height 31-45 m. The envelope area given is 75,066 m2, a ratio of 0.96. WWR 0.116.
Areas: a footprint of about 25,000 m2 gives a roof of about 25,000 m2, a ground slab of about 25,000 m2 and walls of about 25,000 m2. Glazing is about 2,900 m2 and opaque wall about 22,100 m2.
Assemblies: Type I-B steel in zone 5A. Walls are precast or metal panel on steel stud with insulation at about 90. Curtain wall and storefront at about 140. Roof: membrane over polyiso at about 26. HFC XPS is plausible in the Midwest, so I allow some upside.
Totals: opaque 22,100 x 90 = 1,989,000; glazing 2,900 x 140 = 406,000; roof 25,000 x 26 = 650,000. Sum about 3.05 Mt kgCO2e, about 41 kgCO2e/m2 of envelope. That is acceptable because a third of the envelope area is uninsulated or lightly insulated slab and the glazing is low.
Per CFA: 38.8. Range 32-50, so A = 41.
Calibration: Public Assembly, envelope area given, K = 1.37, giving 56.2.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 56.2 + 0.5 x 97 = 76.6. Range 61.3-91.9.

BOTTOM_UP_kgCO2e_per_m2: 41
CALIBRATED_kgCO2e_per_m2: 56.2
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 61.3 - 91.9

===== KEY: project-62__run1 =====
Scope check: BSECF includes E.

Step A. CFA 7,850 m2 (GFA 4,500 m2 plus 3,350 m2 of below-grade parking). Public assembly, 1 storey, height 0-7.5 m, California 3B, no envelope area given. Walls R-19, roof R-30.
Areas: roof = footprint = 4,500 m2. A plan of about 67 x 67 m has a perimeter of about 268 m; at about 6 m high the wall area is about 1,610 m2. WWR missing, so I use 0.18: glazing about 290 m2 and opaque wall about 1,320 m2.
Assemblies: concrete frame with wood infill (Type V-B). Walls are stud or concrete with stucco and batts at about 60. Aluminum storefront at about 145. Roof: membrane over polyiso at about 25. Below-grade waterproofing and insulation add about 10,000.
Totals: opaque 1,320 x 60 = 79,200; glazing 290 x 145 = 42,000; roof 4,500 x 25 = 112,500; below grade 10,000. Sum about 243,700 kgCO2e, about 40 kgCO2e/m2 of walls and roof. That is roof-dominated, and I allow upside for a heavier roof.
Per CFA: 31.0. Range 26-40, so A = 33.
Calibration: Public Assembly, no envelope area given, K = 1.29, giving 42.6.

Step B. Public Assembly, 1 storey: B = 108.

Step C. FINAL = 0.5 x 42.6 + 0.5 x 108 = 75.3. Range 60.2-90.4.

BOTTOM_UP_kgCO2e_per_m2: 33
CALIBRATED_kgCO2e_per_m2: 42.6
BENCHMARK_kgCO2e_per_m2: 108
RANGE_kgCO2e_per_m2: 60.2 - 90.4

===== KEY: project-231__run1 =====
Scope check: BSE includes E.

Step A. CFA 54,500 m2. Laboratory, 11-15 storeys (I assume 12), height 61-90 m (tall lab floors), no envelope area given. Massachusetts 5A.
Areas: footprint and roof about 4,410 m2. Wall: tall floor-to-floor heights put it at about 0.33 m2 per m2 of floor, about 17,500 m2. WWR missing, so I use 0.35 for a lab: glazing about 6,125 m2 and opaque wall about 11,375 m2.
Assemblies: Type I-B steel. Glazing is unitized curtain wall at about 180. Opaque wall is curtain-wall spandrel, metal panel or precast with backup at about 110. Roof: membrane over polyiso at about 28. HFC XPS at grade is plausible in Massachusetts.
Totals: glazing 6,125 x 180 = 1,102,500; opaque 11,375 x 110 = 1,251,250; roof 4,410 x 28 = 123,500. Sum about 2.48 Mt kgCO2e, about 113 kgCO2e/m2 of walls and roof, which is consistent with a curtain-wall lab.
Per CFA: 45.4. Range 38-56, so A = 47.
Calibration: Laboratory, no envelope area given, K = 1.33, giving 62.5.

Step B. Laboratory, 11 or more storeys: B = 129.

Step C. FINAL = 0.5 x 62.5 + 0.5 x 129 = 95.8. Range 76.6-114.9.

BOTTOM_UP_kgCO2e_per_m2: 47
CALIBRATED_kgCO2e_per_m2: 62.5
BENCHMARK_kgCO2e_per_m2: 129
RANGE_kgCO2e_per_m2: 76.6 - 114.9

===== KEY: project-148__run1 =====
Scope check: BSECF includes E.

Step A. CFA 25,250 m2. Education, mass timber over a steel podium, 6-10 storeys (I assume 8), height 31-45 m. The envelope area given is 20,337 m2. WWR 0.35, walls R-13.9, roof R-39.1. BC 4C.
Areas: roof about 3,156 m2 and ground slab about 3,156 m2, so the walls are about 14,025 m2. Glazing is about 4,909 m2 and opaque wall about 9,116 m2.
Assemblies: walls are steel or wood stud with exterior insulation and a metal-panel or fiber-cement rainscreen at about 85. Aluminum windows and curtain wall at about 140. Roof: membrane over polyiso at about 28. Canada banned HFC XPS in 2021, so a low-GWP insulation case applies.
Totals: opaque 9,116 x 85 = 774,900; glazing 4,909 x 140 = 687,300; roof 3,156 x 28 = 88,400. Sum about 1.55 Mt kgCO2e, about 76 kgCO2e/m2 of envelope, which is consistent.
Per floor area: 61.4. Range 52-72, so A = 62.
Calibration: Education, envelope area given, K = 1.05, giving 65.1.

Step B. Education, 6-10 storeys: B = 85.

Step C. FINAL = 0.5 x 65.1 + 0.5 x 85 = 75.1. Range 60.0-90.1.

BOTTOM_UP_kgCO2e_per_m2: 62
CALIBRATED_kgCO2e_per_m2: 65.1
BENCHMARK_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 60.0 - 90.1

===== KEY: project-169__run1 =====
Scope check: BSE includes E.

Step A. CFA 119,000 m2 (GFA 88,750 m2 plus 30,250 m2 of below-grade parking). Concrete office, 11-15 storeys (I assume 13), height 46-60 m. The envelope area given is 30,956 m2. WWR 0.35, walls R-24, roof R-39.5. Seattle 4C.
Areas: roof about 6,830 m2. The ground slab sits over the parking, so I treat the remaining 24,126 m2 as wall. Glazing is about 8,444 m2 and opaque wall about 15,682 m2.
Assemblies: an office above 10 storeys suggests unitized curtain wall at about 180. Opaque wall is spandrel, metal panel or precast with backup at about 100. Roof: membrane over polyiso at about 30.
Totals: glazing 8,444 x 180 = 1,520,000; opaque 15,682 x 100 = 1,568,200; roof 6,830 x 30 = 204,900. Sum about 3.29 Mt kgCO2e, about 106 kgCO2e/m2 of envelope, which is consistent.
Per CFA (including the large parking area): 27.7. Range 23-34, so A = 28.5.
Calibration: Office, envelope area given, K = 1.23, giving 35.1.

Step B. Office, 11 or more storeys: B = 72.

Step C. FINAL = 0.5 x 35.1 + 0.5 x 72 = 53.5. Range 42.8-64.3.

BOTTOM_UP_kgCO2e_per_m2: 28.5
CALIBRATED_kgCO2e_per_m2: 35.1
BENCHMARK_kgCO2e_per_m2: 72
RANGE_kgCO2e_per_m2: 42.8 - 64.3

===== KEY: project-17__run1 =====
Scope check: BSECF includes E.

Step A. CFA 10,500 m2. Education, 2-5 storeys (I assume 3), height 15.1-22.5 m, South East zone 2A, no envelope area given.
Areas: footprint and roof about 3,500 m2. Wall at about 0.4 x 10,500 gives 4,200 m2. WWR missing, so I use 0.33: glazing about 1,386 m2 and opaque wall about 2,814 m2.
Assemblies: Type II-B steel. Schools are mostly brick veneer, here on steel stud, at about 105. Aluminum windows and storefront at about 125. Roof: membrane over polyiso at about 24 (warm climate).
Totals: opaque 2,814 x 105 = 295,500; glazing 1,386 x 125 = 173,250; roof 3,500 x 24 = 84,000. Sum about 552,750 kgCO2e, about 72 kgCO2e/m2 of walls and roof, which is consistent.
Per floor area: 52.6. Brick on CMU backup is common in the South East and would raise it. Range 45-62, so A = 53.5.
Calibration: Education, no envelope area given, K = 1.46, giving 78.1.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 78.1 + 0.5 x 86 = 82.1. Range 65.6-98.5.

BOTTOM_UP_kgCO2e_per_m2: 53.5
CALIBRATED_kgCO2e_per_m2: 78.1
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 65.6 - 98.5

===== KEY: project-48__run1 =====
Scope check: BSECF includes E.

Step A. CFA 21,750 m2. Warehouse, 1 storey, height 7.6-15 m, California 3B, no envelope area given.
Areas: roof = 21,750 m2. A 2:1 plan (about 209 x 104 m) has a perimeter of about 626 m; at about 11 m high the wall area is about 6,886 m2. WWR 0.05 gives glazing of about 344 m2 and opaque wall of about 6,542 m2.
Assemblies: steel roof framing with a concrete lateral system, so tilt-up concrete panels with furring and insulation at about 100. Storefront and doors at about 150. Roof: membrane over polyiso at about 24. California banned HFC XPS in 2021, so that case is unlikely.
Totals: walls 6,542 x 100 = 654,200; glazing 344 x 150 = 51,600; roof 21,750 x 24 = 522,000. Sum about 1.23 Mt kgCO2e, about 43 kgCO2e/m2 of walls and roof, which is consistent with a roof-dominated warehouse.
Per floor area: 56.5. Range 48-66, so A = 57.
Calibration: Warehouse, no envelope area given, K = 1.22, giving 69.5.

Step B. Warehouse and Storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 69.5 + 0.5 x 65 = 67.3. Range 53.8-80.7.

BOTTOM_UP_kgCO2e_per_m2: 57
CALIBRATED_kgCO2e_per_m2: 69.5
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 53.8 - 80.7
