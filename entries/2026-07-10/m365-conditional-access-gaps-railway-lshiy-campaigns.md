---
schema: 1
kind: research
horizon: operational
title: >
  Two 2026 M365 account-takeover campaigns (Railway device-code phishing, LSHIY ROPC spray) beat
  Conditional Access without breaking MFA
headline: >
  Huntress: device-code phishing and ROPC token-spray defeat M365 tenants by routing around the
  auth paths Conditional Access actually inspects
summary: >
  Huntress published a comparative root-cause analysis of two 2026 Microsoft 365 account-takeover
  campaigns that both bypassed Conditional Access policies requiring MFA — not by defeating MFA
  but by using auth flows CA rarely covers. "Railway" (March 2026, 344 orgs incl. Germany) used
  device-code phishing to harvest 90-day OAuth tokens; "LSHIY" (June 2026, 78 accounts across 64
  orgs) ran 81M+ ROPC login attempts against Azure CLI through the /token endpoint. Of the 78
  LSHIY-compromised accounts, 55 had active CA policies requiring MFA that failed because of
  scoping gaps. Every M365 tenant should block the device-code flow and ensure CA covers all cloud
  apps and all client app types including legacy auth.
discovered_at: "2026-07-10T04:36:19Z"
updated_at: "2026-08-01T04:24:59Z"
event_date: 2026-07-09
run_id: 2026-07-10T0409Z-intel
priority: high
immediate_action: null
tags:
  - identity
  - phishing
  - cloud
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
  - finance
  - healthcare
  - telco
entities:
  - "campaign:lshiy-ropc-azure-cli-password-spray-2026"
  - "campaign:railway-device-code-phishing-m365-2026"
techniques:
  - T1528
  - T1110.003
  - T1078.004
  - T1556.006
  - T1566.002
  - T1550.001
affected_products:
  - Microsoft 365
  - Microsoft Entra ID
  - Azure CLI
cves: []
sources:
  - url: "https://www.huntress.com/blog/conditional-access-misconfigurations"
    publisher: Huntress
    date: 2026-07-09
    role: primary
  - url: "https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html"
    publisher: The Hacker News
    date: 2026-07-01
    role: corroborating
  - url: "https://www.huntress.com/blog/lshiy-password-spray-attack"
    publisher: Huntress
    date: 2026-06-30
    role: corroborating
  - url: "https://www.huntress.com/blog/device-code-phishing-evolving-threats"
    publisher: Huntress
    date: 2026-07-31
    role: primary
closed_sources: []
evidence:
  - quote: "Device code phishing is effective because it doesn't try to beat MFA. It sidesteps it."
    publisher: Huntress
  - quote: "Of the 78 compromised accounts, 55 had active Conditional Access policies requiring MFA."
    publisher: Huntress
  - quote: "One glaring error here is that legacy protocols like ROPC can bypass some poorly-configured CAPs entirely since they don't go through the authorization endpoint where policies are enforced."
    publisher: The Hacker News
  - quote: "Infrastructure reputation is holding too much weight in many defense stacks. When a login originates from a provider or autonomous system that is generally trusted across commercial controls, attackers get a window to operate. That window may be short, but in token abuse operations, short is often long enough."
    publisher: Huntress
  - quote: "Between July 3 and July 27, we saw 26 critical-severity incidents linked to BL Networks spanning 23 identities."
    publisher: Huntress
  - quote: Assume MFA alone is not enough when the attacker is abusing a legitimate Microsoft flow rather than stealing a password.
    publisher: Huntress
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
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
updates:
  - at: "2026-08-01T04:24:59Z"
    run_id: 2026-08-01T0409Z-intel
    type: update
    summary: >
      Huntress reported on 2026-07-31 that the Microsoft 365 device-code phishing it tracked earlier
      in 2026 on the Railway platform has a parallel second wave hosted on BL Networks, a VPS reseller
      operating since at least 2017 that also provides ordinary hosting. Suspicious M365
      authentication tied to it began on 2026-04-13 and continues; between 3 and 27 July, Huntress saw
      26 critical-severity incidents spanning 23 identities. The operational point is a detection one:
      researchers have flagged the provider's addresses before, but because it is generally trusted
      across commercial controls the operator still gets a window, and Huntress argues defenders
      should cluster successful sign-ins by provider-versus-user-context mismatch and device-code flow
      usage rather than lean on infrastructure reputation.
    fields:
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-08-01/device-code-phishing-bl-networks-second-wave-2026
migrated_from: null
---

Huntress compared two structurally different but strategically identical 2026 Microsoft 365 account-takeover campaigns, both of which got through tenants whose Conditional Access (CA) policies required MFA — because each used an authentication path CA typically does not inspect ([Huntress, 2026-07-09](https://www.huntress.com/blog/conditional-access-misconfigurations)). The "Railway" campaign (March 2026) abused Microsoft's OAuth device-code flow: attackers generate a legitimate device-authorization code, embed it in a lure, and collect the resulting OAuth token (valid up to 90 days) when the victim enters the code at the real Microsoft endpoint — the victim may complete MFA, but the token is already gone, so the flow sidesteps MFA rather than defeating it (`T1528`). The operation ran from clean Railway.com PaaS IP ranges with trusted reputation (three IPs accounted for ~84% of traffic), used construction-RFP lure themes and in some chains triple-wrapped URLs through Cisco, Trend Micro and Microsoft SafeLinks in sequence, and reached 344 organisations across the US, Canada, Australia, New Zealand and Germany before Huntress published; it was attributed to a commercial phishing-as-a-service operation Huntress tracks as EvilTokens — a subscription platform with a storefront, a support team and AI-assisted lure generation ([Huntress, 2026-07-09](https://www.huntress.com/blog/conditional-access-misconfigurations)).

The "LSHIY" campaign (active mid-June 2026) took the opposite approach: no phishing, just 81M+ login attempts from an IPv6 range against Azure CLI using the deprecated Resource Owner Password Credentials (ROPC) OAuth flow, which posts credentials straight to the `/token` endpoint and never touches the authorization endpoint where most CA policies are enforced (`T1110.003`, `T1078.004`, [The Hacker News, 2026-07-01](https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html)). It compromised at least 78 accounts across 64 organisations; the finding that matters for defenders is that 55 of those had active CA policies requiring MFA that failed for predictable scoping reasons (`T1556.006`): MFA scoped to specific apps such as Admin Portals but not "All Cloud Apps", so Azure CLI slipped through; MFA scoped to specific user groups that omitted the compromised accounts; MFA required only from "untrusted" locations, bypassed by an attacker IP that geolocated inconsistently to the US; and two policies left in report-only mode. Huntress notes one tenant had a CA policy explicitly named "Block Azure CLI" that did not, in fact, block Azure CLI.

**Defender takeaway:** MFA presence is not the control surface — CA policy *scope* is. Block the device-code flow tenant-wide (a victim who enters a code into the genuine Microsoft endpoint achieves nothing if the flow is disabled), and ensure MFA-requiring CA policies target all users, all cloud apps and all client app types including legacy/ROPC, backed by client-level strong-auth enforcement (`userStrongAuthClientAuthNRequired`) that blocks ROPC even with correct credentials. **Triage:** legitimate developer use of Azure CLI from a known device is the benign lookalike for the LSHIY pattern; the discriminators are volume (thousands of attempts), single-ASN concentration, and a successful legacy-auth/ROPC sign-in to a resource app with no interactive MFA event in the same session — and for device-code phishing, a device-code completion originating from something that is plainly not an input-constrained device.

## Update — 2026-08-01T04:24:59Z

The device-code phishing wave covered earlier as a Railway-hosted campaign is not a single episode that tapered off. Huntress reports a second, parallel 2026 wave on entirely different infrastructure, and the delta that matters is what kind of infrastructure it is.

Huntress states it "started seeing suspicious Microsoft 365 authentication activity linked to BL Networks on April 13, 2026, which continues as of this writing", initially from a single address, spreading across several subnets in May, and continuing into July: "between July 3 and July 27, we saw 26 critical-severity incidents linked to BL Networks spanning 23 identities" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). For the April window it records 533 events tied to one address, including 113 successful logins in a 48-hour span between 20 and 21 April ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress describes BL Networks as a VPS reseller "active since at least 2017, operating under ASN AS399629, according to Bushido Token Threat Intel" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

The distinction from the earlier wave is the delta. The Railway campaign, which Huntress attributes to the EvilTokens phishing-as-a-service platform, ran on a platform-as-a-service product; BL Networks "is a bit different because it also provides standard hosting", with legitimate small-hosting customers alongside the abuse ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress is careful not to overstate the blind spot — it notes that "cybersecurity researchers have frequently flagged its IP addresses because bad actors have used its servers for malicious campaigns as well", and closes that "the bigger lesson here is not that one provider is bad forever" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). The narrower and more useful claim is about weighting: "infrastructure reputation is holding too much weight in many defense stacks. When a login originates from a provider or autonomous system that is generally trusted across commercial controls, attackers get a window to operate. That window may be short, but in token abuse operations, short is often long enough" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress's broader argument is that defenders should stop tracking these as branded campaigns at all — "whether a campaign is discussed internally as Railway, EvilTokens, or potentially Kali365-aligned, the more durable lesson is that this is now an attack pattern" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

**Defender takeaway:** the original entry's controls stand — restrict the device-code flow, close the Conditional Access scoping gaps that let non-interactive flows past MFA requirements, and enable Continuous Access Evaluation so revocation takes effect quickly. What this wave adds is that an infrastructure-reputation feed will not tell you when the pattern recurs, so the detection has to be built on account context instead. Huntress's own recommended threshold is worth adopting as an internal rule rather than waiting for a vendor to classify the next provider: it flagged BL Networks on the strength of disproportionate device-code logins alone, and argues that when the evidence is that strong, "waiting for pristine attribution can become a luxury" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Its closing control set is to review and restrict device-code authentication where it is not required, monitor successful sign-ins from unusual infrastructure paired with device-code activity, investigate clusters of successful sign-in events from one autonomous system even when they do not individually score as high risk, revoke sessions and tokens quickly on suspicion, and "assume MFA alone is not enough when the attacker is abusing a legitimate Microsoft flow rather than stealing a password" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

**Triage:** a successful sign-in from a commodity hosting provider is not by itself an incident — remote workers use VPNs, and small suppliers legitimately host services there. The discriminating combination Huntress sets out is three-part and needs all three: the sign-in succeeded, it is tied to the device-code flow rather than an ordinary interactive or browser-based authentication, and the hosting provider makes no business sense for that particular user's normal working pattern. The strongest variant is cross-tenant — the same autonomous system appearing behind successful sign-ins for multiple unrelated identities or organisations in a short window, which reads as operational rather than coincidental. Because the flow itself is a genuine Microsoft authentication path and MFA may legitimately have been satisfied, neither the presence of MFA nor a clean risk score is evidence against the finding.
