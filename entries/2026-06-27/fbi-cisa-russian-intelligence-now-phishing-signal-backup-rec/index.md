---
schema: 1
kind: threat
title: >
  FBI/CISA: Russian intelligence now phishing Signal Backup Recovery Keys for persistent account
  takeover
headline: >
  FBI/CISA: Russian intelligence now phishing Signal Backup Recovery Keys for persistent account
  takeover
summary: >
  **Russian intelligence now phishes Signal Backup Recovery Keys.** FBI/CISA say UNC5792/UNC4221
  elicit the 30-character backup key for persistent account takeover that survives re-registration
  on the same number; regenerate keys for high-risk staff (FBI IC3, 2026-06-26).
discovered_at: "2026-06-27T05:17:38Z"
updated_at: "2026-06-30T05:10:43Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - phishing
  - identity
  - mobile
  - russia-nexus
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - defense
  - media
entities: []
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.ic3.gov/PSA/2026/PSA260626"
    publisher: FBI IC3 PSA I-062626-PSA
    role: primary
  - url: "https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html"
    publisher: The Hacker News
    role: corroborating
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
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-30T05:10:43Z"
    run_id: 2026-06-30-9aaa1114
    type: update
    summary: >
      UPDATE (originally covered 2026-06-27): The US Department of State's Rewards for Justice program
      posted a $10 million reward on 2026-06-29 for information on members of UNC5792 (assessed
      associated with Russia's FSB) and UNC4221 (assessed associated with the GRU), and the FBI/CISA
      advisory was updated with a newly …
    fields:
      - sources
      - body
    merged_from: 2026-06-30/us-posts-10m-bounty-on-the-russia-nexus-signal-whatsapp-crew
migrated_from: briefs/2026-06-27.md
---

The FBI and CISA issued an updated joint advisory (PSA I-062626-PSA, 2026-06-26) escalating their March 2026 warning about Russian Intelligence Services operators tracked as **UNC5792** (FSB-linked) and **UNC4221** (military-linked) ([FBI IC3, 2026-06-26](https://www.ic3.gov/PSA/2026/PSA260626)). The new tactic abuses Signal's optional encrypted-backup feature rather than any flaw in the Signal Protocol: operators impersonate Signal support, walk the target through *Settings → Chats → Chat Backups*, then elicit the 30-character **Backup Recovery Key**. With that key an attacker can download and decrypt the complete private and group message history offline. Critically, the advisory states the compromised key remains valid *even if the victim later re-registers a new account on the same phone number* — generating a new key in Settings invalidates future downloads but does not undo data already exfiltrated ([FBI IC3, 2026-06-26](https://www.ic3.gov/PSA/2026/PSA260626)). Stated targets are current and former government officials, military personnel, political figures, journalists, and Ukraine-related officials. This is `T1598.003` (spearphishing via service) leading to `T1078` (valid-account takeover via the backup mechanism), with no platform-layer sensor — detection relies on user reporting and MDM telemetry for backup-enable events.
**Why it matters to us:** Swiss federal, cantonal-police, and parliamentary staff using Signal for sensitive coordination sit squarely in the named target population. Issue policy now: high-risk personnel should regenerate their Signal Backup Recovery Key, treat any unsolicited "Signal support" message as hostile, and on managed devices disable Signal backups via MDM where operational security requires it.

## Update — 2026-06-30T05:10:43Z

The US Department of State's Rewards for Justice program posted a $10 million reward on 2026-06-29 for information on members of UNC5792 (assessed associated with Russia's FSB) and UNC4221 (assessed associated with the GRU), and the FBI/CISA advisory was updated with a newly observed tactic — theft of Signal **Backup Recovery Keys** ([Rewards for Justice, 2026-06-29](https://rewardsforjustice.net/rewards/unc5792/) · [BleepingComputer, 2026-06-29](https://www.bleepingcomputer.com/news/security/us-offers-10-million-for-hackers-targeting-whatsapp-signal-users/)).

The recovery-key tactic is the operationally material change: a stolen backup recovery key is persistent — even after the victim rotates their phone number or reinstalls, the attacker can restore the full message backup, including prior history and group content, so access survives the initial social-engineering window ([SecurityWeek, 2026-06-29](https://www.securityweek.com/us-offers-10-million-bounty-for-russian-state-hackers-as-messaging-app-attacks-evolve/)). Targets are current/former government and military officials, political figures, journalists, and Ukraine-based officials across Europe and the US. Swiss federal and cantonal officials using Signal should treat backup-recovery-key protection (and re-checking the NCSC-CH Signal guidance covered 2026-06-25) as an action item, not a watch item.
