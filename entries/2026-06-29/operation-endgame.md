---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: Operation Endgame
headline: Operation Endgame
summary: "Europol's law-enforcement campaign extended its reach this week: the 06-24/25 Amadey and StealC takedown actioned 326 servers and 142 domains and recovered approximately 27 million stolen credentials from over 385,000 compromised systems (BleepingComputer), with Microsoft providing the Amadey/StealC infrastructure …"
discovered_at: "2026-06-29T00:21:22Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - infostealer
  - botnet
  - organized-crime
regions:
  - europe
  - global
sectors:
  - public-sector
  - finance
entities:
  - "campaign:operation-endgame-amadey-stealc"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/amadey-stealc-malware-operations-disrupted-in-operation-endgame-action/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/"
    publisher: Microsoft Threat Intelligence
    role: corroborating
  - url: "https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks"
    publisher: Europol newsroom
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
migrated_from: briefs/weekly/2026-W26.md
---

Europol's law-enforcement campaign extended its reach this week: the 06-24/25 Amadey and StealC takedown actioned 326 servers and 142 domains and recovered approximately 27 million stolen credentials from over 385,000 compromised systems ([BleepingComputer](https://www.bleepingcomputer.com/news/security/amadey-stealc-malware-operations-disrupted-in-operation-endgame-action/)), with Microsoft providing the Amadey/StealC infrastructure analysis ([Microsoft](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)). Combined with the W25 SocGholish/TA569 seizure (106 servers), Endgame has now dismantled three commodity delivery-and-theft networks in quick succession. The defender gap: no arrests were announced for this phase, so infrastructure can reconstitute — cross-reference the recovered 27M credentials against your identity-store canaries and hunt Amadey persistence (`HKCU` run-key, `rundll32`/`regsvr32` side-loads, short-lived child processes under `%AppData%\Roaming`).
