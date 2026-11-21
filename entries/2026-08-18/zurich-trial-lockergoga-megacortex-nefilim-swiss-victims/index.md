---
schema: 1
kind: incident
title: "Zurich District Court opens the LockerGoga / MegaCortex / Nefilim trial: four named Swiss victims, CHF 100m+ in damage, and an indictment that describes the intrusion pattern step by step"
headline: "Zurich District Court sentences the Stadler Rail ransomware developer to 12 years 9 months — nine months more than the prosecution itself asked for"
summary: >
  A 52-year-old Ukrainian software developer resident in canton Basel-Landschaft was sentenced by Zurich
  District Court on 2026-09-10 to 12 years 9 months' unconditional imprisonment, a 10-year expulsion order
  and forfeiture of CHF 300,000, for a central development and organising role in an international
  ransomware operation that ran from December 2018 to May 2020 using LockerGoga, MegaCortex and Nefilim.
  The indictment named four Swiss victims — Stadler Rail, Meier Tobler, Crealogix and IHI Ionbond — among
  ten companies across seven countries, put economic damage above CHF 100 million, and recorded that none of
  the Swiss companies paid while three non-Swiss victims paid CHF 4.5 million between them. The verdict is
  not final; the defendant can still appeal to the cantonal Obergericht and the Bundesgericht.
discovered_at: "2026-08-18T04:50:00Z"
updated_at: "2026-09-11T04:38:00Z"
event_date: "2026-08-17"
run_id: 2026-08-18T0410Z-intel
priority: notable
immediate_action: null
tags: [ransomware, law-enforcement, organized-crime]
regions: [switzerland, europe]
sectors: [transport, finance, manufacturing]
entities: [incident:zurich-lockergoga-megacortex-nefilim-trial-2026, malware:lockergoga, malware:megacortex, malware:nefilim]
techniques: [T1685, T1486, T1490, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362"
    publisher: "cash.ch"
    date: "2026-08-17"
    role: primary
  - url: "https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489"
    publisher: "20 Minuten"
    date: "2026-08-17"
    role: primary
  - url: "https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht"
    publisher: "Netzwoche"
    date: "2026-08-17"
    role: corroborating
  - url: "https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt"
    publisher: "SRF (Schweizer Radio und Fernsehen)"
    date: "2026-09-10"
    role: corroborating
  - url: "https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811"
    publisher: "cash.ch (AWP wire)"
    date: "2026-09-10"
    role: corroborating
  - url: "https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489"
    publisher: "20 Minuten"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Sie verschafften sich Zugang zu den Systemen, schalteten Überwachungsprozesse ab und verschlüsselten anschliessend Server sowie Arbeitsplatzrechner."
    publisher: "cash.ch"
  - quote: "Beim Angriff auf Stadler Rail entwendete der Beschuldigte zudem rund 500 Gigabyte an vertraulichen Daten."
    publisher: "cash.ch"
  - quote: "die Daten inklusive Back-up-Dateien zu verschlüsseln"
    publisher: "20 Minuten"
  - quote: "Nach Angaben der Staatsanwaltschaft belaufen sich die wirtschaftlichen Schäden der Angriffe auf über 130 Millionen Franken."
    publisher: "Netzwoche"
  - quote: "Das Zürcher Bezirksgericht hat einen 52-jährigen ukrainischen Hacker zu einer Freiheitsstrafe von 12 Jahren und 9 Monaten und zu einem Landesverweis von 10 Jahren verurteilt."
    publisher: "SRF"
    source_url: "https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt"
  - quote: "Mit seinem Urteil ging das Bezirksgericht sogar noch weiter, als die Staatsanwaltschaft beantragt hatte. Gemäss Anklage sollte der Hacker «nur» zwölf Jahre Freiheitsstrafe erhalten - jetzt werden es neun Monate mehr."
    publisher: "cash.ch (AWP wire)"
    source_url: "https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811"
  - quote: "Zudem wird er für zehn Jahre des Landes verwiesen und muss 300'000 Franken dem Staat abliefern. Für das Gericht war er der Erpressung, der versuchten Erpressung, der schweren Datenbeschädigung und der Pornografie schuldig."
    publisher: "20 Minuten"
    source_url: "https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489"
  - quote: "Es gab jedoch keine Hinweise darauf, dass der 52-jährige Mann aus dem Baselbiet selbst Verbindungen zu russischen Geheimdiensten besessen habe."
    publisher: "cash.ch (AWP wire)"
    source_url: "https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811"
verification: multi-source
sourcing_note: >
  Three independent Swiss outlets reporting the same court proceeding, each with its own detail: cash.ch on
  the intrusion pattern and the Stadler Rail exfiltration, 20 Minuten on the indictment's victim list and the
  alleged Moscow principal, Netzwoche on the charge sheet and the damage figure. No Zurich prosecutor's or
  court media release could be found published independently of the press coverage, so this rests on
  journalism reporting an open hearing rather than on an authority document. The two damage figures in
  circulation differ — over CHF 100 million per 20 Minuten, over CHF 130 million per Netzwoche, both
  attributed to the prosecution — and both are reported rather than reconciled. The ransom figures look
  further apart than they are: 20 Minuten's CHF 4.5 million is what three companies paid, while Netzwoche's
  450 bitcoin for the single largest payment is explicitly valued at today's rate rather than at the time of
  payment, so the two franc amounts are denominated differently and neither outlet reconciles them. Every allegation, the
  FSB-linked-principal claim above all, was untested at the time of the original charge-sheet reporting.
  Zurich District Court delivered its verdict on 2026-09-10, corroborated by SRF, cash.ch (AWP wire) and
  20 Minuten; the 20 Minuten article cited for the verdict is the same URL as this entry's original
  indictment-stage citation, live-updated with the verdict content, so its page metadata still carries the
  2026-08-17 publish date even though the cited content is the 2026-09-10 proceeding — the article text itself
  states the verdict date explicitly ("am Donnerstag, 10. September, wurde das Urteil gefällt").
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
  - at: "2026-09-11T04:38:00Z"
    run_id: 2026-09-11T0410Z-intel
    type: update
    summary: >
      Zurich District Court delivered its verdict on 2026-09-10: 12 years 9 months' unconditional
      imprisonment, a 10-year expulsion order and forfeiture of CHF 300,000 — nine months more than
      the prosecution's own 12-year demand. The court found the defendant guilty of extortion,
      attempted extortion, serious data damage and possession of child-sexual-abuse material,
      rejecting his defense that he was an unwitting IT consultant and his bid to have all seized
      digital evidence ruled inadmissible. The court found no evidence the defendant himself had
      intelligence-service ties, though the prosecutor's closing argument repeated the contested
      claim that the group's Moscow-based principal held an FSB cover identity. The verdict is not
      final and remains open to appeal.
    fields: [headline, summary, sourcing_note, body, sources, evidence]
migrated_from: null
---

A 52-year-old Ukrainian software developer, resident in canton Basel-Landschaft and in custody since October 2021, appeared before Zurich District Court on 2026-08-17 charged with commercial extortion, multiple counts of serious data corruption, serious money laundering and possession of child pornography ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). The charge sheet covers attacks between December 2018 and May 2020 involving the ransomware families LockerGoga, MegaCortex and Nefilim ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)); the proceedings were triggered by a series of ransomware attacks on Zurich-area companies from July 2019. Per the indictment as reported by cash.ch, the defendant developed LockerGoga largely independently on the instruction of a co-accused in Moscow, later contributed to MegaCortex, and took a leading role as project manager on a further tool ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). The prosecution seeks twelve years' imprisonment and a twelve-year entry ban ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)).

The indictment lists ten companies, four of them Swiss: Meier Tobler, Crealogix, IHI Ionbond and Stadler Rail ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). Netzwoche reports the defendant is alleged to have taken part, from his residence in Switzerland, in attacks on ten companies in Switzerland, France, Norway, Scotland, Canada, the Netherlands and the United States ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). Three victims, none Swiss, paid ransoms totalling CHF 4.5 million; the Swiss companies paid nothing ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). Netzwoche reports the same proceedings differently, putting the single largest payment at 450 bitcoin, which it values at roughly CHF 41 million at today's rate ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). The two franc figures are not measuring the same thing: one is what was paid at the time, the other is what that bitcoin is worth now, and neither outlet reconciles them. Prosecutors put the economic damage above CHF 100 million, from business interruptions, delivery delays, work stoppages and the special measures the companies had to mount ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)); Netzwoche reports the prosecution figure as above CHF 130 million, arising mainly from revenue lost to business interruption and the cost of restoring IT systems ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). Per the indictment as reported by 20 Minuten, the defendant joined with a Ukrainian principal based in Moscow in June 2018, and that principal is alleged to have operated under a cover identity of Russia's FSB — an allegation the prosecution makes in a trial the defendant contests, and one no investigating authority has published independently.

**What the charge sheet describes operationally.** Unusually for court reporting, the intrusion pattern is spelled out: "Sie verschafften sich Zugang zu den Systemen, schalteten Überwachungsprozesse ab und verschlüsselten anschliessend Server sowie Arbeitsplatzrechner" — they obtained access to the systems, switched off monitoring processes, and then encrypted servers as well as workstations ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). 20 Minuten records the group's stated objective as penetrating as many company networks as possible in Western Europe and North America and encrypting "die Daten inklusive Back-up-Dateien" — the data including the backup files ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). At Stadler Rail the defendant is additionally accused of taking around 500 gigabytes of confidential data and threatening to publish it to increase pressure ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)) — double extortion, inside a charged period Netzwoche reports as December 2018 to May 2020 ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)); no cited source dates that exfiltration more precisely than the period as a whole. The extortion notes claimed the data was encrypted with military-grade algorithms and that any third-party recovery attempt would destroy it ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)) — a pressure device rather than a technical fact.

**Detection, telemetry class first.** Nothing here is a new technique, and the value is not novelty: it is that a court record independently corroborates the ordering that ransomware detection is built around. Defence-impairment precedes encryption, so the telemetry that matters arrives before any file changes — security service and agent stop or configuration-change events, sudden gaps in endpoint agent check-ins across multiple hosts, and audit or logging services terminating outside a maintenance window. Backup infrastructure is a target in the same operation rather than a recovery path afterwards, so authentication and deletion activity against backup catalogues and repositories belongs in the same alerting tier as domain controllers. **Triage:** legitimate maintenance also stops security agents and touches backup stores — the discriminators are that maintenance is scoped to a change window and a host set, is performed by accounts that routinely do it, and does not spread to servers and workstations at once; a monitoring-process stop that fans out across both populations within a short window, from an account with no history of that action, is the sequence worth waking someone for.

**Defender takeaway:** the transferable content for this constituency is the confirmation, in an evidentiary rather than a vendor setting, that the encryption stage is the end of the sequence and not the beginning — the operation deliberately removed monitoring first and destroyed the backup files as part of the same action. For Swiss operators the concrete follow-up is to check that backup repositories are outside the credential and network reach of the production estate they protect, and that the loss of endpoint agent telemetry across several hosts raises an alert on its own rather than only being noticed once encryption starts. This is a prosecution's account of a six-year-old operation, so it changes no patching or hunting priority today; it is carried because four Swiss companies in rail manufacturing, building technology, banking software and industrial coatings are named victims, and because a verdict would convert the FSB-linked-principal allegation into something a defender could reason about.

## Update — 2026-09-11T04:38:00Z

Zurich District Court delivered its verdict on 2026-09-10: 12 years 9 months' imprisonment and a 10-year expulsion order ([SRF, 2026-09-10](https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt)) — an unconditional (non-suspended) sentence ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)) — plus forfeiture of CHF 300,000 to the state ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)) — nine months more than the prosecution's own 12-year demand ([cash.ch, 2026-09-10](https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811)). The court found the defendant guilty of extortion, attempted extortion, serious data damage and possession of child-sexual-abuse material found on his devices ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)); it rejected his defense that he was an unwitting IT consultant, citing ransom notes ([SRF, 2026-09-10](https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt)) and a body of digital traces found on his own storage media ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)), and it dismissed his bid to have all seized digital evidence ruled inadmissible for want of adequate notice of his data-sealing rights during the searches ([cash.ch, 2026-09-10](https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811)). The judge noted his frequent invocation of the right to silence undermined his credibility ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)), and observed "he was not a mastermind" (translated from German) while finding it proven that he developed the ransomware and passed it to still-unidentified operators who selected victims and coordinated the extortion ([SRF, 2026-09-10](https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt)) — a professional effort the judge said spanned three years ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)). The prosecutor's closing argument repeated the contested claim that the group's Moscow-based principal, Oleksandr Ieremenko, held an FSB cover identity and was the subject of a US Secret Service bounty ([20 Minuten, 2026-09-10](https://www.20min.ch/story/bezirksgericht-zuerich-ukrainischer-hacker-52-muss-fuer-fast-13-jahre-ins-gefaengnis-103618489)); the court found no evidence that the convicted defendant himself had intelligence-service ties ([cash.ch, 2026-09-10](https://www.cash.ch/news/hacker-von-stadler-rail-und-meier-tobler-zu-langer-haft-verurteilt-967811)). The verdict is not final — the defendant, in security detention throughout, can still appeal to the cantonal Obergericht and the Bundesgericht ([SRF, 2026-09-10](https://www.srf.ch/news/schweiz/zuercher-bezirksgericht-hackerangriff-auf-stadler-rail-taeter-zu-langer-haft-verurteilt)).
