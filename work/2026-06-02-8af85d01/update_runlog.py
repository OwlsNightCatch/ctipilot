#!/usr/bin/env python3
"""Append run_log entry for 2026-06-02-8af85d01 (verification block provisional)."""
import json, pathlib
ROOT = pathlib.Path("/home/user/ctipilot")
p = ROOT / "state/run_log.json"
rl = json.loads(p.read_text())

RUN_ID = "2026-06-02-8af85d01"
started = (ROOT / "work" / RUN_ID / "main.started_at").read_text().strip()
completed = (ROOT / "work" / RUN_ID / "main.ended_at").read_text().strip()

def secs(a, b):
    from datetime import datetime
    f = "%Y-%m-%dT%H:%M:%SZ"
    return int((datetime.strptime(b, f) - datetime.strptime(a, f)).total_seconds())

record = {
    "run_id": RUN_ID,
    "date": "2026-06-02",
    "kind": "daily",
    "started": started,
    "completed": completed,
    "duration_seconds": secs(started, completed),
    "model": "Claude Opus 4.8",
    "model_id": "claude-opus-4-8",
    "prompt_version": "v2.60",
    "sub_agents": {
        "S1": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6",
               "started_at": "2026-06-02T04:11:20Z", "ended_at": "2026-06-02T04:16:04Z", "duration_seconds": 284,
               "sources_attempted": ["cisa-kev", "bsi-de", "advisories-ncsc-nl", "anssi-fr", "cert-eu", "rapid7-research", "watchtowr", "projectzero", "shadowserver", "vulncheck", "oracle-cpu", "wiz-blog", "enisa"],
               "sources_used": ["wiz-blog", "bleepingcomputer", "hackernews"], "items_returned": 4, "returned": True,
               "telemetry": {"webfetch_calls": 14, "websearch_calls": 9, "bridge_fetches": 12}},
        "S2": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6",
               "started_at": "2026-06-02T04:11:33Z", "ended_at": "2026-06-02T04:21:09Z", "duration_seconds": 576,
               "sources_attempted": ["heise-sec", "bsi-de", "cert-pl", "cert-eu", "anssi-fr", "enisa", "ncsc-ch-security-hub", "cnil-fr", "ico-uk", "inside-it-ch", "csirt-acn-it", "ccb-belgium"],
               "sources_used": ["bleepingcomputer", "helpnetsecurity", "securityweek", "heise-sec", "bsi-de", "cert-pl", "enisa", "ccb-belgium"], "items_returned": 6, "returned": True,
               "telemetry": {"webfetch_calls": 14, "websearch_calls": 11, "bridge_fetches": 9}},
        "S3": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6",
               "started_at": "2026-06-02T04:11:46Z", "ended_at": "2026-06-02T04:15:55Z", "duration_seconds": 249,
               "sources_attempted": ["sekoia", "checkpoint-research", "elastic-seclabs", "sophos-xops", "therecord", "hackernews", "bleepingcomputer", "unit42", "talos", "wiz-blog", "dfirreport", "infosec-magazine"],
               "sources_used": ["sekoia", "bleepingcomputer", "hackernews", "infosec-magazine", "wiz-blog"], "items_returned": 8, "returned": True,
               "telemetry": {"webfetch_calls": 11, "websearch_calls": 4, "bridge_fetches": 14}},
        "S4": {"model": "Claude Sonnet 4.6", "model_id": "claude-sonnet-4-6",
               "started_at": "2026-06-02T04:11:57Z", "ended_at": "2026-06-02T04:15:16Z", "duration_seconds": 199,
               "sources_attempted": ["sec-disclosures-edgar", "ico-uk", "cnil-fr", "edpb", "databreaches-net", "krebs", "bleepingcomputer", "securityaffairs", "troyhunt", "therecord"],
               "sources_used": ["krebs", "securityaffairs", "troyhunt", "bleepingcomputer"], "items_returned": 4, "returned": True,
               "telemetry": {"webfetch_calls": 18, "websearch_calls": 5, "bridge_fetches": 14}},
    },
    "fetch_failures": [
        {"id": "sec-disclosures-edgar", "url_tried": "https://efts.sec.gov/LATEST/search-index?q=%22Item+1.05%22&forms=8-K&startdt=2026-05-31&enddt=2026-06-02",
         "fetch_method": "bridge:url", "status_code": 500, "error_class": "transport-5xx",
         "error_message": "EDGAR EFTS full-text search returned HTTP 500 for both date windows tried",
         "attempted_methods": ["bridge:url"], "mitigation_applied": "none — no 8-K Item 1.05 filings retrievable", "covered_anyway": False},
        {"id": "sophos-xops", "url_tried": "https://www.sophos.com/en-us/blog",
         "fetch_method": "webfetch", "status_code": 503, "error_class": "transport-5xx",
         "error_message": "Sophos blog feed + news firehose returned HTTP 503 (rotation-priority source)",
         "attempted_methods": ["webfetch"], "mitigation_applied": "none — Wayback time-boxed; no Sophos items this run", "covered_anyway": False},
        {"id": "cert-fr-actualite", "url_tried": "https://www.cert.ssi.gouv.fr/",
         "fetch_method": "webfetch", "status_code": 200, "error_class": "other",
         "error_message": "CERT-FR actualites RSS stalled — most recent item dated 2025-10-27; no in-window content",
         "attempted_methods": ["webfetch"], "mitigation_applied": "none — feed not updating", "covered_anyway": False},
    ],
    "bridge_uses": [
        {"id": "cisa-kev", "method": "bridge:cisa-kev", "outcome": "ok"},
        {"id": "enisa", "method": "bridge:enisa-euvd.recent", "outcome": "ok"},
        {"id": "bsi-de", "method": "bridge:bsi-csaf", "outcome": "ok"},
        {"id": "ncsc-ch-security-hub", "method": "bridge:ncsc-csh.recent", "outcome": "ok"},
    ],
    "items_published": 12,
    "items_dropped_by_verification": 0,
    "deep_dive": "operation-dragon-weave",
    "verification_iterations": 0,
    "verification_residual_count": 0,
    "verification": {"iterations": []},
}

runs = rl["runs"]
existing = next((i for i, r in enumerate(runs) if r.get("run_id") == RUN_ID), None)
if existing is not None:
    runs[existing] = record
    print(f"run_log: updated existing record at index {existing}")
else:
    runs.append(record)
    print("run_log: appended new record")
rl["runs"] = runs[-90:]
rl["last_updated"] = "2026-06-02"
p.write_text(json.dumps(rl, indent=2, ensure_ascii=False) + "\n")
print(f"run_log: now {len(rl['runs'])} runs; duration={record['duration_seconds']}s")
