===== KEY: project-225__run0 =====
Scope check: lca_phys_scope BSECF includes E, so I ran the full method.

Step A. Areas: envelope 12,133 m2, CFA 25,000 m2, about 8 storeys. Roof is about 3,125 m2 and the ground slab about 3,125 m2, which leaves 5,883 m2 of wall. At WWR 0.4 that is 2,353 m2 of glazing and 3,530 m2 of opaque wall.
Assemblies (healthcare, steel Type I-A, Zone 5A, Tally 2023): brick veneer on steel stud at 105, aluminum windows/curtain wall at 145, polyiso membrane roof at 25, and slab-edge/under-slab insulation at about 10 per m2 of slab.
Totals: walls 371k + glazing 341k + roof 78k + slab 31k = 821k kgCO2e. That is 68 per m2 of envelope, or 32.8 per m2 of floor.
Range: the low case (90/120/20) gives 27.1. The high case (brick on CMU at 135, glazing at 180, HFC-XPS roof at 100) gives 50.9. A = 39.
Calibration: K = 1.35 (healthcare, envelope area given), so CALIBRATED = 52.7.

Step B. Healthcare has no 6-10 storey benchmark, so I used the "other storeys" value: B = 73.

Step C. FINAL = 0.5 x 52.7 + 0.5 x 73 = 62.9. Range 50.3 - 75.4.

BOTTOM_UP_kgCO2e_per_m2: 39
CALIBRATED_kgCO2e_per_m2: 52.7
BENCHMARK_kgCO2e_per_m2: 73
RANGE_kgCO2e_per_m2: 50.3 - 75.4

===== KEY: project-277__run0 =====
Scope check: BSE includes E.

Step A. Areas: envelope 44,594 m2, CFA 18,900 m2, 1 storey. Roof 18,900 m2 and slab 18,900 m2, leaving 6,794 m2 of wall. WWR is missing, so I used 0.05 for a warehouse: 340 m2 of glazing and 6,454 m2 of opaque wall.
Assemblies: concrete shear walls point to tilt-up concrete with interior insulation (100), aluminum storefront (145), and membrane over polyiso on bare metal deck (25). Colorado banned HFC XPS in 2021, so the base case uses low-carbon roof insulation. Perimeter slab insulation is about 10k.
Totals: walls 645k + glazing 49k + roof 473k + slab 10k = 1,177k, which is 62.3 per m2 of floor. The envelope value of 26 per m2 is driven by the roof and slab, which is expected for a warehouse.
Range: the low case (tilt-up 80, roof 20) gives 49.9. The high case (tilt-up 125, roof 40) gives 86.5. A = 68.2.
Calibration: K = 0.88, so CALIBRATED = 60.0.

Step B. Warehouse, 1 storey: B = 65.

Step C. FINAL = 0.5 x 60.0 + 0.5 x 65 = 62.5. Range 50.0 - 75.0.

BOTTOM_UP_kgCO2e_per_m2: 68.2
CALIBRATED_kgCO2e_per_m2: 60
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 50 - 75

===== KEY: project-138__run0 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 15,002 m2. Above-grade GFA is 16,550 m2 over about 7 storeys, so the roof is about 2,364 m2 and the slab over the garage about 2,364 m2. That leaves 10,274 m2 of wall. At WWR 0.34 this is 3,493 m2 of glazing and 6,781 m2 of opaque wall.
Assemblies (wood light-frame on a concrete podium, Oregon 4C, R-26 walls, R-32 roof): wood stud with continuous insulation and fiber-cement siding (45), vinyl windows (65), polyiso roof (25), and podium-deck insulation at about 8 per m2.
Totals: walls 305k + windows 227k + roof 59k + podium 19k = 610k. That is 41 per m2 of envelope, or 29.8 per m2 of CFA (20,500 m2).
Range: the low case (35/50/22) gives 23.1. The high case (mixed brick/metal panel at 70, aluminum windows at 120, roof at 30) gives 48.3. A = 35.7.
Calibration: K = 0.97, so CALIBRATED = 34.6.

Step B. Multifamily, 6-10 storeys: B = 48.

Step C. FINAL = 0.5 x 34.6 + 0.5 x 48 = 41.3. Range 33.0 - 49.6.

BOTTOM_UP_kgCO2e_per_m2: 35.7
CALIBRATED_kgCO2e_per_m2: 34.6
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 33 - 49.6

===== KEY: project-25__run0 =====
Scope check: ECF includes E. This is a minor renovation of 6,650 m2 with mass_total 232 kg/m2, so only part of the envelope is likely new.

Step A. Areas: no envelope area is given. At about 3 storeys the roof is about 2,217 m2. For walls I used about 0.4 x floor = 2,660 m2. With an education WWR of 0.33 that is 878 m2 of glazing and 1,782 m2 of opaque wall.
Assemblies (concrete frame, California 2B, Tally): steel stud with stucco (70), aluminum windows (130), polyiso roof (25).
Full new-envelope equivalent: 125k + 114k + 55k = 294k, which is 44 per m2.
Renovation share: the low mass suggests partial work, such as new windows, re-roofing and some cladding. The low case (about 30% of the full envelope) gives 13. The high case (full re-clad at higher intensities) gives 53. A = 33.
Calibration: K = 1.46 (education, no envelope area), so CALIBRATED = 48.2.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 48.2 + 0.5 x 86 = 67.1. Range 53.7 - 80.5.

BOTTOM_UP_kgCO2e_per_m2: 33
CALIBRATED_kgCO2e_per_m2: 48.2
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 53.7 - 80.5

===== KEY: project-93__run0 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 5,379 m2, CFA 4,650 m2, about 3 storeys. Roof 1,550 m2 and slab 1,550 m2, leaving 2,279 m2 of wall. At WWR 0.68 that is 1,550 m2 of glazing and 729 m2 of opaque wall.
Assemblies (lab, concrete, California 3C, Tally 2019, R-22 roof): aluminum stick curtain wall (135), metal panel/spandrel (90), polyiso roof (23). The under-slab slab is uninsulated in this mild climate.
Totals: glazing 209k + opaque 66k + roof 36k = 311k. That is 58 per m2 of envelope, or 66.8 per m2 of floor.
Range: the low case (120/75/20) gives 58.4. The high case (unitized curtain wall at 180, opaque at 110, HFC-XPS roof at 100, which is plausible for a 2019 Tally model) gives 110.6. A = 84.5.
Calibration: K = 1.81 (laboratory, envelope area given), so CALIBRATED = 152.9.

Step B. Laboratory, 2-5 storeys: B = 77.

Step C. FINAL = 0.5 x 152.9 + 0.5 x 77 = 115.0. Range 92.0 - 138.0.

BOTTOM_UP_kgCO2e_per_m2: 84.5
CALIBRATED_kgCO2e_per_m2: 152.9
BENCHMARK_kgCO2e_per_m2: 77
RANGE_kgCO2e_per_m2: 92 - 138

===== KEY: project-39__run0 =====
Scope check: BSE includes E.

Step A. Areas: envelope 48,623 m2, CFA 19,900 m2, 1 storey. Roof 19,900 m2 and slab 19,900 m2, leaving 8,823 m2 of wall. At WWR 0.02 that is 176 m2 of glazing and 8,647 m2 of opaque wall.
Assemblies: wall R-1.35 means essentially uninsulated tilt-up concrete, which I set at 80 (the low end). Storefront is 145. The roof is R-20 polyiso membrane on bare deck at 20.
Totals: walls 692k + glazing 26k + roof 398k = 1,116k, which is 56.0 per m2 of floor. For a warehouse with almost no glazing this is plausible.
Range: the low case (tilt-up 70, roof 18) gives 49.7. The high case (tilt-up 110, roof 35, for mineral wool or a higher-carbon board) gives 84.1. A = 66.9.
Calibration: K = 0.88, so CALIBRATED = 58.9.

Step B. Warehouse, 1 storey: B = 65.

Step C. FINAL = 0.5 x 58.9 + 0.5 x 65 = 62.0. Range 49.6 - 74.4.

BOTTOM_UP_kgCO2e_per_m2: 66.9
CALIBRATED_kgCO2e_per_m2: 58.9
BENCHMARK_kgCO2e_per_m2: 65
RANGE_kgCO2e_per_m2: 49.6 - 74.4

===== KEY: project-73__run0 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. CFA is 8,400 m2. A height of 15-22.5 m suggests about 4 storeys, so the footprint and roof are about 2,100 m2. The perimeter is about 190 m, and at 18 m height the wall area is about 3,400 m2. At WWR 0.33 that is 1,122 m2 of glazing and 2,278 m2 of opaque wall.
Assemblies (concrete Type I-A school, California 3C, One Click 2023): steel stud with stucco/fiber cement or a light precast mix (75), aluminum windows/storefront (135), polyiso roof (25).
Totals: 171k + 152k + 53k = 375k, which is 44.6 per m2 of floor.
Range: the low case (55/115/22) gives 35.8. The high case (concrete/precast walls at 110, glazing at 160, roof at 35) gives 60.0. A = 47.9.
Calibration: K = 1.46, so CALIBRATED = 69.9.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 69.9 + 0.5 x 86 = 78.0. Range 62.4 - 93.6.

BOTTOM_UP_kgCO2e_per_m2: 47.9
CALIBRATED_kgCO2e_per_m2: 69.9
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 62.4 - 93.6

===== KEY: project-101__run0 =====
Special case. lca_phys_scope is CF, which does not include E, so the enclosure was not modelled and only incidental items are booked under it. I skipped Steps A to C and reported the fixed values.

BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-271__run0 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. CFA is 1,860 m2, 1 storey, under 7.5 m tall. Roof is 1,860 m2. The perimeter is about 173 m, and at 6 m height the wall area is about 1,040 m2. WWR is missing; I assumed 0.35 for a transit building, giving 364 m2 of glazing and 676 m2 of opaque wall.
Assemblies (steel, Colorado 5B, One Click 2023): metal panel on steel stud (90), aluminum storefront (148), R-30 polyiso roof (26), slab-edge insulation at about 9k.
Totals: 61k + 54k + 48k + 9k = 172k, which is 92.7 per m2 of floor.
Range: the low case (75/140/22) gives 79.2. The high case (110/180, roof at 45 to cover tool-lag XPS, slab at 28k) gives 135.2. A = 107.2.
Calibration: K = 1.44 (transportation hub, no envelope area), so CALIBRATED = 154.4.

Step B. Transportation hub, 1 storey, uses the "other storeys" value: B = 157.

Step C. FINAL = 0.5 x 154.4 + 0.5 x 157 = 155.7. Range 124.6 - 186.8.

BOTTOM_UP_kgCO2e_per_m2: 107.2
CALIBRATED_kgCO2e_per_m2: 154.4
BENCHMARK_kgCO2e_per_m2: 157
RANGE_kgCO2e_per_m2: 124.6 - 186.8

===== KEY: project-270__run0 =====
Scope check: BSECF includes E.

Step A. Areas: envelope 3,858 m2, CFA 2,750 m2, about 4 storeys. Roof 688 m2 and slab 688 m2, leaving 2,482 m2 of wall. At WWR 0.19 that is 472 m2 of glazing and 2,010 m2 of opaque wall.
Assemblies (wood light-frame Type V-B, Colorado 5B, R-21 walls, R-49 roof): wood stud with siding or fiber cement (40), vinyl windows (65), thick roof insulation (35), slab insulation at about 3k.
Totals: 80k + 31k + 24k + 3k = 139k. That is 36 per m2 of envelope, or 50.4 per m2 of floor.
Range: the low case (30/50/25) gives 37.3. The high case (partial brick/stucco at 60, fiberglass/aluminum windows at 100, roof at 50) gives 75.5. A = 56.4.
Calibration: K = 0.97, so CALIBRATED = 54.7.

Step B. Multifamily, 2-5 storeys: B = 55.

Step C. FINAL = 0.5 x 54.7 + 0.5 x 55 = 54.9. Range 43.9 - 65.9.

BOTTOM_UP_kgCO2e_per_m2: 56.4
CALIBRATED_kgCO2e_per_m2: 54.7
BENCHMARK_kgCO2e_per_m2: 55
RANGE_kgCO2e_per_m2: 43.9 - 65.9
