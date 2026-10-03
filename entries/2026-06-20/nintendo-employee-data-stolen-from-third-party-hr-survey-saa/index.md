---
schema: 1
kind: incident
title: "Nintendo employee data stolen from third-party HR-survey SaaS (TinyPulse), not Nintendo's own systems"
headline: "Nintendo employee data stolen from third-party HR-survey SaaS (TinyPulse), not Nintendo's own systems"
summary: "Nintendo of America confirmed that the extortion group Shadowbyt3$ stole a trove of employee data — not from Nintendo's perimeter, but from TinyPulse, an employee-engagement / pulse-survey SaaS owned by WebMD Health Services (BleepingComputer, 2026-06-18)."
discovered_at: "2026-06-20T05:12:12Z"
event_date: 2026-06-18
run_id: 2026-06-20-4cfd00ef
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - us
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/nintendo-confirms-data-stolen-in-webmd-subsidiary-cyberattack/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.technadu.com/nintendo-confirms-tinypulse-data-stolen-in-shadowbyt3-extortion-attack/629628/"
    publisher: TechNadu
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
migrated_from: briefs/2026-06-20.md
---

Nintendo of America confirmed that the extortion group Shadowbyt3$ stole a trove of employee data — not from Nintendo's perimeter, but from TinyPulse, an employee-engagement / pulse-survey SaaS owned by WebMD Health Services ([BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/nintendo-confirms-data-stolen-in-webmd-subsidiary-cyberattack/)). The exfiltrated dataset (2016–early 2026) reportedly includes employee names, email addresses, W-9 tax forms, bank-statement PDFs and HR analytics ([TechNadu, 2026-06-18](https://www.technadu.com/nintendo-confirms-tinypulse-data-stolen-in-shadowbyt3-extortion-attack/629628/)). The actors demanded USD 2 million from Nintendo on 12 June with a 48-hour deadline; when Nintendo refused, they redirected extortion to TinyPulse directly and began releasing samples. Nintendo characterised the exposure as "internal survey content" for a small subset of employees — narrower than the attacker's claims.

**Defender takeaway:** HR/engagement SaaS tenants (TinyPulse, Glint, Culture Amp, Leapsome, Qualtrics) routinely store financial-onboarding documents far beyond their nominal survey use-case and are under-weighted in third-party risk reviews. Enforce DLP classification on uploads to these platforms, inventory what data classes each tenant actually retains in its own cloud storage, and treat SSO integrations whose SaaS keeps a separate credential store as a lateral-movement path from one compromised employee credential to the vendor's full dataset.
