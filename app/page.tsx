"use client";

import React, { useState } from "react";
import {
  BookOpen,
  Share2,
  Sparkles,
  ArrowRight,
  ShieldCheck,
  Zap,
  Layers,
  Coins,
  CheckCircle2,
  ChevronDown,
  Menu,
  X,
  ExternalLink,
  Laptop,
  Check,
  Star,
  Users,
  TrendingUp,
  Image as ImageIcon,
  MessageSquare,
} from "lucide-react";

export default function Home() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [faqOpen, setFaqOpen] = useState<number | null>(0);

  const toggleFaq = (index: number) => {
    setFaqOpen(faqOpen === index ? null : index);
  };

  const services = [
    {
      id: "novel",
      name: "ThaiD Novel Studio",
      subdomain: "novel.thaid.online",
      badge: "AI สำหรับนักเขียนและสำนักพิมพ์",
      badgeColor: "from-amber-500 to-orange-500",
      icon: BookOpen,
      iconColor: "text-amber-400",
      accentBg: "bg-amber-500/10 border-amber-500/20",
      glowColor: "group-hover:border-amber-500/50",
      tagline: "ระบบสตูดิโอแต่งนิยายและพล็อตเรื่องอัจฉริยะ",
      description:
        "เขียนนิยายได้ไวขึ้น 10 เท่า ด้วย AI ช่วยคิดพล็อต สร้างภูมิหลังตัวละคร ตรวจสอบบทสนทนา พร้อมระบบสร้างภาพปกนิยายและเผยแพร่ออนไลน์ในที่เดียว",
      features: [
        "ระบบแต่งนิยาย Rich Editor พร้อมโหมดสว่าง-ซีเปีย-มืด",
        "AI Co-Writer ช่วยคิดพล็อตและแตกบทบรรยายตามสไตล์คุณ",
        "ระบบสร้างภาพปกนิยายความละเอียดสูง สไตล์อนิเมะและสมจริง",
        "ระบบอ่านนิยายทั้งแบบบรรยาย (Text) และแชท (Chat Fiction)",
        "รองรับการติดเหรียญและระบบโดเนทของขวัญให้นักเขียน",
      ],
      href: "https://novel.thaid.online",
      status: "พร้อมใช้งาน",
    },
    {
      id: "social",
      name: "ThaiD Social Auto-Post",
      subdomain: "social.thaid.online",
      badge: "AI สำหรับธุรกิจ & แอดมินเพจ",
      badgeColor: "from-blue-500 to-cyan-500",
      icon: Share2,
      iconColor: "text-cyan-400",
      accentBg: "bg-cyan-500/10 border-cyan-500/20",
      glowColor: "group-hover:border-cyan-500/50",
      tagline: "ระบบสร้างคอนเทนต์และตั้งเวลาโพสต์ Facebook อัตโนมัติ",
      description:
        "หมดปัญหาตันไอเดีย! AI ช่วยสร้างแคปชั่นเกาะกระแส ออกแบบภาพกราฟิกประกอบ และตั้งเวลาโพสต์ลง Facebook Fanpage ล่วงหน้าได้แบบอัตโนมัติ 24 ชม.",
      features: [
        "AI Content Generator คิดแคปชั่นและแฮชแท็กโดนใจตามหมวดหมู่",
        "Auto-Schedule ตั้งเวลาโพสต์ล่วงหน้าได้เป็นเดือน ไม่ต้องเฝ้าจอ",
        "Multi-Page Management เชื่อมต่อและจัดการได้หลายเพจพร้อมกัน",
        "วิเคราะห์สถิติ Engagement และช่วงเวลาที่ลูกเพจมีส่วนร่วมสูงสุด",
        "รองรับระบบตอบแชทและคอมเมนต์อัตโนมัติ (Coming Soon)",
      ],
      href: "https://social.thaid.online",
      status: "พร้อมใช้งาน",
    },
    {
      id: "sticker",
      name: "ThaiD Sticker Studio",
      subdomain: "sticker.thaid.online",
      badge: "AI สำหรับนักวาด & ครีเอเตอร์",
      badgeColor: "from-emerald-500 to-teal-500",
      icon: Sparkles,
      iconColor: "text-emerald-400",
      accentBg: "bg-emerald-500/10 border-emerald-500/20",
      glowColor: "group-hover:border-emerald-500/50",
      tagline: "ระบบออกแบบและผลิตสติกเกอร์ไลน์ด้วย AI ครบชุด",
      description:
        "ออกแบบคาแรกเตอร์สติกเกอร์ไลน์สวยงาม 40 ท่าทางได้ภายในไม่กี่นาที ระบบตัดพื้นหลังโปร่งใสและปรับขนาดไฟล์ตามมาตรฐาน LINE Creators Market เป๊ะ 100%",
      features: [
        "สร้างคาแรกเตอร์สม่ำเสมอ (Consistent Character) ทุกแอ็กชัน",
        "ตัดพื้นหลังโปร่งใส PNG และจัดขนาดตามสเปก LINE อัตโนมัติ",
        "ชุดแพ็กสติกเกอร์สำเร็จรูป 8, 16, 24, 32 และ 40 รูปพร้อมส่ง",
        "ระบบใส่ข้อความภาษาไทยฟอนต์น่ารักลงบนสติกเกอร์",
        "ส่งออกเป็น ZIP ไฟล์พร้อมอัปโหลดขึ้น LINE Creators Market ได้ทันที",
      ],
      href: "https://sticker.thaid.online",
      status: "พร้อมใช้งาน",
    },
  ];

  const faqs = [
    {
      q: "ต้องสมัครสมาชิกแยกแต่ละบริการหรือไม่?",
      a: "ไม่ต้องครับ! แพลตฟอร์ม ThaiD.online ใช้ระบบ Single Sign-On (SSO) ผ่านบัญชีกลางบัญชีเดียว (auth.thaid.online) คุณสามารถล็อกอินครั้งเดียวแล้วเปิดใช้งานได้ทั้งระบบแต่งนิยาย, ระบบคอนเทนต์ Facebook และระบบทำสติกเกอร์ไลน์ทันที",
    },
    {
      q: "มีให้ทดลองใช้งานฟรีก่อนหรือไม่?",
      a: "มีครับ ผู้ใช้งานใหม่ทุกคนสามารถลงทะเบียนเพื่อรับเหรียญเครดิตทดลองใช้งานฟรีในทุกบริการโดยไม่มีค่าใช้จ่าย และไม่ต้องผูกบัตรเครดิต",
    },
    {
      q: "ระบบสติกเกอร์ไลน์ AI ส่งตรวจกับ LINE ผ่านแน่นอนไหม?",
      a: "ระบบ ThaiD Sticker Studio ถูกพัฒนาขึ้นโดยคำนึงถึง Guideline ของ LINE Creators Market ทั้งเรื่องขนาดพิกเซล (370x320 px), ระยะขอบ Safe Zone 10 px, และการบีบอัดไฟล์ภาพโปร่งใส จึงมั่นใจได้ว่าจะผ่านเกณฑ์ด้านเทคนิค 100%",
    },
    {
      q: "ระบบ Facebook Auto-Post ปลอดภัยต่อเพจหรือไม่?",
      a: "ปลอดภัย 100% ครับ ระบบเชื่อมต่อผ่าน Facebook Official Graph API ที่ได้รับการอนุญาตอย่างถูกต้องจาก Meta โดยไม่มีการขอรหัสผ่านส่วนตัวของบัญชีคุณ",
    },
    {
      q: "ข้อมูลและผลงานที่สร้างเป็นลิขสิทธิ์ของใคร?",
      a: "ผลงานทั้งหมดที่คุณสร้างผ่านแพลตฟอร์ม ThaiD.online (ไม่ว่าจะเป็นเนื้อหานิยาย, แคปชั่น, ภาพกราฟิก หรือสติกเกอร์) เป็นลิขสิทธิ์ของคุณ 100% สามารถนำไปจำหน่าย ทำการค้า หรือเผยแพร่ต่อได้อิสระ",
    },
  ];

  return (
    <div className="flex flex-col min-h-screen">
      {/* ── Top Bar Announcement ── */}
      <div className="bg-gradient-to-r from-indigo-900/60 via-purple-900/60 to-pink-900/60 border-b border-indigo-500/20 px-4 py-2 text-center text-xs sm:text-sm text-indigo-200">
        <span className="font-semibold text-white">✨ เปิดตัว ThaiD Ecosystem:</span>{" "}
        รวมทุกเครื่องมือ AI เพื่อคนไทย เชื่อมต่อระบบเดียว สมัครวันนี้รับเครดิตทดลองฟรี!
      </div>

      {/* ── Header / Navigation ── */}
      <header className="sticky top-0 z-50 glass-nav">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          {/* Logo */}
          <a href="#" className="flex items-center gap-3 group">
            <div className="w-11 h-11 rounded-2xl bg-gradient-to-br from-indigo-500 via-purple-600 to-pink-500 p-[1.5px] transition-transform duration-300 group-hover:scale-105">
              <div className="w-full h-full bg-[#07090e] rounded-2xl flex items-center justify-center">
                <span className="font-extrabold text-xl bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">
                  TD
                </span>
              </div>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-2xl tracking-tight text-white font-['Plus_Jakarta_Sans']">
                  ThaiD<span className="text-indigo-400">.online</span>
                </span>
                <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                  AI SaaS
                </span>
              </div>
              <p className="text-[11px] text-slate-400 hidden sm:block">
                ศูนย์รวมเครื่องมือ AI สำหรับคนไทย
              </p>
            </div>
          </a>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-300">
            <a href="#services" className="hover:text-white transition-colors">
              บริการของเรา
            </a>
            <a href="#ecosystem" className="hover:text-white transition-colors">
              จุดเด่น
            </a>
            <a href="#pricing" className="hover:text-white transition-colors">
              แพ็กเกจราคา
            </a>
            <a href="#faq" className="hover:text-white transition-colors">
              คำถามที่พบบ่อย
            </a>
          </nav>

          {/* Desktop Right CTA */}
          <div className="hidden md:flex items-center gap-3">
            <a
              href="https://auth.thaid.online"
              className="px-4 py-2 text-sm font-medium text-slate-200 hover:text-white transition-colors"
            >
              เข้าสู่ระบบ
            </a>
            <a
              href="#services"
              className="px-5 py-2.5 rounded-xl text-sm font-semibold text-white bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:opacity-95 shadow-lg shadow-indigo-600/25 transition-all duration-200 hover:scale-[1.02]"
            >
              ทดลองใช้ฟรี
            </a>
          </div>

          {/* Mobile menu button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 text-slate-300 hover:text-white"
            aria-label="Toggle Menu"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile menu dropdown */}
        {mobileMenuOpen && (
          <div className="md:hidden bg-[#0d111a] border-b border-slate-800 px-6 py-6 flex flex-col gap-4">
            <a
              href="#services"
              onClick={() => setMobileMenuOpen(false)}
              className="text-slate-200 hover:text-white py-2"
            >
              บริการของเรา
            </a>
            <a
              href="#ecosystem"
              onClick={() => setMobileMenuOpen(false)}
              className="text-slate-200 hover:text-white py-2"
            >
              จุดเด่น
            </a>
            <a
              href="#pricing"
              onClick={() => setMobileMenuOpen(false)}
              className="text-slate-200 hover:text-white py-2"
            >
              แพ็กเกจราคา
            </a>
            <a
              href="#faq"
              onClick={() => setMobileMenuOpen(false)}
              className="text-slate-200 hover:text-white py-2"
            >
              คำถามที่พบบ่อย
            </a>
            <div className="pt-4 border-t border-slate-800 flex flex-col gap-3">
              <a
                href="https://auth.thaid.online"
                className="w-full text-center py-2.5 rounded-xl border border-slate-700 text-sm font-medium text-slate-200"
              >
                เข้าสู่ระบบ
              </a>
              <a
                href="#services"
                onClick={() => setMobileMenuOpen(false)}
                className="w-full text-center py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 text-sm font-semibold text-white"
              >
                ทดลองใช้ฟรี
              </a>
            </div>
          </div>
        )}
      </header>

      {/* ── Hero Section ── */}
      <section className="relative overflow-hidden pt-16 pb-24 lg:pt-28 lg:pb-32">
        {/* Glowing Background Orbs */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[400px] bg-gradient-to-tr from-indigo-600/20 via-purple-600/20 to-pink-500/15 blur-[120px] rounded-full pointer-events-none -z-10" />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900/80 border border-indigo-500/30 text-indigo-300 text-xs sm:text-sm font-medium mb-8 backdrop-blur-md shadow-inner">
            <Sparkles className="w-4 h-4 text-indigo-400" />
            <span>แพลตฟอร์ม AI ครบวงจร อันดับ 1 เพื่อครีเอเตอร์และธุรกิจไทย</span>
          </div>

          {/* Main Headline */}
          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white mb-6 leading-[1.15]">
            ปลดล็อกพลังแห่งอนาคต <br />
            <span className="bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">
              สร้างสรรค์ผลงานด้วย AI
            </span>
          </h1>

          {/* Subtitle */}
          <p className="max-w-3xl mx-auto text-base sm:text-xl text-slate-300 font-light mb-10 leading-relaxed">
            ศูนย์รวมโซลูชัน AI อัจฉริยะภาษาไทยที่จะช่วยคุณประหยัดเวลา ตั้งแต่แต่งนิยาย
            คิดคอนเทนต์โพสต์เฟสบุ๊กอัตโนมัติ ไปจนถึงสร้างสติกเกอร์ไลน์พร้อมขาย ในบัญชีเดียว
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
            <a
              href="#services"
              className="w-full sm:w-auto px-8 py-4 rounded-xl text-base font-semibold text-white bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:opacity-95 shadow-xl shadow-indigo-600/30 flex items-center justify-center gap-2 group transition-all duration-200 hover:scale-105"
            >
              <span>เลือกใช้งานบริการ AI</span>
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </a>
            <a
              href="#ecosystem"
              className="w-full sm:w-auto px-8 py-4 rounded-xl text-base font-semibold text-slate-200 bg-slate-900/80 hover:bg-slate-800 border border-slate-700/80 transition-all duration-200 flex items-center justify-center gap-2"
            >
              <span>ดูข้อมูลสถาปัตยกรรมระบบ</span>
            </a>
          </div>

          {/* Metrics Strip */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto pt-8 border-t border-slate-800/80">
            <div>
              <div className="text-3xl font-extrabold text-white font-['Plus_Jakarta_Sans']">
                3+
              </div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">
                ระบบ SaaS ในเครือ
              </div>
            </div>
            <div>
              <div className="text-3xl font-extrabold text-indigo-400 font-['Plus_Jakarta_Sans']">
                1 SSO
              </div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">
                ล็อกอินเดียวเข้าได้ทุกเว็บ
              </div>
            </div>
            <div>
              <div className="text-3xl font-extrabold text-purple-400 font-['Plus_Jakarta_Sans']">
                99.9%
              </div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">
                Uptime Cloud เสถียรสูง
              </div>
            </div>
            <div>
              <div className="text-3xl font-extrabold text-emerald-400 font-['Plus_Jakarta_Sans']">
                100%
              </div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">
                รองรับภาษาไทยสมบูรณ์
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Services Section ── */}
      <section id="services" className="py-20 relative bg-slate-950/40 border-t border-slate-800/60">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-indigo-400 text-xs sm:text-sm font-semibold tracking-wider uppercase mb-2 block">
              Flagship Products
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold text-white tracking-tight mb-4">
              บริการ AI ชั้นนำในเครือ ThaiD
            </h2>
            <p className="text-slate-400 text-base sm:text-lg">
              แต่ละบริการได้รับการพัฒนาแยกเป็นอิสระ เพื่อประสิทธิภาพสูงสุดและความแม่นยำเฉพาะทาง
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {services.map((srv) => {
              const Icon = srv.icon;
              return (
                <div
                  key={srv.id}
                  className={`group relative glass-panel rounded-3xl p-8 flex flex-col justify-between transition-all duration-300 hover:-translate-y-2 glow-card ${srv.glowColor}`}
                >
                  <div>
                    {/* Top Tag & Status */}
                    <div className="flex items-center justify-between gap-2 mb-6">
                      <span
                        className={`text-[11px] font-bold px-3 py-1 rounded-full text-white bg-gradient-to-r ${srv.badgeColor}`}
                      >
                        {srv.badge}
                      </span>
                      <span className="text-[11px] font-medium text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                        {srv.status}
                      </span>
                    </div>

                    {/* Icon & Name */}
                    <div className="flex items-center gap-4 mb-4">
                      <div
                        className={`w-14 h-14 rounded-2xl flex items-center justify-center border ${srv.accentBg}`}
                      >
                        <Icon className={`w-7 h-7 ${srv.iconColor}`} />
                      </div>
                      <div>
                        <h3 className="text-2xl font-bold text-white group-hover:text-indigo-300 transition-colors">
                          {srv.name}
                        </h3>
                        <span className="text-xs text-slate-400 font-mono">
                          {srv.subdomain}
                        </span>
                      </div>
                    </div>

                    <p className="text-sm font-medium text-slate-200 mb-3">
                      {srv.tagline}
                    </p>
                    <p className="text-xs sm:text-sm text-slate-400 leading-relaxed mb-6">
                      {srv.description}
                    </p>

                    {/* Feature bullet points */}
                    <div className="space-y-2.5 mb-8">
                      {srv.features.map((feat, idx) => (
                        <div key={idx} className="flex items-start gap-2 text-xs sm:text-sm text-slate-300">
                          <CheckCircle2 className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
                          <span>{feat}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Action Link Button */}
                  <a
                    href={srv.href}
                    className="w-full py-3.5 px-4 rounded-xl font-semibold text-sm text-center bg-slate-900 border border-slate-700/80 text-white hover:bg-indigo-600 hover:border-indigo-600 transition-all duration-200 flex items-center justify-center gap-2 group-hover:shadow-lg group-hover:shadow-indigo-600/20"
                  >
                    <span>เข้าสู่ {srv.name}</span>
                    <ExternalLink className="w-4 h-4" />
                  </a>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ── Unified Ecosystem Architecture ── */}
      <section id="ecosystem" className="py-20 relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-indigo-400 text-xs sm:text-sm font-semibold tracking-wider uppercase mb-2 block">
              Why ThaiD.online
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold text-white tracking-tight mb-4">
              สถาปัตยกรรมระบบที่ออกแบบเพื่ออนาคต
            </h2>
            <p className="text-slate-400 text-base sm:text-lg">
              เราแยกบริการออกจากกันอย่างชัดเจนบนระบบ Cloud เพื่อความเร็วและเสถียรภาพสูงสุด แต่ผูกโยงด้วยประสบการณ์ที่ไร้รอยต่อ
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="glass-panel p-6 rounded-2xl glow-card">
              <div className="w-12 h-12 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 mb-4">
                <ShieldCheck className="w-6 h-6" />
              </div>
              <h4 className="text-lg font-bold text-white mb-2">Single Sign-On (SSO)</h4>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                สมัครครั้งเดียวที่ `auth.thaid.online` แล้วสามารถเข้าถึงทุกโปรเจกต์ในเครือได้ทันทีด้วย Cookie ข้าม Subdomain
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl glow-card">
              <div className="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400 mb-4">
                <Coins className="w-6 h-6" />
              </div>
              <h4 className="text-lg font-bold text-white mb-2">Shared ThaiD Credits</h4>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                กระเป๋าเหรียญกลาง เติมเงินครั้งเดียวสามารถนำเครดิตไปใช้แต่งนิยาย ทำรูปเฟส หรือสร้างสติกเกอร์ไลน์ได้อย่างยืดหยุ่น
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl glow-card">
              <div className="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 mb-4">
                <Zap className="w-6 h-6" />
              </div>
              <h4 className="text-lg font-bold text-white mb-2">High-Speed Cloud</h4>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                เซิร์ฟเวอร์รันอยู่บน Oracle Cloud Ampere A1 (24GB RAM) เครือข่าย Fiber ในภูมิภาคเอเชีย โหลดไว ไม่หน่วง
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl glow-card">
              <div className="w-12 h-12 rounded-xl bg-pink-500/10 border border-pink-500/20 flex items-center justify-center text-pink-400 mb-4">
                <Layers className="w-6 h-6" />
              </div>
              <h4 className="text-lg font-bold text-white mb-2">Independent Scaling</h4>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                แต่ละบริการแยก Docker Container หากระบบใดมีผู้ใช้งานหนาแน่น จะไม่ส่งผลกระทบต่อบริการอื่นในเครือ
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ── Pricing Section ── */}
      <section id="pricing" className="py-20 bg-slate-950/60 border-t border-slate-800/60">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <span className="text-indigo-400 text-xs sm:text-sm font-semibold tracking-wider uppercase mb-2 block">
              Pricing Plans
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold text-white tracking-tight mb-4">
              แพ็กเกจราคาที่คุ้มค่า เริ่มต้นได้ทันที
            </h2>
            <p className="text-slate-400 text-base sm:text-lg">
              เลือกแพ็กเกจที่ตรงกับความต้องการของคุณ อัปเกรดหรือยกเลิกได้ตลอดเวลา
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {/* Free Plan */}
            <div className="glass-panel rounded-3xl p-8 flex flex-col justify-between glow-card">
              <div>
                <h3 className="text-xl font-bold text-white mb-1">Starter</h3>
                <p className="text-xs text-slate-400 mb-6">สำหรับผู้เริ่มต้นทดลองใช้ระบบ</p>
                <div className="flex items-baseline gap-1 mb-6">
                  <span className="text-4xl font-extrabold text-white">฿0</span>
                  <span className="text-xs text-slate-400">/ ตลอดชีพ</span>
                </div>
                <div className="space-y-3 mb-8 text-sm text-slate-300">
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>50 เครดิตทดลองฟรีทุกระบบ</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>แต่งนิยายได้สูงสุด 3 เรื่อง</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>ตั้งเวลาโพสต์ Facebook 5 โพสต์/วัน</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>สร้างสติกเกอร์ไลน์ 1 ชุด (8 รูป)</span>
                  </div>
                </div>
              </div>
              <a
                href="https://auth.thaid.online/register"
                className="w-full py-3 rounded-xl font-semibold text-sm text-center bg-slate-900 border border-slate-700 text-slate-200 hover:text-white hover:bg-slate-800 transition-colors"
              >
                สมัครใช้งานฟรี
              </a>
            </div>

            {/* Pro Plan */}
            <div className="glass-panel rounded-3xl p-8 flex flex-col justify-between relative border-indigo-500/50 glow-primary bg-gradient-to-b from-indigo-950/40 to-slate-950/80">
              <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 text-[11px] font-bold text-white uppercase tracking-wider shadow-md">
                ยอดนิยม 🔥
              </div>
              <div>
                <h3 className="text-xl font-bold text-white mb-1">Creator Pro</h3>
                <p className="text-xs text-indigo-300 mb-6">สำหรับนักเขียน ครีเอเตอร์ และร้านค้า</p>
                <div className="flex items-baseline gap-1 mb-6">
                  <span className="text-4xl font-extrabold text-white">฿390</span>
                  <span className="text-xs text-slate-400">/ เดือน</span>
                </div>
                <div className="space-y-3 mb-8 text-sm text-slate-200">
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>1,500 เครดิต AI รายเดือน</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>แต่งนิยายไม่จำกัดเรื่อง + สร้างภาพปก AI ไม่จำกัด</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>ตั้งเวลาโพสต์ Facebook อัตโนมัติ 5 เพจ</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>สร้างสติกเกอร์ไลน์ 40 ท่าทาง พร้อมไฟล์ ZIP</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>ความเร็วในการประมวลผลระดับ VIP Fast-lane</span>
                  </div>
                </div>
              </div>
              <a
                href="https://auth.thaid.online/register"
                className="w-full py-3 rounded-xl font-semibold text-sm text-center bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 hover:opacity-95 transition-opacity"
              >
                เริ่มต้นใช้งาน Pro
              </a>
            </div>

            {/* Enterprise Plan */}
            <div className="glass-panel rounded-3xl p-8 flex flex-col justify-between glow-card">
              <div>
                <h3 className="text-xl font-bold text-white mb-1">Business & Agency</h3>
                <p className="text-xs text-slate-400 mb-6">สำหรับธุรกิจ สำนักพิมพ์ และเอเจนซี่</p>
                <div className="flex items-baseline gap-1 mb-6">
                  <span className="text-4xl font-extrabold text-white">฿1,290</span>
                  <span className="text-xs text-slate-400">/ เดือน</span>
                </div>
                <div className="space-y-3 mb-8 text-sm text-slate-300">
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>6,000 เครดิต AI พร้อมแชร์ในทีม</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>ไม่จำกัดเพจ Facebook และทีมงานร่วมจัดการ</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>ระบบ API Access สำหรับเชื่อมต่อระบบภายนอก</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>บริการลูกค้าแบบ Priority 1-on-1 Support</span>
                  </div>
                </div>
              </div>
              <a
                href="mailto:contact@thaid.online"
                className="w-full py-3 rounded-xl font-semibold text-sm text-center bg-slate-900 border border-slate-700 text-slate-200 hover:text-white hover:bg-slate-800 transition-colors"
              >
                ติดต่อทีมงาน
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* ── FAQ Section ── */}
      <section id="faq" className="py-20 relative">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <span className="text-indigo-400 text-xs sm:text-sm font-semibold tracking-wider uppercase mb-2 block">
              Got Questions?
            </span>
            <h2 className="text-3xl sm:text-4xl font-bold text-white tracking-tight mb-4">
              คำถามที่พบบ่อย (FAQ)
            </h2>
            <p className="text-slate-400 text-sm sm:text-base">
              คำตอบสำหรับทุกข้อสงสัยเกี่ยวกับการใช้งานแพลตฟอร์ม ThaiD.online
            </p>
          </div>

          <div className="space-y-4">
            {faqs.map((faq, index) => (
              <div
                key={index}
                className="glass-panel rounded-2xl overflow-hidden border border-slate-800/80 transition-all duration-200"
              >
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full px-6 py-5 text-left flex items-center justify-between gap-4 font-semibold text-white hover:text-indigo-300 transition-colors"
                >
                  <span className="text-sm sm:text-base">{faq.q}</span>
                  <ChevronDown
                    className={`w-5 h-5 text-slate-400 shrink-0 transition-transform duration-200 ${
                      faqOpen === index ? "rotate-180 text-indigo-400" : ""
                    }`}
                  />
                </button>
                {faqOpen === index && (
                  <div className="px-6 pb-5 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-slate-800/50 pt-4">
                    {faq.a}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Call To Action Banner ── */}
      <section className="py-16 relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="relative rounded-3xl overflow-hidden bg-gradient-to-r from-indigo-900/80 via-purple-900/80 to-pink-900/80 border border-indigo-500/30 p-8 sm:p-14 text-center glow-primary">
            <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight mb-4">
              พร้อมเริ่มต้นสร้างสรรค์ผลงานด้วย AI แล้วหรือยัง?
            </h2>
            <p className="max-w-2xl mx-auto text-sm sm:text-base text-indigo-100 font-light mb-8">
              สมัครสมาชิกวันนี้ รับเครดิตทดลองใช้ฟรีทันทีในทุกเครื่องมือ บัญชีเดียวใช้งานได้ทั้งระบบ
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="https://auth.thaid.online/register"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-bold text-slate-900 bg-white hover:bg-slate-100 shadow-xl transition-all duration-200 hover:scale-105"
              >
                สมัครสมาชิกฟรีทันที
              </a>
              <a
                href="#services"
                className="w-full sm:w-auto px-8 py-3.5 rounded-xl font-semibold text-white border border-white/30 hover:bg-white/10 transition-colors"
              >
                ทดลองดูฟีเจอร์เด่น
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="bg-[#05070a] border-t border-slate-800/80 py-12 text-slate-400 text-xs sm:text-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
            {/* Col 1 */}
            <div className="md:col-span-1">
              <div className="flex items-center gap-2 mb-3">
                <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-white text-sm">
                  TD
                </div>
                <span className="font-bold text-lg text-white">ThaiD.online</span>
              </div>
              <p className="text-xs text-slate-400 leading-relaxed mb-4">
                แพลตฟอร์ม SaaS อัจฉริยะเพื่อคนไทย สร้างสรรค์นิยาย คอนเทนต์โซเชียล และสติกเกอร์ไลน์ด้วยพลัง AI
              </p>
              <p className="text-[11px] text-slate-400">
                &copy; 2026 ThaiD Platform. All rights reserved.
              </p>
            </div>

            {/* Col 2 */}
            <div>
              <h4 className="font-bold text-white mb-3 text-sm">บริการในเครือ</h4>
              <ul className="space-y-2 text-xs">
                <li>
                  <a href="https://novel.thaid.online" className="hover:text-indigo-400 transition-colors">
                    ThaiD Novel Studio (แต่งนิยาย)
                  </a>
                </li>
                <li>
                  <a href="https://social.thaid.online" className="hover:text-indigo-400 transition-colors">
                    ThaiD Social Auto-Post (โพสต์ FB)
                  </a>
                </li>
                <li>
                  <a href="https://sticker.thaid.online" className="hover:text-indigo-400 transition-colors">
                    ThaiD Sticker Studio (สติกเกอร์ไลน์)
                  </a>
                </li>
                <li>
                  <a href="https://auth.thaid.online" className="hover:text-indigo-400 transition-colors">
                    ThaiD Account SSO (บัญชีกลาง)
                  </a>
                </li>
              </ul>
            </div>

            {/* Col 3 */}
            <div>
              <h4 className="font-bold text-white mb-3 text-sm">ทรัพยากร & บทความ</h4>
              <ul className="space-y-2 text-xs">
                <li>
                  <a href="#faq" className="hover:text-indigo-400 transition-colors">
                    คำถามที่พบบ่อย (FAQ)
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    คู่มือการใช้งาน (Documentation)
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    แนวทางการส่งสติกเกอร์ LINE
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    สถานะเซิร์ฟเวอร์ (System Status)
                  </a>
                </li>
              </ul>
            </div>

            {/* Col 4 */}
            <div>
              <h4 className="font-bold text-white mb-3 text-sm">กฎหมายและนโยบาย</h4>
              <ul className="space-y-2 text-xs">
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    นโยบายความเป็นส่วนตัว (Privacy Policy)
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    ข้อกำหนดการใช้งาน (Terms of Service)
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-indigo-400 transition-colors">
                    นโยบายการใช้คุกกี้ (Cookie Policy)
                  </a>
                </li>
                <li>
                  <a href="mailto:contact@thaid.online" className="hover:text-indigo-400 transition-colors">
                    ติดต่อทีมงาน (contact@thaid.online)
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div className="pt-8 border-t border-slate-900 text-center text-xs text-slate-400">
            ThaiD.online เป็นแพลตฟอร์มอิสระและไม่มีความเกี่ยวข้องโดยตรงกับ LINE Corporation หรือ Meta Platforms, Inc.
          </div>
        </div>
      </footer>
    </div>
  );
}
