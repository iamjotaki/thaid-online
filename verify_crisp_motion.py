import asyncio
import json
from playwright.async_api import async_playwright

async def verify_crisp_motion():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        print("Navigating to live https://thaid.online ...")
        await page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        
        scroll_points = [0, 250, 500]
        results = []
        for y in scroll_points:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(300)
            
            data = await page.evaluate("""() => {
                const card = document.querySelector('.orbit-card-scatter');
                return {
                    scrollY: window.scrollY,
                    cardFilter: card ? window.getComputedStyle(card).filter : null,
                    cardOpacity: card ? window.getComputedStyle(card).opacity : null,
                    cardScale: card ? window.getComputedStyle(card).scale : null,
                };
            }""")
            results.append(data)
            await page.screenshot(path=f"C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/thaid_crisp_scroll_{y}.png")
            print(f"Scroll {y}px:", data)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_crisp_motion())
