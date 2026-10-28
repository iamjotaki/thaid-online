import os
import re

# 1. Update app.py to add brute-force protection
app_path = r'C:\ThaiD-Vault\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    app_code = f.read()

# Add failed_attempts dict and Request import
if 'from fastapi import' in app_code and 'Request' not in app_code:
    app_code = app_code.replace('from fastapi import FastAPI', 'from fastapi import FastAPI, Request')

if 'failed_attempts: Dict[str, list] = {}' not in app_code:
    app_code = app_code.replace(
        'active_sessions: Dict[str, datetime] = {}',
        'active_sessions: Dict[str, datetime] = {}\nfailed_attempts: Dict[str, list] = {}  # ip -> list of timestamps'
    )

old_verify = '''@app.post("/api/auth/verify-pin")
def verify_pin(data: VerifyPinRequest):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = 'master_pin_salt'")
    salt = cursor.fetchone()["value"]
    cursor.execute("SELECT value FROM settings WHERE key = 'master_pin_hash'")
    stored_hash = cursor.fetchone()["value"]
    conn.close()

    if hash_pin(data.pin, salt) != stored_hash:
        raise HTTPException(status_code=400, detail="รหัส PIN ไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

    token = secrets.token_hex(24)
    active_sessions[token] = datetime.now() + timedelta(minutes=30)
    return {"token": token, "message": "ปลดล็อกสำเร็จ"}'''

new_verify = '''@app.post("/api/auth/verify-pin")
def verify_pin(data: VerifyPinRequest, request: Request):
    import time
    client_ip = request.client.host if request.client else "unknown"
    now = datetime.now()

    # Brute-force protection: check failed attempts in last 10 minutes
    attempts = failed_attempts.get(client_ip, [])
    attempts = [t for t in attempts if now - t < timedelta(minutes=10)]
    failed_attempts[client_ip] = attempts

    if len(attempts) >= 5:
        raise HTTPException(status_code=429, detail="คุณใส่รหัสผิดเกิน 5 ครั้ง ระบบถูกล็อกชั่วคราวเป็นเวลา 15 นาที เพื่อความปลอดภัยสูงสุด")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM settings WHERE key = 'master_pin_salt'")
    salt = cursor.fetchone()["value"]
    cursor.execute("SELECT value FROM settings WHERE key = 'master_pin_hash'")
    stored_hash = cursor.fetchone()["value"]
    conn.close()

    if hash_pin(data.pin, salt) != stored_hash:
        # Record failed attempt and sleep 1s to slow down brute force
        failed_attempts[client_ip].append(now)
        time.sleep(1)
        remaining = 5 - len(failed_attempts[client_ip])
        raise HTTPException(status_code=400, detail=f"รหัส PIN ไม่ถูกต้อง (เหลือโอกาส {max(0, remaining)} ครั้งก่อนระบบล็อก)")

    # Successful login: reset failed attempts
    failed_attempts[client_ip] = []
    token = secrets.token_hex(24)
    active_sessions[token] = datetime.now() + timedelta(minutes=60)
    return {"token": token, "message": "ปลดล็อกสำเร็จ"}'''

app_code = app_code.replace(old_verify, new_verify)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(app_code)
print("Updated app.py with brute-force protection!")

# 2. Update static/index.html to remove demo bypass button and placeholder hint
html_path = r'C:\ThaiD-Vault\static\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_code = f.read()

# Replace placeholder
html_code = html_code.replace(
    'placeholder="ป้อนรหัส PIN (เริ่มต้น: 2026)"',
    'placeholder="ป้อนรหัส PIN ส่วนตัว"'
)

# Remove quick demo unlock button and starting PIN text
demo_btn_pattern = r'<button type="button" onclick="document\.getElementById\(\'pinInput\'\)\.value=\'2026\'; submitPin[\s\S]*?</button>\s*'
html_code = re.sub(demo_btn_pattern, '', html_code)

hint_pattern = r'<p class="text-\[11px\] text-stone-400">PIN เริ่มต้นระบบ:[\s\S]*?</p>\s*'
html_code = re.sub(hint_pattern, '', html_code)

# Remove SaaS dropdown from ThaiD-Vault header (make it private)
saas_dropdown_pattern = r'<div class="relative" id="thaidSaasDropdownWrap">[\s\S]*?</div>\s*<!-- Zone 3'
html_code = re.sub(saas_dropdown_pattern, '<!-- Zone 3', html_code)

# Update left title in header to show Private
html_code = html_code.replace(
    '<span class="text-xs font-semibold text-[#5e6675]">Security Vault</span>',
    '<span class="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Personal Private Vault 🔒</span>'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_code)
print("Updated ThaiD-Vault static/index.html: removed demo buttons and made private!")
