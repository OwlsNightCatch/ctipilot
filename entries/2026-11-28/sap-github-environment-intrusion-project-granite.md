---
schema: 1
kind: incident
title: "SAP: suspicious activity in its GitHub development platform (Project Granite), with reports that employee authentication tokens were stolen and source code copied or modified; SAP says it found no evidence of unauthorized access to customer business data and has not said whether any delivered software is affected"
headline: "SAP confirms suspicious activity; GitHub, Project Granite and token theft reported; no customer-data access found"
summary: >
  SAP told dpa and BleepingComputer on 2026-11-26 and 2026-11-27 that it identified suspicious activity, took measures to protect customers and has found no evidence of unauthorized access to customer business data; a letter that dpa saw in part places the activity in SAP's GitHub developer platform. DER SPIEGEL's insider reports, without SAP's confirmation, stolen employee authentication tokens and copied and possibly modified source code, and heise, relaying Handelsblatt's company circles, reports restricted GitHub access, paused development workflows and replaced signing keys. SAP has not said how the attackers got in, who they are, or whether any software delivered to customers or any signing key customers verify is affected.
discovered_at: "2026-11-28T05:06:00Z"
updated_at: null
event_date: "2026-11-26"
run_id: 2026-11-28T0355Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, data-breach, identity]
regions: [europe, switzerland]
sectors: [technology, public-sector]
entities: ["incident:sap-github-project-granite-2026-11"]
techniques: [T1528, T1213.003]
affected_products: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/"
    publisher: "BleepingComputer"
    date: "2026-11-27"
    role: primary
  - url: "https://www.tagesschau.de/wirtschaft/unternehmen/sap-hacker-angriff-100.html"
    publisher: "tagesschau.de (dpa)"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.spiegel.de/netzwelt/sap-wird-opfer-von-hackerangriff-a-6648b5ce-5d74-48dc-86ea-9469705bb91d"
    publisher: "DER SPIEGEL"
    date: "2026-11-26"
    role: corroborating
  - url: "https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html"
    publisher: "Handelsblatt"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.heise.de/news/IT-Vorfall-bei-SAP-Entwicklungssysteme-betroffen-11539973.html"
    publisher: "heise online"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/"
    publisher: "SecurityWeek"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.wiwo.de/unternehmen/it/hackerangriff-auf-sap-warum-der-vorfall-auf-github-alarmiert/100273346.html"
    publisher: "WirtschaftsWoche"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.efk.admin.ch/en/audit/dti-key-project-superb-finance-project/"
    publisher: "Swiss Federal Audit Office (EFK)"
    date: "2023-05-10"
    role: corroborating
  - url: "https://www.inside-it.ch/zuercher-finanzverwaltung-vergibt-auftrag-fuer-sap-migration-20261127"
    publisher: "Inside IT"
    date: "2026-11-27"
    role: corroborating
  - url: "https://1password.com/blog/update-on-nov-2026-security-incident"
    publisher: "1Password"
    date: "2026-11-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "SAP has identified suspicious activity and promptly implemented the necessary measures to protect its customers and preserve the security of its services"
    publisher: "BleepingComputer (SAP statement)"
    source_url: "https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/"
  - quote: "Based on our investigation to date, we have found no evidence of unauthorized access to customer business data."
    publisher: "BleepingComputer (SAP statement)"
    source_url: "https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/"
  - quote: "Insider sources say that the attacker managed to steal authentication tokens from SAP employees and leveraged them to copy and also modify SAP source code on GitHub."
    publisher: "BleepingComputer (relaying DER SPIEGEL)"
    source_url: "https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/"
  - quote: "within our platform for developer productivity and software delivery GitHub"
    original: "innerhalb unserer Plattform für Entwicklerproduktivität und Softwarebereitstellung GitHub"
    publisher: "tagesschau.de (dpa)"
    source_url: "https://www.tagesschau.de/wirtschaft/unternehmen/sap-hacker-angriff-100.html"
  - quote: "the DAX group detected the incident last week. Software development was attacked."
    original: "stellte der Dax-Konzern den Vorfall in der vergangenen Woche fest. Attackiert wurde die Softwareentwicklung."
    publisher: "Handelsblatt (company circles)"
    source_url: "https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html"
  - quote: "reports, citing group circles, that SAP restricted access to GitHub, stopped automated processes in software development and replaced signing keys."
    original: "berichtet unter Berufung auf Konzernkreise, SAP habe den Zugriff auf GitHub eingeschränkt, automatisierte Abläufe in der Softwareentwicklung gestoppt und Signaturschlüssel ausgetauscht."
    publisher: "heise online (relaying Handelsblatt)"
    source_url: "https://www.heise.de/news/IT-Vorfall-bei-SAP-Entwicklungssysteme-betroffen-11539973.html"
  - quote: "None of the reports indicate that tampered code was incorporated into software delivered to SAP customers."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/"
  - quote: "Whether customers must act, SAP has so far left open."
    original: "Ob Kunden aktiv werden müssen, ließ SAP bisher offen."
    publisher: "WirtschaftsWoche"
    source_url: "https://www.wiwo.de/unternehmen/it/hackerangriff-auf-sap-warum-der-vorfall-auf-github-alarmiert/100273346.html"
verification: multi-source
sourcing_note: >
  Three first-hand strands exist: SAP's own statement (quoted by BleepingComputer and dpa; no SAP-hosted page was found), DER SPIEGEL's insider and internal memo, and Handelsblatt's company circles, plus a letter that dpa saw in part; the other outlets restate them. DER SPIEGEL's article is paywalled, so its token-theft, source-code and AI claims were read only through relays. The containment steps (restricted GitHub access, paused workflows, replaced signing keys) are attributed to Handelsblatt by heise and others, but the Handelsblatt text readable now does not contain them and SAP has not confirmed them. SAP confirmed suspicious activity and an incident, not an attack, and it did not address token theft, code copying or modification, or the AI possibility, which comes from SPIEGEL's company sources. No source says SPIEGEL's memo and dpa's letter are one document.
confidence: medium
references:
  - 2026-11-26/1password-employee-github-account-backend-compromise
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

SAP told BleepingComputer and dpa that it identified suspicious activity, promptly took the necessary measures to protect its customers, and found no evidence of unauthorized access to customer business data on the investigation to date; it gave no vector, actor, discovery date or list of affected systems ([BleepingComputer, 2026-11-27](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/); [tagesschau.de, 2026-11-27](https://www.tagesschau.de/wirtschaft/unternehmen/sap-hacker-angriff-100.html); [Handelsblatt, 2026-11-27](https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html)). A letter that dpa saw in part places the activity within SAP's platform for developer productivity and software delivery on GitHub and asks staff to check whether they must change credentials (translated from German) ([tagesschau.de, 2026-11-27](https://www.tagesschau.de/wirtschaft/unternehmen/sap-hacker-angriff-100.html)). Handelsblatt, citing company circles, says SAP detected the incident the week before and that software development was attacked (translated from German) ([Handelsblatt, 2026-11-27](https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html)).

Reported by media from internal sources and not confirmed by SAP: DER SPIEGEL's insider says the attacker stole authentication tokens of SAP employees and used them to copy and also modify SAP source code on GitHub, and that the attackers may have had help from AI systems; heise, relaying Handelsblatt, reports that SAP restricted access to GitHub, stopped automated processes in software development and replaced signing keys; BleepingComputer, Handelsblatt and heise add that, according to SPIEGEL, SAP tracks the incident internally as Project Granite, a name SAP has not confirmed ([BleepingComputer, 2026-11-27](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/); [DER SPIEGEL, 2026-11-26](https://www.spiegel.de/netzwelt/sap-wird-opfer-von-hackerangriff-a-6648b5ce-5d74-48dc-86ea-9469705bb91d); [heise online, 2026-11-27](https://www.heise.de/news/IT-Vorfall-bei-SAP-Entwicklungssysteme-betroffen-11539973.html); [Handelsblatt, 2026-11-27](https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-kunden-fordern-lueckenlose-aufklaerung/100273138.html)). SecurityWeek notes that none of the reports indicate tampered code reached software delivered to SAP customers, and WirtschaftsWoche that SAP has left open whether customers must act ([SecurityWeek, 2026-11-27](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/); [WirtschaftsWoche, 2026-11-27](https://www.wiwo.de/unternehmen/it/hackerangriff-auf-sap-warum-der-vorfall-auf-github-alarmiert/100273346.html)). SAP is part of the Swiss public sector's estate: the Federal Audit Office says the federal administration runs SAP R/3, supported until the end of 2027 and being replaced with S/4HANA, and Inside IT reports an existing S/4HANA landscape in the canton of Zurich's administration; no Swiss impact is reported ([EFK, 2023-05-10](https://www.efk.admin.ch/en/audit/dti-key-project-superb-finance-project/); [Inside IT, 2026-11-27](https://www.inside-it.ch/zuercher-finanzverwaltung-vergibt-auftrag-fuer-sap-migration-20261127)).

**Exposure:** organisations that consume SAP-delivered code, packages or updates, or verify SAP signatures; SAP has said nothing on which artifacts or keys are in scope, and no source says delivered software is affected ([SecurityWeek, 2026-11-27](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/)).

**Detection:** the reported behaviour is use of stolen employee tokens against a source-control platform; for SAP customers the observable is on their side of the boundary, namely the provenance of SAP-delivered artifacts and any signing-key change in SAP's own communications.

**Defender takeaway:** SAP customers should watch SAP's own security communications for which artifacts or signing keys are in scope and verify any key change through SAP's channel; no customer action has been published, and SAP declined to say whether customers pulling SAP code from GitHub should act ([BleepingComputer, 2026-11-27](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/)). For your own pipelines, 1Password disclosed on 2026-11-25 an intrusion through an employee's corporate GitHub account ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)); review how employee tokens reach source control and CI.
