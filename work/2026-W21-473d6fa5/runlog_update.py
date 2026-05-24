#!/usr/bin/env python3
"""Append/update the weekly 2026-W21 run_log record. Idempotent on run_id."""
import json

RUN_ID = "2026-W21-473d6fa5"
rl = json.load(open("state/run_log.json"))
runs = rl["runs"]

started = open("work/2026-W21-473d6fa5/main.started_at").read().strip()
ended = open("work/2026-W21-473d6fa5/main.ended_at").read().strip()

def to_s(ts):
    import datetime
    return int(datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").timestamp())

duration = to_s(ended) - to_s(started)

rec = {
    "run_id": RUN_ID,
    "date": "2026-05-24",
    "iso_week": "2026-W21",
    "kind": "weekly",
    "started": started,
    "completed": ended,
    "duration_seconds": duration,
    "model": "Claude Opus 4.7",
    "model_id": "claude-opus-4-7",
    "prompt_version": "v2.59",
    "sub_agents": {
        "W1": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-24T22:15:30Z",
            "ended_at": "2026-05-24T22:21:56Z",
            "duration_seconds": 386,
            "sources_attempted": ["bleepingcomputer","hackernews","therecord","securityweek","unit42","talos","eset","mandiant-gtig","msft-ti","checkpoint-research","rapid7-research","vulncheck","sophos-xops","trendmicro-research","databreaches-net"],
            "sources_used": ["securityweek","helpnetsecurity","unit42"],
            "items_returned": 2,
            "returned": True,
            "telemetry": {"webfetch_calls": 9, "websearch_calls": 18, "bridge_fetches": 8},
        },
        "W2": {
            "model": "Claude Sonnet 4.6",
            "model_id": "claude-sonnet-4-6",
            "started_at": "2026-05-24T22:15:52Z",
            "ended_at": "2026-05-24T22:24:42Z",
            "duration_seconds": 530,
            "sources_attempted": ["ncsc-ch-security-hub","ncsc-ch-incidents","anssi-fr","bsi-de","cert-eu","enisa","edpb","ico-uk","csirt-acn-it","us-treasury-ofac","cisa-news","inside-it-ch","heise-sec"],
            "sources_used": ["us-treasury-ofac"],
            "items_returned": 1,
            "returned": True,
            "telemetry": {"webfetch_calls": 8, "websearch_calls": 15, "bridge_fetches": 7},
        },
    },
    "fetch_failures": [
        {
            "id": "cyble-eu-threat-landscape",
            "url_tried": "https://cyble.com/threat-intelligence-reports/",
            "fetch_method": "webfetch",
            "status_code": 503,
            "error_class": "transport-503",
            "error_message": "W1: 503 on rotation-priority source; date unverifiable; dropped (no in-window content lost)",
            "attempted_methods": ["webfetch"],
            "mitigation_applied": "none — quarterly-report axis covered via Verizon/Rapid7/Check Point",
            "covered_anyway": True,
        }
    ],
    "bridge_uses": [
        {"id": "github-blog", "method": "bridge:feed", "outcome": "200 — GitHub post-incident blog item"},
        {"id": "ico-uk", "method": "bridge", "outcome": "200"},
    ],
    "items_published": 39,
    "items_dropped_by_verification": 0,
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {"iterations": []},
}

# idempotent on run_id
idx = next((i for i, r in enumerate(runs) if r.get("run_id") == RUN_ID), None)
if idx is None:
    runs.append(rec)
    print("run_log: appended new record", RUN_ID)
else:
    runs[idx] = rec
    print("run_log: updated existing record", RUN_ID)

rl["last_updated"] = "2026-05-24"
json.dump(rl, open("state/run_log.json", "w"), indent=2, ensure_ascii=False)
open("state/run_log.json", "a").write("\n")
print("duration_seconds =", duration)
