import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm
ids = set(json.load(open(ROOT / "work/2026-10-21T1148Z-audit/entries.json")))
plan = json.load(open(ROOT / "work/cleanup/plan.json"))
held = {}
for r in plan["rows"]:
    if isinstance(r.get("entries"), list) and r.get("wave") != "04":
        for e in r["entries"]: held[e] = f"{r['id']} (wave {r.get('wave')})"
idx = {}
for e in cm.collect_entries():
    for c in e.get("cves") or []:
        cid = c.get("id") if isinstance(c, dict) else c
        idx.setdefault(cid, []).append(e["id"])
for cid, es in sorted(idx.items()):
    mine = [e for e in es if e in ids]
    if mine and len(es) > 1:
        print(cid, "|", "; ".join(f"{e}{' [MINE]' if e in ids else ' ['+held.get(e,'unheld')+']'}" for e in es))
