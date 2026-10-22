import json,sys
d=json.load(open('/home/user/ctipilot/work/2026-10-21T1148Z-audit/truth-2/kev.json'))
idx={v['cveID']:v for v in d['vulnerabilities']}
for c in sys.argv[1:]:
    v=idx.get(c)
    print(c, json.dumps(v) if v else 'NOT IN KEV')
