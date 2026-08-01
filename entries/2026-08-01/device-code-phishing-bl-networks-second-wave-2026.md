---
schema: 1
kind: threat
horizon: operational
title: "M365 device-code phishing runs a second 2026 wave from a general-purpose VPS reseller — the same playbook on infrastructure that carries enough commercial trust to buy a window"
headline: "Huntress records a second device-code phishing wave on a VPS reseller whose general commercial trust buys the operator a working window"
summary: >
  Huntress reported on 2026-07-31 that the Microsoft 365 device-code phishing it tracked earlier in 2026 on the Railway
  platform has a parallel second wave hosted on BL Networks, a VPS reseller operating since at least 2017 that also
  provides ordinary hosting. Suspicious M365 authentication tied to it began on 2026-04-13 and continues; between 3 and
  27 July, Huntress saw 26 critical-severity incidents spanning 23 identities. The operational point is a detection one:
  researchers have flagged the provider's addresses before, but because it is generally trusted across commercial
  controls the operator still gets a window, and Huntress argues defenders should cluster successful sign-ins by
  provider-versus-user-context mismatch and device-code flow usage rather than lean on infrastructure reputation.
discovered_at: "2026-08-01T04:24:59Z"
event_date: "2026-07-31"
run_id: 2026-08-01T0409Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global]
sectors: [public-sector, finance, healthcare, telco]
entities: [campaign:railway-device-code-phishing-m365-2026]
techniques: [T1528, T1566.002, T1550.001, T1078.004]
affected_products: ["Microsoft 365", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/device-code-phishing-evolving-threats"
    publisher: "Huntress"
    date: "2026-07-31"
    role: primary
closed_sources: []
evidence:
  - quote: "Infrastructure reputation is holding too much weight in many defense stacks. When a login originates from a provider or autonomous system that is generally trusted across commercial controls, attackers get a window to operate. That window may be short, but in token abuse operations, short is often long enough."
    publisher: "Huntress"
  - quote: "Between July 3 and July 27, we saw 26 critical-severity incidents linked to BL Networks spanning 23 identities."
    publisher: "Huntress"
  - quote: "Assume MFA alone is not enough when the attacker is abusing a legitimate Microsoft flow rather than stealing a password."
    publisher: "Huntress"
verification: single-source
sourcing_note: >
  Single-source: Huntress is the only party reporting this second wave, and the counts are its own customer telemetry
  rather than an independent measurement of the campaign. Huntress attributes the earlier Railway wave to the
  EvilTokens phishing-as-a-service platform but does not attribute the BL Networks activity to a named operator, so no
  attribution is carried here. The provider's founding year and ASN are attributed by Huntress to a third-party threat
  intelligence account rather than asserted from its own observation, and are reported here in the same terms. Network
  indicators from the report are deliberately not reproduced.
confidence: high
update_of: 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-10):** the device-code phishing wave covered earlier as a Railway-hosted campaign is not a single episode that tapered off. Huntress reports a second, parallel 2026 wave on entirely different infrastructure, and the delta that matters is what kind of infrastructure it is.

Huntress states it "started seeing suspicious Microsoft 365 authentication activity linked to BL Networks on April 13, 2026, which continues as of this writing", initially from a single address, spreading across several subnets in May, and continuing into July: "between July 3 and July 27, we saw 26 critical-severity incidents linked to BL Networks spanning 23 identities" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). For the April window it records 533 events tied to one address, including 113 successful logins in a 48-hour span between 20 and 21 April ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress describes BL Networks as a VPS reseller "active since at least 2017, operating under ASN AS399629, according to Bushido Token Threat Intel" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

The distinction from the earlier wave is the delta. The Railway campaign, which Huntress attributes to the EvilTokens phishing-as-a-service platform, ran on a platform-as-a-service product; BL Networks "is a bit different because it also provides standard hosting", with legitimate small-hosting customers alongside the abuse ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress is careful not to overstate the blind spot — it notes that "cybersecurity researchers have frequently flagged its IP addresses because bad actors have used its servers for malicious campaigns as well", and closes that "the bigger lesson here is not that one provider is bad forever" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). The narrower and more useful claim is about weighting: "infrastructure reputation is holding too much weight in many defense stacks. When a login originates from a provider or autonomous system that is generally trusted across commercial controls, attackers get a window to operate. That window may be short, but in token abuse operations, short is often long enough" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Huntress's broader argument is that defenders should stop tracking these as branded campaigns at all — "whether a campaign is discussed internally as Railway, EvilTokens, or potentially Kali365-aligned, the more durable lesson is that this is now an attack pattern" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

**Defender takeaway:** the original entry's controls stand — restrict the device-code flow, close the Conditional Access scoping gaps that let non-interactive flows past MFA requirements, and enable Continuous Access Evaluation so revocation takes effect quickly. What this wave adds is that an infrastructure-reputation feed will not tell you when the pattern recurs, so the detection has to be built on account context instead. Huntress's own recommended threshold is worth adopting as an internal rule rather than waiting for a vendor to classify the next provider: it flagged BL Networks on the strength of disproportionate device-code logins alone, and argues that when the evidence is that strong, "waiting for pristine attribution can become a luxury" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)). Its closing control set is to review and restrict device-code authentication where it is not required, monitor successful sign-ins from unusual infrastructure paired with device-code activity, investigate clusters of successful sign-in events from one autonomous system even when they do not individually score as high risk, revoke sessions and tokens quickly on suspicion, and "assume MFA alone is not enough when the attacker is abusing a legitimate Microsoft flow rather than stealing a password" ([Huntress, 2026-07-31](https://www.huntress.com/blog/device-code-phishing-evolving-threats)).

**Triage:** a successful sign-in from a commodity hosting provider is not by itself an incident — remote workers use VPNs, and small suppliers legitimately host services there. The discriminating combination Huntress sets out is three-part and needs all three: the sign-in succeeded, it is tied to the device-code flow rather than an ordinary interactive or browser-based authentication, and the hosting provider makes no business sense for that particular user's normal working pattern. The strongest variant is cross-tenant — the same autonomous system appearing behind successful sign-ins for multiple unrelated identities or organisations in a short window, which reads as operational rather than coincidental. Because the flow itself is a genuine Microsoft authentication path and MFA may legitimately have been satisfied, neither the presence of MFA nor a clean risk score is evidence against the finding.
