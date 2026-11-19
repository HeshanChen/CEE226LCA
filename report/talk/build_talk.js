// build_talk.js - 3-slide talk (4-5 minutes): envelope, whole building, results.
// English and Chinese scripts are in each slide's speaker notes and on two backup slides at the end.
// Uses v1-v5 (enclosure) and wb5 (whole building); the later wb6 is deliberately not used.
// Run: NODE_PATH=<dir with pptxgenjs,jszip> PPTX_SKILL=<pptx skill dir> node report/talk/build_talk.js
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const SKILL = process.env.PPTX_SKILL || "";
const FIG = path.resolve(__dirname, "../figures");
const WFIG = path.resolve(__dirname, "../weekly/figures");

const THEME = { name: "Stanford Cardinal", headFontFace: "Cambria", bodyFontFace: "Arial",
  colors: { dk1: "1A1A1A", lt1: "FFFFFF", dk2: "4D4F53", lt2: "F4F1EE", accent1: "8C1515", accent2: "B1040E",
            accent3: "2A78D6", accent4: "EDA100", accent5: "175E54", accent6: "820000", hlink: "8C1515", folHlink: "820000" } };
const HEX = THEME.colors;
const W = 13.333, M = 0.6, TOP = 1.45, BOT = 6.8;
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "LLM estimates of embodied carbon - CEE226 Group 8";
pres.author = "CEE226 Group 8";
const C = pres.SchemeColor;

// ---- layout -------------------------------------------------------------------------------
pres.defineSlideMaster({
  title: "CONTENT", background: { color: C.background1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M, y: 0.35, w: 12.1, h: 0.8, fontFace: THEME.headFontFace,
      fontSize: 28, bold: true, color: C.accent1, margin: 0, valign: "middle", align: "left" }, text: "" } },
    { text: { text: "CEE226 Group 8 · LLM estimates of embodied carbon · Benke et al. (2025) dataset, 292 buildings",
      options: { x: M, y: 7.0, w: 9, h: 0.3, fontSize: 10, color: C.text2, margin: 0, valign: "middle" } } },
    { placeholder: { options: { name: "tag", type: "body", x: 9.7, y: 7.0, w: 2.5, h: 0.3, fontSize: 10, color: C.text2,
      align: "right", valign: "middle", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 12.35, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.text2, align: "right" },
});

// ---- helpers --------------------------------------------------------------------------------
function pngSize(file) { const b = fs.readFileSync(file); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }
function runs(s, base = {}) {                  // "**bold** text" -> runs
  return s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(p => {
    const b = p.startsWith("**");
    return { text: b ? p.slice(2, -2) : p, options: { ...base, bold: b || !!base.bold } };
  });
}
function bullets(s, items, box, { fs = 15, gap = 6, color = C.text1 } = {}) {
  const out = [];
  items.forEach((it, i) => {
    const r = runs(it, { fontSize: fs, color });
    r[0].options.bullet = { indent: 16 };
    r[0].options.paraSpaceAfter = gap;
    if (i < items.length - 1) r[r.length - 1].options.breakLine = true;
    out.push(...r);
  });
  s.addText(out, { ...box, margin: 0, valign: "top", isTextBox: true, objectName: "bullets" });
}
function h3(s, text, box) {
  s.addText(text, { ...box, fontSize: 17, bold: true, color: C.accent1, margin: 0, valign: "bottom", isTextBox: true });
}
function image(s, file, box, alt, dir = FIG) {
  const p = path.join(dir, file);
  const [pw, ph] = pngSize(p);
  let w = box.w, h = w * ph / pw;
  if (h > box.h) { h = box.h; w = h * pw / ph; }
  s.addImage({ path: p, x: box.x + (box.w - w) / 2, y: box.y, w, h, altText: alt, objectName: file });
  return h;
}
function chartOpts(title, max) {
  return { showTitle: true, title, titleFontSize: 14, titleColor: HEX.dk1, titleFontFace: "+mn-lt",
    barGrouping: "stacked", barGapWidthPct: 45, showValue: true, dataLabelPosition: "inEnd",
    dataLabelColor: "FFFFFF", dataLabelFontSize: 12, dataLabelFontBold: true, dataLabelFontFace: "+mn-lt",
    dataLabelFormatCode: '0.0"%"', valAxisMinVal: 0, valAxisMaxVal: max, valAxisMajorUnit: 10,
    valAxisLabelFormatCode: '0"%"', valAxisLabelFontSize: 10, valAxisLabelColor: HEX.dk2, valAxisLabelFontFace: "+mn-lt",
    catAxisLabelFontSize: 11, catAxisLabelColor: HEX.dk1, catAxisLabelFontFace: "+mn-lt",
    valGridLine: { color: "E3DFDA", size: 0.75 }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "b", legendFontSize: 10, legendColor: HEX.dk2, legendFontFace: "+mn-lt" };
}

// ---- scripts ------------------------------------------------------------------------------------
const EN = [
  `Our question: can a large language model estimate the embodied carbon of a building's envelope at early design, before any LCA exists? We used the 292 North American buildings of the Benke et al. 2025 dataset. For each building, Claude Opus 5.5 gets 48 early-design features and gives a range for the cradle-to-gate carbon of the enclosure, per square metre of floor. A hit means the reference LCA lies within plus or minus 20 percent of the estimate.

Before scoring, we set aside 30 buildings whose reference data cannot be estimated: LCAs that never assessed the enclosure, new buildings with no glass in the inventory, and renovations where a little enclosure work is spread over the whole floor area.

With a plain prompt, only 19.5 percent were hits. The figure shows why: the model pulls every building toward a typical value, so light envelopes are overestimated and heavy ones underestimated three to four times. It also never considered HFC-blown XPS insulation, which alone is 15 percent of enclosure carbon.

So we changed the prompt step by step. More qualitative instructions made it worse. Giving sourced component numbers at the step where the model picks them raised it to 25 percent. Weighing the model's own take-off equally against a benchmark, the median of similar buildings by use, raised it to 32. Finally, as the course asked, we fitted the tables to the reference data: 35.6 percent.`,
  `The course reference results are for the whole building, stages A to C, so we applied the same idea to that target. The prompt builds three estimates. First, the model's own estimate, element by element: 20 percent of the weight. Second, a mass route: the total material mass per square metre of floor times a carbon factor per kilogram, about 0.37 for concrete structures and 0.49 for steel: 50 percent. Third, a benchmark by use and structural material: 30 percent.

The whole building is easier than the envelope. Its values are less spread out, and the material mass nearly fixes the result. One caveat: that mass comes from the reference LCA itself, so it would not be known at early design, and the tables were fitted to the data.

In the figure, each row is a building, sorted by its reference value; green means a hit. The model's own estimate alone gets 44.5 percent. The three combined get 53.4.`,
  `To sum up. On the envelope, coverage rose from 19.5 percent with the plain prompt to 32.2 with weighted evidence and 35.6 with the fitted prompt, 38.5 without the 30 outliers. For scale: one constant for every building covers 27 percent, and a machine-learning model trained on this dataset reaches only 26 to 34 percent on unseen buildings. So the features cap the envelope at about a third, and our prompt reaches that cap. On 88 held-out buildings, the version whose benchmark never saw them covers 35.2 percent, so the gain carries over.

On the whole building, we reach 53.4 percent, against 34 to 46 percent in the course reference results.

Three lessons. One: the model's errors are structured, so reading its reasoning tells you which fix to make. Two: give numbers at the step where the model chooses them; general advice and long documents did not help. Three: to go further on the envelope, the model needs what the features lack, the wall and insulation assembly. Thank you.`];
const ZH = [
  `我们的问题是：在早期设计阶段、还没有任何 LCA 的时候，大语言模型能不能估出建筑外围护结构的隐含碳？我们用的是 Benke 等人 2025 年数据集里的 292 栋北美建筑。每栋楼，模型 Claude Opus 5.5 拿到 48 个早期设计特征，给出围护结构从摇篮到大门阶段、每平米楼面的碳排范围。如果参考 LCA 的数值落在估算值正负 20% 以内，就算命中。

打分之前，我们先剔除了 30 栋参考数据本身没法估的楼：有的 LCA 根本没评估围护，有的新建楼清单里没有玻璃，还有的改造项目只动了一点围护，却除以了整栋楼的面积。

用最简单的 prompt，只有 19.5% 命中。图上能看到原因：模型把所有楼都往一个典型值拉，轻的围护被高估，重的被低估三到四倍。它还完全没考虑 HFC 发泡的 XPS 保温，而光这一种材料就占围护碳排的 15%。

所以我们一步步改 prompt。加更多定性的指导反而更差；在模型选数字的那一步直接给出有出处的构件数值，提高到 25%；把模型自己的估算和同用途建筑的中位数，也就是 benchmark，各占一半，提高到 32%；最后按课程要求，用参考数据拟合表格，到 35.6%。`,
  `课程的参考结果针对的是整楼 A 到 C 阶段，所以我们把同样的思路用到这个目标上。Prompt 让模型做三个估算：第一，模型自己按构件逐项估，占 20%；第二，质量估算：每平米楼面的材料总质量，乘以每公斤的碳排系数，混凝土结构大约 0.37，钢结构 0.49，占 50%；第三，按用途和结构材料的 benchmark，占 30%。

整楼比围护容易：数值没那么分散，而且材料质量基本决定了结果。需要说明的是，这个质量来自参考 LCA 本身，早期设计时其实拿不到，而且表格是用数据拟合的。

图里每一行是一栋楼，按参考值从低到高排，绿色表示命中。只用模型自己的估算是 44.5%，三个合起来是 53.4%。`,
  `总结一下。围护结构上，命中率从最简单 prompt 的 19.5%，到加权证据的 32.2%，再到拟合后的 35.6%；去掉 30 个 outlier 是 38.5%。做个参照：所有楼都猜同一个数能命中 27%；用这个数据集训练的机器学习模型，在没见过的楼上也只有 26% 到 34%。所以这些特征本身就把围护的上限卡在三分之一左右，我们的 prompt 达到了这个上限。在 88 栋留出的测试楼上，benchmark 从没见过这些楼的版本命中 35.2%，说明提升能迁移到新楼上。

整楼上我们达到 53.4%，课程参考结果是 34% 到 46%。

三点体会：第一，模型的错误是有规律的，读它的推理过程就知道该改哪里；第二，在模型选数字的那一步直接给数字，泛泛的指导和长篇文献没有用；第三，围护要再往上走，模型需要特征里没有的信息，也就是墙体和保温的构造。谢谢大家。`];
const TIME = ["1:45", "1:20", "1:30"];
const TIME_ZH = ["约 1 分 45 秒", "约 1 分 20 秒", "约 1 分 30 秒"];
function notes(s, i) {
  s.addNotes(`EN (about ${TIME[i]})\n\n${EN[i]}\n\n中文（${TIME_ZH[i]}）\n\n${ZH[i]}`);
}

// ---- slide 1: envelope ----------------------------------------------------------------------
let s = pres.addSlide({ masterName: "CONTENT" });
s.addText("Envelope: the model compresses, the prompt corrects it", { placeholder: "title" });
s.addText("1 · Envelope (A1–A3)", { placeholder: "tag" });
s.addShape(pres.shapes.RECTANGLE, { x: M, y: TOP, w: W - 2 * M, h: 0.72, fill: { color: C.background2 },
  line: { color: C.background2, width: 0 }, objectName: "task strip" });
s.addText(runs("**Task:** 48 early-design features → enclosure carbon, A1–A3, kgCO₂e per m² floor · Claude Opus 5.5 · " +
  "**hit** = reference LCA within ±20% of the estimate · **30 outliers set aside** (LCA without the enclosure, no glass modelled, partial renovations)",
  { fontSize: 14, color: C.text1 }), { x: M + 0.2, y: TOP + 0.04, w: W - 2 * M - 0.4, h: 0.64, margin: 0, valign: "middle",
  isTextBox: true });
const LW = 5.9, RX = M + LW + 0.45, RW = W - M - RX;
h3(s, "Plain prompt (v1): 19.5% hits", { x: M, y: 2.35, w: LW, h: 0.4 });
bullets(s, ["**Compression:** light envelopes overestimated, heavy ones underestimated 3–4×.",
  "**Blind spot:** never considers HFC-blown XPS insulation, 15.5% of all enclosure carbon."],
  { x: M, y: 2.85, w: LW, h: 1.0 }, { fs: 14, gap: 4 });
image(s, "fig_bins_v1.png", { x: M, y: 3.9, w: LW, h: 2.85 }, "Median estimate over reference by reference bin for prompt v1: falls from 1.6 below 25 to 0.29 above 200", WFIG);
h3(s, "How the prompt changed (coverage, all 292)", { x: RX, y: 2.35, w: RW, h: 0.4 });
const steps = [
  ["v1", "Plain prompt, innate knowledge", "19.5%", false],
  ["v2", "+ qualitative method advice: worse", "15.1%", false],
  ["v3", "+ sourced component numbers where the model picks them", "25.0%", false],
  ["v4", "own take-off 50% + **benchmark** by use 50% (held-out: 35.2%)", "32.2%", true],
  ["v5", "tables fitted to the reference data (in-sample)", "35.6%", true]];
const rowH = 0.78;
steps.forEach(([v, label, num, hi], i) => {
  const y = 2.88 + i * rowH;
  s.addShape(pres.shapes.RECTANGLE, { x: RX, y, w: RW, h: rowH - 0.1, fill: { color: hi ? C.background2 : C.background1 },
    line: { color: "E3DFDA", width: 0.75 }, objectName: "step " + v });
  s.addShape(pres.shapes.OVAL, { x: RX + 0.15, y: y + (rowH - 0.1 - 0.5) / 2, w: 0.5, h: 0.5,
    fill: { color: hi ? C.accent1 : C.text2 }, line: { color: hi ? C.accent1 : C.text2, width: 0 }, objectName: "badge " + v });
  s.addText(v, { x: RX + 0.15, y: y + (rowH - 0.1 - 0.5) / 2, w: 0.5, h: 0.5, fontSize: 13, bold: true, color: C.background1,
    align: "center", valign: "middle", margin: 0, isTextBox: true });
  s.addText(runs(label, { fontSize: 14, color: C.text1 }), { x: RX + 0.8, y, w: RW - 2.05, h: rowH - 0.1, margin: 0,
    valign: "middle", isTextBox: true });
  s.addText(num, { x: RX + RW - 1.2, y, w: 1.05, h: rowH - 0.1, fontFace: THEME.headFontFace, fontSize: 22, bold: true,
    color: hi ? C.accent1 : C.text1, align: "right", valign: "middle", margin: 0, isTextBox: true });
});
notes(s, 0);

// ---- slide 2: whole building --------------------------------------------------------------------
s = pres.addSlide({ masterName: "CONTENT" });
s.addText("Whole building: the material mass carries the estimate", { placeholder: "title" });
s.addText("2 · Whole building (A–C)", { placeholder: "tag" });
const L2 = 6.3;
h3(s, "Same idea on the course's target (stages A–C)", { x: M, y: TOP, w: L2, h: 0.4 });
const ev = [["20%", "Model's own estimate", "element by element, from use, structure, size and region"],
  ["50%", "Mass route", "mass_total / floor area × carbon per kg (concrete 0.37, steel 0.49, wood 0.47 kgCO₂e/kg)"],
  ["30%", "Benchmark", "median of similar buildings by use × structural material"]];
ev.forEach(([w, head, body], i) => {
  const y = TOP + 0.52 + i * 0.95;
  s.addShape(pres.shapes.RECTANGLE, { x: M, y, w: L2, h: 0.85, fill: { color: i === 1 ? C.background2 : C.background1 },
    line: { color: "E3DFDA", width: 0.75 }, objectName: "evidence " + head });
  s.addText(w, { x: M + 0.15, y, w: 1.1, h: 0.85, fontFace: THEME.headFontFace, fontSize: 26, bold: true, color: C.accent1,
    align: "left", valign: "middle", margin: 0, isTextBox: true });
  s.addText([{ text: head, options: { fontSize: 15, bold: true, color: C.text1, breakLine: true } },
    { text: body, options: { fontSize: 13, color: C.text2 } }], { x: M + 1.3, y: y + 0.06, w: L2 - 1.45, h: 0.78, margin: 0,
    valign: "middle", isTextBox: true });
});
h3(s, "Why it is easier than the envelope", { x: M, y: 4.85, w: L2, h: 0.4 });
bullets(s, ["Values are less spread out (log standard deviation 0.66 vs 0.98).",
  "The material mass nearly fixes the result.",
  "**Caveat:** mass_total comes from the reference LCA itself, so it is not known at early design; tables fitted to the data."],
  { x: M, y: 5.35, w: L2, h: 1.45 }, { fs: 14, gap: 4 });
image(s, "fig_bands_wholebuilding.png", { x: M + L2 + 0.35, y: TOP, w: W - 2 * M - L2 - 0.35, h: BOT - TOP },
  "Band figure, whole building: the model's own estimate alone covers 44.5 percent, the three sources combined 53.4 percent");
notes(s, 1);

// ---- slide 3: results ---------------------------------------------------------------------------
s = pres.addSlide({ masterName: "CONTENT" });
s.addText("Results: 35.6% on the envelope, 53.4% on the whole building", { placeholder: "title" });
s.addText("3 · Results", { placeholder: "tag" });
const CW = (W - 2 * M - 0.4) / 2;
s.addChart(pres.charts.BAR, [
  { name: "Our prompts", labels: ["Constant", "v1", "v2", "v3", "v4", "v5 fitted"], values: [null, 19.5, 15.1, 25.0, 32.2, 35.6] },
  { name: "One constant for every building", labels: ["Constant", "v1", "v2", "v3", "v4", "v5 fitted"], values: [27.1, null, null, null, null, null] }],
  { x: M, y: TOP, w: CW, h: 3.35, barDir: "col", chartColors: [HEX.accent1, "8F8C87"],
    ...chartOpts("Envelope A1–A3: share within ±20%", 40), objectName: "envelope chart" });
s.addChart(pres.charts.BAR, [
  { name: "Ours (Claude Opus 5.5)", labels: ["Course: innate", "Course: papers", "Course: papers + ontology", "Ours"], values: [null, null, null, 53.4] },
  { name: "Course reference (Gemini, 10 runs)", labels: ["Course: innate", "Course: papers", "Course: papers + ontology", "Ours"], values: [34.2, 45.2, 45.9, null] }],
  { x: M + CW + 0.4, y: TOP, w: CW, h: 3.35, barDir: "col", chartColors: [HEX.accent1, "8F8C87"],
    ...chartOpts("Whole building A–C: share within ±20%", 60), objectName: "whole building chart" });
s.addText(runs("All 292 buildings. Cleaned set (without the 30 outliers): v5 **38.5%**. Held-out: v4, whose benchmark never saw them, covers **35.2%** of 88 unseen buildings. " +
  "v5 and the whole-building tables are fitted to the reference data (in-sample), as the course asked.", { fontSize: 12, color: C.text2 }),
  { x: M, y: TOP + 3.42, w: W - 2 * M, h: 0.45, margin: 0, valign: "top", isTextBox: true });
const lessons = [["Errors are structured", "Compression and blind spots (XPS). Reading the model's reasoning shows which fix to make."],
  ["Numbers, not advice", "Sourced numbers at the step where the model picks them help; general advice and long documents did not."],
  ["Features set the ceiling", "One constant covers 27%, a model trained on the data 26–34%. Going further needs the wall and insulation assembly."]];
const LWc = (W - 2 * M - 0.6) / 3;
lessons.forEach(([head, body], i) => {
  const x = M + i * (LWc + 0.3), y = 5.42;
  s.addShape(pres.shapes.RECTANGLE, { x, y, w: LWc, h: 1.35, fill: { color: C.background2 }, line: { color: C.background2, width: 0 },
    objectName: "lesson " + (i + 1) });
  s.addShape(pres.shapes.OVAL, { x: x + 0.15, y: y + 0.15, w: 0.42, h: 0.42, fill: { color: C.accent1 },
    line: { color: C.accent1, width: 0 }, objectName: "lesson badge " + (i + 1) });
  s.addText(String(i + 1), { x: x + 0.15, y: y + 0.15, w: 0.42, h: 0.42, fontSize: 14, bold: true, color: C.background1,
    align: "center", valign: "middle", margin: 0, isTextBox: true });
  s.addText(head, { x: x + 0.7, y: y + 0.12, w: LWc - 0.85, h: 0.48, fontSize: 15, bold: true, color: C.accent1, margin: 0,
    valign: "middle", isTextBox: true });
  s.addText(body, { x: x + 0.2, y: y + 0.62, w: LWc - 0.4, h: 0.68, fontSize: 12.5, color: C.text1, margin: 0, valign: "top",
    isTextBox: true });
});
notes(s, 2);

// ---- backup: the scripts ------------------------------------------------------------------------
function scriptSlide(title, tag, texts, heads, fs) {
  const sl = pres.addSlide({ masterName: "CONTENT" });
  sl.addText(title, { placeholder: "title" });
  sl.addText(tag, { placeholder: "tag" });
  const cw = (W - 2 * M - 0.6) / 3;
  texts.forEach((t, i) => {
    const x = M + i * (cw + 0.3);
    sl.addText(heads[i], { x, y: TOP - 0.05, w: cw, h: 0.4, fontSize: 14, bold: true, color: C.accent1, margin: 0,
      valign: "bottom", isTextBox: true });
    sl.addText(t.split("\n\n").map((p, j, a) => ({ text: p, options: { breakLine: j < a.length - 1, paraSpaceAfter: 5 } })),
      { x, y: TOP + 0.45, w: cw, h: BOT - TOP - 0.45, fontSize: fs, color: C.text1, margin: 0, valign: "top", isTextBox: true,
        objectName: "script " + (i + 1) });
  });
  sl.addNotes("Backup slide: the full speaker script, also in the notes of slides 1-3. Not presented.");
}
scriptSlide("Speaker script (English) · backup", "Backup · script EN", EN,
  [`Slide 1 · Envelope (about ${TIME[0]})`, `Slide 2 · Whole building (about ${TIME[1]})`, `Slide 3 · Results (about ${TIME[2]})`], 10.5);
scriptSlide("讲稿（中文）· 备用", "备用 · 中文讲稿", ZH,
  [`第 1 页 · 围护结构（${TIME_ZH[0]}）`, `第 2 页 · 整楼（${TIME_ZH[1]}）`, `第 3 页 · 结果（${TIME_ZH[2]}）`], 11);

(async () => {
  const out = path.resolve(__dirname, "talk.pptx");
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
  fs.writeFileSync(path.resolve(__dirname, "script.md"),
    "# Speaker script / 讲稿 (3 slides, 4-5 minutes)\n\nGenerated by `report/talk/build_talk.js`; the same text is in the speaker notes of `talk.pptx`.\n\n" +
    EN.map((t, i) => `## Slide ${i + 1} (about ${TIME[i]})\n\n### English\n\n${t}\n\n### 中文（${TIME_ZH[i]}）\n\n${ZH[i]}\n`).join("\n"));
  const words = EN.join(" ").split(/\s+/).length;
  console.log("wrote", out, `| English script ${words} words (about ${(words / 135).toFixed(1)} min at 135 wpm)`);
})();
