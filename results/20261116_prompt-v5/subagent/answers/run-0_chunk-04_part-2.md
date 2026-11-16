===== KEY: project-145__run0 =====
Scope check: BSE includes E.

Step A. CFA is 21,250 m2 of multifamily in BC, with no envelope area. I assume 6 storeys (15-22.5 m), so the footprint is 3,540 m2 of roof. Wall area is between the geometric 4,940 m2 (perimeter 260 m x 19 m) and the 0.4/m2 floor guide (8,500 m2); I take 6,500 m2. At WWR 0.30, glazing is 1,950 m2 and opaque wall 4,550 m2.
Assemblies: a concrete residential building in 4C. Steel stud with fiber cement/metal panel and mineral wool ci at 75. Aluminum window wall/vinyl windows, blended at 130. Roof is low-GWP XPS (HFC banned in Canada from 2021) or polyiso at 28.
Totals: walls 341,300 + glazing 253,500 + roof 99,100 = 693,900 kgCO2e, or 70 per m2 of envelope (OK). Per floor area that is 33. The range is 25-42, so A = 33.
K = 1.60 (no envelope area), so CALIBRATED = 53.

Step B. Multifamily, 6-10 storeys: B = 48.

Step C. FINAL = 0.5 x 53 + 0.5 x 48 = 50.5, range 40 - 61.
BOTTOM_UP_kgCO2e_per_m2: 33
CALIBRATED_kgCO2e_per_m2: 53
BENCHMARK_kgCO2e_per_m2: 48
RANGE_kgCO2e_per_m2: 40 - 61

===== KEY: project-109__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 6,100 m2, a single tall storey (15-22.5 m). bldg_therm_env_area is 14,083 m2. I take the roof as 6,100 m2 and the walls as about 6,000 m2 (perimeter about 320 m x 18 m), with about 1,980 m2 of insulated slab/perimeter. At WWR 0.13, glazing is 780 m2 and opaque wall 5,220 m2.
Assemblies: a public-assembly building in NY 4A on a long-span steel frame, walls R-28, roof R-30. Steel stud/metal panel or IMP, with some masonry, at 85. Aluminum storefront/curtain wall at 145. Polyiso roof at 25 (NY banned HFC XPS in 2021, but Tally data may carry it). Slab insulation at 5.
Totals: walls 443,700 + glazing 113,100 + roof 152,500 + slab 9,900 = 719,200 kgCO2e, or 51 per m2 of envelope (OK). Per floor area that is 118. The range is 100-140 (HFC XPS roof at the high end), so A = 118.
K = 1.37, so CALIBRATED = 162.

Step B. Public Assembly, 1 storey: B = 108.

Step C. FINAL = 0.5 x 162 + 0.5 x 108 = 135, range 108 - 162.
BOTTOM_UP_kgCO2e_per_m2: 118
CALIBRATED_kgCO2e_per_m2: 162
BENCHMARK_kgCO2e_per_m2: 108
RANGE_kgCO2e_per_m2: 108 - 162

===== KEY: project-42__run0 =====
Special case. lca_phys_scope is CF (interior construction and finishes only). It does not contain E, so the enclosure was not modelled and only incidental items are booked under it. Per the instructions, Steps A to C are skipped and the fixed values are reported. This is a minor renovation of 4,200 m2 of education space in California, assessed in Tally in 2020. Its mass is about 103 kg/m2, consistent with interior fit-out only, which supports the conclusion that no new exterior walls, glazing or roofing were included in the model.
BOTTOM_UP_kgCO2e_per_m2: 8
CALIBRATED_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-245__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 24,000 m2 (20,750 residential + 3,250 below-grade parking), with 21+ storeys (61-90 m). bldg_therm_env_area is 33,763 m2, a high ratio of 1.4 that probably includes the podium and complex massing. I take the roof (tower plus podium) as about 2,000 m2, the slab/below-grade as 1,500 m2 and the walls as about 30,260 m2. At WWR 0.47, glazing is 14,220 m2 and opaque wall 16,040 m2.
Assemblies: a Canadian concrete high-rise in 5A. Aluminum window wall at 175. Spandrel/steel stud with metal panel at 90. Roof is low-GWP XPS/polyiso at 35 (HFC banned in Canada).
Totals: walls 1,443,500 + glazing 2,489,200 + roof 70,000 + slab 7,500 = 4,010,200 kgCO2e, or 119 per m2 of envelope. Per CFA that is 167. With punched aluminum/vinyl windows at about 120 instead, the result is about 134. The envelope area looks high, so I moderate: the range is 130-180 and A = 155.
K = 0.97, so CALIBRATED = 150.

Step B. Multifamily, 11+ storeys: B = 71.

Step C. FINAL = 0.5 x 150 + 0.5 x 71 = 110.5, range 88 - 133.
BOTTOM_UP_kgCO2e_per_m2: 155
CALIBRATED_kgCO2e_per_m2: 150
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 88 - 133

===== KEY: project-264__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 9,600 m2. bldg_therm_env_area is 8,165 m2. I assume 3 tall storeys (15-22.5 m), so the roof is 3,200 m2 and the slab 3,200 m2, leaving 1,765 m2 of wall. At WWR 0.34, glazing is 600 m2 and opaque wall 1,165 m2.
Assemblies: a mass-timber public-assembly building in Oregon 5B, walls R-19, roof R-36. Metal panel/masonry on stud with ci at 85. Aluminum curtain wall at 140. Polyiso membrane roof at R-36 at 30. Slab insulation at 5.
Totals: walls 99,000 + glazing 84,000 + roof 96,000 + slab 16,000 = 295,000 kgCO2e, or only 36 per m2 of envelope, because the roof dominates. Revisiting: a mineral wool roof (45) or HFC XPS (Oregon has no ban; Tally 2023 data) at about 100 raise it. Per floor area the base is 31 and the high case about 50. The range is 28-50, so A = 39.
K = 1.37, so CALIBRATED = 53.

Step B. Public Assembly, 2-5 storeys: B = 97.

Step C. FINAL = 0.5 x 53 + 0.5 x 97 = 75, range 60 - 90.
BOTTOM_UP_kgCO2e_per_m2: 39
CALIBRATED_kgCO2e_per_m2: 53
BENCHMARK_kgCO2e_per_m2: 97
RANGE_kgCO2e_per_m2: 60 - 90

===== KEY: project-157__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 680 m2. bldg_therm_env_area is 1,932 m2, a very high ratio of 2.8 for a small, tall building. I assume 3 storeys (15-22.5 m), so the roof is 227 m2 and the slab 227 m2, leaving 1,478 m2 of wall. At WWR 0.20, glazing is 296 m2 and opaque wall 1,182 m2.
Assemblies: a WA 4C public-safety building with concrete shear walls, walls R-22, roof R-38. Concrete/brick on CMU mixed with metal panel, blended at 120. Aluminum (security) windows at 135. Polyiso roof at 30. Slab insulation at 5.
Totals: walls 141,800 + glazing 40,000 + roof 6,800 + slab 1,100 = 189,700 kgCO2e, or 98 per m2 of envelope (masonry-heavy, consistent). Per floor area that is 279, high because of the envelope-to-floor ratio. The range is 220-330, so A = 275.
K = 1.07, so CALIBRATED = 294.

Step B. Public Order and Safety, 2-5 storeys: B = 160.

Step C. FINAL = 0.5 x 294 + 0.5 x 160 = 227, range 182 - 272.
BOTTOM_UP_kgCO2e_per_m2: 275
CALIBRATED_kgCO2e_per_m2: 294
BENCHMARK_kgCO2e_per_m2: 160
RANGE_kgCO2e_per_m2: 182 - 272

===== KEY: project-243__run0 =====
Scope check: BSE includes E.

Step A. CFA is 16,200 m2, with no envelope area. I assume 4 storeys (15-22.5 m), so the footprint is 4,050 m2 of roof. Perimeter is about 270 m and height 18 m, giving 4,860 m2 of wall. At WWR 0.33, glazing is 1,604 m2 and opaque wall 3,256 m2.
Assemblies: a Massachusetts 5A steel school. Brick veneer on steel stud with ci at 105. Aluminum windows at 130. Polyiso membrane roof at 25. Under-slab insulation at 3. Because this is Tally 2020 and MA has no HFC ban, HFC XPS at the roof (about 100) is plausible.
Totals: walls 341,900 + glazing 208,500 + roof 101,300 + slab 12,200 = 663,900 kgCO2e, or 51 per m2 of envelope (OK). Per floor area that is 41. With HFC XPS the result is about 59. The range is 35-58, so A = 47.
K = 1.46, so CALIBRATED = 69.

Step B. Education, 2-5 storeys: B = 86.

Step C. FINAL = 0.5 x 69 + 0.5 x 86 = 77.5, range 62 - 93.
BOTTOM_UP_kgCO2e_per_m2: 47
CALIBRATED_kgCO2e_per_m2: 69
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 62 - 93

===== KEY: project-106__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 1,950 m2 over 1 tall storey above grade (15-22.5 m) and 2 storeys below, with no envelope area. Footprint and roof are about 700 m2. Perimeter is about 110 m and height 16 m, giving 1,760 m2 of above-grade wall, plus about 770 m2 of insulated below-grade wall. At WWR 0.18, glazing is 317 m2 and opaque wall 1,443 m2.
Assemblies: a mass-timber ILFI project in PA 4A, which avoids red-list materials and so uses no HFC foam. Wood stud with wood/fiber cement or stone cladding at 60. Fiberglass/aluminum windows at 120. Mineral wool/polyiso roof at 35. Below-grade EPS/mineral wool at 6.
Totals: walls 86,600 + glazing 38,000 + roof 24,500 + below-grade 4,600 = 153,700 kgCO2e, or 51 per m2 of envelope (OK). Per floor area that is 79. The range is 62-95, so A = 79.
K = 1.29 (no envelope area), so CALIBRATED = 102.

Step B. Public Assembly, 1 storey: B = 108.

Step C. FINAL = 0.5 x 102 + 0.5 x 108 = 105, range 84 - 126.
BOTTOM_UP_kgCO2e_per_m2: 79
CALIBRATED_kgCO2e_per_m2: 102
BENCHMARK_kgCO2e_per_m2: 108
RANGE_kgCO2e_per_m2: 84 - 126

===== KEY: project-55__run0 =====
Scope check: BSEC includes E.

Step A. CFA is 37,500 m2, with no envelope area. I assume 3 storeys (7.6-15 m), so the footprint is 12,500 m2 of roof. Wall area is between the geometric 6,240 m2 and the 0.3 x floor guide (11,250 m2); I take 9,000 m2. At WWR 0.45 (large office), glazing is 4,050 m2 and opaque wall 4,950 m2.
Assemblies: a California 3B steel/concrete office. Aluminum stick curtain wall at 135. Opaque metal panel/precast on steel stud at 95. Polyiso roof at 25 (Tally 2019 may carry HFC XPS).
Totals: walls 470,300 + glazing 546,800 + roof 312,500 = 1,329,500 kgCO2e, or 62 per m2 of envelope (OK). Per floor area that is 35.5. The range is 30-48 (HFC XPS roof or a unitized system at the high end), so A = 39.
K = 1.49, so CALIBRATED = 58.

Step B. Office, 2-5 storeys: B = 82.

Step C. FINAL = 0.5 x 58 + 0.5 x 82 = 70, range 56 - 84.
BOTTOM_UP_kgCO2e_per_m2: 39
CALIBRATED_kgCO2e_per_m2: 58
BENCHMARK_kgCO2e_per_m2: 82
RANGE_kgCO2e_per_m2: 56 - 84

===== KEY: project-191__run0 =====
Scope check: BSECF includes E.

Step A. CFA is 13,800 m2 (11,350 residential + 2,450 below-grade parking), with no envelope area. I assume 5 storeys (podium plus 4 wood), so the footprint is 2,270 m2 of roof. Perimeter is about 212 m and height 17 m, giving 3,600 m2 of wall. At WWR 0.18, glazing is 648 m2 and opaque wall 2,952 m2.
Assemblies: a WA 4C wood-frame building over a concrete podium, walls R-21, roof R-38. Wood stud with fiber cement and a little ci at 45. Vinyl windows with some aluminum storefront at the podium, blended at 75. Polyiso roof (R-38) at 30.
Totals: walls 132,800 + glazing 48,600 + roof 68,100 = 249,500 kgCO2e, or 44 per m2 of envelope, typical for wood/vinyl. Per CFA that is 18. The range is 15-26 (brick accents or aluminum windows at the high end), so A = 20.
K = 1.60, so CALIBRATED = 32.

Step B. Multifamily, 2-5 storeys: B = 55.

Step C. FINAL = 0.5 x 32 + 0.5 x 55 = 43.5, range 35 - 52.
BOTTOM_UP_kgCO2e_per_m2: 20
CALIBRATED_kgCO2e_per_m2: 32
BENCHMARK_kgCO2e_per_m2: 55
RANGE_kgCO2e_per_m2: 35 - 52
