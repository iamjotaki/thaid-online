from coolify_ops import run_tinker

code = """
$d3 = App\\Models\\ApplicationDeploymentQueue::where('application_id', 3)->latest()->first();
$logs = $d3->logs ?? '';
echo substr($logs, -500);
"""
print(run_tinker(code))
