---
schema: 1
kind: policy
title: "Canton of Bern confirms 1 November 2026 entry-into-force for its new cybersecurity law (ICSG): 24h/72h mandatory incident reporting and named security accountability for every cantonal administrative unit"
headline: "Bern's cantonal administration gets a fixed incident-reporting clock and a named accountable officer per agency ahead of its 1 November 2026 go-live"
summary: >
  Canton Bern's government council confirmed on 2026-09-10 that its new Gesetz über Informations-
  und Cybersicherheit (ICSG) and implementing ordinance (IDSV) enter into force on 1 November 2026.
  From that date, every cantonal administrative unit must report cyberattacks and security
  incidents within 24 hours (72 hours where personal data is affected), classify ICT assets by
  protection need, and name each agency's top leadership as the accountable security officer.
discovered_at: "2026-09-11T04:37:00Z"
event_date: "2026-09-10"
run_id: 2026-09-11T0410Z-intel
priority: notable
immediate_action: null
tags: [policy]
regions: [switzerland]
sectors: [public-sector]
entities:
  - policy:bern-icsg-cybersecurity-law-2026
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html"
    publisher: "Kanton Bern — Amt für Informatik und Organisation (KAIO), official cantonal source"
    date: "2026-09-09"
    role: primary
  - url: "https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698"
    publisher: "headtopics.com, relaying a Kanton Bern Regierungsrat press statement"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Agencies will in future have to report cyberattacks and security incidents within 24 hours. Where personal data is affected, a 72-hour deadline applies, the cantonal government council wrote in a statement on Thursday. (translated from German)"
    original: "So müssen die Dienststellen künftig Cyberangriffe und Sicherheitsvorfälle innert 24 Stunden melden. Sind Personendaten betroffen, gilt eine Frist von 72 Stunden, wie der Regierungsrat am Donnerstag in einer Mitteilung schrieb."
    publisher: "headtopics.com, relaying a Kanton Bern Regierungsrat press statement"
    source_url: "https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698"
  - quote: "The ICSG enters into force on 1 November 2026. (translated from German)"
    original: "Das ICSG tritt am 1. November 2026 in Kraft."
    publisher: "Kanton Bern — Amt für Informatik und Organisation (KAIO), official cantonal source"
    source_url: "https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html"
  - quote: "From 1 November 2026, responsibility for security lies with each agency's or directorate's top leadership as the designated security-responsible officer (SIVE DIR/Amt). (translated from German)"
    original: "Verantwortlich für die Sicherheit ist ab 1. November 2026 die oberste Führung der Behörden (Amts- oder Direktionsleitung) als Sicherheitsverantwortliche oder -verantwortlicher (SIVE DIR/Amt)."
    publisher: "Kanton Bern — Amt für Informatik und Organisation (KAIO), official cantonal source"
    source_url: "https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html"
verification: multi-source
sourcing_note: >
  Kanton Bern's own KAIO office is the primary, first-party authority for its own cantonal
  legislation. The specific 24-hour/72-hour reporting-clock figure is sourced to the cantonal
  government council's own press statement, relayed by headtopics.com and independently by Der
  Bund; both press outlets restate the same government release rather than independently verifying
  its contents, which is why credibility is not raised above what a single official announcement
  supports. inside-it.ch also covered this law but its article body could not be fetched (persistent
  429 rate-limit) and is not cited.
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

Canton Bern's government council (Regierungsrat) confirmed on 2026-09-10 that the cantonal Gesetz über Informations- und Cybersicherheit (ICSG) — passed by the Grand Council on 12 June 2025 ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)) — and its implementing Verordnung über die Informations- und Datensicherheit (IDSV) enter into force on 1 November 2026 ([headtopics.com / Kanton Bern Regierungsrat, 2026-09-10](https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698)), a date also carried on KAIO's own page. From that date, every cantonal administrative unit must report cyberattacks and security incidents within 24 hours; where personal data is affected, a 72-hour deadline applies instead ([headtopics.com / Kanton Bern Regierungsrat, 2026-09-10](https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698)). The law introduces a graduated procedure for ICT assets: depending on protection need, either uniform baseline minimum measures apply or a detailed security-and-data-protection concept is required, and the canton classifies information as "intern", "vertraulich" or "geheim" only where unauthorised disclosure would harm its interests ([headtopics.com / Kanton Bern Regierungsrat, 2026-09-10](https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698)). New obligations include rules on personal security screening (Personensicherheitsprüfung) and, from 1 November 2026, explicit accountability assigned to each agency's or directorate's own top leadership as the designated security officer, supported by security officers and a new central advisory unit inside KAIO that also runs the cantonal information-security management system ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)). The ICSG/IDSV explicitly satisfies the security requirements for cooperation with the federal government under the national Informationssicherheitsgesetz ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)).

Municipal bodies and other public-task carriers in the canton are bound by the ICSG/IDSV only to the extent they process cantonal or federal information, use cantonal or federal ICT resources, or handle personal data on the canton's behalf; the cantonal rules otherwise apply to them only as a recommendation ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)). The canton is also standing up a dedicated platform for reporting security incidents, vulnerabilities and data-security breaches, not yet published as of this writing, ahead of the 1 November 2026 go-live ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)). Transition periods of two to three years apply for administrative units to fully implement the new requirements ([headtopics.com / Kanton Bern Regierungsrat, 2026-09-10](https://ch.headtopics.com/news/kanton-bern-verscharft-cyberschutz-bei-angriffen-gilt-ab-87600698)), and this complements rather than duplicates the revised cantonal data-protection law, already in force since 1 September 2026 ([Kanton Bern KAIO, 2026-09-09](https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html)).

**Defender takeaway:** cantonal Bern administrative units and any body handling cantonal or federal Bern information or ICT resources should confirm now who holds the SIVE (Sicherheitsverantwortliche/r) role in their agency, that a 24-hour/72-hour incident-reporting path exists and is rehearsed before 1 November 2026, and that ICT-asset classification work is scheduled within the two-to-three-year transition window rather than left to the deadline.

