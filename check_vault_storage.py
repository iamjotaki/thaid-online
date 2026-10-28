from coolify_ops import run_tinker

code = """
$a = App\\Models\\Application::find(4);
echo "NAME: " . $a->name . PHP_EOL;
echo "STORAGES: " . json_encode($a->persistentStorages) . PHP_EOL;
echo "OPTIONS: " . $a->custom_docker_run_options . PHP_EOL;
"""
print(run_tinker(code))
