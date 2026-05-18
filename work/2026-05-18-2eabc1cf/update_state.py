#!/usr/bin/env python3
"""Phase 5 state update — appends today's coverage to covered_items / cves_seen /
deep_dive_history / run_log."""
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TODAY = "2026-05-18"
BRIEF_PATH = "briefs/2026-05-18.md"
RUN_ID = "2026-05-18-2eabc1cf"

# ------------------------------------------------------------------
# covered_items.json — append per-H3 appearance records
# ------------------------------------------------------------------
ci_path = REPO / "state" / "covered_items.json"
with ci_path.open() as fh:
    ci = json.load(fh)

# Build lookup
by_key = {it["key"]: it for it in ci["items"]}

# New today: THORChain item
thor_key = "item:thorchain-gg20-tss-vault-drain-11m-nine-chains-switzerland"
thor_appearances = [
    {
        "date": TODAY,
        "section": "tldr",
        "brief_path": BRIEF_PATH,
        "delta_summary": "TL;DR bullet — $11M drained across nine chains via GG20 TSS implementation flaw; user funds unaffected, treasury recovery portal live.",
    },
    {
        "date": TODAY,
        "section": "active_threats",
        "brief_path": BRIEF_PATH,
        "delta_summary": "First coverage. Switzerland-incorporated cross-chain liquidity protocol. Malicious newly-churned validator leaked vault key shards gradually during GG20 keygen/signing rounds, then forged outbound signatures. TRM Labs traced to two-address cluster; Chainalysis linked attacker-controlled wallets via Monero/Hyperliquid pre-staging. No actor attribution. Treasury recovery portal live (claims deadline 2026-06-04).",
    },
]
if thor_key not in by_key:
    ci["items"].append({
        "key": thor_key,
        "type": "incident",
        "title": "THORChain GG20 Threshold Signature Scheme vault drain — ~$11M across nine chains (Switzerland-incorporated)",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain",
        "appearances": thor_appearances,
    })
else:
    by_key[thor_key]["last_covered"] = TODAY
    by_key[thor_key]["appearances"].extend(thor_appearances)

# New today: Tycoon2FA deep dive
tyc_key = "item:tycoon2fa-oauth-device-authorization-grant-microsoft-365-post-takedown"
tyc_appearances = [
    {
        "date": TODAY,
        "section": "tldr",
        "brief_path": BRIEF_PATH,
        "delta_summary": "TL;DR bullet — kit rebuilt post-March-2026 takedown; pivots AiTM → OAuth Device Authorization Grant abuse; BunnyCDN.",
    },
    {
        "date": TODAY,
        "section": "deep_dive",
        "brief_path": BRIEF_PATH,
        "delta_summary": "Deep dive — Tycoon2FA OAuth Device Authorization Grant abuse on Microsoft 365. Four-layer browser chain → fake CAPTCHA → victim pastes attacker device code into microsoft.com/devicelogin. MFA fires on real Microsoft endpoint; tokens issued to attacker. Microsoft Authentication Broker AppId 29d9ed98-a469-4536-ade2-f981bc1d605e. T1528 / T1550.001 / T1078.004. Hardening: CA block device-code flow; FIDO2 phishing-resistant MFA; CAE.",
    },
    {
        "date": TODAY,
        "section": "action_items",
        "brief_path": BRIEF_PATH,
        "delta_summary": "Action: block OAuth Device Code flow tenant-wide in Entra Conditional Access where not operationally required.",
    },
]
if tyc_key not in by_key:
    ci["items"].append({
        "key": tyc_key,
        "type": "campaign",
        "title": "Tycoon2FA PhaaS post-March-2026-takedown — OAuth Device Authorization Grant abuse on Microsoft 365",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing",
        "appearances": tyc_appearances,
    })
else:
    by_key[tyc_key]["last_covered"] = TODAY
    by_key[tyc_key]["appearances"].extend(tyc_appearances)

# CVE-2026-42897 — UPDATE + immediate action
cve_42897 = by_key["CVE-2026-42897"]
cve_42897["last_covered"] = TODAY
cve_42897["appearances"].extend([
    {
        "date": TODAY,
        "section": "tldr",
        "brief_path": BRIEF_PATH,
        "delta_summary": "TL;DR bullet — Exchange Team Blog 2026-05-17 update confirms EM Service auto-mitigation requires outbound HTTPS to officemitigations.microsoft.com.",
    },
    {
        "date": TODAY,
        "section": "immediate_actions",
        "brief_path": BRIEF_PATH,
        "delta_summary": "Immediate Action — verify EEMS service active AND outbound connectivity to officemitigations.microsoft.com from every on-prem Exchange Mailbox host.",
    },
    {
        "date": TODAY,
        "section": "updates",
        "brief_path": BRIEF_PATH,
        "delta_summary": "UPDATE — Exchange Team Blog 2026-05-17 clarifies EM Service URL-Rewrite M2.1.x mitigation only auto-applies when Exchange host has outbound HTTPS connectivity to officemitigations.microsoft.com. Segmented environments may be silently unprotected. No permanent patch.",
    },
    {
        "date": TODAY,
        "section": "action_items",
        "brief_path": BRIEF_PATH,
        "delta_summary": "Action: verify EEMS health on every Exchange Mailbox host; apply EOMT.ps1 manually on segmented hosts.",
    },
])

# CVE-2026-42945 — UPDATE
cve_42945 = by_key["CVE-2026-42945"]
cve_42945["last_covered"] = TODAY
cve_42945["appearances"].extend([
    {
        "date": TODAY,
        "section": "tldr",
        "brief_path": BRIEF_PATH,
        "delta_summary": "TL;DR bullet — VulnCheck honeypot telemetry confirms in-the-wild exploitation 2026-05-17.",
    },
    {
        "date": TODAY,
        "section": "updates",
        "brief_path": BRIEF_PATH,
        "delta_summary": "UPDATE — VulnCheck honeypot telemetry confirmed active exploitation 2026-05-17. Promoted from PoC-public to actively-exploited. Patches: NGINX OS 1.30.1 / 1.31.0; Plus R32 P6, R36 P4, 37.0.0.",
    },
    {
        "date": TODAY,
        "section": "action_items",
        "brief_path": BRIEF_PATH,
        "delta_summary": "Action: patch NGINX 1.30.0 → 1.30.1 / Plus R34 P2 immediately on internet-exposed instances; convert unnamed PCRE captures to named as interim mitigation.",
    },
])

# CVE-2026-0300 — UPDATE
cve_0300 = by_key["CVE-2026-0300"]
cve_0300["last_covered"] = TODAY
cve_0300["appearances"].append({
    "date": TODAY,
    "section": "updates",
    "brief_path": BRIEF_PATH,
    "delta_summary": "UPDATE — Palo Alto PSIRT revised 2026-05-16 with retimed fix-release schedule for 10.2.13-h21 (May 16) and 10.2.16-h7 (May 14). Wave-2 patch target remains 2026-05-28. Active exploitation continues.",
})
cve_0300["appearances"].append({
    "date": TODAY,
    "section": "action_items",
    "brief_path": BRIEF_PATH,
    "delta_summary": "Action: inventory PAN-OS builds; if 10.2.13-h21 or 10.2.16-h7, verify Captive Portal mitigation remains active until wave-2 patch.",
})

with ci_path.open("w") as fh:
    json.dump(ci, fh, indent=2, ensure_ascii=False)

# ------------------------------------------------------------------
# cves_seen.json — bump last_seen
# ------------------------------------------------------------------
cv_path = REPO / "state" / "cves_seen.json"
with cv_path.open() as fh:
    cv = json.load(fh)

bumped = []
for cve_id in ("CVE-2026-42897", "CVE-2026-42945", "CVE-2026-0300"):
    for entry in cv["cves"]:
        if entry["id"] == cve_id:
            entry["last_seen"] = TODAY
            bumped.append(cve_id)
            break

with cv_path.open("w") as fh:
    json.dump(cv, fh, indent=2, ensure_ascii=False)
print(f"cves bumped: {bumped}")

# ------------------------------------------------------------------
# deep_dive_history.json — append today's deep dive
# ------------------------------------------------------------------
dd_path = REPO / "state" / "deep_dive_history.json"
with dd_path.open() as fh:
    dd = json.load(fh)

dd["entries"].append({
    "date": TODAY,
    "category": "identity-infra",
    "title": "Tycoon2FA after the March 2026 takedown — OAuth Device Authorization Grant abuse on Microsoft 365",
    "primary_cve": None,
    "brief_path": BRIEF_PATH,
})
# Cap at 30 most recent
dd["entries"] = dd["entries"][-30:]
dd["last_updated"] = TODAY

with dd_path.open("w") as fh:
    json.dump(dd, fh, indent=2, ensure_ascii=False)

print("state updates: covered_items.json, cves_seen.json, deep_dive_history.json")
