===== KEY: project-41__run1 =====
Scope check: lca_phys_scope BSECF includes E, so the enclosure was modelled.

Step A (bottom-up). Floor area (CFA) is 37,250 m2 on one storey, so the roof is about 37,250 m2. The footprint is about 236 x 158 m, giving a perimeter of about 790 m. At about 11 m height, the walls are about 8,700 m2. With the warehouse default WWR of 0.05, glazing is about 435 m2 and opaque wall is about 8,265 m2. The ground slab is uninsulated in climate zone 3A.
Assemblies: tilt-up concrete walls with interior insulation, suggested by the concrete lateral system in Texas, at 95 kgCO2e/m2, giving 785 t. Aluminum storefront and windows at 140 give 61 t. The roof is a low-slope membrane over polyiso (about R-25) on bare metal deck at 24, giving 894 t. HFC XPS is unlikely over metal deck, but thicker or mineral wool insulation is possible.
Total is about 1,740 t, or 38 kgCO2e per m2 of roof plus wall, which is plausible for a warehouse. That is 46.7 kgCO2e/m2 of floor. The range is 38 (lighter walls, thinner roof) to 60 (heavier tilt-up, mineral wool or HFC board roof), so A = 49.

Step B (benchmark). Warehouse and Storage median: 62.

Step C. FINAL = 0.5 x 49 + 0.5 x 62 = 55.5. Range 44.4 - 66.6.

BOTTOM_UP_kgCO2e_per_m2: 49
BENCHMARK_kgCO2e_per_m2: 62
RANGE_kgCO2e_per_m2: 44.4 - 66.6

===== KEY: project-234__run1 =====
Scope check: BSE includes E.

Step A (bottom-up). CFA is 64,500 m2 on about 13 storeys. The envelope ratio of 0.5 gives about 32,250 m2: roof about 4,960 m2, ground slab about 4,960 m2, and walls about 20,000 m2 (a hospital wall-to-floor ratio of about 0.3). WWR is not given, so I assume 0.35 for a high-rise hospital. That gives about 7,000 m2 of glazing and 13,000 m2 of opaque wall.
Assemblies: at this height, unitized or stick curtain wall and window wall at 165 give 1,155 t. Opaque brick, precast and metal panel on steel stud at 110 give 1,430 t. The roof is membrane over polyiso at 25, giving 124 t. Below-grade wall and slab insulation for two basement levels is about 2,000 m2 at 10, giving 20 t.
Base total is about 2,730 t, or 42 kgCO2e/m2 of floor, or about 110 kgCO2e/m2 of wall plus roof, which is consistent.
Higher alternative: climate zone 5A in the Midwest with One Click LCA makes HFC XPS on the roof and below grade plausible (+400 t), along with more curtain wall, for about 3,600 t (56). The low case is about 36. A = 46.

Step B (benchmark). Healthcare median: 79.

Step C. FINAL = 0.5 x 46 + 0.5 x 79 = 62.5. Range 50 - 75.

BOTTOM_UP_kgCO2e_per_m2: 46
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 50 - 75

===== KEY: project-44__run1 =====
Scope check: BSECF includes E.

Step A (bottom-up). This is a minor renovation of a 3,600 m2 wood light-frame multifamily building, about 4 storeys. Mass is about 529 kg/m2, which suggests meaningful but not complete new work. For the full envelope: roof about 900 m2, walls about 1,620 m2 (0.45 x floor area), WWR 0.172, so glazing about 280 m2 and opaque wall about 1,340 m2.
Assemblies: wood stud with R-13 batts and stucco or fiber-cement siding at 40 give 54 t. Vinyl windows (California multifamily) at 65 give 18 t. The R-38 roof (batt or polyiso, membrane or shingles) at 25 gives 22 t.
A full new envelope would be about 94 t, or 26 kgCO2e/m2 of floor, or about 37 per m2 of wall plus roof. That is low because the wood frame and vinyl windows are light.
The renovation likely replaced only part of the envelope: windows, re-roofing and some re-siding. The new-work fraction could range from about 55% to 100%, and aluminum windows are an upper alternative. The bottom-up range is 15 - 33, so A = 24.

Step B (benchmark). Residential: Multifamily median: 54.

Step C. FINAL = 0.5 x 24 + 0.5 x 54 = 39. Range 31.2 - 46.8.

BOTTOM_UP_kgCO2e_per_m2: 24
BENCHMARK_kgCO2e_per_m2: 54
RANGE_kgCO2e_per_m2: 31.2 - 46.8

===== KEY: project-42__run1 =====
Special case check: lca_phys_scope is CF (interior construction and finishes only). It does not contain E, so the enclosure was not modelled and only incidental items would be booked under it. Following the prompt, I skip Steps A to C and report the prescribed values.

The renovation of 4,200 m2 of education space, with a mass of only about 103 kg/m2, is consistent with interior-only work. This supports the conclusion that no exterior walls, glazing or roofing were included in the assessment boundary.

BOTTOM_UP_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-69__run1 =====
Scope check: BSE includes E.

Step A (bottom-up). CFA is 11,100 m2 on about 8 storeys. The envelope ratio of 0.7 gives about 7,770 m2: roof about 1,390 m2, slab about 1,390 m2, walls about 4,990 m2. With the multifamily default WWR of 0.3, glazing is about 1,500 m2 and opaque wall about 3,490 m2.
Assemblies: Type II-B with concrete shear walls and steel framing in climate zone 3C (California) suggests aluminum windows or window wall at about 150, giving 225 t. Opaque walls are steel stud with fiber cement, stucco or metal panel and mineral wool continuous insulation at 75, giving 262 t. The roof is membrane over polyiso at 24, giving 33 t. HFC XPS is unlikely in California in 2023, and the slab is uninsulated in this mild climate.
Total is about 520 t, which is about 81 kgCO2e/m2 of wall plus roof (consistent) and 46.8 kgCO2e/m2 of floor.
Range: the low case is vinyl windows and stucco (38). The high case is window wall at 175 and metal panel or ACM rainscreen at 100 (58). A = 48.

Step B (benchmark). Residential: Multifamily median: 54.

Step C. FINAL = 0.5 x 48 + 0.5 x 54 = 51. Range 40.8 - 61.2.

BOTTOM_UP_kgCO2e_per_m2: 48
BENCHMARK_kgCO2e_per_m2: 54
RANGE_kgCO2e_per_m2: 40.8 - 61.2

===== KEY: project-123__run1 =====
Scope check: BSECF includes E.

Step A (bottom-up). CFA is 4,800 m2 on about 3 storeys. The envelope ratio of 1.1 gives about 5,280 m2: roof about 1,600 m2, slab about 1,600 m2, walls about 2,080 m2. With the education default WWR of 0.33, glazing is about 690 m2 and opaque wall about 1,390 m2.
Assemblies: this is Type III-B mass timber, so the exterior walls are FRT wood or steel stud with fiber cement, metal panel or partial brick, plus mineral wool continuous insulation, at about 75, giving 104 t. Aluminum windows and storefront at 130 give 90 t. The roof is membrane over polyiso (about R-30) at 26, giving 42 t. In climate zone 4C, Washington state, 2023, HFC XPS is banned and unlikely. Under-slab and slab-edge EPS at about RSI 1.8 (4.4 kgCO2e/m2) over 1,600 m2 adds 7 t.
Total is about 243 t, which is about 66 kgCO2e/m2 of wall plus roof (reasonable) and 50.6 per m2 of floor.
Range: 40 (wood siding, lean take-off) to 64 (more brick and curtain wall, mineral wool roof). A = 52.

Step B (benchmark). Education median: 91.

Step C. FINAL = 0.5 x 52 + 0.5 x 91 = 71.5. Range 57.2 - 85.8.

BOTTOM_UP_kgCO2e_per_m2: 52
BENCHMARK_kgCO2e_per_m2: 91
RANGE_kgCO2e_per_m2: 57.2 - 85.8

===== KEY: project-224__run1 =====
Scope check: BSECF includes E.

Step A (bottom-up). CFA is 5,100 m2 on about 3 storeys plus a basement. The thermal envelope is 3,583 m2: roof about 1,500 m2, walls about 2,080 m2, with the below-grade portion small. At WWR 0.35, glazing is about 730 m2 and opaque wall about 1,350 m2.
Assemblies: the public assembly building with a mass timber structure in climate zone 5A, Massachusetts, likely has stick curtain wall and storefront at 140, giving 102 t. Opaque walls are wood or steel stud with brick or metal panel and continuous insulation at about 85, giving 115 t. The 60% reduction effort suggests low-carbon choices. The roof is membrane over polyiso (about R-30) at 26, giving 39 t. Below-grade insulation of about 500 m2 at 10 adds 5 t.
Base total is about 261 t, which is 73 kgCO2e/m2 of envelope (consistent) and 51 per m2 of floor.
Higher alternative: Massachusetts is not an HFC-ban state, and a Tally 2023 model may carry HFC XPS on the roof and below grade (+110 t) along with heavier masonry, for about 75. The low case is about 45. A = 60.

Step B (benchmark). Public Assembly median: 94.

Step C. FINAL = 0.5 x 60 + 0.5 x 94 = 77. Range 61.6 - 92.4.

BOTTOM_UP_kgCO2e_per_m2: 60
BENCHMARK_kgCO2e_per_m2: 94
RANGE_kgCO2e_per_m2: 61.6 - 92.4

===== KEY: project-107__run1 =====
Scope check: BSECF includes E.

Step A (bottom-up). This is a major renovation with 960 m2 added and 90 m2 renovated, so the floor area is 1,050 m2. Mass is about 1,190 kg/m2, indicating essentially new construction. The thermal envelope is 1,449 m2: about 500 m2 of roof and about 900 m2 of wall, with a small slab. At WWR 0.57, glazing is about 513 m2 and opaque wall about 387 m2.
Assemblies: the steel-frame public assembly addition in climate zone 4A, Eastern region, likely has aluminum stick curtain wall and storefront at 140, giving 72 t. Opaque walls are metal panel or brick veneer on steel stud with continuous insulation at 95, giving 37 t. The roof is membrane over polyiso at 26, giving 13 t.
Total is about 122 t, which is 84 kgCO2e/m2 of envelope (consistent with a glass-heavy facade) and 116 per m2 of floor.
Higher alternative: HFC XPS roof in a Tally model (+37 t) or unitized-grade glazing gives about 150. The low case is about 100. A = 125.

Step B (benchmark). Public Assembly median: 94.

Step C. FINAL = 0.5 x 125 + 0.5 x 94 = 109.5. Range 87.6 - 131.4.

BOTTOM_UP_kgCO2e_per_m2: 125
BENCHMARK_kgCO2e_per_m2: 94
RANGE_kgCO2e_per_m2: 87.6 - 131.4

===== KEY: project-43__run1 =====
Special case check: lca_phys_scope is CF (interior construction and finishes only). It does not contain E, so the enclosure was not modelled in this LCA and only incidental items could be booked under the enclosure category. Following the prompt, I skip Steps A to C and report the prescribed values.

Although a thermal envelope area (786 m2) and WWR (0.8) are reported, the minor renovation of 2,500 m2 has a mass of only about 135 kg/m2, which is consistent with interior fit-out only. No new walls, glazing or roofing were assessed.

BOTTOM_UP_kgCO2e_per_m2: 8
BENCHMARK_kgCO2e_per_m2: 8
RANGE_kgCO2e_per_m2: 6 - 10

===== KEY: project-14__run1 =====
Scope check: BSECF includes E.

Step A (bottom-up). This is a single-storey school with 750 m2 of CFA, so the roof is about 750 m2. The footprint is about 37 x 20 m, giving a perimeter of about 115 m. At about 4.5 m height, after parapet allowance, the walls are about 450 m2 net. With the education default WWR of 0.3, glazing is about 135 m2 and opaque wall about 315 m2. The slab is uninsulated in climate zone 1A.
Assemblies: the masonry shear walls mean structural CMU exterior walls, likely grouted, with stucco or paint and little insulation in this very hot humid climate, at about 110 per m2 (counted as the wall), giving 35 t. Aluminum windows and storefront at 120 give 16 t. The roof is a low-slope membrane or metal roof over polyiso (about R-20 to R-25) at about 30, giving 22 t.
Total is about 73 t, which is 97 kgCO2e/m2 of floor and about 60 per m2 of envelope. This is consistent with the high mass of 2,936 kg/m2.
Range: 80 (lighter CMU share, thinner roof) to 120 (fully grouted CMU, metal roof, more glazing). A = 100.

Step B (benchmark). Education median: 91.

Step C. FINAL = 0.5 x 100 + 0.5 x 91 = 95.5. Range 76.4 - 114.6.

BOTTOM_UP_kgCO2e_per_m2: 100
BENCHMARK_kgCO2e_per_m2: 91
RANGE_kgCO2e_per_m2: 76.4 - 114.6
