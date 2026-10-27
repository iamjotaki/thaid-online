import asyncio
import json
from playwright.async_api import async_playwright

async def check_lang_options():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://fastwork.com", wait_until="networkidle")

        lang_btn = page.locator('.start-selling-language-switch, button[aria-label*="Language"]')
        await lang_btn.click()
        await page.wait_for_timeout(500)

        options = await page.evaluate("""() => {
            const list = Array.from(document.querySelectorAll('button, a, [role="option"], li'));
            return list.map(el => ({
                text: el.innerText,
                tag: el.tagName,
                href: el.getAttribute('href'),
                className: el.className
            })).filter(x => x.text && (x.text.includes('TH') || x.text.includes('ไทย') || x.text.includes('EN')));
        }""")

        print(json.dumps(options, indent=2, ensure_ascii=False))
        await browser.close()

if __name__ == "__main__":
    asyncio.run(check_lang_options())
