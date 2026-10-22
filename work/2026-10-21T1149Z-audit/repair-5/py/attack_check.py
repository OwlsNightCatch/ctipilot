"""Report each ATT&CK id's name, tactics and status in the pinned dataset."""
import json, sys
t = json.load(open('/home/user/ctipilot/attack/enterprise-attack.json'))['techniques']
for i in sys.argv[1:]:
    o = t.get(i)
    if not o:
        print(i, 'UNKNOWN')
        continue
    st = 'revoked->%s' % o.get('revoked_by') if o.get('revoked') else ('deprecated' if o.get('deprecated') else 'active')
    print(i, st, '|', o['name'], '|', ','.join(o.get('tactics') or []))
