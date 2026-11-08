"""Build the G1-G3 re-sweep slices for this audit from sources.json + the rotation cursor."""
import json, sys
RUN = "2026-11-08T1309Z-audit"
W = f"work/{RUN}"
s = json.load(open("sources/sources.json"))["sources"]
rot = {r["id"]: r for r in json.load(open(f"{W}/state-summary.json"))["sources"]["rotation"]}
by_id = {r["id"]: r for r in s}
def rec(r):
    notes = r.get("notes") or ""
    if isinstance(notes, list): notes = " | ".join(map(str, notes))
    return {"id": r["id"], "publisher": r.get("publisher"), "url": r.get("url"), "rss_url": r.get("rss_url"),
            "tier": r.get("tier"), "status": r.get("status"), "fetch_method": r.get("fetch_method"),
            "reliability": r.get("reliability"), "language": r.get("language"), "health_cmd": r.get("health_cmd"),
            "lookback_hours": 168, "rotation_key": (rot.get(r["id"]) or {}).get("rotation_key"),
            "latest_note": notes[-600:]}
def live(r): return r.get("status") in ("active", "candidate")
def build(cats, majors, cap, ess_cats=None):
    ess_cats = ess_cats or cats
    out, seen = [], set()
    def add(r):
        if r["id"] not in seen and live(r): seen.add(r["id"]); out.append(rec(r))
    for r in s:
        if r.get("tier") == "essential" and set(r.get("category") or []) & set(ess_cats): add(r)
    for m in majors:
        if m in by_id: add(by_id[m])
    rest = [r for r in s if set(r.get("category") or []) & set(cats) and r["id"] not in seen and live(r)]
    rest.sort(key=lambda r: ((rot.get(r["id"]) or {}).get("rotation_key") or "0000"))
    for r in rest:
        if len(out) >= cap: break
        add(r)
    return out
claimed = set()
G1 = build(["vulns", "vendor-psirt", "active-breaking"], ["qnap-security-advisories", "synology-security-advisories", "cisco-psirt", "ivanti-psirt", "oracle-cpu", "sap-security-notes", "zdi", "apple-security", "chrome-releases", "adobe-psirt", "drupal-security", "wordpress-org-news", "gitlab-security", "patchstack"], 46)
claimed |= {r["id"] for r in G1}
G2 = [r for r in build(["ch-eu", "gov", "breaches", "ransomware", "sanctions"], ["news-admin-ch", "fuitesinfos", "dcod-ch", "zataz", "sec-disclosures-edgar", "europol-newsroom", "jpcert"], 44 + 10) if r["id"] not in claimed][:44]
claimed |= {r["id"] for r in G2}
G3 = [r for r in build(["research", "discovery", "news"], ["msft-ti", "mandiant-gtig", "talos", "unit42", "checkpoint-research", "eset", "kaspersky-securelist", "sentinellabs", "proofpoint", "trendmicro-research", "google-tag", "huntress", "sophos-xops", "crowdstrike", "elastic-seclabs", "dfirreport", "recordedfuture-insikt", "volexity", "citizen-lab", "zscaler-threatlabz", "symantec-security-com", "lumen-black-lotus-labs", "group-ib", "gitguardian", "datadog-security-labs", "morphisec"], 50 + 15, ess_cats=["research"]) if r["id"] not in claimed][:50]
for n, sl in (("G1", G1), ("G2", G2), ("G3", G3)):
    json.dump(sl, open(f"{W}/slice-{n}.json", "w"), indent=1, ensure_ascii=False)
    print(n, len(sl), sum(1 for r in sl if r["tier"] == "essential"), "essential;", [r["id"] for r in sl])
