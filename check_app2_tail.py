from coolify_ops import run_tinker

code = """
$d2 = App\\Models\\ApplicationDeploymentQueue::where('application_id', 2)->latest()->first();
$logs = $d2->logs ?? '';
echo substr($logs, -500);
"""
print(run_tinker(code))
