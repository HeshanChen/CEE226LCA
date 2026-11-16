===== KEY: project-41__run1 =====
Scope check: lca_phys_scope BSECF includes E, so the enclosure was modelled.

Step A. Floor area (CFA) 37,250 m2, 1 storey, height 7.6-15 m, no envelope area given. Roof = footprint = 37,250 m2. A 2:1 plan (about 273 x 136 m) gives a perimeter of about 818 m; at about 11 m high the wall area is about 9,000 m2. WWR missing, so I use 0.05 for a warehouse: glazing about 450 m2 and opaque wall about 8,550 m2.
Assemblies: Type II-B steel with a concrete lateral system, so tilt-up concrete panels with interior insulation (R-21) at about 100 kgCO2e/m2. Storefront and doors at about 150. Roof: membrane over polyiso on bare metal deck at about 24 (Texas, 2022, One Click LCA).
Totals: walls 8,550 x 100 = 855,000; glazing 450 x 150 = 67,500; roof 37,250 x 24 = 894,000. Sum about 1.82 Mt kgCO2e, which is about 39 kgCO2e/m2 of envelope. That is plausible here because the envelope is mostly roof.
Per floor area: 49 kgCO2e/m2. With a mineral-wool or XPS roof (about 40) the result rises to about 65. Range 42-62, so A = 52.
Calibration: Warehouse, no envelope area given, K = 1.22, giving 63.4.

Step B. Warehouse and Storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 63.4 + 0.5 x 65 = 64.2. Range 51.4-77.0.

BOTTOM_UP_kgCO2e_per_m2: 52
CALIBRATED_kgCO2e_per_m2: 63.4
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 51.4 - 77.0

===== KEY: project-234__run1 =====
Scope check: BSE includes E.

Step A. CFA 64,500 m2 over 11-15 storeys (I assume 13), height 61-90 m, no envelope area given. Footprint about 4,960 m2, so the roof is about 4,960 m2. Wall: at about 0.3 m2 per m2 of floor for a hospital, about 19,500 m2. A check with a 70 x 70 m plan and 70 m height gives a similar figure. WWR missing, so I use 0.3: glazing 5,850 m2 and opaque wall 13,650 m2.
Assemblies: Type I-B steel frame in zone 5A, so brick veneer or metal panel on steel stud with continuous insulation at about 100. Aluminum windows or curtain wall at about 150. Roof: membrane over polyiso at about 25.
Totals: opaque 13,650 x 100 = 1,365,000; glazing 5,850 x 150 = 877,500; roof 4,960 x 25 = 124,000. Sum about 2.37 Mt kgCO2e, about 78 kgCO2e/m2 of walls and roof, which is consistent.
Per floor area: 36.7. Higher options are unitized curtain wall, brick on CMU, and HFC XPS at grade. Range 30-45, so A = 37.5.
Calibration: Healthcare, no envelope area given, K = 1.34, giving 50.3.

Step B. Healthcare, 11-15 storeys is not listed, so I use other storeys: B = 73.

Step C. FINAL = 0.5 x 50.3 + 0.5 x 73 = 61.6. Range 49.3-73.9.

BOTTOM_UP_kgCO2e_per_m2: 37.5
CALIBRATED_kgCO2e_per_m2: 50.3
BENCHMARK_kgCO2e_per_m2: 73
RANGE_kgCO2e_per_m2: 49.3 - 73.9

===== KEY: project-44__run1 =====
Scope check: BSECF includes E.

Step A. Minor renovation. Floor area = renovated GFA = 3,600 m2. Multifamily, 2-5 storeys (I assume 3), no envelope area given. Mass is about 529 kg/m2, which shows substantial new material but less than a new building.
Areas: footprint and roof about 1,200 m2. Wall at about 0.45 m2 per m2 of floor gives about 1,620 m2. With WWR 0.172, glazing is about 279 m2 and opaque wall about 1,341 m2.
Assemblies: Type V-A wood light-frame in California 3B. Walls are wood stud, R-13 batt and stucco or fiber cement at about 40. Vinyl windows at about 65. Roof R-38 over polyiso or batts with membrane at about 25.
Totals for a full new envelope: 53,600 + 18,100 + 30,000 = 101,700 kgCO2e, about 36 kgCO2e/m2 of envelope. That is reasonable for wood-frame walls with little glazing. Per floor area this is 28.
Because this is a minor renovation, only part of the envelope is likely replaced (windows, re-roofing, some cladding). Range 15-35, so A = 25.
Calibration: Multifamily, no envelope area given, K = 1.60, giving 40.

Step B. Multifamily, 2-5 storeys: B = 55.

Step C. FINAL = 0.5 x 40 + 0.5 x 55 = 47.5. Range 38-57.

BOTTOM_UP_kgCO2e_per_m2: 25
CALIBRATED_kgCO2e_per_m2: 40
BENCHMARK_kgCO2e_per_m2: 55
RANGE_kgCO2e_per_m2: 38 - 57

===== KEY: project-42__run1 =====
Special case: lca_phys_scope is CF (interior construction and finishes only) and does not contain E. The enclosure was not modelled, and only incidental items are booked under it. Steps A to C are skipped, and the fixed values apply.

BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-69__run1 =====
Scope check: BSE includes E.

Step A. CFA 11,100 m2. Multifamily, 6-10 storeys (I assume 8), height 15-22.5 m, no envelope area given. Footprint and roof about 1,390 m2. Wall at about 0.45 m2 per m2 of floor gives about 5,000 m2. WWR missing, so I use 0.3: glazing 1,500 m2 and opaque wall 3,500 m2.
Assemblies: Type II-B with a concrete core and steel frame in California 3C (mild climate). Walls are steel stud with fiber cement or stucco and mineral wool at about 65. Aluminum windows at about 120. Roof: membrane over polyiso at about 25. California banned HFC XPS from 2021, so a high-GWP foam case is unlikely.
Totals: opaque 3,500 x 65 = 227,500; glazing 1,500 x 120 = 180,000; roof 1,390 x 25 = 34,750. Sum about 442,000 kgCO2e, about 69 kgCO2e/m2 of walls and roof, which is consistent.
Per floor area: 39.8. A metal-panel rainscreen or window wall is possible. Range 33-48, so A = 40.5.
Calibration: Multifamily, no envelope area given, K = 1.60, giving 64.8.

Step B. Multifamily, 6-10 storeys: B = 48.

Step C. FINAL = 0.5 x 64.8 + 0.5 x 48 = 56.4. Range 45.1-67.7.

BOTTOM_UP_kgCO2e_per_m2: 40.5
CALIBRATED_kgCO2e_per_m2: 64.8
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 45.1 - 67.7

===== KEY: project-123__run1 =====
Scope check: BSECF includes E.

Step A. CFA 4,800 m2. Education, 2-5 storeys (I assume 3), height 7.6-15 m, no envelope area given. Footprint and roof about 1,600 m2. Wall at about 0.4 m2 per m2 of floor gives 1,920 m2. WWR missing, so I use 0.33: glazing about 634 m2 and opaque wall about 1,286 m2.
Assemblies: Type III-B mass timber in Washington 4C. Walls are stud backup with continuous mineral wool and a brick or fiber-cement and metal rainscreen at about 75. Aluminum windows and storefront at about 120. Roof: membrane over polyiso at about 25. Washington banned HFC XPS in 2021, so that case is unlikely.
Totals: opaque 1,286 x 75 = 96,450; glazing 634 x 120 = 76,080; roof 1,600 x 25 = 40,000. Sum about 212,500 kgCO2e, about 60 kgCO2e/m2 of walls and roof, which is acceptable.
Per floor area: 44.3. The project reports a 44% reduction, which suggests low-carbon choices. Range 37-52, so A = 44.5.
Calibration: Education, no envelope area given, K = 1.46, giving 65.0.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 65.0 + 0.5 x 86 = 75.5. Range 60.4-90.6.

BOTTOM_UP_kgCO2e_per_m2: 44.5
CALIBRATED_kgCO2e_per_m2: 65.0
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 60.4 - 90.6

===== KEY: project-224__run1 =====
Scope check: BSECF includes E.

Step A. CFA 5,100 m2. Public assembly, 2-5 storeys, height 15-22.5 m (I assume 4 storeys). The envelope area given is 3,583 m2, a ratio of 0.70.
Areas: roof about 1,275 m2. I treat the remainder, about 2,308 m2, as above-grade wall, because the ground slab appears not to be included. With WWR 0.35, glazing is about 808 m2 and opaque wall about 1,500 m2.
Assemblies: Type V-A mass timber in Massachusetts zone 5A. Walls are stud backup with continuous insulation and a brick or metal-panel rainscreen at about 85. Curtain wall and storefront at about 140. Roof: membrane over thick polyiso at about 28. An HFC XPS case is possible at grade (Massachusetts had no ban).
Totals: opaque 1,500 x 85 = 127,500; glazing 808 x 140 = 113,100; roof 1,275 x 28 = 35,700. Sum about 276,300 kgCO2e, about 77 kgCO2e/m2 of envelope, which is consistent.
Per floor area: 54.2. The project reports a 60% reduction. Range 45-68, so A = 56.5.
Calibration: Public Assembly, envelope area given, K = 1.37, giving 77.4.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 77.4 + 0.5 x 97 = 87.2. Range 69.8-104.6.

BOTTOM_UP_kgCO2e_per_m2: 56.5
CALIBRATED_kgCO2e_per_m2: 77.4
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 69.8 - 104.6

===== KEY: project-107__run1 =====
Scope check: BSECF includes E.

Step A. Major renovation with an addition. Floor area = 960 + 90 = 1,050 m2. Mass is about 1,190 kg/m2, so this is substantially new construction, and the envelope is treated as new. The envelope area given is 1,449 m2. WWR is high at 0.57.
Areas: about 2 storeys, so the roof is about 525 m2 and the walls about 924 m2. Glazing is about 527 m2 and opaque wall about 397 m2.
Assemblies: Type II-B steel in zone 4A. The glazing is aluminum curtain wall and storefront at about 140. Opaque wall is steel stud with a metal-panel or brick veneer at about 95. Roof: membrane over polyiso at about 26.
Totals: glazing 527 x 140 = 73,800; opaque 397 x 95 = 37,700; roof 525 x 26 = 13,650. Sum about 125,100 kgCO2e, about 86 kgCO2e/m2 of envelope, which is consistent with a heavily glazed facade.
Per floor area: 119. Range 100-135, so A = 118.
Calibration: Public Assembly, envelope area given, K = 1.37, giving 161.7.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 161.7 + 0.5 x 97 = 129.3. Range 103.5-155.2.

BOTTOM_UP_kgCO2e_per_m2: 118
CALIBRATED_kgCO2e_per_m2: 161.7
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 103.5 - 155.2

===== KEY: project-43__run1 =====
Special case: lca_phys_scope is CF and does not contain E. The enclosure was not modelled, and only incidental items are booked under it. Steps A to C are skipped, and the fixed values apply.

BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-14__run1 =====
Scope check: BSECF includes E.

Step A. CFA 750 m2. Education, 1 storey, height 0-7.5 m, no envelope area given, zone 1A (very hot humid). Roof = footprint = 750 m2. For a small single building (about 30 x 25 m), the perimeter is about 100 m and the wall height about 4.5 m, so the wall area is about 450 m2. WWR missing, so I use 0.3: glazing about 135 m2 and opaque wall about 315 m2.
Assemblies: the masonry shear walls indicate CMU exterior walls with stucco or veneer and furring with insulation at about 110. Aluminum windows and doors at about 120. Roof: membrane over thin polyiso (hot climate) at about 22.
Totals: opaque 315 x 110 = 34,650; glazing 135 x 120 = 16,200; roof 750 x 22 = 16,500. Sum about 67,350 kgCO2e, about 56 kgCO2e/m2 of walls and roof, which is consistent.
Per floor area: 90. A brick-on-CMU option (about 150) or a metal roof would push it higher, and a thin roof would push it lower. Range 75-105, so A = 90.
Calibration: Education, no envelope area given, K = 1.46, giving 131.4.

Step B. Education, 1 storey: B = 104.

Step C. FINAL = 0.5 x 131.4 + 0.5 x 104 = 117.7. Range 94.2-141.2.

BOTTOM_UP_kgCO2e_per_m2: 90
CALIBRATED_kgCO2e_per_m2: 131.4
BENCHMARK_kgCO2e_per_m2: 104
RANGE_kgCO2e_per_m2: 94.2 - 141.2
