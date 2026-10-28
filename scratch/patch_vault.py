import os

path = r"C:\ThaiD-Vault\app.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """@app.get("/", response_class=HTMLResponse)
def index():
    html_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h3>ThaiD Vault Loading...</h3>")"""

replacement = """@app.get("/", response_class=HTMLResponse)
def index():
    html_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h3>ThaiD Vault Loading...</h3>")


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return index()


@app.get("/admin", response_class=HTMLResponse)
def admin():
    admin_file = os.path.join(STATIC_DIR, "admin.html")
    if os.path.exists(admin_file):
        with open(admin_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return index()"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("ThaiD-Vault app.py successfully patched!")
else:
    print("Target not found in ThaiD-Vault app.py")
