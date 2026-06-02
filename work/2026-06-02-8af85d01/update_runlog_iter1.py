#!/usr/bin/env python3
import json, pathlib
ROOT = pathlib.Path("/home/user/ctipilot")
p = ROOT / "state/run_log.json"
rl = json.loads(p.read_text())
rec = next(r for r in rl["runs"] if r["run_id"] == "2026-06-02-8af85d01")

iter1 = {
    "n": 1,
    "model": "Anthropic Claude Opus 4.8",
    "model_id": "claude-opus-4-8",
    "started_at": "2026-06-02T04:41:03Z",
    "ended_at": "2026-06-02T04:44:05Z",
    "duration_seconds": 182,
    "verdict": "NEEDS_FIXES",
    "truth": 2,
    "editorial": 0,
    "advisory": 3,
    "findings": [
        {"code": "F3", "category": "claim-not-supported", "section": "trending-vulnerabilities",
         "item": "CVE-2026-8931 — Disig Web Signer",
         "url_or_quote": "https://www.disig.sk/en/news/important-update-of-the-web-signer-application/",
         "summary": "Disig vendor advisory does not itself state CVE/RCE/CVSS 9.4/eIDAS context; those rest on EUVD which verifier saw as empty SPA shell.",
         "remediation_applied": "Re-anchored item to ENISA EUVD EUVD-2026-33648 as primary (CVE/RCE/CVSS 9.4/SK-CERT confirmed via enisa-euvd bridge re-fetch); dropped unsourced specifics (slovensko.sk, primary-QTSP, researcher name, eIDAS-legal framing); Disig advisory demoted to corroborating.",
         "remediation_outcome": "fixed-clean"},
        {"code": "F13", "category": "analytical-link-as-fact", "section": "deep-dive",
         "item": "Operation Dragon Weave",
         "url_or_quote": "Seqrite ... tooling overlaps it links to SteppeDriver and UNC5221",
         "summary": "Seqrite primary names no group / never mentions SteppeDriver/UNC5221; that grouping is from The Hacker News roundup.",
         "remediation_applied": "Re-attributed the SteppeDriver/UNC5221 overlap to The Hacker News (with inline link); kept Seqrite's China-nexus as moderate-confidence, no-named-group.",
         "remediation_outcome": "fixed-clean"},
        {"code": "F9", "category": "surface-contradiction", "section": "active-threats",
         "item": "Miasma worm — Red Hat npm",
         "url_or_quote": "~80,000 weekly downloads (Wiz) vs 116,991 (Aikido)",
         "summary": "Brief silently used Wiz's ~80k figure; Aikido states ~117k for the same clause.",
         "remediation_applied": "Surfaced both figures with attribution (Wiz ~80,000; Aikido ~117,000).",
         "remediation_outcome": "fixed-clean"},
        {"code": "F11", "category": "editorial-advisory", "section": "trending-vulnerabilities",
         "item": "CVE-2026-8732 — WP Maps Pro",
         "url_or_quote": "BleepingComputer date / CVSS-9.8 attribution",
         "summary": "BleepingComputer article dated 2026-05-31 (not 06-01); CVSS 9.8 carried by THN not BleepingComputer.",
         "remediation_applied": "Corrected BleepingComputer inline date to 2026-05-31; attributed CVSS 9.8 to The Hacker News.",
         "remediation_outcome": "fixed-clean"},
        {"code": "F11", "category": "editorial-advisory", "section": "updates",
         "item": "Charter §4 UPDATE — ShinyHunters",
         "url_or_quote": "vishing/Entra/Salesforce chain",
         "summary": "Chain not in cited Security Affairs source but valid as prior-coverage callback.",
         "remediation_applied": "Reframed the vishing/Entra/Salesforce chain explicitly as established prior-coverage callback rather than a claim from the cited source.",
         "remediation_outcome": "fixed-clean"},
    ],
    "telemetry": {"webfetch_calls": 10, "websearch_calls": 0, "bridge_fetches": 1, "urls_checked": 11},
}

rec["verification"] = {"iterations": [iter1]}
rec["verification_iterations"] = 1
rec["verification_residual_count"] = 0  # provisional; finalised at loop end
rl["last_updated"] = "2026-06-02"
p.write_text(json.dumps(rl, indent=2, ensure_ascii=False) + "\n")
print("run_log: iter1 recorded; verification_iterations=1")
