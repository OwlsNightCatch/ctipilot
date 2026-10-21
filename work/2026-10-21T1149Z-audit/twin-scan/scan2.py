"""Second, wider pass of the W4-05 twin scan: same non-product entity and
discovered within 3 days (title Jaccard >= 0.12), or a shared specific source
URL (cited by <= 4 entries) with title Jaccard >= 0.15. Unlinked, no shared CVE."""
import itertools, json, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from scan import cm, norm_url, words, jac  # noqa: E402


def main():
    ents = {e["id"]: e for e in cm.collect_entries()}
    refs = {i: set(e.get("references") or []) for i, e in ents.items()}
    cves = {i: {(c.get("id") if isinstance(c, dict) else c) for c in (e.get("cves") or [])} - {None} for i, e in ents.items()}
    tw = {i: words(e.get("title")) | words(e.get("headline")) for i, e in ents.items()}
    day = {i: cm.parse_ts(e.get("discovered_at")) for i, e in ents.items()}
    byent, byurl = defaultdict(set), defaultdict(set)
    for i, e in ents.items():
        for k in e.get("entities") or []:
            if not str(k).startswith("product:"):
                byent[k].add(i)
        for s in e.get("sources") or []:
            if isinstance(s, dict) and s.get("url"):
                byurl[norm_url(s["url"])].add(i)
    cand = {}
    def add(a, b, why):
        a, b = sorted((a, b))
        if b in refs[a] or a in refs[b] or (cves[a] & cves[b]):
            return
        cand.setdefault((a, b), set()).add(why)
    for k, ids in byent.items():
        for a, b in itertools.combinations(ids, 2):
            if day[a] and day[b] and abs((day[a] - day[b]).total_seconds()) <= 3 * 86400 and jac(tw[a], tw[b]) >= 0.12:
                add(a, b, f"entity3d:{k}")
    for u, ids in byurl.items():
        if 2 <= len(ids) <= 4:
            for a, b in itertools.combinations(ids, 2):
                if jac(tw[a], tw[b]) >= 0.15:
                    add(a, b, f"url:{u}")
    out = [{"a": a, "b": b, "why": sorted(w), "jaccard": round(jac(tw[a], tw[b]), 2),
            "title_a": ents[a].get("title"), "title_b": ents[b].get("title")} for (a, b), w in sorted(cand.items())]
    (Path(__file__).parent / "candidates2.json").write_text(json.dumps(out, indent=1) + "\n")
    print(len(out), "candidate pairs")
    for c in sorted(out, key=lambda c: -c["jaccard"]):
        print(c["jaccard"], c["a"][:62], "|", c["b"][:62], "|", c["why"][0][:70])


main()
