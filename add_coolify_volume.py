from coolify_ops import run_tinker

code = """
$app = App\\Models\\Application::find(4);
echo "Application 4: " . $app->name . PHP_EOL;

// Check existing persistent volumes for this app
$vols = App\\Models\\LocalPersistentVolume::where('resource_id', 4)->get();
echo "Existing vols count: " . $vols->count() . PHP_EOL;

if ($vols->count() == 0) {
    $vol = new App\\Models\\LocalPersistentVolume();
    $vol->name = 'vault-data';
    $vol->mount_path = '/app/data';
    $vol->host_path = '/data/vault';
    $vol->resource_type = 'App\\Models\\Application';
    $vol->resource_id = 4;
    $vol->save();
    echo "Created persistent volume ID: " . $vol->id . PHP_EOL;
} else {
    foreach ($vols as $v) {
        echo "Vol: " . $v->id . " | Mount: " . $v->mount_path . " | Host: " . $v->host_path . PHP_EOL;
    }
}
"""
print(run_tinker(code))
