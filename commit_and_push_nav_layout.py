import subprocess

tasks = [
    (r"C:\ThaiD.online", ["app/page.tsx"], "feat(nav): move saas dropdown to right next to login, remove sub home link and sheet handle", "origin", "main"),
    (r"C:\ReadAWrite", ["web_saas_stitch/index.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "thaid-studio", "main"),
    (r"C:\Auto Post FB", ["templates/landing.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "thaid-social", "main"),
    (r"C:\ThaiD-Sticker", ["static/index.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "origin", "main"),
    (r"C:\ThaiD-Clip", ["static/index.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "origin", "main"),
    (r"C:\ThaiD-Chat", ["static/index.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "origin", "main"),
    (r"C:\ThaiD-Mockup", ["static/index.html"], "feat(nav): move saas dropdown to right next to login, remove sub home link", "origin", "main")
]

for repo, files, msg, remote, branch in tasks:
    print(f"=== {repo} -> {remote}/{branch} ===")
    for f in files:
        subprocess.run(["git", "add", f], cwd=repo, check=True)
    c_res = subprocess.run(["git", "commit", "-m", msg], cwd=repo, capture_output=True, text=True)
    if c_res.stdout:
        print("Commit:", c_res.stdout.strip())
    p_res = subprocess.run(["git", "push", remote, branch], cwd=repo, capture_output=True, text=True)
    print("Push:", (p_res.stdout or "") + (p_res.stderr or ""))
