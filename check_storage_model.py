from coolify_ops import run_tinker

code = """
$cols = DB::select("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'local_persistent_volumes'");
foreach ($cols as $c) {
    echo "COL: " . $c->column_name . " (" . $c->data_type . ")" . PHP_EOL;
}
echo "--- SAMPLE ---" . PHP_EOL;
$sample = DB::table('local_persistent_volumes')->get();
echo json_encode($sample) . PHP_EOL;
"""
print(run_tinker(code))
