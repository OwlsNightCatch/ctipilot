---
schema: 1
kind: research
horizon: operational
title: "Krebs and Qurium tie the \"Popa\" Android-TV residential-proxy botnet to a NASDAQ-listed proxy vendor"
headline: "Krebs and Qurium tie the \"Popa\" Android-TV residential-proxy botnet to a NASDAQ-listed proxy vendor"
summary: "Krebs on Security and the Qurium Media Foundation jointly documented Popa, a residential-proxy botnet that has run on millions of Android-based consumer TV boxes for roughly four years, operating as a plugin component of the larger Vo1d botnet (Krebs on Security, 2026-06-18)."
discovered_at: "2026-06-21T04:55:01Z"
event_date: 2026-06-18
run_id: 2026-06-21-2b75e32c
priority: notable
immediate_action: null
tags:
  - botnet
  - organized-crime
  - cryptocrime
regions:
  - global
sectors:
  - technology
  - media
entities: []
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/"
    publisher: Krebs on Security
    role: primary
  - url: "https://www.qurium.org/forensics/finding-popa/"
    publisher: Qurium Media Foundation
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-21.md
---

Krebs on Security and the Qurium Media Foundation jointly documented Popa, a residential-proxy botnet that has run on millions of Android-based consumer TV boxes for roughly four years, operating as a plugin component of the larger Vo1d botnet ([Krebs on Security, 2026-06-18](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/)). The botnet monetises infected devices by relaying advertising fraud, account-takeover traffic and AI data-scraping through residential IP space so the traffic appears to originate from ordinary home users. Qurium's forensic tracing of several dozen control domains found infrastructure operated in lockstep with NetNut — a "residential proxy" service tied to publicly-traded Alarum Technologies (NASDAQ: ALAR) — via the NinjaTech entity and a shared `neonative` library ([Qurium, 2026-06-18](https://www.qurium.org/forensics/finding-popa/)). Propagation is through thousands of malware-laced pirated streaming and torrent apps reaching unofficial Android TV hardware. Per the fake-news guard, this is the researchers' documented corporate-infrastructure linkage — Alarum has not been charged with any offence, and the legal characterisation of the proxy traffic is unresolved; attribute the connection to Krebs/Qurium rather than asserting it as adjudicated fact.

**Why it matters to us:** Residential-proxy traffic is hard to block without collateral damage, and it inverts a common SOC assumption — an authentication attempt arriving from a "residential" ASN may be proxy-relayed attack traffic, not a geographic-targeting signal. Practical posture for a public-sector SOC: flag authentication events from residential ASNs that are anomalous for your user population, watch for consumer Android-TV IP ranges touching sensitive portals (those devices have no business authenticating to corporate services), and treat residential-proxy provider ranges as a credential-stuffing source against citizen-facing portals. Maps to [T1090.002 Proxy: External Proxy](https://attack.mitre.org/techniques/T1090/002/) and [T1496 Resource Hijacking](https://attack.mitre.org/techniques/T1496/).
