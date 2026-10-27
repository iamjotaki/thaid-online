import asyncio
import json
from playwright.async_api import async_playwright

async def inspect_accent_css():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://fastwork.com', wait_until='networkidle')

        accent_styles = await page.evaluate("""() => {
            const rules = [];
            for (const sheet of Array.from(document.styleSheets)) {
                try {
                    for (const rule of Array.from(sheet.cssRules || [])) {
                        if (rule.selectorText && (
                            rule.selectorText.includes('script-accent') || 
                            rule.selectorText.includes('accent-svg') ||
                            rule.selectorText.includes('accent-path')
                        )) {
                            rules.push({
                                selector: rule.selectorText,
                                cssText: rule.cssText
                            });
                        }
                    }
                } catch (e) {}
            }
            return rules;
        }""")

        with open("fastwork_accent_css.json", "w", encoding="utf-8") as f:
            json.dump(accent_styles, f, indent=2, ensure_ascii=False)
        print(f"Found {len(accent_styles)} accent CSS rules.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect_accent_css())
