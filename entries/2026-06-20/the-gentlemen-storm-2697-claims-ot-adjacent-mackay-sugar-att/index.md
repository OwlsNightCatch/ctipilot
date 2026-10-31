---
schema: 1
kind: threat
title: "The Gentlemen (Storm-2697) claims OT-adjacent Mackay Sugar attack; operator attributed to a Russian national"
headline: "The Gentlemen (Storm-2697) claims OT-adjacent Mackay Sugar attack; operator attributed to a Russian national"
summary: "UPDATE (originally covered 2026-06-19): Following ESET's 2026-06-19 documentation of the group's GentleKiller EDR-killer framework, The Gentlemen ransomware group has claimed an OT-adjacent attack on Mackay Sugar (Australia's second-largest sugar producer), which confirmed on 2026-06-18 that an external party …"
discovered_at: "2026-06-20T05:12:20Z"
event_date: 2026-06-18
run_id: 2026-06-20-4cfd00ef
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - russia-nexus
regions:
  - global
sectors:
  - manufacturing
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://therecord.media/mackay-sugar-cyberattack-claimed-gentlemen"
    publisher: The Record
    role: primary
  - url: "https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/"
    publisher: KrebsOnSecurity
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-06-19)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-20.md
---

**UPDATE (originally covered 2026-06-19):** Following ESET's 2026-06-19 documentation of the group's GentleKiller EDR-killer framework, The Gentlemen ransomware group has claimed an OT-adjacent attack on Mackay Sugar (Australia's second-largest sugar producer), which confirmed on 2026-06-18 that an external party accessed its IT environment around 10 June, halting milling at two of three mills ([The Record, 2026-06-18](https://therecord.media/mackay-sugar-cyberattack-claimed-gentlemen)).

Separately, KrebsOnSecurity reported OSINT attribution identifying the group's administrator — operating as "Hastalamuerte" / "Zeta88" — as Alexander Andreevich Yapaev, a 36-year-old from Izhevsk, Russia, cross-matched across ProtonMail addresses, Telegram IDs and Russian breach corpora ([KrebsOnSecurity, 2026-06-10](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/)). Krebs reports the administrator uses AI tooling to develop ransomware and assist post-exploitation. The attribution is Krebs's analytical claim, not a confirmed indictment; for defenders the operational signal remains the group's 90%-affiliate RaaS model and its BYOVD EDR-kill tradecraft documented on 2026-06-19.
