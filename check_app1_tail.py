from coolify_ops import run_tinker

code = """
$d1 = App\\Models\\ApplicationDeploymentQueue::where('application_id', 1)->latest()->first();
echo "STATUS: " . $d1->status . PHP_EOL;
$lines = explode(PHP_EOL, $d1->logs ?? '');
echo implode(PHP_EOL, array_slice($lines, -10));
"""
print(run_tinker(code))
