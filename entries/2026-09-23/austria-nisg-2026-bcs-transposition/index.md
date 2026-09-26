---
schema: 1
kind: policy
title: "Austria's NISG 2026 creates the Bundesamt für Cybersicherheit, 24h/72h incident-reporting clock live 1 October 2026"
headline: "Austria stands up a new federal cybersecurity authority with 24h/72h reporting and active-scanning powers"
summary: >
  Austria's NIS2-transposition law (NISG 2026) enters into force on 1
  October 2026, creating the Bundesamt für Cybersicherheit (BCS) as the
  supervisory authority for essential/important entities, with a graduated
  24h/72h incident-reporting clock, mandatory management security training,
  and new powers for the BCS to run active vulnerability scans against
  covered entities' internet-facing systems — obstruction becomes a
  criminal offence.
discovered_at: "2026-09-23T04:44:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: notable
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
  - quote: "Blocking or defending against such state scans is a criminal offence from 1 October, and affected essential entities must also actively cooperate on request."
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
updates: []
migrated_from: null
---

Austria's Netz- und Informationssystemsicherheitsgesetz 2026 (NISG 2026) — the country's NIS2 transposition, two years late — enters into force on 1 October 2026: "with the entry into force of the [NISG 2026], the new Federal Office for Cybersecurity (BCS) officially begins its work on 1 October 2026" (translated from German; Austrian Federal Ministry of the Interior, via OTS, 2026-09-22). The new Bundesamt für Cybersicherheit (BCS), under the Interior Ministry and led by former Austrian Power Grid CIO Markus Kasinger, becomes the central registration and supervision authority for "essential" and "important" entities across energy, transport, health, water, digital infrastructure, industry and food supply (municipalities excluded), takes over operation of the civilian-administration GovCERT, and gains oversight of sectoral CERTs — including the Austrian HealthCERT — and the general-economy CERT.at ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)). Covered entities face a graduated reporting clock: "an initial early warning is required without delay, in any case within 24 hours of becoming aware of the incident. A more detailed notification must be made without delay, at the latest within 72 hours" (translated from German; Austrian BMI, via OTS, 2026-09-22), followed by further reports and a final report as the incident develops. The law also mandates security-awareness training for management and gives the BCS new powers to run active vulnerability scans against internet-facing systems of essential entities: "blocking or defending against such state scans is a criminal offence from 1 October, and affected essential entities must also actively cooperate on request" (translated from German; heise online, 2026-09-22). Enforcement and fines run through the competent district administrative authority rather than the BCS itself ([heise online, 2026-09-22](https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html)).

This continues the pattern already tracked for Finland's NCSC-FI CRA reporting checklist and Canton Bern's ICSG — also a 24h/72h reporting clock, entering force 1 November 2026 — giving Swiss cantonal and federal authorities a further live comparator for reporting-obligation design as additional cantons stand up their own ICSG-equivalents.
