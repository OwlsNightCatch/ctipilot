---
schema: 1
kind: incident
title: "Technical University of Munich: attackers captured the central-login passwords of everyone who signed in to the legacy myTUM portal, took a TUMonline system administrator's credentials and attacked the campus-management system; accounts with MFA were protected"
headline: "TUM: legacy portal harvested central-login passwords, an admin's credentials reached TUMonline; MFA accounts held"
summary: >
  The Technical University of Munich said on 2026-11-06 that unknown attackers attacked its myTUM portal and captured the central-login passwords of all persons who had signed in there, among them the credentials of a TUMonline system administrator, with which they attacked the campus-management system TUMonline, which TUM took off the network. TUM says accounts with multi-factor authentication were protected, reported the incident to the Bavarian data-protection commissioner and filed a criminal complaint; heise reports that the entry point was a legacy system and that about 60,000 users are concerned.
discovered_at: "2026-11-07T04:03:00Z"
updated_at: null
event_date: "2026-11-06"
run_id: 2026-11-07T0256Z-intel
priority: routine
immediate_action: null
tags: [data-breach, identity]
regions: [dach, europe]
sectors: [education, public-sector]
entities: ["incident:tum-mytum-legacy-portal-credential-harvest-2026-11"]
techniques: [T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum"
    publisher: "Technische Universität München (incident notice, status 2026-11-06 12:20)"
    date: "2026-11-06"
    role: primary
  - url: "https://www.heise.de/news/Plattformen-offline-Cyberangriff-auf-TU-Muenchen-11515734.html"
    publisher: "heise online"
    date: "2026-11-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In doing so they captured passwords for the central login to TUM systems (e.g. login.tum.de, TUMonline, etc.), namely from all persons who had logged in to myTUM. (translated from German)"
    original: "Dabei haben sie Passwörter für die zentrale Anmeldung an TUM-Systemen (z.B. login.tum.de, TUMonline, usw) erbeutet, und zwar von allen Personen, die sich bei myTUM angemeldet haben."
    publisher: "Technische Universität München"
    source_url: "https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum"
  - quote: "Among these were also the access credentials of a system administrator for TUMonline. (translated from German)"
    original: "Hierunter befanden sich auch die Zugangsdaten eines Systemverwalters für TUMonline."
    publisher: "Technische Universität München"
    source_url: "https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum"
  - quote: "User accounts with MFA were protected in this attack. (translated from German)"
    original: "Benutzerkonten mit MFA waren bei diesem Angriff geschützt."
    publisher: "Technische Universität München"
    source_url: "https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum"
verification: single-source-victim
sourcing_note: >
  TUM's own incident notice is the source for what was captured, the administrator pivot, the data categories and the MFA statement; heise relays a TUM spokesperson, and the 60,000 figure (a good 60,000 in heise's wording) is heise's own sentence and the account that the old system served as the way into the current campus administration is an unattributed report from university circles. Neither source states how the passwords were captured at myTUM, when the attack began, or whether the administrator account had MFA, and heise's teaser says data was stolen while its text says exfiltration is still being investigated.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The Technical University of Munich says unknown persons attacked its myTUM portal and captured the passwords for the central login to TUM systems, among them login.tum.de and TUMonline, from all persons who had logged in to myTUM; among them were the access credentials of a system administrator for TUMonline, with which the attackers attacked the central campus-management system TUMonline, which TUM then took off the network (translated from German) ([TUM, 2026-11-06](https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum)). TUM says the attackers may have reached the account password, name, private address and date of birth of everyone affected, plus staff and student details, that the attackers' accesses within TUMonline were largely logged and that it currently assumes no further TUMonline data such as grades is affected, and that accounts with multi-factor authentication were protected in this attack (translated from German) ([TUM, 2026-11-06](https://www.tum.de/aktuelles/alle-meldungen/pressemitteilungen/details/it-sicherheitsvorfall-an-der-tum)). heise, quoting a TUM spokesperson, reports that the attackers entered through a legacy system and that whether data was exfiltrated is still being investigated, and adds that about 60,000 students and employees are concerned (translated from German) ([heise online, 2026-11-06](https://www.heise.de/news/Plattformen-offline-Cyberangriff-auf-TU-Muenchen-11515734.html)). Neither source states how the passwords were captured at myTUM.

**Exposure:** a public university or other public body that keeps a retired or secondary sign-in portal validating against its central directory, so that every password typed there is a credential for the primary identity and administration systems; TUM's accounts with MFA held, and the lesson transfers to Swiss cantonal and university portals.

**Defender takeaway:** inventory legacy and secondary portals that accept the central directory password and retire them or put them behind MFA, require MFA on administrator accounts of campus and school-management systems, and check whether an administrator ever signed in to such a portal.
