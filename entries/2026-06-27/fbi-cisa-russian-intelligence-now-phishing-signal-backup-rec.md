---
schema: 1
kind: threat
horizon: operational
title: "FBI/CISA: Russian intelligence now phishing Signal Backup Recovery Keys for persistent account takeover"
headline: "FBI/CISA: Russian intelligence now phishing Signal Backup Recovery Keys for persistent account takeover"
summary: "**Russian intelligence now phishes Signal Backup Recovery Keys.** FBI/CISA say UNC5792/UNC4221 elicit the 30-character backup key for persistent account takeover that survives re-registration on the same number; regenerate keys for high-risk staff (FBI IC3, 2026-06-26)."
discovered_at: "2026-06-27T05:17:38Z"
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
cves: []
sources:
  - url: "https://www.ic3.gov/PSA/2026/PSA260626"
    publisher: FBI IC3 PSA I-062626-PSA
    role: primary
  - url: "https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-06-27.md
---

The FBI and CISA issued an updated joint advisory (PSA I-062626-PSA, 2026-06-26) escalating their March 2026 warning about Russian Intelligence Services operators tracked as **UNC5792** (FSB-linked) and **UNC4221** (military-linked) ([FBI IC3, 2026-06-26](https://www.ic3.gov/PSA/2026/PSA260626)). The new tactic abuses Signal's optional encrypted-backup feature rather than any flaw in the Signal Protocol: operators impersonate Signal support, walk the target through *Settings → Chats → Chat Backups*, then elicit the 30-character **Backup Recovery Key**. With that key an attacker can download and decrypt the complete private and group message history offline. Critically, the advisory states the compromised key remains valid *even if the victim later re-registers a new account on the same phone number* — generating a new key in Settings invalidates future downloads but does not undo data already exfiltrated ([FBI IC3, 2026-06-26](https://www.ic3.gov/PSA/2026/PSA260626)). Stated targets are current and former government officials, military personnel, political figures, journalists, and Ukraine-related officials. This is `T1598.003` (spearphishing via service) leading to `T1078` (valid-account takeover via the backup mechanism), with no platform-layer sensor — detection relies on user reporting and MDM telemetry for backup-enable events.
**Why it matters to us:** Swiss federal, cantonal-police, and parliamentary staff using Signal for sensitive coordination sit squarely in the named target population. Issue policy now: high-risk personnel should regenerate their Signal Backup Recovery Key, treat any unsolicited "Signal support" message as hostile, and on managed devices disable Signal backups via MDM where operational security requires it.
