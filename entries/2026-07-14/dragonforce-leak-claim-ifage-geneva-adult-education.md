---
schema: 1
kind: incident
horizon: operational
title: "DragonForce lists Geneva's IFAGE adult-education foundation on its leak site, claiming 850 GB — an attribution and volume IFAGE has not confirmed"
headline: "DragonForce claims 850 GB from Geneva's IFAGE, layering an unconfirmed extortion listing onto a narrower April breach the foundation already disclosed"
summary: >
  DragonForce has listed IFAGE — the Fondation pour la formation des adultes à Genève, a Geneva adult-education
  foundation — on its extortion leak site, claiming 850 GB
  of exfiltrated data (Inside IT, 2026-07-14). IFAGE had already disclosed a narrower April 2026 employee-data
  exfiltration; the DragonForce attribution and the 850 GB figure are single-sourced and unconfirmed by IFAGE.
  Treat as a watch item, not a confirmed breach.
discovered_at: "2026-07-14T20:22:57Z"
event_date: "2026-07-14"
run_id: 2026-07-14T2009Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland, europe]
sectors: [education]
entities: [actor:dragonforce, incident:ifage-geneva-dragonforce-leak-claim-2026-07]
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.inside-it.ch/ransomware-bande-bekennt-sich-zu-angriff-auf-genfer-erwachsenenbildung-20260714"
    publisher: "Inside IT Switzerland"
    date: "2026-07-14"
    role: primary
  - url: "https://latele.ch/articles/la-fondation-ifage-a-geneve-victime-d-une-cyberattaque"
    publisher: "La Télé"
    date: "2026-05-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Die Gruppe Dragonforce will 850 Gigabyte an Daten von Ifage erbeutet haben. Die Stiftung hatte bereits vor einem Abfluss sensibler Daten gewarnt."
    publisher: "Inside IT Switzerland"
  - quote: "Des données usuelles de collaborateurs ont été compromises"
    publisher: "La Télé"
verification: single-source
sourcing_note: "The DragonForce attribution and the 850 GB figure rest on a single C-reliability outlet (Inside IT) and are unconfirmed by IFAGE or any second outlet; IFAGE's leak-site entry was not visible among ransomware.live's most recent listings at fetch time. The underlying April 2026 intrusion is separately victim-confirmed (La Télé, citing IFAGE) but narrower in scope, with no vector disclosed — so no exploitation technique can be mapped. Framed as a watch item per the fake-news guard's handling of uncorroborated leak-site claims, matching the earlier MedusaLocker/Canton of Zürich Baudirektion item (2026-07-02)."
confidence: low
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

The German-title source reads "the DragonForce group claims to have captured 850 gigabytes of data from IFAGE; the foundation had already warned of a leak of sensitive data." IFAGE (Fondation pour la formation des adultes à Genève), a Geneva adult-education foundation, disclosed in May 2026 that it suffered an intrusion on 11–12 April 2026 (detected 13 April): unauthorized exfiltration of current- and former-employee data, no ransom demand recorded at the time, reported to the Federal Data Protection and Transparency Commissioner, and described by IFAGE as resolved ([La Télé, 2026-05-15](https://latele.ch/articles/la-fondation-ifage-a-geneve-victime-d-une-cyberattaque)). On 14 July 2026, Swiss IT outlet Inside IT reported that the extortion group DragonForce has now listed IFAGE on its leak site, claiming 850 GB — an order of magnitude beyond the scope IFAGE described, and a specific actor attribution IFAGE itself never made ([Inside IT, 2026-07-14](https://www.inside-it.ch/ransomware-bande-bekennt-sich-zu-angriff-auf-genfer-erwachsenenbildung-20260714)). No IFAGE statement responding to the listing, and no second independent outlet corroborating the DragonForce name or the 850 GB figure, could be located as of this run.

**Defender takeaway:** for Swiss defenders this is situational awareness of DragonForce activity against a home-region education institution, not an actionable incident — the intrusion vector was never disclosed, so there is no transferable technique, and the leak-site claim is unverified. The relevant posture is to watch for victim confirmation or a second-source corroboration and, if IFAGE or affected staff are in your constituency, to anticipate the follow-on identity-abuse and targeted-phishing risk that an 850 GB employee-data dump would create if the claim proves real. This item exists to keep the DragonForce-vs-Swiss-public-sector thread visible; if corroboration emerges it should ship as a delta on this entry rather than a fresh report.
