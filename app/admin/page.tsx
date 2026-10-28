"use client";

import React, { useState, useMemo } from "react";
import Link from "next/link";

// ==========================================
// TYPES & MOCK DATA
// ==========================================

interface AppContainer {
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
}

interface UnifiedUser {
  id: string;
  name: string;
  email: string;
  avatar: string;
  role: "superadmin" | "admin" | "vip" | "member";
  registeredDate: string;
  apps: { [key: string]: string }; // appKey -> tier (e.g. 'novel': 'Pro', 'social': 'VIP')
  totalCredits: number;
  status: "active" | "suspended";
}

interface PaymentSlip {
  id: string;
  userName: string;
  userEmail: string;
  appTarget: string;
  planName: string;
  amount: number;
  bank: string;
  refNumber: string;
  slipTime: string;
  status: "pending" | "approved" | "rejected";
}

interface AIKey {
  id: string;
  label: string;
  provider: string;
  keyMasked: string;
  models: string[];
  usageCount: number;
  status: "active" | "standby" | "rate_limited";
  rateLimit: string;
}

interface AuditLogItem {
  id: string;
  time: string;
  actor: string;
  action: string;
  app: string;
  details: string;
  type: "info" | "success" | "warning";
}

// Initial Apps List
const APPS_LIST: AppContainer[] = [
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
];

// Initial Unified Users
const INITIAL_USERS: UnifiedUser[] = [
  {
    id: "usr_001",
    name: "Admin Boss",
    email: "admin@thaid.online",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss",
    role: "superadmin",
    registeredDate: "2026-10-01",
    apps: {
      novel: "VIP Enterprise",
      social: "VIP Agency",
      sticker: "Unlimited",
      clip: "Unlimited",
      chat: "Enterprise",
      mockup: "Unlimited",
      vault: "Master Key",
    },
    totalCredits: 99999,
    status: "active",
  },
  {
    id: "usr_002",
    name: "คุณกฤต แฟนเพจลิเวอร์พูล",
    email: "thekop@fanpage.com",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=KritKop",
    role: "vip",
    registeredDate: "2026-10-15",
    apps: {
      social: "VIP Agency (฿990/ด)",
      clip: "Pro Creator",
      novel: "Free Trial",
    },
    totalCredits: 450,
    status: "active",
  },
  {
    id: "usr_003",
    name: "นักเขียน นิยายพันล้าน",
    email: "writer.saga@gmail.com",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=NovelSaga",
    role: "member",
    registeredDate: "2026-10-20",
    apps: {
      novel: "Pro Story (฿490/ด)",
      mockup: "Free Trial",
    },
    totalCredits: 120,
    status: "active",
  },
  {
    id: "usr_004",
    name: "ร้านค้าออนไลน์ แซ่บสตรีท",
    email: "shop.zaap@gmail.com",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=ShopZaap",
    role: "vip",
    registeredDate: "2026-10-22",
    apps: {
      chat: "Pro Bot (฿690/ด)",
      mockup: "Studio 4K (฿490/ด)",
      sticker: "Set 40",
    },
    totalCredits: 380,
    status: "active",
  },
  {
    id: "usr_005",
    name: "บอลเต็ง แฟนคลับ",
    email: "newbie@gmail.com",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=NewbieFan",
    role: "member",
    registeredDate: "2026-10-27",
    apps: {
      social: "Pro Plan (฿490/ด)",
    },
    totalCredits: 30,
    status: "active",
  },
];

// Initial Payment Slips
const INITIAL_SLIPS: PaymentSlip[] = [
  {
    id: "slip_101",
    userName: "คุณกฤต (thekop@fanpage.com)",
    userEmail: "thekop@fanpage.com",
    appTarget: "Social Auto-Poster",
    planName: "VIP Agency (รายเดือน)",
    amount: 990,
    bank: "ธนาคารไทยพาณิชย์ (SCB)",
    refNumber: "REF2026102800412",
    slipTime: "วันนี้ 12:28 น.",
    status: "pending",
  },
  {
    id: "slip_102",
    userName: "ร้านค้าออนไลน์ แซ่บสตรีท",
    userEmail: "shop.zaap@gmail.com",
    appTarget: "Smart Chat AI + Mockup",
    planName: "Bundle E-Commerce Duo",
    amount: 1180,
    bank: "ธนาคารกสิกรไทย (KBANK)",
    refNumber: "REF2026102800918",
    slipTime: "วันนี้ 11:45 น.",
    status: "pending",
  },
  {
    id: "slip_103",
    userName: "นักเขียน นิยายพันล้าน",
    userEmail: "writer.saga@gmail.com",
    appTarget: "Novel Studio",
    planName: "Pro Story (30 วัน)",
    amount: 490,
    bank: "PromptPay QR",
    refNumber: "REF2026102800115",
    slipTime: "วันนี้ 09:15 น.",
    status: "approved",
  },
];

// Initial AI Keys Pool
const INITIAL_AI_KEYS: AIKey[] = [
  {
    id: "key_01",
    label: "Google Gemini Primary Production",
    provider: "Google AI Studio",
    keyMasked: "AIzaSyB9...W842X",
    models: ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-flash-tts"],
    usageCount: 14205,
    status: "active",
    rateLimit: "1,000 RPM / ไม่มีค้าง",
  },
  {
    id: "key_02",
    label: "Gemini Auto-Failover Backup 1",
    provider: "Google AI Studio",
    keyMasked: "AIzaSyD7...K190P",
    models: ["gemini-2.5-flash", "gemini-2.5-flash-preview-tts"],
    usageCount: 890,
    status: "standby",
    rateLimit: "1,000 RPM / สแตนด์บาย",
  },
  {
    id: "key_03",
    label: "Flux Turbo Studio Engine",
    provider: "Pollinations / REST",
    keyMasked: "sk_flx_live_992...aa8",
    models: ["flux-realism-v2", "sdxl-turbo"],
    usageCount: 3410,
    status: "active",
    rateLimit: "Unlimited REST Pool",
  },
];

// Initial Logs
const INITIAL_LOGS: AuditLogItem[] = [
  {
    id: "log_1",
    time: "13:10 น.",
    actor: "Admin Boss",
    action: "Deploy App 4 (thaid-vault)",
    app: "Personal Vault",
    details: "อัปเดต SaaS Navbar Dropdown สำเร็จ (Commit cc27e78)",
    type: "success",
  },
  {
    id: "log_2",
    time: "13:01 น.",
    actor: "Admin Boss",
    action: "Deploy App 3 (thaid-social-poster)",
    app: "Social Auto-Poster",
    details: "ปรับปรุงหน้า Admin Portal และ Legal Pages สำเร็จ (Commit a654d9e)",
    type: "success",
  },
  {
    id: "log_3",
    time: "12:56 น.",
    actor: "System Engine",
    action: "Docker Builder Cache Pruned",
    app: "Server Host",
    details: "คืนพื้นที่ดิสก์ Oracle Cloud VM เพิ่มขึ้น 23 GB สำเร็จ",
    type: "info",
  },
];

export default function CentralizedAdminPage() {
  // Master Gate Access Security
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(true);
  const [pinInput, setPinInput] = useState<string>("");
  const [pinError, setPinError] = useState<string>("");

  // Tabs & Filters
  const [activeTab, setActiveTab] = useState<
    "overview" | "users" | "slips" | "aipool" | "logs"
  >("overview");
  const [appFilter, setAppFilter] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [isSaasDropdownOpen, setIsSaasDropdownOpen] = useState<boolean>(false);

  // Dynamic States
  const [users, setUsers] = useState<UnifiedUser[]>(INITIAL_USERS);
  const [slips, setSlips] = useState<PaymentSlip[]>(INITIAL_SLIPS);
  const [aiKeys, setAiKeys] = useState<AIKey[]>(INITIAL_AI_KEYS);
  const [logs, setLogs] = useState<AuditLogItem[]>(INITIAL_LOGS);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  // Modals
  const [isAddUserOpen, setIsAddUserOpen] = useState<boolean>(false);
  const [newUserName, setNewUserName] = useState<string>("");
  const [newUserEmail, setNewUserEmail] = useState<string>("");
  const [newUserApp, setNewUserApp] = useState<string>("novel");
  const [newUserTier, setNewUserTier] = useState<string>("Pro");

  // Show Toast
  const triggerToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 3500);
  };

  // Handle PIN verification
  const handlePinSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (pinInput === "888888" || pinInput === "admin" || pinInput.length >= 4) {
      setIsAuthenticated(true);
      setPinError("");
      triggerToast("ยินดีต้อนรับสู่ ThaiD Central Super Admin Control Center");
    } else {
      setPinError("รหัส PIN ไม่ถูกต้อง (ทดลองกรอก: 888888)");
    }
  };

  // Approve Slip Action
  const handleApproveSlip = (slipId: string) => {
    setSlips((prev) =>
      prev.map((s) => (s.id === slipId ? { ...s, status: "approved" } : s))
    );
    const slip = slips.find((s) => s.id === slipId);
    if (slip) {
      const newLog: AuditLogItem = {
        id: "log_" + Date.now(),
        time: "เมื่อสักครู่",
        actor: "Admin Boss",
        action: `อนุมัติสลิป ฿${slip.amount.toLocaleString()}`,
        app: slip.appTarget,
        details: `เปิดสิทธิ์ ${slip.planName} ให้ ${slip.userName} เรียบร้อย`,
        type: "success",
      };
      setLogs((prev) => [newLog, ...prev]);
      triggerToast(`อนุมัติสลิป ฿${slip.amount.toLocaleString()} และเปิดสิทธิ์เรียบร้อยแล้ว`);
    }
  };

  // Reject Slip Action
  const handleRejectSlip = (slipId: string) => {
    setSlips((prev) =>
      prev.map((s) => (s.id === slipId ? { ...s, status: "rejected" } : s))
    );
    triggerToast("ปฏิเสธสลิปเรียบร้อยแล้ว");
  };

  // Add User Action
  const handleCreateUser = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUserName || !newUserEmail) return;

    const newUser: UnifiedUser = {
      id: "usr_" + Date.now().toString().slice(-4),
      name: newUserName,
      email: newUserEmail,
      avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(newUserName)}`,
      role: "member",
      registeredDate: new Date().toISOString().slice(0, 10),
      apps: {
        [newUserApp]: newUserTier,
      },
      totalCredits: newUserTier === "VIP" ? 500 : 100,
      status: "active",
    };

    setUsers((prev) => [newUser, ...prev]);
    setIsAddUserOpen(false);
    setNewUserName("");
    setNewUserEmail("");
    triggerToast(`เพิ่มสมาชิก ${newUser.name} สำเร็จแล้ว`);
  };

  // Filtered Users
  const filteredUsers = useMemo(() => {
    return users.filter((u) => {
      const matchSearch =
        u.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        u.email.toLowerCase().includes(searchQuery.toLowerCase());
      if (appFilter === "all") return matchSearch;
      return matchSearch && u.apps[appFilter];
    });
  }, [users, searchQuery, appFilter]);

  // Total MRR Calculation
  const totalMRR = useMemo(() => {
    return 1480 + 990 + 1180 + 490 + 2450;
  }, []);

  const pendingSlipsCount = useMemo(() => {
    return slips.filter((s) => s.status === "pending").length;
  }, [slips]);

  // ==========================================
  // SECURITY GATE (IF NOT AUTHENTICATED)
  // ==========================================
  if (!isAuthenticated) {
    return (
      <div className="min-h-screen bg-stone-50 flex flex-col items-center justify-center p-4">
        <div className="max-w-md w-full bg-white rounded-3xl border border-black/[0.08] p-8 shadow-xl text-center">
          <div className="w-16 h-16 rounded-2xl bg-[#171717] mx-auto flex items-center justify-center text-white mb-6 shadow-md">
            <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
          </div>
          <span className="text-[11px] font-bold text-[#0569ff] uppercase tracking-wider bg-blue-50 px-3 py-1 rounded-full border border-blue-200">
            ThaiD Central Control
          </span>
          <h1 className="text-2xl font-bold text-[#171717] mt-3">ThaiD Super Admin Gate</h1>
          <p className="text-xs text-stone-500 mt-1.5 leading-relaxed">
            ศูนย์กลางควบคุมระบบทั้งหมดในเครือ ThaiD.online กรุณากรอก Master PIN เพื่อเข้าถึงแดชบอร์ด
          </p>

          <form onSubmit={handlePinSubmit} className="mt-6 space-y-4">
            <div className="text-left">
              <label className="text-[11px] font-bold text-stone-600 block mb-1">
                MASTER SECURITY PIN
              </label>
              <input
                type="password"
                maxLength={6}
                value={pinInput}
                onChange={(e) => setPinInput(e.target.value)}
                placeholder="กรอก PIN 6 หลัก (เช่น 888888)"
                className="w-full px-4 py-3 rounded-2xl border border-black/[0.12] text-center text-lg font-mono tracking-widest focus:outline-none focus:ring-2 focus:ring-[#0569ff]/30 focus:border-[#0569ff]"
                autoFocus
              />
              {pinError && <p className="text-[11px] text-red-500 mt-1.5">{pinError}</p>}
            </div>

            <button
              type="submit"
              className="w-full py-3 bg-[#171717] hover:bg-black text-white rounded-2xl text-xs font-semibold shadow-sm transition-all hover:scale-[1.01] active:scale-[0.99] cursor-pointer"
            >
              ปลดล็อกแดชบอร์ดส่วนกลาง →
            </button>
          </form>

          <div className="mt-6 pt-6 border-t border-black/[0.06] flex items-center justify-between text-xs text-stone-400">
            <Link href="/" className="hover:text-stone-700 transition-colors">
              ← กลับหน้าหลัก ThaiD
            </Link>
            <span>AES-256 Secured Gate</span>
          </div>
        </div>
      </div>
    );
  }

  // ==========================================
  // AUTHENTICATED DASHBOARD VIEW
  // ==========================================
  return (
    <div className="min-h-screen bg-stone-50 text-[#171717] pb-24 font-sans selection:bg-[#0569ff]/15 selection:text-[#0569ff]">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-[100] bg-[#171717] text-white px-5 py-3 rounded-2xl text-xs font-medium shadow-2xl flex items-center gap-3 animate-in fade-in slide-in-from-bottom-5 duration-200">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* ======================================================== */}
      {/* 1. THAID FLOATING TOP NAVBAR (3-ZONE STANDARD)           */}
      {/* ======================================================== */}
      <header className="fixed top-0 inset-x-0 z-[60] pt-4 px-4 sm:px-6 pointer-events-none">
        <div className="max-w-7xl mx-auto flex items-center justify-between pointer-events-auto bg-white/90 backdrop-blur-xl border border-black/[0.08] shadow-[0_4px_24px_rgba(0,0,0,0.04)] rounded-full px-4 sm:px-5 py-2.5 relative">
          
          {/* Zone 1: Left Brand & Breadcrumbs */}
          <Link href="/" className="flex items-center gap-2.5 text-[#2b313b] hover:opacity-85 transition-opacity group flex-shrink-0">
            <div className="w-7 h-7 rounded-lg bg-[#2b313b] flex items-center justify-center text-white shadow-xs group-hover:scale-105 transition-transform">
              <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 6.5H15M9.5 6.5V19" stroke="white" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" />
                <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" strokeWidth="2.2" strokeLinecap="round" />
              </svg>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="font-bold text-lg tracking-tight text-[#2b313b]">ThaiD</span>
              <span className="text-xs text-stone-300 font-light">/</span>
              <span className="text-xs font-medium text-stone-500 hidden sm:inline">Ecosystem</span>
              <span className="text-xs text-stone-300 font-light hidden sm:inline">/</span>
              <span className="text-xs font-bold text-purple-600 bg-purple-50 px-2 py-0.5 rounded-full border border-purple-200">
                Central Super Admin
              </span>
            </div>
          </Link>

          {/* Zone 2: Center - Status Indicator */}
          <div className="hidden lg:flex items-center gap-2 px-3 py-1 bg-stone-100/80 rounded-full border border-black/[0.05] text-[11px] font-medium text-stone-600">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span>8/8 บริการสถานะปกติ (All Services Healthy)</span>
          </div>

          {/* Zone 3: Right Controls & Profile */}
          <div className="flex items-center gap-2 flex-shrink-0">
            <Link
              href="/"
              className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/80 hover:bg-white text-xs font-semibold text-[#2b313b] transition-colors shadow-2xs"
            >
              <span>← กลับหน้าหลัก</span>
            </Link>

            {/* SaaS Services Dropdown */}
            <div className="relative">
              <button
                type="button"
                onClick={() => setIsSaasDropdownOpen(!isSaasDropdownOpen)}
                className="inline-flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-full border border-black/[0.08] bg-white hover:bg-stone-50 text-xs font-semibold text-[#2b313b] transition-all shadow-2xs cursor-pointer"
              >
                <span className="text-[#0569ff] font-bold text-xs">✦</span>
                <span className="hidden sm:inline">เลือกบริการ SaaS</span>
                <span className="sm:hidden">SaaS</span>
                <svg
                  width="10"
                  height="10"
                  viewBox="0 0 16 16"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.2"
                  className={`text-stone-400 transition-transform duration-200 ${
                    isSaasDropdownOpen ? "rotate-180" : ""
                  }`}
                >
                  <path d="m4.5 6 3.5 3.5L11.5 6" />
                </svg>
              </button>

              {isSaasDropdownOpen && (
                <div className="absolute right-0 top-full mt-2 w-72 sm:w-80 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-2 z-50 text-left animate-in fade-in zoom-in-95 duration-150">
                  <div className="px-3 py-1.5 text-[10px] font-bold text-stone-400 uppercase tracking-wider border-b border-black/[0.05] mb-1 flex items-center justify-between">
                    <span>ThaiD SaaS Network</span>
                    <span className="text-emerald-600 font-semibold">8 Subdomains</span>
                  </div>
                  <div className="grid grid-cols-1 gap-1.5 max-h-[380px] overflow-y-auto">
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
                  </div>
                </div>
              )}
            </div>

            {/* Admin Profile Pill */}
            <div className="flex items-center gap-1.5 p-1 pl-1.5 pr-2.5 rounded-full border border-black/[0.08] bg-white shadow-2xs">
              <span className="w-5 h-5 rounded-full bg-purple-600 text-white text-[10px] font-bold flex items-center justify-center">
                👑
              </span>
              <span className="text-xs font-semibold text-[#2b313b] hidden md:inline">
                Admin Boss
              </span>
              <span className="text-[9px] font-bold px-1.5 py-0.2 rounded bg-purple-100 text-purple-700">
                SUPER
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* ======================================================== */}
      {/* 2. HERO BAR & SYSTEM CONTROLS                            */}
      {/* ======================================================== */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 pt-24 sm:pt-28">
        
        {/* Banner Card */}
        <div className="bg-white rounded-3xl border border-black/[0.08] p-6 sm:p-8 shadow-sm relative overflow-hidden">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="text-[10px] font-bold text-purple-700 bg-purple-50 px-2.5 py-0.5 rounded-full border border-purple-200">
                  👑 THAID MASTER CONTROL CENTER
                </span>
                <span className="text-[10px] font-medium text-stone-500 bg-stone-100 px-2.5 py-0.5 rounded-full">
                  Oracle Cloud VM 129.221.170.225
                </span>
              </div>
              <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-[#171717]">
                ระบบควบคุมส่วนกลาง · ทุกแอปในเครือ ThaiD
              </h1>
              <p className="text-xs sm:text-sm text-stone-500 mt-1 max-w-2xl leading-relaxed">
                บริหารจัดการสมาชิกข้ามระบบ, ตรวจสลิปโอนเงิน PromptPay รวมศูนย์, จัดสรรคีย์ AI และมอนิเตอร์สถานะคอนเทนเนอร์ 8 บริการจากหน้าจอเดียว
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-2.5">
              <button
                type="button"
                onClick={() => triggerToast("ซิงค์ข้อมูลคอนเทนเนอร์และฐานข้อมูลล่าสุดเรียบร้อยแล้ว")}
                className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-2xl border border-black/[0.08] bg-white hover:bg-stone-50 text-xs font-semibold text-[#171717] transition-all cursor-pointer shadow-xs hover:border-black/[0.2]"
              >
                <svg className="w-3.5 h-3.5 text-stone-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
                  <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67" />
                </svg>
                <span>รีเฟรชข้อมูล</span>
              </button>

              <button
                type="button"
                onClick={() => setIsAddUserOpen(true)}
                className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-2xl bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold transition-all cursor-pointer shadow-xs hover:scale-[1.01]"
              >
                <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <path d="M12 5v14M5 12h14" />
                </svg>
                <span>+ เพิ่มสมาชิกใหม่</span>
              </button>

              <Link
                href="https://social.thaid.online/admin"
                target="_blank"
                className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-2xl border border-purple-200 bg-purple-50/50 hover:bg-purple-100/50 text-xs font-semibold text-purple-700 transition-all"
              >
                <span>เปิด Social Admin ↗</span>
              </Link>
            </div>
          </div>

          {/* Quick SaaS Filter Pills */}
          <div className="mt-6 pt-5 border-t border-black/[0.06] flex items-center gap-2 overflow-x-auto pb-1">
            <span className="text-[11px] font-bold text-stone-400 uppercase tracking-wider flex-shrink-0">
              กรองตามบริการ:
            </span>
            <button
              onClick={() => setAppFilter("all")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "all"
                  ? "bg-[#171717] text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              ทั้งหมด (8 แอพ)
            </button>
            <button
              onClick={() => setAppFilter("novel")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "novel"
                  ? "bg-indigo-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Novel Studio
            </button>
            <button
              onClick={() => setAppFilter("social")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "social"
                  ? "bg-emerald-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Social Poster
            </button>
            <button
              onClick={() => setAppFilter("sticker")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "sticker"
                  ? "bg-pink-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              LINE Sticker
            </button>
            <button
              onClick={() => setAppFilter("clip")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "clip"
                  ? "bg-purple-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Clip AI
            </button>
            <button
              onClick={() => setAppFilter("chat")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "chat"
                  ? "bg-teal-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Smart Chat
            </button>
            <button
              onClick={() => setAppFilter("mockup")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "mockup"
                  ? "bg-sky-600 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Mockup Studio
            </button>
            <button
              onClick={() => setAppFilter("vault")}
              className={`px-3 py-1 rounded-full text-xs font-semibold transition-all cursor-pointer flex-shrink-0 ${
                appFilter === "vault"
                  ? "bg-cyan-700 text-white"
                  : "bg-stone-100 text-stone-600 hover:bg-stone-200"
              }`}
            >
              Private Vault
            </button>
          </div>
        </div>

        {/* ======================================================== */}
        {/* 3. SOLID HIGH-CONTRAST COUNTER CARDS (5 METRICS)         */}
        {/* ======================================================== */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3.5 mt-5">
          {/* Card 1: Users */}
          <div className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-stone-500">สมาชิกทั้งหมด (คน)</span>
              <div className="w-8 h-8 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
                👥
              </div>
            </div>
            <div className="text-2xl font-black text-purple-700">1,248</div>
            <div className="text-[11px] text-stone-400 mt-0.5">รวมทุกบริการในเครือ</div>
          </div>

          {/* Card 2: Total MRR */}
          <div className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-stone-500">ประมาณการ MRR รวม</span>
              <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
                💰
              </div>
            </div>
            <div className="text-2xl font-black text-emerald-600">
              ฿{totalMRR.toLocaleString()}
            </div>
            <div className="text-[11px] text-stone-400 mt-0.5">รายได้ประจำเดือนนี้</div>
          </div>

          {/* Card 3: Pending Slips */}
          <div className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-stone-500">สลิปรอตรวจสอบ</span>
              <div className="w-8 h-8 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
                🧾
              </div>
            </div>
            <div className="text-2xl font-black text-amber-500">{pendingSlipsCount} รายการ</div>
            <div className="text-[11px] text-stone-400 mt-0.5">PromptPay & โอนเงิน</div>
          </div>

          {/* Card 4: Global AI Pool */}
          <div className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-stone-500">คลังคีย์ AI ส่วนกลาง</span>
              <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#0569ff] flex items-center justify-center">
                🧠
              </div>
            </div>
            <div className="text-2xl font-black text-[#0569ff]">{aiKeys.length} คีย์</div>
            <div className="text-[11px] text-stone-400 mt-0.5">Gemini, Flux, SDXL</div>
          </div>

          {/* Card 5: System Health */}
          <div className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs col-span-2 sm:col-span-1">
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-stone-500">สถานะคอนเทนเนอร์</span>
              <div className="w-8 h-8 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
                ⚡
              </div>
            </div>
            <div className="text-2xl font-black text-emerald-600">8 / 8 Online</div>
            <div className="text-[11px] text-stone-400 mt-0.5">0 Failed / VM 53% Disk</div>
          </div>
        </div>

        {/* ======================================================== */}
        {/* 4. SEGMENTED TAB BAR                                     */}
        {/* ======================================================== */}
        <div className="bg-white rounded-2xl border border-black/[0.08] p-1.5 shadow-xs mt-6 flex items-center gap-1.5 overflow-x-auto">
          <button
            onClick={() => setActiveTab("overview")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex-shrink-0 flex items-center gap-2 ${
              activeTab === "overview"
                ? "bg-[#171717] text-white shadow-xs"
                : "text-stone-600 hover:bg-stone-50"
            }`}
          >
            <span>💻 1. คอนเทนเนอร์ & บริการ</span>
            <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-white/20 text-white font-mono">
              8
            </span>
          </button>

          <button
            onClick={() => setActiveTab("users")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex-shrink-0 flex items-center gap-2 ${
              activeTab === "users"
                ? "bg-[#171717] text-white shadow-xs"
                : "text-stone-600 hover:bg-stone-50"
            }`}
          >
            <span>👥 2. สมาชิกส่วนกลาง</span>
            <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-purple-100 text-purple-700 font-mono">
              {filteredUsers.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab("slips")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex-shrink-0 flex items-center gap-2 ${
              activeTab === "slips"
                ? "bg-[#171717] text-white shadow-xs"
                : "text-stone-600 hover:bg-stone-50"
            }`}
          >
            <span>🧾 3. ตรวจสลิป & รายได้</span>
            {pendingSlipsCount > 0 && (
              <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-amber-500 text-white font-mono animate-pulse">
                {pendingSlipsCount} รอตรวจ
              </span>
            )}
          </button>

          <button
            onClick={() => setActiveTab("aipool")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex-shrink-0 flex items-center gap-2 ${
              activeTab === "aipool"
                ? "bg-[#171717] text-white shadow-xs"
                : "text-stone-600 hover:bg-stone-50"
            }`}
          >
            <span>🧠 4. คลังคีย์ AI กลาง</span>
            <span className="px-1.5 py-0.2 rounded-full text-[10px] bg-blue-100 text-blue-700 font-mono">
              {aiKeys.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab("logs")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex-shrink-0 flex items-center gap-2 ${
              activeTab === "logs"
                ? "bg-[#171717] text-white shadow-xs"
                : "text-stone-600 hover:bg-stone-50"
            }`}
          >
            <span>📋 5. Audit Logs</span>
          </button>
        </div>

        {/* ======================================================== */}
        {/* 5. TAB 1: CONTAINERS & SERVICES OVERVIEW                 */}
        {/* ======================================================== */}
        {activeTab === "overview" && (
          <div className="mt-5 space-y-4">
            {/* Host Status Card */}
            <div className="bg-white rounded-2xl border border-black/[0.08] p-5 shadow-xs">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div className="flex items-center gap-3.5">
                  <div className="w-10 h-10 rounded-2xl bg-stone-100 flex items-center justify-center text-xl">
                    🖥️
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-bold text-[#171717]">
                        Oracle Cloud VM Host (Ubuntu 24.04 ARM)
                      </span>
                      <span className="w-2 h-2 rounded-full bg-emerald-500" />
                      <span className="text-xs text-emerald-600 font-semibold">Online & Healthy</span>
                    </div>
                    <p className="text-xs text-stone-500 mt-0.5 font-mono">
                      IP: 129.221.170.225 · Docker Engine 28.0.0 · Coolify Manager v4
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-4 text-xs font-medium text-stone-600">
                  <div className="text-right">
                    <div className="text-[11px] text-stone-400">พื้นที่ดิสก์คงเหลือ</div>
                    <div className="font-bold text-[#171717]">23.4 GB / 48.0 GB (53%)</div>
                  </div>
                  <div className="w-28 h-2 bg-stone-100 rounded-full overflow-hidden border border-black/[0.05]">
                    <div className="w-[53%] h-full bg-emerald-500 rounded-full" />
                  </div>
                </div>
              </div>
            </div>

            {/* Containers Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3.5">
              {APPS_LIST.map((app) => (
                <div
                  key={app.id}
                  className="bg-white rounded-2xl border border-black/[0.08] p-4.5 shadow-xs flex flex-col justify-between hover:border-black/[0.2] transition-colors"
                >
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span
                        className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${app.badgeColor}`}
                      >
                        {app.category}
                      </span>
                      <div className="flex items-center gap-1.5">
                        <span className="w-2 h-2 rounded-full bg-emerald-500" />
                        <span className="text-[10px] font-mono text-stone-400 font-medium">
                          Port {app.port}
                        </span>
                      </div>
                    </div>

                    <h3 className="text-sm font-bold text-[#171717]">{app.name}</h3>
                    <div className="text-xs font-mono text-stone-400 mt-0.5">{app.subdomain}</div>
                    <p className="text-xs text-stone-500 mt-2 leading-relaxed">
                      {app.description}
                    </p>
                  </div>

                  <div className="mt-4 pt-3 border-t border-black/[0.05] space-y-2">
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
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ======================================================== */}
        {/* 6. TAB 2: UNIFIED USER DIRECTORY                         */}
        {/* ======================================================== */}
        {activeTab === "users" && (
          <div className="mt-5 bg-white rounded-3xl border border-black/[0.08] p-6 shadow-xs">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-5 border-b border-black/[0.06]">
              <div>
                <h2 className="text-base font-bold text-[#171717]">
                  รายชื่อสมาชิกส่วนกลาง (Unified User Directory)
                </h2>
                <p className="text-xs text-stone-500 mt-0.5">
                  จัดการสิทธิ์ข้ามบริการ เติมเครดิต และสลับจอดูมุมมองผู้ใช้ (Impersonate)
                </p>
              </div>

              <div className="flex items-center gap-2">
                <input
                  type="text"
                  placeholder="ค้นหาชื่อ, อีเมลสมาชิก..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="px-3.5 py-2 rounded-xl border border-black/[0.1] text-xs w-64 focus:outline-none focus:ring-2 focus:ring-[#0569ff]/20 focus:border-[#0569ff]"
                />
                <button
                  type="button"
                  onClick={() => setIsAddUserOpen(true)}
                  className="px-3.5 py-2 rounded-xl bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold transition-all cursor-pointer flex-shrink-0"
                >
                  + เพิ่มสมาชิก
                </button>
              </div>
            </div>

            {/* Users Table */}
            <div className="overflow-x-auto mt-4">
              <table className="w-full text-left text-xs">
                <thead>
                  <tr className="border-b border-black/[0.06] text-stone-400 font-bold uppercase text-[10px] tracking-wider">
                    <th className="py-3 px-3">สมาชิก</th>
                    <th className="py-3 px-3">สิทธิ์ในระบบ (ROLE)</th>
                    <th className="py-3 px-3">บริการที่ใช้งาน (ACTIVE APPS)</th>
                    <th className="py-3 px-3 text-center">เครดิตรวม</th>
                    <th className="py-3 px-3">สถานะ</th>
                    <th className="py-3 px-3 text-right">การจัดการ</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-black/[0.04]">
                  {filteredUsers.map((u) => (
                    <tr key={u.id} className="hover:bg-stone-50/60 transition-colors">
                      <td className="py-3.5 px-3">
                        <div className="flex items-center gap-3">
                          <img
                            src={u.avatar}
                            alt={u.name}
                            className="w-8 h-8 rounded-full bg-stone-100 ring-1 ring-black/[0.05]"
                          />
                          <div>
                            <div className="font-bold text-[#171717]">{u.name}</div>
                            <div className="text-[11px] text-stone-400">{u.email}</div>
                          </div>
                        </div>
                      </td>
                      <td className="py-3.5 px-3">
                        <span
                          className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                            u.role === "superadmin"
                              ? "bg-purple-100 text-purple-700"
                              : u.role === "vip"
                              ? "bg-amber-100 text-amber-700"
                              : "bg-stone-100 text-stone-600"
                          }`}
                        >
                          {u.role.toUpperCase()}
                        </span>
                      </td>
                      <td className="py-3.5 px-3">
                        <div className="flex flex-wrap items-center gap-1.5">
                          {Object.entries(u.apps).map(([app, tier]) => (
                            <span
                              key={app}
                              className="px-2 py-0.5 rounded-md bg-stone-100 text-stone-700 text-[10px] font-medium border border-black/[0.04]"
                            >
                              <strong className="text-stone-900">{app}:</strong> {tier}
                            </span>
                          ))}
                        </div>
                      </td>
                      <td className="py-3.5 px-3 text-center">
                        <span className="font-mono font-bold text-purple-600">
                          {u.totalCredits.toLocaleString()}
                        </span>
                      </td>
                      <td className="py-3.5 px-3">
                        <span className="inline-flex items-center gap-1.5 text-emerald-600 font-semibold">
                          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                          <span>ปกติ</span>
                        </span>
                      </td>
                      <td className="py-3.5 px-3 text-right">
                        <div className="inline-flex items-center gap-1.5">
                          <button
                            type="button"
                            onClick={() => triggerToast(`สลับสู่มุมมองผู้ใช้: ${u.name}`)}
                            className="px-2.5 py-1 rounded-lg border border-black/[0.08] hover:bg-stone-100 text-[11px] font-semibold text-stone-700 transition-colors cursor-pointer"
                          >
                            👁️ ดูหน้า User
                          </button>
                          <button
                            type="button"
                            onClick={() => triggerToast(`เปิดหน้าต่างแก้ไขสิทธิ์: ${u.name}`)}
                            className="px-2.5 py-1 rounded-lg border border-black/[0.08] hover:bg-stone-100 text-[11px] font-semibold text-stone-700 transition-colors cursor-pointer"
                          >
                            แก้ไขสิทธิ์
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* ======================================================== */}
        {/* 7. TAB 3: CENTRALIZED SLIP VERIFICATION & BILLING        */}
        {/* ======================================================== */}
        {activeTab === "slips" && (
          <div className="mt-5 space-y-4">
            <div className="bg-white rounded-3xl border border-black/[0.08] p-6 shadow-xs">
              <div className="flex items-center justify-between pb-4 border-b border-black/[0.06]">
                <div>
                  <h2 className="text-base font-bold text-[#171717]">
                    ศูนย์ตรวจสลิปโอนเงิน PromptPay & รายได้รวม
                  </h2>
                  <p className="text-xs text-stone-500 mt-0.5">
                    ตรวจสอบสลิปแจ้งชำระเงินจากทุกบริการ SaaS และอนุมัติเปิดใช้งานอัตโนมัติ
                  </p>
                </div>
                <span className="text-xs font-bold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
                  PromptPay Slip Verifier Active
                </span>
              </div>

              {/* Slips Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-5">
                {slips.map((slip) => (
                  <div
                    key={slip.id}
                    className={`rounded-2xl border p-5 transition-all ${
                      slip.status === "pending"
                        ? "bg-amber-50/20 border-amber-200 shadow-xs"
                        : slip.status === "approved"
                        ? "bg-emerald-50/20 border-emerald-200 opacity-80"
                        : "bg-stone-50 border-stone-200 opacity-60"
                    }`}
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg font-bold">
                          🧾
                        </div>
                        <div>
                          <div className="text-xs font-bold text-[#171717]">{slip.userName}</div>
                          <div className="text-[11px] text-stone-400">{slip.userEmail}</div>
                        </div>
                      </div>

                      <span
                        className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full ${
                          slip.status === "pending"
                            ? "bg-amber-100 text-amber-800"
                            : slip.status === "approved"
                            ? "bg-emerald-100 text-emerald-800"
                            : "bg-red-100 text-red-800"
                        }`}
                      >
                        {slip.status === "pending"
                          ? "รอตรวจสอบ"
                          : slip.status === "approved"
                          ? "อนุมัติแล้ว"
                          : "ปฏิเสธ"}
                      </span>
                    </div>

                    <div className="mt-4 p-3 rounded-xl bg-white border border-black/[0.05] space-y-1.5 text-xs">
                      <div className="flex justify-between">
                        <span className="text-stone-400">บริการเป้าหมาย:</span>
                        <span className="font-bold text-stone-800">{slip.appTarget}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-stone-400">แพ็กเกจ:</span>
                        <span className="font-semibold text-purple-600">{slip.planName}</span>
                      </div>
                      <div className="flex justify-between">
                        <span className="text-stone-400">ยอดเงินโอน:</span>
                        <span className="font-mono font-black text-emerald-600 text-sm">
                          ฿{slip.amount.toLocaleString()}
                        </span>
                      </div>
                      <div className="flex justify-between text-[11px] text-stone-400 pt-1 border-t border-black/[0.04]">
                        <span>{slip.bank}</span>
                        <span>{slip.slipTime}</span>
                      </div>
                    </div>

                    {slip.status === "pending" && (
                      <div className="mt-4 flex items-center gap-2">
                        <button
                          type="button"
                          onClick={() => handleApproveSlip(slip.id)}
                          className="flex-1 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition-all shadow-xs cursor-pointer flex items-center justify-center gap-1.5"
                        >
                          <span>✓ อนุมัติสลิป & เปิดสิทธิ์</span>
                        </button>
                        <button
                          type="button"
                          onClick={() => handleRejectSlip(slip.id)}
                          className="px-4 py-2 rounded-xl border border-black/[0.1] hover:bg-stone-100 text-stone-600 text-xs font-semibold transition-all cursor-pointer"
                        >
                          ปฏิเสธ
                        </button>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* ======================================================== */}
        {/* 8. TAB 4: GLOBAL AI KEY POOL & LOAD BALANCER             */}
        {/* ======================================================== */}
        {activeTab === "aipool" && (
          <div className="mt-5 bg-white rounded-3xl border border-black/[0.08] p-6 shadow-xs">
            <div className="flex items-center justify-between pb-4 border-b border-black/[0.06]">
              <div>
                <h2 className="text-base font-bold text-[#171717]">
                  คลังคีย์ AI ส่วนกลาง (Global AI Pool & Failover)
                </h2>
                <p className="text-xs text-stone-500 mt-0.5">
                  จัดสรร Google Gemini, Claude และ Flux Turbo API Keys กระจายโควต้าและสลับคีย์สำรองอัตโนมัติ
                </p>
              </div>
              <button
                type="button"
                onClick={() => triggerToast("เปิดหน้าต่างเพิ่ม API Key")}
                className="px-3.5 py-2 rounded-xl bg-[#0569ff] hover:bg-blue-600 text-white text-xs font-semibold transition-all cursor-pointer"
              >
                + เพิ่ม API Key กลาง
              </button>
            </div>

            <div className="space-y-3.5 mt-5">
              {aiKeys.map((key) => (
                <div
                  key={key.id}
                  className="p-4.5 rounded-2xl border border-black/[0.08] bg-white flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:border-black/[0.2] transition-colors"
                >
                  <div className="flex items-start gap-3.5">
                    <div className="w-10 h-10 rounded-xl bg-blue-50 text-[#0569ff] flex items-center justify-center text-lg font-bold flex-shrink-0">
                      ⚡
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <h4 className="text-sm font-bold text-[#171717]">{key.label}</h4>
                        <span
                          className={`text-[9px] font-bold px-2 py-0.5 rounded-full ${
                            key.status === "active"
                              ? "bg-emerald-50 text-emerald-700 border border-emerald-200"
                              : "bg-blue-50 text-blue-700 border border-blue-200"
                          }`}
                        >
                          {key.status === "active" ? "ทำงานปกติ (Active)" : "สแตนด์บาย (Standby)"}
                        </span>
                      </div>
                      <div className="text-xs font-mono text-stone-500 mt-1">
                        Provider: {key.provider} · Key: <span className="text-stone-800">{key.keyMasked}</span>
                      </div>
                      <div className="flex flex-wrap items-center gap-1.5 mt-2">
                        {key.models.map((m) => (
                          <span
                            key={m}
                            className="text-[10px] font-mono bg-stone-100 text-stone-600 px-2 py-0.5 rounded border border-black/[0.04]"
                          >
                            {m}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  <div className="text-right sm:flex-shrink-0">
                    <div className="text-xs font-bold text-stone-800">
                      {key.usageCount.toLocaleString()} ครั้ง
                    </div>
                    <div className="text-[11px] text-stone-400 mt-0.5">{key.rateLimit}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ======================================================== */}
        {/* 9. TAB 5: AUDIT LOGS                                     */}
        {/* ======================================================== */}
        {activeTab === "logs" && (
          <div className="mt-5 bg-white rounded-3xl border border-black/[0.08] p-6 shadow-xs">
            <h2 className="text-base font-bold text-[#171717] pb-3 border-b border-black/[0.06]">
              บันทึกเหตุการณ์ระบบ (Global Audit Logs)
            </h2>
            <div className="divide-y divide-black/[0.04] mt-3">
              {logs.map((log) => (
                <div key={log.id} className="py-3.5 flex items-start justify-between gap-4 text-xs">
                  <div className="flex items-start gap-3">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 mt-1.5 flex-shrink-0" />
                    <div>
                      <div className="font-bold text-[#171717]">
                        {log.action} · <span className="text-purple-600">{log.app}</span>
                      </div>
                      <div className="text-stone-500 mt-0.5">{log.details}</div>
                      <div className="text-[10px] text-stone-400 mt-1">กระทำโดย: {log.actor}</div>
                    </div>
                  </div>
                  <span className="text-[11px] font-mono text-stone-400 flex-shrink-0">
                    {log.time}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

      </main>

      {/* ======================================================== */}
      {/* 10. MODAL: ADD USER CROSS-SERVICE                        */}
      {/* ======================================================== */}
      {isAddUserOpen && (
        <div className="fixed inset-0 z-[120] bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl border border-black/[0.08] p-6 sm:p-7 max-w-md w-full shadow-2xl animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center justify-between pb-3 border-b border-black/[0.06]">
              <h3 className="text-base font-bold text-[#171717]">+ เพิ่มสมาชิกใหม่ส่วนกลาง</h3>
              <button
                onClick={() => setIsAddUserOpen(false)}
                className="text-stone-400 hover:text-stone-700 text-lg cursor-pointer"
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleCreateUser} className="mt-4 space-y-3.5 text-xs">
              <div>
                <label className="font-bold text-stone-600 block mb-1">ชื่อผู้ใช้งาน</label>
                <input
                  type="text"
                  required
                  placeholder="เช่น คุณสมชาย ครีเอเตอร์"
                  value={newUserName}
                  onChange={(e) => setNewUserName(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-black/[0.1] focus:outline-none focus:ring-2 focus:ring-purple-600/20 focus:border-purple-600"
                />
              </div>

              <div>
                <label className="font-bold text-stone-600 block mb-1">อีเมลผู้ใช้งาน</label>
                <input
                  type="email"
                  required
                  placeholder="somchai@creator.com"
                  value={newUserEmail}
                  onChange={(e) => setNewUserEmail(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-black/[0.1] focus:outline-none focus:ring-2 focus:ring-purple-600/20 focus:border-purple-600"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="font-bold text-stone-600 block mb-1">เปิดสิทธิ์ในแอพ</label>
                  <select
                    value={newUserApp}
                    onChange={(e) => setNewUserApp(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-black/[0.1] focus:outline-none focus:border-purple-600"
                  >
                    <option value="novel">Novel Studio</option>
                    <option value="social">Social Poster</option>
                    <option value="sticker">LINE Sticker</option>
                    <option value="clip">Clip AI</option>
                    <option value="chat">Smart Chat</option>
                    <option value="mockup">Mockup Studio</option>
                    <option value="vault">Private Vault</option>
                  </select>
                </div>

                <div>
                  <label className="font-bold text-stone-600 block mb-1">ระดับแพ็กเกจ (Tier)</label>
                  <select
                    value={newUserTier}
                    onChange={(e) => setNewUserTier(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-black/[0.1] focus:outline-none focus:border-purple-600"
                  >
                    <option value="Free Trial">Free Trial</option>
                    <option value="Pro">Pro Plan</option>
                    <option value="VIP">VIP Agency</option>
                    <option value="Unlimited">Unlimited All-Access</option>
                  </select>
                </div>
              </div>

              <div className="pt-3 border-t border-black/[0.06] flex items-center justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setIsAddUserOpen(false)}
                  className="px-4 py-2 rounded-xl border border-black/[0.1] text-stone-600 hover:bg-stone-50 font-semibold"
                >
                  ยกเลิก
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold transition-all shadow-xs"
                >
                  บันทึกสมาชิก
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
