import json,sys
d=json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))['techniques']
for t in sys.argv[1:]:
    x=d.get(t,{})
    print(t, x.get('name'), 'REVOKED' if x.get('revoked') else '', 'DEPRECATED' if x.get('deprecated') else '', 'UNKNOWN' if t not in d else '')
