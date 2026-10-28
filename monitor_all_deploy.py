import time
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_tinker(php_code):
    cmd = ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', r'C:\NV\oracle_key.pem', 'ubuntu@129.221.170.225', 'sudo docker exec -i coolify php artisan tinker']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    stdout, stderr = p.communicate(input=php_code)
    return stdout

def get_statuses():
    code = """
$ids = [1, 2, 3, 4, 5, 6, 7, 8];
foreach ($ids as $id) {
    $a = App\\Models\\Application::find($id);
    $d = App\\Models\\ApplicationDeploymentQueue::where('application_id', $id)->latest()->first();
    $status = $d ? $d->status : 'none';
    $commit = $d ? substr($d->commit, 0, 7) : 'none';
    echo "APP_STAT: " . $id . " | " . $a->name . " | " . $status . " | " . $commit . PHP_EOL;
}
"""
    out = run_tinker(code)
    results = {}
    for line in out.splitlines():
        if "APP_STAT: " in line:
            clean_line = line.replace("APP_STAT: ", "").strip()
            clean_line = clean_line.lstrip("> ").strip()
            parts = [p.strip() for p in clean_line.split("|")]
            try:
                results[int(parts[0])] = {"name": parts[1], "status": parts[2], "commit": parts[3]}
            except Exception:
                pass
    return results

print("Starting deployment monitor for all 8 apps...")
for iteration in range(30):
    stats = get_statuses()
    all_finished = True
    print(f"\n--- Check #{iteration+1} ---")
    for app_id, data in sorted(stats.items()):
        print(f"App {app_id} ({data['name']}): {data['status']} [{data['commit']}]")
        if data['status'] not in ['finished']:
            all_finished = False
    if all_finished:
        print("\nAll 8 applications have finished deploying successfully!")
        break
    time.sleep(10)
