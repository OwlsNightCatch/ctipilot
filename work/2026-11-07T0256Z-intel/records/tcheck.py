import json,sys
t=json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))['techniques']
for k in sys.argv[1:]:
    v=t.get(k)
    if not v: print(k,'NOT FOUND'); continue
    st='OK' if not v['deprecated'] and not v['revoked'] else f"DEAD revoked_by={v['revoked_by']}"
    print(k,v['name'],st)
