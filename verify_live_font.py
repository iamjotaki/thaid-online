import asyncio
import json
from playwright.async_api import async_playwright

async def verify_live():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://thaid.online", wait_until="networkidle")
        await page.wait_for_timeout(1500)

        info = await page.evaluate("""() => {
            const getF = (sel) => {
                const el = document.querySelector(sel);
                if (!el) return null;
                const cs = window.getComputedStyle(el);
                return {
                    fontFamily: cs.fontFamily,
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight
                };
            };

            const loadedFonts = Array.from(document.fonts).map(f => ({
                family: f.family,
                status: f.status,
                weight: f.weight,
                style: f.style
            }));

            return {
                body: getF('body'),
                h1: getF('h1'),
                p: getF('p'),
                button: getF('button'),
                loadedGoogleSans: loadedFonts.filter(f => f.family.includes('Google Sans') && f.status === 'loaded')
            };
        }""")

        print(json.dumps(info, indent=2, ensure_ascii=False))
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_fastwork_font.png")
        print("Captured live screenshot")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_live())
