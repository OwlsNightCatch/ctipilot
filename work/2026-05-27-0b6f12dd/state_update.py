#!/usr/bin/env python3
import json, sys

RID = "2026-05-27-0b6f12dd"
TODAY = "2026-05-27"
BRIEF = f"briefs/{TODAY}.md"

def load(p): return json.load(open(p))
def save(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")

# ---------- cves_seen.json ----------
cs = load("state/cves_seen.json")
existing = {c["id"] for c in cs["cves"]}
new_cves = [
    ("CVE-2026-9312", "GitHub Enterprise Server < 3.22 — unauthenticated SSRF via upload-endpoint path traversal exposes internal services and credentials (CVSS 4.0 = 9.2; GHSA-fwfp-h68w-2hcr)", "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-32027"),
    ("CVE-2026-9642", "Delta Electronics DIAView SCADA — incomplete fix / mitigation bypass of CVE-2025-62582 unauthenticated remote database access (CVSS 3.1 = 9.8; Tenable TRA-2026-44)", "https://www.tenable.com/security/research/tra-2026-44"),
    ("CVE-2025-62582", "Delta Electronics DIAView SCADA — unauthenticated remote database access (predecessor to CVE-2026-9642 mitigation bypass)", "https://www.tenable.com/security/research/tra-2026-44"),
    ("CVE-2026-45659", "Microsoft SharePoint Server 2016/2019/SE — authenticated Site Member untrusted-data deserialization RCE (CWE-502, CVSS 8.8); patched May 2026 PT, added out-of-band 2026-05-26; NCSC-CH adv 12594 / BSI WID-SEC-2026-1652; dropped from § 2 (post-auth, sub-9.0, not exploited)", "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45659"),
    ("CVE-2026-44895", "yoda-digital mcp-gitlab-server < 0.6.0 — no-auth SSE RPC endpoint bound to 0.0.0.0 with wildcard CORS exposes operator GitLab PAT (CVSS 4.0 = 9.2; GHSA-8jr5-6gvj-rfpf); noted in § 7 (niche package)", "https://github.com/yoda-digital/mcp-gitlab-server/security/advisories/GHSA-8jr5-6gvj-rfpf"),
]
added = []
for cid, title, url in new_cves:
    if cid in existing:
        for c in cs["cves"]:
            if c["id"] == cid:
                c["last_seen"] = TODAY
        continue
    cs["cves"].append({"first_seen": TODAY, "id": cid, "last_seen": TODAY, "primary_source_url": url, "title": title})
    added.append(cid)
cs["last_updated"] = TODAY
save("state/cves_seen.json", cs)
print("cves_seen: added", added)

# ---------- covered_items.json ----------
ci = load("state/covered_items.json")
items = ci["items"]
by_key = {it["key"]: it for it in items}

def add_appearance(key, section, delta):
    it = by_key.get(key)
    if it is None:
        return False
    it["last_covered"] = TODAY
    it["appearances"].append({"date": TODAY, "section": section, "brief_path": BRIEF, "delta_summary": delta})
    return True

def new_item(key, typ, title, url, section, delta):
    it = {"key": key, "type": typ, "title": title, "first_covered": TODAY,
          "last_covered": TODAY, "primary_source_url": url,
          "appearances": [{"date": TODAY, "section": section, "brief_path": BRIEF, "delta_summary": delta}]}
    items.append(it); by_key[key] = it

# New items
new_item("incident:lithuania-centre-of-registers-2026", "incident",
         "Lithuania Centre of Registers breach — ~600,000 property/legal-entity records exfiltrated via abused institutional API credentials; foreign-state actor suspected; agency head resigned",
         "https://therecord.media/lithuania-investigates-theft-of-state-records",
         "active_threats",
         "First coverage. ~600k records from Real Estate Register / Register of Legal Entities; credential abuse of authorised institutional accounts from foreign infrastructure; names/DOB/national-ID/cadastral data; Russia-suspected; CoR head resigned.")

new_item("CVE-2026-9312", "cve",
         "GitHub Enterprise Server < 3.22 — unauthenticated SSRF via upload-endpoint path traversal (CVSS 4.0 = 9.2)",
         "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-32027",
         "trending_vulns",
         "First coverage. Pre-auth SSRF reaching internal services / credential exposure (App tokens, service-account keys); EPSS 0.0, no ITW; patched 3.16.20–3.21.1.")

new_item("CVE-2026-9642", "cve",
         "Delta Electronics DIAView SCADA — incomplete fix / mitigation bypass of CVE-2025-62582 unauthenticated remote DB access (CVSS 9.8) [SINGLE-SOURCE]",
         "https://www.tenable.com/security/research/tra-2026-44",
         "trending_vulns",
         "First coverage. Tenable TRA-2026-44 mitigation-bypass disclosure; OT/ICS; prior CVE-2025-62582 fix incomplete; single-source (Tenable).")

# UPDATE appearances on existing keys
updates = [
    ("actor:ShinyHunters", "updates", "UPDATE: Charter Communications confirms breach (disputes 42M-record / sensitive-PI-CPNI claim); 7-Eleven confirms 185,000 franchise-applicant records incl. SSNs/driver's licences. Both via vishing→Entra→Salesforce-Aura pattern."),
    ("campaign:mini-shai-hulud", "updates", "UPDATE: CERT-FR CERTFR-2026-ACT-023 first national-CERT confirmation of French victims; widened affected-package scope (@antv, @mistralai/mistralai, guardrails-ai, lightning); source code leaked to forum 2026-05-13."),
    ("actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt", "updates", "UPDATE: Check Point Research details MiniFast backdoor (replaces MiniJunk), JSON-HTTP API C2 (14 opcodes), ZoomUpdateTaskUser-<SID> scheduled-task hijacking, SEO-poisoning delivery, three waves keyed to Operation Epic Fury."),
    ("item:tycoon2fa-oauth-device-authorization-grant-microsoft-365-post-takedown", "deep_dive", "Deep dive: Elastic Security Labs detection-engineering analysis — two-tier operator architecture (cloud-VPS Kit Relay vs residential Operator Console), device-code PRT-replay variant, Graph reconnaissance-burst detection, Identity Protection aiConfirmedSafe false-negative gap."),
]
missing = []
for key, section, delta in updates:
    if not add_appearance(key, section, delta):
        missing.append(key)
ci["last_updated"] = TODAY
save("state/covered_items.json", ci)
print("covered_items: new=3 ; update-appearances applied; missing keys:", missing)

# ---------- deep_dive_history.json ----------
dd = load("state/deep_dive_history.json")
dd["entries"].append({
    "date": TODAY,
    "category": "identity-infra",
    "title": "Tycoon 2FA after the March 2026 takedown — two-tier AiTM operator architecture and the OAuth device-code variant",
    "primary_cve": "",
    "brief_path": BRIEF,
})
dd["entries"] = dd["entries"][-30:]
dd["last_updated"] = TODAY
save("state/deep_dive_history.json", dd)
print("deep_dive_history: appended identity-infra; entries=", len(dd["entries"]))

# ---------- run_log.json ----------
rl = load("state/run_log.json")
runs = rl["runs"]
started = open(f"work/{RID}/main.started_at").read().strip()
ended = open(f"work/{RID}/main.ended_at").read().strip()
from datetime import datetime
def secs(a, b):
    f = "%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds())

sub = {
    "S1": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6", "started_at": "2026-05-27T04:11:51Z", "ended_at": "2026-05-27T04:18:34Z", "duration_seconds": 403,
           "sources_attempted": ["cisa-kev","cisa-advisories","enisa","anssi-fr","bsi-de","cert-eu","cert-pl","ncsc-ch-security-hub","ncsc-ch-incidents","ncsc-uk","cisco-psirt","tenable-research","zdi","watchtowr","wiz-blog","jpcert","mozilla-mfsa","oracle-cpu","greynoise","projectzero","rapid7-research","trustwave-spiderlabs","vulncheck","shadowserver","apple-security","chrome-releases","advisories-ncsc-nl"],
           "sources_used": ["ncsc-ch-security-hub","bsi-de","enisa","tenable-research"],
           "items_returned": 6, "returned": True,
           "telemetry": {"webfetch_calls": 22, "websearch_calls": 4, "bridge_fetches": 18}},
    "S2": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6", "started_at": "2026-05-27T04:12:09Z", "ended_at": "2026-05-27T04:20:53Z", "duration_seconds": 524,
           "sources_attempted": ["anssi-fr","bsi-de","cert-at","cert-eu","cert-pl","cisa-advisories","cisa-news","citizen-lab","cnil-fr","compass-security","crowdstrike","csirt-acn-it","edpb","enisa","google-tag","govcert-at","heise-sec","ibm-xforce","ico-uk","infoguard-ch","inside-it-ch","jpcert","kudelski-security","le-monde-info","mandiant-gtig","msft-ti","ncc-research","ncsc-ch-focus","ncsc-ch-incidents","ncsc-ch-security-hub","ncsc-ie","ncsc-uk","oneconsult-ch","prodaft","recordedfuture-insikt","safeonweb-be","scip-ch","sekoia","truesec","us-treasury-ofac","withsecure-labs","advisories-ncsc-nl"],
           "sources_used": ["anssi-fr","ncsc-ch-security-hub","bsi-de"],
           "items_returned": 2, "returned": True,
           "telemetry": {"webfetch_calls": 12, "websearch_calls": 14, "bridge_fetches": 14}},
    "S3": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6", "started_at": "2026-05-27T04:12:29Z", "ended_at": "2026-05-27T04:23:22Z", "duration_seconds": 653,
           "sources_attempted": ["akamai-sirt","bleepingcomputer","checkpoint-research","cloudflare-cf1","dfirreport","dragos","elastic-seclabs","eset","google-tag","greynoise","hackernews","helpnetsecurity","huntress","ibm-xforce","intel471","kaspersky-securelist","krebs","malwarebytes","mandiant-gtig","msft-ti","projectzero","push-security","rapid7-research","recordedfuture-insikt","redcanary","risky-biz-news","sans-ics","sans-isc","schneier","sentinellabs","shadowserver","socprime","sophos-xops","sygnia","talos","tenable-research","therecord","trellix","trendmicro-research","unit42","volexity","watchtowr","withsecure-labs","wiz-blog","zdi","cyberscoop","darkreading","infosec-magazine","securityaffairs","securityweek","sans-newsbites"],
           "sources_used": ["elastic-seclabs","checkpoint-research","hackernews","securityaffairs"],
           "items_returned": 5, "returned": True,
           "telemetry": {"webfetch_calls": 14, "websearch_calls": 2, "bridge_fetches": 16}},
    "S4": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6", "started_at": "2026-05-27T04:12:39Z", "ended_at": "2026-05-27T04:23:13Z", "duration_seconds": 634,
           "sources_attempted": ["sec-disclosures-edgar","ico-uk","cnil-fr","edpb","databreaches-net","troyhunt","bleepingcomputer","therecord","securityaffairs","cyberscoop","krebs","heise-sec","le-monde-info"],
           "sources_used": ["bleepingcomputer","therecord","securityweek","securityaffairs"],
           "items_returned": 4, "returned": True,
           "telemetry": {"webfetch_calls": 14, "websearch_calls": 13, "bridge_fetches": 9}},
}

entry = {
    "run_id": RID,
    "date": TODAY,
    "started": started,
    "completed": ended,
    "duration_seconds": secs(started, ended),
    "model": "Claude Opus 4.7",
    "model_id": "claude-opus-4-7",
    "prompt_version": "v2.60",
    "sub_agents": sub,
    "fetch_failures": [
        {"id": "databreaches-net", "url_tried": "https://databreaches.net/category/breach-incidents/", "fetch_method": "bridge:url", "status_code": 403, "error_class": "transport-403", "error_message": "bridge:url returned HTTP 403; no Wayback snapshot for listing page", "attempted_methods": ["webfetch","bridge:url"], "mitigation_applied": "none", "covered_anyway": False},
        {"id": "inside-it-ch", "url_tried": "https://www.inside-it.ch/", "fetch_method": "bridge:url", "status_code": 403, "error_class": "transport-403", "error_message": "bridge:url returned HTTP 403 (rotation gap 5 runs)", "attempted_methods": ["webfetch","bridge:url"], "mitigation_applied": "none", "covered_anyway": False},
        {"id": "sec-disclosures-edgar", "url_tried": "https://www.sec.gov/Archives/edgar/data/1799191/000107997326000721/toi_8k.htm", "fetch_method": "webfetch", "status_code": 403, "error_class": "transport-403", "error_message": "sec.gov/Archives 403 via WebFetch and bridge; full-text search bridge works, individual filing htm does not", "attempted_methods": ["webfetch","bridge:url"], "mitigation_applied": "relied on SecurityWeek summary; item dropped to § 7 as unverifiable primary", "covered_anyway": False},
    ],
    "bridge_uses": [
        {"id": "ncsc-ch-security-hub", "method": "api", "outcome": "ok"},
        {"id": "cisa-kev", "method": "bridge:cisa-kev", "outcome": "ok"},
        {"id": "sophos-xops", "method": "bridge:url", "outcome": "empty-feed"},
        {"id": "trendmicro-research", "method": "bridge:url", "outcome": "empty-feed"},
    ],
    "items_published": 7,
    "items_dropped_by_verification": 0,
    "deep_dive": "tycoon-2fa-aitm-operator-architecture",
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {"iterations": []},
}

# idempotent: replace if run_id exists
existing_idx = next((i for i, r in enumerate(runs) if r.get("run_id") == RID), None)
if existing_idx is not None:
    runs[existing_idx] = entry
    print("run_log: updated existing run_id in place")
else:
    runs.append(entry)
    print("run_log: appended new run")
rl["runs"] = runs[-90:]
rl["last_updated"] = TODAY
save("state/run_log.json", rl)
print("run_log: runs now", len(rl["runs"]))
