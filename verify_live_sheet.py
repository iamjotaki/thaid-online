import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        print("Navigating to https://thaid.online...")
        await page.goto("https://thaid.online", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # 1. Capture initial hero
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_thaid_initial.png")
        print("Captured live initial hero")

        # 2. Check Scroll Down button
        scroll_btn = page.locator('button[aria-label="Scroll down to services"]')
        is_visible = await scroll_btn.is_visible()
        print(f"Scroll down button visible on live: {is_visible}")

        # 3. Click Scroll Down button
        await scroll_btn.click()
        await page.wait_for_timeout(1500)

        post_click_scroll = await page.evaluate("() => window.scrollY")
        print(f"Live scrollY after clicking Scroll Down button: {post_click_scroll}")

        # 4. Capture after click
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_thaid_sheet_after_click.png")
        print("Captured live after-click elevated sheet")

        # 5. Capture gradual scroll positions to verify the slide-up pop effect
        for y in [350, 700]:
            await page.evaluate(f"() => window.scrollTo(0, {y})")
            await page.wait_for_timeout(400)
            await page.screenshot(path=f"C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/live_thaid_scroll_{y}.png")
            print(f"Captured live screenshot at scroll {y}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
