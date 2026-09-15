---
schema: 1
kind: threat
title: "A recurring wave of data-leak claims against French departmental fire-and-rescue services (SDIS) hits seven more units, with the first board-level victim confirmation"
headline: "SDIS du Gard's own board confirms the theft a criminal forum had already been claiming for weeks"
summary: >
  Over the last weekend of August 2026 a criminal actor published fresh data-leak claims against
  seven more French Services départementaux d'incendie et de secours (SDIS) — Somme, Essonne,
  Bas-Rhin, Bouches-du-Rhône, Gard, Vosges and Moselle — extending a campaign first documented in
  July 2026 against five other SDIS. Contacted directly, SDIS du Gard's board president confirmed
  the intrusion and theft of personnel identity-document copies and bank details; the other six
  units named in this wave remain unconfirmed criminal claims.
discovered_at: "2026-08-31T05:00:00Z"
updated_at: null
event_date: "2026-08-30"
run_id: 2026-08-31T0411Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime]
regions: [europe]
sectors: [public-sector]
entities: ["campaign:france-sdis-data-leaks-2026", "actor:chimeraz", "actor:cybernox", "actor:aplagroup"]
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-08-30"
    role: primary
  - url: "https://www.objectifgard.com/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
    publisher: "Objectif Gard"
    date: "2026-08-30"
    role: primary
  - url: "https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-07-26"
    role: primary
closed_sources: []
evidence:
  - quote: "SDIS du Gard was indeed the victim of a cyberattack and data theft. Contacted this Sunday 30 August by Objectif Gard, Alexandre Pissas, chairman of SDIS 30's board, confirms the computer attack and the theft of personal data concerning personnel."
    original: "Le SDIS du Gard a bien été victime d'une cyberattaque et d'un vol de données. Contacté ce dimanche 30 août par Objectif Gard, Alexandre Pissas, président du conseil d'administration du SDIS 30, confirme l'attaque informatique ainsi que le vol de données personnelles concernant les personnels."
    publisher: "Objectif Gard"
    source_url: "https://www.objectifgard.com/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
  - quote: "Among the stolen information are said to be particularly sensitive data, notably copies of identity documents and bank details."
    original: "Parmi les informations dérobées figureraient des données particulièrement sensibles, notamment des copies de pièces d'identité et des coordonnées bancaires."
    publisher: "Objectif Gard"
    source_url: "https://www.objectifgard.com/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php"
  - quote: "this data can help map personnel, roles, technical structures, hierarchical relationships and digital infrastructure of the French rescue services"
    original: "ces données peuvent contribuer à cartographier personnels, fonctions, structures techniques, relations hiérarchiques et infrastructures numériques des secours français"
    publisher: "ZATAZ.COM"
    source_url: "https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/"
verification: single-source
sourcing_note: "SDIS du Gard's victimisation is independently confirmed on the record by its own board president via Objectif Gard's direct contact. The other six SDIS named in this wave (Somme, Essonne, Bas-Rhin, Bouches-du-Rhône, Vosges, Moselle) remain unconfirmed criminal-forum claims relayed only by ZATAZ; no common intrusion vector has been established across any of the incidents in this campaign."
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
updates: []
migrated_from: null
---

Over the last weekend of August 2026 a criminal actor published fresh data-leak claims against seven more French Services départementaux d'incendie et de secours — Somme, Essonne, Bas-Rhin, Bouches-du-Rhône, Gard, Vosges and Moselle — extending a campaign ZATAZ first documented in late July 2026 against five other SDIS (Aisne, Alpes-de-Haute-Provence, Landes, Marne, Alpes-Maritimes), where postings were attributed to three separate criminal-forum handles: ChimeraZ, Cybernox and AplaGroup ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/)). Of the August wave, Objectif Gard names only ChimeraZ, tying the same handle to five of the seven units (Gard, Bouches-du-Rhône, Moselle, Bas-Rhin and Vosges); no source names an actor for the Somme or Essonne claims, or ties Cybernox or AplaGroup to this wave. This is not merely a criminal claim: contacted directly on 30 August, the president of SDIS du Gard's governing board confirmed the cyberattack and theft of personal data on personnel, including copies of identity documents and bank details, with the full scope and intrusion method still under investigation ([Objectif Gard, 2026-08-30](https://www.objectifgard.com/faits-divers/gard-cyberattaque-chez-les-pompiers-des-donnees-personnelles-sensibles-derobees-168493.php)).

No common intrusion vector has been established across the incidents in this campaign. The one case with a stated mechanism is from the July wave: SDIS de l'Aisne, where a claimed administrator-level access credential was posted in cleartext by the actor; ZATAZ notes its current validity cannot be established from the post alone, since access can be disabled or changed after disclosure, but the posting itself is a more critical indicator than a plain directory extraction ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/)). The July wave's cumulative claims — spanning the Landes, Marne (2,167 people), Alpes-Maritimes (2,325 people), Alpes-de-Haute-Provence and Aisne SDIS, plus separate claims against SDIS d'Indre-et-Loire (2,637 public-service agents plus 54 individuals linked to private structures) and the Pompiers.fr / Fédération nationale des sapeurs-pompiers de France membership platform ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/des-donnees-de-pompiers-francais-exposees-en-serie/)) — totalled at least 166,376 exposed individuals, with a potential total exceeding 932,376 depending on the volumes claimed; ZATAZ is explicit that this estimate is a straight sum of announced record counts and does not mean each line was technically verified or maps to a distinct person ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/un-pirate-cible-a-nouveau-les-sdis-francais/)). Each publication in the campaign otherwise appears to be a distinct claim rather than evidence of one coordinated technical compromise.

**Defender takeaway:** the pattern that matters is not any single leak's volume but the aggregation risk. Personnel identity, rank, assignment, hierarchical role, contact details and — in the Aisne case — an exposed administrative credential, accumulated across repeated incidents against the same category of organisation, builds a reconnaissance dataset usable for targeted phishing, impersonation or infrastructure mapping against emergency-services personnel specifically. That is the same organisational category as Swiss cantonal and communal fire and rescue services within this constituency's core; treat personnel-directory applications and any administrative credentials at emergency-services organisations as high-value reconnaissance and access targets even where any single leak's data looks individually low-sensitivity, and assume that recurring incidents against peer organisations are building a profiling dataset regardless of whether your own organisation has been named yet.
