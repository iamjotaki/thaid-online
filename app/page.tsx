"use client";

import React, { useState, useEffect, useRef } from "react";
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
  features: string[];
  stats: { primary: string; primaryLabel: string; secondary: string; secondaryLabel: string };
  actionText: string;
}

interface OrbitCardConfig {
  id: string;
  name: string;
  role: string;
  avatar: string;
  cover: string;
  url: string;
  left: string;
  top: string;
  width: string;
  height: string;
  rot: string;
  scatterX: string;
  scatterY: string;
  animClass: string;
  badge: string;
  rating: string;
  price: string;
}

export default function HomePage() {
  const [activeTab, setActiveTab] = useState<string>("all");
  const [countdown, setCountdown] = useState({ days: 19, hours: 18, mins: 30, secs: 49 });
  
  const trackRef = useRef<HTMLElement | null>(null);
  const heroRef = useRef<HTMLDivElement | null>(null);

  // Countdown timer effect
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

  // Fastwork Scroll Physics Engine:
  // Drives --exit-opacity (1 -> 0) and --exit-scatter (0 -> 1) directly via requestAnimationFrame
  useEffect(() => {
    let ticking = false;

    const onScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          if (trackRef.current && heroRef.current) {
            const rect = trackRef.current.getBoundingClientRect();
            const trackScrollable = trackRef.current.offsetHeight - window.innerHeight;
            
            // Calculate scroll ratio through the 200vh track
            const currentScroll = -rect.top;
            const progress = Math.min(1, Math.max(0, currentScroll / Math.max(1, trackScrollable)));
            
            // Fastwork curves: scatter completes within first 75% of track scroll
            const scatterFactor = Math.min(1, progress / 0.72);
            const opacity = Math.max(0, 1 - scatterFactor);
            const scatter = scatterFactor;

            heroRef.current.style.setProperty("--exit-opacity", opacity.toFixed(4));
            heroRef.current.style.setProperty("--exit-scatter", scatter.toFixed(4));
            
            if (opacity < 0.02) {
              heroRef.current.style.pointerEvents = "none";
            } else {
              heroRef.current.style.pointerEvents = "auto";
            }
          }
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // 10 Real Fastwork Orbit Cards (Actual ThaiD AI Tools & Outputs)
  const orbitCards: OrbitCardConfig[] = [
    {
      id: "mockup_1",
      name: "ThaiD Mockup AI",
      role: "3D Product Studio · Bangkok",
      avatar: "/avatars/weng.png",
      cover: "/cards/mockup_gen_1.jpg",
      url: "https://mockup.thaid.online",
      left: "-1.8%",
      top: "9.2%",
      width: "205px",
      height: "255px",
      rot: "3.05deg",
      scatterX: "-55vw",
      scatterY: "-28vh",
      animClass: "anim-float-a",
      badge: "Mockup 3D",
      rating: "5.0 (214)",
      price: "1080×1080",
    },
    {
      id: "novel_1",
      name: "ReadAWrite AI",
      role: "Web Novel Studio · Chiang Mai",
      avatar: "/avatars/chapavich.png",
      cover: "/cards/novel_gen_1.jpg",
      url: "https://novel.thaid.online",
      left: "76.4%",
      top: "-4.5%",
      width: "200px",
      height: "250px",
      rot: "4deg",
      scatterX: "55vw",
      scatterY: "-28vh",
      animClass: "anim-float-b",
      badge: "Novel AI",
      rating: "5.0 (389)",
      price: "10 ตอนจบ",
    },
    {
      id: "social_1",
      name: "Social Auto-Poster",
      role: "Viral Content · Bangkok",
      avatar: "/avatars/leobeer.png",
      cover: "/cards/social_gen_1.jpg",
      url: "https://social.thaid.online",
      left: "8.5%",
      top: "-5.0%",
      width: "200px",
      height: "250px",
      rot: "4deg",
      scatterX: "-45vw",
      scatterY: "-30vh",
      animClass: "anim-float-c",
      badge: "Viral Shorts",
      rating: "5.0 (342)",
      price: "Reels 9:16",
    },
    {
      id: "sticker_1",
      name: "LINE Sticker AI",
      role: "Sticker Pack · Bangkok",
      avatar: "/avatars/peter.png",
      cover: "/cards/sticker_gen_1.jpg",
      url: "https://sticker.thaid.online",
      left: "13.0%",
      top: "27.2%",
      width: "210px",
      height: "260px",
      rot: "-2deg",
      scatterX: "-50vw",
      scatterY: "12vh",
      animClass: "anim-float-b",
      badge: "3D Chibi Mascot",
      rating: "5.0 (310)",
      price: "40 แอ็กชัน",
    },
    {
      id: "clip_1",
      name: "AI Clip Studio",
      role: "Karaoke Subtitles · Phuket",
      avatar: "/avatars/nam.png",
      cover: "/cards/clip_gen_1.jpg",
      url: "https://clip.thaid.online",
      left: "-0.7%",
      top: "48.5%",
      width: "240px",
      height: "300px",
      rot: "4deg",
      scatterX: "-55vw",
      scatterY: "18vh",
      animClass: "anim-float-a",
      badge: "Karaoke Video",
      rating: "5.0 (195)",
      price: "1080p Shorts",
    },
    {
      id: "mockup_2",
      name: "Luxury Mockup Studio",
      role: "Cast Shadow · Bangkok",
      avatar: "/avatars/bold.png",
      cover: "/cards/mockup_real_2.jpg",
      url: "https://mockup.thaid.online",
      left: "5.3%",
      top: "68.5%",
      width: "260px",
      height: "325px",
      rot: "3.05deg",
      scatterX: "-55vw",
      scatterY: "38vh",
      animClass: "anim-float-c",
      badge: "Studio Scene",
      rating: "5.0 (412)",
      price: "AI Matting",
    },
    {
      id: "vault_1",
      name: "ThaiD Vault Security",
      role: "Cloud Vault · Bangkok",
      avatar: "/avatars/pakincht.png",
      cover: "/cards/vault_gen_1.jpg",
      url: "https://vault.thaid.online",
      left: "76.3%",
      top: "75.8%",
      width: "220px",
      height: "275px",
      rot: "3.8deg",
      scatterX: "52vw",
      scatterY: "38vh",
      animClass: "anim-float-b",
      badge: "AES-256",
      rating: "4.9 (127)",
      price: "Hardware Key",
    },
    {
      id: "novel_2",
      name: "Fantasy Novel Studio",
      role: "Story Engine · Chiang Mai",
      avatar: "/avatars/buttercup.png",
      cover: "/cards/novel_real_2.jpg",
      url: "https://novel.thaid.online",
      left: "86.3%",
      top: "6.4%",
      width: "200px",
      height: "250px",
      rot: "4deg",
      scatterX: "55vw",
      scatterY: "-28vh",
      animClass: "anim-float-a",
      badge: "Thai Web Novel",
      rating: "4.9 (189)",
      price: "ReadAWrite",
    },
    {
      id: "chat_1",
      name: "Smart Chatbot AI",
      role: "LINE OA 24/7 · Bangkok",
      avatar: "/avatars/mod.png",
      cover: "/cards/chat_gen_1.jpg",
      url: "https://chat.thaid.online",
      left: "88.5%",
      top: "62.1%",
      width: "195px",
      height: "245px",
      rot: "-4deg",
      scatterX: "55vw",
      scatterY: "36vh",
      animClass: "anim-float-c",
      badge: "LINE OA 24/7",
      rating: "5.0 (260)",
      price: "ตอบใน 0.8 วิ",
    },
    {
      id: "sticker_2",
      name: "Chibi Sticker Pack",
      role: "LINE Creator · Chiang Mai",
      avatar: "/avatars/slayalldeep.png",
      cover: "/cards/sticker_real_2.jpg",
      url: "https://sticker.thaid.online",
      left: "82.5%",
      top: "32.0%",
      width: "235px",
      height: "295px",
      rot: "-5.2deg",
      scatterX: "55vw",
      scatterY: "-5vh",
      animClass: "anim-float-b",
      badge: "ZIP Ready",
      rating: "5.0 (178)",
      price: "ไดคัตขาว",
    },
  ];

  // Services Directory Data with Real Product Visuals
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
      image: "/cards/mockup_gen_1.jpg",
      creator: "Weng Kitsana",
      location: "Photographer · Bangkok",
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
      image: "/cards/novel_gen_1.jpg",
      creator: "Chapavich T.",
      location: "Fiction Author · Chiang Mai",
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
      image: "/cards/social_gen_1.jpg",
      creator: "LEOBEER",
      location: "Viral Editor · Bangkok",
      features: [
        "Auto-Curation ค้นหาและคัดกรองข่าวดังอัตโนมัติ",
        "ตัดต่อวิดีโอ Shorts/Reels ขนาด 9:16 ด้วย FFmpeg",
        "แปลงข้อความเป็นเสียงพากย์ภาษาไทยเป็นธรรมชาติ",
      ],
      stats: { primary: "24 ชม.", primaryLabel: "ทำงานอัตโนมัติ", secondary: "Reels & Post", secondaryLabel: "รองรับ 2 รูปแบบ" },
      actionText: "เปิดใช้งาน Social Poster",
    },
    {
      id: "clip",
      name: "AI Clip Studio Pro",
      subname: "Viral Video & Subtitle Generator",
      tag: "clip.thaid.online",
      url: "https://clip.thaid.online",
      category: "clip",
      status: "พร้อมใช้งาน",
      badge: "Trending",
      description: "สตูดิโอสร้างคลิปวิดีโอสั้นอัตโนมัติด้วย AI พากย์เสียงภาษาไทย สร้างซับไตเติลคาราโอเกะแบบคำต่อคำ และภาพประกอบแบบไดนามิก",
      icon: "movie_creation",
      image: "/cards/clip_gen_1.jpg",
      creator: "Nguyen Van Nam",
      location: "Video Creator · Phuket",
      features: [
        "ซับไตเติลคาราโอเกะซิงก์เสียงพูดเป๊ะทุกคำ",
        "คลังดนตรีและซาวด์เอฟเฟกต์ประกอบคลิปกว่า 1,000 ชิ้น",
        "เรนเดอร์วิดีโอความคมชัดสูง 1080p พร้อมแชร์ทันที",
      ],
      stats: { primary: "1080×1920", primaryLabel: "ความละเอียด 9:16", secondary: "100%", secondaryLabel: "ซับไตเติลภาษาไทย" },
      actionText: "เปิดใช้งาน Clip Studio",
    },
    {
      id: "sticker",
      name: "LINE Sticker AI Creator",
      subname: "Instant LINE Sticker Pack Generator",
      tag: "sticker.thaid.online",
      url: "https://sticker.thaid.online",
      category: "sticker",
      status: "พร้อมใช้งาน",
      badge: "New Release",
      description: "ระบบสร้างสติกเกอร์ไลน์อัตโนมัติด้วย AI เจนภาพชุด 8/16/24/40 ตัวละครคงที่ พร้อมไดคัตพื้นหลังโปร่งใสและแพ็กเกจส่ง LINE Creators Market",
      icon: "sentiment_satisfied",
      image: "/cards/sticker_gen_1.jpg",
      creator: "Peter Visuals",
      location: "Graphic Artist · Phuket",
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
      image: "/cards/chat_gen_1.jpg",
      creator: "MOD SUPACHA",
      location: "E-Commerce Admin · Bangkok",
      features: [
        "เชื่อมต่อ LINE Messaging API Webhook พร้อมใช้งาน",
        "คลังข้อมูลสินค้า คำถามที่พบบ่อย และเงื่อนไขบริการ",
        "ตอบตรงประเด็น สุภาพ ปิดการขาย ช่วยลดต้นทุนแอดมิน",
      ],
      stats: { primary: "24/7", primaryLabel: "ตอบแชทอัตโนมัติ", secondary: "0.8 วินาที", secondaryLabel: "ความเร็วตอบกลับ" },
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
      image: "/cards/vault_gen_1.jpg",
      creator: "Pakinchit",
      location: "Security Engineer · Bangkok",
      features: [
        "เข้ารหัสความปลอดภัยระดับทหาร AES-256",
        "จัดเก็บ Gemini API Keys และหมุนเวียนคีย์อัตโนมัติ",
        "สำรองข้อมูลและจัดการสภาพแวดล้อมระบบนิเวศ",
      ],
      stats: { primary: "AES-256", primaryLabel: "การเข้ารหัสข้อมูล", secondary: "80 Keys", secondaryLabel: "คลังคีย์ความปลอดภัย" },
      actionText: "เปิดใช้งาน ThaiD Vault",
    },
  ];

  const filteredServices = activeTab === "all" ? services : services.filter((s) => s.category === activeTab);

  return (
    <div className="min-h-screen bg-white text-[#171717] font-sans antialiased overflow-x-hidden selection:bg-[#0569ff]/15 selection:text-[#0569ff]">
      
      {/* ======================================================== */}
      {/* 1. FLOATING PILL NAVBAR                                  */}
      {/* ======================================================== */}
      <header className="fixed top-0 inset-x-0 z-50 pt-4 px-4 sm:px-6 pointer-events-none">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          
          <div className="w-24 hidden sm:block" />

          {/* Centered Floating Fastwork-Style Brand Pill */}
          <div className="pointer-events-auto inline-flex items-center gap-2.5 px-4 py-2 rounded-full border border-black/[0.08] bg-white/85 backdrop-blur-xl shadow-xs hover:shadow-md transition-all">
            <a href="https://thaid.online" className="flex items-center gap-2 text-[#171717]">
              <div className="w-5 h-5 rounded-full bg-[#171717] flex items-center justify-center text-white text-[11px] font-bold">
                ✦
              </div>
              <span className="font-bold text-sm tracking-tight text-[#171717]">
                ThaiD<span className="text-[#0569ff]">.online</span>
              </span>
            </a>
          </div>

          {/* Right Action Pills */}
          <div className="pointer-events-auto flex items-center gap-2">
            <a
              href="https://vault.thaid.online"
              className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full border border-black/[0.08] bg-white/85 backdrop-blur-xl text-xs font-semibold text-[#171717] hover:bg-black/5 transition-colors shadow-xs"
            >
              <span className="material-symbols-outlined text-[15px] text-[#0569ff]">lock</span>
              <span>Vault</span>
            </a>
            <div className="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/85 backdrop-blur-xl text-xs font-medium text-[#171717]">
              <span className="text-[13px]">🌐</span>
              <span className="font-semibold">TH</span>
            </div>
          </div>

        </div>
      </header>

      {/* ======================================================== */}
      {/* 2. FASTWORK PINNED 200VH TRACK & 3D SCATTER STAGE        */}
      {/* ======================================================== */}
      <section ref={trackRef} className="hero-track">
        <div ref={heroRef} className="hero-sticky">
          
          {/* ======================================================== */}
          {/* 3D FLOATING ORBIT CARDS (REAL PRODUCT PHOTOS)            */}
          {/* ======================================================== */}
          <div className="orbit-stage-viewport">
            <div className="orbit-stage-container">
              {orbitCards.map((card) => (
                <article
                  key={card.id}
                  className={`orbit-card-scatter ${card.animClass}`}
                  style={{
                    left: card.left,
                    top: card.top,
                    width: card.width,
                    height: card.height,
                    ["--orbit-rot" as any]: card.rot,
                    ["--scatter-x" as any]: card.scatterX,
                    ["--scatter-y" as any]: card.scatterY,
                  }}
                >
                  <a href={card.url} className="block w-full h-full text-left group">
                    {/* Cover Photo: Real Output of the Tool */}
                    <div className="relative w-full h-[62%] bg-stone-100 overflow-hidden">
                      <Image
                        src={card.cover}
                        alt={card.name}
                        fill
                        sizes="260px"
                        className="object-cover group-hover:scale-105 transition-transform duration-500"
                        priority
                      />
                      <div className="absolute top-2.5 left-2.5 px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-[10px] font-bold text-white tracking-wide">
                        {card.badge}
                      </div>
                    </div>

                    {/* Profile Body */}
                    <div className="relative h-[38%] bg-white px-3 py-2 flex flex-col justify-between">
                      <div className="flex items-center gap-2.5">
                        <div className="relative w-7 h-7 rounded-full bg-stone-200 overflow-hidden flex-shrink-0 border border-black/[0.06]">
                          <Image
                            src={card.avatar}
                            alt={card.name}
                            width={28}
                            height={28}
                            className="object-cover"
                          />
                          <span className="absolute bottom-0 right-0 w-2 h-2 rounded-full bg-[#22c55e] border-[1.5px] border-white" />
                        </div>
                        <div className="flex flex-col min-w-0">
                          <p className="text-xs font-bold text-[#171717] truncate leading-tight group-hover:text-[#0569ff] transition-colors">
                            {card.name}
                          </p>
                          <p className="text-[10px] text-[#737373] truncate leading-tight">
                            {card.role}
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center justify-between pt-1 border-t border-black/[0.05]">
                        <span className="text-[10px] font-semibold text-amber-500 flex items-center gap-0.5">
                          ★ <span className="text-[#171717]">{card.rating}</span>
                        </span>
                        <span className="text-[10px] font-bold text-[#171717] bg-stone-100 px-2 py-0.5 rounded-full">
                          {card.price}
                        </span>
                      </div>
                    </div>
                  </a>
                </article>
              ))}
            </div>
          </div>

          {/* ======================================================== */}
          {/* HERO CENTER COPY (HEADLINE + COUNTDOWN + COMET BUTTON)    */}
          {/* ======================================================== */}
          <div className="hero-copy-scatter relative z-20 flex flex-col items-center text-center px-4 max-w-4xl mx-auto pointer-events-auto">
            
            {/* Top Brand Pill */}
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-black/[0.08] bg-white/90 shadow-xs mb-6 backdrop-blur-md">
              <span className="w-2 h-2 rounded-full bg-[#22c55e] animate-pulse" />
              <span className="text-xs font-bold text-[#171717] tracking-tight">
                ThaiD.online Studio
              </span>
              <span className="text-[11px] text-[#737373] border-l border-black/[0.08] pl-2 font-medium">
                SaaS Ecosystem 2026
              </span>
            </div>

            {/* Exact Fastwork Headline with Cursive Thai "คุณ" */}
            <h1 className="text-4xl sm:text-6xl md:text-7xl font-bold tracking-tight text-[#171717] leading-[1.08] mb-6">
              Show the world
              <br />
              what{" "}
              <span className="font-['Charm'] font-bold text-[#171717] italic text-[1.18em] px-2 inline-block -rotate-2">
                คุณ
              </span>{" "}
              can do
            </h1>

            {/* Subtitle */}
            <p className="text-base sm:text-lg md:text-xl text-[#737373] max-w-2xl font-normal leading-relaxed mb-8">
              In the age of AI, your portfolio proves why clients need you.
              <br />
              <span className="text-sm sm:text-base text-[#171717]/80 font-medium">
                ในยุคแห่งปัญญาประดิษฐ์ พอร์ตผลงานของคุณคือข้อพิสูจน์ที่ดีที่สุด
              </span>
            </p>

            {/* 4-Box Countdown Timer Pills */}
            <div className="flex items-center gap-2 sm:gap-3 mb-10">
              <div className="flex flex-col items-center justify-center w-16 sm:w-20 h-16 sm:h-20 rounded-2xl bg-white border border-black/[0.08] shadow-[0_10px_25px_rgba(0,0,0,0.04)]">
                <span className="text-xl sm:text-2xl font-bold text-[#171717] tabular-nums">
                  {countdown.days.toString().padStart(2, "0")}
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-[#737373] uppercase tracking-wider">
                  days
                </span>
              </div>
              <span className="text-lg font-bold text-[#737373]/40">:</span>
              <div className="flex flex-col items-center justify-center w-16 sm:w-20 h-16 sm:h-20 rounded-2xl bg-white border border-black/[0.08] shadow-[0_10px_25px_rgba(0,0,0,0.04)]">
                <span className="text-xl sm:text-2xl font-bold text-[#171717] tabular-nums">
                  {countdown.hours.toString().padStart(2, "0")}
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-[#737373] uppercase tracking-wider">
                  hours
                </span>
              </div>
              <span className="text-lg font-bold text-[#737373]/40">:</span>
              <div className="flex flex-col items-center justify-center w-16 sm:w-20 h-16 sm:h-20 rounded-2xl bg-white border border-black/[0.08] shadow-[0_10px_25px_rgba(0,0,0,0.04)]">
                <span className="text-xl sm:text-2xl font-bold text-[#171717] tabular-nums">
                  {countdown.mins.toString().padStart(2, "0")}
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-[#737373] uppercase tracking-wider">
                  mins
                </span>
              </div>
              <span className="text-lg font-bold text-[#737373]/40">:</span>
              <div className="flex flex-col items-center justify-center w-16 sm:w-20 h-16 sm:h-20 rounded-2xl bg-white border border-black/[0.08] shadow-[0_10px_25px_rgba(0,0,0,0.04)]">
                <span className="text-xl sm:text-2xl font-bold text-[#0569ff] tabular-nums">
                  {countdown.secs.toString().padStart(2, "0")}
                </span>
                <span className="text-[10px] sm:text-xs font-semibold text-[#737373] uppercase tracking-wider">
                  seconds
                </span>
              </div>
            </div>

            {/* Action Buttons: Comet Glowing Orbit Button + Secondary Button */}
            <div className="flex flex-wrap items-center justify-center gap-4">
              <a href="#services-directory" className="hero-cta-wrap">
                <span className="hero-cta-comet" />
                <span className="hero-cta-inner">
                  <span>เริ่มต้นใช้งาน (Get started)</span>
                  <span className="text-lg leading-none">→</span>
                </span>
              </a>

              <a href="#services-directory" className="hero-cta-secondary">
                สำรวจสตูดิโอทั้งหมด
              </a>
            </div>

          </div>

          {/* ======================================================== */}
          {/* BOTTOM SCROLL CUE                                        */}
          {/* ======================================================== */}
          <div className="scroll-cue-scatter absolute bottom-6 left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 cursor-pointer pointer-events-auto">
            <span className="text-[11px] font-semibold text-[#737373] tracking-wide uppercase">
              Scroll down
            </span>
            <div className="anim-scroll-bounce text-[#737373]">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 5v14M19 12l-7 7-7-7" />
              </svg>
            </div>
          </div>

        </div>
      </section>

      {/* ======================================================== */}
      {/* 3. CATEGORY SELECTOR & STUDIO DIRECTORY                  */}
      {/* ======================================================== */}
      <main id="services-directory" className="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 pt-16 pb-28">
        
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-stone-100 text-[#171717] text-xs font-bold mb-4">
            ✦ AI Studio Directory
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold text-[#171717] tracking-tight mb-4">
            เลือกสตูดิโอ AI ที่คุณต้องการสร้างสรรค์
          </h2>
          <p className="text-[#737373] text-sm sm:text-base leading-relaxed">
            เชื่อมต่อเครื่องมือ AI ระดับโปร ผลงานจริงจากเครื่องมือในระบบ รองรับภาษาไทย 100%
          </p>
        </div>

        {/* Minimalist Pill Filter Tabs */}
        <div className="flex items-center justify-center gap-2 flex-wrap mb-14">
          {[
            { id: "all", label: "ทั้งหมด (All Studios)" },
            { id: "mockup", label: "Mockup AI" },
            { id: "novel", label: "Novel AI" },
            { id: "social", label: "Social Poster" },
            { id: "clip", label: "Clip Video" },
            { id: "sticker", label: "LINE Sticker" },
            { id: "chat", label: "Smart Chat" },
            { id: "vault", label: "Vault Security" },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-5 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all duration-200 cursor-pointer ${
                activeTab === tab.id
                  ? "bg-[#171717] text-white shadow-sm"
                  : "bg-white text-[#737373] hover:text-[#171717] border border-black/[0.08] hover:border-black/20"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Grid of Clean White Fastwork Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredServices.map((service) => (
            <article
              key={service.id}
              className="group rounded-3xl bg-white border border-black/[0.08] shadow-[0_15px_35px_-5px_rgba(0,0,0,0.06)] hover:shadow-[0_25px_50px_-10px_rgba(0,0,0,0.12)] transition-all duration-300 overflow-hidden flex flex-col"
            >
              {/* Card Image Banner */}
              <div className="relative w-full h-56 bg-stone-100 overflow-hidden">
                <Image
                  src={service.image}
                  alt={service.name}
                  fill
                  sizes="(max-width: 768px) 100vw, 33vw"
                  className="object-cover group-hover:scale-105 transition-transform duration-500"
                />
                <div className="absolute top-4 left-4 flex items-center gap-2">
                  <span className="px-3 py-1 rounded-full text-xs font-bold bg-white/90 backdrop-blur-md text-[#171717] border border-black/[0.08] shadow-xs">
                    {service.badge}
                  </span>
                </div>
                <div className="absolute top-4 right-4 flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/90 backdrop-blur-md text-[11px] font-semibold text-[#171717] border border-black/[0.08] shadow-xs">
                  <span className="w-1.5 h-1.5 rounded-full bg-[#22c55e]" />
                  <span>{service.status}</span>
                </div>
              </div>

              {/* Card Content Body */}
              <div className="p-6 flex flex-col flex-1 justify-between">
                <div>
                  <div className="flex items-center gap-2 mb-2 text-[#0569ff] text-xs font-semibold">
                    <span className="material-symbols-outlined text-base">{service.icon}</span>
                    <span>{service.tag}</span>
                  </div>

                  <h3 className="text-xl font-bold text-[#171717] mb-2 group-hover:text-[#0569ff] transition-colors">
                    {service.name}
                  </h3>

                  <p className="text-[#737373] text-xs sm:text-sm leading-relaxed mb-6">
                    {service.description}
                  </p>

                  {/* Feature Highlights */}
                  <div className="space-y-2 mb-6">
                    {service.features.map((feat, idx) => (
                      <div key={idx} className="flex items-start gap-2 text-xs text-[#171717]">
                        <span className="text-[#0569ff] font-bold mt-0.5">✓</span>
                        <span className="text-stone-700 leading-tight">{feat}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Card Footer Metrics & Action */}
                <div>
                  <div className="grid grid-cols-2 gap-3 py-3 border-y border-black/[0.06] mb-5">
                    <div>
                      <span className="block text-sm font-bold text-[#171717]">
                        {service.stats.primary}
                      </span>
                      <span className="text-[10px] text-[#737373]">
                        {service.stats.primaryLabel}
                      </span>
                    </div>
                    <div>
                      <span className="block text-sm font-bold text-[#171717]">
                        {service.stats.secondary}
                      </span>
                      <span className="text-[10px] text-[#737373]">
                        {service.stats.secondaryLabel}
                      </span>
                    </div>
                  </div>

                  <a
                    href={service.url}
                    className="w-full inline-flex items-center justify-center gap-2 py-3 px-4 rounded-full bg-[#171717] hover:bg-black text-white text-xs sm:text-sm font-semibold transition-all duration-200 shadow-sm"
                  >
                    <span>{service.actionText}</span>
                    <span className="text-base leading-none">→</span>
                  </a>
                </div>
              </div>
            </article>
          ))}
        </div>

      </main>

      {/* ======================================================== */}
      {/* 4. FASTWORK CLEAN EDITORIAL FOOTER                       */}
      {/* ======================================================== */}
      <footer className="relative z-20 border-t border-black/[0.08] bg-[#fafafa] py-16 px-4 sm:px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="flex flex-col items-center md:items-start gap-2">
            <div className="flex items-center gap-2">
              <div className="w-5 h-5 rounded-full bg-[#171717] flex items-center justify-center text-white text-[11px] font-bold">
                ✦
              </div>
              <span className="font-bold text-base text-[#171717]">ThaiD.online Studio</span>
            </div>
            <p className="text-xs text-[#737373]">
              Next-generation AI Ecosystem for Thai Creators & Businesses.
            </p>
          </div>

          <div className="flex items-center gap-6 text-xs text-[#737373]">
            <a href="https://thaid.online" className="hover:text-[#171717] transition-colors">หน้าแรก</a>
            <a href="https://mockup.thaid.online" className="hover:text-[#171717] transition-colors">Mockup AI</a>
            <a href="https://novel.thaid.online" className="hover:text-[#171717] transition-colors">Novel AI</a>
            <a href="https://social.thaid.online" className="hover:text-[#171717] transition-colors">Social AI</a>
            <a href="https://vault.thaid.online" className="hover:text-[#171717] transition-colors">Security Vault</a>
          </div>

          <div className="text-xs text-[#737373]">
            © 2026 ThaiD.online. All rights reserved.
          </div>
        </div>
      </footer>

    </div>
  );
}
