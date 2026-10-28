from deploy_batch import run_tinker
print("--- App 2 Log ---")
print(run_tinker("""
$d = App\\Models\\ApplicationDeploymentQueue::where('application_id', 2)->latest()->first();
echo substr($d->logs, -500);
"""))

print("--- App 3 Log ---")
print(run_tinker("""
$d = App\\Models\\ApplicationDeploymentQueue::where('application_id', 3)->latest()->first();
echo substr($d->logs, -500);
"""))
