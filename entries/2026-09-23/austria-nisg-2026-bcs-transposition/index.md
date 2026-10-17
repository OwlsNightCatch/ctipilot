---
schema: 1
kind: policy
title: "Austria's NISG 2026 creates the Bundesamt für Cybersicherheit, 24h/72h incident-reporting clock live 1 October 2026"
headline: "Austria stands up a new federal cybersecurity authority with 24h/72h reporting and active-scanning powers"
summary: >
  Austria's NIS2-transposition law (NISG 2026) enters into force on 1
  October 2026, creating the Bundesamt für Cybersicherheit (BCS) as the
  supervisory authority for essential and important entities, with a graduated
  24h/72h incident-reporting clock, mandatory management security training,
  and new powers for the BCS to run active vulnerability scans against
  essential entities' internet-facing systems. Blocking or defending against
  the scans becomes punishable.
discovered_at: "2026-09-23T04:44:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: routine
immediate_action: null
tags: [policy]
regions: [dach, europe]
sectors: [public-sector, energy, transport, healthcare, water]
entities: ["policy:austria-nisg-2026", "policy:eu-nis2-directive"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.ots.at/presseaussendung/OTS_20260922_OTS0129/bundesamt-fuer-cybersicherheit-oesterreich-buendelt-schutz-vor-digitalen-bedrohungen"
    publisher: "Austrian Federal Ministry of the Interior (BMI), via OTS"
    date: "2026-09-22"
    role: primary
  - url: "https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html"
    publisher: "heise online"
    date: "2026-09-22"
    role: corroborating
  - url: "https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html"
    publisher: "Kanton Bern, Amt für Informatik und Organisation (KAIO)"
    role: corroborating
closed_sources: []
evidence:
  - quote: "With the entry into force of the Network and Information System Security Act 2026 (NISG 2026), the new Federal Office for Cybersecurity (BCS) officially begins its work on 1 October 2026."
    original: "Mit dem Inkrafttreten des Netz- und Informationssystemsicherheitsgesetzes 2026 (NISG 2026) nimmt das neue Bundesamt für Cybersicherheit (BCS) am 1. Oktober 2026 offiziell seine Arbeit auf."
    publisher: "Austrian Federal Ministry of the Interior (BMI), via OTS press release"
    source_url: "https://www.ots.at/presseaussendung/OTS_20260922_OTS0129/bundesamt-fuer-cybersicherheit-oesterreich-buendelt-schutz-vor-digitalen-bedrohungen"
  - quote: "An initial early warning is required without delay, in any case within 24 hours of becoming aware of the incident. A more detailed notification must be made without delay, at the latest within 72 hours."
    original: "Eine erste Frühwarnung ist unverzüglich, jedenfalls innerhalb von 24 Stunden nach Kenntnisnahme des Vorfalls, vorgesehen. Eine ausführlichere Meldung hat unverzüglich, spätestens innerhalb von 72 Stunden, zu erfolgen."
    publisher: "Austrian Federal Ministry of the Interior (BMI), via OTS press release"
    source_url: "https://www.ots.at/presseaussendung/OTS_20260922_OTS0129/bundesamt-fuer-cybersicherheit-oesterreich-buendelt-schutz-vor-digitalen-bedrohungen"
  - quote: "Blocking or defending against such state scans is punishable from 1 October, and affected essential entities must also actively cooperate on request."
    original: "Blockade oder Abwehr solcher staatlichen Scans ist ab 1. Oktober strafbar, auf Aufforderung müssen betroffene wesentliche Einrichtungen auch aktiv mitwirken."
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:06Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: an Austrian NIS2 transposition that changes no
      decision for Swiss entities, so the main text is shortened to the facts a reader needs. The
      closing sentence narrated earlier coverage and credited Canton Bern's ICSG with a 24h/72h
      reporting clock and a Finnish checklist comparison without sources. It now cites the canton's
      own page for the ICSG and IDSV entry into force on 1 November 2026 and the IDSV reporting
      platform. heise's "strafbar" is rendered as punishable rather than as a criminal offence,
      which heise does not specify. The sector list is cited to the ministry's release, and every
      citation carries its link.
    fields: [priority, body, sources, summary, evidence]
migrated_from: null
---

Austria's Netz- und Informationssystemsicherheitsgesetz 2026 (NISG 2026), its NIS2 transposition, enters into force on 1 October 2026, two years late ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)). It creates the Bundesamt für Cybersicherheit (BCS) under the Interior Ministry as the central authority and supervisor for "essential" and "important" entities in sectors including energy, transport, health, drinking and waste water, digital infrastructure, industry and food supply ([Austrian BMI, via OTS, 2026-09-22](https://www.ots.at/presseaussendung/OTS_20260922_OTS0129/bundesamt-fuer-cybersicherheit-oesterreich-buendelt-schutz-vor-digitalen-bedrohungen)). Municipalities are excluded, and the BCS takes over the civilian-administration GovCERT and oversight of the sectoral CERTs and CERT.at ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)). Covered entities must send an early warning without delay and in any case within 24 hours of becoming aware of a significant incident, and a fuller notification within 72 hours ([Austrian BMI, via OTS, 2026-09-22](https://www.ots.at/presseaussendung/OTS_20260922_OTS0129/bundesamt-fuer-cybersicherheit-oesterreich-buendelt-schutz-vor-digitalen-bedrohungen)). Managers must attend security training, and the BCS will run active vulnerability scans of essential entities' internet-facing systems ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)). Blocking or defending against those scans is punishable from 1 October ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)). Penalties under the law are imposed not by the BCS itself but by the competent district administrative authority at the BCS's suggestion ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)).

For Swiss cantonal authorities, a nearer reference point is Canton Bern: its information- and cybersecurity law (ICSG) and implementing ordinance (IDSV) enter into force on 1 November 2026, and with the IDSV the canton is introducing its own platform for reporting security incidents, vulnerabilities and cyberattacks ([Kanton Bern KAIO](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)).

## Correction — 2026-09-30T06:56:06Z

Canton Bern's information- and cybersecurity law (ICSG) and its implementing ordinance (IDSV) enter into force on 1 November 2026, and the canton's incident-reporting platform comes with the IDSV ([Kanton Bern KAIO](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)). An earlier closing sentence credited the ICSG with a 24h/72h reporting clock and compared the Austrian law with a Finnish reporting checklist without sources, and both claims are removed.

heise's word for obstructing the BCS scans is "strafbar" (punishable), and it does not say whether that makes obstruction a criminal offence. It adds that penalties are imposed not by the BCS itself but by the competent district administrative authority at the BCS's suggestion ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)).
