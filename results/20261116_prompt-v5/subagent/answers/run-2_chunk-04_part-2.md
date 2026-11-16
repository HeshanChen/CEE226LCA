===== KEY: project-217__run2 =====
Scope check: BSECF includes E. Floor area = CFA 7,950 m2.

Step A. A1 Areas: envelope area 8,416 m2. Assuming 4 storeys, the roof is about 1,988 m2 and the ground slab about 1,988 m2, leaving about 4,440 m2 of wall. WWR 0.22 gives 977 m2 of glazing and 3,463 m2 of opaque wall.
A2 Assemblies: steel-framed school in Massachusetts (5A), mostly brick veneer on steel stud. Windows are aluminum or curtain wall. The roof is a membrane over R-30 polyiso, with under-slab rigid insulation. Massachusetts has no HFC XPS ban and the model is Tally, so HFC XPS is the high case.
A3 Intensities: brick on stud 105 -> 363,600; glazing 135 -> 131,900; roof 26 -> 51,700; under-slab 6 -> 11,900. Total about 559,100 kg.
A4 Check: about 66 per m2 of envelope, which is consistent.
A5: 559,100 kg / 7,950 = 70.3. With HFC XPS on the roof and slab it is about 93. Range 62-90; A = 76.
A7: K = 1.05 (Education, envelope area given), so CALIBRATED = 79.8.

Step B. Education, 2 to 5 storeys: 86.

Step C. FINAL = 0.5 x 79.8 + 0.5 x 86 = 82.9; range 66.3-99.5.

BOTTOM_UP_kgCO2e_per_m2: 76
CALIBRATED_kgCO2e_per_m2: 79.8
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 66.3 - 99.5

===== KEY: project-19__run2 =====
Scope check: BSECF includes E. Floor area = CFA 1,910 m2.

Step A. A1 Areas: envelope area 4,285 m2, which is a ratio of 2.24 (typical for 1 storey). Split: roof about 1,950 m2 (including overhangs), walls about 1,350 m2, and slab about 985 m2, mostly uninsulated in zone 2A. WWR 0.08 gives 108 m2 of glazing and 1,242 m2 of opaque wall.
A2 Assemblies: one-storey mass-timber school in Texas, likely brick or stone veneer on stud backup. Glazing is aluminum storefront. The roof is a membrane over polyiso, which is thin in this hot climate.
A3 Intensities: veneer on stud 90 -> 111,800; storefront 145 -> 15,700; roof 24 -> 46,800. Total about 174,300 kg.
A4 Check: about 53 per m2 of wall plus roof, or 41 per m2 of envelope including slab. That is plausible with 8% glazing.
A5: 174,300 kg / 1,910 = 91. Masonry backup or HFC XPS would raise it. Range 78-115; A = 96.
A7: K = 1.05 (Education, envelope area given), so CALIBRATED = 100.8.

Step B. Education, 1 storey: 104.

Step C. FINAL = 0.5 x 100.8 + 0.5 x 104 = 102.4; range 81.9-122.9.

BOTTOM_UP_kgCO2e_per_m2: 96
CALIBRATED_kgCO2e_per_m2: 100.8
BENCHMARK_kgCO2e_per_m2: 104
RANGE_kgCO2e_per_m2: 81.9 - 122.9

===== KEY: project-231__run2 =====
Scope check: BSE includes E. Floor area = CFA 54,500 m2.

Step A. A1 Areas: no envelope area. Assuming 13 storeys and 52,960 m2 of GFA, the footprint and roof are about 4,070 m2. About 80 x 51 m gives a 262 m perimeter; at 75 m height the wall is about 19,650 m2. WWR is missing, so the lab default of 0.35 applies: 6,880 m2 of glazing and 12,770 m2 of opaque wall. Below-grade insulation is about 2,000 m2.
A2 Assemblies: high-rise steel lab in Massachusetts. Glazing is unitized curtain wall. Opaque areas are spandrel, metal panel or precast. The roof is a membrane over polyiso; HFC XPS is possible (Tally).
A3 Intensities: curtain wall 180 -> 1,238,000; opaque 105 -> 1,341,000; roof 30 -> 122,000; below grade 8 -> 16,000. Total about 2,717,000 kg.
A4 Check: about 115 per m2 of envelope, which is consistent with a curtain-wall facade.
A5: 2,717,000 kg / 54,500 = 49.9. Range 45-70 (higher WWR, HFC); A = 57.
A7: K = 1.33 (Laboratory, no envelope area), so CALIBRATED = 75.8.

Step B. Laboratory, 11 or more storeys: 129.

Step C. FINAL = 0.5 x 75.8 + 0.5 x 129 = 102.4; range 81.9-122.9.

BOTTOM_UP_kgCO2e_per_m2: 57
CALIBRATED_kgCO2e_per_m2: 75.8
BENCHMARK_kgCO2e_per_m2: 129
RANGE_kgCO2e_per_m2: 81.9 - 122.9

===== KEY: project-94__run2 =====
Scope check: BSECF includes E. Floor area = CFA 47,750 m2, including 10,900 m2 of below-grade parking.

Step A. A1 Areas: no envelope area. Assuming 5 storeys over 36,850 m2 of GFA, the roof is about 7,370 m2. Walls at 0.45 x 36,850 are about 16,580 m2. WWR is missing, so the multifamily default of 0.3 applies: 4,975 m2 of glazing and 11,610 m2 of opaque wall.
A2 Assemblies: wood light-frame over a concrete podium in California (3C). Walls are wood stud with stucco or fiber cement. Windows are vinyl. The roof is a membrane over polyiso. California banned HFC XPS, and the insulation is thin.
A3 Intensities: wood-stud wall 45 -> 522,500; vinyl windows 65 -> 323,400; roof 24 -> 176,900. Total about 1,022,800 kg.
A4 Check: about 36 per m2 of envelope. That is low but typical for wood frame with vinyl windows; aluminum windows would add about 300,000 kg.
A5: 1,022,800 kg / 47,750 = 21.4. Range 18-32; A = 25.
A7: K = 1.60 (Multifamily, no envelope area), so CALIBRATED = 40.

Step B. Multifamily, 2 to 5 storeys: 55.

Step C. FINAL = 0.5 x 40 + 0.5 x 55 = 47.5; range 38-57.

BOTTOM_UP_kgCO2e_per_m2: 25
CALIBRATED_kgCO2e_per_m2: 40
BENCHMARK_kgCO2e_per_m2: 55
RANGE_kgCO2e_per_m2: 38 - 57

===== KEY: project-118__run2 =====
Scope check: BSECF includes E. There is no CFA, so floor area = renovated GFA 18,300 m2.

Step A. A1 Areas: no envelope area. Assuming 8 storeys, the roof is about 2,290 m2. Walls at 0.4 x 18,300 are about 7,320 m2. WWR is missing, so the large-office default of 0.4 applies: 2,930 m2 of glazing and 4,390 m2 of opaque wall.
A6 Renovation: this is a major renovation with mass of about 670 kg/m2 and full BSECF scope, which is substantial new work. A re-clad with new windows is likely, but some existing walls may be retained.
A2 Assemblies: concrete office in zone 4A. Glazing is aluminum windows or curtain wall. Opaque walls are metal panel or precast on stud. The roof is a membrane over polyiso.
A3 Intensities: glazing 150 -> 439,500; opaque 95 -> 417,000; roof 26 -> 59,500. Total about 916,000 kg.
A4 Check: about 95 per m2 of wall plus roof, which is consistent.
A5: 916,000 kg / 18,300 = 50 for a full re-clad, or about 30 if the walls are partly kept. Range 30-65; A = 48.
A7: K = 1.49 (Office, no envelope area), so CALIBRATED = 71.5.

Step B. Office, 6 to 10 storeys: 79.

Step C. FINAL = 0.5 x 71.5 + 0.5 x 79 = 75.3; range 60.2-90.3.

BOTTOM_UP_kgCO2e_per_m2: 48
CALIBRATED_kgCO2e_per_m2: 71.5
BENCHMARK_kgCO2e_per_m2: 79
RANGE_kgCO2e_per_m2: 60.2 - 90.3

===== KEY: project-123__run2 =====
Scope check: BSECF includes E. Floor area = CFA 4,800 m2.

Step A. A1 Areas: no envelope area. Assuming 3 storeys, footprint and roof are about 1,600 m2. About 49 x 33 m gives a 164 m perimeter; at 13 m height the wall is about 2,130 m2. WWR is missing, so the education default of 0.32 applies: 680 m2 of glazing and 1,450 m2 of opaque wall.
A2 Assemblies: mass-timber school in Washington (4C). Walls are stud with fiber cement, wood or brick cladding. Windows are aluminum. The roof is a membrane over polyiso. Washington banned HFC XPS in 2021, but tool data may lag.
A3 Intensities: opaque wall 80 -> 116,000; windows 130 -> 88,400; roof 26 -> 41,600. Total about 246,000 kg.
A4 Check: about 66 per m2 of wall plus roof, or about 46 per m2 including the slab. That is acceptable.
A5: 246,000 kg / 4,800 = 51. Range 45-65 (brick, HFC); A = 55.
A7: K = 1.46 (Education, no envelope area), so CALIBRATED = 80.3.

Step B. Education, 2 to 5 storeys: 86.

Step C. FINAL = 0.5 x 80.3 + 0.5 x 86 = 83.2; range 66.5-99.8.

BOTTOM_UP_kgCO2e_per_m2: 55
CALIBRATED_kgCO2e_per_m2: 80.3
BENCHMARK_kgCO2e_per_m2: 86
RANGE_kgCO2e_per_m2: 66.5 - 99.8

===== KEY: project-198__run2 =====
Scope check: BSECF includes E. Floor area = CFA 7,200 m2.

Step A. A1 Areas: no envelope area. Assuming 4 storeys over 6,830 m2 of GFA, the roof is about 1,708 m2. Walls at 0.45 x 6,830 are about 3,070 m2. WWR 0.0687 gives 211 m2 of glazing and 2,860 m2 of opaque wall.
A2 Assemblies: wood light-frame lodging in Washington (4C). Walls are wood stud with fiber cement and some brick veneer, at R-25 (including continuous insulation). Windows are vinyl. The roof is a membrane over R-38 polyiso.
A3 Intensities: wall 55 -> 157,300; windows 70 -> 14,800; roof 30 -> 51,200. Total about 223,300 kg.
A4 Check: about 34 per m2 of envelope. That is low, but this is a wood frame with only 7% glazing. More brick or aluminum windows would push it up.
A5: 223,300 kg / 7,200 = 31. Range 27-45; A = 36.
A7: Lodging is not listed, so K = 1.31 and CALIBRATED = 47.2.

Step B. Lodging falls under "any other use": 84.

Step C. FINAL = 0.5 x 47.2 + 0.5 x 84 = 65.6; range 52.5-78.7.

BOTTOM_UP_kgCO2e_per_m2: 36
CALIBRATED_kgCO2e_per_m2: 47.2
BENCHMARK_kgCO2e_per_m2: 84
RANGE_kgCO2e_per_m2: 52.5 - 78.7

===== KEY: project-1__run2 =====
Scope check: BSECF includes E. Floor area = CFA 48,500 m2, including 23,500 m2 of below-grade parking.

Step A. A1 Areas: envelope area 13,355 m2. Assuming about 25 storeys, the roof is about 1,000 m2 and the ground slab about 1,000 m2, leaving about 11,355 m2 of wall. WWR 0.46 gives 5,223 m2 of glazing and 6,132 m2 of opaque wall.
A2 Assemblies: concrete high-rise residential in BC, which is mostly aluminum window wall. Opaque areas are insulated concrete with metal or fiber-cement cladding, or spandrel. The roof is a membrane over polyiso. Canada banned HFC XPS in 2021.
A3 Intensities: window wall 175 -> 914,000; opaque 85 -> 521,200; roof 26 -> 26,000; slab 8 -> 8,000. Total about 1,469,200 kg.
A4 Check: about 110 per m2 of envelope, which is consistent with window wall.
A5: 1,469,200 kg / 48,500 = 30.3 (CFA includes the large parkade). Range 26-38; A = 32.
A7: K = 0.97 (Multifamily, envelope area given), so CALIBRATED = 31.

Step B. Multifamily, 11 or more storeys: 71.

Step C. FINAL = 0.5 x 31 + 0.5 x 71 = 51; range 40.8-61.2.

BOTTOM_UP_kgCO2e_per_m2: 32
CALIBRATED_kgCO2e_per_m2: 31
BENCHMARK_kgCO2e_per_m2: 71
RANGE_kgCO2e_per_m2: 40.8 - 61.2

===== KEY: project-234__run2 =====
Scope check: BSE includes E. Floor area = CFA 64,500 m2.

Step A. A1 Areas: no envelope area. Assuming 13 storeys, the roof is about 4,960 m2. Walls at 0.3 x 64,500 (hospital) are about 19,350 m2. WWR is missing, so the healthcare default of 0.3 applies: 5,805 m2 of glazing and 13,545 m2 of opaque wall.
A2 Assemblies: steel hospital tower in zone 5A. Glazing is curtain wall and aluminum windows. Opaque walls are brick, metal panel or precast on steel stud. The roof is a membrane over polyiso.
A3 Intensities: glazing 150 -> 870,750; opaque 105 -> 1,422,200; roof 26 -> 129,000. Total about 2,421,950 kg.
A4 Check: about 99 per m2 of wall plus roof, which is consistent.
A5: 2,421,950 kg / 64,500 = 37.5. Range 33-50 (unitized curtain wall, HFC XPS); A = 42.
A7: K = 1.34 (Healthcare, no envelope area), so CALIBRATED = 56.3.

Step B. Healthcare, 11 to 15 storeys is not listed, so the "other storeys" value applies: 73.

Step C. FINAL = 0.5 x 56.3 + 0.5 x 73 = 64.7; range 51.7-77.6.

BOTTOM_UP_kgCO2e_per_m2: 42
CALIBRATED_kgCO2e_per_m2: 56.3
BENCHMARK_kgCO2e_per_m2: 73
RANGE_kgCO2e_per_m2: 51.7 - 77.6

===== KEY: project-108__run2 =====
Scope check: SEC includes E. Floor area = 3,350 + 50 = 3,400 m2.

Step A. A1 Areas: no envelope area. This is a minor renovation of a 2- to 5-storey mercantile building in New York.
A6 Renovation: mass_total is only 146,000 kg, about 43 kg/m2, so very little new material was installed. The data indicate the existing envelope was largely kept. New envelope work is likely limited to storefront or door replacement and some roofing patches.
A2 Assemblies: aluminum storefront and doors, plus small areas of membrane and insulation.
A3 Intensities: about 100 m2 of storefront at 145 -> 14,500; incidental roofing, flashing and sealants about 5,000-20,000. Total about 15,000-35,000 kg.
A4 Check: per m2 of envelope this cannot be compared, because most of the envelope is existing and excluded.
A5: 15,000-35,000 kg / 3,400 gives 4.4-10.3; A = 7.
A7: Mercantile is not listed, so K = 1.31 and CALIBRATED = 9.2.

Step B. Mercantile falls under "any other use": 84.

Step C. FINAL = 0.5 x 9.2 + 0.5 x 84 = 46.6; range 37.3-55.9.

BOTTOM_UP_kgCO2e_per_m2: 7
CALIBRATED_kgCO2e_per_m2: 9.2
BENCHMARK_kgCO2e_per_m2: 84
RANGE_kgCO2e_per_m2: 37.3 - 55.9
