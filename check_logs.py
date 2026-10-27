from coolify_ops import run_tinker

code = """
foreach ([2, 3] as $id) {
    $d = App\\Models\\ApplicationDeploymentQueue::where('application_id', $id)->latest()->first();
    echo "=== APP " . $id . " (" . $d->status . ") ===" . PHP_EOL;
    $lines = explode(PHP_EOL, $d->logs ?? '');
    $last_lines = array_slice($lines, -8);
    echo implode(PHP_EOL, $last_lines) . PHP_EOL;
}
"""
print(run_tinker(code))
