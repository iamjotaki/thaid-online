from deploy_batch import run_tinker

code = """
foreach ([1,2,3,4,5,6,7,8] as $id) {
    $a = App\\Models\\Application::find($id);
    if ($a) {
        echo 'APP: ' . $a->id . ' | ' . $a->name . ' | ' . $a->git_repository . ' | ' . $a->git_branch . PHP_EOL;
    }
}
"""
print(run_tinker(code))
