---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "ARWINI (Lower Saxony prescription-audit body) — exfiltration confirmed; Kairos claims 2.87 TB including ~70,000 GDPR Art. 9 records"
headline: "ARWINI (Lower Saxony prescription-audit body) — exfiltration confirmed; Kairos claims 2.87 TB including ~70,000 GDPR Art. 9 records"
summary: Investigators confirmed on 2026-05-18 that the cyberattack on ARWINI — the body that audits prescription cost-effectiveness for statutory health insurers in Lower Saxony — exfiltrated data after a 4 May intrusion.
discovered_at: "2026-05-18T05:00:20Z"
event_date: 2026-05-18
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - dach
  - europe
sectors:
  - healthcare
  - public-sector
entities:
  - "actor:kairos-extortion"
cves: []
sources:
  - url: "https://www.aerzteblatt.de/news/hackerangriff-auf-rezeptprufer-c259a70c-595b-4770-9d84-87f6c8338c0c"
    publisher: "Deutsches Ärzteblatt"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W21.md
---

Investigators confirmed on [2026-05-18](/briefs/2026-05-19/) that the cyberattack on ARWINI — the body that audits prescription cost-effectiveness for statutory health insurers in Lower Saxony — exfiltrated data after a 4 May intrusion. The Kairos ransomware group claims 2.87 TB, with roughly 70,000 special-category (Art. 9) health records in scope. This is the second DACH healthcare-adjacent data-theft event of the window after Unimed, reinforcing that the sector's softest surfaces are the administrative and audit intermediaries, not the hospitals' clinical systems.
