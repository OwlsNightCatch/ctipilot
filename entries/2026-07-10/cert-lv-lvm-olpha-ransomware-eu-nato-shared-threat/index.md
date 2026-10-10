---
schema: 1
kind: incident
title: "CERT.LV: ransomware crew breaches Latvia's state forestry operator LVM via a 2-year-unpatched system, hits essential-services provider Olpha, and is probing other EU/NATO institutions"
headline: "CERT.LV warns a financially-motivated crew that breached Latvian state forestry and an essential-services provider is targeting other EU/NATO state institutions"
summary: >
  CERT.LV confirms a foreign, financially-motivated ransomware group breached AS Latvijas valsts meži (LVM), Latvia's state-owned forestry company, through a public-facing system left ~2 years without a security update — dwelling ~11 days before detonating on 22-23 June 2026 and exfiltrating 44 GB including credentials and their hashes. The same actor also compromised a server at essential-services provider AS Olpha with forensic log-wiping. CERT.LV states the group has run comparable operations against other NATO/EU member-state companies and state institutions and is still probing Latvian infrastructure — a cross-border shared-threat signal for European critical-infrastructure and government operators.
discovered_at: "2026-07-10T04:36:19Z"
event_date: "2026-06-22"
run_id: 2026-07-10T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, vulnerabilities]
regions: [europe, nordics]
sectors: [public-sector, healthcare]
entities: [incident:cert-lv-lvm-olpha-ransomware-2026]
techniques: [T1190, T1071, T1070, T1078]
affected_products: []
cves: []
sources:
  - url: "https://cert.lv/lv/2026/06/as-latvijas-valsts-mezi-kiberdrosibas-incidents-aktuala-informacija"
    publisher: "CERT.LV (Latvia national CERT)"
    date: "2026-07-03"
    role: primary
  - url: "https://cert.lv/lv/2026/07/cert-lv-rekomendacijas-infrastrukturas-kiberdrosibas-noturibas-uzlabosanai-pret-kiberuzbrukumiem"
    publisher: "CERT.LV (Latvia national CERT)"
    date: "2026-07-03"
    role: primary
  - url: "https://therecord.media/latvia-state-owned-foresty-company-lvm-ransomware"
    publisher: "The Record (Recorded Future News)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://bnn-news.com/hacker-remained-undetected-in-latvijas-valsts-mezi-system-for-several-days-281634"
    publisher: "BNN News (Baltic News Network)"
    date: "2026-07-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attackers exploited a vulnerability in a system that had not been updated for two years, but he did not identify the affected software."
    publisher: "The Record (Recorded Future News)"
  - quote: "It is unacceptable that there were no detection tools in the system to identify abnormal activity."
    publisher: "BNN News (Baltic News Network)"
verification: multi-source
sourcing_note: "Primary disclosure is CERT.LV (Latvia's national CERT, its own jurisdiction — Admiralty A); incident facts (timeline, 44 GB exfiltration, second Olpha intrusion) are corroborated by The Record and Latvian press. CERT.LV's assessment that the same actor is targeting other NATO/EU member-state institutions is a single-authority claim not independently corroborated in-run."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Treat any authentication material (passwords, hashes, service-account credentials, certificates/keys) tied to an internet-exposed system that has gone unpatched for an extended period as already compromised and rotate it — LVM's 44 GB exfiltration included user passwords and their hashes."
  - "Inventory internet-facing systems for anything unpatched beyond ~1 year and prioritise it for patching or isolation; CERT.LV names long-unpatched exposed systems as the entry point here."
  - "Hunt for abuse of legitimate tunnelling services (Cloudflare Tunnel, Microsoft Dev Tunnels, ngrok-class tunnels) and open-source C2 frameworks (Sliver) as an egress/C2 class, and deploy out-of-band log retention that survives host encryption or deliberate log deletion."
migrated_from: null
---

CERT.LV, Latvia's national CERT, confirmed that a foreign, financially-motivated ransomware group breached AS "Latvijas valsts meži" (LVM), the state-owned forestry company, by exploiting a public-facing system that LVM's own IT director says had gone roughly two years without a security update (he declined to name the affected software) (`T1190`, [The Record, 2026-07-09](https://therecord.media/latvia-state-owned-foresty-company-lvm-ransomware)). Initial access was gained on 11 June 2026, but the actor stayed dormant for about eleven days before detonating on the night of 22-23 June — Latvia's prime minister stated publicly that no detection tooling existed to catch the intervening abnormal activity, and CERT.LV separately flagged a gap in LVM's compliance with Latvia's national cybersecurity law ([BNN News, 2026-07-02](https://bnn-news.com/hacker-remained-undetected-in-latvijas-valsts-mezi-system-for-several-days-281634)). Before the extortion attempt the actor exfiltrated 44 GB — internal documents, email, business-IT project code repositories, digital certificates and keys, and user passwords together with their hash values — and CERT.LV's incident recommendations state that all authentication material tied to the affected infrastructure must be treated as compromised and rotated (`T1078`, [CERT.LV, 2026-07-03](https://cert.lv/lv/2026/06/as-latvijas-valsts-mezi-kiberdrosibas-incidents-aktuala-informacija)). During analysis CERT.LV found the same actor had also gained unauthorised access to at least one server at AS Olpha (formerly Olainfarm), a Latvian essential-services provider; data there was not encrypted but forensic log deletion was observed (`T1070`), a technically separate, contemporaneous intrusion by the same group.

The reason this is a signal beyond Latvia: CERT.LV states the group has run comparable operations against other companies and state institutions in NATO and EU member states, and is continuing to probe Latvian public- and private-sector infrastructure for new footholds. CERT.LV's published network-indicator set names Sliver (an open-source red-team C2 framework) alongside generic C2 servers and Proton VPN egress as the observed infrastructure (`T1071`), and its guidance explicitly calls out legitimate-looking tunnelling services (Cloudflare Tunnel, Microsoft Dev Tunnels, ngrok-class tunnels) as a traffic class defenders should treat as suspicious for this campaign profile ([CERT.LV, 2026-07-03](https://cert.lv/lv/2026/07/cert-lv-rekomendacijas-infrastrukturas-kiberdrosibas-noturibas-uzlabosanai-pret-kiberuzbrukumiem)).

**Defender takeaway:** the durable lessons are non-IOC and portable to any European CI/government operator. Long-unpatched internet-exposed systems remain the highest-yield entry point, and their associated credentials must be assumed compromised on breach; a ~11-day dwell with no detection underscores the need for out-of-band, tamper-resistant log retention that survives both encryption and deliberate log-wiping; and open-source C2 (Sliver) plus abuse of sanctioned tunnelling services is the egress/command-and-control class to hunt. **Triage:** Cloudflare Tunnel, Dev Tunnels and ngrok are used legitimately by many teams, so their mere presence is not the signal — the discriminator is a tunnel or a Sliver-class beacon originating from a server that has no business initiating outbound tunnelled sessions, correlated with anomalous access to a long-unpatched asset.
