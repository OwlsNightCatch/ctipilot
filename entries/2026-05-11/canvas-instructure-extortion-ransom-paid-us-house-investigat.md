---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Canvas / Instructure extortion — ransom paid, US House investigation, second-intrusion vulnerability re-exploited"
headline: "Canvas / Instructure extortion — ransom paid, US House investigation, second-intrusion vulnerability re-exploited"
summary: The W19 weekly closed with the Canvas / Instructure extortion deadline of 2026-05-12 pending.
discovered_at: "2026-05-11T05:00:06Z"
event_date: 2026-05-13
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - organized-crime
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
    publisher: The Record
    role: primary
  - url: "https://homeland.house.gov/2026/05/11/chairman-garbarino-seeks-information-from-canvas-developer-after-cyberattacks-impact-schools-and-universities-nationwide/"
    publisher: US House Homeland Security Committee
    role: corroborating
  - url: "https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access"
    publisher: NL Times — Dutch universities disconnect Canvas
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
migrated_from: briefs/weekly/2026-W20.md
---

The W19 weekly closed with the Canvas / Instructure extortion deadline of 2026-05-12 pending. The trajectory through W20: **Tuesday 2026-05-12:** Instructure confirmed ransom payment to ShinyHunters with claimed data return and digital confirmation of destruction; second intrusion separately confirmed; per-institution leak deadline reset to the same day ([daily 2026-05-12 UPDATE](/briefs/2026-05-12/); [The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation)). **Wednesday 2026-05-13:** the US House Homeland Security Committee (Chairman Garbarino) opened a formal investigation and requested an Instructure CEO briefing by 2026-05-21 covering both intrusion circumstances, scope and nature of accessed data, IR adequacy, and CISA coordination ([House Homeland Security Committee letter, 2026-05-11](https://homeland.house.gov/2026/05/11/chairman-garbarino-seeks-information-from-canvas-developer-after-cyberattacks-impact-schools-and-universities-nationwide/); [daily 2026-05-13 UPDATE](/briefs/2026-05-13/)). **Post-payment:** ShinyHunters defaced approximately 330 institutional Canvas login pages by re-exploiting the same Free-For-Teacher account vulnerability that enabled the second intrusion — demonstrating that the "no customer extortion" covenant in the ransom agreement was at best narrowly observed and that the access vector was not actually closed ([The Record](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation)).

The story matters to Swiss / EU public-sector defenders for three reasons that crystallise only across the multi-day arc. First, **paying the ransom did not close the access vector**: Instructure's patches did not eliminate the Free-For-Teacher abuse path, so the defacement wave is operational evidence that the underlying flaw remained exploitable; this is the "what did the patch actually fix" question every IR-receiving organisation should be asking of every paid-ransom-with-promised-fix vendor. Second, **the seven Dutch universities** (VU Amsterdam, UvA, Erasmus, Tilburg, TU/e, Maastricht, Twente) **disconnected Canvas** rather than wait for vendor remediation ([NL Times, 2026-05-09](https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access)) — a defender posture worth pattern-matching for any future SaaS-LMS / SaaS-LRS / SaaS-grade-management vendor compromise. Third, the **US House investigation** is the regulatory analogue Swiss / EU SOC managers should anticipate from cantonal education ministries; the questions Chairman Garbarino's letter lists (intrusion timeline, data scope, IR adequacy, CISA / national-CSIRT coordination) are the same questions a cantonal Bildungsdirektion will ask after the next EdTech SaaS incident. Outcome of the 2026-05-21 briefing is the open horizon item for 2026-W21.
