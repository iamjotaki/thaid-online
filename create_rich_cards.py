import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

cards_dir = r"c:\ThaiD.online\public\cards"

# 1. STICKER GEN 1: Beautiful pastel 3D studio card with the real chibi sticker
sticker_path = r"C:\ThaiD-Sticker\output\test_processed.png"
if os.path.exists(sticker_path):
    stk = Image.open(sticker_path).convert("RGBA")
    
    # Create 1080x1080 soft gradient background (cream to light peach/lavender)
    bg = Image.new("RGBA", (1080, 1080), (255, 255, 255, 255))
    d = ImageDraw.Draw(bg)
    # Draw radial gradient or soft pastel shapes
    d.rectangle([0, 0, 1080, 1080], fill="#fff7ed") # Soft orange/cream
    d.ellipse([200, 200, 880, 880], fill="#ffedd5") # Peach inner glow
    d.ellipse([300, 300, 780, 780], fill="#fed7aa") # Warmer center
    
    # Blur background softly
    bg = bg.filter(ImageFilter.GaussianBlur(radius=40))
    
    # Scale sticker to 620x576
    stk_large = stk.resize((620, int(620 * stk.height / stk.width)), Image.Resampling.LANCZOS)
    
    # Create 3D drop shadow for sticker
    shadow = Image.new("RGBA", (1080, 1080), (0, 0, 0, 0))
    sh_w, sh_h = stk_large.size
    shadow_mask = stk_large.split()[3]
    # Draw soft black shadow
    sh_img = Image.new("RGBA", (sh_w, sh_h), (30, 20, 20, 90))
    shadow.paste(sh_img, ((1080 - sh_w) // 2 + 10, (1080 - sh_h) // 2 + 45), shadow_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=25))
    
    # Composite shadow and sticker onto bg
    bg = Image.alpha_composite(bg, shadow)
    bg.paste(stk_large, ((1080 - sh_w) // 2, (1080 - sh_h) // 2), stk_large)
    
    # Add subtle floating sparkles & badges
    d2 = ImageDraw.Draw(bg)
    d2.rounded_rectangle([70, 70, 420, 140], radius=35, fill=(255, 255, 255, 240), outline="#e2e8f0", width=2)
    d2.text((105, 92), "LINE Creators Studio · 40 Packs", fill="#06c755")
    
    bg.convert("RGB").save(os.path.join(cards_dir, "sticker_gen_1.jpg"), "JPEG", quality=95)
    print("Created sticker_gen_1.jpg")

# 2. CHAT GEN 1: Modern 3D glassmorphic conversational assistant
chat_bg = Image.new("RGB", (1080, 1080), "#f0fdf4") # Mint white
cd = ImageDraw.Draw(chat_bg)
# Draw decorative background tech circles
cd.ellipse([400, 100, 1000, 700], fill="#dcfce7")
cd.ellipse([100, 400, 800, 1100], fill="#bbf7d0")
chat_bg = chat_bg.filter(ImageFilter.GaussianBlur(radius=50))
cd = ImageDraw.Draw(chat_bg)

# Central Glass Card
cd.rounded_rectangle([100, 120, 980, 960], radius=40, fill="#ffffff", outline="#06c755", width=4)
# Header
cd.rounded_rectangle([100, 120, 980, 260], radius=40, fill="#06c755")
cd.rectangle([100, 200, 980, 260], fill="#06c755")
cd.ellipse([140, 155, 210, 225], fill="#ffffff")
cd.text((165, 175), "AI", fill="#06c755")
cd.text((235, 165), "ThaiD Smart Chat Assistant", fill="#ffffff")
cd.text((235, 205), "LINE Official Account · 24/7 Active Agent", fill="#dcfce7")

# Customer Message
cd.rounded_rectangle([440, 310, 930, 440], radius=28, fill="#f1f5f9", outline="#e2e8f0", width=2)
cd.text((475, 345), "อยากทราบแพ็กเกจ AI Mockup สตูดิโอครับ\nมีระบบทดลองใช้งานฟรีไหมครับ?", fill="#0f172a")

# AI Reply Message
cd.rounded_rectangle([140, 480, 840, 680], radius=28, fill="#06c755")
cd.text((180, 520), "สวัสดีครับคุณลูกค้า! ยินดีต้อนรับสู่ ThaiD AI ครับ ✨\nมีระบบทดลองสร้างภาพฟรี 10 ภาพแรกทันที\nระบบจะไดคัตและจัดแสงเงาสมจริงใน 1 วินาทีครับ!", fill="#ffffff")

# Metrics Banner
cd.rounded_rectangle([140, 730, 930, 910], radius=24, fill="#f8fafc", outline="#cbd5e1", width=2)
cd.text((180, 765), "⚡ ความเร็วตอบกลับ: 0.8 วินาที  |  🎯 อัตราปิดการขาย: 96.4%", fill="#0569ff")
cd.text((180, 825), "เชื่อมต่ออัตโนมัติผ่าน LINE Messaging API Webhook ตลอด 24 ชม.", fill="#64748b")

chat_bg.save(os.path.join(cards_dir, "chat_gen_1.jpg"), "JPEG", quality=95)
print("Created chat_gen_1.jpg")

# 3. VAULT GEN 1: Futuristic cyber-security crystal vault
vault_bg = Image.new("RGB", (1080, 1080), "#090d16") # Deep tech obsidian
vd = ImageDraw.Draw(vault_bg)
# Glowing cyber background
vd.ellipse([200, 200, 880, 880], fill="#082f49") # Sky blue glow
vd.ellipse([350, 350, 730, 730], fill="#0369a1")
vault_bg = vault_bg.filter(ImageFilter.GaussianBlur(radius=60))
vd = ImageDraw.Draw(vault_bg)

# Central Glass Obsidian Shield
vd.rounded_rectangle([100, 120, 980, 960], radius=40, fill="#0f172a", outline="#0284c7", width=3)
# Header
vd.rounded_rectangle([100, 120, 980, 250], radius=40, fill="#0284c7")
vd.rectangle([100, 180, 980, 250], fill="#0284c7")
vd.text((150, 165), "🔒 ThaiD Personal Vault — Hardware AES-256", fill="#ffffff")
vd.text((150, 205), "Zero-Knowledge Cloud Key & Credential Isolation", fill="#e0f2fe")

# Key Card 1
vd.rounded_rectangle([150, 300, 930, 460], radius=24, fill="#1e293b", outline="#22c55e", width=2)
vd.ellipse([185, 335, 205, 355], fill="#22c55e")
vd.text((225, 335), "GEMINI_API_KEYS_POOL (80 Keys Rotated)", fill="#22c55e")
vd.text((185, 390), "AQ.Ab8RN6K... · AES-256 Encrypted · Auto-Rotate Active", fill="#94a3b8")

# Key Card 2
vd.rounded_rectangle([150, 500, 930, 660], radius=24, fill="#1e293b", outline="#38bdf8", width=2)
vd.ellipse([185, 535, 205, 555], fill="#38bdf8")
vd.text((225, 535), "LINE_MESSAGING_API_SECRET", fill="#38bdf8")
vd.text((185, 590), "1522aab2a4... · Hardware Isolated · Webhook Verified", fill="#94a3b8")

# Status Card
vd.rounded_rectangle([150, 700, 930, 900], radius=24, fill="#0c4a6e", outline="#38bdf8", width=2)
vd.text((185, 740), "🛡️ Security Status: 100% PROTECTED", fill="#38bdf8")
vd.text((185, 805), "Encrypted via Fernet AES-256 on Oracle Cloud Infrastructure", fill="#ffffff")

vault_bg.save(os.path.join(cards_dir, "vault_gen_1.jpg"), "JPEG", quality=95)
print("Created vault_gen_1.jpg")

print("All rich cards created successfully!")
