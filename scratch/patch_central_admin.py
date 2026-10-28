# -*- coding: utf-8 -*-
import os

path = r"C:\ThaiD.online\app\admin\page.tsx"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update AppContainer interface
old_interface = """interface AppContainer {
  id: number;
  name: string;
  subdomain: string;
  url: string;
  coolifyId: string;
  port: number;
  status: "healthy" | "running" | "deploying";
  uptime: string;
  category: string;
  badgeColor: string;
  description: string;
}"""

new_interface = """interface AppContainer {
  id: number;
  name: string;
  subdomain: string;
  url: string;
  dashboardUrl: string;
  adminUrl: string;
  coolifyId: string;
  port: number;
  status: "healthy" | "running" | "deploying";
  uptime: string;
  category: string;
  badgeColor: string;
  description: string;
}"""

if old_interface in content:
    content = content.replace(old_interface, new_interface, 1)
    print("Interface updated successfully")
else:
    print("Old interface not matched exactly")

# 2. Update APPS_LIST
old_apps_list = """const APPS_LIST: AppContainer[] = [
  {
    id: 1,
    name: "ThaiD Main Portal Hub",
    subdomain: "thaid.online",
    url: "https://thaid.online",
    coolifyId: "daegz6kwhnqnctgmhil9zkqv",
    port: 3000,
    status: "healthy",
    uptime: "2 วัน 14 ชม.",
    category: "Master Portal",
    badgeColor: "bg-blue-50 text-[#0569ff] border-blue-200",
    description: "Next.js Turbopack Master Gateway & Hub",
  },
  {
    id: 2,
    name: "Novel Studio",
    subdomain: "novel.thaid.online",
    url: "https://novel.thaid.online",
    coolifyId: "vs61mcmytgecg3pbfgv9pxo0",
    port: 8081,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Story Creator",
    badgeColor: "bg-indigo-50 text-indigo-600 border-indigo-200",
    description: "AI แต่งนิยาย 10 ตอนจบ ซิงค์ ReadAWrite",
  },
  {
    id: 3,
    name: "Social Auto-Poster",
    subdomain: "social.thaid.online",
    url: "https://social.thaid.online",
    coolifyId: "dP6SPDctRMHxJMqbVONKMm2o",
    port: 5000,
    status: "healthy",
    uptime: "22 นาที (Deploy ใหม่)",
    category: "Social Media",
    badgeColor: "bg-emerald-50 text-emerald-600 border-emerald-200",
    description: "ดึงข่าว RSS & สร้างคอนเทนต์โพสต์ Facebook 24 ชม.",
  },
  {
    id: 4,
    name: "Personal Private Vault",
    subdomain: "vault.thaid.online",
    url: "https://vault.thaid.online",
    coolifyId: "rfchl2dnuzastzbwz9af",
    port: 8094,
    status: "healthy",
    uptime: "10 นาที (Deploy ใหม่)",
    category: "Security & Keys",
    badgeColor: "bg-cyan-50 text-cyan-700 border-cyan-200",
    description: "ระบบจัดเก็บรหัสและข้อมูลลับ เข้ารหัส AES-256",
  },
  {
    id: 5,
    name: "LINE Sticker Creator",
    subdomain: "sticker.thaid.online",
    url: "https://sticker.thaid.online",
    coolifyId: "mjp4m1pv2xv9qbqug6dz",
    port: 8092,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Design & Art",
    badgeColor: "bg-pink-50 text-pink-600 border-pink-200",
    description: "สร้างชุดสติกเกอร์ไลน์ 40 แอ็กชันด้วย AI ไดคัต",
  },
  {
    id: 6,
    name: "Clip AI & Reels",
    subdomain: "clip.thaid.online",
    url: "https://clip.thaid.online",
    coolifyId: "i5ol6htcy54ppahx9axb",
    port: 8091,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Video Studio",
    badgeColor: "bg-purple-50 text-purple-600 border-purple-200",
    description: "สร้างคลิปสั้นแนวตั้ง 9:16 สไตล์ไวรัลด้วย AI พากย์",
  },
  {
    id: 7,
    name: "Smart Chat AI",
    subdomain: "chat.thaid.online",
    url: "https://chat.thaid.online",
    coolifyId: "mljfyc3nj0ape3oeywnr",
    port: 8093,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Chatbot & CRM",
    badgeColor: "bg-teal-50 text-teal-600 border-teal-200",
    description: "บอทแอดมินตอบแชทลูกค้า LINE OA 24/7 ตอบไวใน 0.8 วิ",
  },
  {
    id: 8,
    name: "Mockup Studio",
    subdomain: "mockup.thaid.online",
    url: "https://mockup.thaid.online",
    coolifyId: "uqcyaheimcodjvb6s3yw",
    port: 8096,
    status: "healthy",
    uptime: "11 ชม.",
    category: "E-Commerce Media",
    badgeColor: "bg-sky-50 text-sky-600 border-sky-200",
    description: "ภาพถ่ายสินค้าลักชัวรี ไดคัตและจัดแสงฉากหลังแบบ 4K",
  },
];"""

new_apps_list = """const APPS_LIST: AppContainer[] = [
  {
    id: 1,
    name: "ThaiD Main Portal Hub",
    subdomain: "thaid.online",
    url: "https://thaid.online",
    dashboardUrl: "https://thaid.online",
    adminUrl: "https://thaid.online/admin",
    coolifyId: "daegz6kwhnqnctgmhil9zkqv",
    port: 3000,
    status: "healthy",
    uptime: "2 วัน 14 ชม.",
    category: "Master Portal",
    badgeColor: "bg-blue-50 text-[#0569ff] border-blue-200",
    description: "Next.js Turbopack Master Gateway & Hub",
  },
  {
    id: 2,
    name: "Novel Studio",
    subdomain: "novel.thaid.online",
    url: "https://novel.thaid.online",
    dashboardUrl: "https://novel.thaid.online/dashboard",
    adminUrl: "https://novel.thaid.online/admin",
    coolifyId: "vs61mcmytgecg3pbfgv9pxo0",
    port: 8081,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Story Creator",
    badgeColor: "bg-indigo-50 text-indigo-600 border-indigo-200",
    description: "AI แต่งนิยาย 10 ตอนจบ ซิงค์ ReadAWrite",
  },
  {
    id: 3,
    name: "Social Auto-Poster",
    subdomain: "social.thaid.online",
    url: "https://social.thaid.online",
    dashboardUrl: "https://social.thaid.online/dashboard",
    adminUrl: "https://social.thaid.online/admin",
    coolifyId: "dP6SPDctRMHxJMqbVONKMm2o",
    port: 5000,
    status: "healthy",
    uptime: "22 นาที (Deploy ใหม่)",
    category: "Social Media",
    badgeColor: "bg-emerald-50 text-emerald-600 border-emerald-200",
    description: "ดึงข่าว RSS & สร้างคอนเทนต์โพสต์ Facebook 24 ชม.",
  },
  {
    id: 4,
    name: "Personal Private Vault",
    subdomain: "vault.thaid.online",
    url: "https://vault.thaid.online",
    dashboardUrl: "https://vault.thaid.online/dashboard",
    adminUrl: "https://vault.thaid.online/admin",
    coolifyId: "rfchl2dnuzastzbwz9af",
    port: 8094,
    status: "healthy",
    uptime: "10 นาที (Deploy ใหม่)",
    category: "Security & Keys",
    badgeColor: "bg-cyan-50 text-cyan-700 border-cyan-200",
    description: "ระบบจัดเก็บรหัสและข้อมูลลับ เข้ารหัส AES-256",
  },
  {
    id: 5,
    name: "LINE Sticker Creator",
    subdomain: "sticker.thaid.online",
    url: "https://sticker.thaid.online",
    dashboardUrl: "https://sticker.thaid.online/dashboard",
    adminUrl: "https://sticker.thaid.online/admin",
    coolifyId: "mjp4m1pv2xv9qbqug6dz",
    port: 8092,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Design & Art",
    badgeColor: "bg-pink-50 text-pink-600 border-pink-200",
    description: "สร้างชุดสติกเกอร์ไลน์ 40 แอ็กชันด้วย AI ไดคัต",
  },
  {
    id: 6,
    name: "Clip AI & Reels",
    subdomain: "clip.thaid.online",
    url: "https://clip.thaid.online",
    dashboardUrl: "https://clip.thaid.online/dashboard",
    adminUrl: "https://clip.thaid.online/admin",
    coolifyId: "i5ol6htcy54ppahx9axb",
    port: 8091,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Video Studio",
    badgeColor: "bg-purple-50 text-purple-600 border-purple-200",
    description: "สร้างคลิปสั้นแนวตั้ง 9:16 สไตล์ไวรัลด้วย AI พากย์",
  },
  {
    id: 7,
    name: "Smart Chat AI",
    subdomain: "chat.thaid.online",
    url: "https://chat.thaid.online",
    dashboardUrl: "https://chat.thaid.online/dashboard",
    adminUrl: "https://chat.thaid.online/admin",
    coolifyId: "mljfyc3nj0ape3oeywnr",
    port: 8093,
    status: "healthy",
    uptime: "11 ชม.",
    category: "Chatbot & CRM",
    badgeColor: "bg-teal-50 text-teal-600 border-teal-200",
    description: "บอทแอดมินตอบแชทลูกค้า LINE OA 24/7 ตอบไวใน 0.8 วิ",
  },
  {
    id: 8,
    name: "Mockup Studio",
    subdomain: "mockup.thaid.online",
    url: "https://mockup.thaid.online",
    dashboardUrl: "https://mockup.thaid.online/dashboard",
    adminUrl: "https://mockup.thaid.online/admin",
    coolifyId: "uqcyaheimcodjvb6s3yw",
    port: 8096,
    status: "healthy",
    uptime: "11 ชม.",
    category: "E-Commerce Media",
    badgeColor: "bg-sky-50 text-sky-600 border-sky-200",
    description: "ภาพถ่ายสินค้าลักชัวรี ไดคัตและจัดแสงฉากหลังแบบ 4K",
  },
];"""

if old_apps_list in content:
    content = content.replace(old_apps_list, new_apps_list, 1)
    print("APPS_LIST updated successfully")
else:
    print("Old APPS_LIST not matched exactly")

# 3. Update SaaS dropdown menu items to include direct Dashboard and Admin buttons
old_dropdown_loop = """                  <div className="grid grid-cols-1 gap-1 max-h-[360px] overflow-y-auto">
                    {APPS_LIST.map((app) => (
                      <a
                        key={app.id}
                        href={app.url}
                        target="_blank"
                        rel="noreferrer"
                        className="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left"
                      >
                        <div>
                          <div className="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">
                            {app.name}
                          </div>
                          <div className="text-[10px] text-stone-400 truncate max-w-[190px]">
                            {app.subdomain}
                          </div>
                        </div>
                        <span className="text-[9px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-mono font-medium">
                          :{app.port}
                        </span>
                      </a>
                    ))}
                  </div>"""

new_dropdown_loop = """                  <div className="grid grid-cols-1 gap-1.5 max-h-[380px] overflow-y-auto">
                    {APPS_LIST.map((app) => (
                      <div
                        key={app.id}
                        className="p-2 rounded-xl hover:bg-stone-50 transition-colors border border-transparent hover:border-black/[0.04]"
                      >
                        <div className="flex items-center justify-between">
                          <a
                            href={app.url}
                            target="_blank"
                            rel="noreferrer"
                            className="text-xs font-bold text-[#171717] hover:text-[#0569ff] transition-colors"
                          >
                            {app.name}
                          </a>
                          <span className="text-[9px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-mono font-medium">
                            :{app.port}
                          </span>
                        </div>
                        <div className="text-[10px] text-stone-400 truncate max-w-[210px] mb-1.5">
                          {app.subdomain}
                        </div>
                        <div className="flex items-center gap-1.5 pt-1 border-t border-stone-100">
                          <a
                            href={app.dashboardUrl}
                            target="_blank"
                            rel="noreferrer"
                            className="flex-1 py-1 px-1.5 rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-700 text-[10px] font-semibold text-center transition-colors flex items-center justify-center gap-1"
                          >
                            <span>💻</span>
                            <span>ห้องทำงาน</span>
                          </a>
                          <a
                            href={app.adminUrl}
                            target="_blank"
                            rel="noreferrer"
                            className="flex-1 py-1 px-1.5 rounded-lg bg-purple-50 hover:bg-purple-100 text-purple-700 border border-purple-200 text-[10px] font-semibold text-center transition-colors flex items-center justify-center gap-1"
                          >
                            <span>⚙️</span>
                            <span>หลังบ้าน</span>
                          </a>
                        </div>
                      </div>
                    ))}
                  </div>"""

if old_dropdown_loop in content:
    content = content.replace(old_dropdown_loop, new_dropdown_loop, 1)
    print("Dropdown loop updated successfully")
else:
    print("Old dropdown loop not matched exactly")

# 4. Update Tab 1 Container Card Footer
old_card_footer = """                  <div className="mt-4 pt-3.5 border-t border-black/[0.05] flex items-center justify-between text-xs">
                    <span className="text-[11px] text-stone-400">Uptime: {app.uptime}</span>
                    <a
                      href={app.url}
                      target="_blank"
                      rel="noreferrer"
                      className="font-semibold text-[#0569ff] hover:underline flex items-center gap-1"
                    >
                      <span>เปิดเว็บ</span>
                      <span>↗</span>
                    </a>
                  </div>"""

new_card_footer = """                  <div className="mt-4 pt-3 border-t border-black/[0.05] space-y-2">
                    <div className="flex items-center justify-between text-[11px] text-stone-400">
                      <span>Uptime: {app.uptime}</span>
                      <a
                        href={app.url}
                        target="_blank"
                        rel="noreferrer"
                        className="text-stone-500 hover:text-stone-800 transition-colors font-medium flex items-center gap-0.5"
                      >
                        <span>เปิดเว็บ</span>
                        <span>↗</span>
                      </a>
                    </div>
                    <div className="grid grid-cols-2 gap-1.5 pt-0.5">
                      <a
                        href={app.dashboardUrl}
                        target="_blank"
                        rel="noreferrer"
                        className="py-1.5 px-2 rounded-xl bg-stone-100 hover:bg-stone-200 text-stone-700 text-center font-semibold text-[11px] transition-colors flex items-center justify-center gap-1"
                      >
                        <span>💻</span>
                        <span>ห้องทำงาน</span>
                      </a>
                      <a
                        href={app.adminUrl}
                        target="_blank"
                        rel="noreferrer"
                        className="py-1.5 px-2 rounded-xl bg-purple-50 hover:bg-purple-100 text-purple-700 border border-purple-200 text-center font-semibold text-[11px] transition-colors flex items-center justify-center gap-1"
                      >
                        <span>⚙️</span>
                        <span>หลังบ้านแอดมิน</span>
                      </a>
                    </div>
                  </div>"""

if old_card_footer in content:
    content = content.replace(old_card_footer, new_card_footer, 1)
    print("Card footer updated successfully")
else:
    print("Old card footer not matched exactly")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("page.tsx written successfully!")
