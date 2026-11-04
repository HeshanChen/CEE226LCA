===== KEY: project-8__run0 =====
1. Areas. CFA 3,850 m2, 2-5 storeys (assume 3), so the footprint is ~1,280 m2 (e.g. 50 x 26 m, perimeter ~152 m). Height ~10 m gives ~1,520 m2 of walls. WWR is not given; I assume ~0.20 for multifamily, so ~300 m2 of windows and ~1,220 m2 of opaque wall. The roof is ~1,280 m2. Envelope ~2,800 m2, ratio ~0.73.
2. Assemblies. Texas Zone 1A, high wind (62 m/s), with a precast concrete vertical system. That suggests precast load-bearing exterior wall panels with thin rigid insulation (polyiso ~25-50 mm) and interior furring/gypsum, or alternatively stucco/fiber cement on studs where the precast is interior. Windows are vinyl double low-e, impact rated. The roof is polyiso ~90 mm (R-20 to R-25) with a TPO membrane over wood joists.
3. Intensities (One Click LCA):
- Precast exterior wall panel (~150-200 mm, plus insulation and gypsum): ~95 kgCO2e/m2 x 1,220 = ~116 t (if precast forms the wall)
- Vinyl windows: ~70 x 300 = ~21 t
- Roof: ~25 x 1,280 = ~32 t
- Doors: ~5 t
4. Total. With precast walls about 174 t / 3,850 = ~45 kgCO2e/m2. With framed walls about 25. Mass_total of 1,300 kg/m2 supports substantial concrete, but part of it is foundations. I weight the two cases to ~35.
BEST_kgCO2e_per_m2: 35
RANGE_kgCO2e_per_m2: 20 - 55

===== KEY: project-179__run0 =====
1. Areas. Thermal envelope 6,024 m2 for 3,700 m2 CFA, ratio 1.63. Assuming 3 storeys above grade plus 1 below, the roof is ~1,230 m2, slab/basement floor ~1,230 m2 (partly insulated) and walls (above and below grade) ~3,560 m2. Above-grade walls ~3,000 m2 at WWR 0.36 give ~1,080 m2 of glazing. Opaque wall ~2,480 m2.
2. Assemblies. A Washington Zone 4C steel braced-frame school with high R-values (walls R-26, roof R-40). The wall is likely metal panel or brick veneer on steel studs with ~75-100 mm mineral wool CI plus batts and gypsum. Glazing is aluminum curtain wall/windows with double low-e IGUs. The roof is polyiso ~170 mm with a membrane. Below-grade walls have XPS/waterproofing.
3. Intensities (Tally 2021):
- Aluminum glazing: ~130 kgCO2e/m2 x 1,080 = ~140 t
- Opaque rainscreen wall: ~65 x 2,480 = ~161 t
- Roof: ~38 x 1,230 = ~47 t
- Below-grade/under-slab insulation (partly XPS): ~15 x 1,230 = ~18 t
- Doors: ~5 t
4. Total. About 371 t / 3,700 = ~100 kgCO2e/m2. I shade slightly lower (~90) for the possibility of fiber-cement cladding or a lower glazing frame intensity. The high envelope ratio of a small low-rise school drives the result.
BEST_kgCO2e_per_m2: 90
RANGE_kgCO2e_per_m2: 55 - 140

===== KEY: project-134__run0 =====
1. Areas. Floor area = renovated GFA 7,450 m2. No envelope area is given. For a 3-storey office the envelope would be roughly 2,500 m2 of roof plus ~3,000 m2 of walls, but this matters little here.
2. Scope check. This is a tenant improvement with lca_phys_scope = CF. The assessed scope covers interior construction and finishes (or equivalent non-shell categories) only. Structure and enclosure are excluded. A TI in an existing Portland office typically leaves the base-building curtain wall and roof untouched.
3. Renovation extent. mass_total is only 160.7 t, ~22 kg/m2, typical of interior partitions, ceilings and flooring. Nothing indicates new enclosure material.
4. Intensity and total. At most some incidental items could be classified as enclosure, such as interior gypsum on exterior walls, new entry doors or perimeter insulation furring. Even 300 m2 of perimeter gypsum and insulation at ~6 kgCO2e/m2 is ~2 t, or ~0.3 kgCO2e/m2. The best estimate is essentially zero. The range allows minor perimeter work.
BEST_kgCO2e_per_m2: 0.5
RANGE_kgCO2e_per_m2: 0 - 3

===== KEY: project-70__run0 =====
1. Areas. Thermal envelope 13,471 m2 for 4,600 m2 CFA, ratio 2.9, very envelope-intensive. Assuming 2 storeys gives a ~2,300 m2 roof and a ~2,300 m2 slab on grade, leaving ~8,870 m2 of walls (a spread-out, articulated clinic plan with high floor heights). WWR is not given; I assume ~0.25, so ~2,200 m2 of glazing and ~6,650 m2 of opaque wall.
2. Assemblies. A California Zone 3C healthcare/food service building. The steel bare-deck roof, concrete CIP vertical system and shear walls suggest some exterior walls are concrete. Elsewhere, cement plaster or metal panel on steel studs with batts (R-13 to R-19) and a thin CI, plus gypsum. Glazing is aluminum storefront/windows. The roof is polyiso ~100 mm (R-25) with a membrane on metal deck.
3. Intensities (One Click LCA):
- Aluminum glazing: ~120 kgCO2e/m2 x 2,200 = ~264 t
- Opaque walls (mix of stud and concrete): ~50 x 6,650 = ~333 t
- Roof: ~25 x 2,300 = ~58 t
- Slab-edge insulation, doors: ~15 t
4. Total. About 670 t / 4,600 = ~146 kgCO2e/m2. Given the EC reductions and the possibility that the envelope figure includes interior or less-intensive surfaces, I take ~120. The range reflects uncertainty in glazing share and wall type.
BEST_kgCO2e_per_m2: 120
RANGE_kgCO2e_per_m2: 70 - 190

===== KEY: project-44__run0 =====
1. Areas. Floor area = renovated GFA 3,600 m2. Assuming 3 storeys, the footprint is ~1,200 m2 (perimeter ~150 m). Height ~10 m gives ~1,500 m2 of walls. WWR 0.17 gives ~260 m2 of glazing and ~1,240 m2 of opaque wall. Roof ~1,200 m2. Envelope ~2,700 m2, ratio ~0.75.
2. Assemblies. A California Zone 3B wood light-frame multifamily building with retail. R-13 walls (fiberglass batts in 2x4) and an R-38 roof (blown fiberglass or ~165 mm polyiso). Existing stucco cladding. Replacement windows would be vinyl.
3. Renovation extent. This is a minor renovation, but mass_total of 1,904 t (~529 kg/m2) suggests notable new material, possibly seismic strengthening, new slabs or a new stucco/roof. The R-values indicate upgraded insulation, at least at the roof. I assume new roof insulation and membrane, some window replacement and partial wall re-siding/insulation.
4. Intensities and total:
- Roof insulation and membrane: ~20 kgCO2e/m2 x 1,200 = ~24 t
- Vinyl windows (assume half replaced): ~70 x 130 = ~9 t
- Partial wall work (batts, gypsum, stucco patch on ~40%): ~20 x 500 = ~10 t
Total ~43 t / 3,600 = ~12 kgCO2e/m2. If the full envelope was redone, ~25. If only interior work, near 3.
BEST_kgCO2e_per_m2: 12
RANGE_kgCO2e_per_m2: 3 - 25

===== KEY: project-254__run0 =====
1. Areas. Floor area = renovated 7,300 m2 + added 4,200 m2 = 11,500 m2. Envelope 13,936 m2, ratio 1.21. WWR 0.19. For the addition (assume 2 storeys): ~2,100 m2 of roof and ~2,000 m2 of walls (~380 m2 glazing). The existing part has ~3,650 m2 of roof and ~3,500 m2 of walls.
2. Assemblies. An eastern Washington Zone 5B steel-frame school with food service. The new walls are likely brick or metal panel on steel studs with ~75 mm mineral wool/polyiso CI plus batts and gypsum. Glazing is aluminum storefront/windows with double low-e IGUs. The roof is polyiso ~150-180 mm (R-30 to R-38) with a membrane. Under-slab and perimeter XPS is likely in 5B.
3. Intensities:
- Addition glazing: 130 x 380 = ~49 t
- Addition opaque walls: 65 x 1,620 = ~105 t
- Addition roof: 35 x 2,100 = ~74 t
- Addition slab insulation (XPS edge/partial): 10 x 2,100 = ~21 t
- Existing re-roof (assumed): 25 x 3,650 = ~91 t
- Existing partial window replacement: 110 x 450 = ~50 t
4. Total. About 390 t / 11,500 = ~34 kgCO2e/m2. The 33% EC reduction reflects reuse of the existing envelope, and the moderate mass (358 kg/m2) suggests limited work on the existing building, so I take ~30.
BEST_kgCO2e_per_m2: 30
RANGE_kgCO2e_per_m2: 15 - 50

===== KEY: project-208__run0 =====
1. Areas. Floor area = renovated GFA 7,050 m2. Envelope 7,740 m2, ratio 1.10. WWR 0.13, so glazing is ~0.13 x ~6,000 m2 of walls = ~780 m2. Roof ~1,500 m2.
2. Assemblies. An existing Washington Zone 4C concrete education building (CIP shear walls, so the exterior walls are likely board-formed or clad concrete). Any new enclosure work would be aluminum window replacements, interior insulation furring or a roof recover (polyiso and membrane).
3. Renovation extent. This is a minor renovation with an 80% EC reduction claimed, indicating substantial reuse of the existing building. mass_total is 1,436 t, ~204 kg/m2, which is moderate. It is probably interior slabs/partitions and some structural upgrades. The new enclosure scope is likely limited.
4. Intensities and total:
- Possible partial window replacement (~20% of glazing): 156 m2 x 120 = ~19 t
- Spot roof repair/recover (~25%): 375 m2 x 25 = ~9 t
- Perimeter insulation/gypsum at selected walls: 1,000 m2 x 8 = ~8 t
Total ~36 t / 7,050 = ~5 kgCO2e/m2. I take ~6 to allow some entry storefront work. The range spans essentially nothing up to a full window replacement plus roof (~20).
BEST_kgCO2e_per_m2: 6
RANGE_kgCO2e_per_m2: 1 - 20

===== KEY: project-27__run0 =====
1. Areas. CFA 18,200 m2, all parking (GFA 0): a 6-10 level open parking structure plus 1 basement level. Footprint ~18,200/8 = ~2,300 m2, perimeter ~200 m, height ~20 m, so ~4,000 m2 of facade, largely open. There is no conditioned thermal envelope.
2. Assemblies. A California Zone 2B open concrete PT garage. Enclosure items would be perimeter screening (metal mesh/perforated aluminum or steel panels on part of the facade), stair/elevator tower glazing (aluminum storefront), a top-deck traffic coating or waterproofing membrane, and possibly basement waterproofing. There is no insulation. Concrete spandrel/upturn beams are structural.
3. Intensities (Tally 2020):
- Metal screen on ~30% of facade: ~40 kgCO2e/m2 x 1,200 = ~48 t
- Stair tower glazing: ~120 x 100 = ~12 t
- Top-deck traffic membrane: ~5 x 2,300 = ~12 t
- Doors, misc.: ~3 t
4. Total. About 75 t / 18,200 = ~4 kgCO2e/m2. If there is no screening it is ~1-2. If it has a heavier architectural screen (aluminum fins), up to ~10.
BEST_kgCO2e_per_m2: 4
RANGE_kgCO2e_per_m2: 1 - 10

===== KEY: project-212__run0 =====
1. Areas. Envelope 16,238 m2 for 16,600 m2 CFA, ratio 0.98. Assuming 7 storeys above grade gives a ~2,370 m2 roof. Above-grade walls ~10,000 m2 (31-45 m tall lab with high floor-to-floor). Below-grade walls ~2,500 m2 plus the base slab ~1,370 m2. WWR 0.29 gives ~2,900 m2 of glazing and ~7,100 m2 of opaque wall.
2. Assemblies. A Washington Zone 4C concrete laboratory. The opaque wall is likely precast/metal panel rainscreen or insulated concrete walls with ~75 mm mineral wool CI, steel stud furring and gypsum. Glazing is aluminum curtain wall/windows with double low-e IGUs. The roof is polyiso ~150 mm (R-30) with a membrane and pavers at mechanical areas. Below grade: XPS/waterproofing.
3. Intensities (Tally):
- Curtain wall/windows: ~140 kgCO2e/m2 x 2,900 = ~406 t
- Opaque wall: ~70 x 7,100 = ~497 t
- Roof: ~35 x 2,370 = ~83 t
- Below-grade wall and slab insulation (partly XPS): ~15 x 3,870 = ~58 t
4. Total. About 1,044 t / 16,600 = ~63 kgCO2e/m2. I take ~60. The range covers metal panel versus precast or concrete exterior walls being counted, and the curtain wall framing intensity.
BEST_kgCO2e_per_m2: 60
RANGE_kgCO2e_per_m2: 38 - 95

===== KEY: project-105__run0 =====
1. Areas. Envelope 2,685 m2 for 1,600 m2 CFA, ratio 1.68 (single-storey school). Roof ~1,600 m2 and walls ~1,085 m2; the slab appears not to be counted. WWR 0.388 gives ~421 m2 of glazing and ~664 m2 of opaque wall.
2. Assemblies. A New York Zone 4A single-storey steel school. Walls R-16.7: brick veneer or metal panel on steel studs with ~50 mm polyiso/mineral wool CI plus batts and gypsum. Glazing is aluminum storefront/windows with double low-e IGUs (high wind, 56 m/s). The roof is R-30 polyiso ~130 mm on bare metal deck with a cover board and TPO.
3. Intensities (One Click LCA):
- Aluminum glazing: ~130 kgCO2e/m2 x 421 = ~55 t
- Opaque wall: ~65 x 664 = ~43 t
- Roof: ~28 x 1,600 = ~45 t
- Doors, slab-edge insulation: ~5 t
4. Total. About 148 t / 1,600 = ~92 kgCO2e/m2. The 21.6% EC reduction may have included lower-carbon insulation or cladding, so I take ~85. The range covers lighter metal-panel walls versus brick with XPS.
BEST_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 55 - 130
