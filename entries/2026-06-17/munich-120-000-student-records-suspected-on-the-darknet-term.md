---
schema: 1
kind: incident
horizon: operational
title: "Munich: ~120,000 student records suspected on the darknet — terminated employee under investigation"
headline: "Munich: ~120,000 student records suspected on the darknet — terminated employee under investigation"
summary: "120,000 Munich student records suspected on the darknet — a City-of-Munich IT subsidiary reports a suspected insider-threat mass export; Bavarian DPA notified, criminal complaint filed — a direct EU public-sector deprovisioning lesson (§ 1)."
discovered_at: "2026-06-17T05:14:25Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: high
immediate_action: null
tags:
  - data-breach
  - insider-threat
  - identity
regions:
  - dach
  - europe
sectors:
  - education
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.heise.de/news/Datenschutzvorfall-in-Muenchen-120-000-sensible-Schuldaten-im-Darknet-11333920.html"
    publisher: "Heise Security, 2026-06-16"
    role: primary
  - url: "https://lhm-services.de/wp-content/uploads/2026/06/Pressemitteilung_LHM-Services-GmbH_15.06.2026-1.pdf"
    publisher: "LHM-Services GmbH press release, 2026-06-15"
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
migrated_from: briefs/2026-06-17.md
---

LHM-Services GmbH, the municipal IT subsidiary of the City of Munich that runs school-administration systems for Bavarian schools, is investigating a suspected data-protection incident involving roughly 120,000 students — names, addresses, dates of birth, nationalities and school assignments (the 120,000 figure originates in press reporting; LHM-Services says it learned of the incident from the press and questioned whether the data was actually publicly available) ([Heise Security, 2026-06-16](https://www.heise.de/news/Datenschutzvorfall-in-Muenchen-120-000-sensible-Schuldaten-im-Darknet-11333920.html)). The investigation, led by Munich's cybercrime unit and the Bamberg prosecutor, centres on a former employee suspected of having mass-downloaded and retained the dataset shortly before leaving — i.e. a suspected insider data-theft, not an external intrusion. A darknet-research firm engaged by LHM-Services found no evidence the data was publicly listed for sale at the time of writing, so the actual circulation scope is uncertain. LHM-Services notified the Bavarian State Data Protection Authority under GDPR Article 33 and filed a criminal complaint ([LHM-Services GmbH press release, 2026-06-15](https://lhm-services.de/wp-content/uploads/2026/06/Pressemitteilung_LHM-Services-GmbH_15.06.2026-1.pdf)).

**Defender takeaway:** The root cause is the universal public-sector control gap — access deprovisioning for departing staff who hold export rights over centralised citizen/student data. Hunt for bulk export/download events (Windows EID 4663 object access; DLP/UEBA volume thresholds) by accounts flagged for offboarding, and bind database read/export credentials to just-in-time access tied to the HR offboarding workflow rather than only disabling the directory account. The exposure mirrors any Swiss canton or municipality running centralised school/citizen data through a third-party processor (GDPR/DPA Art. 5(1)(f) accountability extends to the processor).
