# Answer-guided passages: enclosure A1–A3 GWP per m² floor area

Compiled 2026-11-16 for CEE226.

**Method disclosure.** This is deliberate answer-guided retrieval. The target values were known in advance. The search looked for published passages that state numbers close to them, so a model reading a passage would be pointed toward the target. Hits are therefore selected for agreement, not sampled. They must not be read as independent validation.

**Scope.**
- Sources already carded in `feature_keyed_facts.md` and `envelope_intensities_sources.md` are not repeated (CSA Group 2023, LETI, Amany 2019, LMN, Arup façades, Kawneer EPDs and others). Where they bear on a target, the "no hit" list says so.
- "Same dataset" marks sources derived from the CLF WBLCA Benchmark Study v2 / Benke et al. 2025 harmonized dataset, which is very probably the source of the target values. Treat these as near-circular.

**Conventions.**
- 1 kgCO2e/ft² = 10.76 kgCO2e/m².
- **A1–A3 share of A–C for enclosure.** The CLF Benchmark Report gives the SE-scope (structure + enclosure) interquartile ranges as A1–A3 ~280–540, A4 ~4–10, B4–B5 ~16–50 and C2–C4 ~26–60 kgCO2e/m². A1–A3 is therefore about 80–85 % of A–C. Enclosure carries more replacement (B4), so I use **0.75–0.85 (central 0.8)** to convert A–C to A1–A3. This factor is my assumption and is not sourced for enclosure specifically.
- **A1–A5 to A1–A3:** × ~0.93. This is my assumption, based on the CLF calculator's enclosure A4 + A5 ≈ 11.5 on top of A1–A3 108.
- **"Verified"** means the quote was read on the opened page or PDF. For BDP Quadrangle, the text is image-only, so the quote was read from rendered PDF pages.

## (a) Archetype targets: passages

| Target (archetype, value) | Verbatim quote | Number as stated (unit, boundary) | Converted to kgCO2e/m² floor, A1–A3 | Source | Type | Status |
|---|---|---|---|---|---|---|
| Whole set, 84 | "15% and 18% are attributed respectively to the façade and to the building services." and "Case studies average 560 kgCO2e/m2" | Façade 15 % of the A1–A5 average of 560 kgCO2e/m² (6 Arup case studies; 5 London offices of 6–11 storeys + 1 Amsterdam timber tower; total includes services) | 0.15 × 560 = **84** (A1–A5). × 0.93 ≈ **78** A1–A3 | WBCSD & Arup (2021), *Net-zero buildings: Where do we stand?*, p. 34 | report (industry/institutional; UK/EU) | verified |
| Whole set, 84 | "Commercial 295 108 21 128" (row of the table "A1-A3 values per Building Typology and Physical Scope (all values in kgCO2/m2)": Structure, Enclosure, Interiors, MEP) | Enclosure A1–A3 = 108 kgCO2/m² (**average** of 199 commercial buildings) | **108**; it is a mean, so the median is lower. 108 / 84 = 1.29 | CLF, *EC Policy Reduction Calculator: Embodied carbon intensities* (documentation page) | same dataset | verified |
| Whole set, 84 | "It's followed by average ECIs of Shell - Enclosure (141 kgCO2e/m2), Substructure (75 kgCO2e/m2)…" | Mean Shell-Enclosure ECI 141, A–C (Benke harmonized dataset, n ≈ 292) | 141 × 0.75–0.85 = **106–120** (a mean; the median is lower). Borderline: 1.26–1.43 × 84 | Benke et al. (2025), *Scientific Data* | same dataset (peer-reviewed) | verified |
| Whole set, 84 | "The IQRs of each physical scope (A, above) included Structure (~230-440 kgCO2e/m2), Enclosure (~80-170 kgCO2e/m2), and Interiors (~45-100 kgCO2e/m2)." | Enclosure IQR 80–170, A–C without A5 (n = 154 SEI projects) | × 0.8 → IQR ≈ **64–136**, midpoint ≈ 100; it brackets 84 | Benke, Jensen, Lewis, Chafart, Simonen (2025), *The Embodied Carbon Benchmark Report*, §4.5 | same dataset | verified |
| Whole set, 84 | "They were followed by enclosures ranging from 20-250 kg CO₂e/m²…". Fig. 20 average label for enclosure: "106 (~22%)" | Enclosure 20–250 (30 CA buildings); average 106 (~22 % of total) for the 19 SEI projects; A–C, 60 yr | 106 × 0.8 ≈ **85** | Benke, Roberts, Shen, Carlisle, Chafart, Simonen (2024), *The California Carbon Report*, §4.3.2.2 and Fig. 20 | same dataset | verified (the 106 is a figure label in the PDF text layer) |
| Office, 84 | Same WBCSD passage as above ("15% … to the façade"; "Case studies average 560 kgCO2e/m2") | 15 % × 560, A1–A5; 5 of the 6 cases are offices | **84** A1–A5; ≈ 78 A1–A3 | WBCSD & Arup (2021) | report | verified |
| Office 6–10 storeys, 79 | Same WBCSD passage (the case-study offices are 6, 7, 8, 9 and 11 storeys) | as above | ≈ 78–84 | WBCSD & Arup (2021) | report | verified |
| Office, 84 | Same CLF calculator row: "Commercial 295 108 21 128" | Commercial enclosure A1–A3 mean 108 | 108 (1.29 × target) | CLF EC Policy Reduction Calculator | same dataset | verified |
| Education, 86 | Same CLF calculator row (the "Commercial" category includes education) | 108 mean, A1–A3 | 108 (1.26 × target) | CLF EC Policy Reduction Calculator | same dataset | verified |
| Laboratory, 92 | Same CLF calculator row | 108 mean, A1–A3 | 108 (1.17 × target) | CLF EC Policy Reduction Calculator | same dataset | verified |
| Public assembly, 96 | Same CLF calculator row | 108 mean, A1–A3 | 108 (1.13 × target) | CLF EC Policy Reduction Calculator | same dataset | verified |
| Multifamily 11+ storeys, 71 | "Multifamily Residential 204 72 26 64" (same table: Structure, Enclosure, Interiors, MEP) | Enclosure A1–A3 mean 72 (44 multifamily buildings) | **72** | CLF EC Policy Reduction Calculator | same dataset | verified |
| Multifamily concrete, 69 | Same row as above | 72 | **72** (1.04 × target) | CLF EC Policy Reduction Calculator | same dataset | verified |
| Multifamily overall, 54 | Same row as above | 72 | 72 (1.33 × target; just outside ±30 %) | CLF EC Policy Reduction Calculator | same dataset | verified (marginal) |
| Multifamily 2–5 storeys, 55 | Same row as above | 72 | 72 (1.31 × target; marginal) | CLF EC Policy Reduction Calculator | same dataset | verified (marginal) |
| Multifamily 11+ storeys, 71 (concrete, 69) | "To meet the TGS target of 350kgCO2e/m2, the average envelope ECI should not exceed 80.5 kgCO2e/m²" and "Among the 44 projects analyzed, 31% of the upfront embodied emissions assessments align with this carbon budget" | Envelope 80.5 kgCO2e/m² GFA = 23 % of 350, A1–A5, One Click LCA. 44 Toronto MURBs (30 high-rise, 12 mid-rise, 2 low-rise). Fig. 13 points span ≈ 45–145, with most at 80–110 | Median ≈ 85–95 A1–A5 (read from chart; 69 % of projects are above 80.5) → × 0.93 ≈ **79–88** A1–A3 (1.1–1.25 × 71) | BDP Quadrangle (2024), *How Design Drives Embodied Carbon: Envelope Upfront Embodied Carbon in MURBs*, pp. 16–18 | industry | verified (read from rendered PDF pages; text is image-only) |
| Multifamily 11+ storeys, 71 (window-wall high tail) | "Aluminum, exceeding the TGS budget by 50%, significantly increases embodied carbon and requires careful attention to form, WWR, and density." | Aluminum window-wall projects average ≈ 1.5 × 80.5 ≈ 120, A1–A5 | ≈ 112 A1–A3 (tail, not median) | BDP Quadrangle (2024), p. 23 | industry | verified (rendered page) |

## (b) Calibration: why early or simplified enclosure take-offs come out low

| Target | Verbatim quote | Number as stated | Implied under-estimate of a simplified take-off | Source | Type | Status |
|---|---|---|---|---|---|---|
| Calibration ×1.2–1.6 | "Using the early design tool (scenario ED1) gives a higher impact of 18-42% for the whole building compared to the detailed LCA approach. This is due to the additional building elements, the conservative materials estimation and the completeness of inventory…" | Complete or conservative inventory is 18–42 % higher than a typical detailed LCA. The paper also notes "for case B; the windows were missing materials for frame." | Typical take-off ≈ 15–30 % low (ratio 1.18–1.42) | Zimmermann R.K. et al. (2019), IOP Conf. Ser.: Earth Environ. Sci. 323:012118 | peer-reviewed (conference) | verified |
| Calibration (omitted elements) | "The result is 4-19% lower in global warming potential (GWP) for the buildings where the early design tool was used. The reduced impact is mainly due to the exclusion of some building elements…" | Early tool 4–19 % low (LCAP study, cited in the same paper) | 4–19 % low, whole building | Zimmermann et al. (2019), citing the LCAP tool study | peer-reviewed (conference) | verified |
| Calibration (truncation / generic data) | "Process LCAs thus tend to systematically underestimate the emissions… According to Lenzen and Treloar (2006), the truncation error can be even as high as 50%." The paper also says truncation "may lead to underestimations of tens of percentages". It gives windows as an example of missing production-phase impacts. | up to 50 % | 20–50 % low | Heinonen et al. (2016), *Building and Environment* 95:116–125 | peer-reviewed | verified |
| Calibration (attachments / clips) | Table row: "Thermally Broken Cladding Attachment System … 87.3 kg 190 30.4%" (CC2 steel-stud + aluminum panel wall, total 626 kgCO2 per 9 m²). UC3 wall: "… 200 23.8%" | Clips are 30.4 % and 23.8 % of the wall's A1–A3 | Omitting attachments makes the wall 24–30 % low (a 1.31–1.44 × uplift is needed) | RDH Building Science (2025), *Embodied Carbon Analysis: Spray Foam Assemblies* (for Elastochem), pp. 21–22 | industry | verified |
| Calibration (tool element tagging) | "These represented an average of 23% of each project's total GWP from life cycle stages A–C not being assigned to a building element… the average A–C GWP impacts… increase… Shell-Enclosure (+19%)" | Raw tool output left 23 % of GWP "undefined". Reclassification raised enclosure by 19 %. | Raw tool enclosure ≈ 16 % low | Benke et al. (2025), *Scientific Data*, Technical Validation | same dataset (peer-reviewed) | verified |
| Calibration (waste is small) | Wastage rates "glazing 1%, aluminum 1%, other materials including concrete 5%". Commercial enclosure A5.3 = 2.3 vs A1–A3 108. | ≈ 2 % | Waste explains little of the gap | CLF EC Policy Reduction Calculator (ASHRAE 240P draft rates) | same dataset / report | verified (via fetch summary of the page) |
| Calibration (tool choice) | "the whole building life cycle carbon equivalents of One-Click LCA is less than half than of Tally" | One Click < 0.5 × Tally for the same bill of materials | Tool choice alone can move results by more than 2×; the direction depends on the tool | Cormick H. (2017), MRP thesis (Scribd copy) | thesis | snippet, unverified |

## (c) Targets with no hit within ±30 % (new sources)

- **Education 1-storey (104), 2–5 storeys (86), steel (105), concrete (83), wood (89):** no storey- or structure-specific passage found. Only the pooled "Commercial 108" (same dataset) applies.
- **Healthcare (73) and healthcare steel (79):** none. The pooled commercial 108 is 1.48 × target, so it is not a hit.
- **Laboratory 2–5 storeys (77), 11+ (129), steel (93), concrete (109):** none new. Amany 2019 (Rosling Center, ≈ 104 A1–A3) is already carded as F11.
- **Office 1-storey (131), 2–5 storeys (82), 11+ (72), steel (104), concrete (66), wood (91):** none new. The CSA Group 2023 Toronto offices (envelope ≈ 138–140 A–C) are already carded as F9–F10.
- **Public assembly 1-storey (108):** none.
- **Public order and safety (132; 2–5 storeys, 160):** none. Vancouver Fire Hall 17 gives only a whole-building figure (≈ 424 kgCO2e/m²).
- **Multifamily 6–10 storeys (48) and wood frame (43):** none. The CLF multifamily figure of 72 is 1.5–1.7 × these targets.
- **Transportation hub (157; 2–5 storeys, 196):** none. No published terminal or station enclosure intensity was found.
- **Warehouse (65):** none. The GLP Magnitude declaration (UK) gives only a total of ≈ 400 A1–A5 with no element split.
- **Not opened (blocked):**
  - City of Vancouver / Morrison Hershfield 2023 reduction study (403)
  - Vancouver ZGF mid-rise case study (403)
  - RICS whole-life carbon assessment PS 2023 (403)
  - CLF-BC case studies West 42nd and Cambie St (404)
  - Make Architects *Upfront carbon: how good is good enough?* (the body did not load). Its snippet says a precast façade is "55kgCO2e/m2 GIA" on a compact plan vs "85" on an elongated plan. That would hit office 6–10 / 11+ storeys, but it is a **snippet, unverified**.

## (d) Full citations

1. WBCSD & Arup (2021). *Net-zero buildings: Where do we stand?* World Business Council for Sustainable Development, July 2021. https://archive.wbcsd.org/contentwbc/download/12446/185553/1
2. Carbon Leadership Forum. *EC Policy Reduction Calculator: Documentation, Embodied carbon intensities.* https://ec-policy-reduction-calculator.carbonleadershipforum.org/documentation/embodied-carbon-intensities (accessed 2026-11-16). Values are averages from the CLF WBLCA Benchmark Study v2 (same dataset).
3. Benke B., Chafart M., Shen Y., Ashtiani M., Carlisle S., Simonen K. (2025). A harmonized dataset of high-resolution embodied life cycle assessment results for buildings in North America. *Scientific Data*. https://doi.org/10.1038/s41597-025-05216-0 (same dataset)
4. Benke B., Jensen A., Lewis M., Chafart M., Simonen K. (2025). *The Embodied Carbon Benchmark Report: Embodied Carbon Budgets and Analysis of 292 Buildings in the US and Canada.* Carbon Leadership Forum, April 2025. https://doi.org/10.6084/m9.figshare.32827298 (same dataset)
5. Benke B., Roberts M., Shen Y., Carlisle S., Chafart M., Simonen K. (2024). *The California Carbon Report: An Analysis of the Embodied and Operational Carbon Impacts of 30 Buildings.* Carbon Leadership Forum, University of Washington. http://hdl.handle.net/1773/51287 (PDF: https://digital.lib.washington.edu/researchworks/bitstreams/5db4c2ff-0689-409c-8b0b-2768a521a0c6/download) (same dataset)
6. BDP Quadrangle (2024). *How Design Drives Embodied Carbon: Envelope Upfront Embodied Carbon in Multi-Unit Residential Buildings* (December 2024). https://bdp.payloadcms.app/api/media-files/file/How%20Design%20Drives%20Embodied%20Carbon%20-%20Envelope%20Upfront%20Carbon%20in%20MURBs.pdf
7. Zimmermann R.K., Kanafani K., Rasmussen F.N., et al. (2019). Early design stage building LCA using the LCAbyg tool: Comparing cases for early stage and detailed LCA approaches. *IOP Conf. Ser.: Earth Environ. Sci.* 323, 012118. https://doi.org/10.1088/1755-1315/323/1/012118
8. Heinonen J., Säynäjoki A., Junnonen J.-M., Pöyry A., Junnila S. (2016). Pre-use phase LCA of a multi-story residential building: Can greenhouse gas emissions be used as a more general environmental performance indicator? *Building and Environment* 95, 116–125. https://doi.org/10.1016/j.buildenv.2015.09.006 (accepted preprint: https://opinvisindi.is/bitstream/20.500.11815/201/1/j.buildenv.2015.09.006.pdf)
9. RDH Building Science (2025). *Embodied Carbon Analysis: Spray Foam Assemblies* (Rev. 3, 13 Nov 2025), prepared for Elastochem. https://res.cloudinary.com/elastochem/image/upload/v1766159206/RDH_EmbodiedCarbon_Rev3_ga4gjq.pdf
10. Cormick H. (2017). Master's research paper comparing Athena, Tally and One Click LCA (Scribd copy). https://www.scribd.com/document/726774344/Cormick-Hayley (snippet only)
11. Make Architects. *Upfront carbon: how good is good enough?* https://www.makearchitects.com/thinking/upfront-carbon-how-good-is-good-enough/ (snippet only)
