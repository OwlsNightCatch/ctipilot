---
schema: 1
kind: incident
title: >
  DragonForce lists Geneva's IFAGE adult-education foundation on its leak site, claiming 850 GB —
  an attribution and volume IFAGE has not confirmed
headline: >
  DragonForce claims 850 GB from Geneva's IFAGE, layering an unconfirmed extortion listing onto a
  narrower April breach the foundation already disclosed
summary: >
  DragonForce has listed IFAGE — the Fondation pour la formation des adultes à Genève, a Geneva
  adult-education foundation — on its extortion leak site, claiming 850 GB of exfiltrated data
  (Inside IT, 2026-07-14). IFAGE had already disclosed a narrower April 2026 employee-data
  exfiltration; the DragonForce attribution and the 850 GB figure are single-sourced and
  unconfirmed by IFAGE. Treat as a watch item, not a confirmed breach.
discovered_at: "2026-07-14T20:22:57Z"
updated_at: "2026-07-26T13:58:00Z"
event_date: 2026-07-14
run_id: 2026-07-14T2009Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - switzerland
  - europe
sectors:
  - education
  - public-sector
entities:
  - "actor:dragonforce"
  - "incident:ifage-geneva-dragonforce-leak-claim-2026-07"
techniques:
  - T1657
affected_products: []
cves: []
sources:
  - url: "https://www.inside-it.ch/ransomware-bande-bekennt-sich-zu-angriff-auf-genfer-erwachsenenbildung-20260714"
    publisher: Inside IT Switzerland
    date: 2026-07-14
    role: primary
  - url: "https://latele.ch/articles/la-fondation-ifage-a-geneve-victime-d-une-cyberattaque"
    publisher: "La Télé"
    date: 2026-05-15
    role: corroborating
  - url: "https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147"
    publisher: 20 minutes (Switzerland)
    date: 2026-07-24
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse"
    publisher: ICTjournal
    date: 2026-07-17
    role: corroborating
closed_sources: []
evidence:
  - quote: Die Gruppe Dragonforce will 850 Gigabyte an Daten von Ifage erbeutet haben. Die Stiftung hatte bereits vor einem Abfluss sensibler Daten gewarnt.
    publisher: Inside IT Switzerland
  - quote: "Des données usuelles de collaborateurs ont été compromises"
    publisher: "La Télé"
  - quote: "Des photos de pièces d'identité, des adresses e-mail et postales, ainsi que des numéros de téléphone ou encore des résultats d'examens ont été publiés."
    publisher: 20 minutes
  - quote: "Leur divulgation par les cybercriminels concerne tant des employés de l'institut que des bénéficiaires (étudiants, entreprises, etc.)."
    publisher: 20 minutes
verification: single-source
sourcing_note: >
  The DragonForce attribution and the 850 GB figure rest on a single C-reliability outlet (Inside
  IT) and are unconfirmed by IFAGE or any second outlet; IFAGE's leak-site entry was not visible
  among ransomware.live's most recent listings at fetch time. The underlying April 2026 intrusion
  is separately victim-confirmed (La Télé, citing IFAGE) but narrower in scope, with no vector
  disclosed — so no exploitation technique can be mapped. Framed as a watch item per the fake-news
  guard's handling of uncorroborated leak-site claims, matching the earlier MedusaLocker/Canton of
  Zürich Baudirektion item (2026-07-02).
confidence: low
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 3
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-26T13:58:00Z"
    run_id: 2026-07-26T1308Z-audit
    type: update
    summary: >
      DragonForce published the data it stole from IFAGE, the Geneva adult-education foundation, on
      2026-07-23. The published set includes identity-document photographs, e-mail and postal
      addresses, telephone numbers and multi-year student exam results running to 2026 — categories
      that contradict the institute's earlier public position that the incident affected employee data
      rather than student and pedagogical records. The disclosure covers both staff and beneficiaries;
      the group posted a ransom ultimatum that IFAGE says never reached it; it has filed a criminal
      complaint and is working with cantonal police and federal authorities.
    fields:
      - evidence
      - sectors
      - sources
      - body
    merged_from: 2026-07-26/ifage-geneva-dragonforce-data-published-student-records
migrated_from: null
---

The German-title source reads "the DragonForce group claims to have captured 850 gigabytes of data from IFAGE; the foundation had already warned of a leak of sensitive data." IFAGE (Fondation pour la formation des adultes à Genève), a Geneva adult-education foundation, disclosed in May 2026 that it suffered an intrusion on 11–12 April 2026 (detected 13 April): unauthorized exfiltration of current- and former-employee data, no ransom demand recorded at the time, reported to the Federal Data Protection and Transparency Commissioner, and described by IFAGE as resolved ([La Télé, 2026-05-15](https://latele.ch/articles/la-fondation-ifage-a-geneve-victime-d-une-cyberattaque)). On 14 July 2026, Swiss IT outlet Inside IT reported that the extortion group DragonForce has now listed IFAGE on its leak site, claiming 850 GB — an order of magnitude beyond the scope IFAGE described, and a specific actor attribution IFAGE itself never made ([Inside IT, 2026-07-14](https://www.inside-it.ch/ransomware-bande-bekennt-sich-zu-angriff-auf-genfer-erwachsenenbildung-20260714)). No IFAGE statement responding to the listing, and no second independent outlet corroborating the DragonForce name or the 850 GB figure, could be located as of this run.

**Defender takeaway:** for Swiss defenders this is situational awareness of DragonForce activity against a home-region education institution, not an actionable incident — the intrusion vector was never disclosed, so there is no transferable technique, and the leak-site claim is unverified. The relevant posture is to watch for victim confirmation or a second-source corroboration and, if IFAGE or affected staff are in your constituency, to anticipate the follow-on identity-abuse and targeted-phishing risk that an 850 GB employee-data dump would create if the claim proves real. This item exists to keep the DragonForce-vs-Swiss-public-sector thread visible; if corroboration emerges it should ship as a delta on this entry rather than a fresh report.

## Update — 2026-07-26T13:58:00Z

The DragonForce listing against IFAGE — the Fondation pour la formation des adultes à Genève — is no longer an unverified leak-site claim. The group carried out its threat and published the data, which Le Temps reported had been done as of Thursday 2026-07-23: "Des photos de pièces d'identité, des adresses e-mail et postales, ainsi que des numéros de téléphone ou encore des résultats d'examens ont été publiés." — identity-document photographs, e-mail and postal addresses, telephone numbers and examination results ([20 minutes, 2026-07-24](https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147)). The same report states that their disclosure by the cybercriminals "concerne tant des employés de l'institut que des bénéficiaires (étudiants, entreprises, etc.)" — it covers both the institute's employees and its beneficiaries, meaning students and companies. It also cites an expert consulted by Le Temps who put the exposure at thousands of documents spanning several years and running to 2026. ICTjournal had reported the extortion threat a week earlier ([ICTjournal, 2026-07-17](https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse)).

The operationally interesting part is the gap between the victim's scoping and the published set. IFAGE's earlier public account of its incident placed the impact on employee data rather than student or pedagogical records; the leak contains multi-year examination results for students. First coverage flagged that the group's claimed volume already exceeded the institute's own disclosure, and publication has now settled that discrepancy in the attackers' favour. Nothing in the reporting identifies the initial-access vector, so no access-path lesson is available from this incident.

**Contradiction:** the sources and the victim do not agree on whether a ransom was ever demanded, and this entry does not resolve it. 20 minutes frames the publication as the consequence of an unpaid demand — "Si la rançon demandée n'était pas payée, les pirates informatiques qui s'en sont pris en avril à l'Ifage (Fondation pour la formation des adultes à Genève) promettaient de mettre en ligne les données dérobées" — while also reporting the foundation's own position that "La fondation avait aussi affirmé qu'elle n'avait pas reçu de demande de rançon, mais que, le cas échéant, elle refuserait de payer": it had received no ransom demand, but would refuse to pay if one came ([20 minutes, 2026-07-24](https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147)). ICTjournal is more definite on the demand's existence, reporting a week earlier that a ransom was now being demanded and that the group threatened to publish at the expiry of the ultimatum posted on its leak site ([ICTjournal, 2026-07-17](https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse)). A leak-site ultimatum naming a ransom the victim says never reached it is a common pattern and not necessarily either party misspeaking — demands are frequently posted publicly rather than delivered.

**Defender takeaway:** for Swiss and European public-sector and education bodies, the reusable point is about disclosure discipline under extortion rather than about DragonForce's tradecraft. A scope statement issued before forensics are complete tends to describe what the victim has confirmed, not what the attacker holds, and a leak-site publication is the moment that difference becomes public — organisations should scope their public statements to what they can defend after the data is released, and plan notification obligations for the categories in the attacker's possession rather than the categories confirmed so far. Where an institution's records include identity documents and examination results, the affected-person notification set extends well beyond staff.
