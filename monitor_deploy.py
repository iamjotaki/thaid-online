import sys, time
sys.path.append(r'C:\ThaiD.online')
from deploy_batch import get_statuses

for attempt in range(40):
    stats = get_statuses()
    all_done = True
    in_prog = []
    queued = []
    finished = []
    failed = []
    for aid in range(1, 9):
        d = stats.get(aid, {'status': 'unknown', 'name': f'app_{aid}', 'commit': ''})
        st = d['status']
        if st == 'in_progress':
            in_prog.append(aid)
            all_done = False
        elif st == 'queued':
            queued.append(aid)
            all_done = False
        elif st == 'finished':
            finished.append(aid)
        else:
            failed.append((aid, st))
    print(f"[{time.strftime('%H:%M:%S')}] Finished: {finished} | In Progress: {in_prog} | Queued: {queued} | Other: {failed}", flush=True)
    if all_done:
        print("ALL APPS FINISHED DEPLOYMENT!")
        break
    time.sleep(8)
