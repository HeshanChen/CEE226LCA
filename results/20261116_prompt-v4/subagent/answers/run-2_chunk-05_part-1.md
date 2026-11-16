===== KEY: project-70__run2 =====
Scope check: lca_phys_scope BSE includes E, so the enclosure was modelled.

Step A. Areas: the envelope is 13,471 m2 for a CFA of 4,600 m2, a ratio of 2.9. This is high for a building of about 3 storeys. Roof is about 1,533 m2 and the ground slab about 1,533 m2, which leaves about 10,400 m2 of wall. WWR is missing, so I use 0.3 for healthcare: about 3,120 m2 of glazing and 7,280 m2 of opaque wall.
Assemblies: this is a Type II-B healthcare building in CA zone 3C. I assume steel stud with stucco or veneer at 85, aluminum windows at 130 and a polyiso membrane roof at 25. HFC XPS is unlikely because California banned it in 2021 and the LCA was done with One Click LCA in 2023.
Totals: walls 7,280 x 85 = 619k; glazing 3,120 x 130 = 406k; roof 1,533 x 25 = 38k. That gives about 1,063k kgCO2e, or about 79 per m2 of envelope, which is consistent with the reference values. Per floor area this is about 231 kgCO2e/m2, with a range of 190-270.
A = 231.

Step B. Healthcare benchmark = 79.

Step C. FINAL = 0.5 x 231 + 0.5 x 79 = 155. Range = 124 - 186.

BOTTOM_UP_kgCO2e_per_m2: 231
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 124 - 186

===== KEY: project-197__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 33,393 m2 and the CFA is 69,000 m2. With about 13 storeys over 54,700 m2 of GFA, the footprint is about 4,200 m2. That gives a roof of about 4,200 m2, a slab of about 4,200 m2 and about 25,000 m2 of wall. At WWR 0.4 that is 10,000 m2 of glazing and 15,000 m2 of opaque wall.
Assemblies: this is an 11-15 storey Type I-A healthcare tower in WA zone 4C. I assume unitized or stick curtain wall at 150 per m2, with spandrel or metal-panel opaque wall at 95. The roof is polyiso or XPS, at 40 per m2, which allows some legacy XPS in the Tally data.
Totals: glazing 1,500k; opaque 1,425k; roof 168k. That gives about 3,093k kgCO2e, or about 93 per m2 of envelope, which is reasonable for a curtain-wall-heavy facade. Per CFA this is about 45, with a range of 38-55.
A = 46.

Step B. Healthcare benchmark = 79.

Step C. FINAL = 0.5 x 46 + 0.5 x 79 = 62.5. Range = 50 - 75.

BOTTOM_UP_kgCO2e_per_m2: 46
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 50 - 75

===== KEY: project-192__run2 =====
Scope check: BSECF includes E.

Step A. Areas: no envelope area is given. The building has about 7 storeys (wood over a concrete podium) and a CFA of 57,500 m2, so the footprint is about 8,200 m2. I take wall area as 0.4 x CFA, which is about 23,000 m2. At WWR 0.19 that gives about 4,440 m2 of glazing and 18,560 m2 of opaque wall.
Assemblies: this is Type III-A multifamily in WA zone 4C, with R-25 walls and an R-38 roof. I assume wood stud with fiber cement or panel cladding and exterior continuous insulation at 50, vinyl windows at 70, and a polyiso roof at about 35 for the R-38 thickness.
Totals: walls 928k; windows 311k; roof 287k. That gives about 1,526k kgCO2e, or about 49 per m2 of envelope, which is plausible for wood-frame construction with low glazing. Per CFA this is about 27. Allowing for aluminum windows or an XPS roof, the range is 22-36.
A = 29.

Step B. Residential: Multifamily benchmark = 54.

Step C. FINAL = 0.5 x 29 + 0.5 x 54 = 41.5. Range = 33 - 50.

BOTTOM_UP_kgCO2e_per_m2: 29
BENCHMARK_kgCO2e_per_m2: 54
RANGE_kgCO2e_per_m2: 33 - 50

===== KEY: project-113__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 21,448 m2 and the CFA is 35,000 m2. With about 13 storeys, the footprint is about 2,460 m2. That gives a roof of about 2,460 m2, a slab of about 2,460 m2 and about 16,500 m2 of wall. At WWR 0.33 that is about 5,450 m2 of glazing and 11,050 m2 of opaque wall.
Assemblies: this is a Type I-A laboratory tower in Pennsylvania zone 4A. I assume curtain wall glazing at 160 and metal panel or precast opaque wall at 100. For the roof I use 60 per m2 because HFC XPS is plausible: the state has no ban and the LCA was done in Tally in 2023.
Totals: glazing 872k; opaque 1,105k; roof 148k. That gives about 2,125k kgCO2e, or about 99 per m2 of envelope. Per CFA this is about 61, with a range of 50-75.
A = 62.

Step B. Laboratory benchmark = 95.

Step C. FINAL = 0.5 x 62 + 0.5 x 95 = 78.5. Range = 63 - 94.

BOTTOM_UP_kgCO2e_per_m2: 62
BENCHMARK_kgCO2e_per_m2: 95
RANGE_kgCO2e_per_m2: 63 - 94

===== KEY: project-150__run2 =====
Scope check: BSECF includes E.

Step A. This is a minor renovation of 1,940 m2 with a 2,026 m2 envelope and WWR 0.36. The mass is about 205 kg per m2 of floor, which is low and points to mostly interior work with only limited new envelope.
Areas: if the full envelope were replaced, there would be about 1,300 m2 of wall (470 m2 of it glazing) and about 650 m2 of roof.
Assemblies: I assume partial new aluminum storefront, about 200 m2 at 150 = 30k; partial re-roofing with polyiso, about 600 m2 at 25 = 15k; and some patching of the steel-stud wall, about 10k. That gives about 55k kgCO2e, or about 28 per m2 of floor.
The range runs from 15 (minimal envelope work) to 45 (larger storefront and wall replacement).
A = 30.

Step B. Mercantile counts as "any other use", so the benchmark = 85.

Step C. FINAL = 0.5 x 30 + 0.5 x 85 = 57.5. Range = 46 - 69.

BOTTOM_UP_kgCO2e_per_m2: 30
BENCHMARK_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 46 - 69

===== KEY: project-187__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 3,089 m2 and the CFA is 1,610 m2. With about 3 storeys, the roof is about 540 m2 and the slab about 540 m2, which leaves about 2,010 m2 of wall. At WWR 0.32 that is 643 m2 of glazing and 1,367 m2 of opaque wall.
Assemblies: this is a Type V-B mass-timber school in WA zone 4C, with R-24 walls and an R-55 roof. I assume wood or stud framing with fiber cement or metal panel and exterior insulation at 60, aluminum or fiberglass windows at 120, and a thick polyiso roof at 40 for R-55. Under-slab insulation adds about 5k.
Totals: walls 82k; glazing 77k; roof 22k; slab 5k. That gives about 186k kgCO2e, or 60 per m2 of envelope. Per CFA this is about 116, with a range of 95-140.
A = 117.

Step B. Education benchmark = 91.

Step C. FINAL = 0.5 x 117 + 0.5 x 91 = 104. Range = 83 - 125.

BOTTOM_UP_kgCO2e_per_m2: 117
BENCHMARK_kgCO2e_per_m2: 91
RANGE_kgCO2e_per_m2: 83 - 125

===== KEY: project-154__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 3,724 m2 and the CFA is 2,050 m2. With about 2 storeys, the roof is about 1,025 m2 and the slab about 1,025 m2, which leaves about 1,674 m2 of wall. WWR is missing, so I use 0.18 for public safety: about 300 m2 of glazing and 1,374 m2 of opaque wall.
Assemblies: this is a steel-framed public safety building in WA, with R-22 walls and an R-40 roof. I assume steel stud with brick or metal panel at 100, aluminum windows at 130, a polyiso roof at 32 and slab-edge insulation of about 5k.
Totals: walls 137k; glazing 39k; roof 33k; slab 5k. That gives about 214k kgCO2e, or 57 per m2 of envelope. Per CFA this is about 104, with a range of 85-125.
A = 105.

Step B. Public Order and Safety benchmark = 161.

Step C. FINAL = 0.5 x 105 + 0.5 x 161 = 133. Range = 106 - 160.

BOTTOM_UP_kgCO2e_per_m2: 105
BENCHMARK_kgCO2e_per_m2: 161
RANGE_kgCO2e_per_m2: 106 - 160

===== KEY: project-273__run2 =====
Scope check: BSE includes E.

Step A. Areas: no envelope area is given. The CFA is 5,200 m2 over about 2 storeys, so the roof is about 2,600 m2. I take wall area as about 0.3 x CFA, which is 1,560 m2. WWR is missing, so I use 0.33 for education: about 515 m2 of glazing and 1,045 m2 of opaque wall.
Assemblies: this is a Type II-B steel school in Colorado zone 5B. I assume steel stud with brick veneer at 105, aluminum windows at 125 and a polyiso roof at 25. Colorado banned HFC XPS in 2021 and the LCA was done with One Click LCA in 2023, so XPS is unlikely.
Totals: walls 110k; glazing 64k; roof 65k. That gives about 239k kgCO2e, or about 46 per m2 of floor. The range is 38-58.
A = 48.

Step B. Education benchmark = 91.

Step C. FINAL = 0.5 x 48 + 0.5 x 91 = 69.5. Range = 56 - 83.

BOTTOM_UP_kgCO2e_per_m2: 48
BENCHMARK_kgCO2e_per_m2: 91
RANGE_kgCO2e_per_m2: 56 - 83

===== KEY: project-49__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 10,418 m2 and the CFA is 23,250 m2. With about 5 storeys, the roof is about 4,650 m2, which leaves about 5,770 m2 of wall (the slab appears to be largely excluded). At WWR 0.25 that is 1,440 m2 of glazing and 4,330 m2 of opaque wall.
Assemblies: this is a Type I-A steel healthcare building in CA zone 3B, with R-30 walls and roof. I assume steel stud with stucco, veneer or panel at 90, aluminum windows at 130 and a polyiso roof at 25.
Totals: walls 390k; glazing 187k; roof 116k. That gives about 693k kgCO2e, or about 67 per m2 of envelope. Per CFA this is about 30. The range is 25-38, which covers heavier veneer.
A = 31.

Step B. Healthcare benchmark = 79.

Step C. FINAL = 0.5 x 31 + 0.5 x 79 = 55. Range = 44 - 66.

BOTTOM_UP_kgCO2e_per_m2: 31
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 44 - 66

===== KEY: project-287__run2 =====
Scope check: BSECF includes E.

Step A. Areas: the envelope is 16,685 m2 and the CFA is 5,000 m2, a ratio of 3.3. With about 3 storeys, the roof is about 1,670 m2 and the slab about 1,670 m2, which leaves about 13,350 m2 of wall. At WWR 0.08 that is 1,070 m2 of glazing and 12,280 m2 of opaque wall.
Assemblies: this is a steel food-service building in very cold zone 7. I assume steel stud with metal panel or insulated metal panel at 80, aluminum windows at 130, a polyiso roof at 35 and under-slab insulation of about 25k. HFC XPS is possible: the state is unspecified and the LCA was done in Tally in 2023.
Totals: walls 982k; glazing 139k; roof 58k; slab 25k. That gives about 1,204k kgCO2e, or 72 per m2 of envelope. Per CFA this is about 241. The range is 200-290, which includes the XPS case.
A = 245.

Step B. Food Service counts as "any other use", so the benchmark = 85.

Step C. FINAL = 0.5 x 245 + 0.5 x 85 = 165. Range = 132 - 198.

BOTTOM_UP_kgCO2e_per_m2: 245
BENCHMARK_kgCO2e_per_m2: 85
RANGE_kgCO2e_per_m2: 132 - 198
