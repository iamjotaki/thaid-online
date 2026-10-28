import os

path = r'C:\ThaiD.online\app\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state in HomePage
old_state = '''export default function HomePage() {
  const [activeTab, setActiveTab] = useState<string>("all");
  const [countdown, setCountdown] = useState({ days: 19, hours: 18, mins: 30, secs: 49 });'''

new_state = '''export default function HomePage() {
  const [activeTab, setActiveTab] = useState<string>("all");
  const [countdown, setCountdown] = useState({ days: 19, hours: 18, mins: 30, secs: 49 });
  const [saasMenuOpen, setSaasMenuOpen] = useState(false);
  const [profileMenuOpen, setProfileMenuOpen] = useState(false);
  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [user, setUser] = useState<{ name: string; email: string; avatar: string } | null>(null);

  const saasMenuRef = useRef<HTMLDivElement | null>(null);
  const profileMenuRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const saved = localStorage.getItem("thaid_user");
    if (saved) {
      try {
        setUser(JSON.parse(saved));
      } catch (e) {}
    }

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

  const handleLogin = (name: string, email: string, avatar: string) => {
    const u = { name, email, avatar };
    setUser(u);
    localStorage.setItem("thaid_user", JSON.stringify(u));
    setAuthModalOpen(false);
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem("thaid_user");
    setProfileMenuOpen(false);
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
      name: "Personal Vault",
      sub: "คลังเก็บรหัสผ่าน & API Keys ส่วนตัว",
      url: "https://vault.thaid.online",
      tag: "vault.thaid.online",
      badge: "AES-256",
      icon: (
        <svg className="w-4 h-4 text-amber-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
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
  ];'''

content = content.replace(old_state, new_state, 1)

# 2. Replace Header
old_header = '''      {/* ======================================================== */}
      {/* 1. THAID FLOATING TOP NAVBAR                              */}
      {/* ======================================================== */}
      <header className="fixed top-0 inset-x-0 z-50 pt-4 px-4 sm:px-6 pointer-events-none">
        <div className="max-w-5xl mx-auto flex items-center justify-between pointer-events-auto bg-white/70 backdrop-blur-xl border border-black/[0.08] shadow-[0_4px_24px_rgba(0,0,0,0.04)] rounded-full px-5 py-2.5">
          
          {/* Left: Brand Logo + ThaiD */}
          <a href="https://thaid.online" className="flex items-center gap-2.5 text-[#2b313b] hover:opacity-85 transition-opacity">
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

          {/* Right: Language Switcher (No Vault button) */}
          <div className="flex items-center">
            <button
              type="button"
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/80 hover:bg-white text-xs font-semibold text-[#2b313b] transition-colors shadow-2xs cursor-pointer"
            >
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="1.8" className="text-[#2b313b]">
                <circle cx="12" cy="12" r="8.5" />
                <path d="M3.8 12h16.4M12 3.5c2.3 2.3 3.5 5.1 3.5 8.5S14.3 18.2 12 20.5M12 3.5C9.7 5.8 8.5 8.6 8.5 12s1.2 6.2 3.5 8.5" />
              </svg>
              <span>TH</span>
              <svg width="10" height="10" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2.2">
                <path d="m4.5 6 3.5 3.5L11.5 6" />
              </svg>
            </button>
          </div>

        </div>
      </header>'''

new_header = '''      {/* ======================================================== */}
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

          {/* Zone 2: Center - SaaS Services Selector Dropdown */}
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
              <div className="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-72 sm:w-80 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-2 z-50 animate-in fade-in zoom-in-95 duration-150">
                <div className="px-3 py-1.5 text-[10px] font-bold text-stone-400 uppercase tracking-wider border-b border-black/[0.05] mb-1 flex items-center justify-between">
                  <span>ThaiD SaaS Ecosystem</span>
                  <span className="text-emerald-600 font-semibold">7 เครื่องมือ</span>
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

          {/* Zone 3: Right - Link to Sub Home + Far Right Login / Profile */}
          <div className="flex items-center gap-2 flex-shrink-0">
            {/* Link to Sub / Services Home */}
            <a
              href="#services-directory"
              className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/80 hover:bg-white text-xs font-semibold text-[#2b313b] transition-colors shadow-2xs"
            >
              <span>หน้าแรกบริการ</span>
            </a>

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
                      <a
                        href="https://vault.thaid.online"
                        className="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors"
                      >
                        <span>ไปที่ Security Vault</span>
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
      </header>'''

content = content.replace(old_header, new_header, 1)

# 3. Add Login Modal before </div>\n  );\n}
old_footer = '''      </footer>

    </div>
  );
}'''

new_modal = '''      </footer>

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
}'''

content = content.replace(old_footer, new_modal, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app/page.tsx successfully!")
