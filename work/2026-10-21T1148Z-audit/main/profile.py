import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm
ids = json.load(open(ROOT / "work/2026-10-21T1148Z-audit/entries.json"))
by = {e["id"]: e for e in cm.collect_entries()}
rows = []
for i in ids:
    e = by[i]
    body = (ROOT / f"entries/{i}.md").read_text().split("\n---\n", 1)[-1]
    rows.append(dict(id=i, kind=e.get("kind"), pri=e.get("priority"),
        cves=len(e.get("cves") or []), srcs=len(e.get("sources") or []), ev=len(e.get("evidence") or []),
        tech=len(e.get("techniques") or []), cls=bool(e.get("classification")),
        upd=len(e.get("updates") or []), links=len(re.findall(r"\]\(https?://", body)),
        lab=sum(1 for l in ("**Exposure:**","**Detection:**","**Triage:**","**Defender takeaway:**") if l in body),
        words=len(body.split())))
from collections import Counter
print(Counter(r["kind"] for r in rows)); print(Counter(r["pri"] for r in rows))
print("ev>0", sum(r["ev"]>0 for r in rows), "links>0", sum(r["links"]>0 for r in rows), "tech>0", sum(r["tech"]>0 for r in rows), "cls", sum(r["cls"] for r in rows), "upd>0", sum(r["upd"]>0 for r in rows))
print("words total", sum(r["words"] for r in rows), "cves total", sum(r["cves"] for r in rows), "srcs total", sum(r["srcs"] for r in rows))
json.dump(rows, open(ROOT / "work/2026-10-21T1148Z-audit/main/profile.json", "w"), indent=1)
for r in rows: print(r["id"][:70].ljust(70), r["kind"][:5], r["pri"][:4] if r["pri"] else "-", r["cves"], r["srcs"], r["links"], r["lab"], r["words"], r["upd"])
