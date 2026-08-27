---
schema: 1
kind: research
horizon: operational
title: >
  Krebs and Qurium tie the "Popa" Android-TV residential-proxy botnet to a NASDAQ-listed proxy
  vendor
headline: >
  Krebs and Qurium tie the "Popa" Android-TV residential-proxy botnet to a NASDAQ-listed proxy
  vendor
summary: >
  Krebs on Security and the Qurium Media Foundation jointly documented Popa, a residential-proxy
  botnet that has run on millions of Android-based consumer TV boxes for roughly four years,
  operating as a plugin component of the larger Vo1d botnet (Krebs on Security, 2026-06-18).
discovered_at: "2026-06-21T04:55:01Z"
updated_at: "2026-07-04T00:26:13Z"
event_date: 2026-06-18
run_id: 2026-06-21-2b75e32c
priority: notable
immediate_action: null
tags:
  - botnet
  - organized-crime
  - cryptocrime
  - law-enforcement
  - espionage
regions:
  - global
sectors:
  - technology
  - media
entities:
  - "campaign:popa-vo1d-residential-proxy-botnet"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/"
    publisher: Krebs on Security
    role: primary
  - url: "https://www.qurium.org/forensics/finding-popa/"
    publisher: Qurium Media Foundation
    role: corroborating
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks"
    publisher: Google Threat Intelligence Group
    date: 2026-07-02
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/"
    publisher: BleepingComputer
    date: 2026-07-03
    role: corroborating
closed_sources: []
evidence:
  - quote: "Google Threat Intelligence Group (GTIG) estimates the size of the NetNut network to be at least 2 million devices, distributed across the world."
    publisher: Google Threat Intelligence Group
  - quote: "In a single week during June 2026, GTIG observed 316 distinct threat clusters using suspected NetNut exit nodes, including cybercriminal and espionage groups."
    publisher: Google Threat Intelligence Group
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "Treat the NetNut/Popa disruption as temporary attrition, not elimination, of residential-proxy exit-node traffic; keep residential-ASN anomaly detection and IP-reputation controls in place as rival operators absorb displaced capacity."
  - "Hunt for Badbox 2.0-class trojanized-application behaviour on any managed Android smart-TV, set-top or IoT devices reachable from the corporate network."
updates:
  - at: "2026-07-04T00:26:13Z"
    run_id: 2026-07-04T0009Z-intel
    type: update
    summary: >
      Google's Threat Intelligence Group, with the FBI, Lumen and The Shadowserver Foundation,
      disrupted NetNut (also tracked as Popa), a residential-proxy botnet GTIG estimates spans at
      least 2 million Android-based smart TVs and streaming boxes infected via Badbox 2.0-carrying
      trojanized apps. The FBI seized netnut.com; Google disabled C2 accounts and Play-Protect-blocked
      the apps. This is the law-enforcement/industry disruption of the same botnet Krebs/Qurium tied
      to Alarum/NetNut in June 2026.
    fields:
      - actions
      - entities
      - evidence
      - sources
      - tags
      - body
    merged_from: 2026-07-04/netnut-popa-residential-proxy-botnet-disrupted-by-google-fbi
migrated_from: briefs/2026-06-21.md
---

Krebs on Security and the Qurium Media Foundation jointly documented Popa, a residential-proxy botnet that has run on millions of Android-based consumer TV boxes for roughly four years, operating as a plugin component of the larger Vo1d botnet ([Krebs on Security, 2026-06-18](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/)). The botnet monetises infected devices by relaying advertising fraud, account-takeover traffic and AI data-scraping through residential IP space so the traffic appears to originate from ordinary home users. Qurium's forensic tracing of several dozen control domains found infrastructure operated in lockstep with NetNut — a "residential proxy" service tied to publicly-traded Alarum Technologies (NASDAQ: ALAR) — via the NinjaTech entity and a shared `neonative` library ([Qurium, 2026-06-18](https://www.qurium.org/forensics/finding-popa/)). Propagation is through thousands of malware-laced pirated streaming and torrent apps reaching unofficial Android TV hardware. Per the fake-news guard, this is the researchers' documented corporate-infrastructure linkage — Alarum has not been charged with any offence, and the legal characterisation of the proxy traffic is unresolved; attribute the connection to Krebs/Qurium rather than asserting it as adjudicated fact.

**Why it matters to us:** Residential-proxy traffic is hard to block without collateral damage, and it inverts a common SOC assumption — an authentication attempt arriving from a "residential" ASN may be proxy-relayed attack traffic, not a geographic-targeting signal. Practical posture for a public-sector SOC: flag authentication events from residential ASNs that are anomalous for your user population, watch for consumer Android-TV IP ranges touching sensitive portals (those devices have no business authenticating to corporate services), and treat residential-proxy provider ranges as a credential-stuffing source against citizen-facing portals. Maps to [T1090.002 Proxy: External Proxy](https://attack.mitre.org/techniques/T1090/002/) and [T1496 Resource Hijacking](https://attack.mitre.org/techniques/T1496/).

## Update — 2026-07-04T00:26:13Z

Google's Threat Intelligence Group, coordinating with the FBI, Lumen Technologies and The Shadowserver Foundation, has disrupted the residential-proxy botnet previously tracked here as Popa — Google refers to it as NetNut — which GTIG estimates controls at least 2 million infected devices worldwide, predominantly Android-based smart TVs and streaming/set-top boxes compromised via trojanized apps carrying the Badbox 2.0 malware family ([Google Threat Intelligence Group, 2026-07-02](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks)). Google disabled the Google accounts and infrastructure used for NetNut command-and-control, shared technical intelligence with ecosystem partners, and used Google Play Protect to block apps bundling NetNut SDKs, while the FBI separately seized the `netnut.com` domain ([BleepingComputer, 2026-07-03](https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/)).

The delta since June is the scale of shared abuse the disruption exposes: GTIG reports that in a single week in June 2026 it observed 316 distinct threat clusters — spanning both cybercriminal and espionage actors — routing traffic through suspected NetNut exit nodes to hide malicious activity behind residential IP space (`T1090.003 Multi-hop Proxy`), confirming this proxy layer as shared criminal/state infrastructure rather than a single-group tool. Google cautions that the action reduced the operator's available device pool "by millions" but that individual proxy operators can appear resilient and rival operators may absorb displaced capacity.

**Defender takeaway:** residential-proxy exit nodes exist to defeat geo- and IP-reputation-based fraud and abuse controls, so SOC teams relying on residential-ASN anomaly detection should treat this takedown as temporary attrition, not elimination, of that traffic class — and should hunt for Badbox 2.0-class trojanized-app behaviour on any managed Android TV/IoT devices on their networks.
