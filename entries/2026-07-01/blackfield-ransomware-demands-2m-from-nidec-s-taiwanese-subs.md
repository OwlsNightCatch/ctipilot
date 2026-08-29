---
schema: 1
kind: incident
title: "Blackfield ransomware demands $2M from Nidec's Taiwanese subsidiary after a 22 June server compromise"
headline: "Blackfield ransomware demands $2M from Nidec's Taiwanese subsidiary after a 22 June server compromise"
summary: "Nidec Corporation's own investor-relations disclosure (2026-06-24, Tokyo Stock Exchange 6594) confirmed that its Taiwanese subsidiary Nidec Chaun Choung Technology suffered \"ransomware-originated damage\" to part of a subsidiary server on 2026-06-22, that the affected server and network were shut down as an emergency …"
discovered_at: "2026-07-01T04:41:15Z"
event_date: 2026-06-30
run_id: 2026-07-01-af9e697d
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - apac
sectors:
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.nidec.com/files/user/www-nidec-com/corporate/news/2026/0624-01/260624-01en.pdf"
    publisher: Nidec Corporation disclosure
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/blackfield-ransomware-asks-nidec-corporation-for-2-million-ransom/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-07-01.md
---

Nidec Corporation's own investor-relations disclosure (2026-06-24, Tokyo Stock Exchange 6594) confirmed that its Taiwanese subsidiary Nidec Chaun Choung Technology suffered "ransomware-originated damage" to part of a subsidiary server on 2026-06-22, that the affected server and network were shut down as an emergency measure, and that the subsidiary runs an independent network isolated from the wider Nidec Group so parent operations are unaffected ([Nidec Corporation, 2026-06-24](https://www.nidec.com/files/user/www-nidec-com/corporate/news/2026/0624-01/260624-01en.pdf)). The in-window development: BleepingComputer reported on 2026-06-30 that the Blackfield ransomware crew claims the intrusion, is demanding $2 million to delete allegedly stolen data with a 15-day negotiation deadline, and is separately advertising the archive for immediate sale ([BleepingComputer, 2026-06-30](https://www.bleepingcomputer.com/news/security/blackfield-ransomware-asks-nidec-corporation-for-2-million-ransom/)). Note the gap between the actor's exfiltration claim and Nidec's own statement, which as of 2026-06-24 says no personal or confidential data had been confirmed leaked — Blackfield *claims* data theft; Nidec has not confirmed a leak.

**Why it matters to us:** subsidiary/OT-adjacent segmentation is doing its job here (isolated subsidiary network limited blast radius) — a concrete counter-example worth citing when arguing for network isolation of acquired-company and regional-subsidiary estates. Attribute the extortion claim, not confirmed exfiltration.
