===== KEY: project-255__run2 =====
1. Areas: The envelope area is given as 1,039 m2 and floor area is 1,040 m2, a ratio of 1.0. A single storey implies about 1,040 m2 of roof, so the given figure likely counts only part of the roof, or omits it in part. I use the given envelope (about 600 m2 of roof and 440 m2 of wall) as the base and test the full-roof case.
- At WWR 0.33 the walls are about 145 m2 of glazing and 295 m2 of opaque wall.
- A physical estimate is about 650 m2 of wall (perimeter about 130 m x 5 m).
2. Assemblies: This is a Type V-B wood-frame school in zone 5B (Colorado). The walls (R-12.5) are likely 2x6 wood stud with batt insulation, OSB, a WRB, fiber cement or metal siding, and gypsum. The windows are likely aluminum storefront or fiberglass. The roof (R-30) is likely about 5 in of polyiso with a membrane. One Click LCA may instead model the roof as HFC XPS with blowing-agent emissions included.
3. Intensities:
- Glazing: 145 x 120 = 17 t
- Opaque walls: 295 x 45 = 13 t
- Roof: 600 x 28 = 17 t (full 1,040 m2 roof: 29 t; HFC XPS at 100: about 104 t)
4. Check: The base total is about 47 t, or about 45 kgCO2e/m2 of envelope. That is a little low, so I lift the central estimate slightly.
5. Total:
- Base: 47 t / 1,040 = 45 kgCO2e/m2
- Full roof area: about 57
- HFC XPS roof: about 130
RANGE_kgCO2e_per_m2: 40 - 120

===== KEY: project-141__run2 =====
1. Areas: This is a parking-only structure of 9,550 m2, with 2 levels below grade and 1 at or near grade, and above-grade GFA of 0. It has essentially no conditioned envelope. The candidate enclosure items are:
- Waterproofing and possibly insulation on the roof or plaza deck over the garage, about 4,800 m2 (footprint about 9,550 / 2)
- Small above-grade walls or screens, about 300-500 m2
- Doors and louvres
Below-grade concrete walls are foundation or structure, not enclosure.
2. Assemblies: The deck is likely a hot-applied or sheet waterproofing membrane, maybe with protection board and some XPS where it sits under occupied plaza or landscape. The above-grade elements are likely concrete or metal screen walls. One Click LCA may model any XPS as HFC XPS.
3. Intensities:
- Deck membrane and protection: 4,800 x 10-15 = 48-72 t (with 2-3 in of HFC XPS, about 30 per m2 product stage: 144 t)
- Above-grade screens and walls: about 400 x 60 = 24 t
- Doors: about 5 t
4. Check: The total is about 80-170 t, or about 15-30 kgCO2e/m2 of covered area. That is low, as expected for an unconditioned garage.
5. Total: 80-170 t / 9,550 = about 8-18 kgCO2e/m2. If the deck waterproofing is classified elsewhere, the result could be as low as about 3.
RANGE_kgCO2e_per_m2: 3 - 20

===== KEY: project-282__run2 =====
1. Areas: No envelope area is given. Floor area is 3,600 m2 added plus 6,050 m2 renovated, so 9,650 m2, over about 3 storeys and about 12 m tall.
- Addition: footprint about 1,200 m2 (roof 1,200 m2); walls about 140 m x 12 m = 1,700 m2; assuming WWR 0.40, that is about 680 m2 of glazing and 1,020 m2 of opaque wall.
- Existing building: roof about 2,000 m2 and walls about 2,500 m2.
The ratio for new envelope work is about 0.3-0.8.
2. Assemblies: This is a steel office in zone 6A (Midwest).
- Addition: aluminum curtain wall or windows, plus metal panel or brick on steel stud with about 3 in of mineral wool or polyiso continuous insulation.
- Roof: about R-30 to R-35, likely 6 in of polyiso, or XPS. One Click LCA may book HFC XPS with blowing-agent emissions.
- Renovation: likely re-roofing and partial window replacement.
3. Intensities:
- Addition glazing: 680 x 140 = 95 t
- Addition opaque walls: 1,020 x 95 = 97 t
- Addition roof: 1,200 x 30 = 36 t
- Renovation re-roof: 2,000 x 30 = 60 t
- Renovation window replacement: about 800 m2 x 120 = 96 t
4. Check: The addition alone comes to about 80 kgCO2e/m2 of its envelope. That is consistent with metal panel and glazing.
6. Renovation: Mass is about 760 kg/m2, which shows substantial new material, so I include partial new envelope work on the existing building.
5. Total: 384 t / 9,650 = about 40 kgCO2e/m2.
- Low case (addition only): about 20-24
- High case (HFC XPS on 3,200 m2 of roof at about 150): about 80
RANGE_kgCO2e_per_m2: 20 - 80

===== KEY: project-46__run2 =====
1. Areas: No envelope area is given. Floor area is 35,750 m2 over about 13 storeys, so the footprint is about 2,650 m2 (perimeter about 206 m). The height is about 55 m, so the walls are about 11,300 m2. Assuming a typical office WWR of 0.50 gives about 5,650 m2 of glazing and 5,650 m2 of opaque wall. With 2,650 m2 of roof the envelope is about 14,000 m2, a ratio of 0.39.
2. Assemblies: This is a PT concrete office in California (zone 3B). The glazing is likely aluminum unitized or stick curtain wall, or window wall. The opaque walls are likely metal panel, precast or spandrel over steel stud with mineral wool continuous insulation; some areas may be exposed concrete shear wall with furring. The roof is likely polyiso under a membrane, with HFC XPS as the alternative.
3. Intensities:
- Curtain wall: 5,650 x 150 = 850 t
- Opaque walls: 5,650 x 95 = 537 t
- Roof: 2,650 x 28 = 74 t (HFC XPS at 100 gives 265 t)
4. Check: The total is about 1,460 t, or about 104 kgCO2e/m2 of envelope. That is consistent.
5. Total: 1,460 t / 35,750 = about 41 kgCO2e/m2. The reported 15% embodied-carbon reduction is mostly in the structure.
- Low case (lower WWR, stick system): about 30
- High case (unitized system and HFC roof): about 58
RANGE_kgCO2e_per_m2: 30 - 58

===== KEY: project-269__run2 =====
1. Areas: The envelope area is given as 596 m2 and floor area is 680 m2, a ratio of 0.88. That is below what a single storey implies (680 m2 of roof plus about 550 m2 of wall, about 1,230 m2), so the given figure probably counts only part of the envelope. I use it as the base and test the physical case.
- Given envelope: about 300 m2 of roof and 296 m2 of wall; at WWR 0.21 that is about 62 m2 of glazing and 234 m2 of opaque wall.
- Physical case: about 680 m2 of roof, about 115 m2 of glazing and about 435 m2 of opaque wall.
2. Assemblies: This is a steel-framed office and lab in zone 5B (Oregon). The walls are R-28, which is high: likely steel stud with about 4 in of mineral wool or polyiso continuous insulation and metal panel or fiber cement. The windows are likely aluminum or fiberglass. The roof is R-38, which is about 6.5 in of polyiso, with HFC XPS as the alternative.
3. Intensities:
- Windows: 62 x 120 = 7.5 t (physical case: 14 t)
- Opaque walls: 234 x 95 = 22 t (physical case: 41 t)
- Roof: 300 x 32 = 10 t (physical case: 22 t; HFC XPS at about 130: 88 t)
4. Check: The total is about 40-77 t, or about 63-67 kgCO2e/m2 of envelope. That is consistent.
5. Total:
- Given-envelope basis: about 40 t / 680 = 58 kgCO2e/m2
- Physical basis: about 113
- Physical basis with an HFC roof: about 210
The project reports embodied-carbon reductions, which argues against the HFC case.
RANGE_kgCO2e_per_m2: 50 - 150

===== KEY: project-288__run2 =====
1. Areas: No envelope area is given. This is a single-storey transit facility of 1,110 m2, so the roof is about 1,110 m2. The walls are about 140 m x 6 m = 840 m2. Assuming WWR 0.35 gives about 295 m2 of glazing and 545 m2 of opaque wall. Slab-edge or perimeter insulation adds about 170 m2. The envelope is about 2,100 m2, a ratio of 1.9.
2. Assemblies: The climate is very cold (zone 7), so the enclosure is thickly insulated.
- Walls: likely insulated metal panel or steel or wood framing with about R-25 to R-30 (4-5 in of continuous insulation).
- Roof: about R-49 over the wood joist deck, likely 8-9 in of polyiso or XPS.
- Glazing: thermally broken aluminum storefront with triple glazing.
One Click LCA may model the roof and perimeter insulation as HFC XPS.
3. Intensities:
- Glazing: 295 x 150 = 44 t
- Opaque walls: 545 x 95 = 52 t (legacy HFC IMP at 4-6 in, about 190-270 per m2: 104-150 t)
- Roof: 1,110 x 40 = 44 t (HFC XPS at R-49, product stage only, about 170 per m2: 189 t)
- Perimeter insulation: about 3 t (HFC: about 10 t)
4. Check: The base total is about 143 t, or about 68 kgCO2e/m2 of envelope. That is consistent.
5. Total: 143 t / 1,110 = about 129 kgCO2e/m2.
- Low case (leaner walls and polyiso): about 100
- High case (HFC roof and legacy IMP): about 290
I cap the high end slightly below that extreme.
RANGE_kgCO2e_per_m2: 100 - 260

===== KEY: project-25__run2 =====
1. Areas: This is a minor renovation of a 6,650 m2 school in zone 2B (hot and dry), over about 3-4 storeys and about 18 m tall. The roof is about 1,900 m2 and the walls about 180 m x 18 m = 3,240 m2. Assuming WWR 0.25 gives about 810 m2 of glazing and 2,430 m2 of opaque wall.
2. Assemblies: The scope is "ECF", which includes enclosure, so some new envelope work is likely. The existing structure is concrete frame. The plausible new work is:
- Replacement windows, likely aluminum
- A new roof membrane with about R-25 polyiso
- Possibly an EIFS or insulation overclad on parts of the walls
Mass is about 232 kg/m2, which points mostly to finishes, with modest envelope work.
3. Intensities:
- Window replacement: 810 x 130 = 105 t
- Re-roof: 1,900 x 25 = 48 t (HFC XPS: about 190 t)
- EIFS overclad: 2,430 x 50 = 120 t
4. Check: If every element is replaced, the work comes to about 50 kgCO2e/m2 of envelope. That is reasonable for re-glazing and overclad.
6. Renovation: For a minor renovation, partial replacement is most likely.
5. Total:
- Minimal case (partial windows or roof only): about 5-10 kgCO2e/m2
- Windows plus roof: about 23
- Including overclad: about 41
RANGE_kgCO2e_per_m2: 5 - 35

===== KEY: project-143__run2 =====
1. Areas: No envelope area is given. Floor area is 22,500 m2 over about 8 storeys, so the footprint is about 2,800 m2 (perimeter about 212 m). The height is about 38 m, so the walls are about 8,050 m2. Assuming WWR 0.40 gives about 3,220 m2 of glazing and 4,830 m2 of opaque wall. With 2,800 m2 of roof and some below-grade insulation, the envelope is about 11,000 m2, a ratio of 0.49.
2. Assemblies: This is a PT concrete public assembly building in zone 4C (Oregon). The glazing is likely aluminum curtain wall or storefront. The opaque walls are likely metal panel or fiber cement rainscreen on steel stud with mineral wool continuous insulation. The roof is likely about R-30 polyiso, though One Click LCA may model it as HFC XPS.
3. Intensities:
- Glazing: 3,220 x 145 = 467 t
- Opaque walls: 4,830 x 90 = 435 t
- Roof: 2,800 x 28 = 78 t (HFC XPS at 100: 280 t)
- Below-grade insulation: about 15 t
4. Check: The total is about 995 t, or about 90 kgCO2e/m2 of envelope. That is consistent.
5. Total: 995 t / 22,500 = about 44 kgCO2e/m2. However, the reported mass is only about 135 kg/m2, which suggests an incomplete take-off, and the project reports a 30% embodied-carbon reduction. I therefore widen the range downward.
RANGE_kgCO2e_per_m2: 20 - 60
