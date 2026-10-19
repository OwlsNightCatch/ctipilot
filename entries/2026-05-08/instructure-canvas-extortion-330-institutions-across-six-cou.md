---
schema: 1
kind: incident
title: "Instructure Canvas breach: ShinyHunters exploits a Free-for-Teacher flaw twice, defaces about 330 login portals, and Instructure reaches an agreement with the actor"
headline: "ShinyHunters claims 275 million records from Canvas; Instructure struck an agreement with the gang after a second intrusion defaced school portals"
summary: >
  ShinyHunters stole names, email addresses, student IDs and messages from Instructure's Canvas through a
  vulnerability in its Free-for-Teacher system, claiming about 275 million records from about 8,800
  schools, then defaced about 330 school login portals through the same flaw on 2026-05-07. Seven Dutch
  universities disconnected Canvas. Instructure announced an agreement with the actor on 2026-05-11, and a
  US House committee requested a briefing.
discovered_at: "2026-05-08T05:00:15Z"
updated_at: "2026-05-13T05:00:12Z"
event_date: "2026-04-29"
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
  - cryptocrime
  - identity
regions:
  - europe
  - global
  - us
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
techniques: [T1190, T1491.002, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/"
    publisher: "BleepingComputer"
    date: "2026-05-03"
    role: primary
  - url: "https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361"
    publisher: "The Register"
    date: "2026-05-12"
    role: primary
  - url: "https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/"
    publisher: "Techzine EU"
    date: "2026-05-08"
    role: corroborating
  - url: "https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/"
    publisher: "DutchNews.nl"
    date: "2026-05-08"
    role: corroborating
  - url: "https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers"
    publisher: "Inside Higher Ed"
    date: "2026-05-11"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/"
    publisher: "Infosecurity Magazine"
    date: "2026-05-11"
    role: corroborating
  - url: "https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation"
    publisher: "The Record"
    date: "2026-05-12"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927"
    publisher: "The Register"
    date: "2026-05-12"
    role: corroborating
  - url: "https://nltimes.nl/2026/05/05/canvas-hack-student-data-44-dutch-universities-schools-taken-massive-breach"
    publisher: "NL Times"
    date: "2026-05-05"
    role: corroborating
  - url: "https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access"
    publisher: "NL Times"
    date: "2026-05-09"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
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
  - at: "2026-10-11T14:19:55Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      Most of the headline figures had no source: 330 was the number of defaced login portals, not institutions; six countries, 16 million records, 44 Dutch institutions confirmed as victims and German or Dutch regulator inquiries appear nowhere (the 44 are names on the actor's own list); the actor is ShinyHunters, not WorldLeaks, and no EUR 3.2 million demand, 3 GB sample or LTI service-account vector was reported. The entry is rewritten from its sources, the earlier sections are corrected in place (dates of the second notice and the agreement, Instructure's statement that the agreement covers all customers, unsupported UK university statements and speculation removed), the dead SURF source is dropped, and the entry gains its rating and ATT&CK mapping. Priority moves from high to notable. NL Times is added as the source for the seven Dutch universities that disconnected Canvas. The agreement sentence is cited to Inside Higher Ed alone, the Dutch disconnections to NL Times, and the Free-for-Teacher attribution in the 2026-05-09 section is marked as a later statement.
    fields: [title, headline, summary, event_date, priority, techniques, sources, verification, sourcing_note, classification, body, regions]
migrated_from: briefs/2026-05-08.md
---

Instructure detected unauthorized activity on 2026-04-29 ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)) and disclosed a security incident on Friday, 2026-05-01 ([BleepingComputer, 2026-05-03](https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/)). It said the information involved covers names, email addresses, student ID numbers and messages among users of affected institutions, with no evidence that passwords, dates of birth, government identifiers or financial information were involved ([BleepingComputer, 2026-05-03](https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/)). ShinyHunters claimed the attack, first for "nearly 9,000 schools" and 275 million individuals ([BleepingComputer, 2026-05-03](https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/)), later for about 3.65 TB holding about 275 million records from about 8,800 schools ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). Instructure says the criminals exploited a vulnerability in its Free-for-Teacher learning system; on 2026-05-07 ShinyHunters used the same vulnerability to deface about 330 Canvas school login portals, and Instructure took Canvas into maintenance mode to contain the activity ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). Seven Dutch universities disconnected Canvas ([NL Times, 2026-05-09](https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access)), and VU Amsterdam notified the Dutch data protection authority ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/)).

After ShinyHunters set a final deadline of end of day 2026-05-12 for individual institutions to negotiate ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)), Instructure said on 2026-05-11 that it had reached an agreement with the actor, received "digital confirmation of data destruction (shred logs)" and an assurance that no Instructure customers would be extorted as a result of the incident ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers)). The chairman of the US House Homeland Security Committee asked Instructure for a briefing on both intrusions ([The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation)). Instructure retained CrowdStrike for forensic analysis and incident response ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)).

**Defender takeaway:** the agreement does not make the data safe: treat the names, email addresses, student IDs and messages of Canvas users as exposed when planning breach notifications and phishing awareness, whatever the vendor's destruction confirmation says.

## Update — 2026-05-09T05:00:13Z

Instructure later attributed the intrusion to a vulnerability in its Free-for-Teacher learning system, and ShinyHunters set a pay-or-leak deadline for 2026-05-12 ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)).

## Update — 2026-05-10T05:00:08Z

ShinyHunters left a message on Canvas on the evening of Thursday 2026-05-07 after breaking in again ([DutchNews.nl, 2026-05-08](https://www.dutchnews.nl/2026/05/hackers-break-into-ed-tech-giant-again-after-massive-data-heist/)). Seven Dutch universities, VU Amsterdam, the University of Amsterdam, Erasmus University Rotterdam, Tilburg University, Eindhoven University of Technology, Maastricht University and the University of Twente, disconnected Canvas ([NL Times, 2026-05-09](https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access)), and VU Amsterdam reported the incident to the Dutch data protection authority ([Techzine EU, 2026-05-08](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/)). After the first incident Instructure had deployed patches, increased monitoring and rotated application keys ([BleepingComputer, 2026-05-03](https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/)).

## Update — 2026-05-12T05:00:05Z

On 2026-05-11 Instructure said it had reached a deal with the actor and received "digital confirmation of data destruction (shred logs)", without disclosing the deal's monetary value ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers)). Instructure also confirmed the second intrusion of 2026-05-07, in which about 330 school login portals were defaced through the same Free-for-Teacher vulnerability ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). ShinyHunters had set a final deadline of end of day 2026-05-12 for individual institutions to contact it, and Instructure's statement says no customers will be extorted as a result of the incident ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)); ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers)). CrowdStrike is assisting with the forensic analysis ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)).

## Update — 2026-05-13T05:00:12Z

Late on 2026-05-11, US House Homeland Security Committee Chairman Andrew Garbarino wrote to Instructure CEO Steve Daly requesting a briefing by 2026-05-21 on both Canvas intrusions, the volume of data accessed, containment measures and coordination with federal law enforcement and CISA ([The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation)); ([The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/congress-investigates-canvas-breach-after-instructure-cuts-deal-with-shinyhunters/5238927)). The same evening Instructure announced its agreement with ShinyHunters ([The Record, 2026-05-12](https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation)). ShinyHunters' claim covers about 275 million records from about 8,800 schools ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)).

## Correction — 2026-10-11T14:19:55Z

ShinyHunters claims about 275 million records from about 8,800 schools; about 330 is the number of school login portals it defaced on 2026-05-07 ([The Register, 2026-05-12](https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)). No source supports the earlier figures of 330 institutions in six countries or 16 million records, and the 44 Dutch institutions are names on ShinyHunters' own victim list as BNR reviewed it, not confirmed victims ([NL Times, 2026-05-05](https://nltimes.nl/2026/05/05/canvas-hack-student-data-44-dutch-universities-schools-taken-massive-breach)); seven Dutch universities disconnected Canvas ([NL Times, 2026-05-09](https://nltimes.nl/2026/05/09/dutch-universities-disconnect-canvas-hackers-claim-continued-access)). Instructure attributes both intrusions to a vulnerability in its Free-for-Teacher system, not to a compromised LTI integration account, and the actor is ShinyHunters; the earlier references to WorldLeaks, a EUR 3.2 million demand, a 3 GB sample and German or Dutch regulator inquiries had no source. Instructure announced its agreement with the actor on 2026-05-11 and said no customers would be extorted as a result ([Inside Higher Ed, 2026-05-11](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers)).
