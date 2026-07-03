---
schema: 1
kind: incident
horizon: operational
title: "Instructure (Canvas LMS) — ransom paid to ShinyHunters with \"shred logs\"; second intrusion confirmed; per-institution leak deadline reset to today"
headline: "Instructure (Canvas LMS) — ransom paid to ShinyHunters with \"shred logs\"; second intrusion confirmed; per-institution leak deadline reset to today"
summary: "**Instructure paid ShinyHunters; double Canvas intrusion confirmed; per-institution leak deadline is today (2026-05-12).** Ransom acknowledged and \"shred logs\" received for the platform-wide dataset; a second intrusion on 2026-05-07 defaced ~330 institution portals via the same Free-for-Teacher flaw, and ShinyHunters has now set a fresh per-institution payment deadline (The Register, 2026-05-12). European universities reliant on Canvas should treat the platform-wide settlement as legally unverifiable destruction."
discovered_at: "2026-05-12T05:00:05Z"
event_date: 2026-05-12
run_id: 2026-05-12-cd1ab844
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
  - cryptocrime
  - identity
regions:
  - global
  - europe
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361"
    publisher: "The Register, 2026-05-12"
    role: primary
  - url: "https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers"
    publisher: "Inside Higher Ed, 2026-05-11"
    role: corroborating
  - url: "https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/"
    publisher: "Infosecurity Magazine, 2026-05-11"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-09/canvas-instructure-extortion-oxford-cambridge-liverpool-issu
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
---

**UPDATE (originally covered 2026-05-09; updated 2026-05-10):** Instructure on 2026-05-11 disclosed that it "reached an agreement with the unauthorized actor" and received "digital confirmation of data destruction (shred logs)" — a ransom payment in everything but name, undisclosed amount, covering the platform-wide ~3.65 TB dataset that ShinyHunters claimed to have lifted from Canvas's Free-for-Teacher tier on 2026-04-29 ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers); [Infosecurity Magazine, 2026-05-11](https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/)).

Two material developments accompany the settlement: (a) Instructure confirmed a **second intrusion on 2026-05-07** in which ShinyHunters defaced approximately 330 individual institution login portals via the same Free-for-Teacher vulnerability — the first ITW evidence that the underlying flaw remained exploitable post-patch; (b) ShinyHunters has now **reset a per-institution payment deadline to end-of-day 2026-05-12** (today), positioning the central settlement as covering only the bulk dataset while leaving individual institutions exposed to targeted publication ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). CEO Steve Daly publicly acknowledged delayed external communication ("we got the balance wrong" on disclosure timing). CrowdStrike remains engaged for the IR work.

Operational reality for any European university running Canvas: the "data was destroyed" claim is not technically verifiable — by ransomware-actor practice, the artefact provided is typically a hash list or a video, not a forensically meaningful proof of deletion. The dataset must continue to be treated as compromised in perpetuity for GDPR / Swiss DSG purposes, downstream phishing risk planning, and student-identity exposure communications. Institutions that received the per-institution deadline note should validate that any locally-stored Canvas-derived data (course rosters, communications, gradebooks) is included in the breach-notification scope, regardless of the platform-wide settlement.
