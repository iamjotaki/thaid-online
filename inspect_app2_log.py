from deploy_batch import run_tinker
print(run_tinker("""
$d = App\\Models\\ApplicationDeploymentQueue::where('application_id', 2)->latest()->first();
$logs = json_decode($d->logs, true);
if (is_array($logs)) {
    $last_logs = array_slice($logs, -5);
    foreach ($last_logs as $entry) {
        echo ($entry['output'] ?? '') . PHP_EOL;
    }
} else {
    echo "Logs not array or empty" . PHP_EOL;
}
"""))
