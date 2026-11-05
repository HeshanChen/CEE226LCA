// Render poster.html to poster.pdf (48x36 in) and a PNG preview. Usage: node render.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 4608, height: 3456 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(__dirname, 'poster.html'));
  await page.waitForLoadState('networkidle');
  const over = await page.evaluate(() => [...document.querySelectorAll('.col')].map(c => c.scrollHeight - c.clientHeight));
  console.log('column overflow px:', over);
  await page.pdf({ path: path.resolve(__dirname, 'poster.pdf'), width: '48in', height: '36in', printBackground: true });
  await page.screenshot({ path: path.resolve(__dirname, 'poster_preview.png'), scale: 'css' });
  await browser.close();
})();
