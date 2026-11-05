// build_pptx.js - the conference poster as an editable one-slide PowerPoint (48 x 36 in).
// Text, tables and shapes are native; figures are the 300-dpi PNGs from report/make_figures.py.
// Logos: Stanford (identity.stanford.edu art sheet) and CEE lockup (cee.stanford.edu), white versions.
// Run: node report/poster/build_pptx.js   ->  report/poster/poster.pptx
const path = require("path");
const pptxgen = require("pptxgenjs");
const SKILL = process.env.PPTX_SKILL || "";
const FIG = path.resolve(__dirname, "../figures");
const ASSET = path.resolve(__dirname, "assets");

const THEME = { name: "Stanford Cardinal", headFontFace: "Cambria", bodyFontFace: "Arial",
  colors: { dk1: "1A1A1A", lt1: "FFFFFF", dk2: "4D4F53", lt2: "F4F1EE", accent1: "8C1515", accent2: "B1040E",
            accent3: "2A78D6", accent4: "EDA100", accent5: "175E54", accent6: "820000", hlink: "8C1515", folHlink: "820000" } };
const SIZES = { "feature_study.png": [1520, 770], "fig_bins.png": [1504, 1006], "fig_composition.png": [1602, 907],
  "fig_diagnostics.png": [1859, 1166], "fig_prompts.png": [2243, 789], "fig_scatter_v1_v3.png": [2138, 1028],
  "stanford_white.png": [1521, 418], "cee_white.png": [1080, 438] };

const W = 48, H = 36, M = 0.9, GAP = 0.6, HEAD = 6.1, TOP = HEAD + 0.55;
const COLW = (W - 2 * M - 3 * GAP) / 4;
const BODY = 30, CAP = 22, H2 = 58, H3 = 34;

const pres = new pptxgen();
pres.defineLayout({ name: "POSTER", width: W, height: H });
pres.layout = "POSTER";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "LLM enclosure embodied carbon - CEE226 poster";
pres.author = "CEE226 Group 8";
const C = pres.SchemeColor;
const slide = pres.addSlide();
slide.background = { color: "FFFFFF" };

// ---- helpers -------------------------------------------------------------------------
function runs(s, base = {}) {             // "**bold** text" -> text runs
  const out = [];
  s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).forEach(p => {
    const b = p.startsWith("**");
    out.push({ text: b ? p.slice(2, -2) : p, options: { ...base, bold: b || !!base.bold } });
  });
  return out;
}
function lines(text, fs, w) {             // rough line count for Arial at size fs in a box w inches wide
  const perLine = Math.floor((w * 72) / (fs * 0.54));
  return text.split("\n").reduce((n, p) => n + Math.max(1, Math.ceil(p.replace(/\*\*/g, "").length / perLine)), 0);
}
const cols = [0, 1, 2, 3].map(i => ({ x: M + i * (COLW + GAP), y: TOP }));

function h2(c, t) {
  slide.addShape(pres.shapes.RECTANGLE, { x: c.x, y: c.y, w: COLW, h: 0.12, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, objectName: "rule " + t });
  slide.addText(t, { x: c.x, y: c.y + 0.2, w: COLW, h: 0.95, fontFace: THEME.headFontFace, fontSize: H2, bold: true,
    color: C.accent1, margin: 0, valign: "top", isTextBox: true, objectName: "h2 " + t });
  c.y += 1.3;
}
function h3(c, t) {
  const h = lines(t, H3, COLW) * H3 * 1.2 / 72;
  slide.addText(t, { x: c.x, y: c.y, w: COLW, h, fontSize: H3, bold: true, color: C.text1, margin: 0, valign: "top", isTextBox: true });
  c.y += h + 0.12;
}
function para(c, t, fs = BODY, color = C.text1) {
  const h = lines(t, fs, COLW) * fs * 1.25 / 72 + 0.1;
  slide.addText(runs(t), { x: c.x, y: c.y, w: COLW, h, fontSize: fs, color, margin: 0, valign: "top", isTextBox: true, lineSpacingMultiple: 1.05 });
  c.y += h + 0.18;
}
function bullets(c, items, numbered = false, fs = BODY) {
  // one text box per item: paragraph-level bullet on the box, mixed bold/regular runs inside
  items.forEach((it, i) => {
    const h = lines(it, fs, COLW - 0.45) * fs * 1.25 / 72 + 0.08;
    const bullet = numbered ? { type: "number", numberStartAt: i + 1 } : { indent: 26 };
    slide.addText(runs(it, { fontSize: fs, color: C.text1 }), { x: c.x, y: c.y, w: COLW, h, margin: 0, valign: "top",
      bullet, isTextBox: true, lineSpacingMultiple: 1.05 });
    c.y += h + 0.12;
  });
  c.y += 0.1;
}
function image(c, file, cap, alt, scale = 1) {
  const [pw, ph] = SIZES[file];
  const w = COLW * scale, h = w * ph / pw;
  slide.addImage({ path: path.join(FIG, file), x: c.x + (COLW - w) / 2, y: c.y, w, h, altText: alt, objectName: file });
  c.y += h + 0.1;
  if (cap) para(c, cap, CAP, C.text2);
  else c.y += 0.15;
}
function stats(c, items) {
  const w = (COLW - 0.3 * (items.length - 1)) / items.length;
  items.forEach(([big, small], i) => {
    const x = c.x + i * (w + 0.3);
    slide.addShape(pres.shapes.RECTANGLE, { x, y: c.y, w, h: 1.9, fill: { color: C.background2 }, line: { color: C.background2, width: 0 } });
    slide.addText(big, { x: x + 0.2, y: c.y + 0.12, w: w - 0.4, h: 1.05, fontFace: THEME.headFontFace, fontSize: 80, bold: true, color: C.accent1, margin: 0, isTextBox: true });
    slide.addText(small, { x: x + 0.2, y: c.y + 1.18, w: w - 0.4, h: 0.6, fontSize: 22, color: C.text2, margin: 0, valign: "top", isTextBox: true });
  });
  c.y += 2.2;
}
function callout(c, t) {
  const h = lines(t, 34, COLW - 0.7) * 34 * 1.25 / 72 + 0.6;
  slide.addShape(pres.shapes.RECTANGLE, { x: c.x, y: c.y, w: COLW, h, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 } });
  slide.addText(runs(t, { color: C.background1 }), { x: c.x + 0.35, y: c.y + 0.3, w: COLW - 0.7, h: h - 0.6, fontSize: 34, margin: 0, valign: "middle", isTextBox: true });
  c.y += h + 0.3;
}
function table(c, rows) {
  const v = { v1: "2A78D6", v2: "EDA100", v3: "B1040E" };
  const data = rows.map((r, i) => r.map((cell, j) => ({
    text: (j === 0 && i > 0 ? "● " : "") + cell,
    options: { fontSize: i === 0 ? 24 : 28, bold: i === 0 || r[0].startsWith("v3"), align: j === 0 ? "left" : "right",
      color: i === 0 ? C.text2 : (r[0].startsWith("v3") ? C.accent1 : C.text1),
      border: [{ type: "none" }, { type: "none" }, { pt: i === 0 ? 3 : 1.5, color: i === 0 ? "4D4F53" : "D9D6D0" }, { type: "none" }],
      margin: [6, 6, 6, 6] } })));
  // colour the dot only: separate run for the bullet dot
  data.slice(1).forEach((r, i) => {
    const key = rows[i + 1][0].slice(0, 2);
    r[0].text = [{ text: "● ", options: { color: v[key], fontSize: 28 } }, { text: rows[i + 1][0], options: { fontSize: 28, bold: key === "v3", color: key === "v3" ? C.accent1 : C.text1 } }];
  });
  const cw = [2.9, 1.85, 1.45, 1.85, 1.35, 1.74];
  slide.addTable(data, { x: c.x, y: c.y, w: COLW, colW: cw, rowH: 0.62 });
  c.y += 0.62 * rows.length + 0.35;
}
function code(c, t) {
  const n = t.split("\n").length;
  const h = n * 20 * 1.25 / 72 + 0.45;
  slide.addShape(pres.shapes.RECTANGLE, { x: c.x, y: c.y, w: COLW, h, fill: { color: C.background2 }, line: { color: C.background2, width: 0 } });
  slide.addText(t, { x: c.x + 0.25, y: c.y + 0.2, w: COLW - 0.4, h: h - 0.4, fontFace: "Courier New", fontSize: 20, color: C.text1, margin: 0, valign: "top", isTextBox: true });
  c.y += h + 0.15;
}

// ---- header --------------------------------------------------------------------------
slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: W, h: HEAD, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 }, objectName: "header" });
const sw = 7.2, sh = sw * SIZES["stanford_white.png"][1] / SIZES["stanford_white.png"][0];
slide.addImage({ path: path.join(ASSET, "stanford_white.png"), x: M, y: 0.5, w: sw, h: sh, altText: "Stanford University logo" });
const cw_ = 8.2, ch_ = cw_ * SIZES["cee_white.png"][1] / SIZES["cee_white.png"][0];
slide.addImage({ path: path.join(ASSET, "cee_white.png"), x: W - M - cw_, y: (HEAD - ch_) / 2, w: cw_, h: ch_, altText: "Stanford Civil and Environmental Engineering logo" });
slide.addText("Can an LLM estimate the embodied carbon of a building enclosure?", { x: M, y: 0.5 + sh + 0.25, w: W - 2 * M - cw_ - 1.2, h: 1.5,
  fontFace: THEME.headFontFace, fontSize: 86, bold: true, color: C.background1, margin: 0, valign: "top", isTextBox: true, fit: "none" });
slide.addText([{ text: "Error analysis and prompt design for early-stage A1–A3 estimates on 292 North American buildings", options: { fontSize: 40, breakLine: true } },
  { text: "George Zheng · Zixuan Zhao · Heshan Chen · Fei Cheng · Jamie Liu   |   CEE226 · Group 8 · November 2026", options: { fontSize: 32 } }],
  { x: M, y: 0.5 + sh + 1.85, w: W - 2 * M - cw_ - 1.2, h: 1.3, color: C.background1, margin: 0, valign: "top", isTextBox: true });

// ---- column 1 ------------------------------------------------------------------------
let c = cols[0];
h2(c, "Question");
para(c, "Exterior-envelope choices lock in much of a building's embodied carbon at schematic design, when no LCA exists yet. Can a large language model, given only early-stage features, estimate the **cradle-to-gate (A1–A3) embodied carbon of the enclosure**, and which prompt design makes it better?");
h2(c, "Data & ground truth");
bullets(c, ["292 US/Canadian projects, harmonized WBLCA dataset (Benke et al., Sci. Data 2025): 928k material rows, 48 early-stage features.",
  "Ground truth: OmniClass **Shell – Enclosure**, stage **A1–A3**, kgCO2e per m² floor area. Median 78, range 0.5–514.",
  "10 new buildings have no window/glazing data at all: incomplete reference LCAs, flagged."]);
image(c, "fig_composition.png", "XPS insulation is 15.5% of all enclosure carbon (43.6 kgCO2e/kg: the HFC-blown product in Tally / One Click LCA of the period).", "Enclosure carbon by material group");
h2(c, "Method");
// flow boxes
const steps = ["48 features + glossary", "Prompt v1 / v2 / v3", "Claude Opus 5.5 subagents", "RANGE low–high", "Compare with reference LCA"];
const bw = (COLW - 0.35 * 4) / 5;
steps.forEach((s, i) => {
  const x = c.x + i * (bw + 0.35);
  slide.addShape(pres.shapes.RECTANGLE, { x, y: c.y, w: bw, h: 1.5, fill: { color: C.background2 }, line: { color: C.accent1, width: 2.5 } });
  slide.addText(s, { x: x + 0.08, y: c.y, w: bw - 0.16, h: 1.5, fontSize: 21, align: "center", valign: "middle", color: C.text1, margin: 0, isTextBox: true });
  if (i < 4) slide.addText("→", { x: x + bw, y: c.y, w: 0.35, h: 1.5, fontSize: 30, bold: true, align: "center", valign: "middle", color: C.accent1, margin: 0, isTextBox: true });
});
c.y += 1.8;
bullets(c, ["3 runs × 292 buildings per prompt; seeded shuffles and identical chunks allow paired comparisons.",
  "Subagents read only their task file: no web, no code, no ground truth.",
  "Metrics: ±20% coverage, RMSE, |log(est/ref)|, bias (geometric mean), run-to-run CV.",
  "Held-out test set: 88 buildings (stratified, seed 226)."]);

// ---- column 2 ------------------------------------------------------------------------
c = cols[1];
h2(c, "Baseline: why the model fails");
stats(c, [["19.5%", "within ±20% (prompt v1)"], ["0.46", "log–log slope (1 = ideal)"], ["0.75", "estimate / reference"]]);
image(c, "fig_bins.png", "The model compresses every building toward ~50–60 kgCO2e/m²: light enclosures are overestimated, heavy ones underestimated 3–4×.", "Compression by reference bin");
image(c, "fig_scatter_v1_v3.png", "Estimate vs. reference (line 1:1, band ±20%). v3 lifts the cloud toward the diagonal; the top end stays compressed.", "Estimate vs reference for prompts v1 and v3");
h3(c, "Root causes, from 876 reasoning texts");
bullets(c, ["**HFC-blown XPS is never considered**: it is mentioned in 0.6% of answers, yet it explains about half of the bias (est/ref 0.72 → 0.84 when XPS is removed from the reference) and the cold-climate gap.",
  "**Envelope area**: 0.81 when given, 0.65 when the model has to estimate it.",
  "**Curtain-wall tail** and **renovations** scoped too narrowly.",
  "**The intensity per m² of envelope** drives the error (r = −0.79), and **no feature describes the wall assembly**."], true);

// ---- column 3 ------------------------------------------------------------------------
c = cols[2];
h2(c, "Three prompts");
table(c, [["Prompt", "Coverage", "RMSE", "|log| med.", "Bias", "CV"],
  ["v1 plain", "19.5%", "79.7", "0.456", "0.75", "19.0%"],
  ["v2 method", "15.1%", "81.0", "0.563", "0.67", "13.8%"],
  ["v3 anchors", "25.0%", "76.0", "0.426", "0.86", "12.5%"]]);
h3(c, "v2: scope + step-by-step take-off + named materials");
para(c, "More consistent, but **less accurate**: 89% of answers still assumed polyiso roofs (roof intensity stayed at 35), bottom-up intensities were low (67 vs. 87 per m² of envelope), and \"count only new materials\" pushed renovations down.");
h3(c, "v3: quantitative anchors where numbers are chosen");
bullets(c, ["Component A1–A3 table from EPDs and CLF baselines (walls, glazing, roofs by insulation type, aluminum).",
  "Tool convention: legacy models often use HFC XPS, so include that case.",
  "Per-envelope sanity check, and a renovation rule that no longer subtracts."]);
image(c, "fig_diagnostics.png", "v3 removes the bias for buildings without XPS (0.97), with a given envelope area (0.99) and in warm zones (0.98).", "Failure modes by prompt");
callout(c, "**Lesson.** Qualitative knowledge in a prompt is repeated but not applied. Sourced numbers at the decision step move the estimate.");

// ---- column 4 ------------------------------------------------------------------------
c = cols[3];
h2(c, "Held-out test & features");
image(c, "fig_prompts.png", null, "Coverage and log error by prompt");
bullets(c, ["All 292: v3 vs. v1 McNemar p = 0.085, Wilcoxon p = 0.053; vs. v2 p = 0.002.",
  "Test 88: v3 26.1% vs. 20.5% coverage, RMSE 69 vs. 74, not significant (p = 0.41). Every finding behind v2/v3 replicates on the 204 dev buildings.",
  "**Feature study**: 10 early-design inputs are as good as all 48, and removing mass_total does not hurt. All differences are within run-to-run noise."]);
image(c, "feature_study.png", null, "Feature study", 0.7);
h2(c, "Takeaways");
bullets(c, ["LLMs give usable early-stage enclosure estimates for hotspot screening (¼ within ±20%, bias −14%), but not reliable building-level credit predictions.",
  "The error is structured (compression, material blind spots), so error analysis on the model's reasoning shows which prompt fix to make.",
  "The ceiling is information, not prompting: adding **assembly type** to the inputs is the next step."], true);
h2(c, "Final prompt (v3, excerpt)");
code(c, ["1. Areas: bldg_therm_env_area, or take off roof,",
  "   walls and glazing (bldg_wwr).",
  "2. Assemblies: name insulation type and thickness;",
  "   LCA models often use HFC-blown XPS on roofs.",
  "3. A1-A3 per m2 of component, e.g. metal panel",
  "   wall 70-110, unitized CW 150-210, roof+polyiso",
  "   20-28, roof+HFC XPS 85-110 (up to 335-410).",
  "4. Check: < ~50 per m2 envelope -> missing items.",
  "5. Range incl. higher-carbon options; no anchoring.",
  "6. Renovations: don't assume envelope is kept.",
  "RANGE_kgCO2e_per_m2: <low> - <high>"].join("\n"));

// ---- footer --------------------------------------------------------------------------
slide.addText("Data: Benke et al. (2025) Sci. Data 12, doi:10.1038/s41597-025-05216-0 (CC BY 4.0). Intensities: CLF North American Material Baselines 2023/2025, PCI, Kawneer and RDH EPDs. Model: Claude Opus 5.5 (medium effort), Claude Code subagents. Full prompts, code and model answers: github.com/HeshanChen/CEE226LCA",
  { x: M, y: H - 0.75, w: W - 2 * M, h: 0.45, fontSize: 20, color: C.text2, margin: 0, isTextBox: true });

const maxY = Math.max(...cols.map(k => k.y));
console.log("column bottoms (in):", cols.map(k => k.y.toFixed(2)).join(", "), "| limit", (H - 0.9).toFixed(2));

(async () => {
  const out = path.resolve(__dirname, "poster.pptx");
  await pres.writeFile({ fileName: out });
  // pptxgenjs writes an <a:pPr> before every run of a mixed-format paragraph; only the first
  // one is valid OOXML (later ones reset the bullet). Keep the first pPr of each paragraph.
  const JSZip = require("jszip");
  const fs = require("fs");
  const zip = await JSZip.loadAsync(fs.readFileSync(out));
  const name = "ppt/slides/slide1.xml";
  let xml = await zip.file(name).async("string");
  xml = xml.replace(/(<\/a:r>)<a:pPr\b[^>]*?(?:\/>|>[\s\S]*?<\/a:pPr>)/g, "$1");
  zip.file(name, xml);
  fs.writeFileSync(out, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
  if (SKILL) {
    const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));
    await applyTheme(out, THEME);
  }
  console.log("wrote", out);
})();
