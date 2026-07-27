---
schema: 1
kind: threat
horizon: operational
title: "Chat Control backlash turns operational: a hacktivist compiles targeting dossiers on French and EU officials out of old breach data, not a new intrusion"
headline: "Officials doxxed over the EU Chat Control file — dossiers assembled from years of unrelated breach data"
summary: >
  A hacktivist using the handle Cybernox published personal dossiers on French national and European
  officials on 2026-07-25, framed as protest against the EU "Chat Control" communications-scanning file.
  ZATAZ counts 24 figures tied to the vote, while Cyberattaque.org describes a second group as well and
  states that no total is given. The records — home addresses, phone numbers, personal emails, dates of
  birth, French national ID numbers and in some cases banking details — were not taken in a fresh intrusion
  but recomposed from multiple earlier, unrelated breaches of private companies and public bodies, which is
  what makes the technique reusable against any public official attached to a contested digital-policy debate.
discovered_at: "2026-07-27T04:33:46Z"
event_date: "2026-07-25"
run_id: 2026-07-27T0409Z-intel
priority: notable
immediate_action: null
tags:
  - hacktivism
  - data-breach
regions:
  - europe
sectors:
  - public-sector
entities:
  - actor:cybernox
techniques:
  - T1589
  - T1589.002
affected_products: []
cves: []
sources:
  - url: "https://www.zataz.com/chat-control-un-pirate-cible-24-responsables-politiques-francais/"
    publisher: "ZATAZ.COM"
    date: "2026-07-26"
    role: primary
  - url: "https://www.cyberattaque.org/chat-control-des-responsables-francais-cibles-par-une-fuite-de-donnees-sensibles/"
    publisher: "Cyberattaque.org"
    date: "2026-07-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Cette action ne révèle donc pas une intrusion unique contre le Parlement, elle illustre l’exploitation politique de données déjà compromises et leur recomposition en dossier de pression."
    publisher: "ZATAZ.COM"
  - quote: "Le dossier rassemble des photographies, des adresses personnelles, des numéros de téléphone, des courriels, des dates de naissance et plusieurs identifiants administratifs. Certaines fiches contiennent aussi des coordonnées bancaires."
    publisher: "ZATAZ.COM"
  - quote: "Une fuite de données à motivation politique a été revendiquée le 25 juillet 2026 par le hacker Cybernox."
    publisher: "Cyberattaque.org"
verification: multi-source
sourcing_note: >
  Two independent French outlets reported the publication within hours of each other and each contributes
  different detail, but neither verified the data's provenance directly. ZATAZ relays the actor's own account
  that the records came from earlier breaches; Cyberattaque.org states the exact origin of the dataset is not
  established and reaches the same aggregation conclusion from the heterogeneity of the file formats. The
  handle "Cybernox" is named only by Cyberattaque.org — ZATAZ attributes the operation to an unnamed hacker
  it describes as previously having published around ten leaks concerning French companies.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

A hacktivist published personal dossiers on French national and European political figures on 25 July, presenting the release as protest against "Chat Control 1.0" — the temporary EU derogation from ePrivacy rules that permits detection of child-sexual-abuse material in private communications ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/chat-control-un-pirate-cible-24-responsables-politiques-francais/)). The handle "Cybernox" comes from Cyberattaque.org, which dates the claim to 25 July ([Cyberattaque.org, 2026-07-26](https://www.cyberattaque.org/chat-control-des-responsables-francais-cibles-par-une-fuite-de-donnees-sensibles/)); ZATAZ does not name the actor, describing only a hacker previously linked to around ten leaks affecting French companies. The two accounts also differ on scope, and the entry keeps both: ZATAZ puts the number of targeted figures at 24 and lists Nadine Morano, Raphaël Glucksmann, Bernard Guetta, Nathalie Loiseau, Pascal Canfin and François-Xavier Bellamy among them, while Cyberattaque.org describes a second group of officials the actor classified as having voted differently and states that "Le nombre total de personnes présentes dans les fichiers n'est pas non plus précisé" — the total number of people in the files is not specified either. ZATAZ records the contents as "des photographies, des adresses personnelles, des numéros de téléphone, des courriels, des dates de naissance et plusieurs identifiants administratifs" — photographs, home addresses, phone numbers, emails, dates of birth and several administrative identifiers — with banking details in some records ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/chat-control-un-pirate-cible-24-responsables-politiques-francais/)). Cyberattaque.org adds that French social-security numbers (NIR) appear in the set, and notes that the two-group split reflects only the actor's own labelling of how each official voted rather than any verified voting record ([Cyberattaque.org, 2026-07-26](https://www.cyberattaque.org/chat-control-des-responsables-francais-cibles-par-une-fuite-de-donnees-sensibles/)).

The defining fact is what did *not* happen. ZATAZ is explicit that "Cette action ne révèle donc pas une intrusion unique contre le Parlement, elle illustre l'exploitation politique de données déjà compromises et leur recomposition en dossier de pression" — the operation reveals no single intrusion against Parliament, but rather the political exploitation of already-compromised data recomposed into a pressure dossier ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/chat-control-un-pirate-cible-24-responsables-politiques-francais/)). Cyberattaque.org reaches the same conclusion by a different route, noting that the exact origin of the dataset is not established and that the records vary from administrative-looking data to customer files, commercial databases and loyalty-programme entries — heterogeneity that points to aggregation across sources rather than extraction from one system, with no technical evidence offered that any organisation was directly compromised ([Cyberattaque.org, 2026-07-26](https://www.cyberattaque.org/chat-control-des-responsables-francais-cibles-par-une-fuite-de-donnees-sensibles/)). ZATAZ frames the compounding effect precisely: an old address, a still-active number and an administrative document leaked in three separate incidents combine into one exploitable profile, and the risks it names for the targets are spearphishing, identity theft, banking fraud and coordinated harassment ([ZATAZ.COM, 2026-07-26](https://www.zataz.com/chat-control-un-pirate-cible-24-responsables-politiques-francais/)).

**Defender takeaway:** this is a personnel-protection and breach-intelligence problem rather than a network-telemetry one, and it will not appear in any detection stack. For public bodies whose officials are publicly attached to a contested surveillance or digital-identity file — a recurring situation in Swiss federal and cantonal politics as much as in Brussels — the actionable read is that historical breach exposure of named individuals has a long tail: records written off years ago as low-sensitivity become targeting material the moment someone acquires a political motive to correlate them. The practical consequences are that identity-verification steps for high-profile officials cannot rely on data that appears in old leaks (dates of birth, home addresses and national identifiers now circulate for every official named in these dossiers), and that helpdesk and finance staff supporting them should expect impersonation attempts carrying accurate personal detail. **Triage:** a spearphishing or vishing attempt built on this material will look more legitimate than the usual baseline precisely because the personal data is correct, so accuracy of the caller's personal knowledge is not evidence of authenticity — the discriminator remains the channel and the request, not how much the caller appears to know.
