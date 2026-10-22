import json,sys
d=json.load(open('/home/user/ctipilot/state/cves_seen.json'))
idx={c['id']:c for c in d['cves']}
for c in sys.argv[1:]:
    r=idx.get(c)
    print(c, 'MISSING' if not r else {k:r.get(k) for k in ('first_seen','last_seen','title')})
