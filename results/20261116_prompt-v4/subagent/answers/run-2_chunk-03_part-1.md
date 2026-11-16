===== KEY: project-195__run2 =====
Scope check: lca_phys_scope BSECF includes E, so the enclosure was modelled.

Step A (bottom-up). Floor area = CFA 24,500 m2. Envelope area 14,882 m2; about 13 storeys gives a footprint of about 1,885 m2, so roof 1,885 m2, ground slab 1,885 m2 and walls about 11,112 m2. Glazing = 0.48 x 11,112 = 5,334 m2.
Assemblies: this is a Type I-A steel office of 11-15 storeys in Washington, so a unitized aluminum curtain wall with spandrel/metal panel opaque areas and a low-slope membrane roof over polyiso. HFC-blown XPS is banned in WA from 2021, but Tally data lag behind the market, so it goes in the high case.
- Curtain wall 5,334 x 180 = 960 t
- Opaque spandrel/panel 5,778 x 100 = 578 t
- Roof polyiso 1,885 x 25 = 47 t
- Slab edge/under-slab insulation 1,885 x 5 = 9 t
Total ≈ 1,594 t, which is 107 kgCO2e/m2 of envelope (consistent with a curtain-wall facade) and 65 kgCO2e/m2 of floor.
Low case (stick curtain wall 135, opaque 80): about 1,225 t, or 50. High case (unitized 210, spandrel 130, HFC XPS roof 190): about 2,244 t, or 92. Range 50-92, so A = 71.

Step B (benchmark). Office median = 79.

Step C. FINAL = 0.5 x 71 + 0.5 x 79 = 75. Range 60-90.

BOTTOM_UP_kgCO2e_per_m2: 71
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 60 - 90

===== KEY: project-235__run2 =====
Scope check: BSE includes E.

Step A. Floor area = CFA 13,600 m2. No envelope area is given. Assume 4 storeys, so the footprint is 3,400 m2: roof 3,400 m2 and ground slab 3,400 m2. Walls: between the envelope ratio (1.1 x 13,600 less roof and slab gives 8,160) and 0.45 x floor area (6,120), so use about 7,000 m2. WWR is missing; the laboratory default is 0.32, giving 2,240 m2 of glazing.
Assemblies: a Type II-B steel laboratory in Zone 5A, so steel stud with brick or metal panel, aluminum windows or curtain wall, and a membrane roof over polyiso of about R-30. One Click LCA 2021 in the Eastern region could carry HFC XPS for the roof and below grade.
- Glazing 2,240 x 140 = 314 t
- Opaque 4,760 x 100 = 476 t
- Roof 3,400 x 28 = 95 t
- Slab/below-grade insulation 3,400 x 5 = 17 t
Total ≈ 902 t, about 66 kgCO2e/m2 of floor; the per-envelope value (~65 kgCO2e/m2) is plausible.
Low case (lighter cladding): about 52. High case (HFC XPS roof at about 100 adds about 245 t, plus brick at 120): about 1,290 t, or 95. Range 52-95, so A = 73.5.

Step B. Laboratory median = 95.

Step C. FINAL = 0.5 x 73.5 + 0.5 x 95 = 84.25. Range 67.4-101.1.

BOTTOM_UP_kgCO2e_per_m2: 73.5
BENCHMARK_kgCO2e_per_m2: 95
RANGE_kgCO2e_per_m2: 67.4 - 101.1

===== KEY: project-126__run2 =====
Scope check: BSECF includes E.

Step A. Major renovation; there is no CFA, so floor area = renovated GFA 220 m2. The envelope is 850 m2 for this one-storey building: roof 220 m2, slab 220 m2 and walls about 410 m2. Glazing = 0.21 x 410 = 86 m2.
Assemblies: a Type V-B wood light-frame building in WA Zone 4C, so wood stud with siding, vinyl or aluminum windows and a membrane roof over polyiso.
- Windows 86 x 100 = 8.6 t
- Opaque wood stud/siding 324 x 35 = 11.3 t
- Roof 220 x 25 = 5.5 t
- Slab insulation 220 x 4 = 0.9 t
If the whole envelope is new, the total is about 26 t, or 120 kgCO2e/m2 of floor; the envelope-to-floor ratio of 3.9 inflates the per-floor value. Mass_total is 527 kg/m2, which points to moderate new material, so part of the envelope may have been kept. Range: about half the envelope renewed (about 60) up to a full re-envelope with heavier windows or cladding (about 130), so A = 95. The envelope check is about 31 kgCO2e/m2, typical of a wood-frame building with low glazing.

Step B. Office median = 79.

Step C. FINAL = 0.5 x 95 + 0.5 x 79 = 87. Range 69.6-104.4.

BOTTOM_UP_kgCO2e_per_m2: 95
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 69.6 - 104.4

===== KEY: project-38__run2 =====
Scope check: BSECF includes E.

Step A. Floor area = CFA 3,450 m2. Envelope 5,910 m2 (ratio 1.71, which suggests about 2 storeys). Footprint about 1,725 m2: roof 1,725 m2, slab 1,725 m2 and walls about 2,460 m2. WWR is missing; the education default is 0.32, giving 787 m2 of glazing.
Assemblies: a mass-timber school in Zone 3A, so brick veneer over stud backup (typical for schools), aluminum windows and a low-slope membrane roof over polyiso.
- Windows 787 x 120 = 94 t
- Opaque brick veneer/stud 1,673 x 90 = 151 t
- Roof 1,725 x 25 = 43 t
- Slab edge insulation 1,725 x 3 = 5 t
Total ≈ 293 t, which is 85 kgCO2e/m2 of floor and about 50 kgCO2e/m2 of envelope (reasonable given the large roof and slab share).
Low case (wood stud with lighter siding): about 68. High case (heavier brick and an HFC XPS roof in the Tally dataset): about 110. A = 89.

Step B. Education median = 91.

Step C. FINAL = 0.5 x 89 + 0.5 x 91 = 90. Range 72-108.

BOTTOM_UP_kgCO2e_per_m2: 89
BENCHMARK_kgCO2e_per_m2: 91
RANGE_kgCO2e_per_m2: 72 - 108

===== KEY: project-204__run2 =====
Scope check: BSECF includes E.

Step A. Floor area = CFA 125,000 m2 (this includes 40,750 m2 of below-grade parking). Envelope 45,969 m2. With about 18 storeys the footprint is about 4,680 m2: roof 4,680 m2, slab 4,680 m2 and walls about 36,600 m2. Glazing = 0.53 x 36,600 = 19,400 m2.
Assemblies: a high-rise Type I-A healthcare/office tower in Seattle, so unitized aluminum curtain wall with spandrel and metal panel, and a membrane roof over polyiso. HFC XPS stays possible in the Tally data and goes in the high case.
- Curtain wall 19,400 x 180 = 3,492 t
- Opaque 17,200 x 100 = 1,720 t
- Roof 4,680 x 25 = 117 t
- Slab insulation 4,680 x 5 = 23 t
Total ≈ 5,352 t, which is 116 kgCO2e/m2 of envelope (plausible for a mostly curtain-wall facade) and 43 kgCO2e/m2 of CFA; the large parking area dilutes the per-floor value.
Low case (CW 150, opaque 80): 35. High case (CW 210, opaque 130, HFC XPS roof 190): 58. A = 46.5.

Step B. Healthcare median = 79.

Step C. FINAL = 0.5 x 46.5 + 0.5 x 79 = 62.75. Range 50.2-75.3.

BOTTOM_UP_kgCO2e_per_m2: 46.5
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 50.2 - 75.3

===== KEY: project-173__run2 =====
Scope check: BSECF includes E.

Step A. Major renovation with an addition. There is no CFA, so floor area = 2,350 + 3,900 = 6,250 m2. The envelope of 12,982 m2 (ratio 2.1 for 6-10 storeys) is much larger than the work area, which suggests it describes the whole building while the LCA counts only the new work. Mass_total of 758 kg/m2 also points to an addition plus a lighter renovation.
New envelope: the addition at about 3,500 m2 (walls plus new roof) and partial re-cladding and new windows on the existing building at about 2,000 m2, so about 5,500 m2 in total. WWR is 0.57, so this is a glazing-heavy BC mass-timber office: aluminum curtain wall or window wall, metal panel or fiber cement over stud with mineral wool, and a polyiso roof. HFC XPS is unlikely in BC after 2021.
Blended intensity about 110 kgCO2e/m2 of envelope: 5,500 x 110 = 605 t, or 97 kgCO2e/m2 of floor.
Low case (addition only, 3,500 x 95): 53. High case (most of the envelope re-clad): about 140. Midpoint A = 97.

Step B. Office median = 79.

Step C. FINAL = 0.5 x 97 + 0.5 x 79 = 88. Range 70.4-105.6.

BOTTOM_UP_kgCO2e_per_m2: 97
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 70.4 - 105.6

===== KEY: project-43__run2 =====
Scope check: lca_phys_scope is CF (interior construction and finishes only). It does not contain E, so the enclosure was not modelled and only incidental items are booked under it. Steps A-C are skipped as instructed.

BOTTOM_UP_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-285__run2 =====
Scope check: BSE includes E.

Step A. Major renovation with an addition. Floor area = 2,550 + 1,380 = 3,930 m2. The envelope of 2,694 m2 most likely covers the new addition. For about 2 storeys the addition's footprint is about 1,275 m2: roof 1,275 m2 and walls about 1,420 m2 (the slab is probably not counted). WWR is missing; for a worship or assembly-type building use 0.2, giving 284 m2 of glazing.
Assemblies: steel frame in Pennsylvania Zone 6B, so brick veneer on steel stud, aluminum windows and a thick polyiso roof. One Click LCA 2023 in PA could still use HFC XPS.
- Windows 284 x 130 = 37 t
- Opaque 1,136 x 105 = 119 t
- Roof 1,275 x 30 = 38 t
- Slab/foundation insulation about 6 t
- New windows or roofing on the renovated area, about 20 t
Total ≈ 220 t, or 56 kgCO2e/m2 of floor; about 82 kgCO2e/m2 of envelope, consistent with the reference values.
Low case: 42. High case (HFC XPS roof at about 190, brick on CMU): about 95. A = 68.5.

Step B. Religious Worship falls under "any other use", so the median is 85.

Step C. FINAL = 0.5 x 68.5 + 0.5 x 85 = 76.75. Range 61.4-92.1.

BOTTOM_UP_kgCO2e_per_m2: 68.5
BENCHMARK_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 61.4 - 92.1

===== KEY: project-18__run2 =====
Scope check: BSECF includes E.

Step A. Floor area = CFA 19,900 m2. Envelope 17,271 m2. Assuming about 4 storeys, the footprint is 4,975 m2: roof 4,975 m2, slab 4,975 m2 and walls 7,321 m2. Glazing = 0.16 x 7,321 = 1,171 m2.
Assemblies: a Texas Zone 2A hospital with masonry shear walls, so brick veneer over CMU or steel stud (typical for healthcare), R-13 walls, aluminum windows/storefront and an R-30 membrane roof.
- Glazing 1,171 x 135 = 158 t
- Opaque brick (CMU/stud mix) 6,150 x 130 = 800 t
- Roof polyiso R-30 4,975 x 25 = 124 t
- Slab insulation about 10 t
Total ≈ 1,092 t, which is 55 kgCO2e/m2 of floor and 63 kgCO2e/m2 of envelope (fine for masonry with low glazing).
Low case (brick on steel stud 100): 44. High case (brick on CMU 165, roof as HFC XPS at product stage 100): about 90. A = 67.

Step B. Healthcare median = 79.

Step C. FINAL = 0.5 x 67 + 0.5 x 79 = 73. Range 58.4-87.6.

BOTTOM_UP_kgCO2e_per_m2: 67
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 58.4 - 87.6

===== KEY: project-175__run2 =====
Scope check: BSECF includes E.

Step A. Floor area = CFA 16,800 m2. Envelope 16,927 m2. Assuming about 7 storeys, the footprint is 2,400 m2: roof 2,400 m2, slab 2,400 m2 and walls about 12,127 m2. Glazing = 0.356 x 12,127 = 4,317 m2.
Assemblies: a Portland wood-frame multifamily building over a concrete podium, with R-26 walls (likely exterior insulation) and an R-40 roof. Wood stud with fiber cement or panel rainscreen, vinyl windows in the residential floors with aluminum storefront at grade, and a polyiso roof.
- Glazing 4,317 x 80 (blended vinyl/storefront) = 345 t
- Opaque 7,810 x 50 = 391 t
- Roof R-40 polyiso 2,400 x 35 = 84 t
- Slab insulation about 7 t
Total ≈ 827 t, which is 49 kgCO2e/m2 of floor and 49 kgCO2e/m2 of envelope (acceptable for wood frame with vinyl windows).
Low case: 38. High case (aluminum windows at 120, some brick or metal panel, HFC XPS roof in Tally): about 75. A = 56.5.

Step B. Multifamily median = 54.

Step C. FINAL = 0.5 x 56.5 + 0.5 x 54 = 55.25. Range 44.2-66.3.

BOTTOM_UP_kgCO2e_per_m2: 56.5
BENCHMARK_kgCO2e_per_m2: 54
RANGE_kgCO2e_per_m2: 44.2 - 66.3
