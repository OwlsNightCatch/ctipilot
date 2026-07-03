---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Insider and process failures — Munich school data, a lost SSD, and an NHS records caution"
headline: "Insider and process failures — Munich school data, a lost SSD, and an NHS records caution"
summary: "Several of the week's incidents were not external intrusions at all. Munich's municipal IT subsidiary is investigating ~120,000 student records suspected on the darknet, with a terminated employee under investigation (Heise, 2026-06-17; daily 06-17)."
discovered_at: "2026-06-22T00:14:54Z"
event_date: 2026-06-19
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - insider-threat
  - data-breach
regions:
  - dach
  - uk
sectors:
  - education
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.heise.de/news/Datenschutzvorfall-in-Muenchen-120-000-sensible-Schuldaten-im-Darknet-11333920.html"
    publisher: Heise — Munich
    role: primary
  - url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/ico-statement-conclusion-of-criminal-investigation/"
    publisher: ICO statement
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
migrated_from: briefs/weekly/2026-W25.md
---

Several of the week's incidents were not external intrusions at all. Munich's municipal IT subsidiary is investigating ~120,000 student records suspected on the darknet, with a terminated employee under investigation ([Heise, 2026-06-17](https://www.heise.de/news/Datenschutzvorfall-in-Muenchen-120-000-sensible-Schuldaten-im-Darknet-11333920.html); [daily 06-17](/briefs/2026-06-17/)). The Kyushu Electric SSD loss (§ 4) was a physical-custody failure. And the UK ICO closed a two-year criminal investigation into deliberate misuse of Catherine, Princess of Wales' medical records at The London Clinic with a formal caution ([ICO, 2026-06-19](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/ico-statement-conclusion-of-criminal-investigation/); [daily 06-19](/briefs/2026-06-19/)). The common thread: privileged-insider and data-custody controls — offboarding, removable-media encryption, and access auditing on sensitive records — are as consequential as perimeter defence.
