"""Print name/state of ATT&CK ids from the pinned dataset. Usage: attack_ids.py T1190 T1078 ..."""
import json
import sys

d = json.load(open("/home/user/ctipilot/attack/enterprise-attack.json"))
t = d["techniques"]
for tid in sys.argv[1:]:
    r = t.get(tid)
    if not r:
        print(tid, "UNKNOWN")
        continue
    state = "revoked->%s" % r["revoked_by"] if r["revoked"] else ("DEPRECATED" if r["deprecated"] else "active")
    print(tid, "|", r["name"], "|", ",".join(r["tactics"]), "|", state)
