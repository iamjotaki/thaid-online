import sys
sys.stdout.reconfigure(encoding='utf-8')
from deploy_batch import run_tinker
print(run_tinker("""
$d = App\\Models\\ApplicationDeploymentQueue::where('application_id', 3)->latest()->first();
$logs = json_decode($d->logs, true);
if (is_array($logs)) {
    $last_logs = array_slice($logs, -8);
    foreach ($last_logs as $entry) {
        echo ($entry['output'] ?? '') . PHP_EOL;
    }
}
"""))
