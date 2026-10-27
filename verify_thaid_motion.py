import asyncio
import json
from playwright.async_api import async_playwright

async def verify_thaid_motion():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        print("Navigating to live https://thaid.online ...")
        await page.goto("https://thaid.online", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        
        # Test scroll states and capture screenshots
        scroll_points = [0, 250, 500, 750, 1100]
        motion_log = []
        
        for y in scroll_points:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(400)
            
            data = await page.evaluate("""() => {
                const hero = document.querySelector('.hero-sticky');
                const card = document.querySelector('.orbit-card-scatter');
                const copy = document.querySelector('.hero-copy-scatter');
                
                return {
                    scrollY: window.scrollY,
                    exitOpacity: hero ? window.getComputedStyle(hero).getPropertyValue('--exit-opacity') : null,
                    exitScatter: hero ? window.getComputedStyle(hero).getPropertyValue('--exit-scatter') : null,
                    cardTransform: card ? window.getComputedStyle(card).transform : null,
                    cardOpacity: card ? window.getComputedStyle(card).opacity : null,
                    cardScale: card ? window.getComputedStyle(card).scale : null,
                    copyOpacity: copy ? window.getComputedStyle(copy).opacity : null,
                };
            }""")
            
            motion_log.append(data)
            screenshot_path = f"C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/thaid_motion_scroll_{y}.png"
            await page.screenshot(path=screenshot_path)
            print(f"Captured scroll {y}px: {data}")
            
        with open("thaid_motion_verified.json", "w", encoding="utf-8") as f:
            json.dump(motion_log, f, indent=2)
            
        await browser.close()
        print("Verification complete!")

if __name__ == "__main__":
    asyncio.run(verify_thaid_motion())
