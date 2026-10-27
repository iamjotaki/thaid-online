from coolify_ops import run_tinker

code = """
$d2 = App\\Models\\ApplicationDeploymentQueue::where('application_id', 2)->latest()->first();
$d3 = App\\Models\\ApplicationDeploymentQueue::where('application_id', 3)->latest()->first();
echo "App 2 status: " . $d2->status . PHP_EOL;
echo "App 3 status: " . $d3->status . PHP_EOL;
"""
print(run_tinker(code))
