---
schema: 1
kind: research
horizon: operational
title: "Two 2026 M365 account-takeover campaigns (Railway device-code phishing, LSHIY ROPC spray) beat Conditional Access without breaking MFA"
headline: "Huntress: device-code phishing and ROPC token-spray defeat M365 tenants by routing around the auth paths Conditional Access actually inspects"
summary: >
  Huntress published a comparative root-cause analysis of two 2026 Microsoft 365 account-takeover campaigns that both bypassed Conditional Access policies requiring MFA — not by defeating MFA but by using auth flows CA rarely covers. "Railway" (March 2026, 344 orgs incl. Germany) used device-code phishing to harvest 90-day OAuth tokens; "LSHIY" (June 2026, 78 accounts across 64 orgs) ran 81M+ ROPC login attempts against Azure CLI through the /token endpoint. Of the 78 LSHIY-compromised accounts, 55 had active CA policies requiring MFA that failed because of scoping gaps. Every M365 tenant should block the device-code flow and ensure CA covers all cloud apps and all client app types including legacy auth.
discovered_at: "2026-07-10T04:36:19Z"
event_date: "2026-07-09"
run_id: 2026-07-10T0409Z-intel
priority: high
immediate_action: null
tags: [identity, phishing, cloud, ai-abuse]
regions: [global]
sectors: [public-sector, finance, healthcare, telco]
entities: [campaign:lshiy-ropc-azure-cli-password-spray-2026, campaign:railway-device-code-phishing-m365-2026]
techniques: [T1528, T1110.003, T1078.004, T1556.006]
affected_products: ["Microsoft 365", "Microsoft Entra ID", "Azure CLI"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/conditional-access-misconfigurations"
    publisher: "Huntress"
    date: "2026-07-09"
    role: primary
  - url: "https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html"
    publisher: "The Hacker News"
    date: "2026-07-01"
    role: corroborating
  - url: "https://www.huntress.com/blog/lshiy-password-spray-attack"
    publisher: "Huntress"
    date: "2026-06-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Device code phishing is effective because it doesn't try to beat MFA. It sidesteps it."
    publisher: "Huntress"
  - quote: "Of the 78 compromised accounts, 55 had active Conditional Access policies requiring MFA."
    publisher: "Huntress"
  - quote: "One glaring error here is that legacy protocols like ROPC can bypass some poorly-configured CAPs entirely since they don't go through the authorization endpoint where policies are enforced."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Block the OAuth device-authorization (device-code) flow tenant-wide via Conditional Access, or restrict it to the named accounts that genuinely need it — this neutralises device-code phishing regardless of lure quality, because the token is never minted."
  - "Re-scope every MFA-requiring CA policy to 'All cloud apps' and 'All client app types' (including legacy/other clients), not a per-app or per-group allow-list — an omitted app such as Azure CLI is exactly what ROPC spray rides through."
  - "Enable client-level strong-auth enforcement (userStrongAuthClientAuthNRequired) to block ROPC flows from succeeding even with valid credentials, and audit for CA policies set to report-only that were never enforced."
  - "Hunt sign-in logs for successful ROPC/legacy-auth authentications to Azure resource apps with no corresponding interactive MFA challenge, and for device-code completion events not tied to a genuine input-constrained device."
migrated_from: null
---

Huntress compared two structurally different but strategically identical 2026 Microsoft 365 account-takeover campaigns, both of which got through tenants whose Conditional Access (CA) policies required MFA — because each used an authentication path CA typically does not inspect ([Huntress, 2026-07-09](https://www.huntress.com/blog/conditional-access-misconfigurations)). The "Railway" campaign (March 2026) abused Microsoft's OAuth device-code flow: attackers generate a legitimate device-authorization code, embed it in a lure, and collect the resulting OAuth token (valid up to 90 days) when the victim enters the code at the real Microsoft endpoint — the victim may complete MFA, but the token is already gone, so the flow sidesteps MFA rather than defeating it (`T1528`). The operation ran from clean Railway.com PaaS IP ranges with trusted reputation (three IPs accounted for ~84% of traffic), used construction-RFP lure themes and in some chains triple-wrapped URLs through Cisco, Trend Micro and Microsoft SafeLinks in sequence, and reached 344 organisations across the US, Canada, Australia, New Zealand and Germany before Huntress published; it was attributed to a commercial phishing-as-a-service operation Huntress tracks as EvilTokens — a subscription platform with a storefront, a support team and AI-assisted lure generation ([Huntress, 2026-07-09](https://www.huntress.com/blog/conditional-access-misconfigurations)).

The "LSHIY" campaign (active mid-June 2026) took the opposite approach: no phishing, just 81M+ login attempts from an IPv6 range against Azure CLI using the deprecated Resource Owner Password Credentials (ROPC) OAuth flow, which posts credentials straight to the `/token` endpoint and never touches the authorization endpoint where most CA policies are enforced (`T1110.003`, `T1078.004`, [The Hacker News, 2026-07-01](https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html)). It compromised at least 78 accounts across 64 organisations; the finding that matters for defenders is that 55 of those had active CA policies requiring MFA that failed for predictable scoping reasons (`T1556.006`): MFA scoped to specific apps such as Admin Portals but not "All Cloud Apps", so Azure CLI slipped through; MFA scoped to specific user groups that omitted the compromised accounts; MFA required only from "untrusted" locations, bypassed by an attacker IP that geolocated inconsistently to the US; and two policies left in report-only mode. Huntress notes one tenant had a CA policy explicitly named "Block Azure CLI" that did not, in fact, block Azure CLI.

**Defender takeaway:** MFA presence is not the control surface — CA policy *scope* is. Block the device-code flow tenant-wide (a victim who enters a code into the genuine Microsoft endpoint achieves nothing if the flow is disabled), and ensure MFA-requiring CA policies target all users, all cloud apps and all client app types including legacy/ROPC, backed by client-level strong-auth enforcement (`userStrongAuthClientAuthNRequired`) that blocks ROPC even with correct credentials. **Triage:** legitimate developer use of Azure CLI from a known device is the benign lookalike for the LSHIY pattern; the discriminators are volume (thousands of attempts), single-ASN concentration, and a successful legacy-auth/ROPC sign-in to a resource app with no interactive MFA event in the same session — and for device-code phishing, a device-code completion originating from something that is plainly not an input-constrained device.
