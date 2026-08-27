---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: Looking ahead — 2026-W28
headline: 'Looking ahead — 2026-W28: items already in motion for the coming weeks'
summary: 'Items already in motion, not predictions: the Dutch NIS2 Cyberbeveiligingswet enters into force 15 August 2026 (five weeks out) and the EU Cyber Resilience Act''s 11 September vulnerability/incident-reporting obligation is ~60 days away; FINMA''s post-quantum expectation-setting may harden into a binding circular; the Joomla extension file-upload wave''s newest members (RSFiles!/Phoca) are patched but not yet exploited, and prior wave members reached CISA KEV within days; Unit 42 references an Expel write-up of The Gentlemen''s suspected EDR-disable zero-day that has not yet published; and the STAC3725 initial-access broker continues weaponising CitrixBleed 2 against un-session-terminated NetScaler.'
discovered_at: '2026-07-12T23:56:00Z'
event_date: null
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - law-enforcement
  - ransomware
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - finance
entities: []
cves: []
sources:
  - url: https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht
    publisher: Rijksoverheid.nl (Dutch national government)
    role: primary
  - url: https://www.finma.ch/news/2026/07/20260709-mm-am-05-26/
    publisher: FINMA
    role: primary
  - url: https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/
    publisher: mySites.guru
    role: primary
  - url: https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/
    publisher: Palo Alto Networks Unit 42
    role: primary
  - url: https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware
    publisher: Huntress
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: Each item is an already-in-motion development with a dated primary source or an in-week entry reference — this is a tracking list, not a forecast. Reliability B, credibility 2.
confidence: high
classification:
  reliability: B
  credibility: 2
update_of: null
references:
  - 2026-06-29/netherlands-nis2-cyberbeveiligingswet-clears-the-lower-house
  - 2026-07-12/weekly-w28-finma-post-quantum-guidance
  - 2026-07-12/weekly-w28-joomla-file-upload-rce-wave
  - 2026-06-29/the-gentlemen
  - 2026-07-12/weekly-w28-exploited-edge-enterprise-software
  - 2026-06-29/eu-cyber-resilience-act-75-days-to-the-11-september-vulnerab
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---

Items already in motion for the coming weeks — each with a dated source or an in-week entry, none a prediction:

- **EU regulatory clocks.** The Dutch NIS2 **Cyberbeveiligingswet** enters into force **15 August 2026** — now a fixed date after the 7 July Senate passage ([Rijksoverheid.nl, 2026-07-07](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht)). The **EU Cyber Resilience Act** vulnerability/incident-reporting obligation lands **11 September 2026**, roughly 60 days out and previously covered in this store — the reporting-platform readiness is the item to watch next.
- **FINMA post-quantum guidance may harden.** FINMA's Aufsichtsmitteilung 05/2026 is supervisory expectation-setting, not yet a binding circular; the open question is whether it converts into a Rundschreiben revision ([FINMA, 2026-07-09](https://www.finma.ch/news/2026/07/20260709-mm-am-05-26/)).
- **Joomla file-upload wave — the newest members await exploitation.** RSFiles! and Phoca Download are patched but not yet exploited, whereas earlier members of the same CWE-434 wave reached CISA KEV within days ([mySites.guru, 2026-07-11](https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/)) — treat these as likely-imminent-KEV, not resolved.
- **The Gentlemen EDR-disable zero-day.** Unit 42 references an Expel analysis of a suspected zero-day the group uses to disable EDR, distinct from the GentleKiller BYOVD framework; that write-up had not published at the time of Unit 42's report ([Unit 42, 2026-07-10](https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/)).
- **CitrixBleed 2 broker activity continues.** Huntress' STAC3725 reconstruction shows an initial-access broker actively weaponising CVE-2025-5777; organisations that patched but did not terminate live sessions remain exposed to token replay and downstream DragonForce deployment ([Huntress, 2026-07-10](https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware)).
