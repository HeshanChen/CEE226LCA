===== KEY: project-146__run0 =====
Special-case check: lca_phys_scope = ECF, so the enclosure (E) was modelled. Normal steps apply.

Step A. This is an office tenant improvement. bldg_cfa is not given, so floor area = renovated 3,450 m2. There is no envelope area, so K = 1.49. Mass is 395,715 kg, about 115 kg/m2, which is light and points to limited new envelope work within an existing multi-storey concrete building (Type I-B, 15-22 m tall).
1. Areas: affected exterior wall is about 0.2 m2 per m2 of floor, giving about 690 m2. At an assumed 40% WWR, that is 276 m2 glazed and 414 m2 opaque.
2. Assemblies: new aluminum storefront or window replacement, plus steel-stud and metal-panel infill. Oregon 2023, so HFC XPS is unlikely.
3. Intensities: glazing 276 x 145 = 40,000; opaque 414 x 80 = 33,000. Total about 73,000 kgCO2e.
4-5. Divided by 3,450 m2 this is about 21 kgCO2e/m2. Range 10-35 (minimal to partial re-clad), A = 22.
7. CALIBRATED = 1.49 x 22 = 32.8.

Step B. Office, 1 storey: B = 131.

Step C. FINAL = 0.5 x 32.8 + 0.5 x 131 = 81.9. Range 65.5 - 98.3.

BOTTOM_UP_kgCO2e_per_m2: 22
CALIBRATED_kgCO2e_per_m2: 32.8
BENCHMARK_kgCO2e_per_m2: 131
RANGE_kgCO2e_per_m2: 65.5 - 98.3

===== KEY: project-131__run0 =====
Special-case check: scope BSE includes E.

Step A. Education building, 7,900 m2, envelope area 7,804 m2 (so K = 1.05). WWR 0.43, R-16 walls, R-50 roof, mass timber, Washington, assessed 2021.
1. Areas: about 4 storeys, so roof about 1,975 m2 and ground slab about 1,975 m2. Walls = 7,804 - 3,950 = 3,854 m2, of which 1,657 m2 glazed and 2,197 m2 opaque.
2. Assemblies: steel or wood stud with brick and fiber-cement mix; aluminum windows and curtain wall; R-50 polyiso roof. HFC XPS is unlikely in WA after 2021.
3. Intensities: glazing 1,657 x 130 = 215,000; opaque 2,197 x 85 = 187,000; roof (thick polyiso) 1,975 x 40 = 79,000; slab insulation 1,975 x 8 = 16,000. Total about 497,000 kgCO2e.
4. Check: 64 kgCO2e per m2 of envelope, which is consistent.
5. Divided by 7,900 m2 this is about 63. Range 50-80, A = 65.
7. CALIBRATED = 1.05 x 65 = 68.3.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 68.3 + 0.5 x 86 = 77.2. Range 61.7 - 92.6.

BOTTOM_UP_kgCO2e_per_m2: 65
CALIBRATED_kgCO2e_per_m2: 68.3
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 61.7 - 92.6

===== KEY: project-180__run0 =====
Special-case check: scope BSECF includes E.

Step A. Education building, 1,920 m2, envelope area 3,346 m2 (K = 1.05). WWR 0.37, R-18 walls, R-37 roof, Type V-B mass timber, Washington, 2023.
1. Areas: about 2 storeys, so roof about 960 m2 and slab about 960 m2. Walls are 1,426 m2: 528 m2 glazed and 898 m2 opaque.
2. Assemblies: wood stud with fiber cement and some veneer; aluminum or fiberglass windows; polyiso roof. Low-GWP insulation is likely (WA 2023).
3. Intensities: glazing 528 x 130 = 69,000; opaque 898 x 70 = 63,000; roof 960 x 32 = 31,000; slab 960 x 8 = 8,000. Total about 171,000 kgCO2e.
4. Check: 51 kgCO2e per m2 of envelope. I raised the first pass (47) to cover trim and attachments.
5. Divided by 1,920 m2 this is about 89. Range 75-105, A = 90.
7. CALIBRATED = 1.05 x 90 = 94.5.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 94.5 + 0.5 x 86 = 90.25. Range 72.2 - 108.3.

BOTTOM_UP_kgCO2e_per_m2: 90
CALIBRATED_kgCO2e_per_m2: 94.5
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 72.2 - 108.3

===== KEY: project-276__run0 =====
Special-case check: scope BSECF includes E.

Step A. Public assembly building, 20,750 m2, envelope area 10,462 m2 (K = 1.37). WWR 0.07, steel frame with masonry shear walls, Colorado 5B, Tally 2023.
1. Areas: roof about 3,500 m2 and slab about 3,500 m2, leaving 3,460 m2 of wall: 242 m2 glazed and 3,218 m2 opaque.
2. Assemblies: brick or CMU masonry walls with insulation; storefront glazing; membrane roof over rigid insulation. Colorado banned HFC XPS in 2021, but tool datasets lag, so HFC XPS is kept as the high case.
3. Intensities: opaque 3,218 x 140 = 450,000; glazing 242 x 145 = 35,000; roof polyiso 3,500 x 30 = 105,000; slab 3,500 x 8 = 28,000. Total about 618,000 kgCO2e. The HFC XPS roof alternative raises this to about 846,000.
4. Check: 59 kgCO2e per m2 of envelope, which is plausible for masonry.
5. Divided by 20,750 m2: 30 (base) to 41 (HFC XPS). Range 28-42, A = 35.
7. CALIBRATED = 1.37 x 35 = 48.0.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 48.0 + 0.5 x 97 = 72.5. Range 58.0 - 87.0.

BOTTOM_UP_kgCO2e_per_m2: 35
CALIBRATED_kgCO2e_per_m2: 48.0
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 58.0 - 87.0

===== KEY: project-127__run0 =====
Special-case check: scope BSE includes E.

Step A. Public assembly building, 3,750 m2, envelope area 7,517 m2 (ratio 2.0, so tall volumes; K = 1.37). WWR 0.336, R-23 walls, R-42 roof, steel and masonry, Washington, Tally 2019.
1. Areas: about 3 storeys, so roof about 1,250 m2 and slab about 1,250 m2. Walls are 5,017 m2: 1,686 m2 glazed and 3,331 m2 opaque.
2. Assemblies: masonry veneer on CMU or steel stud; curtain wall and storefront; R-42 polyiso roof. An HFC XPS roof is possible in a 2019 Tally model.
3. Intensities: opaque 3,331 x 130 = 433,000; glazing 1,686 x 140 = 236,000; roof 1,250 x 35 = 44,000; slab 1,250 x 8 = 10,000. Total about 723,000 kgCO2e. HFC XPS on the roof would add about 125,000.
4. Check: 96 kgCO2e per m2 of envelope, which is consistent with heavy masonry and high glazing.
5. Divided by 3,750 m2: 193 base, 226 with HFC XPS. Range 170-225, A = 197.
7. CALIBRATED = 1.37 x 197 = 269.9.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 269.9 + 0.5 x 97 = 183.5. Range 146.8 - 220.1.

BOTTOM_UP_kgCO2e_per_m2: 197
CALIBRATED_kgCO2e_per_m2: 269.9
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 146.8 - 220.1

===== KEY: project-172__run0 =====
Special-case check: scope BSECF includes E.

Step A. Multifamily building, 18,900 m2, envelope area 10,655 m2 (K = 0.97). WWR 0.28, 11-15 storeys, mass timber (Type IV-B), BC, 2023. Canada banned HFC XPS in 2021, so low-GWP insulation is assumed.
1. Areas: about 13 storeys, so roof about 1,454 m2 and slab about 1,454 m2. Walls are 7,747 m2: 2,169 m2 glazed and 5,578 m2 opaque.
2. Assemblies: steel or wood stud with metal panel or fiber-cement rainscreen and exterior mineral wool; punched aluminum or fiberglass windows; polyiso roof.
3. Intensities: glazing 2,169 x 120 = 260,000; opaque 5,578 x 75 = 418,000; roof 1,454 x 28 = 41,000; slab 1,454 x 8 = 12,000. Total about 731,000 kgCO2e.
4. Check: 69 kgCO2e per m2 of envelope, which is consistent.
5. Divided by 18,900 m2 this is about 39. Range 32-48, A = 40.
7. CALIBRATED = 0.97 x 40 = 38.8.

Step B. Multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 38.8 + 0.5 x 71 = 54.9. Range 43.9 - 65.9.

BOTTOM_UP_kgCO2e_per_m2: 40
CALIBRATED_kgCO2e_per_m2: 38.8
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 43.9 - 65.9

===== KEY: project-171__run0 =====
Special-case check: scope BSECF includes E.

Step A. Multifamily building, CFA 13,600 m2 (GFA 10,350), envelope area 10,936 m2 (K = 0.97). WWR 0.5, R-30 walls and roof, concrete, 11-15 storeys, 46-60 m tall, BC, 2023.
1. Areas: about 14 storeys, so roof about 740 m2 and slab about 740 m2. Walls are about 9,455 m2: 4,728 m2 glazed and 4,728 m2 opaque.
2. Assemblies: aluminum window wall (typical of BC high-rise residential); steel stud or concrete with metal panel and R-30 exterior mineral wool; polyiso roof. No HFC XPS (Canada 2023).
3. Intensities: window wall 4,728 x 175 = 827,000; opaque 4,728 x 85 = 402,000; roof 740 x 30 = 22,000; slab 740 x 8 = 6,000. Total about 1,257,000 kgCO2e.
4. Check: 115 kgCO2e per m2 of envelope, which is high-glazing and consistent.
5. Divided by 13,600 m2 this is about 92. Range 78-105, A = 92.
7. CALIBRATED = 0.97 x 92 = 89.2.

Step B. Multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 89.2 + 0.5 x 71 = 80.1. Range 64.1 - 96.1.

BOTTOM_UP_kgCO2e_per_m2: 92
CALIBRATED_kgCO2e_per_m2: 89.2
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 64.1 - 96.1

===== KEY: project-10__run0 =====
Special-case check: lca_phys_scope = CF, which does not contain E. The enclosure was not modelled and only incidental items are booked under it, so Steps A to C are skipped and the fixed values are reported.

BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-23__run0 =====
Special-case check: scope BSECF includes E.

Step A. Multifamily tower, CFA 70,000 m2 (GFA 53,100 plus 16,900 m2 of above-grade parking), envelope area 38,392 m2 (K = 0.97). WWR 0.30, R-19 walls, R-25 roof, 21 or more storeys, over 90 m tall, Texas 2A.
1. Areas: roof about 2,500 m2 and slab about 2,500 m2 (podium plus tower). Walls are about 33,400 m2: 10,020 m2 glazed and 23,370 m2 opaque.
2. Assemblies: a mix of aluminum window wall and windows; steel stud with stucco or metal panel, plus parking screen; polyiso roof. The climate is warm, so insulation is thin.
3. Intensities: glazing 10,020 x 160 = 1,603,000; opaque 23,370 x 75 = 1,753,000; roof 2,500 x 25 = 63,000; slab 8,000. Total about 3,427,000 kgCO2e.
4. Check: 89 kgCO2e per m2 of envelope, which is consistent.
5. Divided by 70,000 m2 this is about 49. Range 40-60, A = 50.
7. CALIBRATED = 0.97 x 50 = 48.5.

Step B. Multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 48.5 + 0.5 x 71 = 59.75. Range 47.8 - 71.7.

BOTTOM_UP_kgCO2e_per_m2: 50
CALIBRATED_kgCO2e_per_m2: 48.5
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 47.8 - 71.7

===== KEY: project-65__run0 =====
Special-case check: scope BSE includes E.

Step A. Multifamily building, 16,600 m2, envelope area 9,127 m2 (K = 0.97). WWR 0.65, R-15 walls, R-30 roof, concrete, 11-15 storeys, California, One Click LCA 2022.
1. Areas: about 13 storeys, so roof about 1,277 m2 and slab about 1,277 m2. Walls are 6,573 m2: 4,272 m2 glazed and 2,301 m2 opaque.
2. Assemblies: aluminum window wall; steel stud or concrete with metal panel or stucco; polyiso roof. No HFC XPS (California 2022).
3. Intensities: window wall 4,272 x 175 = 748,000; opaque 2,301 x 80 = 184,000; roof 1,277 x 28 = 36,000; slab 4,000. Total about 972,000 kgCO2e.
4. Check: 106 kgCO2e per m2 of envelope, which is consistent with heavy glazing.
5. Divided by 16,600 m2 this is about 59. Range 50-68, A = 59.
7. CALIBRATED = 0.97 x 59 = 57.2.

Step B. Multifamily, 11 or more storeys: B = 71.

Step C. FINAL = 0.5 x 57.2 + 0.5 x 71 = 64.1. Range 51.3 - 76.9.

BOTTOM_UP_kgCO2e_per_m2: 59
CALIBRATED_kgCO2e_per_m2: 57.2
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 51.3 - 76.9
