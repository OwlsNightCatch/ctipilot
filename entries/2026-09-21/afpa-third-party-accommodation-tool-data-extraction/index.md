---
schema: 1
kind: incident
title: "AFPA (France's national adult vocational-training agency) confirms a data extraction potentially affecting up to 1.7 million people, traced to a flaw in a third-party-hosted accommodation-management tool"
headline: "AFPA confirms a breach in a vendor-hosted tool after two criminal claims a day apart point to the same third-party flaw"
summary: >
  AFPA, France's national public adult vocational-training agency, has
  confirmed a potential data extraction after two criminal-forum claims surfaced 24 hours apart in
  mid-September 2026. AFPA's own investigation traced the extraction to a flaw in a third-party-hosted
  tool it uses to manage worker accommodation, external to its own information system; up to
  1.7 million people are potentially affected, with identity, address and possibly phone-number data
  confirmed by AFPA and additional fields reported by independent breach trackers.
discovered_at: "2026-09-21T04:48:00Z"
updated_at: null
event_date: "2026-09-20"
run_id: 2026-09-21T0410Z-intel
priority: notable
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
  Clubic is mainstream French consumer-technology journalism (Admiralty B) relaying an AFP wire story
  that quotes AFPA's own deputy director directly to the press — a victim-side statement, not a bare
  repetition of a criminal's claim. Cyberattaque.org (Admiralty C, a claim-based community tracker) and
  FrenchBreaches (Admiralty B) are the two niche breach-tracking outlets; both independently paraphrase
  AFPA's own confirmation and the third-party-tool explanation rather than merely relaying the criminals'
  figures, which is what moves this to multi-source rather than the single-source-victim carve-out. Their
  own sample reviews diverge on the email-address field: Cyberattaque.org's samples showed it largely
  empty, while FrenchBreaches' samples showed it, and nationality, populated — both details are cited to
  their respective source below rather than jointly. The Cyberattaque.org page is cited to 2026-09-19
  (its dateModified), not its original 2026-09-15 publish date: its own body narrates the 2026-09-16
  Cybernox announcement as already past, which the content actually live on 2026-09-15 could not have
  done, confirming the cited content was updated after first publication. AFPA's own website carries no
  dedicated press notice reachable from its public news listing, and franceinfo's original article (the
  ultimate AFP-quote primary) returned HTTP 403 on every transport attempted on 2026-09-21; Clubic's direct
  quotation is the best available anchor for AFPA's own words. AFPA has not confirmed the IDOR mechanism
  one of the two criminal claimants describes, and has not stated whether the two claimed datasets
  (971,420 and 1,732,811 records) overlap. AFPA is a French, not Swiss, agency, so this entry rests on a
  double ground rather than home-region domicile alone: it is itself a national public-sector agency
  (the profile's primary-sector criterion, matched directly rather than by analogy), and the potential
  scale — up to 1.7 million people — is large enough on its own terms to carry a transferable
  third-party-vendor-trust lesson regardless of the victim's home country.
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
updates: []
migrated_from: null
---

AFPA (Agence nationale pour la formation des adultes), France's national public adult vocational-training agency, has confirmed a "potential data extraction" after two criminal-forum claims surfaced within 24 hours of each other in mid-September 2026 ([Clubic, 2026-09-20](https://www.clubic.com/actualite-630454-cyberattaque-de-lafpa-jusqua-17-million-de-dossiers-potentiellement-compromis-apres-une-faille-dun-prestataire.html)). The handle xMetah first offered 971,420 records for sale on 2026-09-15; the following day, Cybernox — separately tracked for exposing 101 AFPA accounts a month earlier, with no established link between that exposure and this extraction — claimed 1,732,811 records via an alleged insecure direct object reference (IDOR) flaw ([Cyberattaque.org, 2026-09-19](https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/)). AFPA's own investigation traced the "potential extraction" to a flaw in a third-party-hosted tool it uses to manage worker accommodation, which AFPA's deputy director Pierre Prady told AFP is external to the agency's own information system, so there was "a priori" no impact on AFPA's own services. AFPA has not confirmed the IDOR mechanism Cybernox claims, and has not stated whether the two claimed datasets overlap or were extracted from the same source; FrenchBreaches states the two figures must not simply be summed to declare a combined victim count ([FrenchBreaches, 2026-09-19](https://frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8)). AFPA states the affected application held identity, address and possibly phone-number data, with no banking data or French national ID (Sécurité sociale) numbers identified so far; Cyberattaque.org's own sample review additionally found full dates of birth, internal identifiers and a "partner" field (one observed value, "LHEA," suggesting a partner-feed origin), while noting that several fields provisioned for email addresses, a second phone number or other contact details were observed empty in its samples ([Cyberattaque.org, 2026-09-19](https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/)); FrenchBreaches' separate, independent sample review instead found populated email addresses and nationality fields, in records spanning creation or modification dates from 2006 through 2026 ([FrenchBreaches, 2026-09-19](https://frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8)). Clubic's reporting notes AFPA has not stated whether it has notified the CNIL, despite GDPR's 72-hour breach-notification requirement.

**Defender takeaway:** an agency's own security posture does not bound its exposure once it delegates a function — worker accommodation management, in this case — to an externally-hosted third-party tool; that tool's own access controls become part of the agency's attack surface even though it sits, in AFPA's own words, outside the agency's information system. Any organization relying on an externally-hosted administrative SaaS tool for HR-adjacent or personnel-management functions should confirm that vendor's own vulnerability-disclosure and breach-notification obligations are contractually defined, rather than discovering them after a criminal-forum listing forces the question.
