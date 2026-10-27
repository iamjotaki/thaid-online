import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        print("Navigating to http://localhost:3000...")
        await page.goto("http://localhost:3000", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # 1. Take initial screenshot
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/sheet_test_initial.png")
        print("Captured initial hero screenshot")

        # 2. Check the Scroll Down button
        scroll_btn = page.locator('button[aria-label="Scroll down to services"]')
        is_visible = await scroll_btn.is_visible()
        print(f"Scroll down button visible: {is_visible}")

        # Check initial scroll position
        initial_scroll = await page.evaluate("() => window.scrollY")
        print(f"Initial scrollY: {initial_scroll}")

        # 3. Click the Scroll Down button
        print("Clicking 'Scroll down' button...")
        await scroll_btn.click()
        
        # Wait for smooth scroll to complete (1.5 seconds)
        await page.wait_for_timeout(1500)

        post_click_scroll = await page.evaluate("() => window.scrollY")
        print(f"ScrollY after clicking Scroll Down button: {post_click_scroll}")

        # 4. Take screenshot of the elevated sheet popped up
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/sheet_test_after_click.png")
        print("Captured after-click elevated sheet screenshot")

        # 5. Check the sheet properties and card crispness
        sheet_info = await page.evaluate("""() => {
            const sheet = document.getElementById('services-directory');
            const rect = sheet ? sheet.getBoundingClientRect() : null;
            const style = sheet ? window.getComputedStyle(sheet) : null;
            return {
                exists: !!sheet,
                top: rect ? rect.top : null,
                borderRadius: style ? style.borderTopLeftRadius : null,
                boxShadow: style ? style.boxShadow : null,
                marginTop: style ? style.marginTop : null
            };
        }""")
        print(f"Sheet evaluation: {sheet_info}")

        # 6. Test gradual scroll from 0 to 800 to see the sheet slide up
        await page.evaluate("() => window.scrollTo(0, 0)")
        await page.wait_for_timeout(500)

        for scroll_y in [0, 300, 600, 900]:
            await page.evaluate(f"() => window.scrollTo(0, {scroll_y})")
            await page.wait_for_timeout(300)
            await page.screenshot(path=f"C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/sheet_scroll_{scroll_y}.png")
            print(f"Captured screenshot at scrollY={scroll_y}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
