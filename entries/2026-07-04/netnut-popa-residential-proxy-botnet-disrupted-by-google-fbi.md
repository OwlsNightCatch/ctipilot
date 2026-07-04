---
schema: 1
kind: incident
horizon: operational
title: "Google, FBI, Lumen and Shadowserver disrupt the NetNut (Popa) residential-proxy botnet"
headline: "Google/FBI-led action degrades NetNut (Popa) — ~2 million Badbox 2.0-infected TVs and streaming boxes cut off"
summary: >
  Google's Threat Intelligence Group, with the FBI, Lumen and The Shadowserver Foundation, disrupted
  NetNut (also tracked as Popa), a residential-proxy botnet GTIG estimates spans at least 2 million
  Android-based smart TVs and streaming boxes infected via Badbox 2.0-carrying trojanized apps. The FBI
  seized netnut.com; Google disabled C2 accounts and Play-Protect-blocked the apps. This is the
  law-enforcement/industry disruption of the same botnet Krebs/Qurium tied to Alarum/NetNut in June 2026.
discovered_at: "2026-07-04T00:26:13Z"
event_date: 2026-07-02
run_id: 2026-07-04T0009Z-intel
priority: notable
immediate_action: null
tags: [botnet, law-enforcement, organized-crime, espionage]
regions: [global]
sectors: [technology]
entities: [campaign:popa-vo1d-residential-proxy-botnet]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks"
    publisher: "Google Threat Intelligence Group"
    date: "2026-07-02"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/"
    publisher: "BleepingComputer"
    date: "2026-07-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Google Threat Intelligence Group (GTIG) estimates the size of the NetNut network to be at least 2 million devices, distributed across the world."
    publisher: "Google Threat Intelligence Group"
  - quote: "In a single week during June 2026, GTIG observed 316 distinct threat clusters using suspected NetNut exit nodes, including cybercriminal and espionage groups."
    publisher: "Google Threat Intelligence Group"
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-21/krebs-and-qurium-tie-the-popa-android-tv-residential-proxy-b
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Treat the NetNut/Popa disruption as temporary attrition, not elimination, of residential-proxy exit-node traffic; keep residential-ASN anomaly detection and IP-reputation controls in place as rival operators absorb displaced capacity."
  - "Hunt for Badbox 2.0-class trojanized-application behaviour on any managed Android smart-TV, set-top or IoT devices reachable from the corporate network."
migrated_from: null
---

**UPDATE (originally covered 2026-06-21):** Google's Threat Intelligence Group, coordinating with the FBI, Lumen Technologies and The Shadowserver Foundation, has disrupted the residential-proxy botnet previously tracked here as Popa — Google refers to it as NetNut — which GTIG estimates controls at least 2 million infected devices worldwide, predominantly Android-based smart TVs and streaming/set-top boxes compromised via trojanized apps carrying the Badbox 2.0 malware family ([Google Threat Intelligence Group, 2026-07-02](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks)). Google disabled the Google accounts and infrastructure used for NetNut command-and-control, shared technical intelligence with ecosystem partners, and used Google Play Protect to block apps bundling NetNut SDKs, while the FBI separately seized the `netnut.com` domain ([BleepingComputer, 2026-07-03](https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/)).

The delta since June is the scale of shared abuse the disruption exposes: GTIG reports that in a single week in June 2026 it observed 316 distinct threat clusters — spanning both cybercriminal and espionage actors — routing traffic through suspected NetNut exit nodes to hide malicious activity behind residential IP space (`T1090.003 Multi-hop Proxy`), confirming this proxy layer as shared criminal/state infrastructure rather than a single-group tool. Google cautions that the action reduced the operator's available device pool "by millions" but that individual proxy operators can appear resilient and rival operators may absorb displaced capacity.

**Defender takeaway:** residential-proxy exit nodes exist to defeat geo- and IP-reputation-based fraud and abuse controls, so SOC teams relying on residential-ASN anomaly detection should treat this takedown as temporary attrition, not elimination, of that traffic class — and should hunt for Badbox 2.0-class trojanized-app behaviour on any managed Android TV/IoT devices on their networks.
