import asyncio
from playwright.async_api import async_playwright

async def inspect_single_card():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://fastwork.com", wait_until="networkidle", timeout=30000)
        
        card_html = await page.evaluate("""() => {
            const card = document.querySelector('.orbit-card');
            return card ? card.innerHTML : '';
        }""")
        
        with open("fastwork_card.html", "w", encoding="utf-8") as f:
            f.write(card_html)
        print("Wrote fastwork_card.html")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(inspect_single_card())
