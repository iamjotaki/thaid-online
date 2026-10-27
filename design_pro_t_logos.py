import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    background: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Google Sans", "Segoe UI", Roboto, sans-serif;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    color: white;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  .card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .card.active {
    border-color: #38bdf8;
    background: #1e293b;
  }
  .num {
    display: inline-block;
    background: #38bdf8;
    color: #0f172a;
    font-weight: 800;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 999px;
    margin-bottom: 4px;
  }
  .name {
    font-size: 16px;
    font-weight: 700;
    color: #f8fafc;
  }
  .desc {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.5;
  }
  .preview-bar {
    background: white;
    border-radius: 999px;
    padding: 10px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  }
  .brand {
    font-size: 22px;
    font-weight: 700;
    color: #2b313b;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .lang {
    font-size: 12px;
    font-weight: 700;
    color: #2b313b;
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 999px;
  }
</style>
</head>
<body>

<div style="text-align: center; margin-bottom: 10px;">
  <h2 style="font-size: 24px; margin: 0 0 6px 0; color: #f8fafc;">เลือกทิศทางการออกแบบโลโก้ตัว "T" (ThaiD)</h2>
  <p style="color: #94a3b8; font-size: 14px; margin: 0;">คัดสรร 4 ดีไซน์ระดับสตูดิโอแบรนด์ดิ้งสากล ปราณีต คมชัด เข้ากับแถบ Fastwork ทุกสไตล์</p>
</div>

<div class="grid">

  <!-- Concept 1: Modern Precision Monoline T (Geometric Architectural) -->
  <div class="card">
    <div>
      <span class="num">แบบที่ 1</span>
      <div class="name">Modern Precision T (เส้นตัดเรขาคณิตคลีนลักชัวรี)</div>
      <div class="desc">คานบนบางคมพร้อมรอยบากสไตล์เทคโนโลยีระดับพรีเมียม (แบบ Tesla/Linear) ดูภูมิฐาน ไม่ดูเป็นการ์ตูน</div>
    </div>
    <div class="preview-bar">
      <div class="brand">
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none">
          <path d="M4 7h24v4H18v16h-4V11H4V7z" fill="#2b313b"/>
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Concept 2: Interlocking Ribbon Knot T (True Fastwork Knot DNA) -->
  <div class="card">
    <div>
      <span class="num">แบบที่ 2</span>
      <div class="name">Fastwork Ribbon Knot T (ปมริบบิ้นขัดกัน 3 มิติ)</div>
      <div class="desc">ดึงดีเอ็นเอของ Fastwork (ปมเชือกขัดกัน) มาขึ้นโครงเป็นตัว T มีมิติซ้อนทับ มีรูกลาง เอกลักษณ์สูงมาก</div>
    </div>
    <div class="preview-bar">
      <div class="brand">
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 10h20 M16 10v16 M10 10c0-3 3-5 6-5s6 2 6 5" />
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Concept 3: Monogram T+D (ThaiD Signature) -->
  <div class="card">
    <div>
      <span class="num">แบบที่ 3</span>
      <div class="name">Signature Monogram T+D (ตัว T ซ้อนผสานตัว D)</div>
      <div class="desc">ผสานอักษร T (Thai) และ D (Digital/Design) เป็นเส้นลื่นไหลเส้นเดียว สื่อถึงแบรนด์ ThaiD โดยตรง</div>
    </div>
    <div class="preview-bar">
      <div class="brand">
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none" stroke="#2b313b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 8h14 M13 8v16 M13 8c6 0 13 3 13 8s-7 8-13 8" />
        </svg>
        <span>ThaiD</span>
      </div>
      <div class="lang">🌐 TH ˅</div>
    </div>
  </div>

  <!-- Concept 4: Minimal Capsule T (Google Material 3 / Fastwork Soft Pill) -->
  <div class="card">
    <div>
      <span class="num">แบบที่ 4</span>
      <div class="name">Minimal Capsule T (แท่งแคปซูลมนมินิมอล)</div>
      <div class="desc">เส้นท่อมนเรียบง่าย สัดส่วนทองคำ บางกำลังดี ไม่บวม ไม่หนาเกินไป กลมกลืนกับฟอนต์ Google Sans</div>
    </div>
    <div class="preview-bar">
      <div class="brand">
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none">
          <path d="M5 8h22" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round"/>
          <path d="M16 8v16" stroke="#2b313b" stroke-width="3.6" stroke-linecap="round"/>
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
        page = await browser.new_page(viewport={"width": 880, "height": 680})
        await page.set_content(html_content)
        await page.screenshot(path="C:/Users/User/.gemini/antigravity/brain/360fe13d-d196-4c61-8c6c-c040f5045eec/pro_t_logos.png", full_page=True)
        await browser.close()
        print("Generated pro_t_logos.png")

if __name__ == "__main__":
    asyncio.run(main())
