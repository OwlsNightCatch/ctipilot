"""W4-05 store-wide non-CVE twin scan (cleanup wave 03, 2026-10-21T1149Z-audit).

Candidate pairs: two entries with no references[] link either way that share
(a) a primary source URL, or (b) a non-product entity key and a similar title
(content-word Jaccard >= 0.30), or (c) any source URL and a title Jaccard >= 0.45.
Writes candidates.json next to this file. Stdlib only.
"""
import itertools, json, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "site"))
import content_model as cm  # noqa: E402

STOP = set("""a an the and or of to in on for with by from at as is are was were be via into after before over under new now
its it this that these those than then up out off not no yes vs versus cve 2025 2026 2024 more most first second two three
attack attacks attacker attackers exploited exploitation exploit active actively flaw flaws vulnerability vulnerabilities
critical high update updates patch patched patches fixed fix fixes zero day zero-day remote code execution rce""".split())


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("#")[0].split("?")[0].rstrip("/")
    return u


def words(t):
    return {w for w in re.findall(r"[a-z0-9][a-z0-9.\-]+", (t or "").lower()) if w not in STOP and len(w) > 2}


def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def main():
    ents = {e["id"]: e for e in cm.collect_entries()}
    refs = {i: set(e.get("references") or []) for i, e in ents.items()}

    def linked(a, b):
        return b in refs[a] or a in refs[b]

    cves = {i: {(c.get("id") if isinstance(c, dict) else c) for c in (e.get("cves") or [])} - {None} for i, e in ents.items()}
    tw = {i: words(e.get("title")) | words(e.get("headline")) for i, e in ents.items()}
    prim = defaultdict(set)
    anyurl = defaultdict(set)
    for i, e in ents.items():
        for s in e.get("sources") or []:
            if not isinstance(s, dict):
                continue
            u = norm_url(s.get("url"))
            if not u:
                continue
            anyurl[u].add(i)
            if s.get("role") == "primary":
                prim[u].add(i)
    byent = defaultdict(set)
    for i, e in ents.items():
        for k in e.get("entities") or []:
            if not str(k).startswith("product:"):
                byent[k].add(i)
    cand = {}

    def add(a, b, why):
        a, b = sorted((a, b))
        if linked(a, b) or (cves[a] & cves[b]):
            return
        cand.setdefault((a, b), set()).add(why)

    for u, ids in prim.items():
        if len(ids) < 12:
            for a, b in itertools.combinations(ids, 2):
                add(a, b, f"primary:{u}")
    for k, ids in byent.items():
        if len(ids) < 60:
            for a, b in itertools.combinations(ids, 2):
                j = jac(tw[a], tw[b])
                if j >= 0.30:
                    add(a, b, f"entity:{k} j={j:.2f}")
    for u, ids in anyurl.items():
        if len(ids) < 12:
            for a, b in itertools.combinations(ids, 2):
                j = jac(tw[a], tw[b])
                if j >= 0.45:
                    add(a, b, f"url:{u} j={j:.2f}")
    out = []
    for (a, b), why in sorted(cand.items()):
        out.append({"a": a, "b": b, "why": sorted(why), "title_a": ents[a].get("title"), "title_b": ents[b].get("title"),
                    "jaccard": round(jac(tw[a], tw[b]), 2)})
    (Path(__file__).parent / "candidates.json").write_text(json.dumps(out, indent=1) + "\n")
    print(len(ents), "entries;", len(out), "candidate pairs")


if __name__ == "__main__":
    main()
