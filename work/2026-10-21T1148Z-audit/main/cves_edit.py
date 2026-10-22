"""Apply the repair workers' state/cves_seen.json changes (cleanup wave 04).

Usage: python3 cves_edit.py <ops.json>
Ops: {"add": {id, title, primary_source_url}}  (first_seen and last_seen = TODAY; a
     present id is bumped instead), {"bump": id}, {"title": id, "value": text},
     {"url": id, "value": url}. The file is re-serialised the way it round-trips
     (indent 1, insertion order, ASCII escapes).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = ROOT / "state" / "cves_seen.json"
TODAY = "2026-10-21"


def main():
    d = json.loads(P.read_text(encoding="utf-8"))
    by = {c["id"]: c for c in d["cves"]}
    for op in json.load(open(sys.argv[1])):
        if "add" in op:
            a = op["add"]
            if a["id"] in by:
                by[a["id"]]["last_seen"] = TODAY
                print("present, bumped", a["id"])
                continue
            rec = {"first_seen": TODAY, "id": a["id"], "last_seen": TODAY,
                   "primary_source_url": a["primary_source_url"], "title": a["title"]}
            d["cves"].append(rec)
            by[a["id"]] = rec
            print("added", a["id"])
        elif "bump" in op:
            if op["bump"] not in by:
                raise SystemExit(f"missing {op['bump']}")
            by[op["bump"]]["last_seen"] = TODAY
        elif "title" in op:
            by[op["title"]]["title"] = op["value"]
            by[op["title"]]["last_seen"] = TODAY
        elif "url" in op:
            by[op["url"]]["primary_source_url"] = op["value"]
        else:
            raise SystemExit(f"unknown op {op}")
    d["last_updated"] = TODAY
    P.write_text(json.dumps(d, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
