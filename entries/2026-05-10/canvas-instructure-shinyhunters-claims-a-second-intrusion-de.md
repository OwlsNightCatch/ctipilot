---
schema: 1
kind: incident
horizon: operational
title: "Canvas/Instructure — ShinyHunters claims a *second* intrusion despite May 8 patches; seven Dutch universities executed emergency disconnects on/before May 9"
headline: "Canvas/Instructure — ShinyHunters claims a *second* intrusion despite May 8 patches; seven Dutch universities executed emergency disconnects on/before May 9"
summary: "**Canvas/Instructure UPDATE — ShinyHunters claims a second intrusion despite the May 8 patch and \"continued active access\". Seven Dutch universities (VU Amsterdam, UvA, Erasmus, Tilburg, TU/e, Maastricht, Twente) executed emergency Canvas disconnects on/before 2026-05-09; Dutch DPA notified by VU Amsterdam.** Original 2026-05-12 extortion deadline now two days away; Instructure rotated application keys and required customer API client re-authorisation."
discovered_at: "2026-05-10T05:00:08Z"
event_date: 2026-05-08
run_id: 2026-05-10-001
priority: high
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
regions:
  - europe
  - uk
  - global
sectors:
  - education
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/"
    publisher: "Techzine EU, 2026-05-08"
    role: primary
  - url: "https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/"
    publisher: "DutchNews.nl, 2026-05-08"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
---

**UPDATE (originally covered 2026-05-08; previous UPDATE 2026-05-09):** ShinyHunters posted a second intrusion notice around 2026-05-08 asserting Instructure's Canvas LMS retained unpatched vulnerabilities allowing re-entry despite the company's earlier security-patch deployment ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/) · [DutchNews.nl, 2026-05-08](https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/)). Instructure confirmed the second breach, rotated application keys, increased monitoring, and required API-client re-authorisation across its customer base.

Seven Dutch universities — **VU Amsterdam, University of Amsterdam, Erasmus University Rotterdam, Tilburg University, Eindhoven University of Technology (TU/e), Maastricht University, and University of Twente** — executed emergency Canvas disconnections on or before 2026-05-09 after the attackers claimed continued active access. The Dutch Data Protection Authority (Autoriteit Persoonsgegevens) received an incident report from VU Amsterdam.

The 2026-05-12 extortion deadline remains active — two days from publication. ShinyHunters's original claim cited 275 million records (names, email addresses, student IDs, private messages) across thousands of educational institutions worldwide ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/)); if the second-intrusion claim is verified, Instructure's remediation was incomplete and the data-release threat is materially more credible. Defenders at European universities using Canvas should treat credential-stuffing risk on stolen student / staff emails as active, audit third-party LTI integrations, and watch for follow-on phishing campaigns referencing course content.
