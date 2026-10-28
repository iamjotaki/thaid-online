import asyncio
from playwright.async_api import async_playwright

async def check():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        await page.goto('https://thaid.online', wait_until='networkidle')
        
        # Check grey bar
        grey_bar = await page.locator('div.w-14.h-1\\.5').count()
        print(f'Grey bar count: {grey_bar}')
        
        # Check sub home link
        home_links = await page.locator('text="หน้าแรกบริการ"').count()
        print(f'Portal home link count: {home_links}')
        
        # Take screenshot of navbar
        shot_nav = r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\audit_nav_portal.png'
        await page.screenshot(path=shot_nav, clip={'x': 0, 'y': 0, 'width': 1440, 'height': 200})
        print('Saved portal nav screenshot')
        
        # Click SaaS dropdown button
        btn = page.locator('button:has-text("เลือกบริการ SaaS")')
        await btn.click()
        await asyncio.sleep(0.5)
        
        shot_drop = r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\audit_nav_portal_dropdown.png'
        await page.screenshot(path=shot_drop, clip={'x': 850, 'y': 0, 'width': 590, 'height': 520})
        print('Saved portal dropdown screenshot')
        
        # Scroll down to page 2 and take screenshot of section heading
        await page.evaluate('window.scrollTo(0, window.innerHeight)')
        await asyncio.sleep(0.8)
        shot_sec = r'C:\Users\User\.gemini\antigravity\brain\360fe13d-d196-4c61-8c6c-c040f5045eec\audit_portal_section_top.png'
        await page.screenshot(path=shot_sec, clip={'x': 0, 'y': 0, 'width': 1440, 'height': 450})
        print('Saved section top screenshot')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(check())
