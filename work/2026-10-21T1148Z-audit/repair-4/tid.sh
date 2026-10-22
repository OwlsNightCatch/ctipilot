#!/bin/sh
cd /home/user/ctipilot && python3 -c "import json,sys;d=json.load(open('attack/enterprise-attack.json'))['techniques'];[print(t, d.get(t,{}).get('name'), 'REVOKED' if d.get(t,{}).get('revoked') else '', 'DEPRECATED' if d.get(t,{}).get('deprecated') else '', 'UNKNOWN' if t not in d else '') for t in sys.argv[1:]]" "$@"
