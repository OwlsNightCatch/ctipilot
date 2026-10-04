---
schema: 1
kind: incident
title: "AFPA (France's national adult vocational-training agency) confirms a data extraction potentially affecting up to 1.7 million people, linked to a flaw in a third-party-hosted accommodation-management tool"
headline: "AFPA links a potential data extraction to a flaw in a vendor-hosted tool after two criminal claims a day apart"
summary: >
  AFPA, France's national public adult vocational-training agency, has
  confirmed a potential data extraction after two criminal-forum claims surfaced 24 hours apart in
  mid-September 2026. AFPA's first investigations link a potential extraction to a flaw in a third-party-hosted accommodation-management tool, external to its own information system; up to
  1.7 million people are potentially affected, with identity, address and possibly phone-number data
  confirmed by AFPA and additional fields reported by independent breach trackers.
discovered_at: "2026-09-21T04:48:00Z"
updated_at: null
event_date: "2026-09-20"
run_id: 2026-09-21T0410Z-intel
priority: routine
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - europe
sectors:
  - public-sector
entities:
  - "actor:cybernox"
  - "actor:xmetah"
  - "incident:afpa-third-party-accommodation-tool-data-extraction-2026-09"
techniques:
  - T1190
  - T1213
affected_products: []
cves: []
sources:
  - url: "https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html"
    publisher: "Clubic (relaying AFP/franceinfo, quoting AFPA deputy director Pierre Prady directly)"
    date: "2026-09-20"
    role: primary
  - url: "https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/"
    publisher: "Cyberattaque.org"
    date: "2026-09-19"
    role: corroborating
  - url: "https://frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8"
    publisher: "FrenchBreaches"
    date: "2026-09-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "According to AFPA, the hacked application contained people's identity and address, and possibly their phone number, but \"a priori\" no banking data or Social Security number. (translated from French)"
    original: "Selon l'Afpa, l'application piratée contenait l'identité et l'adresse des personnes, avec éventuellement leur numéro de téléphone, mais « a priori » aucune donnée bancaire ni aucun numéro de Sécurité sociale."
    publisher: "Clubic"
    source_url: "https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html"
  - quote: "This tool 'is hosted by a third-party vendor and is external to our information system, so there was, a priori, no impact on AFPA's own services and information systems.' (translated from French)"
    original: "Cet outil « est hébergé chez un éditeur tiers et est externe à notre système d'information, donc il n'y a pas eu a priori d'impact sur les services et systèmes d'information de l'Afpa »"
    publisher: "Clubic"
    source_url: "https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html"
  - quote: "AFPA now confirms that a data extraction potentially took place and states that the incident could affect up to 1.7 million people. (translated from French)"
    original: "L'AFPA confirme désormais qu'une extraction de données a potentiellement eu lieu et indique que l'incident pourrait concerner jusqu'à 1,7 million de personnes."
    publisher: "Cyberattaque.org"
    source_url: "https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/"
verification: multi-source
sourcing_note: >
  Clubic relays an AFP wire story quoting AFPA's deputy director. Cyberattaque.org and FrenchBreaches
  paraphrase AFPA's confirmation, and their sample reviews differ on whether email addresses were
  populated.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:04Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority is lowered from notable to routine: a French training-agency data extraction with no
      reusable vector. The body is trimmed to routine-incident length and the sourcing note is plain
      provenance. The title, headline, summary and body now keep AFPA's hedge, a potential
      extraction linked to a flaw in a vendor-hosted accommodation-management tool, instead of
      saying AFPA traced it there. The headline no longer says both claims point to the same flaw,
      the unsourced 'worker' detail is removed, and the claim dates, on which the sources differ,
      are narrowed to a day apart in mid-September.
    fields: [priority, sourcing_note, body, title, headline, summary]
migrated_from: null
---

AFPA, France's national public adult vocational-training agency, confirmed a potential extraction of identity, address and possibly phone-number data on up to 1.7 million people after the handles xMetah and Cybernox claimed 971,420 and 1,732,811 records a day apart in mid-September 2026, figures FrenchBreaches warns must not simply be summed ([Cyberattaque.org, 2026-09-19](https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/) · [Clubic, 2026-09-20](https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html) · [FrenchBreaches, 2026-09-19](https://frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8)). AFPA says its first investigations found the potential extraction linked to a flaw in a third-party-hosted accommodation-management tool outside its own information system, a link it words cautiously, and it has neither confirmed the insecure direct object reference Cybernox describes nor established whether both datasets come from one environment ([Clubic, 2026-09-20](https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html) · [Cyberattaque.org, 2026-09-19](https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/)). It is relevant as a European public agency exposed through a vendor-hosted administrative tool.

**Defender takeaway:** for each externally hosted HR or personnel-management tool, confirm that the vendor's vulnerability-disclosure and breach-notification duties are set in the contract, because that tool's access controls are part of the agency's attack surface even though it sits outside the agency's information system ([Clubic, 2026-09-20](https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html)).

## Correction — 2026-09-30T06:56:04Z

AFPA's statement is hedged: its first investigations found a "potential" data extraction that it links to a flaw in a vendor-hosted accommodation-management tool, and it has not established whether the two claimed datasets were taken from a single environment ([Clubic, 2026-09-20](https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html)). The entry previously said AFPA had traced the extraction to that flaw and that both claims pointed to it.
