import subprocess

tasks = [
    (r"C:\ThaiD-Vault", ["app.py", "static/index.html"], "fix(security): remove public saas menu, demo bypass and add rate limiting", "origin", "main"),
    (r"C:\ReadAWrite", ["web_saas_stitch/index.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "thaid-studio", "main"),
    (r"C:\Auto Post FB", ["templates/landing.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "thaid-social", "main"),
    (r"C:\ThaiD-Sticker", ["static/index.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "origin", "main"),
    (r"C:\ThaiD-Clip", ["static/index.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "origin", "main"),
    (r"C:\ThaiD-Chat", ["static/index.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "origin", "main"),
    (r"C:\ThaiD-Mockup", ["static/index.html"], "feat(nav): remove vault from public saas dropdown and profile menu", "origin", "main")
]

for repo, files, msg, remote, branch in tasks:
    print(f"=== Committing and pushing {repo} -> {remote}/{branch} ===")
    for f in files:
        subprocess.run(["git", "add", f], cwd=repo, check=True)
    c_res = subprocess.run(["git", "commit", "-m", msg], cwd=repo, capture_output=True, text=True)
    if c_res.stdout:
        print("Commit:", c_res.stdout.strip())
    elif c_res.stderr and "nothing to commit" not in c_res.stderr:
        print("Commit err:", c_res.stderr.strip())
    
    p_res = subprocess.run(["git", "push", remote, branch], cwd=repo, capture_output=True, text=True)
    print("Push:", (p_res.stdout or "") + (p_res.stderr or ""))
