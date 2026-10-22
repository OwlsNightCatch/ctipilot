#!/usr/bin/env python3
"""Print name and status of ATT&CK ids from the pinned dataset (repair-2 helper)."""
import json, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[3]
t = json.load(open(root / "attack/enterprise-attack.json"))["techniques"]
for i in sys.argv[1:]:
    r = t.get(i)
    if not r:
        print(i, "MISSING"); continue
    st = "REVOKED->%s" % r["revoked_by"] if r["revoked"] else ("DEPRECATED" if r["deprecated"] else "active")
    print(i, r["name"], st, ",".join(r["tactics"]))
