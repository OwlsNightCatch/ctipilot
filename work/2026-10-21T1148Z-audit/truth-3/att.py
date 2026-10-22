import json,sys
d=json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))['techniques']
for t in sys.argv[1:]:
    x=d.get(t)
    if x is None: print(t,'UNKNOWN'); continue
    st='REVOKED' if x.get('revoked') else ('DEPRECATED' if x.get('deprecated') else 'active')
    print(t, x.get('name'), st)
