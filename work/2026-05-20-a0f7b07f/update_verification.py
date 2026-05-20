#!/usr/bin/env python3
"""Append/update verification iteration N record on the today run."""
import json
from pathlib import Path
import sys

RUN_LOG = Path("state/run_log.json")
RUN_ID = "2026-05-20-a0f7b07f"


def upsert_iteration(record: dict):
    with open(RUN_LOG) as f:
        data = json.load(f)
    runs = data["runs"]
    today = next(r for r in runs if r["run_id"] == RUN_ID)
    today.setdefault("verification", {"iterations": []})
    iterations = today["verification"]["iterations"]
    n = record["n"]
    # idempotent — replace existing or append
    replaced = False
    for i, it in enumerate(iterations):
        if it.get("n") == n:
            iterations[i] = record
            replaced = True
            break
    if not replaced:
        iterations.append(record)

    # Maintain top-level fields
    today["verification_iterations"] = len(iterations)

    # Compute residual count: 0 if final iteration CLEAN; else truth+editorial of final
    final = iterations[-1]
    if final.get("verdict") == "CLEAN":
        today["verification_residual_count"] = 0
    else:
        today["verification_residual_count"] = final.get("truth", 0) + final.get("editorial", 0)

    with open(RUN_LOG, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    action = "replaced" if replaced else "appended"
    print(f"verification iter {n}: {action}; total iterations={len(iterations)}; residual={today['verification_residual_count']}")


if __name__ == "__main__":
    # iter 1
    iter1 = {
        "n": 1,
        "model": "Claude Opus 4.7 (1M context)",
        "model_id": "claude-opus-4-7[1m]",
        "started_at": "2026-05-20T04:35:43Z",
        "ended_at": "2026-05-20T04:42:47Z",
        "duration_seconds": 424,
        "verdict": "NEEDS_FIXES",
        "truth": 3,
        "editorial": 1,
        "advisory": 0,
        "findings": [
            {
                "code": "F4",
                "category": "hallucinated-fact",
                "section": "research",
                "item": "Cisco Talos demo.pdb BadIIS — campaign scope claims",
                "url_or_quote": "over 1,800 Windows IIS servers compromised globally; Thailand, Vietnam, India, Pakistan, Japan",
                "summary": "Cited Talos article does not state any specific server count and does not name those countries; says 'Asia-Pacific region (along with a few in South Africa, Europe, North America)'.",
                "remediation_applied": "Replaced specific count + country list with the verbatim Talos phrasing ('Asia-Pacific region with smaller number in South Africa, Europe, and North America').",
                "remediation_outcome": "fixed-clean"
            },
            {
                "code": "F3",
                "category": "claim-not-supported",
                "section": "active-threats",
                "item": "Fox Tempest pricing / Telegram / Google Form sentence",
                "url_or_quote": "$5,000-$9,000 per signing run via Google Form; 'EV Certs for Sale by SamCodeSign' Telegram channel attributed to The Record",
                "summary": "Specifics come from Microsoft Threat Intelligence blog; The Record citation does not contain them. Re-attribute.",
                "remediation_applied": "Removed the unsupported pricing/Telegram/Google Form specifics; restructured paragraph so Microsoft TI is the cited primary for the technical details and The Record is corroboration for the DCU legal action.",
                "remediation_outcome": "fixed-clean"
            },
            {
                "code": "F3",
                "category": "claim-not-supported",
                "section": "trending-vulnerabilities",
                "item": "vm2 patched-version claim",
                "url_or_quote": "Full patch: upgrade to vm2 3.11.2",
                "summary": "BSI WID-SEC-2026-1583 (cited primary) lists fixed version <3.11.4; brief asserts 3.11.2.",
                "remediation_applied": "Updated brief + § 6 action item to vm2 3.11.4 per BSI primary; added § 7 contradiction line surfacing the 3.11.2 vs 3.11.4 discrepancy.",
                "remediation_outcome": "fixed-clean"
            },
            {
                "code": "F14",
                "category": "quantifier-without-source",
                "section": "trending-vulnerabilities",
                "item": "DirtyDecrypt CVSS 7.5 / CWE-122",
                "url_or_quote": "(CVSS 7.5, CWE-122)",
                "summary": "Primary sources (Moselwal, BleepingComputer) don't state CVSS 7.5 or CWE-122; only Hacker News (Additional source) carries 7.5.",
                "remediation_applied": "Dropped CVSS/CWE inline early in body; added a half-sentence noting Hacker News carries CVSS 7.5 while Moselwal characterises LPE class as 7.8-8.1 range without settled NVD score. CVSS 7.5 retained in footer field (matched to Hacker News).",
                "remediation_outcome": "fixed-clean"
            },
            {
                "code": "F12",
                "category": "single-source-flag-missing",
                "section": "active-threats",
                "item": "Fox Tempest — effectively single-organisational-source",
                "url_or_quote": "Two of three sources are Microsoft properties",
                "summary": "Microsoft Threat Intelligence + Microsoft On the Issues + corroborating The Record; effectively single-organisational primary.",
                "remediation_applied": "Added § 7 Verification Notes line acknowledging single-organisational-source posture; vendor-as-primary carve-out per PD-5 applies (Microsoft is disclosing party).",
                "remediation_outcome": "fixed-clean"
            }
        ],
        "telemetry": {
            "webfetch_calls": 17,
            "websearch_calls": 3,
            "bridge_fetches": 6,
            "urls_checked": 22
        }
    }
    upsert_iteration(iter1)
