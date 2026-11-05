// build_weekly.js - weekly progress updates (one PowerPoint, one section per week).
// Each week shows only the prompt versions presented so far (figures from make_weekly_figures.py).
// Run: NODE_PATH=<dir with pptxgenjs,jszip> PPTX_SKILL=<pptx skill dir> node report/weekly/build_weekly.js
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const SKILL = process.env.PPTX_SKILL || "";
const FIG = path.resolve(__dirname, "../figures");
const WFIG = path.resolve(__dirname, "figures");
const ASSET = path.resolve(__dirname, "../poster/assets");

const THEME = { name: "Stanford Cardinal", headFontFace: "Cambria", bodyFontFace: "Arial",
  colors: { dk1: "1A1A1A", lt1: "FFFFFF", dk2: "4D4F53", lt2: "F4F1EE", accent1: "8C1515", accent2: "B1040E",
            accent3: "2A78D6", accent4: "EDA100", accent5: "175E54", accent6: "820000", hlink: "8C1515", folHlink: "820000" } };

const W = 13.333, H = 7.5, M = 0.6, TOP = 1.45, BOT = 6.75;
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "CEE226 Group 8 - weekly updates";
pres.author = "CEE226 Group 8";
const C = pres.SchemeColor;

function pngSize(file) {                       // width/height from the PNG header
  const b = fs.readFileSync(file);
  return [b.readUInt32BE(16), b.readUInt32BE(20)];
}

// ---- layouts ----------------------------------------------------------------------------
const tag = { placeholder: { options: { name: "tag", type: "body", x: 7.2, y: 7.0, w: 4.9, h: 0.3, fontSize: 10,
  color: C.text2, align: "right", valign: "middle", margin: 0 }, text: "" } };
pres.defineSlideMaster({
  title: "COVER", background: { color: C.accent1 },
  objects: [
    { image: { path: path.join(ASSET, "stanford_white.png"), x: M, y: 0.5, w: 1.82, h: 0.5 } },
    { image: { path: path.join(ASSET, "cee_white.png"), x: W - M - 1.23, y: 6.55, w: 1.23, h: 0.5 } },
    { placeholder: { options: { name: "kicker", type: "body", x: M, y: 1.45, w: 12, h: 0.4, fontSize: 16,
      color: C.background2, margin: 0, valign: "top" }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 1.85, w: 12.1, h: 1.25, fontFace: THEME.headFontFace,
      fontSize: 38, bold: true, color: C.background1, margin: 0, valign: "top", align: "left" }, text: "" } },
    { text: { text: "CEE226 Group 8 · LLM estimation of enclosure embodied carbon", options: { x: M, y: 6.7, w: 8, h: 0.3,
      fontSize: 11, color: C.background2, margin: 0 } } },
  ],
});
const contentObjs = (bg) => ({
  background: { color: bg },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 0.4, w: 12.1, h: 0.8, fontFace: THEME.headFontFace,
      fontSize: 28, bold: true, color: C.accent1, margin: 0, valign: "middle", align: "left" }, text: "" } },
    { text: { text: "CEE226 Group 8 · Stanford University", options: { x: M, y: 7.0, w: 5, h: 0.3, fontSize: 10,
      color: C.text2, margin: 0, valign: "middle" } } },
    tag,
  ],
  slideNumber: { x: 12.35, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.text2, align: "right" },
});
pres.defineSlideMaster({ title: "CONTENT", ...contentObjs(C.background1) });
pres.defineSlideMaster({ title: "NEXT", ...contentObjs(C.background2) });

// ---- helpers ----------------------------------------------------------------------------
function runs(s, base = {}) {                  // "**bold** text" -> runs
  return s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(p => {
    const b = p.startsWith("**");
    return { text: b ? p.slice(2, -2) : p, options: { ...base, bold: b || !!base.bold } };
  });
}
function bulletText(items, { numbered = false, fs = 14, gap = 7 } = {}) {
  const out = [];
  items.forEach((it, i) => {
    const r = runs(it, { fontSize: fs, color: C.text1 });
    r[0].options.bullet = numbered ? { type: "number", numberStartAt: i + 1 } : { indent: 16 };
    r[0].options.paraSpaceAfter = gap;
    if (i < items.length - 1) r[r.length - 1].options.breakLine = true;
    out.push(...r);
  });
  return out;
}
function bullets(s, items, box, opts = {}) {
  s.addText(bulletText(items, opts), { ...box, margin: 0, valign: "top", isTextBox: true, objectName: "bullets" });
}
function image(s, file, box, alt, dir = FIG) {
  const p = path.join(dir, file);
  const [pw, ph] = pngSize(p);
  let w = box.w, h = w * ph / pw;
  if (h > box.h) { h = box.h; w = h * pw / ph; }
  s.addImage({ path: p, x: box.x + (box.w - w) / 2, y: box.y, w, h, altText: alt, objectName: file });
  return h;
}
function statCards(s, stats, box, { dark = false, big = 34 } = {}) {
  const n = stats.length, gap = 0.3, w = (box.w - gap * (n - 1)) / n;
  stats.forEach(([v, lab], i) => {
    const x = box.x + i * (w + gap);
    s.addShape(pres.shapes.RECTANGLE, { x, y: box.y, w, h: box.h, objectName: "card " + v,
      fill: dark ? { color: C.background1, transparency: 88 } : { color: C.background2 },
      line: { color: dark ? C.background1 : C.background2, width: 0, transparency: dark ? 100 : 0 } });
    s.addText(v, { x: x + 0.25, y: box.y + 0.2, w: w - 0.5, h: big * 1.25 / 72, fontFace: THEME.headFontFace, fontSize: big,
      bold: true, color: dark ? C.background1 : C.accent1, margin: 0, valign: "top", isTextBox: true });
    s.addText(lab, { x: x + 0.25, y: box.y + 0.25 + big * 1.25 / 72, w: w - 0.5, h: box.h - 0.45 - big * 1.25 / 72,
      fontSize: 14, color: dark ? C.background1 : C.text1, margin: 0, valign: "top", isTextBox: true });
  });
}
function table(s, head, rows, box, { fs = 12, bold = [] } = {}) {
  const hdr = head.map(t => ({ text: t, options: { bold: true, color: C.background1, fill: { color: C.accent1 } } }));
  const body = rows.map((r, ri) => r.map((t, ci) => ({ text: String(t), options: {
    bold: bold.includes(ri) || ci === 0, fill: { color: ri % 2 ? C.background2 : C.background1 } } })));
  s.addTable([hdr, ...body], { x: box.x, y: box.y, w: box.w, colW: box.colW, fontSize: fs, color: C.text1,
    border: { type: "solid", pt: 0.5, color: "D9D6D0" }, margin: 0.06, valign: "middle", rowH: 0.36 });
}
function numberedCards(s, cards, box, cols = 3, cardFs = 16) {
  const rowsN = Math.ceil(cards.length / cols), gap = 0.3;
  const w = (box.w - gap * (cols - 1)) / cols, h = (box.h - gap * (rowsN - 1)) / rowsN;
  cards.forEach(([t, body], i) => {
    const x = box.x + (i % cols) * (w + gap), y = box.y + Math.floor(i / cols) * (h + gap);
    s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: C.background2 }, line: { color: C.background2, width: 0 },
      objectName: "card " + t });
    s.addShape(pres.shapes.OVAL, { x: x + 0.22, y: y + 0.22, w: 0.5, h: 0.5, fill: { color: C.accent1 },
      line: { color: C.accent1, width: 0 }, objectName: "badge " + (i + 1) });
    s.addText(String(i + 1), { x: x + 0.22, y: y + 0.22, w: 0.5, h: 0.5, fontSize: 16, bold: true, color: C.background1,
      align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(t, { x: x + 0.88, y: y + 0.2, w: w - 1.05, h: 0.55, fontSize: 18, bold: true, color: C.text1, margin: 0,
      valign: "middle", isTextBox: true });
    s.addText(runs(body, { fontSize: cardFs, color: C.text1 }), { x: x + 0.25, y: y + 0.9, w: w - 0.5, h: h - 1.05, margin: 0,
      valign: "top", isTextBox: true });
  });
}
function flow(s, steps, box) {
  const n = steps.length, gap = 0.35, w = (box.w - gap * (n - 1)) / n;
  steps.forEach((t, i) => {
    const x = box.x + i * (w + gap);
    s.addShape(pres.shapes.RECTANGLE, { x, y: box.y, w, h: box.h, fill: { color: i === 2 ? C.accent1 : C.background2 },
      line: { color: i === 2 ? C.accent1 : C.background2, width: 0 }, objectName: "step " + (i + 1) });
    s.addText(runs(t, { fontSize: 15, color: i === 2 ? C.background1 : C.text1 }), { x: x + 0.12, y: box.y + 0.08,
      w: w - 0.24, h: box.h - 0.16, align: "center", valign: "middle", margin: 0, isTextBox: true });
    if (i < n - 1) s.addShape(pres.shapes.LINE, { x: x + w + 0.04, y: box.y + box.h / 2, w: gap - 0.08, h: 0,
      line: { color: C.text2, width: 1.5, endArrowType: "triangle" }, objectName: "arrow " + (i + 1) });
  });
}

// ---- slide builders -----------------------------------------------------------------------
function cover(wk) {
  const s = pres.addSlide({ masterName: "COVER", sectionTitle: `Week ${wk.n}` });
  s.addText(`Weekly update ${wk.n} of 5  ·  week of ${wk.date}`, { placeholder: "kicker" });
  s.addText(wk.topic, { placeholder: "title" });
  s.addText("THIS UPDATE IN THREE NUMBERS", { x: M, y: 3.3, w: 8, h: 0.3, fontSize: 12, bold: true, charSpacing: 2,
    color: C.background2, margin: 0, isTextBox: true });
  statCards(s, wk.take, { x: M, y: 3.7, w: W - 2 * M, h: 2.45 }, { dark: true, big: 44 });
}
function content(wk, sl) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: `Week ${wk.n}` });
  s.addText(sl.title, { placeholder: "title" });
  s.addText(`Week ${wk.n} · ${wk.short}`, { placeholder: "tag" });
  const dir = sl.wfig ? WFIG : FIG;
  if (sl.type === "figtext") {
    const iw = sl.imgW || 7.2;
    image(s, sl.img, { x: M, y: TOP + 0.05, w: iw, h: BOT - TOP - 0.1 }, sl.alt, dir);
    bullets(s, sl.bullets, { x: M + iw + 0.45, y: TOP + 0.05, w: W - 2 * M - iw - 0.45, h: BOT - TOP },
      { numbered: !!sl.numbered, fs: sl.fs || 17, gap: 10 });
  } else if (sl.type === "stats") {
    statCards(s, sl.stats, { x: M, y: TOP + 0.05, w: W - 2 * M, h: 1.75 });
    bullets(s, sl.bullets, { x: M, y: TOP + 2.15, w: W - 2 * M, h: BOT - TOP - 2.15 }, { fs: 18, gap: 12 });
  } else if (sl.type === "flow") {
    flow(s, sl.steps, { x: M, y: TOP + 0.1, w: W - 2 * M, h: 1.45 });
    bullets(s, sl.bullets, { x: M, y: TOP + 1.95, w: W - 2 * M, h: BOT - TOP - 1.95 }, { fs: 17, gap: 12 });
  } else if (sl.type === "tablefig") {
    table(s, sl.head, sl.rows, { x: M, y: TOP + 0.05, w: sl.tw, colW: sl.colW }, { bold: sl.boldRows || [] });
    const ty = TOP + 0.05 + 0.36 * (sl.rows.length + 1) + 0.35;
    bullets(s, sl.bullets, { x: M, y: ty, w: sl.tw, h: BOT - ty }, { fs: 16, gap: 10 });
    if (sl.img) image(s, sl.img, { x: M + sl.tw + 0.4, y: TOP + 0.05, w: W - 2 * M - sl.tw - 0.4, h: BOT - TOP }, sl.alt, dir);
  } else if (sl.type === "cards") {
    numberedCards(s, sl.cards, { x: M, y: TOP + 0.05, w: W - 2 * M, h: BOT - TOP - 0.05 }, sl.cols || 3, sl.cardFs || 16);
  } else if (sl.type === "quote") {
    s.addText(sl.quote, { x: 1.3, y: 2.2, w: W - 2.6, h: 2.2, fontFace: THEME.headFontFace, fontSize: 30, italic: true,
      color: C.accent1, align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(runs(sl.sub, { fontSize: 16, color: C.text2 }), { x: 1.8, y: 4.65, w: W - 3.6, h: 1.4, align: "center",
      valign: "top", margin: 0, isTextBox: true });
  } else if (sl.type === "figure") {
    const h = image(s, sl.img, { x: M, y: TOP + 0.05, w: W - 2 * M, h: BOT - TOP - 0.75 }, sl.alt, dir);
    s.addText(runs(sl.caption, { fontSize: 14, color: C.text2 }), { x: M, y: TOP + 0.2 + h, w: W - 2 * M, h: 0.6,
      margin: 0, valign: "top", isTextBox: true });
  }
}
function twoCol(s, cols) {
  const gap = 0.4, w = (W - 2 * M - gap) / 2;
  cols.forEach(([head, items], i) => {
    const x = M + i * (w + gap);
    s.addShape(pres.shapes.RECTANGLE, { x, y: TOP + 0.05, w, h: BOT - TOP - 0.05, fill: { color: C.background1 },
      line: { color: "D9D6D0", width: 0.75 }, objectName: "panel " + head });
    s.addShape(pres.shapes.RECTANGLE, { x, y: TOP + 0.05, w, h: 0.7, fill: { color: i ? C.text2 : C.accent1 },
      line: { color: i ? C.text2 : C.accent1, width: 0 }, objectName: "panel head " + head });
    s.addText(head, { x: x + 0.3, y: TOP + 0.05, w: w - 0.6, h: 0.7, fontSize: 20, bold: true, color: C.background1,
      margin: 0, valign: "middle", isTextBox: true });
    bullets(s, items, { x: x + 0.3, y: TOP + 1.0, w: w - 0.6, h: BOT - TOP - 1.25 }, { fs: 20, gap: 16 });
  });
}
function next(wk) {
  const s = pres.addSlide({ masterName: "NEXT", sectionTitle: `Week ${wk.n}` });
  s.addText(wk.nextTitle || "Next update", { placeholder: "title" });
  s.addText(`Week ${wk.n} · ${wk.short}`, { placeholder: "tag" });
  twoCol(s, [[wk.nextHead || "Coming next", wk.next], ["Input we'd like", wk.asks]]);
}

// ---- content -------------------------------------------------------------------------------
const CO2 = "kgCO₂e/m²";
const WEEKS = [
  { n: 1, date: "Nov 9", short: "Data & setup", topic: "Data, ground truth and experiment setup",
    take: [["292", "buildings with an enclosure A1–A3 reference value (Benke et al. 2025)"],
           ["78", `median ${CO2} floor area; range 0.5–514`],
           ["15.5%", "of all enclosure carbon comes from XPS insulation alone"]],
    slides: [
      { type: "stats", title: "Ground truth: enclosure A1–A3 per m² of floor area",
        stats: [["55,807", "material rows: Shell – Enclosure, stage A1–A3"], ["243 + 49", "new construction + renovations"],
                ["19%", "median share of whole-building A–C carbon"]],
        bullets: ["**Source:** harmonized North American WBLCA dataset (Benke et al. 2025, CC BY 4.0), 48 early-stage features per project.",
                  "**Normalization:** conditioned floor area; renovated + added GFA for renovations. This reproduces the dataset's own normalization for all 292 projects.",
                  "**Scope:** the enclosure includes windows, doors and roofs. The unit is per m² of floor area, because wall area is missing for most projects (the proposal planned per m² of wall)."] },
      { type: "figtext", title: "What enclosure carbon is made of", img: "fig_composition.png", imgW: 6.9,
        alt: "Bar chart of enclosure A1-A3 GWP share by material group",
        bullets: ["**Insulation (26.4%) and aluminum (22.0%)** dominate.",
                  "**XPS: 43.6 kgCO₂e/kg**, against 1.2 for mineral wool and 3.1 for polyiso: the HFC-blown product that Tally and One Click LCA modelled in the assessment years.",
                  "**149 of 292** projects contain XPS.",
                  "**Data quality:** 10 new-construction projects have no fenestration GWP at all, several with a WWR of 0.5–0.7. They are flagged, and results are reported with and without them."] },
      { type: "flow", title: "LLM experiment protocol",
        steps: ["**48 features** per building", "**Task file:** system prompt, glossary, 48–49 buildings",
                "**Claude Opus 5.5** subagent, medium effort; no web, code or ground truth", "**Answer:** RANGE low – high → midpoint",
                "**Metrics** against the reference LCA"],
        bullets: ["**3 runs × 292 buildings** = 876 estimates per prompt. Seeded shuffles; identical chunks across prompt versions, so comparisons are paired building by building.",
                  "**Metrics:** ±20% coverage (Wilson CI), RMSE, median APE, median |log(est/ref)|, bias (geometric mean of est/ref), CV across runs.",
                  "**Parser change:** a lower bound of 0 is accepted. Renovations that leave the envelope untouched have reference values near zero, and the course parser would have dropped exactly those answers."] },
    ],
    next: ["**Baseline results** with a plain prompt (the model's own knowledge, prompt v1).",
           "**Error analysis:** where the model under- and overestimates, and why."],
    asks: ["Is **per m² of floor area** acceptable as the functional unit, instead of per m² of wall?",
           "Keep the **10 flagged incomplete references** in the main metrics (we report both ways)?"] },

  { n: 2, date: "Nov 16", short: "Baseline & error analysis", topic: "Baseline (prompt v1) and error analysis",
    take: [["19.5%", "of estimates fall within ±20% of the reference LCA"],
           ["0.75", "bias: estimates are about 25% low on average"],
           ["0.46", "log–log slope: every building is pulled toward a typical value"]],
    slides: [
      { type: "figtext", title: "Baseline: a plain prompt, the model's own knowledge", img: "fig_scatter_v1.png", wfig: true, imgW: 5.6,
        alt: "Scatter of v1 estimate vs reference, log axes",
        bullets: ["**Coverage 19.5%** (CI 15.4–24.5%), RMSE 79.7, median APE 37.9%, CV 19.0% across runs.",
                  "**63%** of buildings are underestimated beyond the band; 17.5% are overestimated.",
                  "The **20 largest errors**, all underestimates, carry 68% of the squared error."], fs: 19 },
      { type: "figtext", title: "Main pattern: compression, not uniform underestimation", img: "fig_bins_v1.png", wfig: true, imgW: 6.4,
        alt: "Median estimate/reference by reference bin, prompt v1",
        bullets: ["Below 25 " + CO2 + ": overestimated **1.58×**. Above 200: estimated at **0.28×**.",
                  "The model leans on **geometry**: the envelope-to-floor ratio correlates 0.62 with the log estimate but only 0.39 with the log reference.",
                  "What it misses is **carbon per m² of envelope** (r = −0.79 with the log error). That is set by assembly and material choices, and **no feature describes the wall assembly**."] },
      { type: "figtext", title: "Why the model underestimates", img: "fig_diagnostics_v1.png", wfig: true, imgW: 5.8, numbered: true, fs: 15,
        alt: "Median estimate/reference by subgroup, prompt v1",
        bullets: ["**HFC-blown XPS is never considered:** 0.6% of answers mention XPS. Ratio 0.67 with XPS vs 0.80 without; removing XPS from the reference moves 0.72 → 0.84, about **half the bias**.",
                  "**The climate gap is an insulation effect:** cold zones 0.65, warm 0.77. XPS is in 65–68% of zone 5A/5B projects but 26–33% of zone 3B/3C.",
                  "**Missing envelope area:** 0.81 when given, 0.65 when the model must estimate it.",
                  "**Curtain-wall tail and renovations:** single projects reach 300 from curtain wall alone; 60% of major renovations are underestimated.",
                  "**Scope wording** was narrower than the dataset's enclosure (11% of enclosure GWP is tagged \"Superstructure\" in the source tool)."] },
      { type: "stats", title: "Why the model overestimates",
        stats: [["3.09×", "median estimate/reference for the 10 incomplete references"], ["10", "projects with no fenestration GWP, flagged"],
                ["Fit-outs", "and minor renovations: envelope scope unknown from the features"]],
        bullets: ["The **largest overestimates trace back to incomplete reference LCAs**, not to the model.",
                  "The remaining overestimates are mostly fit-outs and minor renovations, where the extent of envelope work is not described by any feature.",
                  "Flagged projects: 27, 35, 66, 74, 80, 91, 141, 217, 234, 264."] },
    ],
    next: ["**Prompt v2:** add the missing knowledge. A scope matching the dataset, a component take-off, named high-carbon materials, and a renovation rule.",
           "Rerun 3 × 292 and compare **paired** with v1."],
    asks: ["Feedback on the **error taxonomy** before we revise the prompt.",
           "Any **domain knowledge** you would add to the prompt?"] },

  { n: 3, date: "Nov 23", short: "Prompt v2", topic: "Prompt v2: adding qualitative knowledge",
    take: [["13.8%", "run-to-run CV (v1 19.0%): more consistent"],
           ["15.1%", "coverage (v1 19.5%): less accurate"],
           ["89%", "of v2 answers still assume polyiso roof insulation"]],
    slides: [
      { type: "cards", title: "What prompt v2 changed", cardFs: 18,
        cards: [["Scope", "Written to match the dataset's enclosure definition."],
                ["Component take-off", "Areas → assemblies → intensities → total."],
                ["High-carbon materials", "HFC-blown XPS \"ten times or more\" the GWP of other insulation per unit R; aluminum curtain wall 100–200 " + CO2 + "."],
                ["No anchoring", "Estimating from a \"typical building\" is ruled out."],
                ["Renovation rule", "Count only the materials of the envelope work."],
                ["BEST value", "A best estimate is requested alongside the range."]] },
      { type: "tablefig", title: "Results: v2 vs v1 (292 buildings, 3 runs each)", tw: 6.6,
        colW: [1.0, 1.25, 0.8, 1.05, 0.95, 0.7, 0.85], wfig: true, img: "fig_bins_v1_v2.png", alt: "Median ratio by bin, v1 and v2",
        head: ["Prompt", "Coverage", "RMSE", "Med. APE", "Med. |log|", "Bias", "CV"],
        rows: [["v1", "19.5%", "79.7", "37.9%", "0.456", "0.75", "19.0%"], ["v2", "15.1%", "81.0", "44.3%", "0.563", "0.67", "13.8%"]],
        bullets: ["v2 errors are **significantly larger** (Wilcoxon p < 0.0001).",
                  "Compression eased (slope 0.46 → 0.55), but the **whole curve shifted down**.",
                  "More consistent across runs: CV 19.0% → 13.8%."] },
      { type: "figtext", title: "Why v2 got worse", img: "fig_diagnostics_v1_v2.png", wfig: true, imgW: 6.0, numbered: true,
        alt: "Median ratio by subgroup, v1 and v2",
        bullets: ["**The facts were repeated, not applied.** XPS was named 50× more often, but 89% of answers still assumed polyiso roofs; the median roof intensity stayed at 35 " + CO2 + ".",
                  "**The take-offs were too light.** Bottom-up intensities came out at 66.8 per m² of envelope, against 86.7 in the reference.",
                  "**A subtracting rule hurt.** \"Count only new materials\" dropped minor renovations from 0.85 to 0.56."] },
      { type: "quote", title: "Lesson for prompt design",
        quote: "Qualitative knowledge gets repeated, not applied. To move the numbers, give numbers, at the step where the model chooses them.",
        sub: "This is the design principle behind **prompt v3**." },
    ],
    next: ["**Prompt v3:** sourced quantitative anchors. A table of external A1–A3 intensities per m² of component, placed at the decision step.",
           "**Held-out check** on buildings not used for the prompt diagnostics."],
    asks: ["Sources for intensities: CLF baselines, PCI and Kawneer EPDs, RDH studies. **None from the ground-truth dataset or the CLF WBLCA benchmark** (leakage). Any to add or avoid?"] },

  { n: 4, date: "Nov 30", short: "Prompt v3 & held-out", topic: "Prompt v3 and a held-out check",
    take: [["25.0%", "coverage (v1 19.5%, v2 15.1%)"],
           ["0.86", "bias (v1 0.75): half of the underestimate removed"],
           ["12.5%", "run-to-run CV (v1 19.0%)"]],
    slides: [
      { type: "cards", title: "What prompt v3 adds (on top of the v2 scope and method)", cols: 2, cardFs: 17,
        cards: [["Sourced intensity table", "A1–A3 per m² of component, compiled by a separate research subagent from external sources (CLF 2025 baselines, PCI, Kawneer, RDH); **excludes the ground-truth dataset**. Placed at the step where numbers are chosen."],
                ["XPS modelling convention", "LCA tools of the period often used **HFC-blown XPS** for roofs."],
                ["Sanity check", "Roughly **50 " + CO2 + " of envelope** as a cross-check of the total."],
                ["Renovation rule", "Rewritten so that it **no longer subtracts** by default."]] },
      { type: "tablefig", title: "Results: all three prompts (292 buildings, 3 runs each)", tw: 7.3,
        colW: [1.0, 1.4, 0.85, 1.1, 1.1, 0.8, 1.05], boldRows: [2],
        head: ["Prompt", "Coverage", "RMSE", "Med. APE", "Med. |log|", "Bias", "CV"],
        rows: [["v1", "19.5%", "79.7", "37.9%", "0.456", "0.75", "19.0%"], ["v2", "15.1%", "81.0", "44.3%", "0.563", "0.67", "13.8%"],
               ["v3", "25.0%", "76.0", "40.0%", "0.426", "0.86", "12.5%"]],
        img: "fig_bins.png", alt: "Median ratio by bin for v1, v2, v3",
        bullets: ["v3 vs v2: **significant** (p = 0.002). v3 vs v1: consistent but **borderline** (McNemar p = 0.085, Wilcoxon p = 0.053).",
                  "HFC-XPS is now considered in **96%** of answers for projects with XPS.",
                  "Unbiased now: the non-XPS part (0.99), buildings with a given envelope area (0.99), warm zones (0.98)."] },
      { type: "figtext", title: "What is still wrong", img: "fig_scatter_v1_v3.png", imgW: 7.6,
        alt: "Scatter of v1 and v3 estimates vs reference",
        bullets: ["**Compression at the top:** 0.38 above 200 " + CO2 + ".",
                  "**Light enclosures** are overestimated more (1.31 in the 25–50 bin).",
                  "**Renovations** remain hard: the extent of envelope work is not in the features."], fs: 18 },
      { type: "figtext", title: "Held-out check: 88 test buildings", img: "fig_prompts.png", imgW: 6.6, fs: 15,
        alt: "Coverage and median log error for all 292 and test 88",
        bullets: ["**No external test set fits:** the CLF benchmark probably shares source models; CarbEnMats has 172 European buildings, a different element definition and no geometry.",
                  "**Split:** 88 test / 204 dev, stratified on project type × climate (seed 226). It was **assigned after the runs**, so we re-ran every diagnostic on dev only, and all findings replicate (slope 0.44, XPS 14.7%, area effect 0.79 vs 0.65, polyiso 89%).",
                  "**Test:** v3 26.1% vs v1 20.5% coverage, RMSE 69.2 vs 74.1, bias 0.86 vs 0.75. Median |log| unchanged (0.400 vs 0.393); **not significant** at this size (p = 0.41)."] },
    ],
    next: ["**Feature study:** which inputs does the model actually need?",
           "**LEED v5:** what the accuracy means for MRp2 and MRc2.",
           "Final deliverables: paper, final prompt, poster."],
    asks: ["Is the **post-hoc split with dev-only replication** acceptable, or should we collect additional projects?"] },

  { n: 5, date: "Dec 7", short: "Features, LEED & deliverables", topic: "Features, LEED v5 and deliverables",
    take: [["10", "early-design features are as good as all 48"],
           ["7×", "prompt content moved the error 7× more than any feature set"],
           ["≈ 6%", "of whole-building carbon from a 30% enclosure cut"]],
    slides: [
      { type: "tablefig", title: "Feature study: 10 inputs are enough (v3, run 0)", tw: 6.4,
        colW: [1.05, 0.65, 1.05, 1.2, 0.85, 0.65, 0.95],
        head: ["Set", "n", "Coverage", "Med. |log|", "Δ", "p", "Bias"],
        rows: [["all", "48", "24.3%", "0.461", "–", "–", "0.86"], ["early", "39", "21.6%", "0.462", "+0.001", "0.13", "0.88"],
               ["env", "15", "19.9%", "0.463", "+0.001", "0.33", "0.93"], ["min", "10", "25.3%", "0.476", "+0.015", "0.81", "0.81"],
               ["no-lca", "40", "25.3%", "0.441", "−0.020", "0.57", "0.90"], ["no-mass", "47", "22.6%", "0.452", "−0.009", "0.92", "0.85"]],
        img: "feature_study.png", alt: "Feature study: change in median log error by feature set",
        bullets: ["No set differs significantly from all 48; every difference is within v3's run-to-run spread (±0.025).",
                  "The model does **not depend on mass_total** or other LCA-derived fields.",
                  "One run per set; 7 of 9 planned ablations were stopped to limit cost."] },
      { type: "figure", title: "Where the estimate fits in LEED v5", img: "fig_leed.png",
        alt: "Diagram: envelope life cycle, LCA and LLM estimates, LEED v5 MRp2 and MRc2 workflow",
        caption: "The study boundary is A1–A3. A reference LCA and the LLM estimate both produce enclosure results that feed **MRp2** (quantify, hotspots) and **MRc2** (reduce against a baseline). The LLM screens; an LCA documents." },
      { type: "cards", title: "LEED v5: screening yes, credit documentation no", cardFs: 17,
        cards: [["MRp2: hotspots", "Bias is small (−14%; near zero without XPS), and the reasoning names the real drivers: curtain wall and framing, HFC-XPS, metal panels, glazing. **Suited to schematic-design screening.**"],
                ["MRc2: reductions", "CV 12.5%, median error ≈ 35–40%, coverage 1 in 4: as large as typical documented reductions. **Cannot document a credit-level reduction.** Paired comparison of alternatives is the promising, untested use."],
                ["Option 1: dilution", "The enclosure is a median **19%** of whole-building A–C, so a 30% enclosure cut ≈ **6%** of the building. Envelope choices work best together with structure, or via Option 2 EPDs."]] },
      { type: "cards", title: "Deliverables and limitations", cols: 2, cardFs: 17,
        cards: [["Final prompt (v3)", "Full text in the paper's appendix, with the sourced intensity table."],
                ["Paper, reports, poster", "ICML-style paper, English and Chinese reports, PPT poster; all code and results in the GitHub repo."],
                ["Limitations", "Answers in one task file share a context; post-hoc split; v3–v1 gain borderline with 3 runs; feature study one run; per m² floor area; uneven reference quality; one model."],
                ["Future work", "Assembly-type inputs; paired alternative comparison; hotspot-agreement test; an external test set."]] },
    ],
    nextTitle: "Wrap-up", nextHead: "Take-aways",
    next: ["An LLM's error is **structured**: compression and material blind spots, which error analysis can locate.",
           "**Sourced numbers at the decision step** work; qualitative knowledge does not.",
           "For LEED v5: **screening and comparison**, verified by an LCA."],
    asks: ["Feedback on the paper and poster before final submission.",
           "Interest in the **assembly-type** follow-up?"] },
];

WEEKS.forEach(wk => { pres.addSection({ title: `Week ${wk.n}` }); cover(wk); wk.slides.forEach(sl => content(wk, sl)); next(wk); });

(async () => {
  const out = path.resolve(__dirname, "weekly_updates.pptx");
  await pres.writeFile({ fileName: out });
  // pptxgenjs writes an <a:pPr> before every run of a mixed-format paragraph; keep only the first.
  const JSZip = require("jszip");
  const zip = await JSZip.loadAsync(fs.readFileSync(out));
  for (const name of Object.keys(zip.files).filter(n => /^ppt\/slides\/slide\d+\.xml$/.test(n))) {
    let xml = await zip.file(name).async("string");
    xml = xml.replace(/(<\/a:r>)<a:pPr\b[^>]*?(?:\/>|>[\s\S]*?<\/a:pPr>)/g, "$1");
    zip.file(name, xml);
  }
  fs.writeFileSync(out, await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" }));
  if (SKILL) {
    const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));
    await applyTheme(out, THEME);
  }
  fs.writeFileSync(path.resolve(__dirname, "slide_counts.json"),
    JSON.stringify(WEEKS.map(w => ({ week: w.n, date: w.date, slides: w.slides.length + 2 }))));
  console.log("wrote", out);
})();
