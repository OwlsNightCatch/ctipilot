#!/usr/bin/env python3
"""Phase 5 sources/sources.json update + run_log.json append."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = "2026-05-23"
RUN_ID = "2026-05-23-852c21c8"

# --- sources/sources.json -------------------------------------------------
src = json.loads((ROOT / "sources/sources.json").read_text())

# Sources actually used (fetched + contributed content) — bump last_successful_fetch.
# Conservative list — only the IDs that match a source.id we cited or whose
# bridge feed we ingested. Keep this list narrow; speculative bumps mask gaps.
used_today = {
    "bleepingcomputer", "krebs", "therecord", "hackernews", "checkpoint-research",
    "kaspersky-securelist", "unit42", "heise-sec", "anssi-fr", "ncsc-ch-security-hub",
    "cisa-kev", "helpnetsecurity", "cyberscoop", "rapid7-research", "ox-security",
}

# Sources we actually attempted but failed in this run (track failure counters)
failed_today = {
    "databreaches-net": "transport-403 (Cloudflare challenge)",
    "inside-it-ch":     "transport-403 (Cloudflare challenge) + Wayback stale",
    "sophos-xops":      "HTTP 503 — fifth consecutive failing run",
    "dragos":           "HTTP 404 on resource-library RSS (S3 listed as dragos-ot)",
}

for s in src["sources"]:
    if s.get("status") != "active":
        continue
    if s["id"] in used_today:
        s["last_successful_fetch"] = TODAY
        s["consecutive_quiet_periods"] = 0
        s["consecutive_fetch_failures"] = 0
        s["last_covered_in_brief"] = TODAY
    if s["id"] in failed_today:
        s["consecutive_fetch_failures"] = s.get("consecutive_fetch_failures", 0) + 1

# One new candidate per run (PD: hard cap). Pick searchlight-cyber — surfaced
# as corroborating source on Drupal CVE-2026-9082 with high-quality technical
# analysis; clear research-lab profile suitable for promotion path.
existing_ids = {s["id"] for s in src["sources"]}
if "searchlight-cyber" not in existing_ids:
    src["sources"].append({
        "id": "searchlight-cyber",
        "publisher": "Searchlight Cyber",
        "url": "https://slcyber.io/research-center/",
        "category": ["research"],
        "reliability": "MEDIUM",
        "language": ["en"],
        "status": "candidate",
        "fetch_method": "webfetch",
        "last_successful_fetch": TODAY,
        "consecutive_failures": 0,
        "notes": "Discovered on 2026-05-23 via Drupal CVE-2026-9082 coverage — published same-day technical analysis 'Keys to the Kingdom: Anonymous SQL Injection in Drupal Core CVE-2026-9082' (slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/) used as corroborating source by both S2 and S3 sub-agents. Candidate — promote to active after 3 runs with content contribution."
    })

src["last_updated"] = TODAY
(ROOT / "sources/sources.json").write_text(json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("sources/sources.json: bumped {} used + {} failures; +1 candidate (searchlight-cyber)".format(
    len(used_today), len(failed_today)))

# Print second candidate left in § 7 verification notes as overflow
print("note: gambit-security was the second candidate this run (Mexico AI-orchestrated breach primary research) — surfaced in § 7 verification notes; one-candidate-per-run cap.")

# --- run_log.json -------------------------------------------------------
rl = json.loads((ROOT / "state/run_log.json").read_text())

started_at = (ROOT / "work" / RUN_ID / "main.started_at").read_text().strip()
ended_at = (ROOT / "work" / RUN_ID / "main.ended_at").read_text().strip()
from datetime import datetime
def iso_to_ts(s):
    return int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").timestamp())
duration = iso_to_ts(ended_at) - iso_to_ts(started_at)

run_record = {
    "run_id": RUN_ID,
    "date": TODAY,
    "started": started_at,
    "completed": ended_at,
    "duration_seconds": duration,
    "model": "Claude Opus 4.7",
    "model_id": "claude-opus-4-7",
    "prompt_version": "v2.59",
    "sub_agents": {
        "S1": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-23T04:07:57Z",
            "ended_at": "2026-05-23T04:27:00Z",
            "duration_seconds": 1143,
            "sources_attempted": [
                "advisories-ncsc-nl","anssi-fr","apple-security","bsi-de","cert-eu","cert-pl",
                "chrome-releases","cisa-advisories","cisa-directives","cisa-kev","cisco-psirt",
                "greynoise","jpcert","mozilla-mfsa","ncsc-ch-incidents","ncsc-ch-security-hub",
                "ncsc-uk","oracle-cpu","projectzero","rapid7-research","shadowserver",
                "tenable-research","trustwave-spiderlabs","vulncheck","watchtowr","wiz-blog","zdi"
            ],
            "sources_used": ["cisa-kev","ncsc-ch-security-hub","rapid7-research","hackernews","krebs"],
            "items_returned": 6,
            "returned": True,
            "telemetry": {"webfetch_calls": 11, "websearch_calls": 14, "bridge_fetches": 9}
        },
        "S2": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-23T04:08:20Z",
            "ended_at": "2026-05-23T04:13:42Z",
            "duration_seconds": 322,
            "sources_attempted": [
                "advisories-ncsc-nl","anssi-fr","bsi-de","cert-at","cert-eu","cert-pl",
                "cisa-advisories","cisa-directives","cisa-news","citizen-lab","cnil-fr",
                "compass-security","crowdstrike","csirt-acn-it","edpb","enisa","google-tag",
                "govcert-at","heise-sec","ibm-xforce","ico-uk","infoguard-ch","inside-it-ch",
                "jpcert","kudelski-security","le-monde-info","mandiant-gtig","msft-ti",
                "ncc-research","ncsc-ch-focus","ncsc-ch-incidents","ncsc-ch-security-hub",
                "ncsc-ie","ncsc-uk","oneconsult-ch","prodaft","recordedfuture-insikt",
                "safeonweb-be","scip-ch","sekoia","truesec","us-treasury-ofac","withsecure-labs"
            ],
            "sources_used": ["heise-sec","anssi-fr","ncsc-ch-security-hub"],
            "items_returned": 4,
            "returned": True,
            "telemetry": {"webfetch_calls": 8, "websearch_calls": 16, "bridge_fetches": 10}
        },
        "S3": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-23T04:08:40Z",
            "ended_at": "2026-05-23T04:14:10Z",
            "duration_seconds": 330,
            "sources_attempted": [
                "akamai-sirt","bleepingcomputer","checkpoint-research","cisa-news","citizen-lab",
                "cloudflare-cf1","compass-security","crowdstrike","cyberscoop","darkreading",
                "dfirreport","dragos","elastic-seclabs","eset","google-tag","greynoise","hackernews",
                "heise-sec","helpnetsecurity","huntress","ibm-xforce","infosec-magazine","inside-it-ch",
                "intel471","kaspersky-securelist","krebs","kudelski-security","le-monde-info",
                "malwarebytes","mandiant-gtig","msft-ti","ncc-research","oneconsult-ch","prodaft",
                "projectzero","push-security","rapid7-research","recordedfuture-insikt","redcanary",
                "risky-biz-news","sans-ics","sans-isc","sans-newsbites","schneier","scip-ch",
                "securityaffairs","securityweek","sekoia","sentinellabs","shadowserver","socprime",
                "sophos-xops","sygnia","talos","tenable-research","therecord","trellix",
                "trendmicro-research","troyhunt","truesec","trustwave-spiderlabs","unit42",
                "volexity","watchtowr","withsecure-labs","wiz-blog","zdi"
            ],
            "sources_used": ["unit42","kaspersky-securelist","checkpoint-research","krebs","therecord"],
            "items_returned": 5,
            "returned": True,
            "telemetry": {"webfetch_calls": 7, "websearch_calls": 5, "bridge_fetches": 14}
        },
        "S4": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-23T04:08:57Z",
            "ended_at": "2026-05-23T04:18:31Z",
            "duration_seconds": 574,
            "sources_attempted": [
                "bleepingcomputer","cisa-news","cnil-fr","cyberscoop","darkreading","databreaches-net",
                "edpb","hackernews","heise-sec","helpnetsecurity","ico-uk","infosec-magazine",
                "inside-it-ch","krebs","le-monde-info","malwarebytes","risky-biz-news","sans-isc",
                "sans-newsbites","schneier","sec-disclosures-edgar","securityaffairs","securityweek",
                "therecord","troyhunt"
            ],
            "sources_used": ["bleepingcomputer","helpnetsecurity","therecord","cyberscoop"],
            "items_returned": 3,
            "returned": True,
            "telemetry": {"webfetch_calls": 22, "websearch_calls": 12, "bridge_fetches": 8}
        }
    },
    "fetch_failures": [
        {
            "id": "databreaches-net",
            "url_tried": "https://databreaches.net/",
            "fetch_method": "bridge:url",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "upstream HTTP 403 (Cloudflare Managed Challenge)",
            "attempted_methods": ["bridge:url","bridge:wayback"],
            "mitigation_applied": "BleepingComputer/TheRecord/SecurityAffairs cross-check covered the same incidents",
            "covered_anyway": False
        },
        {
            "id": "inside-it-ch",
            "url_tried": "https://www.inside-it.ch/",
            "fetch_method": "bridge:url",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "Cloudflare Managed Challenge page; Wayback snapshot stale (>7 days)",
            "attempted_methods": ["bridge:url","bridge:wayback"],
            "mitigation_applied": "WebSearch fallback found no in-window CH-specific items from this publisher",
            "covered_anyway": False
        },
        {
            "id": "sophos-xops",
            "url_tried": "https://www.sophos.com/en-us/blog/feed?id=blt6f15f4f7deaf4242",
            "fetch_method": "webfetch",
            "status_code": 503,
            "error_class": "transport-5xx",
            "error_message": "HTTP 503 on canonical RSS — fifth consecutive failing run",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "none — quiet host this run; rotation-priority for next",
            "covered_anyway": False
        },
        {
            "id": "dragos",
            "url_tried": "https://www.dragos.com/resource-library/rss/",
            "fetch_method": "webfetch",
            "status_code": 404,
            "error_class": "transport-404",
            "error_message": "HTTP 404 on resource-library RSS — feed appears stale",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "none — no OT/ICS primary research surfaced in this window",
            "covered_anyway": False
        }
    ],
    "bridge_uses": [
        {"id": "cisa-kev", "method": "bridge:cisa-kev", "outcome": "ok"},
        {"id": "ncsc-ch-security-hub", "method": "bridge:ncsc-csh.recent", "outcome": "ok"},
        {"id": "ico-uk", "method": "bridge:url", "outcome": "ok"},
        {"id": "sec-disclosures-edgar", "method": "bridge:sec-edgar.8k", "outcome": "ok"},
        {"id": "ic3-psa", "method": "bridge:url", "outcome": "item-not-found"}
    ],
    "items_published": 14,
    "items_dropped_by_verification": 0,
    "deep_dive": "cve-2026-46333-ssh-keysign-pwn-linux-kernel-ptrace-race",
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {"iterations": []}
}

# Idempotent retry: replace if run_id already present
existing_idx = next((i for i, r in enumerate(rl.get("runs", [])) if r.get("run_id") == RUN_ID), None)
if existing_idx is not None:
    rl["runs"][existing_idx] = run_record
    print(f"run_log.json: replaced existing entry for {RUN_ID}")
else:
    rl.setdefault("runs", []).append(run_record)
    print(f"run_log.json: appended {RUN_ID}")

# Trim to 90 most recent
rl["runs"] = rl["runs"][-90:]
rl["last_updated"] = TODAY
(ROOT / "state/run_log.json").write_text(json.dumps(rl, indent=2, ensure_ascii=False) + "\n")
print("run_log.json: trimmed to 90 most recent")
