---
schema: 1
kind: incident
horizon: operational
title: >
  Instructure/Canvas extortion: 330 institutions across six countries; May 12 extortion deadline;
  44 Dutch institutions confirmed
headline: >
  Instructure/Canvas extortion: 330 institutions across six countries; May 12 extortion deadline;
  44 Dutch institutions confirmed
summary: "(First covered 2026-05-06.) The Instructure/Canvas breach has expanded significantly in scope."
discovered_at: "2026-05-08T05:00:15Z"
updated_at: "2026-05-13T05:00:12Z"
event_date: null
run_id: 2026-05-08-migrated
priority: high
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
  - cryptocrime
  - identity
regions:
  - europe
  - uk
  - global
  - us
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.surf.nl/actualiteiten/2026/canvas-security-update"
    publisher: SURF Security Advisory — Canvas Extortion Update
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/"
    publisher: "BleepingComputer — Instructure Canvas data breach, 2026-05-06"
    role: primary
  - url: "https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/"
    publisher: "Techzine EU, 2026-05-08"
    role: primary
  - url: "https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/"
    publisher: "DutchNews.nl, 2026-05-08"
    role: corroborating
  - url: "https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361"
    publisher: "The Register, 2026-05-12"
    role: primary
  - url: "https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers"
    publisher: "Inside Higher Ed, 2026-05-11"
    role: corroborating
  - url: "https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/"
    publisher: "Infosecurity Magazine, 2026-05-11"
    role: corroborating
  - url: "https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation"
    publisher: "The Record, 2026-05-12"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927"
    publisher: "The Register, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-09T05:00:13Z"
    run_id: 2026-05-09-migrated
    type: update
    summary: "UPDATE (originally covered 2026-05-08):"
    fields:
      - regions
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-05-09/canvas-instructure-extortion-oxford-cambridge-liverpool-issu
  - at: "2026-05-10T05:00:08Z"
    run_id: 2026-05-10-001
    type: update
    summary: >
      **Canvas/Instructure UPDATE — ShinyHunters claims a second intrusion despite the May 8 patch and
      "continued active access". Seven Dutch universities (VU Amsterdam, UvA, Erasmus, Tilburg, TU/e,
      Maastricht, Twente) executed emergency Canvas disconnects on/before 2026-05-09; Dutch DPA
      notified by VU Amsterdam.** Original 2026-05-12 extortion deadline now two days away;
      Instructure rotated application keys and required customer API client re-authorisation.
    fields:
      - entities
      - priority
      - sources
      - body
    merged_from: 2026-05-10/canvas-instructure-shinyhunters-claims-a-second-intrusion-de
  - at: "2026-05-12T05:00:05Z"
    run_id: 2026-05-12-cd1ab844
    type: update
    summary: >
      **Instructure paid ShinyHunters; double Canvas intrusion confirmed; per-institution leak
      deadline is today (2026-05-12).** Ransom acknowledged and "shred logs" received for the
      platform-wide dataset; a second intrusion on 2026-05-07 defaced ~330 institution portals via the
      same Free-for-Teacher flaw, and ShinyHunters has now set a fresh per-institution payment
      deadline (The Register, 2026-05-12). European universities reliant on Canvas should treat the
      platform-wide settlement as legally unverifiable destruction.
    fields:
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-05-12/instructure-canvas-lms-ransom-paid-to-shinyhunters-with-shre
  - at: "2026-05-13T05:00:12Z"
    run_id: 2026-05-13-c148b9a5
    type: update
    summary: >
      UPDATE (originally covered 2026-05-12): Late on 2026-05-11, US House Homeland Security Committee
      Chairman Andrew Garbarino sent a formal letter to Instructure CEO Steve Daly ahead of the
      2026-05-12 ShinyHunters extortion deadline, demanding a briefing by 2026-05-21 on the
      circumstances of both Canvas intrusions …
    fields:
      - regions
      - sources
      - body
    merged_from: 2026-05-13/instructure-canvas-us-house-homeland-security-committee-open
migrated_from: briefs/2026-05-08.md
---

(First covered 2026-05-06.) The Instructure/Canvas breach has expanded significantly in scope. The threat actor now claims access affecting **330 institutions** across six countries, threatening to publish 16 million student and staff records. **SURF** (the Dutch National Research and Education Network) has confirmed **44 Dutch institutions** among the victims. The attacker posted portal defacements at multiple universities and established a **2026-05-12 extortion deadline** for ransom payment. Canvas services were taken offline again on 2026-05-07 for emergency patching. European DPAs in the Netherlands and Germany have opened preliminary inquiries into notification timing. Institutions using Canvas should assess GDPR Article 33/34 breach notification obligations before the May 12 deadline.

## Update — 2026-05-09T05:00:13Z

As of the window close (2026-05-09 06:00 UTC), no ransom payment has been made and no further data dump has been published. Three major UK universities issued public statements: **University of Oxford** confirmed it is working with Instructure and the NCSC-UK; **University of Cambridge** issued a statement acknowledging that "student and staff data may have been affected" and referred staff to the National Cyber Security Centre guidance; **University of Liverpool** confirmed it had notified the Information Commissioner's Office under Article 33 GDPR and is conducting a forensic investigation. **Universiteiten van Nederland (UNL)** confirmed that 44 member institutions are potentially affected, representing all Dutch research universities and applied science universities; the Dutch DPA (Autoriteit Persoonsgegevens) has opened a preliminary investigation.

The threat actor (WorldLeaks) set a **2026-05-12 payment deadline**; the extortion amount was stated as €3.2 million. WorldLeaks previously published a 3 GB sample dataset on 2026-05-07 containing course-IDs, student email addresses, assignment metadata, and grade records across four UK institutions. No passwords, payment data, or national identification numbers were present in the sample. Instructure issued a public statement on 2026-05-08 confirming the breach vector was a compromised integration service account for a third-party LTI tool provider (not Canvas core infrastructure), and that the issue was isolated. Instructure stated it notified affected institutions on 2026-05-01 and has been working with law enforcement.

## Update — 2026-05-10T05:00:08Z

ShinyHunters posted a second intrusion notice around 2026-05-08 asserting Instructure's Canvas LMS retained unpatched vulnerabilities allowing re-entry despite the company's earlier security-patch deployment ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/) · [DutchNews.nl, 2026-05-08](https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/)). Instructure confirmed the second breach, rotated application keys, increased monitoring, and required API-client re-authorisation across its customer base.

Seven Dutch universities — **VU Amsterdam, University of Amsterdam, Erasmus University Rotterdam, Tilburg University, Eindhoven University of Technology (TU/e), Maastricht University, and University of Twente** — executed emergency Canvas disconnections on or before 2026-05-09 after the attackers claimed continued active access. The Dutch Data Protection Authority (Autoriteit Persoonsgegevens) received an incident report from VU Amsterdam.

The 2026-05-12 extortion deadline remains active — two days from publication. ShinyHunters's original claim cited 275 million records (names, email addresses, student IDs, private messages) across thousands of educational institutions worldwide ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/)); if the second-intrusion claim is verified, Instructure's remediation was incomplete and the data-release threat is materially more credible. Defenders at European universities using Canvas should treat credential-stuffing risk on stolen student / staff emails as active, audit third-party LTI integrations, and watch for follow-on phishing campaigns referencing course content.

## Update — 2026-05-12T05:00:05Z

Instructure on 2026-05-11 disclosed that it "reached an agreement with the unauthorized actor" and received "digital confirmation of data destruction (shred logs)" — a ransom payment in everything but name, undisclosed amount, covering the platform-wide ~3.65 TB dataset that ShinyHunters claimed to have lifted from Canvas's Free-for-Teacher tier on 2026-04-29 ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers); [Infosecurity Magazine, 2026-05-11](https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/)).

Two material developments accompany the settlement: (a) Instructure confirmed a **second intrusion on 2026-05-07** in which ShinyHunters defaced approximately 330 individual institution login portals via the same Free-for-Teacher vulnerability — the first ITW evidence that the underlying flaw remained exploitable post-patch; (b) ShinyHunters has now **reset a per-institution payment deadline to end-of-day 2026-05-12** (today), positioning the central settlement as covering only the bulk dataset while leaving individual institutions exposed to targeted publication ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). CEO Steve Daly publicly acknowledged delayed external communication ("we got the balance wrong" on disclosure timing). CrowdStrike remains engaged for the IR work.

Operational reality for any European university running Canvas: the "data was destroyed" claim is not technically verifiable — by ransomware-actor practice, the artefact provided is typically a hash list or a video, not a forensically meaningful proof of deletion. The dataset must continue to be treated as compromised in perpetuity for GDPR / Swiss DSG purposes, downstream phishing risk planning, and student-identity exposure communications. Institutions that received the per-institution deadline note should validate that any locally-stored Canvas-derived data (course rosters, communications, gradebooks) is included in the breach-notification scope, regardless of the platform-wide settlement.

## Update — 2026-05-13T05:00:12Z

Late on 2026-05-11, US House Homeland Security Committee Chairman Andrew Garbarino sent a formal letter to Instructure CEO Steve Daly ahead of the 2026-05-12 ShinyHunters extortion deadline, demanding a briefing by 2026-05-21 on the circumstances of both Canvas intrusions, the volume of data accessed, containment measures, and coordination with federal law enforcement and CISA ([The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation); [The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927)).

On 2026-05-12 — before the deadline expired — Instructure confirmed it had "reached an agreement with the unauthorized actor" and received "digital confirmation of data destruction (shred logs)" from ShinyHunters, the operational reliability of which the committee letter explicitly questions. ShinyHunters claims the agreement covers up to 275 million records across roughly 8,800 colleges, universities and K-12 schools (per The Register; The Record cites ~9,000 institutions), including Dutch and Swedish higher-education customers previously confirmed in scope. The second Canvas intrusion is attributed to ShinyHunters exploiting an unpatched flaw in Instructure's "Free-for-Teacher" environment; the initial 2026-04-29 intrusion yielded ~3.6 TB of uncompressed data (usernames, emails, course names, messages). CrowdStrike was retained for forensic analysis.

Defender takeaway: a vendor-side "shred log" is legally non-binding and technically unverifiable; EU institutions must continue to treat the 275M-record dataset as irrevocably compromised for GDPR Art. 33 / data-subject-rights purposes regardless of Instructure's bulk-platform claim. The congressional investigation will likely prompt CISA guidance for higher-education SaaS incident response — relevant context for Swiss universities and EU edtech procurement teams.
