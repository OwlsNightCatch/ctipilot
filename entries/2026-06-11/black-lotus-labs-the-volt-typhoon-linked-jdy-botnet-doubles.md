---
schema: 1
kind: research
horizon: operational
title: "Black Lotus Labs: the Volt Typhoon-linked JDY botnet doubles to 1,500+ devices and weaponises CVE disclosures within hours"
headline: "Black Lotus Labs: the Volt Typhoon-linked JDY botnet doubles to 1,500+ devices and weaponises CVE disclosures within hours"
summary: "Lumen's Black Lotus Labs reports that the JDY botnet — the reconnaissance cluster that survived the 2024 KV-botnet takedown and is assessed with high confidence to support multiple China-nexus actors including Volt Typhoon — has more than doubled from roughly 650 bots in January 2024 to over 1,500 compromised SOHO and …"
discovered_at: "2026-06-11T05:00:04Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - botnet
  - china-nexus
regions:
  - global
sectors:
  - defense
  - telco
  - public-sector
entities:
  - "campaign:jdy-botnet-volt-typhoon-2026"
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/expanded-jdy-iot-and-soho-botnet-enables-rapid-vulnerability-exploitation"
    publisher: Lumen Black Lotus Labs
    role: primary
  - url: "https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-35616)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-11.md
---

Lumen's Black Lotus Labs reports that the JDY botnet — the reconnaissance cluster that survived the 2024 KV-botnet takedown and is assessed with high confidence to support multiple China-nexus actors including Volt Typhoon — has more than doubled from roughly 650 bots in January 2024 to over 1,500 compromised SOHO and IoT devices ([Lumen Black Lotus Labs, 2026-06-10](https://www.lumen.com/blog/en-us/expanded-jdy-iot-and-soho-botnet-enables-rapid-vulnerability-exploitation)). The botnet now spans Cisco, Araknis, Mimosa Networks, Ubiquiti, Draytek, Hikvision and Linksys devices, performs multiprotocol service fingerprinting, banner-grabbing and TLS-certificate collection at scale, and routes C2 through hidden Tor services while managing victims with the open-source Platypus reverse-shell server. The operationally significant finding: scanning of Fortinet devices spiked within hours of the public disclosure of CVE-2026-35616, demonstrating sub-24-hour integration of new vulnerability intelligence into the recon-to-exploitation pipeline ([The Hacker News, 2026-06-10](https://thehackernews.com/2026/06/china-linked-jdy-botnet-expands-to-1500.html)). Targeting centres on US military and associated entities, with distributed European nodes. Technique mapping: `T1595.002` Active Scanning: Vulnerability Scanning, `T1590` Gather Victim Network Information, `T1584.005` Compromise Infrastructure: Botnet.

**Why it matters to us:** JDY scanning should be treated as a precursor to targeted exploitation, not background noise — the sub-24-hour weaponisation window means CH/EU public-sector and critical-infrastructure operators must compress patch cycles for internet-facing edge appliances to hours, not weeks, after a disclosure. Hunt for outbound connections from edge/SOHO devices to the Platypus default service, unusual high-rate outbound SYN scanning, and unexpected TLS-certificate harvesting.
