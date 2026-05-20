#!/usr/bin/env python3
"""Append iter 2 verification record."""
import json
from pathlib import Path

RUN_LOG = Path("state/run_log.json")
RUN_ID = "2026-05-20-a0f7b07f"

iter2 = {
    "n": 2,
    "model": "Claude Sonnet 4.6",
    "model_id": "claude-sonnet-4-6",
    "started_at": "2026-05-20T04:50:12Z",
    "ended_at": "2026-05-20T04:53:26Z",
    "duration_seconds": 194,
    "verdict": "NEEDS_FIXES",
    "truth": 1,
    "editorial": 0,
    "advisory": 0,
    "findings": [
        {
            "code": "F3",
            "category": "claim-not-supported",
            "section": "trending-vulnerabilities",
            "item": "vm2 H3 heading — stale 'patch to 3.11.2' inconsistent with body / action item / § 7 (all 3.11.4 per BSI)",
            "url_or_quote": "vm2 Node.js sandbox — ... sandbox escape to host RCE, patch to 3.11.2",
            "summary": "Heading drift from iter-1 remediation: body / § 6 / § 7 were updated to 3.11.4 (BSI WID-SEC-2026-1583 primary) but the H3 heading still read 'patch to 3.11.2'.",
            "remediation_applied": "Heading updated to 'upgrade to ≥ 3.11.4' (consistent with body, action item, § 7).",
            "remediation_outcome": "fixed-clean"
        }
    ],
    "telemetry": {
        "webfetch_calls": 4,
        "websearch_calls": 0,
        "bridge_fetches": 3,
        "urls_checked": 10
    }
}


def main():
    with open(RUN_LOG) as f:
        data = json.load(f)
    today = next(r for r in data["runs"] if r["run_id"] == RUN_ID)
    iterations = today.setdefault("verification", {"iterations": []})["iterations"]
    found = False
    for i, it in enumerate(iterations):
        if it.get("n") == 2:
            iterations[i] = iter2
            found = True
            break
    if not found:
        iterations.append(iter2)
    today["verification_iterations"] = len(iterations)
    final = iterations[-1]
    if final.get("verdict") == "CLEAN":
        today["verification_residual_count"] = 0
    else:
        today["verification_residual_count"] = final.get("truth", 0) + final.get("editorial", 0)
    with open(RUN_LOG, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"iter 2 appended; total={len(iterations)}; residual={today['verification_residual_count']}")


if __name__ == "__main__":
    main()
