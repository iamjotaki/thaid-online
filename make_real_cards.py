import os
from PIL import Image, ImageDraw, ImageFont

cards_dir = r"c:\ThaiD.online\public\cards"
os.makedirs(cards_dir, exist_ok=True)

# 1. Mockup 1
im = Image.open(r"C:\ThaiD-Mockup\outputs\mockup_1793092259_25d946.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "mockup_real_1.jpg"), "JPEG", quality=95)
print("Saved mockup_real_1.jpg")

# 2. Mockup 2
im = Image.open(r"C:\ThaiD-Mockup\outputs\test_composite.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "mockup_real_2.jpg"), "JPEG", quality=95)
print("Saved mockup_real_2.jpg")

# 3. Novel 1
im = Image.open(r"C:\ReadAWrite\data\covers\cover_RAW-17F2D1_1792332067.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "novel_real_1.jpg"), "JPEG", quality=95)
print("Saved novel_real_1.jpg")

# 4. Novel 2
im = Image.open(r"C:\ReadAWrite\data\covers\cover_RAW-6C288F_1792745407.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "novel_real_2.jpg"), "JPEG", quality=95)
print("Saved novel_real_2.jpg")

# 5. Sticker 1 (crop the top square of the sticker pack composite)
im = Image.open(r"C:\ThaiD-Sticker\output\proj_test_api\composite_preview.png")
w, h = im.size
crop_h = min(w, h)
im_crop = im.crop((0, 0, w, int(w * 1.05)))
# Place on clean white bg
bg = Image.new("RGB", (1080, 1080), (255, 255, 255))
im_crop.thumbnail((1040, 1040), Image.Resampling.LANCZOS)
bg.paste(im_crop, ((1080 - im_crop.width) // 2, (1080 - im_crop.height) // 2), im_crop if im_crop.mode == "RGBA" else None)
bg.save(os.path.join(cards_dir, "sticker_real_1.jpg"), "JPEG", quality=95)
print("Saved sticker_real_1.jpg")

# 6. Sticker 2
im2 = Image.open(r"C:\ThaiD-Sticker\output\test_pack\composite_preview.png")
w, h = im2.size
im_crop2 = im2.crop((0, 0, w, int(w * 1.05)))
bg2 = Image.new("RGB", (1080, 1080), (255, 255, 255))
im_crop2.thumbnail((1040, 1040), Image.Resampling.LANCZOS)
bg2.paste(im_crop2, ((1080 - im_crop2.width) // 2, (1080 - im_crop2.height) // 2), im_crop2 if im_crop2.mode == "RGBA" else None)
bg2.save(os.path.join(cards_dir, "sticker_real_2.jpg"), "JPEG", quality=95)
print("Saved sticker_real_2.jpg")

# 7. Clip 1 (crop 1080x1920 center square or 4:5 for card)
im = Image.open(os.path.join(cards_dir, "clip_real_1.jpg"))
w, h = im.size
# Crop center portion with subtitle and visual
top = int(h * 0.22)
bottom = int(h * 0.78)
im_crop = im.crop((0, top, w, bottom)).resize((1080, 1080), Image.Resampling.LANCZOS)
im_crop.save(os.path.join(cards_dir, "clip_real_1_sq.jpg"), "JPEG", quality=95)
print("Saved clip_real_1_sq.jpg")

# 8. Social 1
im = Image.open(r"C:\Auto Post FB\downloads\cards\card_1_1792648031.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "social_real_1.jpg"), "JPEG", quality=95)
print("Saved social_real_1.jpg")

# 9. Social 2
im = Image.open(r"C:\Auto Post FB\downloads\cards\card_2_1792648114.jpg")
im = im.convert("RGB").resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(os.path.join(cards_dir, "social_real_2.jpg"), "JPEG", quality=95)
print("Saved social_real_2.jpg")

# 10. Smart Chat UI Mockup (1080x1080)
chat_img = Image.new("RGB", (1080, 1080), "#f4f6f8")
d = ImageDraw.Draw(chat_img)
# Header bar
d.rectangle([0, 0, 1080, 140], fill="#06c755") # LINE Green
d.text((60, 45), "LINE Official Account — Smart AI", fill="#ffffff")
# Customer bubble
d.rounded_rectangle([420, 220, 1000, 360], radius=24, fill="#ffffff", outline="#e2e8f0", width=2)
d.text((460, 260), "สวัสดีครับ อยากทราบโปรโมชันเซ็ตนี้ยังมีไหมครับ?", fill="#1e293b")
# AI Bot bubble
d.rounded_rectangle([80, 420, 860, 680], radius=24, fill="#06c755")
d.text((120, 460), "สวัสดีครับคุณลูกค้า! สินค้าเซ็ตนี้ยังมีพร้อมส่งครับ\nตอนนี้มีโปรลดพิเศษ 20% ถึงเที่ยงคืนนี้เท่านั้น\nสามารถกดสั่งซื้อผ่านลิงก์นี้ได้ทันทีเลยครับ ✨", fill="#ffffff")
# Stats card
d.rounded_rectangle([80, 760, 1000, 980], radius=24, fill="#ffffff", outline="#e2e8f0", width=2)
d.text((120, 800), "AI Assistant Status: ONLINE (ตอบกลับใน 0.8 วินาที)", fill="#0569ff")
d.text((120, 860), "อัตราปิดการขายสำเร็จ: 94.8% · รับออเดอร์ 24 ชม.", fill="#64748b")
chat_img.save(os.path.join(cards_dir, "chat_real_1.jpg"), "JPEG", quality=95)
print("Saved chat_real_1.jpg")

# 11. ThaiD Vault Security Mockup (1080x1080)
vault_img = Image.new("RGB", (1080, 1080), "#0f172a") # Slate 900
d = ImageDraw.Draw(vault_img)
# Header
d.rectangle([0, 0, 1080, 140], fill="#1e293b")
d.text((60, 45), "ThaiD Vault — AES-256 Hardware Encrypted", fill="#38bdf8")
# Key card 1
d.rounded_rectangle([80, 220, 1000, 420], radius=24, fill="#1e293b", outline="#334155", width=2)
d.text((120, 260), "GEMINI_API_KEY [ACTIVE]", fill="#22c55e")
d.text((120, 320), "AIzaSyD-8f9...4c7V8b9N0m1A2s3D4f5G6h7J", fill="#94a3b8")
# Key card 2
d.rounded_rectangle([80, 480, 1000, 680], radius=24, fill="#1e293b", outline="#334155", width=2)
d.text((120, 520), "FACEBOOK_PAGE_ACCESS_TOKEN [ROTATED]", fill="#38bdf8")
d.text((120, 580), "EAAQ8tFf6XU0...9Q2WwE7YnFh5j8K1l0zP3x4", fill="#94a3b8")
# Status
d.rounded_rectangle([80, 740, 1000, 980], radius=24, fill="#1e293b", outline="#38bdf8", width=2)
d.text((120, 780), "Zero-Knowledge Architecture · Oracle Cloud VM 2", fill="#ffffff")
d.text((120, 850), "All Credentials Fully Protected & Isolated", fill="#22c55e")
vault_img.save(os.path.join(cards_dir, "vault_real_1.jpg"), "JPEG", quality=95)
print("Saved vault_real_1.jpg")

print("All real cards generated and saved successfully!")
