"use client";

import React, { useState } from "react";
import OrbitShowcase from "./components/OrbitShowcase";

export default function HomePage() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"all" | "novel" | "social" | "sticker" | "clip" | "chat" | "mockup">("all");

  const services = [
    {
      id: "novel",
      name: "ReadAWrite Pro Studio",
      subname: "AI Novel & Storytelling Platform",
      tag: "novel.thaid.online",
      url: "https://novel.thaid.online",
      category: "novel",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "Flagship Service",
      description:
        "สตูดิโอแต่งนิยาย AI ระดับโปร รองรับระบบ Multi-Agent แต่งนิยายภาษาไทยสละสลวย จัดการคลังตัวละคร พล็อตเรื่อง และอัปโหลดตอนขึ้น ReadAWrite อัตโนมัติ",
      icon: "edit_note",
      accentColor: "#0074e2",
      features: [
        "แต่งนิยายไทยภาษาลื่นไหล สละสลวยด้วย Gemini Flash",
        "Character Bible จัดการตัวละครและปูมหลังแม่นยำ",
        "ProofAI ตรวจคำผิด ปรับสำนวน และจัดหน้าบทความ",
        "Playwright Auto-Upload ส่งบทขึ้น ReadAWrite โดยตรง",
      ],
      stats: { primary: "10 ตอนจบ", primaryLabel: "นิยายพร้อมลงขาย", secondary: "0 บาท", secondaryLabel: "ต้นทุน API (Vault Keys)" },
      actionText: "เปิดใช้งาน Novel Studio",
    },
    {
      id: "social",
      name: "Social Content Poster",
      subname: "Auto Content & Video Reels Engine",
      tag: "social.thaid.online",
      url: "https://social.thaid.online",
      category: "social",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "High Engagement",
      description:
        "ระบบปั่นคอนเทนต์เพจ Facebook อัตโนมัติ ดึงประเด็นข่าวไวรัล สรุปเนื้อหา เจนเนอเรตภาพอินโฟกราฟิก และตัดต่อวิดีโอ Reels พร้อมเสียงพากย์ไทย ยิงโพสต์ทุก 30 นาที",
      icon: "campaign",
      accentColor: "#1877f2",
      features: [
        "AI สรุปข่าวไวรัลและร่างแคปชันโพสต์เฟสบุ๊คคมกริบ",
        "FFmpeg เรนเดอร์คลิป Reels 9:16 สไตล์ข่าวด่วน/สารคดี",
        "ระบบคิวโพสต์อัตโนมัติตลอด 24 ชม. ไม่ต้องเฝ้าจอ",
        "เชื่อมต่อ Meta Graph API ปลอดภัย มีประวัติย้อนหลัง",
      ],
      stats: { primary: "ทุก 30 นาที", primaryLabel: "ความถี่โพสต์เพจ", secondary: "Reels 9:16", secondaryLabel: "วิดีโอความยาว 30-60 วิ" },
      actionText: "เปิดใช้งาน Social Poster",
    },
    {
      id: "sticker",
      name: "LINE Sticker Studio",
      subname: "AI Sticker Set & Merchandising",
      tag: "sticker.thaid.online",
      url: "https://sticker.thaid.online",
      category: "sticker",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "Creators Choice",
      description:
        "เครื่องมือสร้างชุดสติกเกอร์ไลน์อัตโนมัติ 8, 16, 24 และ 40 รูป คุมลายเส้นตัวละครให้คงที่ พร้อมไดคัทพื้นหลังใสและใส่ข้อความฟอนต์ไทยยอดนิยมในคลิกเดียว",
      icon: "sentiment_satisfied",
      accentColor: "#10b981",
      features: [
        "สร้างตัวละครหลักคงเส้นคงวาในทุกอิริยาบถและอารมณ์",
        "Auto Background Removal ไดคัทเนียนคมกริบ",
        "จัดสัดส่วนและฟอนต์ข้อความคำพูดยอดนิยมภาษาไทย",
        "Export แพ็กไฟล์ ZIP พร้อมส่งขึ้น LINE Creators Market",
      ],
      stats: { primary: "40 แอ็กชัน", primaryLabel: "ชุดสติกเกอร์ครบเซ็ต", secondary: "PNG/APNG", secondaryLabel: "มาตรฐาน LINE" },
      actionText: "เปิดใช้งาน Sticker Studio",
    },
    {
      id: "clip",
      name: "ThaiD Clip AI Studio",
      subname: "Automated 9:16 Shorts & Reels Studio",
      tag: "clip.thaid.online",
      url: "https://clip.thaid.online",
      category: "clip",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "High Viral",
      description:
        "ระบบสร้างคลิปสั้นแนวตั้ง 9:16 สำหรับ TikTok, Instagram Reels และ YouTube Shorts อัตโนมัติ ร่างสคริปต์ไวรัลด้วย Gemini พากย์เสียงไทย ผสมผสานภาพ AI/Google Flow Veo และซับคาราโอเกะ",
      icon: "movie",
      accentColor: "#ec4899",
      features: [
        "สคริปต์ไวรัลสไตล์รีวิวป้ายยา/สารคดี/ข่าวสั้น ด้วย Gemini 3.5",
        "พากย์เสียงภาษาไทยสมจริงพร้อมคำนวณไทม์มิ่งเป๊ะ",
        "ภาพแนวตั้ง 9:16 (1080x1920) พร้อม Ken Burns motion zoom",
        "ซับไตเติลคาราโอเกะฟอนต์ไทยไม่ลอย มิกซ์เพลงพื้นหลัง BGM",
      ],
      stats: { primary: "1080×1920", primaryLabel: "Full HD 9:16", secondary: "< 25 วิ", secondaryLabel: "ต่อการเรนเดอร์คลิป" },
      actionText: "เปิดใช้งาน Clip Studio",
    },
    {
      id: "chat",
      name: "ThaiD Smart Chat AI",
      subname: "AI Customer Service & LINE OA Assistant",
      tag: "chat.thaid.online",
      url: "https://chat.thaid.online",
      category: "chat",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "E-Commerce Suite",
      description:
        "แอดมิน AI ตอบแชทลูกค้าบน LINE Official Account ตลอด 24 ชั่วโมง มีคลังความรู้สินค้า โปรโมชั่น และข้อมูลจัดส่ง ช่วยปิดการขายอย่างสุภาพ ตอบกลับรวดเร็วภายใน 1 วินาที",
      icon: "forum",
      accentColor: "#06c755",
      features: [
        "เชื่อมต่อ Webhook กับ LINE Official Account ใน 2 นาที",
        "Knowledge Base จัดการข้อมูลสินค้า ราคา เลขบัญชี และ FAQ",
        "ตอบตรงประเด็น สุภาพ ปิดการขาย ช่วยลดต้นทุนจ้างแอดมิน",
        "จำลองห้องแชทเสมือนจริงในเบราว์เซอร์ก่อนเปิดใช้งานจริง",
      ],
      stats: { primary: "24/7", primaryLabel: "ตอบแชทอัตโนมัติ", secondary: "0 บาท", secondaryLabel: "ต้นทุน API (Vault Keys)" },
      actionText: "เปิดใช้งาน Smart Chat",
    },
    {
      id: "mockup",
      name: "ThaiD Mockup AI Studio",
      subname: "AI Product Photography & Mockup Platform",
      tag: "mockup.thaid.online",
      url: "https://mockup.thaid.online",
      category: "mockup",
      status: "ออนไลน์ (Live)",
      statusColor: "emerald",
      badge: "E-Commerce Pro",
      description:
        "สตูดิโอถ่ายภาพสินค้าและม็อกอัพระดับลักชัวรีด้วย AI ไดคัตพื้นหลังอัตโนมัติ วางสินค้าลงบนฉากหลังพรีเมียม สังเคราะห์แสงเงาเสมือนจริง สำหรับ Shopee, Lazada, TikTok และ Facebook",
      icon: "photo_camera",
      accentColor: "#e85a2d",
      features: [
        "ตัดพื้นหลังสินค้าอัตโนมัติด้วย AI Matting ภายใน 1 วินาที",
        "8 ฉากหลังพรีเซ็ตลักชัวรีจาก Google Flow (หินอ่อน, ไม้โอ๊ค, สปาหรู, โพเดียม)",
        "เจนฉากหลังใหม่ตามจินตนาการด้วย Custom AI Prompt Studio",
        "สังเคราะห์แสงเงา Contact & Cast Shadow สมจริงระดับสตูดิโอ",
      ],
      stats: { primary: "1080×1080", primaryLabel: "Full HD 1:1 / 4:5 / 9:16", secondary: "< 1 วิ", secondaryLabel: "ต่อการเรนเดอร์ภาพ" },
      actionText: "เปิดใช้งาน Mockup Studio",
    },
  ];

  const filteredServices =
    activeTab === "all"
      ? services
      : services.filter((s) => s.category === activeTab);

  return (
    <div className="min-h-screen bg-[#141414] text-[#ffffff] flex flex-col font-sans selection:bg-[#0074e2]/30 selection:text-white">
      
      {/* ======================================================== */}
      {/* 1. FASTWORK-STYLE DARK STUDIO NAVIGATION BAR (h-[54px])  */}
      {/* ======================================================== */}
      <header className="sticky top-0 z-50 h-[54px] border-b border-white/[0.08] bg-[#141414]/85 backdrop-blur-2xl">
        <div className="max-w-[1400px] mx-auto h-full px-4 sm:px-6 flex items-center justify-between gap-4">
          
          {/* Left: Brand Identity */}
          <div className="flex items-center gap-3">
            <a href="https://thaid.online" className="flex items-center gap-2.5 group">
              <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-[#0074e2] to-[#e85a2d] flex items-center justify-center text-white shadow-md shadow-[#0074e2]/25 group-hover:scale-105 transition-transform">
                <span className="material-symbols-outlined text-[19px]">hub</span>
              </div>
              <div className="flex flex-col">
                <span className="font-extrabold text-sm tracking-tight leading-none text-white flex items-center gap-1.5">
                  ThaiD<span className="text-[#0074e2]">.online</span>
                  <span className="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded-full bg-white/[0.08] text-stone-300 font-semibold border border-white/10">Studio</span>
                </span>
                <span className="text-[10px] text-stone-400 font-medium leading-tight">AI Multi-SaaS Platform</span>
              </div>
            </a>
          </div>

          {/* Center: Contextual Segmented Navigation Links */}
          <nav className="hidden lg:flex items-center gap-1 bg-white/[0.04] p-1 rounded-xl border border-white/[0.06] text-xs font-medium">
            <a
              href="https://thaid.online"
              className="px-3 py-1 rounded-lg text-white bg-white/10 shadow-xs font-semibold flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">hub</span>
              <span>Hub</span>
            </a>
            <a
              href="https://novel.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">edit_note</span>
              <span>นิยาย AI</span>
            </a>
            <a
              href="https://social.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">campaign</span>
              <span>โพสต์ FB</span>
            </a>
            <a
              href="https://sticker.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">sentiment_satisfied</span>
              <span>สติกเกอร์</span>
            </a>
            <a
              href="https://clip.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">movie</span>
              <span>คลิปสั้น AI</span>
            </a>
            <a
              href="https://chat.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">forum</span>
              <span>แชทบอท LINE</span>
            </a>
            <a
              href="https://mockup.thaid.online"
              className="px-3 py-1 rounded-lg text-stone-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <span className="material-symbols-outlined text-[14px]">photo_camera</span>
              <span>ม็อกอัพสินค้า</span>
            </a>
          </nav>

          {/* Right Controls: ThaiD Vault & Direct Launch */}
          <div className="flex items-center gap-2 flex-shrink-0">
            <a
              href="https://vault.thaid.online"
              className="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg border border-white/10 hover:border-white/25 text-stone-300 hover:text-white transition-all bg-white/[0.04]"
              title="คลังความปลอดภัยและ API Keys"
            >
              <span className="material-symbols-outlined text-[15px] text-amber-400">lock</span>
              <span>ThaiD Vault</span>
            </a>

            <a
              href="https://novel.thaid.online"
              className="inline-flex items-center gap-1.5 text-xs font-bold px-4 py-1.5 rounded-lg bg-[#0074e2] hover:bg-[#4276fc] text-white shadow-md shadow-[#0074e2]/25 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <span className="material-symbols-outlined text-[15px]">rocket_launch</span>
              <span>เข้าใช้งานระบบ</span>
            </a>

            {/* Mobile Menu Button */}
            <button
              type="button"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="lg:hidden p-1.5 rounded-lg text-stone-400 hover:text-white hover:bg-white/10"
              aria-label="Toggle menu"
            >
              <span className="material-symbols-outlined text-[22px]">
                {mobileMenuOpen ? "close" : "menu"}
              </span>
            </button>
          </div>
        </div>

        {/* Mobile Dropdown Sheet */}
        {mobileMenuOpen && (
          <div className="lg:hidden border-b border-white/[0.08] bg-[#141414]/98 backdrop-blur-2xl px-4 py-4 space-y-2 text-sm shadow-2xl">
            <a
              href="https://thaid.online"
              onClick={() => setMobileMenuOpen(false)}
              className="flex items-center justify-between px-3 py-2 rounded-lg font-semibold bg-white/10 text-white"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-[#0074e2]">hub</span>
                <span>ThaiD Hub (หน้าแรก)</span>
              </span>
              <span className="text-[10px] bg-[#0074e2]/20 text-[#0074e2] px-2 py-0.5 rounded font-bold border border-[#0074e2]/30">ACTIVE</span>
            </a>
            <a
              href="https://novel.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-[#0074e2]">edit_note</span>
                <span>นิยาย AI (Novel Studio)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <a
              href="https://social.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-[#1877f2]">campaign</span>
                <span>โพสต์ Facebook (Social Poster)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <a
              href="https://sticker.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-emerald-400">sentiment_satisfied</span>
                <span>สติกเกอร์ไลน์ (LINE Sticker)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <a
              href="https://clip.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-pink-400">movie</span>
                <span>คลิปสั้น AI (Clip Studio)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <a
              href="https://chat.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-green-400">forum</span>
                <span>แชทบอท LINE (Smart Chat)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <a
              href="https://mockup.thaid.online"
              className="flex items-center justify-between px-3 py-2 rounded-lg font-medium text-stone-300 hover:bg-white/5"
            >
              <span className="flex items-center gap-2">
                <span className="material-symbols-outlined text-[17px] text-orange-400">photo_camera</span>
                <span>ม็อกอัพสินค้า (Mockup Studio)</span>
              </span>
              <span className="material-symbols-outlined text-xs">arrow_outward</span>
            </a>
            <div className="pt-2 border-t border-white/[0.08]">
              <a
                href="https://novel.thaid.online"
                className="w-full py-2.5 rounded-xl bg-[#0074e2] text-white font-bold text-center flex items-center justify-center gap-2"
              >
                <span className="material-symbols-outlined text-[17px]">rocket_launch</span>
                <span>เปิดใช้งาน Novel Studio</span>
              </a>
            </div>
          </div>
        )}
      </header>

      {/* ======================================================== */}
      {/* 2. HERO SECTION (FASTWORK STUDIO DARK HERO)              */}
      {/* ======================================================== */}
      <section id="overview" className="relative pt-12 sm:pt-16 pb-12 overflow-hidden border-b border-white/[0.08]">
        
        {/* Ambient Subtle Gradients */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[350px] bg-gradient-to-tr from-[#0074e2]/15 via-[#e85a2d]/10 to-transparent blur-3xl pointer-events-none rounded-full" />

        <div className="max-w-[1400px] mx-auto px-4 sm:px-6 relative z-10 text-center">
          
          {/* Top Pill Chip */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/[0.05] border border-white/[0.1] shadow-xs text-xs font-semibold mb-6">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-stone-300">ThaiD Cloud Multi-SaaS Platform</span>
            <span className="text-stone-600">|</span>
            <span className="text-[#0074e2] font-bold">Fastwork-Style Studio UI</span>
          </div>

          {/* Main Headline */}
          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white max-w-4xl mx-auto leading-[1.15]">
            ศูนย์รวมโซลูชัน AI อัจฉริยะ <br className="hidden sm:inline" />
            <span className="bg-gradient-to-r from-[#0074e2] via-[#4276fc] to-[#e85a2d] bg-clip-text text-transparent">
              สำหรับครีเอเตอร์และธุรกิจไทย
            </span>
          </h1>

          <p className="mt-5 text-sm sm:text-lg text-stone-400 max-w-2xl mx-auto leading-relaxed">
            เชื่อมต่อเครื่องมือ AI ระดับโปรภายใต้ระบบนิเวศเดียวกัน ทั้งแต่งนิยาย ออโต้โพสต์โซเชียล สติกเกอร์ไลน์ คลิปสั้น แชทบอท และสตูดิโอม็อกอัพ
          </p>

          {/* Main Hero Actions */}
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 max-w-md mx-auto">
            <a
              href="https://novel.thaid.online"
              className="w-full sm:w-auto px-6 py-3 rounded-xl bg-[#0074e2] hover:bg-[#4276fc] text-white font-bold text-sm shadow-lg shadow-[#0074e2]/25 transition-all hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center gap-2"
            >
              <span className="material-symbols-outlined text-[18px]">edit_note</span>
              <span>เข้าสู่ Novel Studio</span>
            </a>
            <a
              href="https://social.thaid.online"
              className="w-full sm:w-auto px-6 py-3 rounded-xl bg-white/[0.06] hover:bg-white/[0.1] text-white font-semibold text-sm border border-white/[0.1] shadow-xs transition-all hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center gap-2"
            >
              <span className="material-symbols-outlined text-[18px]">campaign</span>
              <span>เข้าสู่ Social Poster</span>
            </a>
          </div>

          {/* ======================================================== */}
          {/* FASTWORK-STYLE 3D ORBIT SHOWCASE STAGE                   */}
          {/* ======================================================== */}
          <div className="mt-6">
            <OrbitShowcase />
          </div>

          {/* Live Ecosystem Bar */}
          <div className="mt-8 max-w-4xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-3 text-left">
            <div className="p-3.5 rounded-2xl bg-[#1b1b1e] border border-white/[0.08] shadow-xs">
              <div className="flex items-center gap-2 text-xs font-semibold text-stone-400">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>โฮสต์เซิร์ฟเวอร์</span>
              </div>
              <p className="mt-1 text-sm font-bold text-white">Oracle Cloud ARM</p>
              <p className="text-[11px] text-stone-500">2 OCPU · 12 GB RAM</p>
            </div>

            <div className="p-3.5 rounded-2xl bg-[#1b1b1e] border border-white/[0.08] shadow-xs">
              <div className="flex items-center gap-2 text-xs font-semibold text-stone-400">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>Reverse Proxy</span>
              </div>
              <p className="mt-1 text-sm font-bold text-white">Traefik v3.7</p>
              <p className="text-[11px] text-stone-500">Auto SSL Let&apos;s Encrypt</p>
            </div>

            <div className="p-3.5 rounded-2xl bg-[#1b1b1e] border border-white/[0.08] shadow-xs">
              <div className="flex items-center gap-2 text-xs font-semibold text-stone-400">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>โดเมนหลัก</span>
              </div>
              <p className="mt-1 text-sm font-bold text-white">ThaiD.online</p>
              <p className="text-[11px] text-stone-500">Wildcard DNS (*.thaid)</p>
            </div>

            <div className="p-3.5 rounded-2xl bg-[#1b1b1e] border border-white/[0.08] shadow-xs">
              <div className="flex items-center gap-2 text-xs font-semibold text-stone-400">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>ระบบคอนเทนเนอร์</span>
              </div>
              <p className="mt-1 text-sm font-bold text-white">Coolify v4</p>
              <p className="text-[11px] text-stone-500">8 Services Isolated</p>
            </div>
          </div>

        </div>
      </section>

      {/* ======================================================== */}
      {/* 3. PRODUCT SUITE CATALOG (BENTO GRID SHOWCASE)           */}
      {/* ======================================================== */}
      <section id="services" className="max-w-[1400px] w-full mx-auto px-4 sm:px-6 py-14 sm:py-20">
        
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <div className="inline-flex items-center gap-1.5 text-xs font-bold text-[#0074e2] uppercase tracking-wider mb-1">
              <span className="material-symbols-outlined text-[15px]">apps</span>
              <span>AI PRODUCT PORTFOLIO</span>
            </div>
            <h2 className="text-2xl sm:text-4xl font-extrabold tracking-tight text-white">
              ระบบและบริการทั้งหมดในเครือข่าย
            </h2>
          </div>

          {/* Segmented Filter Control */}
          <div className="flex flex-wrap items-center gap-1 bg-white/[0.04] p-1 rounded-xl border border-white/[0.08] text-xs">
            <button
              type="button"
              onClick={() => setActiveTab("all")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "all"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              ทั้งหมด (8)
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("novel")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "novel"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              นิยาย AI
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("social")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "social"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              โพสต์ Facebook
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("sticker")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "sticker"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              สติกเกอร์ไลน์
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("clip")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "clip"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              คลิปสั้น AI
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("chat")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "chat"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              แชทบอท LINE
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("mockup")}
              className={`px-3 py-1.5 rounded-lg transition-all ${
                activeTab === "mockup"
                  ? "bg-white/10 text-white shadow-xs font-bold"
                  : "text-stone-400 hover:text-white"
              }`}
            >
              ม็อกอัพสินค้า
            </button>
          </div>
        </div>

        {/* Bento Grid Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredServices.map((service) => (
            <div
              key={service.id}
              className="rounded-3xl bg-[#1b1b1e] border border-white/[0.08] p-6 sm:p-7 flex flex-col justify-between fastwork-card-hover fastwork-card-shadow"
            >
              <div>
                {/* Top Row: Icon + Badge + Status */}
                <div className="flex items-center justify-between gap-2 mb-5">
                  <div
                    className="w-12 h-12 rounded-2xl flex items-center justify-center text-white shadow-md"
                    style={{ backgroundColor: service.accentColor }}
                  >
                    <span className="material-symbols-outlined text-[24px]">
                      {service.icon}
                    </span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-[10px] sm:text-xs font-bold px-2.5 py-0.5 rounded-full bg-white/[0.08] text-stone-300 border border-white/[0.06]">
                      {service.badge}
                    </span>
                    <span
                      className={`inline-flex items-center gap-1 text-[11px] font-semibold px-2.5 py-0.5 rounded-full ${
                        service.statusColor === "emerald"
                          ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                          : "bg-amber-500/10 text-amber-400 border border-amber-500/20"
                      }`}
                    >
                      <span
                        className={`w-1.5 h-1.5 rounded-full ${
                          service.statusColor === "emerald"
                            ? "bg-emerald-500"
                            : "bg-amber-500"
                        }`}
                      />
                      {service.status}
                    </span>
                  </div>
                </div>

                {/* Service Name & Tag */}
                <h3 className="text-xl sm:text-2xl font-extrabold tracking-tight text-white">
                  {service.name}
                </h3>
                <p className="text-xs font-mono text-stone-400 mt-1">
                  {service.tag}
                </p>

                {/* Description */}
                <p className="mt-4 text-xs sm:text-sm text-stone-400 leading-relaxed">
                  {service.description}
                </p>

                {/* Feature Bullets */}
                <div className="mt-6 space-y-2.5 pt-5 border-t border-white/[0.08]">
                  {service.features.map((feat, idx) => (
                    <div key={idx} className="flex items-start gap-2.5 text-xs text-stone-300">
                      <span
                        className="material-symbols-outlined text-[16px] mt-0.5 flex-shrink-0"
                        style={{ color: service.accentColor }}
                      >
                        check_circle
                      </span>
                      <span>{feat}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Bottom Card Footer: KPIs + Action CTA */}
              <div className="mt-8 pt-5 border-t border-white/[0.08]">
                <div className="grid grid-cols-2 gap-3 mb-5">
                  <div className="p-3 rounded-xl bg-white/[0.04] border border-white/[0.05]">
                    <p className="text-base font-bold text-white">
                      {service.stats.primary}
                    </p>
                    <p className="text-[10px] text-stone-400">
                      {service.stats.primaryLabel}
                    </p>
                  </div>
                  <div className="p-3 rounded-xl bg-white/[0.04] border border-white/[0.05]">
                    <p className="text-base font-bold text-white">
                      {service.stats.secondary}
                    </p>
                    <p className="text-[10px] text-stone-400">
                      {service.stats.secondaryLabel}
                    </p>
                  </div>
                </div>

                <a
                  href={service.url}
                  className="w-full py-2.5 px-4 rounded-xl font-bold text-xs sm:text-sm text-center flex items-center justify-center gap-2 transition-all shadow-md hover:scale-[1.02] active:scale-[0.98]"
                  style={{
                    backgroundColor: service.accentColor,
                    color: "#ffffff",
                  }}
                >
                  <span>{service.actionText}</span>
                  <span className="material-symbols-outlined text-[16px]">
                    arrow_forward
                  </span>
                </a>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ======================================================== */}
      {/* 4. CLOUD INFRASTRUCTURE & SECURITY SPECIFICATION        */}
      {/* ======================================================== */}
      <section id="cloud-infra" className="py-14 sm:py-20 border-t border-white/[0.08] bg-[#111114]">
        <div className="max-w-[1400px] w-full mx-auto px-4 sm:px-6">
          <div className="max-w-2xl mb-10">
            <div className="inline-flex items-center gap-1.5 text-xs font-bold text-[#0074e2] uppercase tracking-wider mb-1">
              <span className="material-symbols-outlined text-[15px]">dns</span>
              <span>ENTERPRISE ARCHITECTURE</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight text-white">
              โครงสร้างระบบ Cloud มาตรฐานความปลอดภัยสูง
            </h2>
            <p className="mt-2 text-xs sm:text-sm text-stone-400">
              ทุก Subdomain ทำงานแยก Container อิสระ ไม่กระทบซึ่งกันและกัน มี Proxy คอยจัดการ Traffic และต่ออายุ SSL ใบรับรองความปลอดภัยตลอดชีพ
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-3xl bg-[#1b1b1e] border border-white/[0.08]">
              <div className="w-10 h-10 rounded-xl bg-[#0074e2]/15 text-[#0074e2] flex items-center justify-center mb-4">
                <span className="material-symbols-outlined text-[20px]">security</span>
              </div>
              <h4 className="font-bold text-base text-white">Automatic Let&apos;s Encrypt SSL</h4>
              <p className="mt-2 text-xs text-stone-400 leading-relaxed">
                ทุกการเชื่อมต่อผ่านพอร์ต 443 ถูกเข้ารหัสด้วยใบรับรอง TLS ล่าสุด ปลอดภัยจากการดักจับข้อมูล รองรับ HTTP/2 และ HTTP/3
              </p>
            </div>

            <div className="p-6 rounded-3xl bg-[#1b1b1e] border border-white/[0.08]">
              <div className="w-10 h-10 rounded-xl bg-[#0074e2]/15 text-[#0074e2] flex items-center justify-center mb-4">
                <span className="material-symbols-outlined text-[20px]">memory</span>
              </div>
              <h4 className="font-bold text-base text-white">Oracle Cloud Ampere ARM A1</h4>
              <p className="mt-2 text-xs text-stone-400 leading-relaxed">
                ประมวลผลด้วย CPU สถาปัตยกรรม ARM 2 OCPU และ RAM 12 GB ช่วยให้รันโมเดลภาษาและการเรนเดอร์วิดีโอได้อย่างรวดเร็ว
              </p>
            </div>

            <div className="p-6 rounded-3xl bg-[#1b1b1e] border border-white/[0.08]">
              <div className="w-10 h-10 rounded-xl bg-emerald-500/15 text-emerald-400 flex items-center justify-center mb-4">
                <span className="material-symbols-outlined text-[20px]">sync</span>
              </div>
              <h4 className="font-bold text-base text-white">Zero-Downtime Deployment</h4>
              <p className="mt-2 text-xs text-stone-400 leading-relaxed">
                อัปเดตโค้ดใหม่ผ่าน GitHub Webhook และ Coolify อัตโนมัติด้วย Rolling Updates เว็บไซต์ทำงานต่อเนื่องโดยไม่มีจังหวะสะดุด
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ======================================================== */}
      {/* 5. FOOTER (FASTWORK MINIMALIST STUDIO FOOTER)            */}
      {/* ======================================================== */}
      <footer className="mt-auto border-t border-white/[0.08] bg-[#111114] py-10 text-xs text-stone-400">
        <div className="max-w-[1400px] w-full mx-auto px-4 sm:px-6">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pb-6 border-b border-white/[0.08]">
            <div className="flex items-center gap-2">
              <div className="w-5 h-5 rounded-md bg-[#0074e2] flex items-center justify-center text-white">
                <span className="material-symbols-outlined text-[13px]">hub</span>
              </div>
              <span className="font-bold text-sm text-white">ThaiD.online</span>
              <span className="text-[11px] text-stone-500">· Multi-SaaS AI Ecosystem</span>
            </div>
            <div className="flex flex-wrap items-center gap-4 text-xs">
              <a href="https://novel.thaid.online" className="hover:text-white transition-colors">
                novel.thaid.online
              </a>
              <a href="https://social.thaid.online" className="hover:text-white transition-colors">
                social.thaid.online
              </a>
              <a href="https://sticker.thaid.online" className="hover:text-white transition-colors">
                sticker.thaid.online
              </a>
              <a href="https://clip.thaid.online" className="hover:text-white transition-colors">
                clip.thaid.online
              </a>
              <a href="https://chat.thaid.online" className="hover:text-white transition-colors">
                chat.thaid.online
              </a>
              <a href="https://mockup.thaid.online" className="hover:text-white transition-colors">
                mockup.thaid.online
              </a>
            </div>
          </div>

          <div className="pt-6 flex flex-col sm:flex-row items-center justify-between gap-2 text-[11px] text-stone-500">
            <p>© 2026 ThaiD.online. All rights reserved. สงวนลิขสิทธิ์ระบบและเครื่องหมายบริการ</p>
            <p className="flex items-center gap-2">
              <span>Host: Node 2 (Oracle Cloud 12GB ARM)</span>
              <span>·</span>
              <span>Protected with SSL/TLS</span>
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
