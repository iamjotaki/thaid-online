"use client";

import React, { useState, useEffect } from "react";
import Image from "next/image";

interface ServiceItem {
  id: string;
  name: string;
  subname: string;
  tag: string;
  url: string;
  category: "novel" | "social" | "sticker" | "clip" | "chat" | "mockup" | "vault";
  status: string;
  badge: string;
  description: string;
  icon: string;
  image: string;
  creator: string;
  location: string;
  tilt: string;
  features: string[];
  stats: { primary: string; primaryLabel: string; secondary: string; secondaryLabel: string };
  actionText: string;
}

export default function HomePage() {
  const [activeTab, setActiveTab] = useState<string>("all");
  const [countdown, setCountdown] = useState({ days: 19, hours: 18, mins: 30, secs: 49 });

  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev.secs > 0) return { ...prev, secs: prev.secs - 1 };
        if (prev.mins > 0) return { ...prev, mins: 59, secs: 59 };
        if (prev.hours > 0) return { ...prev, hours: prev.hours - 1, mins: 59, secs: 59 };
        return { ...prev, days: Math.max(0, prev.days - 1), hours: 23, mins: 59, secs: 59 };
      });
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const services: ServiceItem[] = [
    {
      id: "mockup",
      name: "ThaiD Mockup AI Studio",
      subname: "AI Product Photography & Studio",
      tag: "mockup.thaid.online",
      url: "https://mockup.thaid.online",
      category: "mockup",
      status: "พร้อมใช้งาน",
      badge: "E-Commerce",
      description: "สตูดิโอถ่ายภาพสินค้าและม็อกอัพระดับลักชัวรีด้วย AI ไดคัตพื้นหลังอัตโนมัติ จัดวางฉากพรีเมียม สังเคราะห์แสงเงาสมจริง",
      icon: "photo_camera",
      image: "/cards/cafe_marble.jpg",
      creator: "Weng Kitsana",
      location: "Photographer · Bangkok",
      tilt: "-rotate-6",
      features: [
        "ตัดพื้นหลังอัตโนมัติด้วย AI Matting ภายใน 1 วินาที",
        "8 ฉากหลังพรีเซ็ตลักชัวรีจาก Google Flow",
        "สังเคราะห์แสงเงา Contact & Cast Shadow สมจริง",
      ],
      stats: { primary: "1080×1080", primaryLabel: "Full HD Studio", secondary: "< 1 วิ", secondaryLabel: "เรนเดอร์ภาพ" },
      actionText: "เปิดใช้งาน Mockup Studio",
    },
    {
      id: "novel",
      name: "ReadAWrite Pro Studio",
      subname: "AI Novel & Chapter Generator",
      tag: "novel.thaid.online",
      url: "https://novel.thaid.online",
      category: "novel",
      status: "พร้อมใช้งาน",
      badge: "Most Popular",
      description: "ระบบผู้ช่วยนักเขียนอัจฉริยะ วางโครงเรื่อง แต่งนิยาย 10 ตอนจบ พร้อมเชื่อมต่ออัปโหลดขึ้น ReadAWrite.com อัตโนมัติ",
      icon: "edit_note",
      image: "/cards/luxury_spa.jpg",
      creator: "Chapavich T.",
      location: "Fiction Author · Chiang Mai",
      tilt: "rotate-2",
      features: [
        "Gemini Multi-Agent Plot & Chapter Engine",
        "ProofAI ตรวจคำผิดและขัดเกลาสำนวนภาษาไทย",
        "อัปโหลดบทและภาพปกขึ้น ReadAWrite อัตโนมัติ",
      ],
      stats: { primary: "10 ตอนจบ", primaryLabel: "โครงเรื่องอัตโนมัติ", secondary: "50,000", secondaryLabel: "โควตาคำทดลองฟรี" },
      actionText: "เปิดใช้งาน Novel Studio",
    },
    {
      id: "social",
      name: "Social Auto-Poster Pro",
      subname: "Facebook Content & Video Reels",
      tag: "social.thaid.online",
      url: "https://social.thaid.online",
      category: "social",
      status: "พร้อมใช้งาน",
      badge: "High Viral",
      description: "ระบบ AI ค้นหาข่าวไวรัล เรียบเรียงใหม่ เจนภาพประกอบและตัดต่อวิดีโอสั้นพร้อมเสียงพากย์ ยิงโพสต์ขึ้น Facebook Page 24 ชม.",
      icon: "campaign",
      image: "/cards/neon_cyberpunk.jpg",
      creator: "LEOBEER",
      location: "Social Producer · Bangkok",
      tilt: "-rotate-3",
      features: [
        "AI ดึงฟีดข่าวกีฬาและไลฟ์สไตล์ไวรัลอัตโนมัติ",
        "ตัดต่อวิดีโอสั้นพร้อมเสียงพากย์ภาษาไทยและซับไตเติล",
        "โพสต์ขึ้น Facebook Page และ Group อัตโนมัติ",
      ],
      stats: { primary: "24 ชม.", primaryLabel: "ทำงานอัตโนมัติ", secondary: "100%", secondaryLabel: "เชื่อมต่อ FB Graph API" },
      actionText: "เปิดใช้งาน Social Poster",
    },
    {
      id: "clip",
      name: "AI Clip & Reels Studio",
      subname: "Short-form Vertical Video Studio",
      tag: "clip.thaid.online",
      url: "https://clip.thaid.online",
      category: "clip",
      status: "พร้อมใช้งาน",
      badge: "TikTok & Reels",
      description: "สตูดิโอสร้างคลิปวิดีโอสั้นแนวตั้ง 9:16 ด้วย AI สคริปต์รีวิวป้ายยา พากย์เสียงไทย ผสมภาพ AI และซับไตเติลคาราโอเกะ",
      icon: "movie",
      image: "/cards/golden_beach.jpg",
      creator: "Nguyen Van Nam",
      location: "Video Creator · Phuket",
      tilt: "rotate-6",
      features: [
        "เขียนสคริปต์วิดีโอสั้นไวรัล 30-60 วินาทีตามสไตล์",
        "เจนภาพประกอบแต่ละฉากด้วย AI ความละเอียดสูง",
        "สังเคราะห์เสียงพากย์ไทยและเรนเดอร์ซับไตเติลคาราโอเกะ",
      ],
      stats: { primary: "9:16", primaryLabel: "แนวตั้ง TikTok/Reels", secondary: "1080p", secondaryLabel: "ความละเอียดสูง" },
      actionText: "เปิดใช้งาน Clip Studio",
    },
    {
      id: "sticker",
      name: "LINE Sticker AI Studio",
      subname: "LINE Creators Market Studio",
      tag: "sticker.thaid.online",
      url: "https://sticker.thaid.online",
      category: "sticker",
      status: "พร้อมใช้งาน",
      badge: "Creators Choice",
      description: "สร้างชุดสติกเกอร์ไลน์ครบเซ็ต 8, 16, 24, 40 รูปด้วย AI ไดคัตพื้นหลังโปร่งใส ขอบขาวไดคัต มาตรฐาน LINE Creators",
      icon: "sentiment_satisfied",
      image: "/cards/nature_wood.jpg",
      creator: "Peter Sato",
      location: "Character Designer · Osaka",
      tilt: "-rotate-4",
      features: [
        "คลังคำพูดยอดนิยมภาษาไทยสำหรับสติกเกอร์ไลน์",
        "สร้างตัวละครคาแรกเตอร์คงที่ในทุกแอ็กชัน",
        "ไดคัตพื้นหลังโปร่งใสใส่ขอบขาวพร้อมดาวน์โหลด ZIP",
      ],
      stats: { primary: "40 แอ็กชัน", primaryLabel: "ชุดสมบูรณ์", secondary: "370×320", secondaryLabel: "มาตรฐาน LINE API" },
      actionText: "เปิดใช้งาน Sticker Studio",
    },
    {
      id: "chat",
      name: "Smart Chat AI",
      subname: "LINE OA 24/7 AI Assistant",
      tag: "chat.thaid.online",
      url: "https://chat.thaid.online",
      category: "chat",
      status: "พร้อมใช้งาน",
      badge: "E-Commerce",
      description: "ระบบ AI แอดมินตอบแชทลูกค้าบน LINE Official Account อัจฉริยะ 24 ชั่วโมง มีคลังความรู้สินค้า ปิดการขาย ตอบไวใน 1 วินาที",
      icon: "forum",
      image: "/cards/cozy_living.jpg",
      creator: "MOD SUPACHA",
      location: "E-Commerce Admin · Bangkok",
      tilt: "rotate-4",
      features: [
        "เชื่อมต่อ LINE Messaging API Webhook พร้อมใช้งาน",
        "คลังข้อมูลสินค้า คำถามที่พบบ่อย และเงื่อนไขบริการ",
        "ตอบตรงประเด็น สุภาพ ปิดการขาย ช่วยลดต้นทุนแอดมิน",
      ],
      stats: { primary: "24/7", primaryLabel: "ตอบแชทอัตโนมัติ", secondary: "1 วินาที", secondaryLabel: "ความเร็วตอบกลับ" },
      actionText: "เปิดใช้งาน Smart Chat",
    },
    {
      id: "vault",
      name: "ThaiD Vault",
      subname: "Personal Cloud Vault & Security",
      tag: "vault.thaid.online",
      url: "https://vault.thaid.online",
      category: "vault",
      status: "พร้อมใช้งาน",
      badge: "Security",
      description: "คลังเก็บข้อมูลส่วนตัว กุญแจ API Keys และระบบความปลอดภัย เข้ารหัสข้อมูลระดับทหาร AES-256",
      icon: "lock",
      image: "/cards/podium_minimal.jpg",
      creator: "Pakinchit",
      location: "Security Engineer · Bangkok",
      tilt: "-rotate-3",
      features: [
        "เข้ารหัสความปลอดภัยระดับทหาร AES-256",
        "จัดเก็บ Gemini API Keys และหมุนเวียนคีย์อัตโนมัติ",
        "สำรองข้อมูลและจัดการสภาพแวดล้อมระบบนิเวศ",
      ],
      stats: { primary: "AES-256", primaryLabel: "การเข้ารหัสข้อมูล", secondary: "80 Keys", secondaryLabel: "คลังคีย์ความปลอดภัย" },
      actionText: "เปิดใช้งาน ThaiD Vault",
    },
    {
      id: "studio_hub",
      name: "ThaiD Cloud Ecosystem",
      subname: "Central SaaS Orchestration",
      tag: "thaid.online",
      url: "https://thaid.online",
      category: "mockup",
      status: "พร้อมใช้งาน",
      badge: "Enterprise",
      description: "ศูนย์กลางควบคุมและเชื่อมต่อทุกบริการในเครือ ThaiD ผ่าน Single Sign-On และสถาปัตยกรรม Microservices ระดับสูง",
      icon: "hub",
      image: "/cards/studio_pastel.jpg",
      creator: "ThaiD Team",
      location: "Core Engineering · Thailand",
      tilt: "rotate-3",
      features: [
        "Single Sign-On และการจัดการโดเมนเดียว",
        "เซิร์ฟเวอร์ความเร็วสูง Oracle Cloud ARM64",
        "Reverse Proxy Traefik พร้อม SSL อัตโนมัติ",
      ],
      stats: { primary: "8 บริการ", primaryLabel: "ระบบนิเวศ AI", secondary: "0.14s", secondaryLabel: "เวลาตอบสนองเซิร์ฟเวอร์" },
      actionText: "สำรวจระบบทั้งหมด",
    },
  ];

  const filteredServices = activeTab === "all" ? services : services.filter((s) => s.category === activeTab);

  return (
    <div className="min-h-screen bg-white text-[#171717] font-sans antialiased overflow-x-hidden selection:bg-[#0569ff]/15 selection:text-[#0569ff]">
      
      {/* ======================================================== */}
      {/* 1. FASTWORK FLOATING PILL HEADER                         */}
      {/* ======================================================== */}
      <header className="sticky top-0 z-50 pt-3 px-4 sm:px-6 pointer-events-none">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          
          {/* Invisible Left Spacer */}
          <div className="w-24 hidden sm:block" />

          {/* Centered Floating Fastwork-Style Brand Pill */}
          <div className="pointer-events-auto inline-flex items-center gap-2.5 px-4 py-2 rounded-full border border-black/[0.08] bg-white/80 backdrop-blur-xl shadow-sm hover:shadow-md transition-all">
            <a href="https://thaid.online" className="flex items-center gap-2 text-[#171717]">
              <div className="w-5 h-5 rounded-full bg-[#171717] flex items-center justify-center text-white text-[11px] font-bold">
                ✦
              </div>
              <span className="font-bold text-sm tracking-tight text-[#171717]">
                ThaiD<span className="text-[#0569ff]">.online</span>
              </span>
            </a>
          </div>

          {/* Right Language / Action Pill */}
          <div className="pointer-events-auto flex items-center gap-2">
            <a
              href="https://vault.thaid.online"
              className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full border border-black/[0.08] bg-white/80 backdrop-blur-xl text-xs font-semibold text-[#171717] hover:bg-black/5 transition-colors shadow-xs"
            >
              <span className="material-symbols-outlined text-[15px] text-[#0569ff]">lock</span>
              <span>Vault</span>
            </a>
            <div className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/80 backdrop-blur-xl text-xs font-medium text-[#171717]">
              <span className="text-[13px]">🌐</span>
              <span className="font-semibold">TH</span>
            </div>
          </div>

        </div>
      </header>

      {/* ======================================================== */}
      {/* 2. FASTWORK EXACT HERO STAGE WITH 3D SCATTERED CARDS      */}
      {/* ======================================================== */}
      <section className="relative min-h-[85vh] sm:min-h-[92vh] flex flex-col items-center justify-center pt-8 pb-16 px-4 overflow-hidden">
        
        {/* ======================================================== */}
        {/* SCATTERED 3D FLOATING PORTFOLIO CARDS (FASTWORK SIGNATURE) */}
        {/* ======================================================== */}
        
        {/* LEFT COLUMN 1 (Outer Left, tilted -8deg) */}
        <div className="hidden xl:block absolute left-4 2xl:left-12 top-[12%] z-10">
          <a
            href="https://mockup.thaid.online"
            className="block w-[220px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] -rotate-6 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[155px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/cafe_marble.jpg" alt="Mockup AI" fill className="object-cover" />
            </div>
            <div className="mt-2.5 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#171717] text-white">W</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">Weng Kitsana</p>
                <p className="text-[10px] text-[#737373] truncate">Photographer · Bangkok</p>
              </div>
            </div>
          </a>
        </div>

        {/* LEFT COLUMN 2 (Inner Left Top, tilted 2deg) */}
        <div className="hidden lg:block absolute left-[12%] 2xl:left-[17%] top-[5%] z-20">
          <a
            href="https://novel.thaid.online"
            className="block w-[200px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] rotate-2 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[140px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/luxury_spa.jpg" alt="Novel Studio" fill className="object-cover" />
            </div>
            <div className="mt-2 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#0569ff] text-white">C</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">Chapavich T.</p>
                <p className="text-[10px] text-[#737373] truncate">Novel Author · Chiang Mai</p>
              </div>
            </div>
          </a>
        </div>

        {/* LEFT COLUMN 3 (Inner Left Bottom, tilted -4deg) */}
        <div className="hidden lg:block absolute left-[5%] 2xl:left-[10%] bottom-[8%] z-10">
          <a
            href="https://social.thaid.online"
            className="block w-[210px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] -rotate-3 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[150px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/neon_cyberpunk.jpg" alt="Social Poster" fill className="object-cover" />
            </div>
            <div className="mt-2.5 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#e85a2d] text-white">L</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">LEOBEER</p>
                <p className="text-[10px] text-[#737373] truncate">Viral Editor · Bangkok</p>
              </div>
            </div>
          </a>
        </div>

        {/* RIGHT COLUMN 1 (Outer Right Top, tilted 6deg) */}
        <div className="hidden xl:block absolute right-4 2xl:right-12 top-[10%] z-10">
          <a
            href="https://clip.thaid.online"
            className="block w-[215px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] rotate-6 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[150px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/golden_beach.jpg" alt="Clip AI" fill className="object-cover" />
            </div>
            <div className="mt-2.5 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#ec4899] text-white">N</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">Nguyen Van Nam</p>
                <p className="text-[10px] text-[#737373] truncate">Video Creator · Phuket</p>
              </div>
            </div>
          </a>
        </div>

        {/* RIGHT COLUMN 2 (Inner Right Upper, tilted -5deg) */}
        <div className="hidden lg:block absolute right-[12%] 2xl:right-[17%] top-[6%] z-20">
          <a
            href="https://sticker.thaid.online"
            className="block w-[205px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] -rotate-4 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[145px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/nature_wood.jpg" alt="LINE Sticker" fill className="object-cover" />
            </div>
            <div className="mt-2 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#10b981] text-white">P</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">Peter Sato</p>
                <p className="text-[10px] text-[#737373] truncate">Sticker Designer · Osaka</p>
              </div>
            </div>
          </a>
        </div>

        {/* RIGHT COLUMN 3 (Inner Right Lower, tilted 4deg) */}
        <div className="hidden lg:block absolute right-[6%] 2xl:right-[11%] bottom-[7%] z-10">
          <a
            href="https://chat.thaid.online"
            className="block w-[210px] rounded-2xl bg-white border border-black/[0.08] p-2.5 shadow-[0_20px_45px_rgba(0,0,0,0.07)] hover:shadow-[0_25px_55px_rgba(0,0,0,0.14)] rotate-4 hover:rotate-0 hover:scale-105 transition-all duration-300"
          >
            <div className="relative w-full h-[150px] rounded-xl overflow-hidden bg-stone-100">
              <Image src="/cards/cozy_living.jpg" alt="Smart Chat" fill className="object-cover" />
            </div>
            <div className="mt-2.5 flex items-center gap-2 px-1">
              <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0">
                <span className="w-full h-full flex items-center justify-center text-xs font-bold bg-[#06c755] text-white">M</span>
                <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-2 border-white" />
              </div>
              <div className="flex flex-col min-w-0">
                <p className="text-xs font-bold text-[#171717] truncate leading-tight">MOD SUPACHA</p>
                <p className="text-[10px] text-[#737373] truncate">E-Commerce Admin · Bangkok</p>
              </div>
            </div>
          </a>
        </div>

        {/* ======================================================== */}
        {/* CENTER HERO COPY & ACTIONS (100% FASTWORK MATCH)          */}
        {/* ======================================================== */}
        <div className="relative z-30 max-w-2xl mx-auto text-center flex flex-col items-center">
          
          {/* Main Headline with Stylized Thai Calligraphy */}
          <h1 className="text-4xl sm:text-6xl md:text-7xl font-extrabold tracking-tight text-[#171717] leading-[1.12]">
            Show the world <br />
            what <span className="font-['Charm'] italic text-5xl sm:text-7xl md:text-8xl px-2 font-normal text-[#171717]">คุณ</span> can do
          </h1>

          {/* Subtitle */}
          <p className="mt-4 sm:mt-5 text-sm sm:text-base md:text-lg text-[#737373] max-w-lg mx-auto font-normal">
            In the age of AI, your portfolio proves why clients need you.
          </p>

          {/* Thai Secondary Subtitle */}
          <p className="mt-1 text-xs sm:text-sm text-stone-400 font-medium">
            ศูนย์รวมโซลูชัน AI อัจฉริยะ สำหรับครีเอเตอร์และธุรกิจไทย
          </p>

          {/* Countdown / Live Metrics Timer (Fastwork 4-Box Signature) */}
          <div className="mt-7 sm:mt-9 flex items-center justify-center gap-2 sm:gap-3.5">
            <div className="w-[66px] sm:w-[76px] py-3 rounded-2xl bg-[#f8f9fa] border border-black/[0.06] text-center shadow-xs">
              <span className="block text-xl sm:text-3xl font-extrabold text-[#171717] tracking-tight">
                {String(countdown.days).padStart(2, "0")}
              </span>
              <span className="block text-[10px] sm:text-[11px] text-[#737373] font-medium mt-0.5">days</span>
            </div>
            <div className="w-[66px] sm:w-[76px] py-3 rounded-2xl bg-[#f8f9fa] border border-black/[0.06] text-center shadow-xs">
              <span className="block text-xl sm:text-3xl font-extrabold text-[#171717] tracking-tight">
                {String(countdown.hours).padStart(2, "0")}
              </span>
              <span className="block text-[10px] sm:text-[11px] text-[#737373] font-medium mt-0.5">hours</span>
            </div>
            <div className="w-[66px] sm:w-[76px] py-3 rounded-2xl bg-[#f8f9fa] border border-black/[0.06] text-center shadow-xs">
              <span className="block text-xl sm:text-3xl font-extrabold text-[#171717] tracking-tight">
                {String(countdown.mins).padStart(2, "0")}
              </span>
              <span className="block text-[10px] sm:text-[11px] text-[#737373] font-medium mt-0.5">mins</span>
            </div>
            <div className="w-[66px] sm:w-[76px] py-3 rounded-2xl bg-[#f8f9fa] border border-black/[0.06] text-center shadow-xs">
              <span className="block text-xl sm:text-3xl font-extrabold text-[#171717] tracking-tight">
                {String(countdown.secs).padStart(2, "0")}
              </span>
              <span className="block text-[10px] sm:text-[11px] text-[#737373] font-medium mt-0.5">seconds</span>
            </div>
          </div>

          {/* Primary Action Button (Fastwork Solid Black Pill) */}
          <div className="mt-8">
            <a
              href="#ecosystem"
              className="inline-flex items-center justify-center px-9 py-3.5 rounded-full bg-[#1f242d] hover:bg-black text-white font-semibold text-sm shadow-md hover:shadow-xl hover:scale-105 active:scale-95 transition-all duration-200"
            >
              Get started
            </a>
          </div>

          {/* Scroll Down Indicator */}
          <div className="mt-12 flex flex-col items-center gap-1 text-[#737373] text-[11px] font-medium">
            <span>Scroll down</span>
            <span className="material-symbols-outlined text-sm animate-bounce">expand_more</span>
          </div>

        </div>

      </section>

      {/* ======================================================== */}
      {/* 3. PLATFORMS DIRECTORY & ECOSYSTEM (CLEAN WHITE EDITORIAL) */}
      {/* ======================================================== */}
      <section id="ecosystem" className="py-16 sm:py-24 px-4 sm:px-6 bg-[#fafafa] border-t border-black/[0.06]">
        <div className="max-w-7xl mx-auto">
          
          {/* Section Header */}
          <div className="text-center max-w-2xl mx-auto mb-10">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white border border-black/[0.08] text-xs font-semibold text-[#171717] mb-3 shadow-xs">
              <span className="w-2 h-2 rounded-full bg-[#22c55e]" />
              <span>ThaiD Multi-SaaS Architecture</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[#171717]">
              เลือกใช้งาน 8 แพลตฟอร์ม AI ในเครือ
            </h2>
            <p className="mt-2 text-sm sm:text-base text-[#737373]">
              ทุกเครื่องมือถูกออกแบบมาเพื่อคนไทยโดยเฉพาะ เร็ว แรง ไร้ขีดจำกัด
            </p>
          </div>

          {/* Segmented Category Filter Pills */}
          <div className="flex items-center justify-center gap-2 overflow-x-auto pb-4 mb-8">
            {[
              { id: "all", label: "ทั้งหมด (All)" },
              { id: "mockup", label: "ม็อกอัพสินค้า" },
              { id: "novel", label: "นิยาย AI" },
              { id: "social", label: "ออโต้โพสต์ FB" },
              { id: "clip", label: "คลิปสั้น AI" },
              { id: "sticker", label: "สติกเกอร์ไลน์" },
              { id: "chat", label: "แชทบอท LINE" },
              { id: "vault", label: "คลังความปลอดภัย" },
            ].map((tab) => (
              <button
                key={tab.id}
                type="button"
                onClick={() => setActiveTab(tab.id)}
                className={`px-4 py-2 rounded-full text-xs font-semibold whitespace-nowrap transition-all ${
                  activeTab === tab.id
                    ? "bg-[#1f242d] text-white shadow-xs"
                    : "bg-white text-[#737373] hover:text-[#171717] border border-black/[0.08]"
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* Grid of 8 Service Cards (Fastwork Clean White Style) */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
            {filteredServices.map((service) => (
              <div
                key={service.id}
                className="rounded-2xl bg-white border border-black/[0.08] p-5 flex flex-col justify-between shadow-[0_10px_30px_rgba(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgba(0,0,0,0.1)] hover:-translate-y-1 transition-all duration-300 group"
              >
                <div>
                  {/* Photo Preview Thumbnail */}
                  <div className="relative w-full h-[160px] rounded-xl overflow-hidden bg-stone-100 mb-4">
                    <Image src={service.image} alt={service.name} fill className="object-cover group-hover:scale-105 transition-transform duration-300" />
                    <div className="absolute top-2.5 right-2.5 px-2 py-0.5 rounded-full bg-white/90 backdrop-blur-md text-[10px] font-bold text-[#171717] border border-black/5 shadow-xs">
                      {service.badge}
                    </div>
                  </div>

                  {/* Title & Domain */}
                  <div className="flex items-center gap-2 mb-1">
                    <span className="w-2 h-2 rounded-full bg-[#22c55e]" />
                    <span className="text-[11px] font-mono text-[#737373]">{service.tag}</span>
                  </div>
                  <h3 className="text-base font-bold text-[#171717] tracking-tight group-hover:text-[#0569ff] transition-colors">
                    {service.name}
                  </h3>
                  <p className="mt-2 text-xs text-[#737373] line-clamp-2 leading-relaxed">
                    {service.description}
                  </p>

                  {/* Features Bullet List */}
                  <ul className="mt-4 space-y-1.5 border-t border-black/[0.06] pt-3 text-[11px] text-stone-600">
                    {service.features.map((f, i) => (
                      <li key={i} className="flex items-center gap-1.5">
                        <span className="text-[#0569ff] font-bold">✓</span>
                        <span className="truncate">{f}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Footer Action */}
                <div className="mt-5 pt-3 border-t border-black/[0.06] flex items-center justify-between">
                  <div>
                    <span className="text-[10px] text-[#737373] block">{service.stats.primaryLabel}</span>
                    <span className="text-xs font-extrabold text-[#171717]">{service.stats.primary}</span>
                  </div>
                  <a
                    href={service.url}
                    className="inline-flex items-center gap-1 px-4 py-2 rounded-full bg-[#1f242d] hover:bg-black text-white text-xs font-semibold shadow-xs transition-colors"
                  >
                    <span>เปิดระบบ</span>
                    <span className="material-symbols-outlined text-[13px]">arrow_outward</span>
                  </a>
                </div>
              </div>
            ))}
          </div>

          {/* Infrastructure Metrics Bar */}
          <div className="mt-14 max-w-4xl mx-auto grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="p-4 rounded-2xl bg-white border border-black/[0.08] text-center shadow-xs">
              <span className="block text-xs font-medium text-[#737373]">Cloud Infrastructure</span>
              <span className="block text-base font-bold text-[#171717] mt-1">Oracle Cloud ARM</span>
              <span className="block text-[11px] text-[#22c55e] font-semibold">2 OCPU · 12 GB RAM</span>
            </div>
            <div className="p-4 rounded-2xl bg-white border border-black/[0.08] text-center shadow-xs">
              <span className="block text-xs font-medium text-[#737373]">Reverse Proxy</span>
              <span className="block text-base font-bold text-[#171717] mt-1">Traefik v3.7</span>
              <span className="block text-[11px] text-[#22c55e] font-semibold">Auto SSL Let&apos;s Encrypt</span>
            </div>
            <div className="p-4 rounded-2xl bg-white border border-black/[0.08] text-center shadow-xs">
              <span className="block text-xs font-medium text-[#737373]">DNS Routing</span>
              <span className="block text-base font-bold text-[#171717] mt-1">ThaiD.online</span>
              <span className="block text-[11px] text-[#22c55e] font-semibold">Wildcard Multi-Domain</span>
            </div>
            <div className="p-4 rounded-2xl bg-white border border-black/[0.08] text-center shadow-xs">
              <span className="block text-xs font-medium text-[#737373]">Container Engine</span>
              <span className="block text-base font-bold text-[#171717] mt-1">Coolify v4</span>
              <span className="block text-[11px] text-[#22c55e] font-semibold">8 Services Isolated</span>
            </div>
          </div>

        </div>
      </section>

      {/* ======================================================== */}
      {/* 4. FOOTER                                                */}
      {/* ======================================================== */}
      <footer className="py-10 px-4 border-t border-black/[0.06] bg-white text-center text-xs text-[#737373]">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
          <p>© 2026 ThaiD.online — All rights reserved.</p>
          <div className="flex items-center gap-4">
            <a href="https://thaid.online" className="hover:text-[#171717] transition-colors">Hub</a>
            <a href="https://mockup.thaid.online" className="hover:text-[#171717] transition-colors">Mockup AI</a>
            <a href="https://novel.thaid.online" className="hover:text-[#171717] transition-colors">Novel AI</a>
            <a href="https://social.thaid.online" className="hover:text-[#171717] transition-colors">Social AI</a>
            <a href="https://clip.thaid.online" className="hover:text-[#171717] transition-colors">Clip AI</a>
            <a href="https://sticker.thaid.online" className="hover:text-[#171717] transition-colors">Sticker AI</a>
            <a href="https://chat.thaid.online" className="hover:text-[#171717] transition-colors">Chat AI</a>
            <a href="https://vault.thaid.online" className="hover:text-[#171717] transition-colors">Vault</a>
          </div>
        </div>
      </footer>

    </div>
  );
}
