---
schema: 1
kind: threat
title: "A recurring wave of data-leak claims against French departmental fire-and-rescue services (SDIS) hits seven more units, with SDIS du Gard confirming a theft; separately, SDIS 66 confirms a theft that forced crews back to paper and radio"
headline: "SDIS 66 confirms theft of patient rescue forms; crews are back to paper and radio"
summary: >
  Over the last weekend of August 2026 a criminal actor published fresh data-leak claims against
  seven more French Services départementaux d'incendie et de secours (SDIS: Somme, Essonne,
  Bas-Rhin, Bouches-du-Rhône, Gard, Vosges and Moselle), extending a campaign first documented in
  July 2026 against five other SDIS. Contacted directly, SDIS du Gard's board president confirmed the intrusion and theft of personal data on personnel, with identity-document copies and bank details said to be among it; the other six units named in this wave remain unconfirmed criminal claims.
  SDIS 66 (Pyrénées-Orientales) then confirmed on 2026-10-01 that data was stolen from a server maintained by a technical provider, which holds patient rescue forms that can contain medical data and copies of identity documents, and that crews now fill
  in the forms by hand and transmit by radio; a forum claim of nearly 120,000 records is unverified.
discovered_at: "2026-08-31T05:00:00Z"
updated_at: "2026-10-02T05:01:06Z"
event_date: "2026-08-30"
run_id: 2026-08-31T0411Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime]
regions: [europe]
sectors: [public-sector]
entities: ["campaign:france-sdis-data-leaks-2026", "actor:chimeraz", "actor:cybernox", "actor:aplagroup", "incident:sdis-66-data-theft-2026-09"]
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-08-30"
    role: primary
  - url: "https://www.objectifsud.fr/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
    publisher: "Objectif Gard"
    date: "2026-08-30"
    role: primary
  - url: "https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-07-26"
    role: primary
  - url: "https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412"
    publisher: "ICI / Radio France"
    date: "2026-10-01"
    role: primary
closed_sources: []
evidence:
  - quote: "SDIS du Gard was indeed the victim of a cyberattack and data theft. Contacted this Sunday 30 August by Objectif Gard, Alexandre Pissas, chairman of SDIS 30's board, confirms the computer attack and the theft of personal data concerning personnel."
    original: "Le SDIS du Gard a bien été victime d'une cyberattaque et d'un vol de données. Contacté ce dimanche 30 août par Objectif Gard, Alexandre Pissas, président du conseil d'administration du SDIS 30, confirme l'attaque informatique ainsi que le vol de données personnelles concernant les personnels."
    publisher: "Objectif Gard"
    source_url: "https://www.objectifsud.fr/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
  - quote: "Among the stolen information are said to be particularly sensitive data, notably copies of identity documents and bank details."
    original: "Parmi les informations dérobées figureraient des données particulièrement sensibles, notamment des copies de pièces d'identité et des coordonnées bancaires."
    publisher: "Objectif Gard"
    source_url: "https://www.objectifsud.fr/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
  - quote: "this data can help map personnel, roles, technical structures, hierarchical relationships and digital infrastructure of the French rescue services"
    original: "ces données peuvent contribuer à cartographier personnels, fonctions, structures techniques, relations hiérarchiques et infrastructures numériques des secours français"
    publisher: "ZATAZ.COM"
    source_url: "https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/"
  - quote: "SDIS 66 confirms it was the victim of a data theft. (translated from French)"
    original: "Le SDIS 66 confirme avoir été victime d’un vol de données."
    publisher: "ICI / Radio France"
    source_url: "https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412"
  - quote: "the forms are now written by hand and transmissions are made by radio (translated from French)"
    original: "les fiches sont désormais rédigées à la main et les transmissions se font par radio"
    publisher: "ICI / Radio France"
    source_url: "https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412"
verification: single-source
sourcing_note: "SDIS du Gard's victimisation is independently confirmed on the record by its own board president via Objectif Gard's direct contact. The other six SDIS named in this wave (Somme, Essonne, Bas-Rhin, Bouches-du-Rhône, Vosges, Moselle) remain unconfirmed criminal-forum claims relayed only by ZATAZ; no common intrusion vector has been established across any of the incidents in this campaign. SDIS 66's theft and its operational effects are confirmed by SDIS 66 itself to Radio France; the claimed volume of nearly 120,000 records is a forum claim that ICI could not verify, and no source links it to the actors named elsewhere in this campaign."
confidence: medium
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
  - at: "2026-10-02T05:01:06Z"
    run_id: 2026-10-02T0404Z-intel
    type: update
    summary: >
      SDIS 66 confirmed on 2026-10-01 that data was stolen from a provider-maintained server that holds patient rescue
      forms, which can contain medical data and identity-document copies, and that crews now work on paper and radio;
      a forum claim of nearly 120,000 records is unverified. ICI notes it comes a month after the SDIS du Gard attack;
      no source links the two or names an actor. The earlier text now says the identity-document and bank-detail theft
      at SDIS du Gard is reported as said to be among the stolen data.
    fields: [title, headline, summary, entities, sources, evidence, sourcing_note, body]
migrated_from: null
---

Over the last weekend of August 2026 a criminal actor published fresh data-leak claims against seven more French Services départementaux d'incendie et de secours (Somme, Essonne, Bas-Rhin, Bouches-du-Rhône, Gard, Vosges and Moselle), extending a campaign ZATAZ first documented in late July 2026 against five other SDIS (Aisne, Alpes-de-Haute-Provence, Landes, Marne, Alpes-Maritimes), where postings were attributed to three separate criminal-forum handles: ChimeraZ, Cybernox and AplaGroup ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/)). Of the August wave, Objectif Gard names only ChimeraZ, tying the same handle to five of the seven units (Gard, Bouches-du-Rhône, Moselle, Bas-Rhin and Vosges); no source names an actor for the Somme or Essonne claims, or ties Cybernox or AplaGroup to this wave. This is not merely a criminal claim: contacted directly on 30 August, the president of SDIS du Gard's governing board confirmed the cyberattack and theft of personal data on personnel, with copies of identity documents and bank details said to be among it, and the full scope and intrusion method still under investigation ([Objectif Gard, 2026-08-30](https://www.objectifsud.fr/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php)).

No common intrusion vector has been established across the incidents in this campaign. The one case with a stated mechanism is from the July wave: SDIS de l'Aisne, where a claimed administrator-level access credential was posted in cleartext by the actor; ZATAZ notes its current validity cannot be established from the post alone, since access can be disabled or changed after disclosure, but the posting itself is a more critical indicator than a plain directory extraction ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/)). The July wave's cumulative claims, spanning the Landes, Marne (2,167 people), Alpes-Maritimes (2,325 people), Alpes-de-Haute-Provence and Aisne SDIS, plus separate claims against SDIS d'Indre-et-Loire (2,637 public-service agents plus 54 individuals linked to private structures) and the Pompiers.fr / Fédération nationale des sapeurs-pompiers de France membership platform ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/)), totalled at least 166,376 exposed individuals, with a potential total exceeding 932,376 depending on the volumes claimed; ZATAZ is explicit that this estimate is a straight sum of announced record counts and does not mean each line was technically verified or maps to a distinct person ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/)). Each publication in the campaign otherwise appears to be a distinct claim rather than evidence of one coordinated technical compromise.

**Defender takeaway:** the pattern that matters is not any single leak's volume but the aggregation risk. Personnel identity, rank, assignment, hierarchical role, contact details and, in the Aisne case, an exposed administrative credential, accumulated across repeated incidents against the same category of organisation, builds a reconnaissance dataset usable for targeted phishing, impersonation or infrastructure mapping against emergency-services personnel specifically. That is the same organisational category as Swiss cantonal and communal fire and rescue services; treat personnel-directory applications and any administrative credentials at emergency-services organisations as high-value reconnaissance and access targets even where any single leak's data looks individually low-sensitivity, and assume that recurring incidents against peer organisations are building a profiling dataset regardless of whether your own organisation has been named yet.

## Update — 2026-10-02T05:01:06Z

SDIS 66, the fire and rescue service of the Pyrénées-Orientales, confirmed to Radio France on 2026-10-01 that data was stolen from one of its servers, which is maintained by a technical provider ([ICI / Radio France, 2026-10-01](https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412)). The data includes the rescue forms crews fill in at a patient's home or an accident scene, which can hold medical data, intervention reports, contact details and copies of identity documents or Vitale health-insurance cards, and SDIS 66 says the nature and extent are still being identified ([ICI / Radio France, 2026-10-01](https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412)). A crisis cell was opened and the system that transmits the documents was blocked to stop further leakage, so the forms are now written by hand and transmitted by radio to keep rescue operations running ([ICI / Radio France, 2026-10-01](https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412)). On 2026-09-30 a forum user claimed nearly 120,000 records and 100,000 documents, figures ICI says cannot be verified, and ICI notes the incident comes a month after the SDIS du Gard attack ([ICI / Radio France, 2026-10-01](https://www.ici.fr/infos/faits-divers-justice/le-sdis-66-victime-d-une-fuite-de-donnees-7983412)). The reporting names no intrusion vector and no actor, and no source links the SDIS 66 theft to the SDIS du Gard attack or to the forum claims against other units.
