"use client";

import React, { useState, useEffect, useRef } from "react";

interface ShowcaseService {
  id: string;
  name: string;
  tag: string;
  url: string;
  icon: string;
  accent: string;
  category: string;
  desc: string;
  highlight: string;
  badge: string;
}

const SHOWCASE_SERVICES: ShowcaseService[] = [
  {
    id: "novel",
    name: "Novel Studio",
    tag: "novel.thaid.online",
    url: "https://novel.thaid.online",
    icon: "edit_note",
    accent: "#0071e3",
    category: "นิยาย AI & ReadAWrite",
    desc: "สร้างสรรค์นิยายหลายตอน พล็อตลึก ซับซ้อน พร้อมระบบออโต้โพสต์ขึ้น ReadAWrite อัตโนมัติ",
    highlight: "10 ตอนจบพร้อมลงขาย",
    badge: "Most Popular",
  },
  {
    id: "social",
    name: "Social Poster",
    tag: "social.thaid.online",
    url: "https://social.thaid.online",
    icon: "campaign",
    accent: "#1877f2",
    category: "คอนเทนต์ & วิดีโอ Reels",
    desc: "AI ดึงข่าวไวรัล สร้างภาพกราฟิก ตัดต่อวิดีโอ Reels เสียงพากย์ไทย พร้อมยิงขึ้น Facebook Page อัตโนมัติ",
    highlight: "ออโต้โพสต์ทุก 30 นาที",
    badge: "High Engagement",
  },
  
  {
    id: "sticker",
    name: "LINE Sticker",
    tag: "sticker.thaid.online",
    url: "https://sticker.thaid.online",
    icon: "sentiment_satisfied",
    accent: "#10b981",
    category: "สตูดิโอสติกเกอร์ไลน์",
    desc: "เจนสติกเกอร์ไลน์ครบชุด 40 แอ็กชัน ลายเส้นคงที่ ไดคัตใส พร้อมฟอนต์คำพูดยอดนิยมภาษาไทย",
    highlight: "ชุด 8/16/24/40 ท่า",
    badge: "Creators Choice",
  },
  {
    id: "clip",
    name: "Clip AI Studio",
    tag: "clip.thaid.online",
    url: "https://clip.thaid.online",
    icon: "movie",
    accent: "#ec4899",
    category: "วิดีโอสั้น 9:16 TikTok/Reels",
    desc: "สตูดิโอสร้างคลิปสั้นแนวตั้งไวรัล สคริปต์รีวิวป้ายยา พากย์เสียงไทย ผสมภาพ AI/Veo และซับคาราโอเกะ",
    highlight: "1080×1920 Full HD",
    badge: "High Viral",
  },
  {
    id: "chat",
    name: "Smart Chat AI",
    tag: "chat.thaid.online",
    url: "https://chat.thaid.online",
    icon: "forum",
    accent: "#06c755",
    category: "แอดมิน LINE OA 24 ชม.",
    desc: "แอดมิน AI อัจฉริยะตอบแชทลูกค้าตลอด 24 ชั่วโมง มีคลังข้อมูลสินค้า ราคา ปิดการขายรวดเร็วใน 1 วินาที",
    highlight: "ปิดการขาย 24/7",
    badge: "E-Commerce",
  },
  {
    id: "mockup",
    name: "Mockup AI Studio",
    tag: "mockup.thaid.online",
    url: "https://mockup.thaid.online",
    icon: "photo_camera",
    accent: "#e85a2d",
    category: "สตูดิโอถ่ายภาพสินค้า",
    desc: "เปลี่ยนรูปสินค้าธรรมดาให้เป็นภาพสตูดิโอลักชัวรี ไดคัตพื้นหลังอัตโนมัติ สังเคราะห์แสงเงาสมจริงระดับโปร",
    highlight: "8 ฉากหรู Google Flow",
    badge: "E-Commerce Pro",
  },
  {
    id: "hub",
    name: "ThaiD Central Hub",
    tag: "thaid.online",
    url: "https://thaid.online",
    icon: "hub",
    accent: "#8b5cf6",
    category: "ศูนย์กลางระบบนิเวศ",
    desc: "พอร์ทัลหลักศูนย์รวม SaaS เครื่องมือ AI สำหรับคนไทย รันบนเซิร์ฟเวอร์ Oracle Cloud Always Free",
    highlight: "Multi-SaaS Core",
    badge: "Ecosystem Hub",
  },
];

export default function OrbitShowcase() {
  const [rotation, setRotation] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const total = SHOWCASE_SERVICES.length;
  const angleStep = 360 / total;

  // Touch / Drag handling
  const startXRef = useRef(0);
  const isDraggingRef = useRef(false);

  // Auto-rotate effect
  useEffect(() => {
    if (isPaused) return;
    const interval = setInterval(() => {
      setRotation((prev) => prev - 0.25);
    }, 40);
    return () => clearInterval(interval);
  }, [isPaused]);

  // Update active index based on rotation angle (closest to front z-plane)
  useEffect(() => {
    // Normalizing rotation
    const normalized = ((-rotation % 360) + 360) % 360;
    const index = Math.round(normalized / angleStep) % total;
    setActiveIndex(index);
  }, [rotation, angleStep, total]);

  const rotateTo = (index: number) => {
    const targetAngle = -index * angleStep;
    setRotation(targetAngle);
    setActiveIndex(index);
  };

  const handlePrev = () => {
    setRotation((prev) => prev + angleStep);
  };

  const handleNext = () => {
    setRotation((prev) => prev - angleStep);
  };

  const handleMouseDown = (e: React.MouseEvent) => {
    isDraggingRef.current = true;
    startXRef.current = e.clientX;
    setIsPaused(true);
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDraggingRef.current) return;
    const delta = e.clientX - startXRef.current;
    setRotation((prev) => prev + delta * 0.35);
    startXRef.current = e.clientX;
  };

  const handleMouseUp = () => {
    isDraggingRef.current = false;
    setTimeout(() => setIsPaused(false), 2000);
  };

  const activeService = SHOWCASE_SERVICES[activeIndex];

  return (
    <div className="relative w-full py-10 sm:py-16 overflow-hidden select-none">
      
      {/* Background Ambient Radial Glow */}
      <div 
        className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] sm:w-[750px] h-[350px] sm:h-[450px] rounded-full blur-[100px] pointer-events-none transition-colors duration-700 opacity-40 dark:opacity-30"
        style={{
          background: `radial-gradient(circle, ${activeService.accent} 0%, transparent 70%)`
        }}
      />

      <div className="max-w-7xl mx-auto px-4 relative z-10 flex flex-col items-center">
        
        {/* Section Pill Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/80 dark:bg-white/[0.08] backdrop-blur-md border border-black/[0.08] dark:border-white/[0.08] shadow-xs text-xs font-semibold mb-4">
          <span className="w-2 h-2 rounded-full animate-ping" style={{ backgroundColor: activeService.accent }} />
          <span className="text-[#1d1d1f] dark:text-stone-300">ThaiD 3D Stage</span>
          <span className="text-stone-300 dark:text-stone-600">•</span>
          <span className="font-mono text-xs font-bold" style={{ color: activeService.accent }}>8 Platforms Orbit</span>
        </div>

        <h2 className="text-2xl sm:text-4xl font-extrabold tracking-tight text-center text-[#1d1d1f] dark:text-white">
          สัมผัสระบบนิเวศ AI แบบ <span className="bg-gradient-to-r from-[#e85a2d] via-amber-500 to-[#0071e3] bg-clip-text text-transparent">3D Interactive</span>
        </h2>
        <p className="mt-2 text-xs sm:text-sm text-stone-500 dark:text-stone-400 text-center max-w-xl">
          หมุนชมและเปิดใช้งาน 8 แพลตฟอร์ม AI ระดับมืออาชีพ ลอยหมุนแบบ 3 มิติ ลื่นไหลระดับ 60 FPS
        </p>

        {/* ======================================================== */}
        {/* 3D ORBIT VIEWPORT STAGE                                  */}
        {/* ======================================================== */}
        <div 
          className="relative w-full h-[400px] sm:h-[480px] flex items-center justify-center orbit-perspective-viewport cursor-grab active:cursor-grabbing mt-4"
          onMouseEnter={() => setIsPaused(true)}
          onMouseLeave={() => {
            if (!isDraggingRef.current) setIsPaused(false);
          }}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onTouchStart={(e) => {
            isDraggingRef.current = true;
            startXRef.current = e.touches[0].clientX;
            setIsPaused(true);
          }}
          onTouchMove={(e) => {
            if (!isDraggingRef.current) return;
            const delta = e.touches[0].clientX - startXRef.current;
            setRotation((prev) => prev + delta * 0.4);
            startXRef.current = e.touches[0].clientX;
          }}
          onTouchEnd={handleMouseUp}
        >
          
          {/* Glowing Center Ring Base */}
          <div className="absolute w-[220px] sm:w-[320px] h-[220px] sm:h-[320px] rounded-full border border-dashed border-stone-300/60 dark:border-white/10 pointer-events-none transform -rotate-x-75 flex items-center justify-center">
            <div className="w-[140px] sm:w-[180px] h-[140px] sm:h-[180px] rounded-full border border-stone-200 dark:border-white/5 animate-pulse" />
          </div>

          {/* 3D Rotating Cards Container */}
          <div 
            className="orbit-3d-stage w-full h-full flex items-center justify-center"
            style={{
              transform: `rotateY(${rotation}deg)`,
              transition: isDraggingRef.current ? "none" : "transform 0.1s linear",
            }}
          >
            {SHOWCASE_SERVICES.map((s, idx) => {
              const cardAngle = idx * angleStep;
              // Radius of 3D cylinder
              const radius = typeof window !== "undefined" && window.innerWidth < 640 ? 250 : 360;
              const isCurrent = idx === activeIndex;

              return (
                <div
                  key={s.id}
                  onClick={(e) => {
                    e.stopPropagation();
                    rotateTo(idx);
                  }}
                  className={`orbit-item-card absolute w-[170px] sm:w-[210px] h-[240px] sm:h-[280px] rounded-2xl p-4 sm:p-5 flex flex-col justify-between cursor-pointer border transition-all ${
                    isCurrent
                      ? "bg-white/95 dark:bg-[#161619]/95 border-brand-500/80 shadow-2xl scale-105 opacity-100 z-30"
                      : "bg-white/70 dark:bg-[#161619]/70 border-black/5 dark:border-white/10 hover:border-brand-500/40 opacity-80 z-10"
                  } backdrop-blur-xl`}
                  style={{
                    transform: `rotateY(${cardAngle}deg) translateZ(${radius}px)`,
                    boxShadow: isCurrent 
                      ? `0 20px 50px -10px ${s.accent}40, 0 0 0 1.5px ${s.accent}80` 
                      : undefined
                  }}
                >
                  {/* Top Card Row */}
                  <div className="flex items-center justify-between">
                    <div 
                      className="w-9 h-9 rounded-xl flex items-center justify-center text-white shadow-md transition-transform group-hover:scale-110"
                      style={{ backgroundColor: s.accent }}
                    >
                      <span className="material-symbols-outlined text-[20px]">{s.icon}</span>
                    </div>

                    <span 
                      className="text-[9px] font-mono uppercase font-bold px-1.5 py-0.5 rounded-full border"
                      style={{ 
                        color: s.accent, 
                        borderColor: `${s.accent}40`,
                        backgroundColor: `${s.accent}15`
                      }}
                    >
                      {s.badge}
                    </span>
                  </div>

                  {/* Middle Info */}
                  <div className="flex flex-col gap-1 my-auto">
                    <span className="text-[10px] font-mono text-stone-400 dark:text-stone-500 truncate">{s.tag}</span>
                    <h3 className="font-extrabold text-sm sm:text-base tracking-tight text-[#1d1d1f] dark:text-white leading-tight">
                      {s.name}
                    </h3>
                    <p className="text-[11px] text-stone-500 dark:text-stone-400 line-clamp-2 leading-snug">
                      {s.desc}
                    </p>
                  </div>

                  {/* Bottom Action / Status */}
                  <div className="pt-2.5 border-t border-black/5 dark:border-white/10 flex items-center justify-between text-[11px]">
                    <span className="text-emerald-500 font-semibold flex items-center gap-1">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                      <span>Live</span>
                    </span>
                    <a
                      href={s.url}
                      onClick={(e) => e.stopPropagation()}
                      className="font-bold flex items-center gap-0.5 hover:underline"
                      style={{ color: s.accent }}
                    >
                      <span>เปิด</span>
                      <span className="material-symbols-outlined text-[13px]">arrow_outward</span>
                    </a>
                  </div>
                </div>
              );
            })}
          </div>

        </div>

        {/* ======================================================== */}
        {/* STAGE CONTROLS (Prev / Next & Direct Launch)            */}
        {/* ======================================================== */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 w-full max-w-3xl mt-4 p-4 rounded-2xl bg-white/70 dark:bg-[#161619]/70 backdrop-blur-xl border border-black/5 dark:border-white/10 shadow-xs">
          
          {/* Active Tool Summary */}
          <div className="flex items-center gap-3">
            <div 
              className="w-10 h-10 rounded-xl flex items-center justify-center text-white font-bold shadow-md"
              style={{ backgroundColor: activeService.accent }}
            >
              <span className="material-symbols-outlined text-[22px]">{activeService.icon}</span>
            </div>
            <div className="flex flex-col">
              <div className="flex items-center gap-2">
                <span className="font-bold text-sm text-[#1d1d1f] dark:text-white">{activeService.name}</span>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-500 font-bold border border-emerald-500/20">ออนไลน์</span>
              </div>
              <span className="text-xs text-stone-500 dark:text-stone-400">{activeService.category} · {activeService.highlight}</span>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center gap-2 w-full sm:w-auto justify-end">
            <button
              type="button"
              onClick={handlePrev}
              className="w-9 h-9 rounded-xl border border-black/5 dark:border-white/10 hover:bg-black/5 dark:hover:bg-white/5 flex items-center justify-center text-stone-600 dark:text-stone-300 transition-colors"
              title="ย้อนกลับ"
            >
              <span className="material-symbols-outlined text-[18px]">chevron_left</span>
            </button>
            <button
              type="button"
              onClick={handleNext}
              className="w-9 h-9 rounded-xl border border-black/5 dark:border-white/10 hover:bg-black/5 dark:hover:bg-white/5 flex items-center justify-center text-stone-600 dark:text-stone-300 transition-colors"
              title="ถัดไป"
            >
              <span className="material-symbols-outlined text-[18px]">chevron_right</span>
            </button>

            <a
              href={activeService.url}
              className="px-4 py-2 rounded-xl text-xs font-bold text-white shadow-md transition-all hover:scale-105 active:scale-95 flex items-center gap-1.5"
              style={{ backgroundColor: activeService.accent }}
            >
              <span>เปิดใช้งาน {activeService.name}</span>
              <span className="material-symbols-outlined text-[14px]">arrow_outward</span>
            </a>
          </div>

        </div>

      </div>
    </div>
  );
}
