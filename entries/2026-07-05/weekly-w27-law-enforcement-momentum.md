---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Law-enforcement and platform-disruption momentum this week — NetNut/Popa proxy botnet dismantled, StegoAd extension cluster killed, $10M bounty on Russia-nexus crews"
headline: "Disruption momentum this week — NetNut proxy botnet dismantled, StegoAd extensions killed, $10M bounty"
summary: "Three coordinated disruption actions landed this week: the FBI, Google, Lumen and Shadowserver dismantled the NetNut (Popa) residential-proxy botnet (~2M devices, abused by 316 distinct threat clusters in a single June week); Microsoft killed the StegoAd cluster of 119 malicious Edge extensions; and the US posted a $10M bounty on Russia-nexus Signal/WhatsApp phishing crews. The defender lesson is attrition, not elimination — residential-proxy abuse and extension-based delivery shift providers rather than stopping."
discovered_at: "2026-07-05T23:33:00Z"
event_date: 2026-07-02
run_id: 2026-07-05T2305Z-weekly
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - botnet
  - organized-crime
regions:
  - global
sectors:
  - technology
  - public-sector
  - finance
entities:
  - "campaign:popa-vo1d-residential-proxy-botnet"
  - "campaign:stegoad-darkspectre-119-edge-extensions-steganography"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks"
    publisher: Google Cloud (GTIG)
    role: primary
  - url: "https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/"
    publisher: Krebs on Security
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "In a single week during June 2026, GTIG observed 316 distinct threat clusters using suspected NetNut exit nodes, including cybercriminal and espionage groups."
    publisher: "Google Cloud (GTIG)"
  - quote: "Google Threat Intelligence Group (GTIG) estimates the size of the NetNut network to be at least 2 million devices, distributed across the world."
    publisher: "Google Cloud (GTIG)"
verification: multi-source
sourcing_note: null
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - "2026-07-04/netnut-popa-residential-proxy-botnet-disrupted-by-google-fbi"
  - "2026-06-30/microsoft-disrupts-stegoad-119-edge-extensions-hid-payloads"
  - "2026-06-30/us-posts-10m-bounty-on-the-russia-nexus-signal-whatsapp-crew"
  - "2026-06-30/mustang-panda-abuses-zoho-workdrive-as-a-dead-drop-c2-channe"
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Treat the NetNut takedown as temporary attrition of residential-proxy abuse, not elimination: keep hunting authentication attempts from residential/consumer-ISP ASN ranges hitting the same account in rapid succession from geographically implausible sequences, and treat 'residential' IP-reputation allowlisting as a gap."
  - "Hunt Badbox 2.0-class trojanized-app behaviour on any managed Android TV / IoT devices; the botnet's device pool was predominantly smart TVs and streaming boxes carrying malicious SDKs."
---

Three disruption actions this week are worth consolidating not as wins to celebrate but for what each says about the durability of the abused technique.

**NetNut (Popa) residential-proxy botnet dismantled.** The FBI — with Google, Lumen and Shadowserver — seized NetNut/Popa infrastructure on 2026-07-02; Google disabled the Google accounts used for C2 and updated Play Protect to block apps bundling the malicious SDKs, while the FBI seized `netnut.com` ([Google GTIG, 2026-07-02](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks); [Krebs on Security, 2026-07-02](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/)). The strategic figure GTIG surfaces is that in a single June week it observed **316 distinct threat clusters** — criminal and suspected-espionage — routing traffic through suspected NetNut exit nodes to mask origin IPs during password-spray, credential-stuffing and infrastructure access. That confirms residential-proxy relay as shared criminal/state infrastructure, and Google's own caution is the key defender note: degraded operators buy capacity from rivals, so proxy-based anonymisation volumes shift providers rather than dropping (§ references, operational coverage 07-04).

**StegoAd extension cluster.** Microsoft disrupted StegoAd — 119 Edge extensions that hid payloads inside image and font files via steganography (`campaign:stegoad-darkspectre-119-edge-extensions-steganography`) — reinforcing browser-extension marketplaces as a recurring, disruptable delivery surface (this week's operational coverage, § references).

**$10M bounty on Russia-nexus crews.** The US added a $10M bounty on the Russia-nexus Signal/WhatsApp phishing crews and folded Signal Backup-Recovery-Key theft into the advisory (this week's operational coverage, § references).

**Weekly takeaway:** all three targets abuse infrastructure that is cheap to re-provision — residential proxies, browser extensions, messaging-app social engineering — so the correct posture for a SOC is to keep the *behavioural* detections (implausible residential-ASN auth sequences, extension-install governance, Signal backup-key hygiene for high-risk staff) running past the headlines, because the operators displaced this week reappear behind new providers. This week's Mustang Panda dead-drop-C2-via-Zoho-WorkDrive case (§ references) is the same lesson from the offensive side: abuse of legitimate, hard-to-block infrastructure is the through-line.
