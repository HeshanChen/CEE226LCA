# Enclosure (OmniClass "Shell - Enclosure") A1-A3 GWP reference values

Compiled 2026-11-04 for the CEE226 enclosure-estimation prompt. North American (NA) context preferred. All values are kgCO2e (GWP100, mostly IPCC AR5 or TRACI 2.1).

**Exclusions (to avoid data leakage):** Nothing here comes from the Benke et al. 2025 harmonized WBLCA dataset (figshare 28462145) or any analysis of it. I also deliberately left out results of the CLF WBLCA Benchmark Study v2 / Life Cycle Lab "material use and embodied carbon" paper and GitHub repository. Those results likely come from the same underlying project models. (The CLF *Material Baselines* report on figshare 30979495 is a different, EPD-based product dataset and is used below.)

**Conventions**
- 1 m2 @ RSI-1 = 1 m2 of insulation at the thickness that gives RSI 1.0 m2K/W (= R-5.678 IP).
- R-25 = RSI 4.40 and R-30 = RSI 5.28 (R / 5.678).
- 1000 ft2 = 92.903 m2.
- "A1-A3" = cradle-to-gate. Where a source adds B1/C4 (foam blowing-agent leakage) or A5, this is stated.
- **Bold** marks values I consider uncertain or derived by me rather than read from a source.

---

## Source tags

| Tag | Source |
|---|---|
| [CLF2023] | Carbon Leadership Forum, *2023 North American Material Baselines*, report + appendices (Aug 2023). [UW ResearchWorks handle 1773/49965](https://digital.lib.washington.edu/researchworks/handle/1773/49965) ([report PDF](https://digital.lib.washington.edu/researchworks/bitstreams/cf14fcca-501e-4a97-8257-b951e893a5ff/download), [appendix PDF](https://digital.lib.washington.edu/researchworks/bitstreams/61e8b8d4-bd38-45a1-bd35-0f50a9a59da6/download)) |
| [CLF2025] | Carbon Leadership Forum, *2025 North American Material Baselines* (report dated 2025-06-24). [doi:10.6084/m9.figshare.30979495](https://doi.org/10.6084/m9.figshare.30979495), [CLF page](https://carbonleadershipforum.org/2025-clf-north-american-material-baselines/) |
| [WA-SBCC] | Washington SBCC IBC Appendix S, CLF Option 1 Amendment 2. Reproduces the CLF 2025 values (secondary; used only as a cross-check). [PDF](https://sbcc.wa.gov/sites/default/files/2026-07/Option%201%20Amendment%202.pdf) |
| [KAWNEER] | Kawneer (Arconic) NA product EPDs, UL Environment, issued Oct 2021, A1-A3, GaBi 2021. Traditional curtain wall 1600 [EPD .108.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.108.1.pdf); unitized CW [.109.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.109.1.pdf); Trifab/storefront [.107.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.107.1.pdf); window wall [.110.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.110.1.pdf); sloped CW [.105.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.105.1.pdf); fixed/ribbon windows [.101.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.101.1.pdf); GLASSvent [.103.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.103.1.pdf); hung/sliding [.104.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.104.1.pdf); projected/casement [.106.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.106.1.pdf); extruded aluminum per kg [.102.1](https://www.kawneer.us//kawneer_files/shared%20files/Sustainability/EPD/EPD4789733794.102.1.pdf) |
| [UBC2022] | Zargar, *Impacts of Fenestration Materials on the Embodied Carbon of Buildings*, UBC Sustainability Scholars 2022 (Cascadia fiberglass window LCA + table of window EPDs). [PDF](https://sustain.ubc.ca/sites/default/files/2022-018_Research%20on%20the%20impacts%20of%20Innovative%20Fenestration%20Materials_Zargar.pdf) |
| [HARMON] | Harmon UCW8000 unitized CW EPD (ASTM). [PDF](https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blt61fa7800cf1f35e9/697b210fd004d2c2f0339807/642.EPD_FOR_Harmon_UCW8000.pdf). The PDF was blocked (403), so the value comes from a search snippet and is unverified. |
| [THERMOPLAST] | PVC windows (Thermoplast profiles, Quebec), ASTM EPD, 1 m2, A1-A3. [PDF](https://www.astm.org/v3/assets/blt5eb0a2cb04534832/bltaee001e300d7c2fd/690374ae2931336410f9e226/DEP_Thermoplast_EN_CT_Signed.pdf). Values come from a search snippet. |
| [RDH2025] | RDH Building Science for Elastochem/Honeywell, *Embodied Carbon Analysis: Spray Foam Assemblies* (Nov 2025). One Click LCA, 9 m2 functional unit normalized to per m2 of enclosure, effective R-24 to R-37, A1-A3 per layer. [PDF](https://res.cloudinary.com/elastochem/image/upload/v1766159206/RDH_EmbodiedCarbon_Rev3_ga4gjq.pdf) |
| [RDH-TMU] | RDH x Toronto Metropolitan University *Embodied Carbon Resource Guide*, 17 wall assemblies, A1-A3 per m2 of enclosure. [RDH page](https://www.rdh.com/embodied-carbon-resources-for-building-enclosures/). Values come from search-engine extracts of the RDH pages (the page returned 404 to the fetcher), so they are secondary. |
| [PCI2025] | PCI regionalized industry-average EPDs, May 2025, per metric tonne, A1-A3: [architectural precast](https://www.pci.org/Common/Uploaded%20files/PCI/Design_Resources/Sustainability/2025-PCI-Architectural-EPD.pdf), [insulated precast](https://www.pci.org/Common/Uploaded%20files/PCI/Design_Resources/Sustainability/2025-PCI-Insulated-EPD.pdf) |
| [AA-INGOT] | Aluminum Association, industry-average *Primary Aluminum Ingot* EPD (NA, 2010 data, issued 2014). [PDF](https://www.aluminum.org/sites/default/files/2021-11/104.1_Aluminum_EPD_PrimaryAluminumIngot.pdf) |
| [ARUP-SG] | Arup and Saint-Gobain Glass, *The carbon footprint of facades: significance of glass* (European data). [PDF](https://arup.com/globalassets/downloads/insights/the-carbon-foot-print-of-facades-the-significance-of-glass.pdf) |
| [GS2025] | Glotman Simpson (Vancouver), *Partition choices, carbon consequences*, May 2025. Rough enclosure intensities; boundary not stated. [Link](https://glotmansimpson.com/partition-choices-carbon-consequences-the-case-for-smarter-material-selection/) |
| [KPF] | KPF, *Lifecycle carbon analysis* (US mid-rise office). [Link](https://www.kpf.com/project/lifecycle-carbon-analysis) |
| [BEO2023] | Smith & Ugliuzza, *Embodied carbon impact of enclosure materials*, Building Enclosure, Sep 2023 (qualitative ranking only; numbers are in an image). [Link](https://www.buildingenclosureonline.com/articles/91886-embodied-carbon-impact-of-enclosure-materials) |
| [OCL-EPDM] | Holcim Elevate RubberGard EPDM product EPDs (ASTM, 2025) via One Click LCA public pages, e.g. [60 mil non-reinforced](https://materials.oneclicklca.com/en/material/epdm-non-reinforced-membrane/68432b56c6ee4b1007bb9900) |
| [OCL-TPO] | TPO product EPDs via One Click LCA public pages, e.g. [Carlisle/Versico 60 mil](https://materials.oneclicklca.com/en/material/tpo-single-ply-waterproofing-roof-membrane-mechanically-fastened/5a0470815d96ff44a4190e27) |

---

## 1. Opaque exterior wall assemblies (per m2 of wall)

Component building blocks (A1-A3, per m2 of wall):
- Steel studs, 6 in at 16 in o.c. ≈ 6.7 kg steel/m2. 6.7 × 2.44 kg/kg [CLF2025 CFS framing] = **16.4**. RDH reports 140/9 = **15.6** [RDH2025].
- 1/2 in gypsum: 207/92.9 = 2.2 [CLF2025] (RDH uses 3.2 with One Click generic data).
- 5/8 in Type X gypsum: 277/92.9 = 3.0 [CLF2025].
- 1/2 in glass-mat sheathing: 437/92.9 = 4.7 [CLF2025].
- Thermally broken cladding attachment: 190–200/9 = **21–22** [RDH2025]. This is large and often omitted.
- Aluminum roll-formed panel: 18.6 [CLF2025: 1,860/100 m2]. RDH uses 170/9 = 18.9.
- Steel roll-formed panel: 15.3 [CLF2025].
- MCM/ACM panel (4 mm, aluminum skins): 28.0 [CLF2025: 2,800/100 m2].
- Brick veneer (90 mm) + mortar: 510/9 = **56.7** [RDH2025, One Click generic clay brick].
- 8 in CMU: 820/9 = **91** [RDH2025, One Click generic CMU]. Uncertain: CLF2025 normal-weight CMU is 208–241 kgCO2e/m3 [WA-SBCC]. If that is per gross m3, 0.203 m3/m2 gives 42–49 plus grout, mortar and rebar.
- Air/vapor barrier membrane (self-adhered, 40 mil): 20/9 = 2.2 [RDH2025].

| Item | Value or range (A1-A3, kgCO2e/m2 wall) | Boundary | Source | Notes / conversions |
|---|---|---|---|---|
| Steel stud + aluminum panel (rainscreen), split insulated: 6 in ocSPF + 2 in ccSPF (HFO), R-26 | 69.6 | A1-A3 | [RDH2025] CC2 | 626 kg / 9 m2. Includes 2 layers of gypsum, studs, clips (30 %), Al panel (27 %). |
| Steel stud + aluminum panel, 4 in ccSPF (HFO) ext. + 6 in fiberglass batt, R-27 | 72.7 | A1-A3 | [RDH2025] UC2 | |
| Steel stud + aluminum panel, 6 in mineral wool board ext. + 2 in ccSPF, R-26 | 93.5 | A1-A3 | [RDH2025] UC3 | 840 kg / 9 m2. Mineral wool 23.8 %, clips 23.8 %, Al panel 20.2 %, studs 16.7 %. |
| Split-insulated steel frame + "lightweight cladding" | 110.3 | A1-A3 | [RDH-TMU] W02 | Secondary value. |
| ACM/MCM on steel stud | **60** | not stated | [GS2025] | Rough designer value. |
| ACM on steel stud, component build-up (my estimate) | **≈ 95–110** | A1-A3 | derived from [CLF2025] + [RDH2025] | MCM 28 + studs 16 + 2 × gypsum ≈ 6 + clips/subframe 22 + 4–6 in MW board ≈ 16–22 (RSI 2.4–3.6 × 6.8) + barrier 2 + extrusions/trim **5–15** (not found). |
| Brick veneer on wood stud (3 in ccSPF + 2 in ocSPF), R-24 | 70.1 | A1-A3 | [RDH2025] CR1 | |
| Brick veneer on wood stud (4 in MW + 4 in ccSPF), R-35 | 96.9 | A1-A3 | [RDH2025] UR2 | |
| Brick veneer + 5 in ccSPF + 8 in CMU backup, R-26 | 164.3 | A1-A3 | [RDH2025] UC1 | CMU 55.5 %, brick 34.5 %. Highest of the 10 RDH walls. |
| Exterior-insulated CMU + brick veneer, RSI 4.6 (R-26) | 136.3 | A1-A3 | [RDH-TMU] W01 | Secondary value. |
| Masonry veneer on steel stud | **200** | not stated | [GS2025] | Seems high next to the RDH build-ups. |
| Masonry veneer on concrete backup | **270** | not stated | [GS2025] | |
| Brick veneer on steel stud, component build-up (my estimate) | **≈ 90–115** | A1-A3 | derived | Brick + mortar 57 + studs 16 + gypsum 5–8 + 3 in MW (RSI ~2.3 × 6.8–8.2 = 16–19) + ties/shelf angles **3–10** + barrier 2. |
| Steel stud + EIFS (EPS), split insulated | 50.1 | A1-A3 | [RDH-TMU] W03 | Secondary value. |
| Stucco (3-coat, 22 mm over lath), cladding layer only | **≈ 12–16** | A1-A3 | my estimate from NIST BEES geometry ([PDF](https://ws680.nist.gov/Bees/ProductListFiles/Generic%20Stucco.pdf)) | 0.022 m × ~1,830 kg/m3 ≈ 40 kg/m2. ~20–25 % cement ≈ 9 kg × 0.92 ≈ 8. Metal lath ~1.5 kg × 2.44 ≈ 3.7. Very uncertain. |
| Fiber-cement cladding layer only (8–10 mm) | 4.7–9.9 (EU EPDs) | A1-A3 | [Cedral EPD](https://media.cedral.world/doc_635803_nl/original/1719081288/epd-hub-4116-cedral-lap.pdf); [Etex panel, One Click](https://materials.oneclicklca.com/en/material/fibre-cement-panel/65111c61ed00ef6f3d446566) | No NA (James Hardie) value found. Cedral GWP-fossil is 7.1. |
| Steel stud + fiber cement or stucco, full assembly (my estimate) | **≈ 45–80** | A1-A3 | derived | Studs 16 + gypsum 5–8 + insulation 10–25 + cladding 5–16 + girts/clips **5–22**. |
| Wood stud + vinyl siding, 3 in XPS + 2 in ccSPF, R-25 | 25.9 | A1-A3 | [RDH2025] UR1 | Biogenic carbon reported separately. |
| Wood stud + wood siding, 2 in MW + 4 in ccSPF, R-27 | 30.3 | A1-A3 | [RDH2025] CR2 | |
| Wood stud + wood siding, 8 in ccSPF (HFO), R-37 | 40.9 | A1-A3 | [RDH2025] UR3 | |
| Wood frame + mineral wool + stone veneer | 60.4 | A1-A3 | [RDH-TMU] W05 | Secondary value. |
| Insulated metal panel (IMP), 2 in, PU core (industry average, HFC era) | 107 | A1-A3 | [CLF2025] | 10,700 per 100 m2. Panel only, no interior finish or girts. |
| IMP, 4 in | 191 | A1-A3 | [CLF2025] | 19,100 per 100 m2. |
| IMP, 6 in | 274 | A1-A3 | [CLF2025] | 27,400 per 100 m2. The CLF printed equation "b = 4184 + 2332 t" does not reproduce the table. "b = 2332 + 4184 t" does (t = 2, 4, 6 gives 10,700, 19,100, 27,400), so the constants appear swapped. |
| IMP, NA product EPDs (all thicknesses, n = 26; many low-GWP or polyiso cores) | 26.5–71.9, mean 44.4 | A1-A3 | [CLF2025] Table 3.8.3 | 2,650–7,190 per 100 m2. CLF notes PU-core (HFC) products are much higher. MCA expects a lower new industry EPD. |
| IMP with polyiso core (assembly) | 105.2 | A1-A3 | [RDH-TMU] W11 | Secondary value. |
| Precast concrete sandwich panel (double-wythe insulated, phenolic core) | 166.2 | A1-A3 | [RDH-TMU] W06 | Secondary value. |
| Architectural precast + interior spray foam | 114.3 | A1-A3 | [RDH-TMU] W13 | Secondary value. |
| Insulated precast, PCI industry average | 240–335 kg/t by region | A1-A3 | [PCI2025] | Per m2: 6 in total concrete ≈ 0.37 t/m2 → **89–124**. 8 in total concrete ≈ 0.49 t/m2 → **117–164**. (0.152 m or 0.203 m × 2,400 kg/m3 + insulation.) 2025 data; 2016–2023 projects were likely somewhat higher. |
| Architectural precast, PCI industry average | 259–354 kg/t by region | A1-A3 | [PCI2025] | 5–6 in panel ≈ 0.30–0.37 t/m2 → **78–130**, plus backup, insulation and gypsum if present. |
| Tilt-up concrete panel, 7.25–9 in, conventional mix (my estimate) | **≈ 70–100** panel only; **≈ 80–125** with interior furring, insulation and gypsum | A1-A3 | derived from [CLF2023]/[WA-SBCC] ready-mix 316–386 kg/m3 (4,000–5,000 psi) | 0.184–0.229 m × 316–386 = 58–88, plus rebar ~10–15 kg × 0.854 = 9–13. |
| CMU with insulation (CMU + brick + ccSPF) | 136–164 | A1-A3 | [RDH2025] UC1, [RDH-TMU] W01 | CMU + EIFS or metal panel was not found. **Estimate ≈ 90–140** (CMU 45–91 + insulation 10–30 + cladding 15–30). |
| Curtain-wall spandrel (mineral wool back-pan + interior spray foam) | 74.5 | A1-A3 | [RDH-TMU] W09 | Secondary value. |
| Curtain-wall spandrel, framing + spandrel glass/back-pan + insulation (my estimate) | **≈ 90–140** | A1-A3 | derived | Kawneer CW frame share 53 per m2 [KAWNEER] + spandrel glass 25–45 or Al back-pan 15–20 + MW 10–25. |
| Existing masonry + interior ocSPF retrofit (reference low end) | 18.2 | A1-A3 | [RDH2025] CC1 | New materials only. |

Qualitative ranking: brick + HFO ccSPF lowest, precast + HFC XPS highest; metal panels lower upfront than precast [BEO2023].

## 2. Fenestration (per m2 of unit, frame + glazing, A1-A3)

| Item | Value or range | Boundary | Source | Notes / conversions |
|---|---|---|---|---|
| Aluminum stick curtain wall (Kawneer 1600) | 136 (frame 53.1 + glazing 83.2) | A1-A3 | [KAWNEER .108.1] | 34.9 kg/m2, 20/80 frame/glass by mass, 1.5 × 1.6 m module. All glass modeled the same (IGU). |
| Aluminum sloped / overhead CW | 141 | A1-A3 | [KAWNEER .105.1] | |
| Aluminum unitized curtain wall (Kawneer) | 166 (frame 82.7 + glazing 83.2) | A1-A3 | [KAWNEER .109.1] | 38.7 kg/m2, 28/72 frame/glass. |
| Aluminum unitized CW (Harmon UCW8000) | **204** | A1-A3 | [HARMON] | Unverified snippet. |
| Aluminum CW, YKK AP America | **52.7** | as reported | [UBC2022] Table 2 | Probably frame only or a different scope; outlier. |
| CW, NA manufacturer spread | **~60–360** | A1-A3 | [CLF forum thread](https://community.carbonleadershipforum.org/t/steel-extrusions-epd/7805) | Anecdotal. |
| Unitized CW, European parametric (78 % recycled Al) | 80–188 | A1-A3 | [ARUP-SG] | Timber frame + Al spandrel ≈ 80–85; Al frame + GRC spandrel 188. European Al (7.0 kg/kg) is lower than NA. |
| 16 European facade typologies (CW, precast, rainscreen, brick) | 160–520 | A1-A5 + B4 + C | [ARUP-SG] | A1-A3 is ≈ 60–78 % of the total, giving **≈ 100–400** A1-A3. |
| Aluminum storefront (Kawneer Trifab) | 146 (frame 62.6 + glazing 83.2) | A1-A3 | [KAWNEER .107.1] | 36.1 kg/m2. |
| Aluminum storefront (EFCO) | 150 | A1-A3 | [UBC2022]; [EFCO EPD](https://www.astm.org/v3/assets/blt5eb0a2cb04534832/bltd412f41eaa3fa750/697b203df6a610b4568f505e/832.EFCO_EPD-Storefront.pdf) | |
| Aluminum window wall (Kawneer) | 170 | A1-A3 | [KAWNEER .110.1] | |
| Aluminum window wall (Arcadia) | 177 | A1-A3 | [UBC2022] | |
| Aluminum windows (Kawneer fixed/ribbon; GLASSvent; hung/sliding; projected/casement) | 106.6; 94.0; 103.3; 122.0 | A1-A3 | [KAWNEER .101/.103/.104/.106] | Declared unit 1.82 m2: 194/1.82, 171/1.82, 188/1.82, 222/1.82. |
| Aluminum windows (EFCO; Arcadia projected; AluQuébec) | 100 (fixed) to 150; 125; 136 | A1-A3 | [UBC2022] | |
| Vinyl (PVC) windows, NA (6 types) | 41–66 | A1-A3 | [THERMOPLAST] | Fixed lowest, awning highest. |
| Hybrid Al/PVC windows, NA | 47–95 | A1-A3 | [Thermoplast hybrid EPD](https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blte32228d1efb77455/69f39c6c5082973ca78c9da5/2026-04-28_DEP_Thermoplast_hybride_EN_v2_signed.pdf) | Snippet value. |
| PVC windows, Europe | ~64–87 per m2 (e.g. European PVC Window 116/1.82 = 64; Cortizo 85–88) | A1-A3 | [UBC2022]; One Click pages | For context only. |
| Fiberglass window (Cascadia), double IGU | 121.2 | A1-A3 | [UBC2022] | Frame alone 84.9 per m2. |
| Fiberglass window (Cascadia), triple IGU | 145.2 | A1-A3 | [UBC2022] | |
| Fiberglass window (Inline, Toronto) | 75.7 | A1-A3 | [UBC2022] Table 5 | |
| IGU, double, implied (Cascadia) | **36.3** | A1-A3 | derived from [UBC2022] | 121.2 − 84.9. Likely thinner glass. |
| IGU, triple, implied (Cascadia) | **60.3** | A1-A3 | derived from [UBC2022] | 145.2 − 84.9. |
| Glazing share of CW (Kawneer; ~27.9 kg glass/m2) | 83.2 per m2 of CW | A1-A3 | [KAWNEER] | |
| Double IGU 6 + 6 mm, low-e (my estimate) | **≈ 54–63** | A1-A3 | derived from NGA flat glass 1,430 kg/t [CLF2025] + Saint-Gobain processing [ARUP-SG] | 30 kg × 1.43 = 42.9 + DGU assembly 9.9 + coating 1.1 + tempering 0–9.4 (4.7 per lite). |
| Triple IGU 3 × 6 mm (my estimate) | **≈ 85–95** | A1-A3 | derived | 45 kg × 1.43 = 64.4 + TGU assembly 18.1 + coatings 2.2 (+ tempering). |
| Flat glass (float) | 1,430 per t ≈ 21.5 per m2 at 6 mm | A1-A3 | [CLF2023]/[CLF2025] (NGA 2019) | Area = 400/t m2 per tonne (t in mm). 6 mm: 66.7 m2/t, so 1,430/66.7 = 21.5. |
| IGU / processed glass / curtain wall CLF baseline | none ("no sufficiently representative data") | – | [CLF2025] | CLF 2023 found 3 NA IGU EPDs spanning ~50–650 per m2 (2 electrochromic). |

## 3. Roof assemblies above the deck (per m2 of roof, A1-A3)

Component values:

| Component | Value | Unit | Boundary | Source | Notes |
|---|---|---|---|---|---|
| TPO 45 / 60 / 80 mil | 3.32 / 4.29 / 6.05 | per m2 | A1-A3 | [CLF2025] (SPRI 2023 IW-EPD) | Product EPDs 3.1–5.8 for 60 mil [OCL-TPO]. |
| EPDM reinforced 45 / 60 / 75 mil | 5.42 / 7.10 / 8.86 | per m2 | A1-A3 | [CLF2025] (SPRI 2022) | |
| EPDM non-reinforced 45 / 60 / 90 mil | 4.73 / 6.14 / 9.56 | per m2 | A1-A3 | [CLF2025] | Holcim RubberGard 60 mil: 4.5–4.7 [OCL-EPDM]. |
| PVC 40 / 48 / 60 / 80 mil | 4.2 / 5.2 / 6.3 / 8.3 | per m2 | A1-A3 | [CLF2023]/[CLF2025] (CFFA 2020) | |
| SBS mod-bit membrane (per ply, by install method) | 5.20–5.85 (parent 5.64) | per m2 | A1-A3 | [CLF2025] (ARMA 2023) | A two-ply system is probably **~10–12** if each ply is counted. Not confirmed whether the ARMA declared unit is per ply or per system. |
| APP mod-bit | 9.01–9.22 | per m2 | A1-A3 | [CLF2025] | |
| BUR (hot asphalt; fastened base + 2 ply + cap) | 2.57; 3.06 | per m2 | A1-A3 | [CLF2025] | |
| Glass-mat gypsum cover board 1/2 in; 5/8 in | 4.70; 5.42 | per m2 | A1-A3 | [CLF2025] | 437/92.903; 504/92.903. |
| Polyiso roof board, GRF facer | 2.11 (A1-A3); 2.20 incl. C4 | per m2 @ RSI-1 | A1-A3 | [CLF2023] Fig. 8; [CLF2025] | A1 1.86 + A2 0.065 + A3 0.184 = 2.11. |
| Polyiso roof board, CGF facer | 2.95 | per m2 @ RSI-1 | A1-A3 | [CLF2023]/[CLF2025] | 2.7 + 0.065 + 0.184. |
| Steel roll-formed roof panel (standing seam) | 15.3 | per m2 | A1-A3 | [CLF2025] | 1,530/100. |
| Aluminum roll-formed roof panel | 18.6 | per m2 | A1-A3 | [CLF2025] | |
| Vapor retarder, adhesives, fasteners, insulation layers | **not found; assume ~1–4** | per m2 | – | – | Uncertain. |

Assembly roll-ups (my arithmetic, A1-A3), at R-25 to R-30 (RSI 4.40–5.28):

| Assembly (R-25 to R-30) | Insulation alone | Assembly total | Notes |
|---|---|---|---|
| Single-ply (TPO 60 mil) + polyiso (GRF) + 1/2 in gypsum cover board | 2.11 × 4.40–5.28 = 9.3–11.1 | 4.29 + 9.3–11.1 + 4.70 = **18–20; ~20–25 with accessories** | With CGF polyiso: 13.0–15.6, giving ~22–28. With EPDM/PVC 60 mil: add ~2–3. With 2-ply SBS instead of TPO: add ~6–8. |
| Membrane + XPS with HFC blowing agent (legacy NA, pre-~2021) | A1-A3 only: 18.3 × 4.40–5.28 = 80.5–96.6. Incl. B1 + C4: 75.2 × 4.40–5.28 = 331–397 | **≈ 85–110 (A1-A3 only); ≈ 335–410 (A1-A3 + B1 + C4)** | Very sensitive to how the tool books blowing agent (see §4). Manufacturer A1-A3 ranges 3.6–29.4 per RSI-1 → 16–155 at R-25 to R-30. |
| Membrane + XPS with low-GWP (HFO/reduced-HFC) blowing agent | A1-A3 4.7 × 4.40–5.28 = 20.7–24.8. Total 6.7 → 29.5–35.4. CLF2025 40 psi total 10.9 → 48–58 | **≈ 28–40 (A1-A3); up to ~65 (B1/C4, 40 psi)** | |
| Membrane + heavy-density mineral wool roof board | 6.82–8.16 × 4.40–5.28 = 30.0–43.1 | **≈ 35–55** | 2025 NAIMA 6.82; 2018 NAIMA 8.16. Usually no cover board. |
| Membrane + EPS | 2.53–2.63 × 4.40–5.28 = 11.1–13.9 | ≈ 20–25 | |
| Metal standing-seam roof + polyiso + underlayment (over deck) | 9–16 | 15.3–18.6 + 9–16 + **2–5** = **≈ 27–40** | Clips and sub-purlins not found. |
| Insulated metal roof panel, 4 in | – | 191 (legacy PU industry average); product EPDs 26.5–71.9 | [CLF2025] |

## 4. Insulation per functional unit (per m2 @ RSI-1)

| Item | Value | Boundary | Source | Notes |
|---|---|---|---|---|
| XPS, conventional HFC (legacy NA): OC FOAMULAR 2019 / DuPont Styrofoam 2021 / Kingspan 40 psi 2021 | A1-A3: 21.9 / 29.4 / 3.6 (avg 18.3). B1: 28.5 / 31.4 / 0. C4: 7.3 / 38.5 / 65.0. **Total 57.7 / 99.3 / 68.6 (avg 75.2)** | A1-A3, B1, C4 itemized | [CLF2023] App. G1 Fig. 9 | Kingspan puts all blowing agent in C4, so the totals are the comparable numbers. Per inch (RSI 0.88 per in at R-5/in): A1-A3 ≈ 16; total ≈ 66. |
| XPS, reduced-HFC / HFO: FOAMULAR NGX / DuPont ST-100 / Kingspan low-GWP | A1-A3 6.9 / 3.5 / 3.8 (avg 4.7); totals 9.6 / 6.1 / 4.3 (avg 6.7) | A1-A3, B1, C4 | [CLF2023] Fig. 9 | |
| XPS, CLF 2023 overall baseline (mix of both) | 41 (A1-A3 11.5 + B1 10.6 + C4 18.8) | A1-A3 + B1 + C4 | [CLF2023] | Product EPD median 12.6, max 102.8. |
| XPS (Owens Corning 2024, low-GWP) ≤25 / 40 / 60 / 100 psi | 8.9 / 10.9 / 14.1 / 20.1 | A1-A3 + B1 + C4 | [CLF2025] | Higher strength (roof/below-grade) gives higher GWP. |
| Polyiso wall (foil facer) | 4.10 (A1-A3); 4.19 incl. C4 | A1-A3 | [CLF2023] Fig. 8; [CLF2025] | CLF2025 parent "polyiso, wall" 3.5. |
| Polyiso roof GRF / CGF | 2.11 / 2.95 | A1-A3 | [CLF2023]/[CLF2025] | |
| EPS Type I | 2.63 (2017 EPD, A1-A3); 2.53 (2023 EPD) | A1-A3 | [CLF2023] Fig. 8; [CLF2025] | |
| Mineral wool heavy-density board | 8.16 (NAIMA 2018); 6.82 (NAIMA 2023) | A1-A3 | [CLF2023]; [CLF2025] | Product EPD median 3.7 (range 1.2–9.1), mostly Rockwool, under a different PCR. |
| Mineral wool batt / light board | 3.33 (2018); 2.68 (2023) | A1-A3 | [CLF2023]; [CLF2025] | |
| Fiberglass batt, faced / unfaced | 1.06 / 1.01 | A1-A3 | [CLF2025]; [WA-SBCC] | No baseline in 2023. |
| Fiberglass board | 5.02 | A1-A3 | [CLF2025] | |
| ccSPF medium density, HFC | 20.1 | A1-A3 + A5 + B1 + C4 | [CLF2023] (SPFA 2018) | |
| ccSPF medium density, HFO | 4.04 (SPFA 2018); 2.63 (SPFA 2024, A1-A3 + A5) | as stated | [CLF2023]; [CLF2025] | |
| ccSPF roofing, HFC / HFO | 26.3 / 4.8 (2018); HFO 3.87 (2024) | A1-A3 + A5 (+ B1, C4 in 2018) | [CLF2023]; [CLF2025] | |
| ccSPF 2K-LP, HFC / HFO | 35.7 / 3.7 | A1-A3 + A5 + B1 + C4 | [CLF2023] | |
| ocSPF | 1.6 (2018); 1.17 (2024) | A1-A3 + A5 | [CLF2023]; [CLF2025] | |

## 5. Aluminum (kgCO2e per kg, A1-A3)

| Item | Value | Source | Notes |
|---|---|---|---|
| Extrusion, mill / anodized / painted (AEC industry average, 2020 data) | 10.3 / 10.8 / 11.7 | [CLF2025] (AEC 2022a) | 2023 report: 10.25 / 10.76 / 11.67. |
| Thermally improved extrusion (CW, storefront, windows), anodized / painted | 11.8 / 12.7 | [CLF2025] (AEC 2022b) | |
| Extrusion, Aluminum Association industry EPD (all finishes) | 6.08 | [CLF2025] footnote 27 (AA 2022b) | Lower because of more recycled input. |
| Kawneer extrusion, painted / anodized (70 % scrap, 30 % primary) | 8.94 / 7.21 | [KAWNEER .102.1] | Module D −4.0. |
| NA primary ingot (2010 data) | 8.94 | [AA-INGOT] | Hydro-heavy Canadian/US mix. Global primary is much higher. |
| Aluminum alloy, 40 % pre-consumer recycled (ecoinvent GLO) | 16.4 | [ARUP-SG] | Shows how generic or global datasets in tools can be ~1.5–2× NA values. |
| Aluminum sheet (NA industry average) | 3.82 | [CLF2025] (AA 2022) | High recycled content. USITC comment cites 3.9 ([link](https://www.usitc.gov/research_and_analysis/documents/sa_emissions/taa_comments_811655-2097185.pdf)). |

## 6. Top-down enclosure intensities

| Item | Value | Boundary | Source | Notes |
|---|---|---|---|---|
| Facade systems, per m2 of facade (16 European typologies) | 160–520 | A1-A5 + B4 + C | [ARUP-SG] | A1-A3 ≈ 61–78 % of each total, so **≈ 100–400 A1-A3**. |
| Opaque NA wall assemblies, per m2 of enclosure | 18–166 (new construction ~26–166) | A1-A3 | [RDH2025], [RDH-TMU] | |
| NA aluminum fenestration, per m2 | 94–204 | A1-A3 | [KAWNEER], [UBC2022], [HARMON] | |
| Rough designer intensities: glazing 120; ACM on stud 60; masonry on stud 200; masonry on concrete 270 per m2 enclosure. Assumes enclosure area ≈ 50 % of floor area. | as listed | not stated | [GS2025] | Uncertain. |
| Curtain wall share of a US mid-rise office's material emissions | "up to 20 %" (life cycle) | life cycle | [KPF] | |
| Ranking | foundation and structure largest; enclosure second | – | [Walter P Moore](https://www.walterpmoore.com/exploring-embodied-carbon-building-enclosures) | |
| Enclosure per m2 of floor area | **not found in a non-excluded NA source** | – | – | My estimate: facade/GFA ratio 0.3–0.6 × blended facade 90–130 (40 % WWR) ≈ 27–78, plus roof (1/floors × 20–100) → **≈ 35–90 kgCO2e/m2 GFA**, A1-A3, for mid-rise commercial. **Derived, uncertain.** |

Not found: a NA industry-average EPD for fiber cement, EIFS, stucco, IGUs or curtain wall; a tilt-up per-m2 EPD; TPO/EPDM accessory and adhesive values; an NA enclosure-per-floor-area benchmark outside the excluded datasets.

Tool caveat: Tally (GaBi) and One Click LCA (generic and EPD data) in 2016–2023 may book HFC XPS/SPF blowing-agent emissions in A1-A3 differently. Conventional XPS ranges from 3.6 to 29.4 (A1-A3 only) and 58–99 (A1-A3 + B1 + C4) per m2 @ RSI-1, depending on allocation. Generic global aluminum (~16 kg/kg) is also ~1.3–1.6× the AEC NA extrusion values.

---

## Prompt-ready summary (A1-A3, kgCO2e per m2 of component unless noted)

- Steel stud + metal panel / ACM rainscreen (with insulation, clips, 2 × gypsum): 70–110 [RDH2025][RDH-TMU][CLF2025]
- Steel stud + brick veneer: 90–120 (designer quote up to 200) [RDH2025][GS2025]
- Brick veneer + CMU backup: 135–165 [RDH2025][RDH-TMU]
- Steel stud + EIFS: ~50. Steel stud + fiber cement or stucco: ~45–80 (estimate) [RDH-TMU][derived]
- Wood stud + siding (vinyl or wood): 25–45. With stone or brick veneer: 60–100 [RDH2025][RDH-TMU]
- Insulated metal panel: 2 in ≈ 107, 4 in ≈ 191, 6 in ≈ 274 (legacy PU/HFC industry average). Newer product EPDs 27–72 [CLF2025]
- Precast concrete sandwich panel: 90–165. Architectural precast + backup: 80–130 [PCI2025][RDH-TMU]
- Tilt-up concrete (7.25–9 in): 70–100 panel only; 80–125 with interior insulation and gypsum (estimate) [CLF2023][derived]
- CW spandrel (opaque CW zone): 75–140 [RDH-TMU][KAWNEER][derived]
- Aluminum stick curtain wall incl. IGU: 120–150 (Kawneer 136) [KAWNEER]
- Aluminum unitized curtain wall incl. IGU: 150–210 (Kawneer 166, Harmon ~204) [KAWNEER][HARMON]
- Aluminum storefront: 140–155. Aluminum window wall: 170–180 [KAWNEER][UBC2022]
- Aluminum windows: 95–140 [KAWNEER][UBC2022]
- Vinyl windows: 40–90. Fiberglass windows: 75–145 [THERMOPLAST][UBC2022]
- IGU alone: double 35–65, triple 60–95. Flat glass ≈ 21.5 per m2 at 6 mm [UBC2022][CLF2025][ARUP-SG]
- Roof membranes: TPO 60 mil 4.3; EPDM 60 mil 6.1–7.1; PVC 60 mil 6.3; SBS mod-bit ≈ 5.6 per ply; gypsum cover board 4.7 [CLF2025]
- Roof, membrane + polyiso (R-25 to R-30) + cover board: 20–28 [CLF2025][derived]
- Roof, membrane + HFC-blown XPS (R-25 to R-30): 85–110 A1-A3. 335–410 if blowing-agent B1/C4 is included [CLF2023][derived]
- Roof, membrane + low-GWP XPS: 28–40 (up to ~65 with B1/C4, 40 psi) [CLF2023][CLF2025]
- Roof, membrane + mineral wool board (R-25 to R-30): 35–55 [CLF2023][CLF2025][derived]
- Metal standing-seam roof + polyiso: 27–40 [CLF2025][derived]
- Insulation per m2 @ RSI-1: polyiso 2.1–4.1; EPS 2.5–2.6; MW board 6.8–8.2; MW batt 2.7–3.3; FG batt 1.0–1.1; HFC XPS 18 (A1-A3) / 58–99 (with B1/C4); low-GWP XPS 4–11; ccSPF HFC 20–36 vs HFO 2.6–4.8 [CLF2023][CLF2025]
- Aluminum: NA thermally broken extrusion 11.8–12.7 kg/kg (AEC); AA/Kawneer extrusion 6–9; NA primary ingot 8.9; sheet 3.8; global generic ~16 [CLF2025][KAWNEER][AA-INGOT][ARUP-SG]
- Top-down per m2 of facade: ~100–400 A1-A3 (160–520 A-C, European) [ARUP-SG]. Per m2 of GFA: ~35–90 (derived, uncertain; no non-excluded NA benchmark found)
