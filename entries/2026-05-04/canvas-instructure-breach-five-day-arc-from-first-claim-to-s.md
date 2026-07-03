---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: Canvas / Instructure breach — five-day arc from first claim to seven Dutch universities executing emergency disconnects
headline: Canvas / Instructure breach — five-day arc from first claim to seven Dutch universities executing emergency disconnects
summary: "Canvas / Instructure — second intrusion claim against Instructure on 2026-05-08 despite the May 8 patches; seven Dutch universities (VU Amsterdam, UvA, Erasmus, Tilburg, TU/e, Maastricht, Twente) executed emergency Canvas disconnects on or before 2026-05-09; the extortion deadline is 2026-05-12 (Tuesday). (Techzine EU · DutchNews.nl · daily 2026-05-10)"
discovered_at: "2026-05-04T05:00:07Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: high
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
  - supply-chain
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
  - url: "https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/"
    publisher: BleepingComputer — Instructure Canvas data breach
    role: primary
  - url: "https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/"
    publisher: Techzine EU — Dutch university disconnects
    role: corroborating
  - url: "https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/"
    publisher: DutchNews.nl — Hackers break into ed-tech giant again
    role: corroborating
  - url: "https://nltimes.nl/2026/05/05/canvas-hack-student-data-44-dutch-universities-schools-taken-massive-breach"
    publisher: "NL Times — Canvas hack: student data from 44 Dutch universities and schools taken"
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

Canvas / Instructure is the cleanest example of a campaign chain that accumulated meaningfully different state every day of 2026-W19, and the one a SOC manager carries into Monday morning with an extortion deadline two days out. Day-by-day: **2026-05-06** — Instructure confirmed names, email addresses, student ID numbers, and user-to-user messages accessed; detected API-tool disruption ~2026-04-30; revoked privileged credentials and access tokens; passwords / financial data / government IDs out of scope; ShinyHunters claimed 275 M records across ~9,000 institutions including EU and APAC ([BleepingComputer, 2026-05-04](https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/) · [TechCrunch, 2026-05-05](https://techcrunch.com/2026/05/05/hackers-steal-students-data-during-breach-at-education-tech-giant-instructure/) · [SecurityWeek, 2026-05-04](https://www.securityweek.com/edtech-firm-instructure-discloses-data-breach/) · [daily 2026-05-06](/briefs/2026-05-06/)). **2026-05-07** — individual universities (University of Nevada Reno, University of Pennsylvania ~300,000+ users) began notifying students and staff directly ([University of Nevada Reno president message, 2026-05-06](https://www.unr.edu/nevada-today/news/president-messages/2026-05-06-cybersecurity-incident) · [daily 2026-05-07 UPDATE](/briefs/2026-05-07/)). **2026-05-08** — SURF (Dutch NREN) confirmed 44 Dutch institutions among victims; attacker posted portal defacements; 2026-05-12 extortion deadline set; Canvas taken offline for emergency patching on 2026-05-07 ([NL Times — Canvas hack: student data from 44 Dutch universities and schools taken](https://nltimes.nl/2026/05/05/canvas-hack-student-data-44-dutch-universities-schools-taken-massive-breach) · [The Next Web — largest education data breach in history](https://thenextweb.com/news/the-largest-education-data-breach-in-history-was-not-an-attack-on-a-school-it-was-an-attack-on-a-vendor) · [daily 2026-05-08 UPDATE](/briefs/2026-05-08/)). **2026-05-09** — three major UK universities (Oxford, Cambridge, Liverpool — Liverpool notified ICO under GDPR Article 33) issued public statements; UNL confirmed 44 Dutch member institutions; 3 GB sample dump on 2026-05-07 contained course-IDs, student emails, assignment metadata, grade records across four UK institutions; Instructure stated the breach vector was a compromised integration service account for a third-party LTI tool provider (not Canvas core infrastructure). The ShinyHunters / WorldLeaks operator-family attribution and the specific extortion-amount figure carried in the daily UPDATE trace to sources not re-fetched at weekly composition time; readers should consult the daily UPDATE for the citation chain ([daily 2026-05-09 UPDATE](/briefs/2026-05-09/)). **2026-05-10** — ShinyHunters posted a *second* intrusion notice 2026-05-08 asserting Canvas retained unpatched vulnerabilities permitting re-entry despite the May 8 patches; Instructure confirmed the second breach, rotated application keys, increased monitoring, and required API-client re-authorisation; seven Dutch universities (**VU Amsterdam, University of Amsterdam, Erasmus Rotterdam, Tilburg, Eindhoven TU/e, Maastricht, Twente**) executed emergency Canvas disconnections on/before 2026-05-09; Dutch DPA (Autoriteit Persoonsgegevens) received an incident report from VU Amsterdam ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/) · [DutchNews.nl, 2026-05-08](https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/) · [daily 2026-05-10 UPDATE](/briefs/2026-05-10/)).

State at week-end: **2026-05-12 extortion deadline is Tuesday (two days out)**; no ransom paid as of 2026-05-09 06:00 UTC; if the second-intrusion claim verifies, Instructure's remediation was incomplete and the data-release threat is materially more credible. European universities running Canvas should treat credential-stuffing risk on stolen student / staff emails as active; audit third-party LTI integrations and revoke service accounts for unused integrations; watch for follow-on phishing campaigns referencing course content. GDPR Article 33/34 notification clocks run from the date Instructure provided scope confirmation to the institution.
