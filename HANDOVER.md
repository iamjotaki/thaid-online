# 🌐 ThaiD.online Multi-SaaS Ecosystem — Master Handover & AI Context
> **คำสั่งสำหรับ Antigravity / AI ในเครื่องใหม่:**  
> อ่านเอกสารนี้ให้จบ คุณจะเข้าใจภาพรวมระบบ โครงสร้างเซิร์ฟเวอร์ บัญชี สิทธิ์การเข้าถึง และมาตรฐาน UI/UX ทั้งหมดของโปรเจกต์ `ThaiD.online` และสามารถเริ่มพัฒนา ปรับแก้ หรือ Deploy งานต่อได้ทันที 100% โดยผู้ใช้ไม่ต้องอธิบายซ้ำ

---

## 📌 1. ภาพรวมโปรเจกต์ (Project Overview)
ระบบ Multi-SaaS แพลตฟอร์มศูนย์รวมเครื่องมือ AI สำหรับคนไทย ใช้โดเมนหลัก `ThaiD.online` และแยกบริการย่อยเป็น Subdomain โดยมี Wildcard DNS `*.thaid.online` รองรับ:

| บริการ | หน้าที่ | โดเมนจริง (Live URL) | ที่มาโค้ด (Source / GitHub) | เทคโนโลยีหลัก | พอร์ต | สถานะ |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **ThaiD Hub** | เว็บหลัก / รวมบริการ / Marketing | [https://thaid.online](https://thaid.online) | `c:\ThaiD.online`<br>[iamjotaki/thaid-online](https://github.com/iamjotaki/thaid-online) | Next.js 16 (Turbopack), React 19, Tailwind CSS v4 | 3000 | 🟢 Live |
| **Novel Studio** | สตูดิโอแต่งนิยาย AI & Auto-Upload | [https://novel.thaid.online](https://novel.thaid.online) | `C:\ReadAWrite`<br>[iamjotaki/thaid-novel-studio](https://github.com/iamjotaki/thaid-novel-studio) | Python 3.10, Playwright Chromium, SQLite, Gemini Flash | 8080 | 🟢 Live |
| **Social Poster** | ผลิตคอนเทนต์ & วิดีโอ Reels เฟสบุ๊ค | [https://social.thaid.online](https://social.thaid.online) | `C:\Auto Post FB`<br>[iamjotaki/thaid-social-poster](https://github.com/iamjotaki/thaid-social-poster) | Python 3.11, Flask, FFmpeg, Thai TLWG Fonts, Neon Postgres | 5000 | 🟢 Live |
| **ThaiD Vault** | คลังข้อมูลความปลอดภัย บัญชี & โฮสติ้ง | [https://vault.thaid.online](https://vault.thaid.online) | `C:\ThaiD-Vault`<br>[iamjotaki/thaid-vault](https://github.com/iamjotaki/thaid-vault) | Python 3.11, FastAPI, SQLite, AES-256 Fernet, Tailwind | 8088 | 🟢 Live |
| **LINE Sticker** | เจนชุดสติกเกอร์ไลน์ 8/16/24/40 รูป | [https://sticker.thaid.online](https://sticker.thaid.online) | `C:\ThaiD-Sticker`<br>[iamjotaki/thaid-sticker](https://github.com/iamjotaki/thaid-sticker) | Python 3.11, FastAPI, Pillow, NumPy, REST API (Flux Turbo & Google Flow) | 8090 | 🟢 Live |
| **Clip AI Studio** | สร้างวิดีโอสั้น 9:16 (TikTok, Reels, Shorts) | [https://clip.thaid.online](https://clip.thaid.online) | `C:\ThaiD-Clip`<br>[iamjotaki/thaid-clip](https://github.com/iamjotaki/thaid-clip) | Python 3.11, FastAPI, FFmpeg, gTTS, Gemini 3.5, Google Flow Veo | 8092 | 🟢 Live |
| **Smart Chat AI** | แอดมิน AI ตอบแชท LINE OA 24 ชม. | [https://chat.thaid.online](https://chat.thaid.online) | `C:\ThaiD-Chat`<br>[iamjotaki/thaid-chat](https://github.com/iamjotaki/thaid-chat) | Python 3.11, FastAPI, Gemini 3.5, LINE Messaging API Webhook | 8094 | 🟢 Live |

---

## 🖥️ 2. โครงสร้างเซิร์ฟเวอร์ & บัญชีเข้าถึง (Infrastructure & Credentials)

### 2.1 เซิร์ฟเวอร์จริง (Oracle Cloud Always Free VM)
Oracle Cloud มีการเปิดใช้งานอยู่ทั้งหมด **3 เครื่อง (Instances)** ครบถ้วนตามสิทธิ์ Always Free Tier:

1. **เครื่องที่ 1 (Primary Production Host - Yayni Platform):**
   - **Instance Name:** `yayni-arm-18gb`
   - **Public IP:** `129.221.220.121` (Private IP: `10.0.0.224`)
   - **OS / Spec:** Ubuntu 24.04 LTS (Ampere ARM A1, 2 OCPU, 12 GB RAM, 80 GB NVMe)
   - **หน้าที่:** รันเว็บไซต์ [https://yayni.com](https://yayni.com), PM2 Processes, PostgreSQL 16
   - **SSH Command:** `ssh -i C:\NV\oracle_key.pem ubuntu@129.221.220.121`

2. **เครื่องที่ 2 (Worker Node 2 - ThaiD.online Ecosystem):**
   - **Instance Name:** `yayni-node2-12gb` (`yayni-arm-node2-384382`)
   - **Public IP:** `129.221.170.225` (Private IP: `10.0.0.241`)
   - **OS / Spec:** Ubuntu 24.04 LTS (Ampere ARM A1, 2 OCPU, 12 GB RAM, 48 GB NVMe)
   - **หน้าที่:** รัน Coolify v4, Docker Containers, Traefik v3.7 Proxy ควบคุมคอนเทนเนอร์ทั้งหมด 7 ตัวของ `*.thaid.online`
   - **SSH Command:** `ssh -i C:\NV\oracle_key.pem ubuntu@129.221.170.225`

3. **เครื่องที่ 3 (AMD Micro Server):**
   - **Instance Name:** `instance-20261004-1558`
   - **Public IP:** `161.118.243.162`
   - **OS / Spec:** Ubuntu 24.04 LTS (AMD E2.1.Micro, 1 OCPU, 1 GB RAM, 45 GB Disk)
   - **หน้าที่:** เครื่องดั้งเดิม รัน PM2 (`novel-studio`, `watchparty`, `yayni-novel`) และ Nginx
   - **SSH Command:** `ssh -i C:\NV\oracle_key.pem ubuntu@161.118.243.162`

### 2.2 ระบบจัดการคอนเทนเนอร์ (Coolify Control Panel)
- **Web Dashboard:** [http://thaid.online:8000](http://thaid.online:8000) (หรือ `http://129.221.170.225:8000`)
- **Admin User:** `Jotaki`
- **Reverse Proxy:** Traefik v3.7 (พอร์ต 80, 443 อัตโนมัติ พร้อมต่ออายุ Let's Encrypt SSL ตลอดชีพ)
- **Docker Network:** Address Pool ถูกตั้งค่าเป็น `172.16.0.0/12` (ป้องกันชนกับ Subnet `10.0.0.0/24` ของ Oracle Cloud)

### 2.3 Application ID ใน Coolify Database (PostgreSQL)
- **App ID 1:** `thaid-online` (UUID: `r0cskossc8wggss88cgg8g8o`, พอร์ต 3000, Build Pack: `nixpacks` / Node.js)
- **App ID 2:** `thaid-novel-studio` (UUID: `swck4gwggkgg0k0gwokkwosg`, พอร์ต 8080, Build Pack: `dockerfile` / Python 3.10)
- **App ID 3:** `thaid-social-poster` (UUID: `cwskck0k0wksogwkcgc484gc`, พอร์ต 5000, Build Pack: `dockerfile` / Python 3.11)
- **App ID 4:** `thaid-vault` (UUID: `sc8kg8wkssoc4cskkocsgc0c`, พอร์ต 8088, Build Pack: `dockerfile` / Python 3.11)
- **App ID 5:** `thaid-sticker` (UUID: `k8c80gwcc8g80wccogskkss4`, พอร์ต 8090, Build Pack: `dockerfile` / Python 3.11)
- **App ID 6:** `thaid-clip` (UUID: `swspkwo1d8qtbquvbzqr9iir`, พอร์ต 8092, Build Pack: `dockerfile` / Python 3.11)
- **App ID 7:** `thaid-chat` (UUID: `304ytjxowbaewvgxk9xxurt4`, พอร์ต 8094, Build Pack: `dockerfile` / Python 3.11)

---

## 🔑 3. บัญชี GitHub & API Keys

### 3.1 GitHub Account
- **User:** `iamjotaki`
- **Repos:**
  - `iamjotaki/thaid-online`
  - `iamjotaki/thaid-novel-studio`
  - `iamjotaki/thaid-social-poster`
  - `iamjotaki/thaid-vault`
  - `iamjotaki/thaid-sticker`
  - `iamjotaki/thaid-clip`
  - `iamjotaki/thaid-chat`

### 3.2 External API Keys & Database
- ตัวแปรทั้งหมดถูกผูกไว้ในระบบ **Coolify Environment Variables** เรียบร้อยแล้ว (ทั้ง Runtime และ Buildtime)
- ข้อมูล API Keys และบัญชีทั้งหมดสามารถเปิดดูและคัดลอกได้ทันทีผ่านระบบ **[ThaiD Vault](https://vault.thaid.online)** (หมวดหมู่ `Google API Keys` มีคลังคีย์ Gemini รวม 80 คีย์ และหมวดหมู่อื่นๆ ครบถ้วน)
- ตัวแปรสำคัญ:
  - `GEMINI_API_KEY`: คีย์สำหรับ Gemini 3.5 Flash-lite / Gemini 3.8
  - `FB_PAGE_ID` & `FB_PAGE_ACCESS_TOKEN`: Graph API สำหรับโพสต์เฟสบุ๊ค
  - `DATABASE_URL`: Neon Cloud PostgreSQL
  - `LINE_CHANNEL_ACCESS_TOKEN` & `LINE_CHANNEL_SECRET`: สำหรับ Webhook LINE OA

---

## 🎨 4. มาตรฐานดีไซน์ (Design System Standard)
ทุกเว็บไซต์ในเครือข่าย `ThaiD.online` ต้องใช้มาตรฐาน UI/UX เดียวกันตามสเปก **Apple Cupertino Luxury Aesthetic**:

1. **Color Palette:**
   - Primary Accent: `#e85a2d` (`apple-coral`), hover `#d64f24`, light `#fef2ee`
   - Secondary Accent: `#0071e3` (`apple-blue`)
   - Light Mode Background: `#f5f5f7` (apple-subtle), Card: `#ffffff`
   - Dark Mode Background: `#0c0c0e` (main), Card: `#161619`
   - Subtle Borders: `rgba(0, 0, 0, 0.08)` (Light) / `rgba(255, 255, 255, 0.08)` (Dark)
2. **Typography & Icons:**
   - Fonts: `Plus Jakarta Sans`, `Prompt`, `Sarabun`, `JetBrains Mono`
   - Icons: `Material Symbols Outlined`
3. **Navbar Standard Layout (`h-[52px]` Sticky Frosted Bar):**
   ```
   [ Logo & Name ] ──── [ Segmented Nav Pills ] ──── [ ☀️/🌙 ] [ Action / Login ] [ ☰ Mobile ]
   ```
   - **Segmented Nav Pills ในลำดับเดียวกันทุกเว็บ:**
     1. 🌐 `ThaiD Hub` (`https://thaid.online`)
     2. ✍️ `นิยาย AI` (`https://novel.thaid.online`)
     3. 📢 `โพสต์ Facebook` (`https://social.thaid.online`)
     4. 🎨 `สติกเกอร์ไลน์` (`https://sticker.thaid.online`)
     5. 🎬 `คลิปสั้น AI` (`https://clip.thaid.online`)
     6. 💬 `แชทบอท LINE` (`https://chat.thaid.online`)
     - เว็บปัจจุบันจะมีแถบไฮไลต์ Active ส่วนเว็บอื่นเป็นลิงก์กดสลับได้ทันที
   - **Right Controls:** ปุ่มสลับ Dark/Light mode (`toggleDarkMode()`) -> ปุ่ม Action หลัก -> ปุ่มแฮมเบอร์เกอร์สำหรับมือถือ
4. **Tailwind v4 Rule สำคัญมาก:**
   ใน Tailwind v4 การสลับ Dark Mode แบบ Class ต้องประกาศคำสั่งนี้ใน CSS เสมอ:
   ```css
   @variant dark (&:where(.dark, .dark *));
   ```

---

## 🛠️ 5. คำสั่งและขั้นตอนการทำงานสำหรับ Antigravity (Workflow)

### 5.1 เมื่อแก้ไขโค้ดเสร็จ (Commit & Push)
```bash
git add -A; git commit -m "feat/fix: ข้อความอธิบายการเปลี่ยนแปลง"; git push origin main
```

### 5.2 สั่ง Deploy อัตโนมัติขึ้นเซิร์ฟเวอร์ Oracle Cloud
สามารถสั่งผ่าน SSH ด้วย PowerShell หรือ Bash เข้าไปสั่ง Laravel Tinker ของ Coolify โดยตรง:
```bash
# App 1 (ThaiD Hub)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(1), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 2 (Novel Studio)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(2), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 3 (Social Poster)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(3), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 4 (ThaiD Vault)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(4), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 5 (LINE Sticker Studio)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(5), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 6 (ThaiD Clip AI Studio)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(6), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"

# App 7 (ThaiD Smart Chat AI)
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "echo 'queue_application_deployment(application: App\Models\Application::find(7), deployment_uuid: (string) Str::uuid(), force_rebuild: true);' | sudo docker exec -i coolify php artisan tinker"
```

### 5.3 ตรวจสอบสถานะการ Deploy และ Container
```bash
# ตรวจสอบคิวบิลด์ล่าสุด
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "sudo docker exec coolify-db psql -U coolify -d coolify -c 'SELECT id, application_id, status, updated_at FROM application_deployment_queues ORDER BY id DESC LIMIT 5;'"

# ตรวจสอบคอนเทนเนอร์ที่กำลังรัน
ssh -i C:\NV\oracle_key.pem -o StrictHostKeyChecking=no ubuntu@129.221.170.225 "sudo docker ps"
```

---

## 🎯 6. สถานะระบบและความคืบหน้า (System Status & Milestones)
1. **ครบถ้วนทั้ง 7 บริการ (All 7 Apps 100% Live in Production):**
   - ThaiD Hub, Novel Studio, Social Poster, ThaiD Vault, LINE Sticker Studio, Clip AI Studio, และ Smart Chat AI ทั้งหมดออนไลน์สมบูรณ์แบบพร้อม SSL อัตโนมัติ
2. **Central Auth / SSO (`auth.thaid.online`):**
   - แผนพัฒนาถัดไป: เชื่อมต่อระบบสมาชิกให้ล็อกอินครั้งเดียวใช้ได้ทุก Subdomain (Cookie Domain: `.thaid.online`)

---
*บันทึกข้อมูลล่าสุด: ตุลาคม 2026 โดย ThaiD Platform Team*
