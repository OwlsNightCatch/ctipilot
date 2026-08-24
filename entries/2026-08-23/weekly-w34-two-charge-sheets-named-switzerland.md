---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Two court filings two days apart put Swiss victims on the record — a Zurich indictment over LockerGoga, MegaCortex and Nefilim, and a US superseding indictment against Iran's Mabna Institute — and both describe tradecraft that is still exactly current"
headline: "The only documents this week that name Swiss victims are charge sheets about operations that ended six and nine years ago"
summary: >
  On 2026-08-17 a 52-year-old Ukrainian software developer resident in canton Basel-Landschaft went on
  trial at Zurich District Court over ransomware attacks between December 2018 and May 2020 using
  LockerGoga, MegaCortex and Nefilim; the indictment names four Swiss victims — Stadler Rail, Meier
  Tobler, Crealogix and IHI Ionbond — among ten companies, puts economic damage
  above CHF 100 million, and describes the intrusion pattern as obtaining access, switching off
  monitoring processes, then encrypting servers and workstations, with the group's stated objective
  including encryption of the backup files. On 2026-08-18 the US Department of Justice unsealed a
  14-count superseding indictment charging 17 members of the Mabna Institute over intrusions running
  since at least 2013 into 144 US and 178 foreign universities, at least 42 US and 11 foreign
  companies and at least five US federal and state agencies; Switzerland appears in both foreign-victim
  lists, and the newly charged conduct against companies and government entities is password spraying.
  Neither filing is notice of a live intrusion. What both are is an evidentiary record of technique
  ordering that defenders otherwise take on vendor authority — arriving on a judicial timescale that
  defence cannot wait for.
discovered_at: "2026-08-23T23:59:20Z"
event_date: "2026-08-18"
run_id: 2026-08-23T2311Z-weekly
priority: notable
immediate_action: null
tags: [ransomware, law-enforcement, espionage, nation-state, iran-nexus, organized-crime]
regions: [switzerland, europe, us]
sectors: [manufacturing, finance, education, public-sector, transport]
entities:
  - incident:zurich-lockergoga-megacortex-nefilim-trial-2026
  - malware:lockergoga
  - malware:megacortex
  - malware:nefilim
  - actor:mabna-institute
techniques: [T1685, T1486, T1490, T1566, T1078, T1110.003]
affected_products: []
cves: []
sources:
  - url: "https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary"
    publisher: "U.S. Department of Justice, Office of Public Affairs"
    date: "2026-08-18"
    role: primary
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
    date: "2026-08-19"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  The Mabna material is the Department of Justice's own press release, a first-party record of its own
  filing. The Zurich material is court reporting from two Swiss outlets present at the hearing rather
  than a published indictment, and everything attributed to the charge sheet is therefore an outlet's
  account of a prosecution document. Both sets of allegations are untested: the Zurich trial is
  contested and its verdict is set for 2026-09-10, and the Mabna defendants are charged, not
  convicted. Damage and ransom figures diverge across the wider Zurich
  reporting and are handled narrowly here. Of the three outlets cited, only 20 Minuten and Netzwoche give a total; 20 Minuten's is
  above CHF 100 million and is the figure used here, while cash.ch quantifies nothing, describing damages from business
  interruption, data loss and remediation only as running to millions; Netzwoche reports the prosecution figure as above CHF 130 million, and the referenced operational entry
  carries both without resolving them. On ransoms, 20 Minuten reports CHF 4.5 million paid by three
  non-Swiss victims, while Netzwoche values the largest single payment on a
  different basis — today's value of the bitcoin rather than what was paid at the time.
  This entry carries only the two 20 Minuten figures and attributes both to that outlet. The alleged FSB cover identity of the operation's Moscow-based principal
  is a prosecution claim in a contested trial, published by no investigating authority, and is not
  carried here as attribution.
confidence: medium
update_of: null
references:
  - 2026-08-18/zurich-trial-lockergoga-megacortex-nefilim-swiss-victims
  - 2026-08-20/doj-mabna-institute-superseding-indictment-swiss-victims
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Two documents this week name Switzerland in a victim list, and both are charge sheets. That is worth pausing on before the technical content, because it says something about where attribution actually comes from for a European defender: the week's live Swiss incidents — a Valais commune's mailbox, a Zurich business school's student records — name no actor at all beyond an extortion brand's own leak-site listing, while the two documents that do name operations and defendants concern intrusions that ended in 2020 and 2017 respectively.

**The Zurich trial.** A 52-year-old Ukrainian software developer resident in canton Basel-Landschaft and in custody since October 2021 appeared before Zurich District Court on 2026-08-17, charged in connection with ransomware attacks, and the prosecution seeks twelve years' imprisonment and a twelve-year entry ban ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)). Netzwoche puts the charged period at December 2018 to May 2020 and names the three families as LockerGoga, MegaCortex and Nefilim ([Netzwoche, 2026-08-19](https://www.netzwoche.ch/news/2026-08-17/update-mutmasslicher-cyberkrimineller-steht-in-zuerich-vor-gericht)); cash.ch names Lockergoga, Megacortex and a further tool called RMS. The indictment lists ten companies, four of them Swiss — Meier Tobler, Crealogix, IHI Ionbond and Stadler Rail — and records that three victims, none Swiss, paid ransoms totalling CHF 4.5 million while the Swiss companies paid nothing ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). Prosecutors put economic damage above CHF 100 million, arising from business interruption, delivery delays, work stoppages and the special measures the companies had to mount ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)).

Unusually for court reporting, the operational sequence is in the charge sheet. Per cash.ch's account of the indictment, the group obtained access to the systems, switched off monitoring processes, and then encrypted servers as well as workstations ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)); 20 Minuten records the group's stated objective as penetrating as many company networks as possible in Western Europe and North America and encrypting the data including the backup files ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489)). At Stadler Rail the defendant is additionally accused of taking around 500 gigabytes of confidential data and threatening to publish it to increase pressure — double extortion, inside the charged period Netzwoche dates to December 2018 to May 2020 ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362)).

**The Mabna indictment.** The Department of Justice unsealed a 14-count superseding indictment on 2026-08-18 charging 17 members of the Mabna Institute, an Iran-based company that in its words "since at least 2013, has conducted a coordinated campaign of cyber intrusions into computer systems for 144 U.S.-based universities, 178 foreign universities, at least 42 U.S.-based private sector companies, at least 11 foreign private sector companies, at least five U.S. federal and state government agencies, and at least two non-governmental organizations (NGOs)" ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)). Nine of the seventeen were charged in 2018; eight are new. Switzerland appears twice in DOJ's own victim breakdown — among the countries hosting the 178 compromised foreign universities, and among the countries hosting the roughly 11 foreign companies whose employee email accounts were compromised, alongside Germany, Italy, Sweden and the United Kingdom ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)). The tradecraft against universities is stolen credentials used to log into professor accounts and pull research; the newly charged conduct against companies and at least two governmental entities is password spraying, which DOJ says cost victims in excess of $20 million to investigate and remediate.

**Why two charge sheets are worth a strategic entry.** Not for attribution — neither changes what anyone hunts for tomorrow, and both sets of allegations are untested. They are worth it for two properties that vendor reporting cannot supply. The first is evidentiary standing: the ordering that every ransomware detection strategy is built around — impair defences, *then* encrypt, and take the backups in the same operation — is here as a prosecution's account of specific attacks on named companies, not as a vendor's characterisation of an intrusion set. That is a different quality of evidence for anyone who has to argue a control budget. The second is the timescale, and it cuts the other way: the Zurich charged period ends in May 2020 and the trial reaches verdict on 2026-09-10; the Mabna university campaign is dated from around 2013 through at least December 2017 and its second wave of defendants is being charged now. Attribution and consequence arrive on a judicial clock measured in years, and the defensive posture that has to work in the meantime cannot be built on it.

**Defender takeaway:** the transferable content is that both filings describe techniques that are entirely current, which is the uncomfortable part of reading a six-year-old indictment and recognising this week's telemetry. For the ransomware case: defence impairment precedes encryption, so the alerting weight belongs before any file changes — security service and agent stop events, sudden gaps in endpoint agent check-ins across multiple hosts, audit or logging services terminating outside a maintenance window — and backup infrastructure is a target inside the same operation rather than a recovery path after it, which puts authentication and deletion activity against backup catalogues in the same alerting tier as domain controllers. For the espionage case: the durable observable is authentication behaviour rather than malware, and password spraying has a distinctive shape — a small number of common passwords tried against a large number of distinct accounts from a limited set of source addresses, producing failures spread thinly across identities rather than concentrated on one. **Triage:** legitimate maintenance also stops security agents and touches backup stores, so the separators are that maintenance is scoped to a change window and a host set, is performed by accounts that routinely do it, and does not fan out across servers and workstations at once. For the spray shape, bulk authentication failures do occur legitimately after a password-policy change or a mass credential expiry; the discriminators are that a spray distributes one credential across many accounts rather than many credentials against one, arrives from infrastructure with no prior relationship to the tenant, and produces a small number of successes that are followed immediately by data access rather than by normal interactive work.
