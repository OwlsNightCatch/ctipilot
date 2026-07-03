---
schema: 1
kind: threat
horizon: operational
title: "Netherlands FIOD arrests two over EU sanctions evasion for Stark Industries front; 800 servers seized; NoName057(16) DDoS plumbing dismantled"
headline: "Netherlands FIOD arrests two over EU sanctions evasion for Stark Industries front; 800 servers seized; NoName057(16) DDoS plumbing dismantled"
summary: "Dutch FIOD seizes 800 servers from Stark Industries proxy hoster — among the first publicly reported EU criminal enforcement actions against a sanctions-shielding bulletproof host. Suspects connected to WorkTitans B.V. and MIRhosting arrested for sustaining the infrastructure that fronted NoName057(16) DDoS operations against EU and Swiss public-sector targets (FIOD, 2026-05-22 · BleepingComputer, 2026-05-22)."
discovered_at: "2026-05-23T05:00:00Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: high
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - ddos
  - russia-nexus
  - eu-nexus
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - telco
entities: []
cves: []
sources:
  - url: "https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/"
    publisher: FIOD official press release
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/netherlands-seizes-800-servers-of-hosting-firm-enabling-cyberattacks/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.dutchnews.nl/2026/05/two-dutch-men-arrested-for-aiding-russian-cyberattacks/"
    publisher: DutchNews.nl
    role: corroborating
  - url: "https://www.recordedfuture.com/research/one-step-ahead-stark-industries-solutions-preempts-eu-sanctions"
    publisher: Recorded Future Insikt Group (2025-06 background)
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
migrated_from: briefs/2026-05-23.md
---

On 2026-05-18 the Dutch Fiscal Information and Investigation Service (FIOD) arrested two suspects — a 57-year-old man from Amsterdam and a 39-year-old man from The Hague, both connected to bulletproof-hosting operators (WorkTitans B.V. and MIRhosting) named in the related corroborating coverage — raiding four locations including data centres in Dronten and Schiphol-Rijk plus the suspects' residences in Enschede and Almere, and seizing 800 servers, laptops, phones and administrative records ([FIOD, 2026-05-22](https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/) · [BleepingComputer, 2026-05-22](https://www.bleepingcomputer.com/news/security/netherlands-seizes-800-servers-of-hosting-firm-enabling-cyberattacks/) · [DutchNews.nl, 2026-05-22](https://www.dutchnews.nl/2026/05/two-dutch-men-arrested-for-aiding-russian-cyberattacks/)). The charges are filed under the Dutch Sanctions Act: the two firms are accused of sustaining bulletproof hosting infrastructure for Stark Industries Solutions Ltd, designated by the EU in May 2025 for facilitating Russian and Belarusian destabilisation operations. Recorded Future's Insikt Group had already documented the sanctions-evasion playbook last year — Stark Industries migrated its ASN (AS44477) to AS209847 (WorkTitans) and rebranded the operating brand to THE.Hosting while retaining the same RIPE maintainer objects under Dmitrii Miasnikov, a transparent shell concealing ownership continuity ([Recorded Future Insikt Group, 2025-06](https://www.recordedfuture.com/research/one-step-ahead-stark-industries-solutions-preempts-eu-sanctions)).

This is one of the first publicly reported criminal enforcement actions in the EU directed at a bulletproof hoster acting as a proxy for a designated Russian entity, and the operational nexus to Switzerland is direct: per De Volkskrant reporting carried by BleepingComputer, Danish authorities have alleged that WorkTitans infrastructure supported NoName057(16) DDoS campaigns against EU and NATO member-state websites — Swiss federal and cantonal public-sector sites included. Defender vantage: the seized intelligence will generate lead packages on the criminal-customer book, but the immediate hunt value is at network level. AS44477 (legacy Stark) and AS209847 (THE.Hosting / WorkTitans) IP space has appeared in blocklist feeds since mid-2024; review ingress rate-limiting and scrubbing SLAs for any remaining traffic from this AS pair and from BGP-adjacent peers, and re-check application-layer rate limits on the citizen-facing portals NoName057(16) historically targeted.

**Why it matters to us:** Swiss public-sector portals have been a recurring NoName057(16) target; the takedown is a chance to re-baseline scrubbing capacity and re-check AS-level blocklists, not a sign that the threat is over (DDoS-for-hire reorganises quickly).
