import subprocess

tasks = [
    (r"C:\ThaiD.online", ["app/page.tsx", "app/components/OrbitShowcase.tsx"], "feat(portal): completely remove vault floating card and orbit card", "origin", "main"),
    (r"C:\ThaiD-Vault", ["static/index.html"], "chore(js): clean unused saas menu functions", "origin", "main"),
    (r"C:\ReadAWrite", ["web_saas_stitch/index.html"], "fix(footer): remove vault link from footer", "thaid-studio", "main"),
    (r"C:\Auto Post FB", ["templates/landing.html"], "fix(footer): remove vault link from footer", "thaid-social", "main"),
    (r"C:\ThaiD-Sticker", ["static/index.html"], "fix(footer): remove vault link from footer", "origin", "main"),
    (r"C:\ThaiD-Clip", ["static/index.html"], "fix(footer): remove vault link from footer", "origin", "main"),
    (r"C:\ThaiD-Chat", ["static/index.html"], "fix(footer): remove vault link and mentions from chat", "origin", "main"),
    (r"C:\ThaiD-Mockup", ["static/index.html"], "fix(footer): remove all vault links from mockup", "origin", "main")
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
