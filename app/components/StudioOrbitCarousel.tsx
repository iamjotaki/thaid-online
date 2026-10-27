"use client";

import React, { useState, useEffect, useRef, useCallback } from "react";
import Image from "next/image";

export interface StudioItem {
  id: string;
  name: string;
  shortLabel: string;
  subname: string;
  tag: string;
  url: string;
  category: string;
  status: string;
  badge: string;
  description: string;
  icon: string;
  image: string;
  accent: string;
  features: string[];
  stats: {
    primary: string;
    primaryLabel: string;
    secondary: string;
    secondaryLabel: string;
  };
  actionText: string;
}

const STUDIOS: StudioItem[] = [
  {
    id: "mockup",
    name: "ThaiD Mockup AI Studio",
    shortLabel: "Mockup AI",
    subname: "AI Product Photography & Studio",
    tag: "mockup.thaid.online",
    url: "https://mockup.thaid.online",
    category: "mockup",
    status: "พร้อมใช้งาน",
    badge: "E-Commerce",
    description: "สตูดิโอถ่ายภาพสินค้าและม็อกอัพระดับลักชัวรีด้วย AI ไดคัตพื้นหลังอัตโนมัติ จัดวางฉากพรีเมียม สังเคราะห์แสงเงาสมจริง",
    icon: "photo_camera",
    image: "/cards/mockup_real_1.jpg",
    accent: "#e85a2d",
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
    shortLabel: "Novel AI",
    subname: "AI Novel & Chapter Generator",
    tag: "novel.thaid.online",
    url: "https://novel.thaid.online",
    category: "novel",
    status: "พร้อมใช้งาน",
    badge: "Most Popular",
    description: "ระบบผู้ช่วยนักเขียนอัจฉริยะ วางโครงเรื่อง แต่งนิยาย 10 ตอนจบ พร้อมเชื่อมต่ออัปโหลดขึ้น ReadAWrite.com อัตโนมัติ",
    icon: "edit_note",
    image: "/cards/novel_real_1.jpg",
    accent: "#0569ff",
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
    shortLabel: "Social Poster",
    subname: "Facebook Content & Video Reels",
    tag: "social.thaid.online",
    url: "https://social.thaid.online",
    category: "social",
    status: "พร้อมใช้งาน",
    badge: "High Viral",
    description: "ระบบ AI ค้นหาข่าวไวรัล เรียบเรียงใหม่ เจนภาพประกอบและตัดต่อวิดีโอสั้นพร้อมเสียงพากย์ ยิงโพสต์ขึ้น Facebook Page 24 ชม.",
    icon: "campaign",
    image: "/cards/social_real_1.jpg",
    accent: "#1877f2",
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
    shortLabel: "Clip Video",
    subname: "Viral Video & Subtitle Generator",
    tag: "clip.thaid.online",
    url: "https://clip.thaid.online",
    category: "clip",
    status: "พร้อมใช้งาน",
    badge: "Trending",
    description: "สตูดิโอสร้างคลิปวิดีโอสั้นอัตโนมัติด้วย AI พากย์เสียงภาษาไทย สร้างซับไตเติลคาราโอเกะแบบคำต่อคำ และภาพประกอบแบบไดนามิก",
    icon: "movie_creation",
    image: "/cards/clip_real_1.jpg",
    accent: "#8b5cf6",
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
    shortLabel: "LINE Sticker",
    subname: "40-Action Character Pack Studio",
    tag: "sticker.thaid.online",
    url: "https://sticker.thaid.online",
    category: "sticker",
    status: "พร้อมใช้งาน",
    badge: "Creators Choice",
    description: "สตูดิโอสร้างชุดสติกเกอร์ไลน์ 40 แอ็กชันพร้อมส่งขาย ลายเส้นคาแรคเตอร์คงที่ ไดคัตพื้นหลังใส คำพูดฮิตภาษาไทย",
    icon: "sentiment_satisfied",
    image: "/cards/sticker_real_1.jpg",
    accent: "#10b981",
    features: [
      "เจนสติกเกอร์ครบชุด 8/16/24/40 ตัวในสไตล์เดียวกัน",
      "ตัดพื้นหลังโปร่งใส PNG และสร้าง Main/Tab Image อัตโนมัติ",
      "จัดแพ็ก ZIP ตามมาตรฐาน LINE Creators Market",
    ],
    stats: { primary: "40 แอ็กชัน", primaryLabel: "ชุดมาตรฐาน LINE", secondary: "370×320", secondaryLabel: "PNG ไดคัตใส" },
    actionText: "เปิดใช้งาน Sticker Studio",
  },
  {
    id: "chat",
    name: "ThaiD Smart Chat AI",
    shortLabel: "Smart Chat",
    subname: "LINE Official Account Bot",
    tag: "chat.thaid.online",
    url: "https://chat.thaid.online",
    category: "chat",
    status: "พร้อมใช้งาน",
    badge: "Fast Reply 0.8s",
    description: "ระบบแอดมิน AI ตอบแชทลูกค้าบน LINE OA ตลอด 24 ชม. เรียนรู้ข้อมูลสินค้า ปิดการขายอัตโนมัติ เชื่อมต่อ webhook ราบรื่น",
    icon: "chat",
    image: "/cards/chat_real_1.jpg",
    accent: "#0d9488",
    features: [
      "ระบบตอบกลับความเร็วสูงเฉลี่ย 0.8 วินาที ด้วย Enterprise API",
      "จดจำบริบทบทสนทนาและปิดการขายได้อย่างเป็นธรรมชาติ",
      "หน้าแดชบอร์ดจัดการคลังความรู้ คอนฟิก LINE OA ในคลิกเดียว",
    ],
    stats: { primary: "0.8 วินาที", primaryLabel: "ความเร็วตอบกลับ", secondary: "24/7", secondaryLabel: "แสตนด์บายตอบแชท" },
    actionText: "เปิดใช้งาน Smart Chat",
  },
];

export default function StudioOrbitCarousel() {
  const [rotation, setRotation] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const [radius, setRadius] = useState(320);

  const total = STUDIOS.length;
  const angleStep = 360 / total;

  // Drag interaction refs
  const startXRef = useRef(0);
  const isDraggingRef = useRef(false);
  const hasDraggedRef = useRef(false);

  // Responsive radius calculation for compact & fit layout
  useEffect(() => {
    const updateRadius = () => {
      if (window.innerWidth < 640) {
        setRadius(210);
      } else if (window.innerWidth < 1024) {
        setRadius(270);
      } else {
        setRadius(320);
      }
    };
    updateRadius();
    window.addEventListener("resize", updateRadius);
    return () => window.removeEventListener("resize", updateRadius);
  }, []);

  // Smooth auto-rotation
  useEffect(() => {
    if (isPaused) return;
    const interval = setInterval(() => {
      setRotation((prev) => prev - 0.16);
    }, 30);
    return () => clearInterval(interval);
  }, [isPaused]);

  // Compute active front index from rotation angle
  useEffect(() => {
    const normalized = ((-rotation % 360) + 360) % 360;
    const index = Math.round(normalized / angleStep) % total;
    setActiveIndex(index);
  }, [rotation, angleStep, total]);

  // Direct rotate to specific studio index
  const rotateTo = useCallback((index: number) => {
    const currentNorm = ((-rotation % 360) + 360) % 360;
    const targetNorm = (index * angleStep) % 360;
    let diff = targetNorm - currentNorm;
    if (diff > 180) diff -= 360;
    if (diff < -180) diff += 360;
    setRotation((prev) => prev - diff);
    setActiveIndex(index);
  }, [rotation, angleStep]);

  const handlePrev = () => {
    setRotation((prev) => prev + angleStep);
  };

  const handleNext = () => {
    setRotation((prev) => prev - angleStep);
  };

  // Drag Handlers (Mouse & Touch)
  const handleDragStart = (clientX: number) => {
    isDraggingRef.current = true;
    hasDraggedRef.current = false;
    startXRef.current = clientX;
    setIsPaused(true);
  };

  const handleDragMove = (clientX: number) => {
    if (!isDraggingRef.current) return;
    const delta = clientX - startXRef.current;
    if (Math.abs(delta) > 5) {
      hasDraggedRef.current = true;
    }
    setRotation((prev) => prev + delta * 0.35);
    startXRef.current = clientX;
  };

  const handleDragEnd = () => {
    if (!isDraggingRef.current) return;
    isDraggingRef.current = false;
    setTimeout(() => {
      setIsPaused(false);
    }, 2000);
  };

  const activeStudio = STUDIOS[activeIndex];

  return (
    <div className="relative w-full select-none">
      {/* Category Filter Pills (Syncs with 3D Orbit Carousel) */}
      <div className="flex items-center justify-center gap-1.5 sm:gap-2 flex-wrap mb-6 sm:mb-8 px-2">
        <button
          type="button"
          onClick={() => {
            setIsPaused(false);
          }}
          className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full text-xs font-semibold transition-all duration-200 cursor-pointer flex items-center gap-1.5 ${
            !isPaused
              ? "bg-[#171717] text-white shadow-xs ring-1 ring-black/10"
              : "bg-white text-[#737373] hover:text-[#171717] border border-black/[0.08] hover:border-black/20"
          }`}
        >
          <span className="text-xs">✦</span>
          <span>ทั้งหมด (All Studios)</span>
        </button>

        {STUDIOS.map((s, idx) => (
          <button
            key={s.id}
            type="button"
            onClick={() => {
              rotateTo(idx);
              setIsPaused(true);
            }}
            className={`px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full text-xs font-semibold transition-all duration-200 cursor-pointer flex items-center gap-1.5 ${
              activeIndex === idx
                ? "bg-[#171717] text-white shadow-xs ring-1 ring-black/10"
                : "bg-white text-[#737373] hover:text-[#171717] border border-black/[0.08] hover:border-black/20"
            }`}
          >
            <span
              className="w-1.5 h-1.5 rounded-full"
              style={{ backgroundColor: s.accent }}
            />
            <span>{s.shortLabel}</span>
          </button>
        ))}
      </div>

      {/* 3D Orbit Stage Viewport - Overflow Visible to Prevent Top Clipping */}
      <div className="relative w-full py-2 overflow-visible">
        {/* Dynamic Ambient Background Glow */}
        <div
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[380px] sm:w-[550px] h-[300px] sm:h-[400px] rounded-full blur-[80px] pointer-events-none transition-colors duration-700 opacity-20"
          style={{
            background: `radial-gradient(circle, ${activeStudio.accent} 0%, transparent 70%)`,
          }}
        />

        {/* 3D Perspective Stage */}
        <div
          className="relative w-full h-[410px] sm:h-[450px] flex items-center justify-center orbit-carousel-viewport cursor-grab active:cursor-grabbing overflow-visible"
          onMouseEnter={() => setIsPaused(true)}
          onMouseLeave={() => {
            if (!isDraggingRef.current) setIsPaused(false);
          }}
          onMouseDown={(e) => handleDragStart(e.clientX)}
          onMouseMove={(e) => handleDragMove(e.clientX)}
          onMouseUp={handleDragEnd}
          onTouchStart={(e) => handleDragStart(e.touches[0].clientX)}
          onTouchMove={(e) => handleDragMove(e.touches[0].clientX)}
          onTouchEnd={handleDragEnd}
        >
          {/* Glowing Ground Disk Ring */}
          <div
            className="absolute w-[280px] sm:w-[380px] h-[280px] sm:h-[380px] rounded-full border border-dashed border-stone-300/70 pointer-events-none flex items-center justify-center opacity-40"
            style={{
              transform: "rotateX(75deg) translateY(140px)",
            }}
          >
            <div
              className="w-[160px] sm:w-[240px] h-[160px] sm:h-[240px] rounded-full border border-stone-200 animate-pulse"
              style={{ borderColor: `${activeStudio.accent}30` }}
            />
          </div>

          {/* 3D Rotating Cylinder Stage */}
          <div
            className="orbit-carousel-stage w-full h-full flex items-center justify-center overflow-visible"
            style={{
              transform: `rotateY(${rotation}deg)`,
              transition: isDraggingRef.current ? "none" : "transform 0.08s linear",
            }}
          >
            {STUDIOS.map((service, idx) => {
              const cardAngle = idx * angleStep;
              const isCurrent = idx === activeIndex;

              // Angular difference to calculate depth opacity & scaling
              const normalizedDiff = Math.abs((((cardAngle + rotation) % 360) + 540) % 360 - 180);
              const isBack = normalizedDiff > 90;

              return (
                <div
                  key={service.id}
                  onClick={(e) => {
                    if (hasDraggedRef.current) return;
                    e.stopPropagation();
                    rotateTo(idx);
                  }}
                  className={`orbit-carousel-card absolute w-[220px] sm:w-[250px] h-[335px] sm:h-[370px] rounded-2xl bg-white border overflow-hidden flex flex-col justify-between transition-all duration-300 select-none ${
                    isCurrent
                      ? "border-black/[0.18] shadow-[0_20px_45px_-10px_rgba(0,0,0,0.18)] scale-105 z-30 opacity-100"
                      : isBack
                      ? "border-black/[0.04] shadow-xs scale-90 opacity-35 hover:opacity-65 z-10 cursor-pointer"
                      : "border-black/[0.07] shadow-sm scale-95 opacity-70 hover:opacity-90 z-20 cursor-pointer"
                  }`}
                  style={{
                    transform: `rotateY(${cardAngle}deg) translateZ(${radius}px)`,
                    boxShadow: isCurrent
                      ? `0 20px 45px -10px ${service.accent}35, 0 0 0 1.5px ${service.accent}`
                      : undefined,
                  }}
                >
                  {/* Card Image Banner */}
                  <div className="relative w-full h-28 sm:h-32 bg-stone-100 overflow-hidden flex-shrink-0">
                    <Image
                      src={service.image}
                      alt={service.name}
                      fill
                      sizes="(max-width: 640px) 220px, 250px"
                      className="object-cover transition-transform duration-500"
                      priority={idx < 3}
                    />
                    <div className="absolute top-2 left-2 flex items-center gap-1">
                      <span className="px-2 py-0.5 rounded-full text-[9px] sm:text-[10px] font-bold bg-white/95 backdrop-blur-md text-[#171717] border border-black/[0.08] shadow-xs">
                        {service.badge}
                      </span>
                    </div>
                    <div className="absolute top-2 right-2 flex items-center gap-1 px-2 py-0.5 rounded-full bg-white/95 backdrop-blur-md text-[9px] sm:text-[10px] font-semibold text-[#171717] border border-black/[0.08] shadow-xs">
                      <span className="w-1.5 h-1.5 rounded-full bg-[#22c55e] animate-pulse" />
                      <span>{service.status}</span>
                    </div>
                  </div>

                  {/* Card Body */}
                  <div className="p-3 sm:p-3.5 flex flex-col flex-1 justify-between text-left">
                    <div>
                      {/* Subdomain link indicator */}
                      <div className="flex items-center gap-1 mb-1 text-[11px] font-semibold" style={{ color: service.accent }}>
                        <span className="material-symbols-outlined text-[14px]">{service.icon}</span>
                        <span className="font-mono text-[10px] sm:text-[11px] truncate">{service.tag}</span>
                      </div>

                      {/* Title */}
                      <h3 className="text-sm sm:text-base font-bold text-[#171717] mb-1 line-clamp-1">
                        {service.name}
                      </h3>

                      {/* Description */}
                      <p className="text-[#737373] text-[10px] sm:text-[11px] leading-relaxed line-clamp-2 mb-2">
                        {service.description}
                      </p>

                      {/* Key Features Bullet List */}
                      <div className="space-y-1 mb-2">
                        {service.features.slice(0, 2).map((feat, fIdx) => (
                          <div key={fIdx} className="flex items-start gap-1 text-[10px] text-[#171717]">
                            <span className="text-[#0569ff] font-bold">✓</span>
                            <span className="text-stone-700 line-clamp-1">{feat}</span>
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Card Footer Metric & Direct Link Button */}
                    <div className="pt-2 border-t border-black/[0.06]">
                      <div className="flex items-center justify-between mb-2 text-[10px]">
                        <div>
                          <span className="font-bold text-[#171717]">{service.stats.primary}</span>
                          <span className="text-[9px] text-[#737373] block">{service.stats.primaryLabel}</span>
                        </div>
                        <div className="text-right">
                          <span className="font-bold text-[#171717]">{service.stats.secondary}</span>
                          <span className="text-[9px] text-[#737373] block">{service.stats.secondaryLabel}</span>
                        </div>
                      </div>

                      <a
                        href={service.url}
                        onClick={(e) => {
                          e.stopPropagation();
                        }}
                        className="w-full inline-flex items-center justify-center gap-1.5 py-1.5 sm:py-2 px-3 rounded-full bg-[#171717] hover:bg-black text-white text-[11px] sm:text-xs font-semibold transition-all duration-200 shadow-xs cursor-pointer group"
                      >
                        <span>{service.actionText}</span>
                        <span className="text-xs transition-transform group-hover:translate-x-0.5">→</span>
                      </a>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Left & Right Floating Navigation Controls */}
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              handlePrev();
            }}
            className="absolute left-1 sm:left-4 top-1/2 -translate-y-1/2 w-9 h-9 sm:w-11 sm:h-11 rounded-full bg-white/95 hover:bg-white border border-black/[0.08] shadow-md flex items-center justify-center text-[#171717] hover:scale-105 transition-all z-40 cursor-pointer backdrop-blur-md"
            aria-label="Previous Studio"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="m15 18-6-6 6-6" />
            </svg>
          </button>

          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              handleNext();
            }}
            className="absolute right-1 sm:right-4 top-1/2 -translate-y-1/2 w-9 h-9 sm:w-11 sm:h-11 rounded-full bg-white/95 hover:bg-white border border-black/[0.08] shadow-md flex items-center justify-center text-[#171717] hover:scale-105 transition-all z-40 cursor-pointer backdrop-blur-md"
            aria-label="Next Studio"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="m9 18 6-6-6-6" />
            </svg>
          </button>
        </div>

        {/* Bottom Focus Tool Summary Bar */}
        <div className="max-w-md mx-auto mt-4 px-2">
          <div className="p-2.5 sm:p-3 rounded-2xl bg-white/95 backdrop-blur-xl border border-black/[0.08] shadow-xs flex items-center justify-between gap-3">
            <div className="flex items-center gap-2.5 min-w-0">
              <div
                className="w-8 h-8 rounded-lg flex items-center justify-center text-white font-bold shadow-xs flex-shrink-0"
                style={{ backgroundColor: activeStudio.accent }}
              >
                <span className="material-symbols-outlined text-[17px]">{activeStudio.icon}</span>
              </div>
              <div className="min-w-0">
                <div className="flex items-center gap-1.5">
                  <h4 className="text-xs sm:text-sm font-bold text-[#171717] truncate">{activeStudio.name}</h4>
                  <span className="text-[9px] font-mono px-1.5 py-0.5 rounded-full bg-emerald-50 text-emerald-600 font-bold border border-emerald-200 flex-shrink-0">
                    Live
                  </span>
                </div>
                <p className="text-[10px] text-[#737373] truncate">
                  {activeStudio.tag} · {activeStudio.stats.primary}
                </p>
              </div>
            </div>

            <a
              href={activeStudio.url}
              className="px-3.5 py-1.5 rounded-full bg-[#171717] hover:bg-black text-white text-[11px] sm:text-xs font-semibold shadow-xs transition-all flex items-center gap-1 flex-shrink-0"
            >
              <span>เปิดระบบ</span>
              <span className="text-xs">→</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
