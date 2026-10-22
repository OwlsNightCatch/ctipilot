import json, sys
d = json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))
T = d['techniques']
for t in sys.argv[1:]:
    r = T.get(t)
    if r is None:
        print(t, 'UNKNOWN'); continue
    flags = {k: r.get(k) for k in ('revoked', 'deprecated', 'revoked_by') if r.get(k)}
    print(t, r.get('name'), r.get('tactics'), flags or 'active')
