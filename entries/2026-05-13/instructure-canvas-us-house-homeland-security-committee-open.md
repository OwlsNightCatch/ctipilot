---
schema: 1
kind: incident
horizon: operational
title: "Instructure Canvas — US House Homeland Security Committee opens formal investigation; Instructure paid ransom"
headline: "Instructure Canvas — US House Homeland Security Committee opens formal investigation; Instructure paid ransom"
summary: "UPDATE (originally covered 2026-05-12): Late on 2026-05-11, US House Homeland Security Committee Chairman Andrew Garbarino sent a formal letter to Instructure CEO Steve Daly ahead of the 2026-05-12 ShinyHunters extortion deadline, demanding a briefing by 2026-05-21 on the circumstances of both Canvas intrusions …"
discovered_at: "2026-05-13T05:00:12Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - data-breach
  - ransomware
  - identity
regions:
  - us
  - europe
sectors:
  - education
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation"
    publisher: "The Record, 2026-05-12"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927"
    publisher: "The Register, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-12/instructure-canvas-lms-ransom-paid-to-shinyhunters-with-shre
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
---

**UPDATE (originally covered 2026-05-12):** Late on 2026-05-11, US House Homeland Security Committee Chairman Andrew Garbarino sent a formal letter to Instructure CEO Steve Daly ahead of the 2026-05-12 ShinyHunters extortion deadline, demanding a briefing by 2026-05-21 on the circumstances of both Canvas intrusions, the volume of data accessed, containment measures, and coordination with federal law enforcement and CISA ([The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation); [The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927)).

On 2026-05-12 — before the deadline expired — Instructure confirmed it had "reached an agreement with the unauthorized actor" and received "digital confirmation of data destruction (shred logs)" from ShinyHunters, the operational reliability of which the committee letter explicitly questions. ShinyHunters claims the agreement covers up to 275 million records across roughly 8,800 colleges, universities and K-12 schools (per The Register; The Record cites ~9,000 institutions), including Dutch and Swedish higher-education customers previously confirmed in scope. The second Canvas intrusion is attributed to ShinyHunters exploiting an unpatched flaw in Instructure's "Free-for-Teacher" environment; the initial 2026-04-29 intrusion yielded ~3.6 TB of uncompressed data (usernames, emails, course names, messages). CrowdStrike was retained for forensic analysis.

Defender takeaway: a vendor-side "shred log" is legally non-binding and technically unverifiable; EU institutions must continue to treat the 275M-record dataset as irrevocably compromised for GDPR Art. 33 / data-subject-rights purposes regardless of Instructure's bulk-platform claim. The congressional investigation will likely prompt CISA guidance for higher-education SaaS incident response — relevant context for Swiss universities and EU edtech procurement teams.
