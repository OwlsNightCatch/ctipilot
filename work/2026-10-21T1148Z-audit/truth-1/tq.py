import json,sys
d=json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))['techniques']
for t in sys.argv[1:]:
    print(t, d.get(t,{}).get('name'), 'REVOKED' if d.get(t,{}).get('revoked') else '', 'DEPRECATED' if d.get(t,{}).get('deprecated') else '', 'UNKNOWN' if t not in d else '')
