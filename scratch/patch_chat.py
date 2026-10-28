import os

path = r"C:\ThaiD-Chat\app.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """@app.get("/")
def serve_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "ThaiD Smart Chat AI Studio Live"}"""

replacement = """@app.get("/")
def serve_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "ThaiD Smart Chat AI Studio Live"}


@app.get("/dashboard")
def serve_dashboard():
    dashboard_file = os.path.join(STATIC_DIR, "dashboard.html")
    if os.path.exists(dashboard_file):
        return FileResponse(dashboard_file)
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.get("/admin")
def serve_admin():
    admin_file = os.path.join(STATIC_DIR, "admin.html")
    if os.path.exists(admin_file):
        return FileResponse(admin_file)
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("ThaiD-Chat app.py successfully patched!")
else:
    print("Target not found in ThaiD-Chat app.py")
