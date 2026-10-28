"use client";

import React, { useState, useEffect, useRef } from "react";
import Image from "next/image";
import StudioOrbitCarousel from "./components/StudioOrbitCarousel";

interface ServiceItem {
  id: string;
  name: string;
  subname: string;
  tag: string;
  url: string;
  category: "novel" | "social" | "sticker" | "clip" | "chat" | "mockup";
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
  const [saasMenuOpen, setSaasMenuOpen] = useState(false);
  const [profileMenuOpen, setProfileMenuOpen] = useState(false);
  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [user, setUser] = useState<{ name: string; email: string; avatar: string } | null>(null);

  const saasMenuRef = useRef<HTMLDivElement | null>(null);
  const profileMenuRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    // 1. Read wildcard cookie thaid_user from .thaid.online (Authority Source)
    let currentUser = null;
    const match = document.cookie.match(/(^|;\s*)thaid_user=([^;]*)/);
    if (match && match[2]) {
      try {
        let raw = decodeURIComponent(match[2]);
        if (raw.startsWith("%")) raw = decodeURIComponent(raw);
        currentUser = JSON.parse(raw);
        setUser(currentUser);
        localStorage.setItem("thaid_user", JSON.stringify(currentUser));
      } catch (e) {}
    } else {
      // If wildcard cookie is absent or expired, clear local cache for Global Sign-Out
      const hasSessionCookie = document.cookie.includes("thaid_session=");
      if (!hasSessionCookie) {
        localStorage.removeItem("thaid_user");
        setUser(null);
      }
    }

    // 3. Verify session in background with SSO Authority
    fetch("/api/auth/me", { credentials: "include" })
      .then((r) => r.json())
      .then((d) => {
        if (d?.ok && d?.authenticated && d?.user) {
          setUser(d.user);
          localStorage.setItem("thaid_user", JSON.stringify(d.user));
        }
      })
      .catch(() => {});

    const handleClickOutside = (e: MouseEvent) => {
      if (saasMenuRef.current && !saasMenuRef.current.contains(e.target as Node)) {
        setSaasMenuOpen(false);
      }
      if (profileMenuRef.current && !profileMenuRef.current.contains(e.target as Node)) {
        setProfileMenuOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const handleLogin = async (name: string, email: string, avatar: string) => {
    const u = { name, email, avatar };
    setUser(u);
    localStorage.setItem("thaid_user", JSON.stringify(u));
    setAuthModalOpen(false);

    // Call SSO central login API to set Domain=.thaid.online wildcard cookies
    try {
      await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ name, email, avatar }),
      });
    } catch (err) {
      console.warn("SSO Cookie sync error:", err);
    }
  };

  const handleLogout = async () => {
    setUser(null);
    localStorage.removeItem("thaid_user");
    setProfileMenuOpen(false);

    // Call SSO logout API to clear Domain=.thaid.online cookies
    try {
      await fetch("/api/auth/logout", {
        method: "POST",
        credentials: "include",
      });
    } catch (err) {
      console.warn("SSO Logout error:", err);
    }
  };

  const saasServices = [
    {
      name: "Novel Studio",
      sub: "แต่งนิยาย AI 10 ตอนจบ",
      url: "https://novel.thaid.online",
      tag: "novel.thaid.online",
      badge: "10 ตอนจบ",
      icon: (
        <svg className="w-4 h-4 text-[#0569ff]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
        </svg>
      )
    },
    {
      name: "Social Auto-Poster",
      sub: "ดึงข่าว RSS & โพสต์ Facebook 24 ชม.",
      url: "https://social.thaid.online",
      tag: "social.thaid.online",
      badge: "Auto 24h",
      icon: (
        <svg className="w-4 h-4 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
        </svg>
      )
    },
    
    {
      name: "LINE Sticker Creator",
      sub: "สร้างชุดสติกเกอร์ไลน์ 40 แอ็กชัน",
      url: "https://sticker.thaid.online",
      tag: "sticker.thaid.online",
      badge: "40 แอ็กชัน",
      icon: (
        <svg className="w-4 h-4 text-pink-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>
        </svg>
      )
    },
    {
      name: "Clip AI & Reels",
      sub: "สคริปต์คลิปสั้น 9:16 สไตล์ไวรัล",
      url: "https://clip.thaid.online",
      tag: "clip.thaid.online",
      badge: "9:16 Shorts",
      icon: (
        <svg className="w-4 h-4 text-purple-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/>
        </svg>
      )
    },
    {
      name: "Smart Chat AI",
      sub: "บอทแอดมินตอบแชทบน LINE OA 24/7",
      url: "https://chat.thaid.online",
      tag: "chat.thaid.online",
      badge: "ตอบ 0.8 วิ",
      icon: (
        <svg className="w-4 h-4 text-teal-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
      )
    },
    {
      name: "Mockup Studio",
      sub: "สตูดิโอภาพถ่ายสินค้าลักชัวรี ไดคัต AI",
      url: "https://mockup.thaid.online",
      tag: "mockup.thaid.online",
      badge: "Studio 4K",
      icon: (
        <svg className="w-4 h-4 text-blue-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>
        </svg>
      )
    },
  ];
  
  const trackRef = useRef<HTMLElement | null>(null);
  const heroRef = useRef<HTMLDivElement | null>(null);

  const handleScrollDown = () => {
    const target = document.getElementById("services-directory");
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    } else {
      window.scrollTo({ top: window.innerHeight * 0.9, behavior: "smooth" });
    }
  };

  // Auto-Snap to Page 2 on scroll down (เด้งหน้าที่ 2 ขึ้นมาอัตโนมัติ ไม่เมื่อยนิ้ว):
  useEffect(() => {
    let isSnapping = false;
    let touchStartY = 0;

    const snapToPage2 = () => {
      if (isSnapping) return;
      const target = document.getElementById("services-directory");
      if (target) {
        isSnapping = true;
        target.scrollIntoView({ behavior: "smooth" });
        setTimeout(() => {
          isSnapping = false;
        }, 1000);
      }
    };

    const handleWheel = (e: WheelEvent) => {
      if (!isSnapping && window.scrollY < 80 && e.deltaY > 15) {
        snapToPage2();
      }
    };

    const handleTouchStart = (e: TouchEvent) => {
      touchStartY = e.touches[0].clientY;
    };

    const handleTouchMove = (e: TouchEvent) => {
      if (isSnapping) return;
      const currentY = e.touches[0].clientY;
      const diff = touchStartY - currentY;
      if (window.scrollY < 60 && diff > 25) {
        snapToPage2();
      }
    };

    window.addEventListener("wheel", handleWheel, { passive: true });
    window.addEventListener("touchstart", handleTouchStart, { passive: true });
    window.addEventListener("touchmove", handleTouchMove, { passive: true });

    return () => {
      window.removeEventListener("wheel", handleWheel);
      window.removeEventListener("touchstart", handleTouchStart);
      window.removeEventListener("touchmove", handleTouchMove);
    };
  }, []);

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

  // ThaiD Studio Scroll Physics Engine:
  // Drives --exit-opacity (1 -> 0) and --exit-scatter (0 -> 1) directly via requestAnimationFrame
  useEffect(() => {
    let ticking = false;

    const onScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          if (trackRef.current && heroRef.current) {
            const scroll = window.scrollY;
            const threshold = Math.max(1, window.innerHeight * 0.75);
            const progress = Math.min(1, Math.max(0, scroll / threshold));
            
            const scatter = progress;
            const opacity = Math.max(0, 1 - progress);

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

  // 10 Real Studio Orbit Cards (Actual ThaiD AI Tools & Outputs)
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
  ];

  const filteredServices = activeTab === "all" ? services : services.filter((s) => s.category === activeTab);

  return (
    <div className="min-h-screen bg-white text-[#171717] font-sans antialiased overflow-x-hidden selection:bg-[#0569ff]/15 selection:text-[#0569ff]">
      
      {/* ======================================================== */}
      {/* 1. THAID FLOATING TOP NAVBAR (MASTER TEMPLATE 3-ZONE)    */}
      {/* ======================================================== */}
      <header className="fixed top-0 inset-x-0 z-50 pt-4 px-4 sm:px-6 pointer-events-none">
        <div className="max-w-5xl mx-auto flex items-center justify-between pointer-events-auto bg-white/80 backdrop-blur-xl border border-black/[0.08] shadow-[0_4px_24px_rgba(0,0,0,0.04)] rounded-full px-4 sm:px-5 py-2.5 relative">
          
          {/* Zone 1: Left - Brand Logo + ThaiD */}
          <a href="https://thaid.online" className="flex items-center gap-2.5 text-[#2b313b] hover:opacity-85 transition-opacity flex-shrink-0 group">
            <div className="w-7 h-7 rounded-lg bg-[#2b313b] flex items-center justify-center text-white shadow-xs group-hover:scale-105 transition-transform">
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 6.5H15M9.5 6.5V19" stroke="white" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" strokeWidth="2.2" strokeLinecap="round"/>
              </svg>
            </div>
            <span className="font-bold text-xl tracking-tight text-[#2b313b]">
              ThaiD
            </span>
          </a>

          {/* Zone 3: Right - Link to Sub Home + Far Right Login / Profile */}
          <div className="flex items-center gap-2 flex-shrink-0">
            {/* SaaS Services Selector Dropdown (Moved to Right) */}
          <div className="relative" ref={saasMenuRef}>
            <button
              type="button"
              onClick={() => setSaasMenuOpen(!saasMenuOpen)}
              className="inline-flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-full border border-black/[0.08] bg-white/90 hover:bg-white text-xs font-semibold text-[#2b313b] transition-all shadow-2xs hover:border-black/[0.2] cursor-pointer"
            >
              <span className="text-[#0569ff] font-bold text-xs">✦</span>
              <span>เลือกบริการ SaaS</span>
              <svg width="10" height="10" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2.2" className={`text-stone-400 transition-transform duration-200 ${saasMenuOpen ? 'rotate-180' : ''}`}>
                <path d="m4.5 6 3.5 3.5L11.5 6" />
              </svg>
            </button>

            {/* Dropdown Menu */}
            {saasMenuOpen && (
              <div className="absolute right-0 top-full mt-2 w-72 sm:w-80 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-2 z-50 animate-in fade-in zoom-in-95 duration-150">
                <div className="px-3 py-1.5 text-[10px] font-bold text-stone-400 uppercase tracking-wider border-b border-black/[0.05] mb-1 flex items-center justify-between">
                  <span>ThaiD SaaS Ecosystem</span>
                  <span className="text-emerald-600 font-semibold">6 เครื่องมือ</span>
                </div>
                <div className="grid grid-cols-1 gap-1 max-h-[380px] overflow-y-auto">
                  {saasServices.map((svc) => (
                    <a
                      key={svc.tag}
                      href={svc.url}
                      onClick={() => setSaasMenuOpen(false)}
                      className="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left"
                    >
                      <div className="flex items-center gap-2.5">
                        <div className="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0">
                          {svc.icon}
                        </div>
                        <div className="text-left">
                          <div className="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors flex items-center gap-1.5">
                            <span>{svc.name}</span>
                          </div>
                          <div className="text-[10px] text-stone-400 truncate max-w-[170px] sm:max-w-[190px]">{svc.sub}</div>
                        </div>
                      </div>
                      <span className="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">{svc.badge}</span>
                    </a>
                  ))}
                </div>
              </div>
            )}
          </div>

            {/* Far Right: Login Button OR Profile Avatar */}
            {user ? (
              <div className="relative" ref={profileMenuRef}>
                <button
                  type="button"
                  onClick={() => setProfileMenuOpen(!profileMenuOpen)}
                  className="flex items-center gap-1.5 p-1 pl-1 pr-2.5 rounded-full border border-black/[0.08] hover:border-[#0569ff] transition-all bg-white shadow-2xs cursor-pointer group"
                  title={user.name}
                >
                  <img
                    src={user.avatar}
                    alt={user.name}
                    className="w-6 h-6 rounded-full object-cover bg-stone-100 ring-1 ring-black/[0.06]"
                  />
                  <span className="text-xs font-semibold text-[#2b313b] hidden md:inline max-w-[80px] truncate">
                    {user.name}
                  </span>
                  <svg width="10" height="10" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2.2" className={`text-stone-400 group-hover:text-[#171717] transition-transform duration-200 ${profileMenuOpen ? 'rotate-180' : ''}`}>
                    <path d="m4.5 6 3.5 3.5L11.5 6" />
                  </svg>
                </button>

                {/* Profile Popup */}
                {profileMenuOpen && (
                  <div className="absolute right-0 top-full mt-2 w-64 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-3 z-50 text-left animate-in fade-in zoom-in-95 duration-150">
                    <div className="flex items-center gap-2.5 pb-2.5 border-b border-black/[0.06]">
                      <img src={user.avatar} alt={user.name} className="w-10 h-10 rounded-full object-cover bg-stone-100 ring-1 ring-black/[0.08]" />
                      <div className="flex-1 min-w-0">
                        <div className="text-xs font-bold text-[#171717] truncate">{user.name}</div>
                        <div className="text-[10px] text-stone-400 truncate">{user.email}</div>
                      </div>
                    </div>
                    <div className="py-2 text-[11px] space-y-1">
                      <div className="flex items-center justify-between px-2 py-1 rounded-lg bg-stone-50">
                        <span className="text-stone-500">สถานะสมาชิก:</span>
                        <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold text-[10px]">Active Pro</span>
                      </div>
                      <a
                        href="https://novel.thaid.online"
                        className="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors"
                      >
                        <span>ไปที่ Novel Studio</span>
                        <span className="text-[10px] text-stone-400">→</span>
                      </a>
                      <a
                        href="https://social.thaid.online/dashboard"
                        className="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors"
                      >
                        <span>ไปที่ Social Dashboard</span>
                        <span className="text-[10px] text-stone-400">→</span>
                      </a>
                      
                    </div>
                    <button
                      type="button"
                      onClick={handleLogout}
                      className="w-full mt-1 pt-2 border-t border-black/[0.06] text-left text-xs font-semibold text-rose-600 hover:text-rose-700 flex items-center justify-between px-2 py-1 rounded-lg hover:bg-rose-50/50 cursor-pointer transition-colors"
                    >
                      <span>ออกจากระบบ</span>
                      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>
                      </svg>
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <button
                type="button"
                onClick={() => setAuthModalOpen(true)}
                className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-[#171717] hover:bg-black text-white text-xs font-semibold shadow-2xs transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer"
              >
                <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2.4">
                  <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M15 12H3" />
                </svg>
                <span>เข้าสู่ระบบ</span>
              </button>
            )}
          </div>

        </div>
      </header>

      {/* ======================================================== */}
      {/* 2. THAID PINNED 200VH TRACK & 3D SCATTER STAGE            */}
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
            
            {/* ThaiD Headline with Animated Handwritten Thai "คุณ" */}
            <h1 className="hero-headline-thaid text-4xl sm:text-6xl md:text-[64px] font-medium tracking-[-0.025em] text-[#2b313b] leading-[1.15] mb-6">
              <span className="block">โชว์ให้โลกได้เห็น</span>
              <span className="inline-flex items-center justify-center flex-wrap gap-x-1.5">
                <span>ว่า</span>
                <em
                  className="script-accent-khun not-italic mx-0.5"
                  aria-label="คุณ"
                >
                  <span className="paint-khun">
                    <svg
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 98 87"
                      className="accent-stroke-svg text-[#2b313b]"
                    >
                      <path
                        className="accent-stroke-path"
                        pathLength="1"
                        stroke="currentColor"
                        strokeWidth="6.5"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M9.67655 34.8743C20.8135 35.6005 24.9848 29.0327 23.8426 25.9298C22.7003 22.8268 15.9267 24.0209 13.0846 28.7026C10.0386 33.7201 6.69237 46.6041 6.69237 53.5362C0.0292325 37.7574 3.18519 9.49143 14.8925 8.56639C26.6006 7.64129 36.1498 17.8753 35.1028 55.9691M30.824 66.4463C27.236 70.8697 21.0441 71.7349 20.1164 67.7076C19.1887 63.6804 21.1303 60.3933 23.8424 60.3933C30.3628 60.3933 30.8416 64.3686 29.048 83.2505M48.0867 48.2104C56.9931 47.4182 59.0749 53.7522 58.8561 55.9691C58.5171 59.4021 52.6963 64.6177 50.2559 57.7834C49.2144 54.8663 51.205 38.6374 52.6963 34.8743C46.5954 35.9306 45.782 27.8761 46.9343 22.7265C48.0867 17.5769 57.3736 11.7011 62.3221 21.01C67.2706 30.3189 66.3216 49.9929 67.1351 50.9832C70.2533 41.8064 81.7093 33.1578 86.9967 33.1578C92.2842 33.1578 94.25 41.4737 94.25 44.8434C94.25 50.9833 90.1742 54.8004 87.3357 47.4182C84.0046 38.755 85.5054 12.2953 86.9967 3.25049"
                      />
                    </svg>
                  </span>
                </em>
                <span>เจ๋งแค่ไหน</span>
              </span>
            </h1>

            {/* Subtitle */}
            <p className="text-base sm:text-lg md:text-xl text-[#5e6675] max-w-2xl font-normal leading-relaxed mb-8">
              ในยุค AI การสร้างพอร์ตฯ คือหลักฐานชั้นดีว่าทำไมลูกค้าต้องเลือกคุณ
              <br />
              <span className="text-sm sm:text-base text-[#2b313b] font-medium mt-1 inline-block">
                รวม 6 เครื่องมือ AI Studio จาก ThaiD — เปลี่ยนผลงานเป็นรายได้จริง
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
          {/* BOTTOM SCROLL CUE (CLICKABLE INTERACTIVE BUTTON)         */}
          {/* ======================================================== */}
          <div className="scroll-cue-scatter absolute bottom-6 left-1/2 -translate-x-1/2 z-30 pointer-events-auto">
            <button
              type="button"
              onClick={handleScrollDown}
              aria-label="Scroll down to services"
              className="group flex flex-col items-center gap-1.5 px-4 py-2 rounded-full hover:bg-black/5 active:scale-95 transition-all cursor-pointer"
            >
              <span className="text-[11px] font-bold text-[#737373] group-hover:text-[#171717] tracking-wider uppercase transition-colors">
                Scroll down
              </span>
              <div className="anim-scroll-bounce text-[#737373] group-hover:text-[#171717] group-hover:translate-y-1 transition-all">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 5v14M19 12l-7 7-7-7" />
                </svg>
              </div>
            </button>
          </div>

        </div>
      </section>

      {/* ======================================================== */}
      {/* 3. ELEVATED CARD SHEET (SLIDES & POPS UP FROM BELOW)     */}
      {/* ======================================================== */}
      <section id="services-directory" className="services-sheet-stage">
        
        

        <main className="max-w-5xl mx-auto px-4 sm:px-6 pt-4 pb-28">
        
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold text-[#171717] tracking-tight mb-4">
            เลือกสตูดิโอ AI ที่คุณต้องการสร้างสรรค์
          </h2>
          <p className="text-[#737373] text-sm sm:text-base leading-relaxed">
            เชื่อมต่อเครื่องมือ AI ระดับโปร ผลงานจริงจากเครื่องมือในระบบ รองรับภาษาไทย 100%
          </p>
        </div>

        {/* 3D Orbit Carousel Showcase (ม้าหมุน 3 มิติ 360 องศา) */}
        <StudioOrbitCarousel />

      </main>
    </section>

      {/* ======================================================== */}
      {/* 4. THAID CLEAN EDITORIAL FOOTER                           */}
      {/* ======================================================== */}
      <footer className="relative z-20 border-t border-black/[0.08] bg-[#fafafa] py-16 px-4 sm:px-6">
        <div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="flex flex-col items-center md:items-start gap-2">
            <div className="flex items-center gap-2.5">
              <div className="w-6 h-6 rounded-lg bg-[#2b313b] flex items-center justify-center text-white">
                <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 6.5H15M9.5 6.5V19" stroke="white" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" strokeWidth="2.2" strokeLinecap="round"/>
                </svg>
              </div>
              <span className="font-bold text-base text-[#171717]">ThaiD Studio</span>
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
            
          </div>

          <div className="text-xs text-[#737373]">
            © 2026 ThaiD.online. All rights reserved.
          </div>
        </div>
      </footer>

      {/* ======================================================== */}
      {/* 5. THAID UNIFIED AUTH MODAL                              */}
      {/* ======================================================== */}
      {authModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border border-black/[0.08] text-center space-y-5 relative animate-in fade-in zoom-in-95 duration-150">
            <button
              onClick={() => setAuthModalOpen(false)}
              className="absolute top-4 right-4 text-stone-400 hover:text-[#171717] p-1 cursor-pointer"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            </button>

            <div className="space-y-1 pt-2">
              <div className="w-10 h-10 rounded-2xl bg-[#2b313b] text-white flex items-center justify-center mx-auto shadow-sm">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M4 6.5H15M9.5 6.5V19" stroke="white" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" strokeWidth="2.2" strokeLinecap="round"/>
                </svg>
              </div>
              <h3 className="text-base font-bold text-[#171717]">เข้าสู่ระบบ ThaiD</h3>
              <p className="text-xs text-stone-500">เข้าถึงทุกบริการ SaaS ใน ThaiD Ecosystem ด้วยบัญชีเดียว</p>
            </div>

            {/* Quick Demo Logins */}
            <div className="space-y-2 pt-2">
              <button
                type="button"
                onClick={() => handleLogin("Admin Boss", "boss@thaid.online", "https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss")}
                className="w-full flex items-center justify-between p-2.5 rounded-2xl border border-black/[0.08] hover:border-black/[0.2] bg-stone-50 hover:bg-stone-100 transition-all text-left cursor-pointer"
              >
                <div className="flex items-center gap-2.5">
                  <img src="https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss" className="w-8 h-8 rounded-full bg-white shadow-2xs" alt="Admin" />
                  <div>
                    <div className="text-xs font-bold text-[#171717]">Admin Boss (Superadmin)</div>
                    <div className="text-[10px] text-stone-400">boss@thaid.online · VIP Enterprise</div>
                  </div>
                </div>
                <span className="text-[11px] font-semibold text-[#0569ff]">เข้าทันที →</span>
              </button>

              <button
                type="button"
                onClick={() => handleLogin("รดา นิยายรัก", "rada@thaid.online", "https://api.dicebear.com/7.x/avataaars/svg?seed=RadaAuthor")}
                className="w-full flex items-center justify-between p-2.5 rounded-2xl border border-black/[0.08] hover:border-black/[0.2] bg-stone-50 hover:bg-stone-100 transition-all text-left cursor-pointer"
              >
                <div className="flex items-center gap-2.5">
                  <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=RadaAuthor" className="w-8 h-8 rounded-full bg-white shadow-2xs" alt="Author" />
                  <div>
                    <div className="text-xs font-bold text-[#171717]">รดา นิยายรัก (Creator)</div>
                    <div className="text-[10px] text-stone-400">rada@thaid.online · Pro Creator</div>
                  </div>
                </div>
                <span className="text-[11px] font-semibold text-[#0569ff]">เข้าทันที →</span>
              </button>
            </div>

            <div className="relative py-1">
              <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-black/[0.08]"></div></div>
              <div className="relative flex justify-center text-[10px] uppercase text-stone-400"><span className="bg-white px-2">หรือเข้าด้วยอีเมล</span></div>
            </div>

            {/* Email input */}
            <form onSubmit={(e) => {
              e.preventDefault();
              const form = e.currentTarget;
              const input = (form.elements.namedItem('email') as HTMLInputElement).value.trim();
              if (input) {
                const name = input.split('@')[0];
                handleLogin(name, input, `https://api.dicebear.com/7.x/avataaars/svg?seed=${name}`);
              }
            }} className="space-y-2">
              <input
                name="email"
                type="email"
                placeholder="your.email@example.com"
                required
                className="w-full px-3 py-2 text-xs rounded-xl border border-black/[0.1] focus:outline-none focus:border-[#0569ff]"
              />
              <button
                type="submit"
                className="w-full py-2.5 rounded-full bg-[#171717] hover:bg-black text-white text-xs font-semibold shadow-xs transition-all cursor-pointer"
              >
                เข้าสู่ระบบด้วยอีเมล
              </button>
            </form>
          </div>
        </div>
      )}

    </div>
  );
}
