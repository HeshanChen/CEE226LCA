===== KEY: project-277__run2 =====
Scope check: lca_phys_scope BSE includes E, so the full method applies.

Step A. Areas: bldg_therm_env_area 44,594 m2 is given for 18,900 m2 of floor, 1 storey. Roof is about 18,900 m2 and the ground slab about 18,900 m2, which leaves about 6,800 m2 of wall. WWR is taken as 0.05 (warehouse), so glazing and doors are about 340 m2 and opaque wall about 6,460 m2.
Assemblies: the wall is tilt-up concrete or insulated metal panel, the roof is membrane over polyiso, and there is perimeter slab-edge insulation. Colorado banned HFC XPS in 2021 and this LCA dates from 2023, so polyiso is likely.
Intensities: wall 100 kg/m2 gives 646k kg. Glazing and doors 150 kg/m2 give 51k. Roof 24 kg/m2 gives 454k. Slab edge adds 10k. The total is about 1,161k kgCO2e, or 61 kg/m2 of floor and 26 kg/m2 of envelope, which is low because the roof and slab dominate a warehouse.
Range: the low case (IMP at 55, polyiso at 20) gives 42. The high case (tilt-up at 125, roof at 40) gives 86. A = 64.
Calibration: Warehouse with envelope area given, K = 0.88, so 0.88 x 64 = 56.

Step B. Warehouse and Storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 56 + 0.5 x 65 = 60.5, and the range is 0.8 to 1.2 x FINAL.
BOTTOM_UP_kgCO2e_per_m2: 64
CALIBRATED_kgCO2e_per_m2: 56
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 48 - 73

===== KEY: project-180__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: bldg_therm_env_area 3,346 m2 for 1,920 m2 of floor, about 3 storeys. Roof is about 640 m2 and the slab about 640 m2, so wall is about 2,066 m2. At WWR 0.37, glazing is 764 m2 and opaque wall 1,302 m2.
Assemblies: a mass-timber school in WA (zone 4C, walls R-18, roof R-37). The likely wall is wood or steel stud with fiber cement, metal panel or partial brick. Windows are aluminum. The roof is membrane over polyiso, since WA banned HFC XPS by 2021 and the LCA dates from 2023. One basement level carries some below-grade insulation.
Intensities: wall 70 gives 91k. Glazing 130 gives 99k. Roof 30 (thick) gives 19k. Below grade and slab add 5k. The total is about 215k, which is 112 kg/m2 of floor and 64 kg/m2 of envelope, consistent with the references.
Range: the low case (siding 45, fiberglass windows 95, roof 24) gives 79. The high case (brick or metal 100, aluminum 150, roof 40) gives 143. A = 111.
Calibration: Education with envelope area given, K = 1.05, so 117.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 117 + 0.5 x 86 = 101.5.
BOTTOM_UP_kgCO2e_per_m2: 111
CALIBRATED_kgCO2e_per_m2: 117
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 81 - 122

===== KEY: project-91__run2 =====
Scope check: lca_phys_scope BSE includes E.

Step A. Areas: no envelope area is given. Floor is 570 m2 in 1 storey, so the footprint is 570 m2. A perimeter of about 96 m at about 8 m height gives about 770 m2 of wall. At WWR 0.05, glazing and doors are about 40 m2 and opaque wall about 730 m2.
Assemblies: a small CA warehouse (zone 3C) with masonry shear walls, so the walls are likely insulated CMU or CMU with a metal panel. The roof is membrane over thin polyiso, and slab insulation is negligible.
Intensities: wall 90 gives 66k. Doors and glazing 150 give 6k. Roof 24 gives 14k. Slab edge adds 1k. The total is about 87k, which is 152 kg/m2 of floor and 45 kg/m2 of envelope. That is plausible given the low glazing.
Range: the low case (metal panel 70, roof 20) gives 122. The high case (insulated CMU with finish 120, roof 40) gives 206. A = 164.
Calibration: Warehouse without envelope area, K = 1.22, so 200.

Step B. Warehouse and Storage, 1 storey: B = 65.

Step C. FINAL = 0.5 x 200 + 0.5 x 65 = 132.5.
BOTTOM_UP_kgCO2e_per_m2: 164
CALIBRATED_kgCO2e_per_m2: 200
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 106 - 159

===== KEY: project-266__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: no envelope area is given. Floor is 590 m2 over 2 storeys, so the footprint is about 295 m2. A perimeter of about 69 m at 8 m height gives about 550 m2 of wall. At WWR 0.15, glazing is 83 m2 and opaque wall 469 m2.
Assemblies: a light wood-frame office in zone 5B (walls R-20, roof R-30). The wall is wood stud with fiber cement or siding and continuous insulation. Windows are aluminum or fiberglass. The roof is membrane over polyiso. The state is unknown and the LCA was done in Tally in 2022, so HFC XPS at the roof and slab edge is plausible in the high case.
Intensities: wall 50 gives 23.5k. Windows 120 give 10k. Roof 24 gives 7k. Slab edge adds 1.5k. The total is about 42k, which is 71 kg/m2 of floor and 37 kg/m2 of envelope. That is low, so I revisited the high-carbon options.
Range: the low case (siding 35, vinyl 70, polyiso 22) gives 51. The high case (wood with brick 80, aluminum 140, HFC XPS roof 100) gives 138. A = 95.
Calibration: Office without envelope area, K = 1.49, so 142.

Step B. Office, 2 to 5 storeys: B = 82.

Step C. FINAL = 0.5 x 142 + 0.5 x 82 = 112.
BOTTOM_UP_kgCO2e_per_m2: 95
CALIBRATED_kgCO2e_per_m2: 142
BENCHMARK_kgCO2e_per_m2: 82
RANGE_kgCO2e_per_m2: 90 - 134

===== KEY: project-190__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: no envelope area is given. Floor is 3,150 m2 over about 4 storeys (15-22.5 m), so the footprint is about 790 m2. A perimeter of about 112 m at 17 m height gives about 1,900 m2 of wall. WWR is assumed at 0.33 (education), so glazing is 627 m2 and opaque wall 1,273 m2.
Assemblies: a concrete Type I-B school in WA, completed 2015 and assessed in Tally in 2021. The likely wall is brick veneer or metal panel on steel stud. Windows are aluminum, with some curtain wall. The roof is membrane over polyiso, with HFC XPS plausible because the design predates the 2021 ban.
Intensities: wall 100 gives 127k. Glazing 140 gives 88k. Roof 24 gives 19k. Slab edge adds 3k. The total is about 237k, which is 75 kg/m2 of floor and 68 kg/m2 of envelope, so it is consistent.
Range: the low case (fiber cement 65, aluminum 110, polyiso 20) gives 54. The high case (brick on CMU 135, curtain wall 160, HFC XPS roof 100) gives 112. A = 83.
Calibration: Education without envelope area, K = 1.46, so 121.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 121 + 0.5 x 86 = 103.5.
BOTTOM_UP_kgCO2e_per_m2: 83
CALIBRATED_kgCO2e_per_m2: 121
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 83 - 124

===== KEY: project-209__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: no envelope area is given. CFA is 8,700 m2, of which 1,010 m2 is below-grade parking. Above-grade floor of 7,690 m2 over about 6 storeys gives a footprint of about 1,280 m2. A perimeter of about 152 m at 20 m height gives about 3,040 m2 of wall. At WWR 0.29, glazing is 895 m2 and opaque wall 2,145 m2.
Assemblies: wood light frame over a concrete podium in WA (walls R-21, roof R-38). The wall is wood stud with fiber cement or panel siding. Windows are mostly vinyl, with aluminum storefront at the retail level. The roof is membrane over polyiso, which is likely given the 2022 WA date. Below-grade insulation is small.
Intensities: wall 55 gives 118k. Glazing blended at 85 gives 76k. Roof 26 gives 33k. Below grade adds 2k. The total is about 229k, which is 26 kg/m2 of CFA and 41 kg/m2 of envelope, typical for vinyl and wood-frame residential.
Range: the low case (siding 35, vinyl 55, polyiso 22) gives 18. The high case (metal panel or brick 90, aluminum 130, roof 40) gives 42. A = 30.
Calibration: Multifamily without envelope area, K = 1.60, so 48.

Step B. Multifamily, 6 to 10 storeys: B = 48.

Step C. FINAL = 0.5 x 48 + 0.5 x 48 = 48.
BOTTOM_UP_kgCO2e_per_m2: 30
CALIBRATED_kgCO2e_per_m2: 48
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 38 - 58

===== KEY: project-100__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: bldg_therm_env_area 23,413 m2 for 24,500 m2 of floor, about 3.5 storeys (15-22.5 m). Roof is about 7,000 m2 and the slab about 7,000 m2, so wall is about 9,400 m2. At WWR 0.36, glazing is 3,390 m2 and opaque wall 6,020 m2.
Assemblies: a steel-frame school in South Central US, zone 4A. The likely wall is brick veneer on steel stud. Fenestration is aluminum windows, storefront and some curtain wall. The roof is membrane over polyiso. The LCA was done in Tally in 2023 in a state with no ban, so HFC XPS is plausible. Insulation is perimeter slab only.
Intensities: wall 105 gives 632k. Glazing 140 gives 475k. Roof 24 gives 168k. Slab adds 5k. The total is about 1,280k, which is 52 kg/m2 of floor and 55 kg/m2 of envelope, so it is consistent.
Range: the low case (stucco or fiber cement 70, aluminum 115, polyiso 20) gives 39. The high case (brick on CMU 150, curtain wall 160, HFC XPS roof 100) gives 88. A = 64.
Calibration: Education with envelope area given, K = 1.05, so 67.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 67 + 0.5 x 86 = 76.5.
BOTTOM_UP_kgCO2e_per_m2: 64
CALIBRATED_kgCO2e_per_m2: 67
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 61 - 92

===== KEY: project-28__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: no envelope area is given. Floor is 5,200 m2 over about 4 storeys, so the footprint is about 1,300 m2. A perimeter of about 150 m at about 17 m height gives about 2,500 m2 of wall. WWR is assumed at 0.33, so glazing is 825 m2 and opaque wall 1,675 m2.
Assemblies: a concrete school in a hot dry climate, zone 2B (walls R-13, roof R-20). The likely wall is steel stud with stucco or cement plaster, possibly with some brick or concrete. Windows are aluminum. The roof is membrane over thin polyiso. The state is unknown and the LCA was done in Tally, so HFC XPS is plausible in the high case.
Intensities: wall 75 gives 126k. Glazing 125 gives 103k. Roof 20 gives 26k. Slab adds 1k. The total is about 256k, which is 49 kg/m2 of floor and about 50 kg/m2 of envelope.
Range: the low case (EIFS 50, aluminum 100, polyiso 18) gives 37. The high case (brick or precast 120, curtain wall 150, HFC XPS 90) gives 85. A = 61.
Calibration: Education without envelope area, K = 1.46, so 89.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 89 + 0.5 x 86 = 87.5.
BOTTOM_UP_kgCO2e_per_m2: 61
CALIBRATED_kgCO2e_per_m2: 89
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 70 - 105

===== KEY: project-134__run2 =====
Special case: lca_phys_scope is CF (interior construction and finishes only) and does not contain E. The enclosure was not modelled and only incidental items are booked under it, so Steps A to C are skipped and the fixed values are reported.
BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-177__run2 =====
Scope check: lca_phys_scope BSECF includes E.

Step A. Areas: bldg_therm_env_area 14,739 m2 for 5,950 m2 of floor, about 2 storeys. Roof is about 2,975 m2 and the slab about 2,975 m2, so wall is about 8,790 m2. At WWR 0.284, glazing is 2,496 m2 and opaque wall 6,293 m2.
Assemblies: a steel-frame school in WA (zone 4C, walls R-18, roof R-36). The likely wall is brick veneer or metal panel on steel stud. Fenestration is aluminum storefront and windows. The roof is membrane over polyiso. Under-slab and edge insulation are included.
Intensities: wall 95 gives 598k. Glazing 135 gives 337k. Roof 28 gives 83k. Slab insulation adds 12k. The total is about 1,030k, which is 173 kg/m2 of floor and 70 kg/m2 of envelope, so it is consistent. The high value per floor area comes from the large envelope-to-floor ratio of 2.5.
Range: the low case (fiber cement 65, aluminum 110, polyiso 22) gives 128. The high case (brick on CMU 140, curtain wall 155, roof 40) gives 235. A = 182.
Calibration: Education with envelope area given, K = 1.05, so 191.

Step B. Education, 2 to 5 storeys: B = 86.

Step C. FINAL = 0.5 x 191 + 0.5 x 86 = 138.5.
BOTTOM_UP_kgCO2e_per_m2: 182
CALIBRATED_kgCO2e_per_m2: 191
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 111 - 166
