import subprocess

repos = [
    ('ThaiD.online', r'C:\ThaiD.online'),
    ('Novel Studio', r'C:\ReadAWrite'),
    ('Social Auto-Poster', r'C:\Auto Post FB'),
    ('LINE Sticker', r'C:\ThaiD-Sticker'),
    ('Clip AI', r'C:\ThaiD-Clip'),
    ('Smart Chat', r'C:\ThaiD-Chat'),
    ('Mockup Studio', r'C:\ThaiD-Mockup'),
]

for name, path in repos:
    try:
        remote = subprocess.check_output(['git', 'remote', '-v'], cwd=path, text=True, encoding='utf-8').strip().splitlines()[0]
        status = subprocess.check_output(['git', 'status', '-s'], cwd=path, text=True, encoding='utf-8').strip()
        last_log = subprocess.check_output(['git', 'log', '-1', '--oneline'], cwd=path, text=True, encoding='utf-8').strip()
        branch_status = subprocess.check_output(['git', 'status', '-b', '--porcelain'], cwd=path, text=True, encoding='utf-8').splitlines()[0]
        print(f"=== {name} ===")
        print(f"Branch: {branch_status}")
        print(f"Commit: {last_log}")
        print(f"Remote: {remote}")
        print(f"Local dirty files:\n{status if status else '(Clean)'}")
        print()
    except Exception as e:
        print(f"=== {name} === Error: {e}\n")
