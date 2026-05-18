#!/usr/bin/env python3
"""Phase 5 run_log.json update — append today's run record."""
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RUN_ID = "2026-05-18-2eabc1cf"
TODAY = "2026-05-18"

path = REPO / "state" / "run_log.json"
with path.open() as fh:
    rl = json.load(fh)

work = REPO / "work" / RUN_ID
started = (work / "main.started_at").read_text().strip()
ended = (work / "main.ended_at").read_text().strip()

# Compute duration
def parse(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))
duration = int((parse(ended) - parse(started)).total_seconds())

# Idempotent retry — replace existing record with same run_id if present
existing_idx = None
for i, r in enumerate(rl["runs"]):
    if r.get("run_id") == RUN_ID:
        existing_idx = i
        break

record = {
    "run_id": RUN_ID,
    "date": TODAY,
    "kind": "daily",
    "started": started,
    "completed": ended,
    "duration_seconds": duration,
    "model": "Claude Opus 4.7",
    "model_id": "claude-opus-4-7",
    "prompt_version": "v2.59",
    "sub_agents": {
        "S1": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-18T04:05:38Z",
            "ended_at": "2026-05-18T04:11:26Z",
            "duration_seconds": 348,
            "sources_attempted": ["cisa-kev", "apple-security", "chrome-releases", "cisco-psirt", "msft-ti", "hackernews", "securityaffairs", "helpnetsecurity", "vulncheck"],
            "sources_used": ["hackernews", "securityaffairs", "helpnetsecurity", "msft-ti"],
            "items_returned": 3,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 8,
                "websearch_calls": 18,
                "bridge_fetches": 6,
            },
        },
        "S2": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-18T04:06:02Z",
            "ended_at": "2026-05-18T04:17:19Z",
            "duration_seconds": 677,
            "sources_attempted": ["ncsc-ch-security-hub", "advisories-ncsc-nl", "msft-ti", "bsi-de", "cert-eu", "cert-pl", "csirt-acn-it", "enisa", "anssi-fr", "inside-it-ch", "heise-sec", "hackernews", "securityweek"],
            "sources_used": ["ncsc-ch-security-hub", "advisories-ncsc-nl", "msft-ti", "enisa", "cert-pl", "hackernews", "securityweek"],
            "items_returned": 6,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 22,
                "websearch_calls": 14,
                "bridge_fetches": 12,
            },
        },
        "S3": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-18T04:06:23Z",
            "ended_at": "2026-05-18T04:15:59Z",
            "duration_seconds": 576,
            "sources_attempted": ["dfirreport", "msft-ti", "unit42", "akamai-sirt", "trendmicro-research", "sophos-xops", "checkpoint-research", "eset", "talos", "kaspersky-securelist"],
            "sources_used": ["dfirreport", "msft-ti", "unit42"],
            "items_returned": 3,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 9,
                "websearch_calls": 8,
                "bridge_fetches": 22,
            },
        },
        "S4": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-18T04:06:33Z",
            "ended_at": "2026-05-18T04:17:52Z",
            "duration_seconds": 679,
            "sources_attempted": ["sec-disclosures-edgar", "ico-uk", "cnil-fr", "databreaches-net", "edpb", "therecord", "bleepingcomputer", "hackernews"],
            "sources_used": ["therecord", "bleepingcomputer"],
            "items_returned": 2,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 14,
                "websearch_calls": 18,
                "bridge_fetches": 12,
            },
        },
    },
    "fetch_failures": [
        {
            "id": "inside-it-ch",
            "url_tried": "https://www.inside-it.ch/",
            "fetch_method": "webfetch",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "WebFetch returned HTTP 403; documented known-403 host",
            "attempted_methods": ["webfetch", "websearch-fallback"],
            "mitigation_applied": "WebSearch fallback found no in-window CH public-sector incidents — source genuinely empty rather than a defender-actionable gap",
            "covered_anyway": False,
        },
        {
            "id": "cert-eu",
            "url_tried": "https://cert.europa.eu/publications/security-advisories",
            "fetch_method": "webfetch",
            "status_code": 200,
            "error_class": "spa-empty-body",
            "error_message": "Feed returned but most-recent entry is 2026-05-06 (PAN-OS) — outside 36h window",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "None — confirmed via RSS that no new CERT-EU advisories published in window",
            "covered_anyway": False,
        },
        {
            "id": "databreaches-net",
            "url_tried": "https://databreaches.net/",
            "fetch_method": "webfetch",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "WebFetch returned HTTP 403 — host blocks routine UA",
            "attempted_methods": ["webfetch", "websearch-fallback"],
            "mitigation_applied": "WebSearch fallback returned no unique in-window breach material beyond what S4's other sources covered",
            "covered_anyway": False,
        },
        {
            "id": "akamai-sirt",
            "url_tried": "https://www.akamai.com/blog/security-research",
            "fetch_method": "webfetch",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "Both RSS feed and blog listing returned 403",
            "attempted_methods": ["webfetch", "websearch-fallback"],
            "mitigation_applied": "WebSearch found no in-window Akamai SIRT research — no content loss confirmed",
            "covered_anyway": False,
        },
        {
            "id": "trendmicro-research",
            "url_tried": "https://www.trendmicro.com/en_us/research.html",
            "fetch_method": "webfetch",
            "status_code": 500,
            "error_class": "other",
            "error_message": "Feed XML parse error during fetch",
            "attempted_methods": ["webfetch", "websearch-fallback"],
            "mitigation_applied": "WebSearch returned only January 2026 TrendMicro research — no in-window content",
            "covered_anyway": False,
        },
        {
            "id": "sophos-xops",
            "url_tried": "https://news.sophos.com/en-us/category/security-operations/",
            "fetch_method": "webfetch",
            "status_code": 503,
            "error_class": "transport-5xx",
            "error_message": "HTTP 503 Service Unavailable",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "Transient transport failure — content loss for this run; will retry next run",
            "covered_anyway": False,
        },
    ],
    "items_published": 8,
    "items_dropped_by_verification": 0,
    "deep_dive": "tycoon2fa-oauth-device-authorization-grant-microsoft-365",
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {
        "iterations": []
    },
}

if existing_idx is not None:
    rl["runs"][existing_idx] = record
else:
    rl["runs"].append(record)

# Trim to 90 most recent
rl["runs"] = rl["runs"][-90:]

with path.open("w") as fh:
    json.dump(rl, fh, indent=2, ensure_ascii=False)

print(f"run_log.json: appended record run_id={RUN_ID} duration={duration}s")
