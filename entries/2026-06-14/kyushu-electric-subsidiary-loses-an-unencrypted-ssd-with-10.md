---
schema: 1
kind: incident
horizon: operational
title: "Kyushu Electric subsidiary loses an unencrypted SSD with 10.9 million customer records — reportedly Japan's largest personal-data breach"
headline: "Kyushu Electric subsidiary loses an unencrypted SSD with 10.9 million customer records — reportedly Japan's largest personal-data breach"
summary: "Kyushu Electric Power Transmission and Distribution disclosed on 8 June that a palm-sized portable SSD holding personal records for roughly 10.9 million customers went missing from a restricted server room; a contractor had backed up data to the drive on 27 April and stored it in a cabinet that was found unlocked and …"
discovered_at: "2026-06-14T05:00:02Z"
event_date: 2026-06-12
run_id: 2026-06-14-e1d80e78
priority: notable
immediate_action: null
tags:
  - data-breach
  - insider-threat
regions:
  - apac
sectors:
  - energy
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-of-109-million-clients/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.techtimes.com/articles/318287/20260612/japan-data-breach-kyushu-electric-loses-unencrypted-ssd-109-million-customer-records.htm"
    publisher: TechTimes
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
migrated_from: briefs/2026-06-14.md
---

Kyushu Electric Power Transmission and Distribution disclosed on 8 June that a palm-sized portable SSD holding personal records for roughly 10.9 million customers went missing from a restricted server room; a contractor had backed up data to the drive on 27 April and stored it in a cabinet that was found unlocked and empty on 26 May ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-of-109-million-clients/)). The drive held names, service addresses, phone numbers, electricity-usage data and retail-supplier names — all stored unencrypted and without password protection; no financial data was included ([TechTimes, 2026-06-12](https://www.techtimes.com/articles/318287/20260612/japan-data-breach-kyushu-electric-loses-unencrypted-ssd-109-million-customer-records.htm)). Kyushu Electric notified Japan's Personal Information Protection Commission and METI, which set an 8 July deadline for a full account.

**Defender takeaway:** This is a pure physical-media-control failure, the kind of exposure EU operators owe under NIS2 Article 21(2)(h). Audit whether backup media that leaves a server room is encrypted at rest with hardware-enforced AES, asset-tagged and access-logged — a single unlocked cabinet here produced a regulatory incident and total exposure with no remote attacker involved.
