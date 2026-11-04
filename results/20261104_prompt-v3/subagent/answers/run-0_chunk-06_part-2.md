===== KEY: project-34__run0 =====
1. Areas. No envelope area is given. Assuming 8 storeys on 32,250 m2, the footprint is about 4,030 m2 (about 63.5 m square, perimeter about 254 m). At a height of about 38 m the wall area is about 9,650 m2. At WWR 0.525, glazing is about 5,070 m2 and opaque wall about 4,580 m2. The roof is about 4,030 m2, and the two below-grade levels add about 2,000 m2 of insulated wall. Total envelope is about 15,700 m2, a ratio of about 0.49.
2. Assemblies. This is a Zone 3A university building with a concrete frame. I assume aluminum curtain wall and windows, with opaque areas of brick or precast on steel stud backup. The roof is a membrane over about R-25 polyiso; One Click LCA may model it as HFC XPS.
3. Intensities.
- Glazing about 150 gives 760 t.
- Opaque walls about 110 give 504 t.
- Roof with polyiso (25) gives 101 t; with HFC XPS at product stage (95) it gives 383 t; with blowing agent booked (370) it gives 1,490 t.
- Below-grade insulation about 15 gives 30 t.
4. Check. The base case is 1,395 t / 15,700 m2, about 89 kgCO2e/m2 of envelope, which is consistent.
5. Total.
- Base case: 1,395 t / 32,250 m2, about 43 kgCO2e/m2.
- Low case (glazing at 120, opaque at 80): about 33.
- XPS roof at product stage: about 52.
- High case (unitized glazing at 190, brick on CMU at 140, XPS with blowing-agent emissions): about 95.
RANGE_kgCO2e_per_m2: 33 - 90

===== KEY: project-24__run0 =====
1. Areas. The envelope area is 21,963 m2 against 16,000 m2 of floor, a ratio of about 1.37. Assuming 3 storeys, the roof is about 5,300 m2. Above-grade walls are about 8,000 m2 (a long, articulated plan about 18 m tall), and the remainder (about 8,600 m2) is basement wall and slab, mostly uninsulated in Texas. At WWR 0.30, glazing is about 2,400 m2 and opaque wall about 5,600 m2.
2. Assemblies. This is a Zone 2A school (R-13 walls, R-25 roof). Walls are likely brick veneer on steel stud or CMU with batt and thin continuous insulation. Glazing is aluminum windows and storefront. The roof is a membrane over about 4 in of polyiso; because this is a Tally model, HFC XPS is possible.
3. Intensities.
- Opaque walls about 110 give 616 t.
- Glazing about 130 gives 312 t.
- Roof with polyiso (25) gives 133 t; with HFC XPS at product stage (95) it gives 504 t; with blowing agent booked (370) it gives 1,960 t.
- Below-grade insulation is minimal, about 10 t.
4. Check. The base case is 1,070 t / 21,963 m2, about 49 kgCO2e/m2 of envelope. That is low only because uninsulated slab and basement area is included; over the walls and roof alone it is about 80.
5. Total.
- Base case: 1,070 t / 16,000 m2, about 67 kgCO2e/m2.
- Low case: about 55.
- Brick on CMU with an XPS roof at product stage: about 106.
- XPS with blowing agent booked: about 200.
RANGE_kgCO2e_per_m2: 55 - 160

===== KEY: project-184__run0 =====
1. Areas. The envelope area is 7,380 m2 against 9,400 m2 of floor, a ratio of about 0.79. Assuming 7 storeys, the roof is about 1,270 m2 and the walls about 6,100 m2. At WWR 0.244, glazing is about 1,490 m2: about 200 m2 of retail storefront and about 1,290 m2 of residential windows. Opaque wall is about 4,610 m2.
2. Assemblies. This is Seattle multifamily, wood frame over a concrete podium, with R-21 walls (2x6 batts plus some exterior insulation) and fiber cement or metal panel siding. Windows are vinyl and the ground floor has aluminum storefront. The roof is R-45, about 8 in of tapered polyiso with a membrane; I also carry an HFC XPS case.
3. Intensities.
- Opaque walls about 50 give 230 t.
- Vinyl windows about 70 give 90 t.
- Storefront about 145 gives 29 t.
- Roof with polyiso (about 35) gives 44 t; with HFC XPS at product stage (RSI 7.9 x 18 + 10, about 152) it gives 193 t; with blowing agent booked (about 650) it gives 825 t.
4. Check. The base case is 393 t / 7,380 m2, about 53 kgCO2e/m2 of envelope. That is reasonable for wood-frame residential.
5. Total.
- Base case: 393 t / 9,400 m2, about 42 kgCO2e/m2.
- Low case (wood siding at 35): about 34.
- High case (metal panel at 80, aluminum windows, XPS at product stage): about 77.
- XPS with blowing agent booked: about 145.
RANGE_kgCO2e_per_m2: 33 - 110

===== KEY: project-199__run0 =====
1. Areas. This is a minor renovation of 20,500 m2 of lab and office space; the envelope area is 24,469 m2 (ratio about 1.2). At WWR 0.43 on about 18,000 m2 of wall, glazing is about 7,700 m2 and opaque wall about 10,300 m2. The roof is about 6,000 m2.
2. Assemblies. If the whole envelope were new, it would be aluminum curtain wall (about 150) plus metal panel or concrete wall (about 90) and a polyiso roof (about 25). That is about 1,160 + 930 + 150 = 2,240 t, or about 109 kgCO2e/m2. However, the project is a minor renovation with a 76% reduction claim, which points to reuse of the existing shell. The mass_total of 8,100 t (about 395 kg/m2) is low for a lab and fits interior and MEP-focused work with some structural infill.
3. Intensities. The likely new envelope work is selective window or curtain-wall replacement (perhaps 5-20% of the glazing, 380-1,540 m2 at about 150, so 60-230 t). Re-roofing at about 25 (polyiso) or about 95 (HFC XPS) over 0-6,000 m2 adds 0-570 t. New exterior doors and louvers add about 10-20 t.
4. Check. The new work is about 100-700 t, or 5-30% of a full new envelope.
5. Total. Dividing by 20,500 m2 gives about 5-35 kgCO2e/m2. The value would be lower if the envelope is untouched.
RANGE_kgCO2e_per_m2: 5 - 35

===== KEY: project-84__run0 =====
1. Areas. The envelope area is 9,832 m2 against 12,400 m2 of floor, a ratio of about 0.79. Assuming 8 storeys, the roof is about 1,550 m2 and the walls about 8,280 m2. At WWR 0.61, glazing is about 5,050 m2 and opaque wall about 3,230 m2.
2. Assemblies. This is Bay Area multifamily, wood frame over a concrete podium, with R-15 walls and an R-36 roof. The very high WWR suggests aluminum window wall or storefront on part of the facade plus vinyl or fiberglass windows elsewhere. Opaque walls are wood stud with fiber cement, stucco or metal panel. The roof is a membrane over about 6 in of polyiso; Tally may use HFC XPS.
3. Intensities.
- Glazing, assuming half aluminum window wall (175) and half vinyl (70), averages about 122, giving 616 t.
- Opaque walls about 55 give 178 t.
- Roof with polyiso (30) gives 47 t; with HFC XPS at product stage (about 125) it gives 194 t; with blowing agent booked (about 500) it gives about 775 t.
4. Check. The base case is 841 t / 9,832 m2, about 86 kgCO2e/m2 of envelope. That is consistent with a facade dominated by glazing.
5. Total.
- Base case: 841 t / 12,400 m2, about 68 kgCO2e/m2.
- Low case (mostly vinyl, averaging 80): about 48.
- High case (all aluminum at 175, opaque at 80, XPS at product stage): about 108.
- XPS with blowing agent booked: about 140.
RANGE_kgCO2e_per_m2: 48 - 120

===== KEY: project-18__run0 =====
1. Areas. The envelope area is 17,271 m2 against 19,900 m2 of floor, a ratio of about 0.87. Assuming 4 storeys, the roof is about 5,000 m2. Walls are about 10,000 m2, and the remainder (about 2,300 m2) is slab edge or ground. At WWR 0.16, glazing is about 1,600 m2 and opaque wall about 8,400 m2.
2. Assemblies. This is a Texas hospital with masonry shear walls, so the exterior walls are likely brick veneer on CMU or steel stud with R-13 batt and continuous insulation. Glazing is aluminum windows and storefront. The roof is a membrane over about 5 in of polyiso (R-30); because this is a Tally model, HFC XPS is possible.
3. Intensities.
- Opaque walls average about 120 (between brick on CMU at 150 and brick on steel stud at 105), giving 1,008 t.
- Glazing about 130 gives 208 t.
- Roof with polyiso (25) gives 125 t; with HFC XPS at product stage (95) it gives 475 t; with blowing agent booked (370) it gives 1,850 t.
4. Check. The base case is 1,341 t / 17,271 m2, about 78 kgCO2e/m2 of envelope, which is consistent for masonry walls.
5. Total.
- Base case: 1,341 t / 19,900 m2, about 67 kgCO2e/m2.
- Low case (walls at 95): about 54.
- High case (brick on CMU at 155, XPS at product stage): about 101.
- XPS with blowing agent booked: about 170.
RANGE_kgCO2e_per_m2: 55 - 150

===== KEY: project-186__run0 =====
1. Areas. No envelope area is given. Assuming 3 storeys on 9,300 m2, the footprint is about 3,100 m2 (about 70 x 44 m, perimeter about 230 m). At a height of about 16 m the wall area is about 3,680 m2. At WWR 0.269, glazing is about 990 m2 and opaque wall about 2,690 m2. Below-grade wall is about 920 m2. Total envelope is about 7,700 m2, a ratio of about 0.83.
2. Assemblies. This is a Seattle-area school with a steel frame, R-25 walls and an R-40 roof. Walls are likely steel stud with about 3-4 in of continuous mineral wool and a metal panel or brick rainscreen. Glazing is thermally broken aluminum curtain wall and windows. The roof is a membrane over about 7 in of polyiso; Tally may use HFC XPS. Below-grade insulation is XPS at about R-10.
3. Intensities.
- Opaque walls about 100 give 269 t.
- Glazing about 145 gives 144 t.
- Roof with polyiso (about 33) gives 102 t; with HFC XPS at product stage (about 136) it gives 422 t; with blowing agent booked (about 560) it gives 1,740 t.
- Below-grade insulation gives 15-29 t.
4. Check. The base case is 530 t / 7,700 m2, about 69 kgCO2e/m2 of envelope, which is consistent.
5. Total.
- Base case: 530 t / 9,300 m2, about 57 kgCO2e/m2.
- Low case: about 46.
- HFC XPS at product stage: about 93.
- Blowing agent booked: about 240.
I give the HFC XPS case moderate weight.
RANGE_kgCO2e_per_m2: 48 - 180

===== KEY: project-281__run0 =====
1. Areas. No envelope area is given. Assuming 4 storeys on 12,900 m2, the footprint is about 3,225 m2 (about 57 m square, perimeter about 227 m). At a height of about 18 m the wall area is about 4,090 m2. No WWR is given; I assume 40% for an office, so about 1,640 m2 of glazing and 2,450 m2 of opaque wall. The roof is about 3,225 m2 and the below-grade wall about 900 m2. Total envelope is about 8,200 m2, a ratio of about 0.64.
2. Assemblies. This is a Zone 6A Midwest office with a steel frame. I assume steel stud with continuous mineral wool or polyiso and a metal panel or brick finish, plus aluminum curtain wall with insulated glass units. The roof is a membrane over about R-30 polyiso; One Click LCA may use HFC XPS. Below-grade XPS is about R-10.
3. Intensities.
- Opaque walls about 95 give 233 t.
- Curtain wall about 140 gives 230 t.
- Roof with polyiso (28) gives 90 t; with HFC XPS at product stage (105) it gives 339 t; with blowing agent booked (380) it gives 1,230 t.
- Below grade gives about 22-40 t.
4. Check. The base case is 575 t / 8,200 m2, about 70 kgCO2e/m2 of envelope, which is consistent.
5. Total.
- Base case: 575 t / 12,900 m2, about 45 kgCO2e/m2.
- Low case: about 38.
- XPS at product stage: about 65.
- Blowing agent booked: about 140.
RANGE_kgCO2e_per_m2: 38 - 120

===== KEY: project-28__run0 =====
1. Areas. No envelope area is given. Assuming 3 storeys on 5,200 m2, the footprint is about 1,730 m2 (about 41.6 m square, perimeter about 166 m). At a height of about 16 m the wall area is about 2,660 m2. I assume a WWR of 25% for an education building in a hot climate, so about 665 m2 of glazing and 2,000 m2 of opaque wall. Total envelope is about 4,400 m2, a ratio of about 0.85.
2. Assemblies. This is a Zone 2B concrete building. The mass_total of about 1,730 kg/m2 suggests heavy concrete, likely including CIP or CMU exterior walls with furred R-13 insulation and stucco or panel cladding. Glazing is aluminum windows and storefront. The roof is a membrane over about 3.5 in of polyiso (R-20); Tally may use HFC XPS.
3. Intensities.
- Concrete or CMU walls about 115 give 230 t.
- Glazing about 135 gives 90 t.
- Roof with polyiso (20) gives 35 t; with HFC XPS at product stage (RSI 3.5 x 18 + 10, about 73) it gives 126 t; with blowing agent booked (about 280) it gives 485 t.
4. Check. The base case is 355 t / 4,400 m2, about 81 kgCO2e/m2 of envelope, which is consistent.
5. Total.
- Base case: 355 t / 5,200 m2, about 68 kgCO2e/m2.
- Low case (lighter walls at 85): about 55.
- High case (heavy concrete at 145, XPS at product stage): about 98.
- Blowing agent booked: about 165.
RANGE_kgCO2e_per_m2: 55 - 150

===== KEY: project-205__run0 =====
1. Areas. This is a minor renovation of 950 m2 of lodging in a 2-5 storey wood-frame building. The existing envelope is roughly 1,200 m2 (roof about 320 m2, walls about 900 m2).
2. Assemblies. The physical scope is SCF, which does not include the enclosure (E) category. The LCA therefore likely did not model any new exterior walls, windows or roofing. The mass_total of 431 t (about 454 kg/m2) is consistent with substructure or structural work and finishes rather than a new shell. If minor envelope items were captured under other categories, they might be a few replaced windows (vinyl, about 70) or patches of R-21 wall and R-49 roof insulation.
3. Intensities. If, say, 30-60 m2 of vinyl windows at 70 and some insulation upgrades at 5-10 per m2 over 300 m2 were included, the result would be about 2-7 t. The full new-envelope equivalent would be about 50 per m2 of envelope, or about 60 t, but that is outside the declared scope.
4. Check. The enclosure total is likely 0-8 t, far below a new envelope, which is consistent with a minor renovation whose scope excludes the enclosure.
5. Total. Dividing 0-8 t by 950 m2 gives about 0-8 kgCO2e/m2.
RANGE_kgCO2e_per_m2: 0 - 8
