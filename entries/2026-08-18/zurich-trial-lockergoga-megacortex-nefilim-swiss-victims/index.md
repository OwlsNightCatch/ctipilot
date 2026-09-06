---
schema: 1
kind: incident
title: "Zurich District Court opens the LockerGoga / MegaCortex / Nefilim trial: four named Swiss victims, CHF 100m+ in damage, and an indictment that describes the intrusion pattern step by step"
headline: "Six years on, the charge sheet for the Stadler Rail ransomware attacks is public — disable monitoring, encrypt servers and workstations, encrypt the backups too"
summary: >
  A 52-year-old Ukrainian software developer resident in canton Basel-Landschaft went on trial at Zurich
  District Court on 2026-08-17, accused of a central development and organising role in an international
  ransomware operation that ran from December 2018 to May 2020 using LockerGoga, MegaCortex and Nefilim.
  The indictment names four Swiss victims — Stadler Rail, Meier Tobler, Crealogix and IHI Ionbond — among
  ten companies across seven countries, puts economic damage above CHF 100 million, and records that none of
  the Swiss companies paid while three non-Swiss victims paid CHF 4.5 million between them. Prosecutors
  allege the group's principal, based in Moscow, operated under a cover identity of Russia's FSB; that is a
  prosecution claim in a contested trial, not an established attribution. The prosecution seeks twelve years'
  imprisonment and a twelve-year entry ban.
discovered_at: "2026-08-18T04:50:00Z"
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
  FSB-linked-principal claim above all, is untested: the defendant contests the charges and no verdict has
  been reached.
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

A 52-year-old Ukrainian software developer, resident in canton Basel-Landschaft and in custody since October 2021, appeared before Zurich District Court on 2026-08-17 charged with commercial extortion, multiple counts of serious data corruption, serious money laundering and possession of child pornography ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). The charge sheet covers attacks between December 2018 and May 2020 involving the ransomware families LockerGoga, MegaCortex and Nefilim ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)); the proceedings were triggered by a series of ransomware attacks on Zurich-area companies from July 2019. Per the indictment as reported by cash.ch, the defendant developed LockerGoga largely independently on the instruction of a co-accused in Moscow, later contributed to MegaCortex, and took a leading role as project manager on a further tool ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). The prosecution seeks twelve years' imprisonment and a twelve-year entry ban ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)).

The indictment lists ten companies, four of them Swiss: Meier Tobler, Crealogix, IHI Ionbond and Stadler Rail ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). Netzwoche reports the defendant is alleged to have taken part, from his residence in Switzerland, in attacks on ten companies in Switzerland, France, Norway, Scotland, Canada, the Netherlands and the United States ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). Three victims, none Swiss, paid ransoms totalling CHF 4.5 million; the Swiss companies paid nothing ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). Netzwoche reports the same proceedings differently, putting the single largest payment at 450 bitcoin, which it values at roughly CHF 41 million at today's rate ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). The two franc figures are not measuring the same thing: one is what was paid at the time, the other is what that bitcoin is worth now, and neither outlet reconciles them. Prosecutors put the economic damage above CHF 100 million, from business interruptions, delivery delays, work stoppages and the special measures the companies had to mount ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)); Netzwoche reports the prosecution figure as above CHF 130 million, arising mainly from revenue lost to business interruption and the cost of restoring IT systems ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)). Per the indictment as reported by 20 Minuten, the defendant joined with a Ukrainian principal based in Moscow in June 2018, and that principal is alleged to have operated under a cover identity of Russia's FSB — an allegation the prosecution makes in a trial the defendant contests, and one no investigating authority has published independently.

**What the charge sheet describes operationally.** Unusually for court reporting, the intrusion pattern is spelled out: "Sie verschafften sich Zugang zu den Systemen, schalteten Überwachungsprozesse ab und verschlüsselten anschliessend Server sowie Arbeitsplatzrechner" — they obtained access to the systems, switched off monitoring processes, and then encrypted servers as well as workstations ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). 20 Minuten records the group's stated objective as penetrating as many company networks as possible in Western Europe and North America and encrypting "die Daten inklusive Back-up-Dateien" — the data including the backup files ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). At Stadler Rail the defendant is additionally accused of taking around 500 gigabytes of confidential data and threatening to publish it to increase pressure ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)) — double extortion, inside a charged period Netzwoche reports as December 2018 to May 2020 ([Netzwoche, 2026-08-17](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)); no cited source dates that exfiltration more precisely than the period as a whole. The extortion notes claimed the data was encrypted with military-grade algorithms and that any third-party recovery attempt would destroy it ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)) — a pressure device rather than a technical fact.

**Detection, telemetry class first.** Nothing here is a new technique, and the value is not novelty: it is that a court record independently corroborates the ordering that ransomware detection is built around. Defence-impairment precedes encryption, so the telemetry that matters arrives before any file changes — security service and agent stop or configuration-change events, sudden gaps in endpoint agent check-ins across multiple hosts, and audit or logging services terminating outside a maintenance window. Backup infrastructure is a target in the same operation rather than a recovery path afterwards, so authentication and deletion activity against backup catalogues and repositories belongs in the same alerting tier as domain controllers. **Triage:** legitimate maintenance also stops security agents and touches backup stores — the discriminators are that maintenance is scoped to a change window and a host set, is performed by accounts that routinely do it, and does not spread to servers and workstations at once; a monitoring-process stop that fans out across both populations within a short window, from an account with no history of that action, is the sequence worth waking someone for.

**Defender takeaway:** the transferable content for this constituency is the confirmation, in an evidentiary rather than a vendor setting, that the encryption stage is the end of the sequence and not the beginning — the operation deliberately removed monitoring first and destroyed the backup files as part of the same action. For Swiss operators the concrete follow-up is to check that backup repositories are outside the credential and network reach of the production estate they protect, and that the loss of endpoint agent telemetry across several hosts raises an alert on its own rather than only being noticed once encryption starts. This is a prosecution's account of a six-year-old operation, so it changes no patching or hunting priority today; it is carried because four Swiss companies in rail manufacturing, building technology, banking software and industrial coatings are named victims, and because a verdict would convert the FSB-linked-principal allegation into something a defender could reason about.
