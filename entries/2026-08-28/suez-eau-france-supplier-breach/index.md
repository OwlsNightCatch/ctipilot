---
schema: 1
kind: incident
title: "SUEZ Eau France notifies customers of a technical service provider's breach — identity, contract and, for some customers, bank and identity-document data exposed"
headline: "A French water utility's supplier breach reaches customer identity documents and bank details, sourced only through specialist trackers"
summary: >
  SUEZ Eau France (10M+ users) is notifying customers of a security incident at a technical
  service provider, compromised by a cyberattack that allowed data access and extraction, with
  part of the exfiltrated data subsequently made accessible online. Affected data may include
  name, contact details, contract/billing documents, and for some customers identity documents,
  photographs and bank details. No major outlet or SUEZ public statement was located; sourcing is
  three independent specialist trackers each stating they obtained the customer notification
  letter directly.
discovered_at: "2026-08-28T06:46:00Z"
updated_at: null
event_date: "2026-08-20"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain]
regions: [europe]
sectors: [water, public-sector]
entities: [incident:suez-eau-france-supplier-breach-2026-08]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://fuitesinfos.fr/article/2026-08-20-suez-eau-france"
    publisher: "Fuites Infos (specialist breach tracker)"
    date: "2026-08-20"
    role: primary
  - url: "https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/"
    publisher: "Cyberattaque.org (specialist breach tracker)"
    date: "2026-08-20"
    role: corroborating
  - url: "https://christophemazzola.fr/en/articles/fuites-donnees-france-aout-2026"
    publisher: "Christophe Mazzola (independent security analyst)"
    date: "2026-08-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "it is a technical service provider used by SUEZ Eau France that is reported to have been compromised. (translated from French)"
    original: "c'est un prestataire technique utilisé par SUEZ Eau France qui aurait été compromis"
    publisher: "Cyberattaque.org (specialist breach tracker)"
  - quote: "certain information exchanged with its customers during the period concerned may have been exposed. (translated from French)"
    original: "certaines informations échangées avec ses clients pendant la période concernée peuvent avoir été exposées"
    publisher: "Cyberattaque.org (specialist breach tracker)"
  - quote: "Technical supplier to Suez Eau France | not disclosed. Bank details, identity documents, contractual papers | Confirmed"
    publisher: "Christophe Mazzola (independent security analyst)"
verification: single-source-victim
sourcing_note: >
  This is treated as a single-source victim disclosure: the underlying source in every
  case is SUEZ's own customer notification letter, independently obtained and quoted by three
  distinct specialist breach-tracking outlets, none of which is itself an Admiralty B-or-above
  outlet, and no SUEZ public statement, CNIL filing, or major-press pickup was located despite a
  multi-query fair-attempt search across major French and international outlets (Le Monde, AFP,
  Reuters, France24, 20 Minutes, BFMTV, Le Parisien). Three independent relays of one first-party
  document is genuine multi-outlet confirmation that the notification exists and says what is
  reported, even though no relaying outlet itself carries an established Admiralty B+ reliability
  track record — credibility is set at 2 rather than 1 to reflect that the underlying claim itself
  (what was actually taken, how many customers, over what period) still rests on SUEZ's own letter
  alone, not on independent verification of its contents.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [evidence, sourcing_note, body]
migrated_from: null
---

SUEZ Eau France (serving 10M+ users in France, per its own figures) is notifying customers of a security incident at one of its technical service providers, which was compromised by a cyberattack that allowed data access and extraction, with part of the exfiltrated data subsequently made accessible online: "it is a technical service provider used by SUEZ Eau France that is reported to have been compromised" (translated from French) ([Cyberattaque.org, quoting the SUEZ customer notification, 2026-08-20](https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/)).

Per the notification — quoted or paraphrased independently by three specialist trackers who each state they obtained a copy — affected data may include name, contact details, contract and billing administrative documents, and for some customers identity documents, photographs and bank details (RIB/IBAN): "certain information exchanged with its customers during the period concerned may have been exposed" (translated from French) ([Cyberattaque.org, quoting the SUEZ customer notification, 2026-08-20](https://www.cyberattaque.org/suez-les-donnees-clients-en-fuite-apres-une-cyberattaque-chez-un-prestataire/)); an independent analyst roundup records the same categories as confirmed: "technical supplier to Suez Eau France | not disclosed. Bank details, identity documents, contractual papers | Confirmed" ([Christophe Mazzola, 2026-08-22](https://christophemazzola.fr/en/articles/fuites-donnees-france-aout-2026)). SUEZ states it cannot yet confirm that every notified person's data was actually stolen, and no total affected-count or exact period has been disclosed.

All available sourcing is three independent specialist breach-tracking sites relaying the same underlying SUEZ customer notification letter; no SUEZ public statement or CNIL filing has been located, and nothing about how the attacker first got into the supplier's environment is disclosed. The confirmed outcome is customer data extracted from the technical supplier's own systems — a supplier-origin exposure reaching a water utility serving over 10 million users, the same shape as several other supplier-origin European disclosures this month.
