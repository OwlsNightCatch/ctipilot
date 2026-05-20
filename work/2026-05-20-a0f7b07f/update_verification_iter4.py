#!/usr/bin/env python3
import json
from pathlib import Path

RUN_LOG = Path("state/run_log.json")
RUN_ID = "2026-05-20-a0f7b07f"

iter4 = {
    "n": 4,
    "model": "Claude Sonnet 4.6",
    "model_id": "claude-sonnet-4-6",
    "started_at": "2026-05-20T05:07:17Z",
    "ended_at": "2026-05-20T05:12:07Z",
    "duration_seconds": 290,
    "verdict": "NEEDS_FIXES",
    "truth": 1,
    "editorial": 0,
    "advisory": 0,
    "findings": [
        {
            "code": "F13",
            "category": "analytical-link-as-fact",
            "section": "tldr",
            "item": "TL;DR over-attributes Nx Console to Mini Shai-Hulud cluster",
            "url_or_quote": "actions-cool/issues-helper GitHub Action and Nx Console VS Code extension — confirmed linked to the Mini Shai-Hulud cluster",
            "summary": "Only actions-cool/issues-helper carries the Socket-attributed Mini Shai-Hulud cluster link (via domain overlap). The Nx Console primary (The Hacker News) attributes to 'a developer's compromised machine and leaked GitHub credentials' — no cluster attribution.",
            "remediation_applied": "Re-scoped the TL;DR sentence: 'actions-cool/issues-helper GitHub Action (exfil infrastructure overlapping with the Mini Shai-Hulud cluster per Socket) and Nx Console VS Code extension (stolen publisher credentials, no cluster attribution)'. Per PD-13 / F13 remediation guidance: present the link as the source's claim (Socket), not the brief's inference.",
            "remediation_outcome": "fixed-clean"
        }
    ],
    "telemetry": {
        "webfetch_calls": 12,
        "websearch_calls": 0,
        "bridge_fetches": 0,
        "urls_checked": 15
    }
}


def main():
    with open(RUN_LOG) as f:
        data = json.load(f)
    today = next(r for r in data["runs"] if r["run_id"] == RUN_ID)
    iterations = today.setdefault("verification", {"iterations": []})["iterations"]
    found = False
    for i, it in enumerate(iterations):
        if it.get("n") == 4:
            iterations[i] = iter4
            found = True
            break
    if not found:
        iterations.append(iter4)
    today["verification_iterations"] = len(iterations)
    final = iterations[-1]
    if final.get("verdict") == "CLEAN":
        today["verification_residual_count"] = 0
    else:
        today["verification_residual_count"] = final.get("truth", 0) + final.get("editorial", 0)
    with open(RUN_LOG, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"iter 4 appended; total={len(iterations)}; residual={today['verification_residual_count']}")


if __name__ == "__main__":
    main()
