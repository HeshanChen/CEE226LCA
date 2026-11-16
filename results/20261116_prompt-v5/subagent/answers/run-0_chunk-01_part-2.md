===== KEY: project-135__run0 =====
Special case. lca_phys_scope is SCF, which does not include E, so the enclosure was not modelled and only incidental items are booked under it. I skipped Steps A to C and reported the fixed values.

BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-16__run0 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. CFA is 23,250 m2, and a height of 22.6-30 m suggests about 5 storeys, so the roof is about 4,650 m2. The perimeter is about 275 m, and at 27 m height the wall area is about 7,400 m2 (0.32 x floor, which is typical for hospitals). With a healthcare WWR of 0.3 that is 2,220 m2 of glazing and 5,180 m2 of opaque wall.
Assemblies (Texas 2A, concrete, One Click 2023): brick veneer on steel stud (105), aluminum windows (135), polyiso roof (24). The slab is uninsulated in this hot climate.
Totals: 544k + 300k + 112k = 955k, which is 41.1 per m2 of floor.
Range: the low case (90/115/20) gives 35.0. The high case (CMU/precast at 135, glazing at 170, roof at 40) gives 54.3. A = 44.7.
Calibration: K = 1.34, so CALIBRATED = 59.9.

Step B. Healthcare, 2-5 storeys: B = 68.

Step C. FINAL = 0.5 x 59.9 + 0.5 x 68 = 64.0. Range 51.2 - 76.7.

BOTTOM_UP_kgCO2e_per_m2: 44.7
CALIBRATED_kgCO2e_per_m2: 59.9
BENCHMARK_kgCO2e_per_m2: 68
RANGE_kgCO2e_per_m2: 51.2 - 76.7

===== KEY: project-108__run0 =====
Scope check: SEC includes E. This is a minor renovation of a mercantile building: 3,350 m2 renovated plus 50 m2 added, so the floor area is 3,400 m2. mass_total is only 146 t, about 43 kg/m2, which shows very little new material.

Step A. Areas: no envelope area is given. At 3 storeys the footprint and roof are about 1,133 m2. New-York-style street frontages limit the new envelope work to likely storefront replacement, some infill cladding and possibly a re-roof.
Assemblies (steel, NY 4A, One Click): aluminum storefront at about 150 m2 x 148 = 22k, opaque infill at about 100 m2 x 80 = 8k, and a possible roof re-cover at 1,133 m2 x 25 = 28k.
Range: the low case (storefront only, about 14k) gives 4.1. The high case (storefront, infill and re-roof, about 58.5k) gives 17.2. A = 10.7.
Calibration: K = 1.31 (other use), so CALIBRATED = 14.0.

Step B. Other use: B = 84.

Step C. FINAL = 0.5 x 14.0 + 0.5 x 84 = 49.0. Range 39.2 - 58.8.

BOTTOM_UP_kgCO2e_per_m2: 10.7
CALIBRATED_kgCO2e_per_m2: 14
BENCHMARK_kgCO2e_per_m2: 84
RANGE_kgCO2e_per_m2: 39.2 - 58.8

===== KEY: project-214__run0 =====
Scope check: BSE includes E.

Step A. Areas: envelope 8,919 m2. CFA is 38,750 m2, of which 29,450 m2 is above grade, over about 8 storeys. The roof is about 3,681 m2. I treated the slab over the below-grade parking as outside the reported area, so walls are about 5,238 m2. At WWR 0.236 that is 1,234 m2 of glazing and 4,004 m2 of opaque wall.
Assemblies (lab, steel, Massachusetts 5A, R-15 walls, R-38 roof, One Click 2023): metal panel or brick on steel stud (100), aluminum windows/curtain wall (145), R-38 polyiso roof (30). Massachusetts did not ban HFC XPS, so that option goes in the high case.
Totals: 400k + 179k + 110k = 690k. That is 77 per m2 of envelope, or 17.8 per m2 of CFA.
Range: the low case (90/130/25) gives 15.8. The high case (135/180, HFC-XPS roof at 100) gives 29.2. A = 22.5.
Calibration: K = 1.81, so CALIBRATED = 40.7.

Step B. Laboratory has no 6-10 storey benchmark, so I used "other storeys": B = 92.

Step C. FINAL = 0.5 x 40.7 + 0.5 x 92 = 66.4. Range 53.1 - 79.7.

BOTTOM_UP_kgCO2e_per_m2: 22.5
CALIBRATED_kgCO2e_per_m2: 40.7
BENCHMARK_kgCO2e_per_m2: 92
RANGE_kgCO2e_per_m2: 53.1 - 79.7

===== KEY: project-255__run0 =====
Scope check: BSE includes E.

Step A. Areas: the reported envelope (1,039 m2) is about equal to the CFA of 1,040 m2, which is low for a 1-storey building, so the slab is evidently excluded. I took walls at 0.2 x floor = 208 m2 (69 m2 of glazing at WWR 0.33 and 139 m2 of opaque wall) and the roof as the remaining 831 m2.
Assemblies (wood Type V-B, Colorado 5B, R-12.5 walls, R-30 roof, One Click 2023): wood stud with fiber cement/siding (45), aluminum windows (130), polyiso membrane roof (25).
Totals: 6.3k + 9.0k + 20.8k = 36.1k, which is 34.7 per m2 of floor and of envelope.
Range: the low case (35/100/22) gives 28.9. The high case (brick veneer at 80, glazing at 150, roof at 45) gives 56.6. A = 42.8.
Calibration: K = 1.05, so CALIBRATED = 44.9.

Step B. Education, 1 storey: B = 104.

Step C. FINAL = 0.5 x 44.9 + 0.5 x 104 = 74.5. Range 59.6 - 89.4.

BOTTOM_UP_kgCO2e_per_m2: 42.8
CALIBRATED_kgCO2e_per_m2: 44.9
BENCHMARK_kgCO2e_per_m2: 104
RANGE_kgCO2e_per_m2: 59.6 - 89.4

===== KEY: project-207__run0 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. CFA is 3,000 m2 over about 4 storeys (15-22.5 m), so the roof is about 750 m2. The perimeter is about 110 m, and at 17 m height the wall area is about 1,870 m2; I used 1,700 m2. WWR is missing, so I used 0.3 for a small office, giving 510 m2 of glazing and 1,190 m2 of opaque wall.
Assemblies (steel, Washington 4C, R-23 walls, R-30 roof, Tally 2021): steel stud with metal panel/fiber cement (80), aluminum windows (125), polyiso roof (25), slab edge at about 2k.
Totals: 95k + 64k + 19k + 2k = 180k, which is 60.0 per m2 of floor.
Range: the low case (1,500 m2 of wall at 60/100/22) gives 41.8. The high case (1,870 m2 of wall at 110/150/40) gives 87.4. A = 64.6.
Calibration: K = 1.49, so CALIBRATED = 96.3.

Step B. Office, 2-5 storeys: B = 82.

Step C. FINAL = 0.5 x 96.3 + 0.5 x 82 = 89.1. Range 71.3 - 106.9.

BOTTOM_UP_kgCO2e_per_m2: 64.6
CALIBRATED_kgCO2e_per_m2: 96.3
BENCHMARK_kgCO2e_per_m2: 82
RANGE_kgCO2e_per_m2: 71.3 - 106.9

===== KEY: project-260__run0 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. CFA is 2,150 m2 over about 2 storeys, so the roof is about 1,075 m2. For walls I used 0.3 x floor = 645 m2, a compromise between the school typical of 0.2 and a geometric estimate of about 0.55. At WWR 0.33 that is 213 m2 of glazing and 432 m2 of opaque wall.
Assemblies (mass timber school, Colorado 5B, Tally 2022): wood or steel framing with brick/fiber-cement cladding (75), aluminum windows (130), R-30 polyiso roof (26; Colorado banned HFC XPS from 2021), slab edge at about 5k.
Totals: 32k + 28k + 28k + 5k = 94k, which is 43.5 per m2 of floor.
Range: the low case (430 m2 of wall at 55/110/22) gives 27.0. The high case (1,000 m2 of wall at 100/150/45) gives 80.7. A = 53.9.
Calibration: K = 1.46, so CALIBRATED = 78.7.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 78.7 + 0.5 x 86 = 82.4. Range 65.9 - 98.8.

BOTTOM_UP_kgCO2e_per_m2: 53.9
CALIBRATED_kgCO2e_per_m2: 78.7
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 65.9 - 98.8

===== KEY: project-29__run0 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. CFA is 1,740 m2 over about 2 storeys, so the roof is about 870 m2. The perimeter is about 120 m, and at 10 m height the wall area is about 1,200 m2; I used 1,000 m2. At WWR 0.24 that is 240 m2 of glazing and 760 m2 of opaque wall.
Assemblies (public safety, steel/concrete, California 2B, R-35 walls, R-38 roof, Tally 2020): masonry/metal panel on steel stud with heavy insulation (120), aluminum security glazing (140), R-38 polyiso roof (30). HFC XPS is plausible because the 2020 model predates the California ban.
Totals: 91k + 34k + 26k = 151k, which is 86.7 per m2 of floor.
Range: the low case (870 m2 of wall at 90/120/25) gives 61.1. The high case (1,200 m2 of wall at 150/170, HFC-XPS roof at 100) gives 156.8. A = 109.0.
Calibration: K = 1.02, so CALIBRATED = 111.2.

Step B. Public order and safety, 2-5 storeys: B = 160.

Step C. FINAL = 0.5 x 111.2 + 0.5 x 160 = 135.6. Range 108.5 - 162.7.

BOTTOM_UP_kgCO2e_per_m2: 109
CALIBRATED_kgCO2e_per_m2: 111.2
BENCHMARK_kgCO2e_per_m2: 160
RANGE_kgCO2e_per_m2: 108.5 - 162.7

===== KEY: project-38__run0 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 5,910 m2, CFA 3,450 m2, about 3 storeys. Roof 1,150 m2 and slab 1,150 m2, leaving 3,610 m2 of wall. WWR is missing, so I used 0.33 for education, giving 1,191 m2 of glazing and 2,419 m2 of opaque wall.
Assemblies (mass timber school seeking ILFI, Southeast 3A, Tally 2024): wood or steel stud with brick/wood cladding (75), aluminum windows (125), polyiso roof (24), minimal slab insulation (about 3.5k).
Totals: 181k + 149k + 28k + 3.5k = 361k. That is 61 per m2 of envelope, or 104.8 per m2 of floor.
Range: the low case (50/95/20) gives 75.2. The high case (100/150/40) gives 136.9. A = 106.1.
Calibration: K = 1.05, so CALIBRATED = 111.4.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 111.4 + 0.5 x 86 = 98.7. Range 79.0 - 118.4.

BOTTOM_UP_kgCO2e_per_m2: 106.1
CALIBRATED_kgCO2e_per_m2: 111.4
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 79 - 118.4

===== KEY: project-242__run0 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. CFA is 25,500 m2 (GFA 21,850 m2 over about 5 storeys), so the roof is about 4,370 m2. The perimeter is about 265 m, and at 27 m height the wall area is about 7,000 m2. At WWR 0.33 that is 2,310 m2 of glazing and 4,690 m2 of opaque wall.
Assemblies (steel school, Massachusetts 5A, Tally 2019): brick veneer on steel stud (105), aluminum windows/curtain wall (140), R-30 polyiso roof (26), below-grade and under-slab insulation at about 35k. HFC XPS is plausible for a 2019 Tally model, so it goes in the high case.
Totals: 493k + 323k + 114k + 35k = 965k, which is 37.8 per m2 of CFA.
Range: the low case (90/120/22, below-grade 15k) gives 31.8. The high case (135/170, HFC-XPS roof at 100, below-grade 70k) gives 60.1. A = 45.9.
Calibration: K = 1.46, so CALIBRATED = 67.0.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 67.0 + 0.5 x 86 = 76.5. Range 61.2 - 91.8.

BOTTOM_UP_kgCO2e_per_m2: 45.9
CALIBRATED_kgCO2e_per_m2: 67
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 61.2 - 91.8
