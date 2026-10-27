import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Google Sans", "Segoe UI", Roboto, sans-serif;
    padding: 40px;
    color: white;
  }
  .header {
    text-align: center;
    margin-bottom: 30px;
  }
  .header h1 {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #f8fafc;
  }
  .header p {
    color: #94a3b8;
    font-size: 14px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    max-width: 900px;
    margin: 0 auto;
  }
  .card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    transition: all 0.2s;
  }
  .tag {
    display: inline-block;
    background: #0284c7;
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 999px;
    margin-bottom: 6px;
  }
  .title {
    font-size: 16px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 4px;
  }
  .desc {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.4;
  }
  .preview {
    background: #ffffff;
    border-radius: 999px;
    padding: 8px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0,0,0,0.12);
  }
  .brand {
    font-size: 21px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .lang {
    font-size: 11px;
    font-weight: 700;
    color: #2b313b;
    padding: 3px 8px;
    border: 1px solid rgba(0,0,0,0.1);
    border-radius: 999px;
  }
</style>
</head>
<body>

<div class="header">
  <h1>เลือกดีไซน์โลโก้ "ThaiD" ที่คุณต้องการ</h1>
  <p>ขออภัยอย่างยิ่งสำหรับดีไซน์ก่อนหน้าที่ดูพองหนาเหมือนเห็ด/ร่มครับ ด้านล่างนี้คือ 4 สไตล์ที่ออกแบบใหม่ด้วยมาตรฐานแบรนด์ระดับสากล</p>
</div>

<div class="grid">

  <!-- Option 1: Minimal Capsule T -->
  <div class="card">
    <div>
      <span class="tag">แบบที่ 1 (แนะนำ)</span>
      <div class="title">Minimal Capsule T (แท่งมนคลีนหรู)</div>
      <div class="desc">สัดส่วนเพรียวบาง คานบนตรง ก้านลงตรง ปลายโค้งมนแบบ Fastwork พอดี ไม่บวม ไม่หนา เรียบหรูที่สุด</div>
    </div>
    <div class="preview">
      <div class="brand">
        <svg width="22" height="22" viewBox="0 0 32 32" fill="none">
          <path d="M4.5 8h23" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round"/>
          <path d="M16 8v17" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round"/>
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Option 2: Monogram T+D -->
  <div class="card">
    <div>
      <span class="tag">แบบที่ 2</span>
      <div class="title">Signature Monogram T+D (เส้นผสาน T & D)</div>
      <div class="desc">คานบนเป็น T ปลายก้านล่างและปีกขวาโค้งต่อเป็นตัว D อย่างแนบเนียน เป็นเอกลักษณ์ของแบรนด์ ThaiD โดยเฉพาะ</div>
    </div>
    <div class="preview">
      <div class="brand">
        <svg width="22" height="22" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 8h14 M13 8v16 M13 8c6 0 13 3 13 8s-7 8-13 8" />
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Option 3: Modern Tech Geometric T -->
  <div class="card">
    <div>
      <span class="tag">แบบที่ 3</span>
      <div class="title">Modern Architectural T (ทรงเหลี่ยมคัตคมระดับโปร)</div>
      <div class="desc">รูปทรงเรขาคณิตทึบแบบโมเดิร์นเทค (สไตล์ Linear/Vercel) มั่นคง หนักแน่น คมกริบ</div>
    </div>
    <div class="preview">
      <div class="brand">
        <svg width="22" height="22" viewBox="0 0 32 32" fill="#2b313b">
          <path d="M4 7h24v4H18.5v16h-5V11H4V7z"/>
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Option 4: Dynamic Fastwork Knot T -->
  <div class="card">
    <div>
      <span class="tag">แบบที่ 4</span>
      <div class="title">Interlocking Knot T (ปมเชือกขัดกัน 3 มิติ)</div>
      <div class="desc">จำลองปมเชือกริบบิ้นขัดกันของ Fastwork โดยรักษามิติห่วงและรูกลาง แต่ขึ้นทรงตัว T อย่างประณีต</div>
    </div>
    <div class="preview">
      <div class="brand">
        <svg width="22" height="22" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 10h20 M16 10v16 M10 10c0-3 3-5 6-5s6 2 6 5" />
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

</div>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 960, "height": 620})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/t_logo_showcase.png")
        await browser.close()
        print("Generated t_logo_showcase.png")

if __name__ == "__main__":
    asyncio.run(main())
