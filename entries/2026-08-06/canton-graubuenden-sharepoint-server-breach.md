---
schema: 1
kind: incident
horizon: operational
title: "Canton Graubünden discloses a SharePoint server breach a day after the Confederation did — the on-premises wave has reached Swiss cantonal government"
headline: "A second Swiss public-sector SharePoint victim in 48 hours, and the intrusion sat unnoticed for a week"
summary: >
  The IT office of the Swiss canton of Graubünden disclosed on 2026-08-05 — one day after Switzerland's federal IT
  provider BIT disclosed an intrusion into its own on-premises SharePoint estate — that a SharePoint server hosting
  the cantonal administration's public web presence was compromised on the afternoon of 29 July 2026. Two
  files were placed on the cantonal server but their code was not executed, and a first analysis found no
  compromised accounts and no data exfiltration; confidential and specially-protected personal data are not held
  on those servers. The canton's IT chief says it could be the same vulnerability found at federal level, but
  neither Swiss disclosure names a CVE, and the canton shipped an out-of-band update on the evening of 5 August.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-07-29"
run_id: 2026-08-06T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited]
regions: [switzerland]
sectors: [public-sector]
entities:
  - incident:graubuenden-canton-sharepoint-breach-2026-08
  - incident:foitt-bit-sharepoint-breach-2026-07
techniques: [T1190, T1105]
affected_products: ["Microsoft SharePoint Server"]
cves: []
sources:
  - url: "https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx"
    publisher: "Kanton Graubünden — Standeskanzlei"
    date: "2026-08-05"
    role: primary
  - url: "https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden"
    publisher: "persoenlich.com (Keystone-SDA)"
    date: "2026-08-05"
    role: corroborating
  - url: "https://www.swissinfo.ch/eng/various/graub%C3%BCnden-has-also-fallen-victim-to-a-cyber-attack/91851604"
    publisher: "swissinfo.ch"
    date: "2026-08-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Das Amt für Informatik hat einen Cyberangriff auf einen SharePoint-Server des Kantons festgestellt."
    publisher: "Kanton Graubünden — Standeskanzlei"
  - quote: "Eine erste Analyse hat ergeben, dass es keine Anzeichen darauf gibt, dass Konten kompromittiert oder Daten abgeflossen sind."
    publisher: "Kanton Graubünden — Standeskanzlei"
  - quote: "Es wurden zwei Dateien platziert, deren Code allerdings nicht ausgeführt worden sei."
    publisher: "persoenlich.com (Keystone-SDA)"
verification: single-source-victim
sourcing_note: >
  Every substantive fact traces to the canton as the disclosing victim — its own press release plus the additional
  timeline and artifact detail its IT-office head gave the Keystone-SDA news agency; swissinfo.ch and other outlets
  republish that account rather than assessing it independently, so this is one assessor with several publishers.
  No CVE is named by either the cantonal or the federal disclosure, and the link between the two Swiss incidents is
  the cantonal IT chief's own stated possibility, not a confirmed technical finding.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Search every on-premises SharePoint farm in cantonal and communal estates for files created under the web-application or layouts directories between 20 July and 5 August 2026, regardless of current patch level — Graubünden found two planted files on a farm where no account compromise and no data loss were detected, so a clean identity picture does not rule the farm out."
migrated_from: null
---

The Amt für Informatik (AFI) of Canton Graubünden detected a cyberattack against the SharePoint server that hosts the cantonal administration's public web presence ([Kanton Graubünden, 2026-08-05](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx)). The canton's own account is that a first analysis found no indication that accounts were compromised or data exfiltrated, and that confidential information and specially-protected personal data are not stored on those web-presence servers in the first place; the cantonal ePortal and specialised applications were unaffected and remained reachable through the remediation ([Kanton Graubünden, 2026-08-05](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx)). AFI head Lorenz Tanner, speaking to the Keystone-SDA news agency, put the intrusion on the afternoon of 29 July and said two files were placed on the server whose code was not executed — meaning the compromise sat unremarked for roughly a week before disclosure ([persoenlich.com, 2026-08-05](https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden)). AFI carried out an extraordinary update from the evening of 5 August ([persoenlich.com, 2026-08-05](https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden)), during which the canton said its website would be unreachable for several hours ([Kanton Graubünden, 2026-08-05](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx)).

What makes this operationally significant for the constituency is not the canton's own limited damage but the pattern: this is the second confirmed Swiss public-sector victim of on-premises SharePoint exploitation disclosed in two days, after the Confederation's IT provider BIT reported roughly 200 compromised federal user and technical accounts (covered here on 2026-08-05). Tanner's stated view is that it could be the same vulnerability identified at federal level, one he describes as affecting SharePoint systems worldwide, and AFI is coordinating with the Federal Office for Cybersecurity ([persoenlich.com, 2026-08-05](https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden)). That link is a plausibility stated by the victim, not a confirmed technical finding — neither Swiss disclosure names a CVE, and no authority has published one for either incident, so an operator should treat "same flaw as the Confederation" as a working hypothesis rather than a scoping fact.

**Defender takeaway:** the two Swiss cases differ in outcome in a way that matters for how you scope your own check. BIT lost credentials for roughly 200 accounts; Graubünden reports no account compromise at all but did find planted files. An estate that finds no identity-side evidence has therefore not cleared itself — the observable at Graubünden was file creation on the server, and the gap between the 29 July intrusion and the 5 August disclosure is the window in which nothing was noticed. Behaviourally, the activity to look for is a web-facing SharePoint server writing new files into content or application directories, and any child process spawned by the IIS worker process serving that site; both surface in file-creation telemetry and process-lineage telemetry without needing a CVE to key on.

**Triage:** SharePoint farms legitimately write files into those directories during solution deployments, patch installation and content updates, so file creation alone is not the signal. The discriminators are timing and actor — writes that fall outside a change window, that are not attributable to an administrator session or a deployment job, and that are performed by the web-server worker process rather than the update or deployment tooling. A file that never executes, as at Graubünden, produces no process-execution event at all, so a detection strategy resting only on child-process spawning would have missed this one.
