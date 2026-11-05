// make_report_pdf.js - render a Markdown report (with the prompt appendix inlined) to PDF.
// Usage: node report/make_report_pdf.js report_zh.md report_zh.pdf
// Needs pandoc and Playwright (Chromium). Run from the repo root or report/.
const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const DIR = __dirname;
const [src = "report_zh.md", out = "report_zh.pdf"] = process.argv.slice(2);
const zh = /zh/.test(src);

let md = fs.readFileSync(path.join(DIR, src), "utf8");
// Inline the prompt appendix (headings demoted one level) in place of the link paragraph.
const app = fs.readFileSync(path.join(DIR, "appendix_prompts.md"), "utf8")
  .replace(/^# .*\n/, "")
  .replace(/^## /gm, "### ");
md = md.replace(/(## (附录 A\. Prompt|Appendix A\. Prompts)\n\n)[^\n]*\n/, (_, h) => h + app + "\n");
// Stand-alone images become <figure> with a visible caption (gfm drops the alt text).
md = md.replace(/^!\[([^\]]*)\]\(([^)]+)\)$/gm,
  (_, cap, src) => `<figure><img src="${src}" alt=""><figcaption>${cap}</figcaption></figure>`);
// Links to other markdown files are meaningless in the PDF.
md = md.replace(/\[`?([^\]`]+\.md)`?\]\([^)]+\.md\)/g, "`$1`");

const css = `
@page { size: Letter; margin: 0.8in 0.75in 0.85in; }
:root { --cardinal: #8C1515; --ink: #1a1a1a; --muted: #555; --rule: #d9d6d0; --code: #f6f5f2; }
html { background: #fff; }
body { font-family: "Noto Serif", "DejaVu Serif", "WenQuanYi Zen Hei", serif; font-size: 10.5pt;
       line-height: 1.62; color: var(--ink); max-width: none; margin: 0; }
${zh ? 'body { font-family: "DejaVu Sans", "WenQuanYi Zen Hei", sans-serif; font-size: 10pt; }' : ""}
h1 { font-size: 19pt; line-height: 1.3; color: var(--cardinal); border-bottom: 3px solid var(--cardinal);
     padding-bottom: 8px; margin: 0 0 10px; }
h2 { font-size: 14pt; color: var(--cardinal); margin: 22px 0 8px; padding-top: 4px;
     border-top: 1px solid var(--rule); break-after: avoid; }
h3 { font-size: 11.5pt; margin: 16px 0 6px; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
a { color: var(--cardinal); text-decoration: none; }
blockquote { margin: 10px 0; padding: 6px 12px; border-left: 3px solid var(--cardinal);
             background: #faf7f6; color: var(--muted); }
code { font-family: "DejaVu Sans Mono", "WenQuanYi Zen Hei Mono", monospace; font-size: 0.86em;
       background: var(--code); padding: 0 3px; border-radius: 2px; overflow-wrap: anywhere; }
pre { background: var(--code); border: 1px solid var(--rule); padding: 8px 10px; font-size: 7.6pt;
      line-height: 1.4; white-space: pre-wrap; overflow-wrap: anywhere; }
pre code { background: none; padding: 0; font-size: inherit; }
table { border-collapse: collapse; margin: 10px 0; font-size: 8.8pt; width: 100%; break-inside: avoid; }
th, td { border-bottom: 1px solid var(--rule); padding: 3px 6px; text-align: left; vertical-align: top; }
th { border-bottom: 1.5px solid var(--ink); }
figure { margin: 14px 0; text-align: center; break-inside: avoid; }
img { max-width: 100%; max-height: 7.2in; height: auto; width: auto; display: block; margin: 0 auto; }
p:has(> img) { margin: 14px 0; break-inside: avoid; }
figcaption { font-size: 8.8pt; color: var(--muted); margin-top: 4px; }
`;

const tmp = path.join(DIR, ".pdf_build");
fs.mkdirSync(tmp, { recursive: true });
const mdPath = path.join(tmp, "in.md");
const htmlPath = path.join(DIR, "_report_render.html");
fs.writeFileSync(mdPath, md);
fs.writeFileSync(path.join(tmp, "style.css"), css);
const title = md.match(/^# (.*)$/m)[1];
execFileSync("pandoc", [mdPath, "-f", "gfm+implicit_figures", "-t", "html5", "--standalone",
  "--metadata", `pagetitle=${title}`, "--css", path.join(tmp, "style.css"),
  "--embed-resources", "--resource-path", DIR, "-o", htmlPath]);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + htmlPath, { waitUntil: "load" });
  await page.pdf({
    path: path.join(DIR, out), format: "Letter", printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: "<span></span>",
    footerTemplate: `<div style="width:100%;font-size:7.5pt;color:#777;font-family:sans-serif;padding:0 0.75in;display:flex;justify-content:space-between">
      <span>CEE226 Group 8 · Stanford University</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
  fs.rmSync(tmp, { recursive: true, force: true });
  fs.rmSync(htmlPath, { force: true });
  console.log("wrote", path.join(DIR, out));
})();
