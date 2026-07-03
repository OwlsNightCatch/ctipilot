---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "Healthcare (CH, NL)"
headline: "Healthcare (CH, NL)"
summary: "Two healthcare incidents define the sector picture this week, both with European public-sector concentration. Groupe 3R (Switzerland) — Akira leak-site listing on a Romandie medical-imaging operator running 20 centres across seven cantons; the operator confirmed publicly on 2026-04-30, will not pay ransom, and is …"
discovered_at: "2026-05-04T05:00:12Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - organized-crime
regions:
  - switzerland
  - europe
sectors:
  - healthcare
entities:
  - "actor:embargo"
  - "actor:akira"
cves: []
sources:
  - url: "https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/"
    publisher: Groupe 3R victim statement
    role: primary
  - url: "https://therecord.media/chipsoft-ransomware-attack-disrupts-dutch-hospitals"
    publisher: The Record — ChipSoft
    role: corroborating
  - url: "https://nltimes.nl/2026/04/29/chipsoft-hackers-destroyed-stolen-patient-data-leaks"
    publisher: NL Times — ChipSoft destroyed claim
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
migrated_from: briefs/weekly/2026-W19.md
---

Two healthcare incidents define the sector picture this week, both with European public-sector concentration. **Groupe 3R (Switzerland)** — Akira leak-site listing on a Romandie medical-imaging operator running 20 centres across seven cantons; the operator confirmed publicly on 2026-04-30, will not pay ransom, and is operating with legacy examination data still inaccessible at week-end ([Groupe 3R victim statement](https://www.groupe3r.ch/fr/information-importante-perturbation-de-nos-services-7268/) · [daily 2026-05-10](/briefs/2026-05-10/)). **ChipSoft (Netherlands)** — The 7 April 2026 attack on the Dutch healthcare software vendor — whose HiX platform serves roughly 70% of Dutch hospitals — was first reported with attacker identity unknown ([The Record, 2026-04-09](https://therecord.media/chipsoft-ransomware-attack-disrupts-dutch-hospitals)); the **Embargo** ransomware group's claim of responsibility, alongside the 66 Dutch DPA notifications, was reported in the subsequent NL Times follow-up. On 28–29 April ChipSoft stated the exfiltrated data had been destroyed in language Dutch security experts noted strongly implies a ransom was paid (ChipSoft did not confirm) ([NL Times, 2026-04-29](https://nltimes.nl/2026/04/29/chipsoft-hackers-destroyed-stolen-patient-data-leaks) · [daily 2026-05-07](/briefs/2026-05-07/)). Both incidents reinforce the same cross-finding pattern: ransomware operators' claims of data destruction are inherently unverifiable; GDPR breach-notification obligations and long-term breach-response posture do not expire when an attacker says they deleted the copy.
