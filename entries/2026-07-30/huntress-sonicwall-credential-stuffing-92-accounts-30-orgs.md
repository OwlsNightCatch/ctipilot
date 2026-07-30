---
schema: 1
kind: threat
horizon: operational
title: "Huntress: a three-day credential-stuffing run logged into 92 SonicWall VPN and firewall accounts across 30 organisations, with no follow-on activity observed"
headline: "Valid credentials, not a CVE, opened 92 SonicWall remote-access accounts in 41 hours — and nobody came back to use them"
summary: >
  Huntress reported on 2026-07-28 that it detected a spike in successful SonicWall VPN and firewall logins
  beginning 2026-07-25 and running through 2026-07-27, in which 92 unique user accounts across 30 distinct
  customer organisations were successfully accessed. No software vulnerability was involved — the logins
  used credentials that were already valid — and the traffic came from five primary addresses all registered
  to one commodity cloud-hosting provider. Huntress states it observed no post-compromise hands-on-keyboard
  activity after any of the successful logins, so the immediate question for any SonicWall operator is not
  whether an exploit landed but whether a valid account of theirs was among them and is still valid.
  SonicWall had published no advisory when CyberScoop went to press.
discovered_at: "2026-07-30T04:58:00Z"
event_date: "2026-07-27"
run_id: 2026-07-30T0409Z-intel
priority: high
immediate_action: null
tags: [identity, infostealer]
regions: [global]
sectors: [public-sector, healthcare, finance]
entities: []
techniques: [T1110.004, T1133]
affected_products: ["SonicWall SonicOS"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/sonicwall-credential-stuffing-campaign"
    publisher: "Huntress"
    date: "2026-07-28"
    role: primary
  - url: "https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/"
    publisher: "CyberScoop"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We did not observe any post-compromise hands-on-keyboard activity from these attacks."
    publisher: "Huntress"
  - quote: "July 25: 26 unique user accounts compromised across 6 distinct organizations. July 26: 34 unique user accounts compromised across 16 distinct organizations. July 27: 32 unique user accounts compromised across 8 distinct organizations."
    publisher: "Huntress"
  - quote: "We have identified five primary malicious IP addresses driving this attack, all of which are registered to DigitalOcean, LLC"
    publisher: "Huntress"
  - quote: "SonicWall hasn't released a security advisory about the malicious activity as of press time. A spokesperson told CyberScoop the company is still investigating and hopes to have more information soon."
    publisher: "CyberScoop"
verification: multi-source
sourcing_note: >
  All telemetry in this entry — the per-day counts, the account and organisation totals, and the
  attacking-infrastructure characterisation — originates solely with Huntress; CyberScoop corroborates the
  reporting and adds its own interview material and a SonicWall spokesperson statement, but does not
  contribute independent telemetry. Two attributions are kept deliberately separate from Huntress's
  observations: the characterisation of the intrusions as possible pre-positioning is CyberScoop's own
  inference and the word does not appear in Huntress's post, and the hypotheses about where the credentials
  came from are a Huntress analyst's explicitly hedged speculation rather than a finding. Neither source
  distinguishes SSLVPN from management-interface targeting for this campaign, so this entry does not either.
confidence: medium
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
  - "Search SonicWall VPN and firewall authentication logs for successful logins between 2026-07-25 and 2026-07-27 sourced from commodity cloud-hosting address space rather than user ISPs, and reset the credentials of every account that authenticated from one — the accounts were opened with valid credentials and left unused, so they remain usable until those credentials are changed."
migrated_from: null
---

Huntress detected what it describes as an out-of-the-ordinary spike in successful SonicWall VPN and firewall logins starting on 2026-07-25 and continuing over the following two days ([Huntress, 2026-07-28](https://www.huntress.com/blog/sonicwall-credential-stuffing-campaign)). The scale is stated day by day: "July 25: 26 unique user accounts compromised across 6 distinct organizations. July 26: 34 unique user accounts compromised across 16 distinct organizations. July 27: 32 unique user accounts compromised across 8 distinct organizations" ([Huntress, 2026-07-28](https://www.huntress.com/blog/sonicwall-credential-stuffing-campaign)) — 92 accounts and 30 organisations in total, which CyberScoop frames as 92 unique accounts compromised over 41 hours ([CyberScoop, 2026-07-29](https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/)).

The mechanism matters more than the numbers, because there is no vulnerability in it. These were successful authentications using credentials that already worked, not exploitation of a flaw in SonicOS, which means no patch addresses the exposure and no version check tells an operator whether they were affected. The traffic was also not distributed: Huntress states it "identified five primary malicious IP addresses driving this attack, all of which are registered to DigitalOcean, LLC" ([Huntress, 2026-07-28](https://www.huntress.com/blog/sonicwall-credential-stuffing-campaign)) — a handful of commodity cloud hosts rather than a residential-proxy pool or a botnet, which is the detail that makes retrospective log review practical.

The most operationally significant finding is what did not happen. Huntress states plainly: "We did not observe any post-compromise hands-on-keyboard activity from these attacks" ([Huntress, 2026-07-28](https://www.huntress.com/blog/sonicwall-credential-stuffing-campaign)). An attacker validated working access to 92 accounts and then stopped. CyberScoop reads that pattern as intrusions that "could be pre-positioning for future attacks" ([CyberScoop, 2026-07-29](https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/)) — that inference is CyberScoop's own, not something Huntress asserts, and the distinction is worth preserving because the two readings imply different urgency. What is not in dispute is the consequence of an unused valid credential: it stays valid. A Huntress analyst put the downstream risk as "with local network access, the sky is essentially the limit for most networks that do not have proper topology controls in place" ([CyberScoop, 2026-07-29](https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/)).

Where the credentials came from is unresolved and should be treated that way. Huntress's principal tactical response analyst offered candidate explanations — "this could be an aggregation of stealer malware logs, previously compromised SonicWall configuration files, or historic CVE compromise that resulted in more credentials than the adversary could use at the time" ([CyberScoop, 2026-07-29](https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/)) — but that is explicitly hedged speculation, not a determination. SonicWall itself has not weighed in: "SonicWall hasn't released a security advisory about the malicious activity as of press time. A spokesperson told CyberScoop the company is still investigating and hopes to have more information soon" ([CyberScoop, 2026-07-29](https://cyberscoop.com/sonicwall-credential-attacks-vpn-firewall/)).

Detection here is authentication-log work, not network-anomaly work. The telemetry class is remote-access authentication events with source-address attribution: successful logins to a VPN or firewall management portal whose source falls in cloud-hosting address space rather than the residential and mobile ranges legitimate remote users come from, clustered tightly in time across multiple accounts. Because the logins succeeded on the first or an early attempt, the classic brute-force signal — a burst of failures preceding a success — may be weak or absent, so keying detection on failure volume will miss this shape entirely. Hardening levers are credential-side rather than patch-side: rotate what may be burned, and constrain where remote-access authentication is accepted from.

**Defender takeaway:** for any SonicWall remote-access estate, the question this raises is retrospective. Ninety-two accounts were opened and abandoned, so the accounts that matter are the ones whose owners saw nothing wrong and whose credentials still work; a log review bounded to 2026-07-25 through 2026-07-27 is cheap and answers it directly.

**Triage:** a genuine remote worker authenticating to a SonicWall VPN arrives from a consumer ISP or mobile carrier range, at a plausible hour, usually to the same account over time. The discriminators for this activity are the source class and the fan-out: authentication from datacentre address space, several distinct accounts inside one organisation succeeding within a short window, and no subsequent session activity of the kind a real user generates after connecting. Any one of those alone is weak — a travelling user behind a VPN service can look like the first — but a datacentre-sourced success followed by silence is the shape to pull.
