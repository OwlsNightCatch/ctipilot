#!/usr/bin/env python3
import json
from pathlib import Path

RUN_LOG = Path("state/run_log.json")
RUN_ID = "2026-05-20-a0f7b07f"

iter3 = {
    "n": 3,
    "model": "Claude Opus 4.7 (1M context)",
    "model_id": "claude-opus-4-7[1m]",
    "started_at": "2026-05-20T04:57:50Z",
    "ended_at": "2026-05-20T05:02:29Z",
    "duration_seconds": 279,
    "verdict": "NEEDS_FIXES",
    "truth": 2,
    "editorial": 0,
    "advisory": 0,
    "findings": [
        {
            "code": "F4",
            "category": "hallucinated-fact",
            "section": "active-threats",
            "item": "Fox Tempest — '~1,000 accounts' takedown count not in sources",
            "url_or_quote": "took down ~1,000 accounts",
            "summary": "Microsoft TI confirms 1,000+ certificates; On the Issues blog references 'hundreds of fraudulent Microsoft accounts' Fox Tempest created. Likely conflation with certificates count.",
            "remediation_applied": "Dropped the '~1,000 accounts' clause; clarified language to 'disabled hundreds of Cloudzy-hosted VMs that Fox Tempest used as its delivery surface'.",
            "remediation_outcome": "fixed-clean"
        },
        {
            "code": "F3",
            "category": "claim-not-supported",
            "section": "deep-dive",
            "item": "Storm-2949 — Key Vault role misattributed as Contributor; Microsoft says Owner",
            "url_or_quote": "pivoted to Azure Key Vault using the Key Vault Contributor role",
            "summary": "Microsoft Storm-2949 blog verbatim: 'Part of the compromised user's Azure RBAC permissions was the privileged Owner role over a specific Key Vault'. Brief misattributed in both Phase 3 narrative and the hardening bullet.",
            "remediation_applied": "Replaced 'Key Vault Contributor' with 'Owner' in the Phase 3 narrative; updated hardening bullet to discuss both Owner and Key Vault Contributor (both confer management-plane mutation). Updated § 6 Action Item to include Owner role.",
            "remediation_outcome": "fixed-clean"
        }
    ],
    "telemetry": {
        "webfetch_calls": 16,
        "websearch_calls": 0,
        "bridge_fetches": 1,
        "urls_checked": 16
    }
}


def main():
    with open(RUN_LOG) as f:
        data = json.load(f)
    today = next(r for r in data["runs"] if r["run_id"] == RUN_ID)
    iterations = today.setdefault("verification", {"iterations": []})["iterations"]
    found = False
    for i, it in enumerate(iterations):
        if it.get("n") == 3:
            iterations[i] = iter3
            found = True
            break
    if not found:
        iterations.append(iter3)
    today["verification_iterations"] = len(iterations)
    final = iterations[-1]
    if final.get("verdict") == "CLEAN":
        today["verification_residual_count"] = 0
    else:
        today["verification_residual_count"] = final.get("truth", 0) + final.get("editorial", 0)
    with open(RUN_LOG, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"iter 3 appended; total={len(iterations)}; residual={today['verification_residual_count']}")


if __name__ == "__main__":
    main()
