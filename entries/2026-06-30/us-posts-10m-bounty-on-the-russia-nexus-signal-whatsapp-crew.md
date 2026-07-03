---
schema: 1
kind: threat
horizon: operational
title: "US posts $10M bounty on the Russia-nexus Signal/WhatsApp crews and adds Signal Backup-Recovery-Key theft to the advisory"
headline: "US posts $10M bounty on the Russia-nexus Signal/WhatsApp crews and adds Signal Backup-Recovery-Key theft to the advisory"
summary: "UPDATE (originally covered 2026-06-27): The US Department of State's Rewards for Justice program posted a $10 million reward on 2026-06-29 for information on members of UNC5792 (assessed associated with Russia's FSB) and UNC4221 (assessed associated with the GRU), and the FBI/CISA advisory was updated with a newly …"
discovered_at: "2026-06-30T05:10:43Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - phishing
  - identity
regions:
  - europe
  - global
sectors:
  - public-sector
  - defense
  - media
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
cves: []
sources:
  - url: "https://rewardsforjustice.net/rewards/unc5792/"
    publisher: Rewards for Justice
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/us-offers-10-million-for-hackers-targeting-whatsapp-signal-users/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.securityweek.com/us-offers-10-million-bounty-for-russian-state-hackers-as-messaging-app-attacks-evolve/"
    publisher: SecurityWeek
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-27/fbi-cisa-russian-intelligence-now-phishing-signal-backup-rec
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-30.md
---

**UPDATE (originally covered 2026-06-27):** The US Department of State's Rewards for Justice program posted a $10 million reward on 2026-06-29 for information on members of UNC5792 (assessed associated with Russia's FSB) and UNC4221 (assessed associated with the GRU), and the FBI/CISA advisory was updated with a newly observed tactic — theft of Signal **Backup Recovery Keys** ([Rewards for Justice, 2026-06-29](https://rewardsforjustice.net/rewards/unc5792/) · [BleepingComputer, 2026-06-29](https://www.bleepingcomputer.com/news/security/us-offers-10-million-for-hackers-targeting-whatsapp-signal-users/)).

The recovery-key tactic is the operationally material change: a stolen backup recovery key is persistent — even after the victim rotates their phone number or reinstalls, the attacker can restore the full message backup, including prior history and group content, so access survives the initial social-engineering window ([SecurityWeek, 2026-06-29](https://www.securityweek.com/us-offers-10-million-bounty-for-russian-state-hackers-as-messaging-app-attacks-evolve/)). Targets are current/former government and military officials, political figures, journalists, and Ukraine-based officials across Europe and the US. Swiss federal and cantonal officials using Signal should treat backup-recovery-key protection (and re-checking the NCSC-CH Signal guidance covered 2026-06-25) as an action item, not a watch item.
