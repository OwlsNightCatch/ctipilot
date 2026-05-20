#!/usr/bin/env python3
"""Append today's run record to state/run_log.json with idempotent retry."""
import json
from pathlib import Path

RUN_LOG = Path("state/run_log.json")
RUN_ID = "2026-05-20-a0f7b07f"

record = {
    "run_id": RUN_ID,
    "date": "2026-05-20",
    "kind": "daily",
    "started": "2026-05-20T04:02:50Z",
    "completed": "2026-05-20T04:28:51Z",
    "duration_seconds": 1561,
    "model": "Claude Opus 4.7",
    "model_id": "claude-opus-4-7",
    "prompt_version": "v2.59",
    "sub_agents": {
        "S1": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-20T04:04:13Z",
            "ended_at": "2026-05-20T04:15:08Z",
            "duration_seconds": 655,
            "sources_attempted": [
                "msrc",
                "cisa-kev",
                "drupal-psa",
                "fortiguard-psirt",
                "advisories-ncsc-nl",
                "openwall-oss-security",
                "ncsc-ch-security-hub",
                "bsi-de",
                "enisa-euvd",
                "bleepingcomputer",
                "thehackernews",
                "securityweek"
            ],
            "sources_used": [
                "msrc",
                "advisories-ncsc-nl",
                "openwall-oss-security",
                "ncsc-ch-security-hub",
                "bleepingcomputer",
                "thehackernews",
                "securityweek"
            ],
            "items_returned": 5,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 14,
                "websearch_calls": 18,
                "bridge_fetches": 16
            }
        },
        "S2": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-20T04:04:34Z",
            "ended_at": "2026-05-20T04:09:55Z",
            "duration_seconds": 321,
            "sources_attempted": [
                "ncsc-ch-security-hub",
                "bsi-de",
                "cert-pl",
                "cert-fr-actu",
                "ncsc-uk",
                "cert-eu",
                "ico-uk",
                "inside-it-ch",
                "enisa-euvd"
            ],
            "sources_used": [
                "ncsc-ch-security-hub",
                "bsi-de",
                "cert-pl",
                "enisa-euvd"
            ],
            "items_returned": 4,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 6,
                "websearch_calls": 10,
                "bridge_fetches": 12
            }
        },
        "S3": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-20T04:04:58Z",
            "ended_at": "2026-05-20T04:12:30Z",
            "duration_seconds": 452,
            "sources_attempted": [
                "msft-secblog",
                "talos-rss",
                "thehackernews",
                "infoguard-labs",
                "stepsecurity",
                "sans-isc",
                "sophos-xops",
                "trendmicro-research",
                "wiz-research",
                "cybersecuritynews",
                "moselwal"
            ],
            "sources_used": [
                "msft-secblog",
                "talos-rss",
                "thehackernews",
                "infoguard-labs",
                "stepsecurity",
                "sans-isc",
                "wiz-research",
                "cybersecuritynews",
                "moselwal"
            ],
            "items_returned": 8,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 22,
                "websearch_calls": 6,
                "bridge_fetches": 14
            }
        },
        "S4": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-20T04:05:16Z",
            "ended_at": "2026-05-20T04:14:48Z",
            "duration_seconds": 572,
            "sources_attempted": [
                "msft-secblog",
                "therecord",
                "bleepingcomputer",
                "databreaches-net",
                "inside-it-ch",
                "sec-edgar-8k",
                "ico-uk",
                "cnil-fr"
            ],
            "sources_used": [
                "msft-secblog",
                "therecord",
                "bleepingcomputer"
            ],
            "items_returned": 4,
            "returned": True,
            "telemetry": {
                "webfetch_calls": 14,
                "websearch_calls": 18,
                "bridge_fetches": 9
            }
        }
    },
    "fetch_failures": [
        {
            "id": "inside-it-ch",
            "url_tried": "https://www.inside-it.ch/",
            "fetch_method": "webfetch",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "Cloudflare Managed Challenge blocks both WebFetch and bridge fetches; rotation-priority candidate for 4 consecutive runs",
            "attempted_methods": ["webfetch", "websearch"],
            "mitigation_applied": "none — no in-window Swiss-only content distinct from NCSC.ch / BSI captures",
            "covered_anyway": False
        },
        {
            "id": "databreaches-net",
            "url_tried": "https://databreaches.net/",
            "fetch_method": "webfetch",
            "status_code": 403,
            "error_class": "transport-403",
            "error_message": "Cloudflare-gated; no usable Wayback snapshot in-window; rotation-priority candidate",
            "attempted_methods": ["webfetch", "websearch"],
            "mitigation_applied": "none — WebSearch pivots returned only aggregator restatements",
            "covered_anyway": False
        },
        {
            "id": "sophos-xops",
            "url_tried": "https://news.sophos.com/feed/",
            "fetch_method": "webfetch",
            "status_code": 503,
            "error_class": "transport-5xx",
            "error_message": "Sophos X-Ops featured-blog feed returned HTTP exit-1 (feed parse failure); rotation-priority candidate (3 runs failing)",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "none — no in-window Sophos content recovered",
            "covered_anyway": False
        }
    ],
    "items_published": 18,
    "items_dropped_by_verification": 0,
    "deep_dive": "storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain",
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {
        "iterations": []
    }
}


def main():
    with open(RUN_LOG) as f:
        data = json.load(f)
    runs = data.get("runs", [])

    # Idempotent retry: replace existing record with same run_id
    found = False
    for i, r in enumerate(runs):
        if r.get("run_id") == RUN_ID:
            runs[i] = record
            found = True
            print(f"Updated existing run record at index {i}")
            break
    if not found:
        runs.append(record)
        print(f"Appended new run record (total runs={len(runs)})")

    # Cap at 90
    if len(runs) > 90:
        runs = runs[-90:]
    data["runs"] = runs

    with open(RUN_LOG, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main()
