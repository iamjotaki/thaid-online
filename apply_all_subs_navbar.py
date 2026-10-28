import os
import re

def generate_header_html(sub_title, sub_home_url, sub_home_label):
    return f'''  <!-- ======================================================== -->
  <!-- 1. THAID FLOATING TOP NAVBAR (MASTER TEMPLATE 3-ZONE)    -->
  <!-- ======================================================== -->
  <header class="fixed top-0 inset-x-0 z-50 pt-4 px-4 sm:px-6 pointer-events-none">
    <div class="max-w-5xl mx-auto flex items-center justify-between pointer-events-auto bg-white/80 backdrop-blur-xl border border-black/[0.08] shadow-[0_4px_24px_rgba(0,0,0,0.04)] rounded-full px-4 sm:px-5 py-2.5 relative">
      
      <!-- Zone 1: Left - Brand Logo + ThaiD -->
      <a href="https://thaid.online" class="flex items-center gap-2.5 text-[#2b313b] hover:opacity-85 transition-opacity group flex-shrink-0">
        <div class="w-7 h-7 rounded-lg bg-[#2b313b] flex items-center justify-center text-white shadow-xs group-hover:scale-105 transition-transform">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 6.5H15M9.5 6.5V19" stroke="white" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="flex items-center gap-1.5">
          <span class="font-bold text-xl tracking-tight text-[#2b313b]">ThaiD</span>
          <span class="text-xs text-stone-300 font-light">/</span>
          <span class="text-xs font-semibold text-[#5e6675]">{sub_title}</span>
        </div>
      </a>

      <!-- Zone 2: Center - SaaS Services Selector Dropdown -->
      <div class="relative" id="thaidSaasDropdownWrap">
        <button
          type="button"
          onclick="toggleThaiDSaasMenu()"
          class="inline-flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-full border border-black/[0.08] bg-white/90 hover:bg-white text-xs font-semibold text-[#2b313b] transition-all shadow-2xs hover:border-black/[0.2] cursor-pointer"
        >
          <span class="text-[#0569ff] font-bold text-xs">✦</span>
          <span>เลือกบริการ SaaS</span>
          <svg id="thaidSaasChevron" width="10" height="10" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.2" class="text-stone-400 transition-transform duration-200">
            <path d="m4.5 6 3.5 3.5L11.5 6" />
          </svg>
        </button>

        <!-- Dropdown Menu -->
        <div id="thaidSaasMenu" class="hidden absolute left-1/2 -translate-x-1/2 top-full mt-2 w-72 sm:w-80 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-2 z-50 text-left">
          <div class="px-3 py-1.5 text-[10px] font-bold text-stone-400 uppercase tracking-wider border-b border-black/[0.05] mb-1 flex items-center justify-between">
            <span>ThaiD SaaS Ecosystem</span>
            <span class="text-emerald-600 font-semibold">7 เครื่องมือ</span>
          </div>
          <div class="grid grid-cols-1 gap-1 max-h-[380px] overflow-y-auto">
            <a href="https://novel.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-[#0569ff]">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Novel Studio</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">แต่งนิยาย AI 10 ตอนจบ</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">10 ตอนจบ</span>
            </a>
            <a href="https://social.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-emerald-600">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Social Auto-Poster</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">ดึงข่าว RSS & โพสต์ Facebook 24 ชม.</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">Auto 24h</span>
            </a>
            <a href="https://vault.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-amber-500">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Personal Vault</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">คลังเก็บรหัสผ่าน & API Keys ส่วนตัว</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">AES-256</span>
            </a>
            <a href="https://sticker.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-pink-500">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">LINE Sticker Creator</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">สร้างชุดสติกเกอร์ไลน์ 40 แอ็กชัน</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">40 แอ็กชัน</span>
            </a>
            <a href="https://clip.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-purple-500">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Clip AI & Reels</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">สคริปต์คลิปสั้น 9:16 สไตล์ไวรัล</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">9:16 Shorts</span>
            </a>
            <a href="https://chat.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-teal-600">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Smart Chat AI</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">บอทแอดมินตอบแชทบน LINE OA 24/7</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">ตอบ 0.8 วิ</span>
            </a>
            <a href="https://mockup.thaid.online" class="flex items-center justify-between p-2 rounded-xl hover:bg-stone-50 transition-colors group text-left">
              <div class="flex items-center gap-2.5">
                <div class="w-7 h-7 rounded-lg bg-stone-100 flex items-center justify-center group-hover:scale-105 transition-transform flex-shrink-0 text-blue-500">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                </div>
                <div class="text-left">
                  <div class="text-xs font-bold text-[#171717] group-hover:text-[#0569ff] transition-colors">Mockup Studio</div>
                  <div class="text-[10px] text-stone-400 truncate max-w-[170px]">สตูดิโอภาพถ่ายสินค้าลักชัวรี ไดคัต AI</div>
                </div>
              </div>
              <span class="text-[10px] px-1.5 py-0.5 rounded bg-stone-100 text-stone-500 font-medium">Studio 4K</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Zone 3: Right - Sub Home Link & Far Right Login/Profile -->
      <div class="flex items-center gap-2 flex-shrink-0">
        <!-- Sub Home Link -->
        <a href="{sub_home_url}" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border border-black/[0.08] bg-white/80 hover:bg-white text-xs font-semibold text-[#2b313b] transition-colors shadow-2xs">
          <span>{sub_home_label}</span>
        </a>

        <!-- Far Right Login Pill (Guest) -->
        <button id="thaidLoginBtn" type="button" onclick="openThaiDAuthModal()" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-[#171717] hover:bg-black text-white text-xs font-semibold shadow-2xs transition-all hover:scale-[1.02] active:scale-[0.98] cursor-pointer">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.4">
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M15 12H3" />
          </svg>
          <span>เข้าสู่ระบบ</span>
        </button>

        <!-- Far Right Profile Pill (Logged-in) -->
        <div id="thaidProfileWrap" class="hidden relative">
          <button id="thaidProfileBtn" type="button" onclick="toggleThaiDProfileMenu()" class="flex items-center gap-1.5 p-1 pl-1 pr-2.5 rounded-full border border-black/[0.08] hover:border-[#0569ff] transition-all bg-white shadow-2xs cursor-pointer group">
            <img id="thaidUserAvatar" src="" alt="User" class="w-6 h-6 rounded-full object-cover bg-stone-100 ring-1 ring-black/[0.06]" />
            <span id="thaidUserName" class="text-xs font-semibold text-[#2b313b] hidden md:inline max-w-[80px] truncate"></span>
            <svg id="thaidProfileChevron" width="10" height="10" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.2" class="text-stone-400 group-hover:text-[#171717] transition-transform duration-200">
              <path d="m4.5 6 3.5 3.5L11.5 6" />
            </svg>
          </button>

          <!-- Profile Dropdown -->
          <div id="thaidProfileMenu" class="hidden absolute right-0 top-full mt-2 w-64 bg-white/95 backdrop-blur-2xl border border-black/[0.08] rounded-2xl shadow-2xl p-3 z-50 text-left">
            <div class="flex items-center gap-2.5 pb-2.5 border-b border-black/[0.06]">
              <img id="thaidUserAvatarLarge" src="" alt="User" class="w-10 h-10 rounded-full object-cover bg-stone-100 ring-1 ring-black/[0.08]" />
              <div class="flex-1 min-w-0">
                <div id="thaidUserNameLarge" class="text-xs font-bold text-[#171717] truncate"></div>
                <div id="thaidUserEmailLarge" class="text-[10px] text-stone-400 truncate"></div>
              </div>
            </div>
            <div class="py-2 text-[11px] space-y-1">
              <div class="flex items-center justify-between px-2 py-1 rounded-lg bg-stone-50">
                <span class="text-stone-500">สถานะสมาชิก:</span>
                <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-bold text-[10px]">Active Pro</span>
              </div>
              <a href="https://thaid.online" class="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors">
                <span>หน้าหลัก ThaiD Hub</span>
                <span class="text-[10px] text-stone-400">→</span>
              </a>
              <a href="https://novel.thaid.online" class="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors">
                <span>ไปที่ Novel Studio</span>
                <span class="text-[10px] text-stone-400">→</span>
              </a>
              <a href="https://social.thaid.online" class="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors">
                <span>ไปที่ Social Dashboard</span>
                <span class="text-[10px] text-stone-400">→</span>
              </a>
              <a href="https://vault.thaid.online" class="flex items-center justify-between px-2 py-1.5 rounded-lg hover:bg-stone-50 text-stone-700 text-xs transition-colors">
                <span>ไปที่ Security Vault</span>
                <span class="text-[10px] text-stone-400">→</span>
              </a>
            </div>
            <button type="button" onclick="thaiDLogout()" class="w-full mt-1 pt-2 border-t border-black/[0.06] text-left text-xs font-semibold text-rose-600 hover:text-rose-700 flex items-center justify-between px-2 py-1 rounded-lg hover:bg-rose-50/50 cursor-pointer transition-colors">
              <span>ออกจากระบบ</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>
              </svg>
            </button>
          </div>
        </div>

      </div>

    </div>
  </header>'''

def generate_modal_and_script():
    return '''  <!-- ==================== THAID UNIFIED AUTH MODAL ==================== -->
  <div id="thaidAuthModal" class="hidden fixed inset-0 z-50 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border border-black/[0.08] text-center space-y-5 relative">
      <button onclick="closeThaiDAuthModal()" class="absolute top-4 right-4 text-stone-400 hover:text-[#171717] p-1 cursor-pointer">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      </button>

      <div class="space-y-1 pt-2">
        <div class="w-10 h-10 rounded-2xl bg-[#2b313b] text-white flex items-center justify-center mx-auto shadow-sm">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 6.5H15M9.5 6.5V19" stroke="white" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M14 10.5C14 10.5 18 10.8 18 14.5C18 18.2 14 18.5 14 18.5" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
          </svg>
        </div>
        <h3 class="text-base font-bold text-[#171717]">เข้าสู่ระบบ ThaiD</h3>
        <p class="text-xs text-stone-500">เข้าถึงทุกบริการ SaaS ใน ThaiD Ecosystem ด้วยบัญชีเดียว</p>
      </div>

      <!-- Quick Demo Logins -->
      <div class="space-y-2 pt-2">
        <button
          type="button"
          onclick="thaiDLogin('Admin Boss', 'boss@thaid.online', 'https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss')"
          class="w-full flex items-center justify-between p-2.5 rounded-2xl border border-black/[0.08] hover:border-black/[0.2] bg-stone-50 hover:bg-stone-100 transition-all text-left cursor-pointer"
        >
          <div class="flex items-center gap-2.5">
            <img src="https://api.dicebear.com/7.x/bottts/svg?seed=AdminBoss" class="w-8 h-8 rounded-full bg-white shadow-2xs" alt="Admin" />
            <div>
              <div class="text-xs font-bold text-[#171717]">Admin Boss (Superadmin)</div>
              <div class="text-[10px] text-stone-400">boss@thaid.online · VIP Enterprise</div>
            </div>
          </div>
          <span class="text-[11px] font-semibold text-[#0569ff]">เข้าทันที →</span>
        </button>

        <button
          type="button"
          onclick="thaiDLogin('รดา นิยายรัก', 'rada@thaid.online', 'https://api.dicebear.com/7.x/avataaars/svg?seed=RadaAuthor')"
          class="w-full flex items-center justify-between p-2.5 rounded-2xl border border-black/[0.08] hover:border-black/[0.2] bg-stone-50 hover:bg-stone-100 transition-all text-left cursor-pointer"
        >
          <div class="flex items-center gap-2.5">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=RadaAuthor" class="w-8 h-8 rounded-full bg-white shadow-2xs" alt="Author" />
            <div>
              <div class="text-xs font-bold text-[#171717]">รดา นิยายรัก (Creator)</div>
              <div class="text-[10px] text-stone-400">rada@thaid.online · Pro Creator</div>
            </div>
          </div>
          <span class="text-[11px] font-semibold text-[#0569ff]">เข้าทันที →</span>
        </button>
      </div>

      <div class="relative py-1">
        <div class="absolute inset-0 flex items-center"><div class="w-full border-t border-black/[0.08]"></div></div>
        <div class="relative flex justify-center text-[10px] uppercase text-stone-400"><span class="bg-white px-2">หรือเข้าด้วยอีเมล</span></div>
      </div>

      <!-- Email input -->
      <form onsubmit="handleThaiDEmailLogin(event)" class="space-y-2">
        <input
          id="thaidEmailInput"
          type="email"
          placeholder="your.email@example.com"
          required
          class="w-full px-3 py-2 text-xs rounded-xl border border-black/[0.1] focus:outline-none focus:border-[#0569ff]"
        />
        <button
          type="submit"
          class="w-full py-2.5 rounded-full bg-[#171717] hover:bg-black text-white text-xs font-semibold shadow-xs transition-all cursor-pointer"
        >
          เข้าสู่ระบบด้วยอีเมล
        </button>
      </form>
    </div>
  </div>

  <script>
    function toggleThaiDSaasMenu() {
      const menu = document.getElementById('thaidSaasMenu');
      const chev = document.getElementById('thaidSaasChevron');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {
        menu.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      } else {
        menu.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      }
    }

    function toggleThaiDProfileMenu() {
      const menu = document.getElementById('thaidProfileMenu');
      const chev = document.getElementById('thaidProfileChevron');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {
        menu.classList.remove('hidden');
        if (chev) chev.classList.add('rotate-180');
      } else {
        menu.classList.add('hidden');
        if (chev) chev.classList.remove('rotate-180');
      }
    }

    function openThaiDAuthModal() {
      const modal = document.getElementById('thaidAuthModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeThaiDAuthModal() {
      const modal = document.getElementById('thaidAuthModal');
      if (modal) modal.classList.add('hidden');
    }

    function thaiDLogin(name, email, avatar) {
      const user = { name, email, avatar };
      localStorage.setItem('thaid_user', JSON.stringify(user));
      syncThaiDUserState();
      closeThaiDAuthModal();
    }

    function handleThaiDEmailLogin(e) {
      e.preventDefault();
      const input = document.getElementById('thaidEmailInput');
      const val = input ? input.value.trim() : '';
      if (val) {
        const name = val.split('@')[0];
        thaiDLogin(name, val, 'https://api.dicebear.com/7.x/avataaars/svg?seed=' + encodeURIComponent(name));
      }
    }

    function thaiDLogout() {
      localStorage.removeItem('thaid_user');
      syncThaiDUserState();
      const pMenu = document.getElementById('thaidProfileMenu');
      if (pMenu) pMenu.classList.add('hidden');
    }

    function syncThaiDUserState() {
      const loginBtn = document.getElementById('thaidLoginBtn');
      const profWrap = document.getElementById('thaidProfileWrap');
      const raw = localStorage.getItem('thaid_user');
      if (raw) {
        try {
          const user = JSON.parse(raw);
          if (loginBtn) loginBtn.classList.add('hidden');
          if (profWrap) {
            profWrap.classList.remove('hidden');
            const av = document.getElementById('thaidUserAvatar');
            const nm = document.getElementById('thaidUserName');
            const avL = document.getElementById('thaidUserAvatarLarge');
            const nmL = document.getElementById('thaidUserNameLarge');
            const emL = document.getElementById('thaidUserEmailLarge');
            if (av) av.src = user.avatar || '';
            if (nm) nm.textContent = user.name || '';
            if (avL) avL.src = user.avatar || '';
            if (nmL) nmL.textContent = user.name || '';
            if (emL) emL.textContent = user.email || '';
          }
          return;
        } catch(e) {}
      }
      if (loginBtn) loginBtn.classList.remove('hidden');
      if (profWrap) profWrap.classList.add('hidden');
    }

    document.addEventListener('click', function(e) {
      const saasWrap = document.getElementById('thaidSaasDropdownWrap');
      const saasMenu = document.getElementById('thaidSaasMenu');
      const saasChev = document.getElementById('thaidSaasChevron');
      if (saasWrap && saasMenu && !saasWrap.contains(e.target)) {
        saasMenu.classList.add('hidden');
        if (saasChev) saasChev.classList.remove('rotate-180');
      }

      const profWrap = document.getElementById('thaidProfileWrap');
      const profMenu = document.getElementById('thaidProfileMenu');
      const profChev = document.getElementById('thaidProfileChevron');
      if (profWrap && profMenu && !profWrap.contains(e.target)) {
        profMenu.classList.add('hidden');
        if (profChev) profChev.classList.remove('rotate-180');
      }
    });

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', syncThaiDUserState);
    } else {
      syncThaiDUserState();
    }
  </script>
'''

def update_file(file_path, sub_title, sub_home_url, sub_home_label):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace header
    h_start = content.find('<header')
    h_end = content.find('</header>')
    if h_start == -1 or h_end == -1:
        print(f"Header not found in {file_path}")
        return False

    new_header = generate_header_html(sub_title, sub_home_url, sub_home_label)
    content = content[:h_start] + new_header + content[h_end+9:]

    # 2. Clean old thaidAuthModal if present
    old_modal_idx = content.find('<!-- ==================== THAID UNIFIED AUTH MODAL ==================== -->')
    if old_modal_idx != -1:
        # cut from here to </body>
        b_idx = content.find('</body>')
        if b_idx != -1:
            content = content[:old_modal_idx] + content[b_idx:]

    # 3. Inject modal and script before </body>
    b_idx = content.find('</body>')
    if b_idx != -1:
        content = content[:b_idx] + generate_modal_and_script() + '\n' + content[b_idx:]
    else:
        content = content + '\n' + generate_modal_and_script()

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path} successfully!")
    return True

CONFIGS = [
    (r"C:\ThaiD-Mockup\static\index.html", "Mockup AI", "https://mockup.thaid.online", "หน้าแรก Mockup"),
    (r"C:\ThaiD-Clip\static\index.html", "Clip AI", "https://clip.thaid.online", "หน้าแรก Clip AI"),
    (r"C:\ThaiD-Chat\static\index.html", "Smart Chat", "https://chat.thaid.online", "หน้าแรก Chat"),
    (r"C:\ThaiD-Sticker\static\index.html", "LINE Sticker", "https://sticker.thaid.online", "หน้าแรก Sticker"),
    (r"C:\ThaiD-Vault\static\index.html", "Security Vault", "https://vault.thaid.online", "หน้าแรก Vault"),
    (r"C:\ReadAWrite\web_saas_stitch\index.html", "Novel Studio", "https://novel.thaid.online", "หน้าแรก Novel"),
    (r"C:\Auto Post FB\templates\landing.html", "Social Poster", "https://social.thaid.online", "หน้าแรก Social"),
]

for fp, title, url, label in CONFIGS:
    update_file(fp, title, url, label)
