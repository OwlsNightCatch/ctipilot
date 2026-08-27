---
schema: 1
kind: incident
horizon: operational
title: >
  Romania's national cadastre agency ANCPI hit by a multi-day cyberattack; ByteToBreach claims
  citizen-data and e-Terra source-code theft plus ransomware
headline: >
  Romanian land-registry authority ANCPI down for days after a cyberattack; data-leak operator
  ByteToBreach claims theft and ransomware
summary: >
  Romania's National Agency for Cadastre and Real Estate Publicity (ANCPI) — the government
  authority running the national land-registry and cadastre systems (e-Terra, RENNS) used by
  citizens, notaries, banks and other authorities — has had all IT systems down since 14 July 2026
  after what it confirmed is a cyberattack. A data-leak operator using the alias ByteToBreach,
  tracked by KELA and with a cross-country victimology spanning government, banking and other
  sectors, claims to have stolen Romanian-citizen data and the e-Terra/RENNS source code from a
  copied GitLab server, deployed ransomware, and begun deleting backups; ANCPI disputes that its
  data was compromised. A live, unresolved EU public-sector incident.
discovered_at: "2026-07-19T04:24:00Z"
updated_at: "2026-07-26T13:55:00Z"
event_date: 2026-07-14
run_id: 2026-07-19T0408Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
  - hacktivism
regions:
  - europe
sectors:
  - public-sector
entities:
  - "actor:bytetobreach"
  - "incident:ancpi-romania-cyberattack-2026-07"
techniques:
  - T1190
  - T1078
  - T1110
  - T1213
  - T1486
  - T1490
  - T1485
  - T1005
affected_products:
  - VMware vCenter Server
  - VMware ESXi
cves: []
sources:
  - url: "https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/"
    publisher: Help Net Security
    date: 2026-07-16
    role: primary
  - url: "https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/"
    publisher: Public Record (RO investigative outlet)
    date: 2026-07-17
    role: corroborating
  - url: "https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/"
    publisher: KELA Cyber
    date: 2026-07-17
    role: corroborating
  - url: "https://www.digi24.ro/stiri/actualitate/agentia-nationala-de-cadastru-spune-ca-bazele-de-date-nu-au-fost-afectate-cand-se-reiau-serviciile-3870161"
    publisher: Digi24 (Romania)
    date: 2026-07-20
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/"
    publisher: Risky Business News
    date: 2026-07-20
    role: corroborating
  - url: "https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/"
    publisher: go4it.ro (relaying the DNSC interim technical report)
    date: 2026-07-24
    role: primary
  - url: "https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/"
    publisher: PS News (relaying the same DNSC report)
    date: 2026-07-24
    role: corroborating
  - url: "https://www.go4it.ro/securitate-informatica/seful-dnsc-despre-atacul-cibernetic-de-la-cadastru-putea-fi-prevenit-hackerii-au-exploatat-vulnerabilitati-deja-cunoscute-19279543/"
    publisher: go4it.ro (DNSC director statement)
    date: 2026-07-18
    role: corroborating
closed_sources: []
evidence:
  - quote: "They claim to have compromised data of Romanian citizens and various ANCPI databases, made a copy of the agency's GitLab servers and the source code contained within, and deployed ransomware."
    publisher: Help Net Security
  - quote: ANCPI stated that the data administered through its IT systems has not been compromised as a result of this incident.
    publisher: Help Net Security
  - quote: "Exploiting known vulnerabilities in cloud and corporate infrastructure, reusing stolen credentials harvested from infostealers and phishing, and at times resorting to brute force"
    publisher: KELA Cyber
  - quote: "The hacker entered using valid credentials, mapped internal systems, and wiped systems and backups after failing to extort the agency."
    publisher: Risky Business News
  - quote: "KELA assesses the actor behind the campaign, ByteToBreach, is likely operated by Zakaria Mahdjoub, an individual based in Oran, Algeria."
    publisher: KELA Cyber Intelligence Center
  - quote: "atacatorii au extras aproximativ două milioane de înregistrări privind utilizatori ai platformei de plăți, care conțineau: nume; e-mailuri; identificatori; hash-uri ale parolelor"
    publisher: PS News (relaying the same DNSC report)
  - quote: "au compromis serverele de autentificare; au pătruns în VMware vCenter, adică sistemul care administrează întreaga infrastructură virtuală; au enumerat toate cele 1.083 de mașini virtuale; au executat mișcare laterală în rețea; au șters aproximativ 100 de mașini virtuale; au criptat servere ESXi cu ransomware"
    publisher: PS News (relaying the same DNSC report)
  - quote: "infrastructura ANCPI nu beneficia de un antivirus instalat pe serverele care rulau aplicațiile principale"
    publisher: go4it.ro (relaying the DNSC interim technical report)
  - quote: "nu există indicii că baza de date principală Oracle Exadata ar fi fost compromisă"
    publisher: go4it.ro (relaying the DNSC interim technical report)
verification: multi-source
sourcing_note: >
  The cyberattack and the multi-day systems outage are confirmed by ANCPI's own statements as
  relayed by multiple outlets. The theft, source-code-copy and ransomware-deployment claims are
  ByteToBreach's dark-web-forum assertions relayed by Help Net Security; the backup-deletion claim
  and the vendor-contract detail are from Public Record's investigation (the backup-deletion is
  quoted from a screenshot the attacker himself published). All are unverified and directly
  contradicted by ANCPI's data-not-compromised position; credibility rated 2 accordingly. The
  initial-access techniques are KELA's documented profile of the actor's general tradecraft, not a
  confirmed reconstruction of this intrusion.
confidence: medium
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-21T04:45:00Z"
    run_id: 2026-07-21T0409Z-intel
    type: update
    summary: >
      Update on the ANCPI (Romanian National Agency for Cadastre) cyberattack: on 2026-07-20 the
      agency stated, after security verification, that its technical and legal databases "have not
      been affected" — directly contradicting data-leak operator ByteToBreach's claim of deleting
      backups after a failed extortion. ANCPI is migrating its applications to the Romanian Government
      Cloud, expected to finish 22 July, before any phased service restoration. KELA separately
      profiled the ByteToBreach operator; the contradiction between the wipe claim and the "databases
      intact" statement is itself the notable fact — both are held, neither is resolved.
    fields:
      - evidence
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-21/ancpi-romania-cadastre-databases-not-affected-update
  - at: "2026-07-26T13:55:00Z"
    run_id: 2026-07-26T1308Z-audit
    type: update
    summary: >
      Romania's national cybersecurity directorate DNSC published an interim technical report on the
      ANCPI national land-registry attack that materially supersedes the agency's earlier "databases
      not affected" assurance. DNSC describes compromise of the authentication servers, entry into
      VMware vCenter, enumeration of all 1,083 virtual machines, deletion of roughly 100 of them and
      ransomware encryption of ESXi hosts — plus exfiltration of approximately two million ePayment
      platform user records (names, e-mail addresses, identifiers and password hashes). The "core
      database intact" claim survives only for the Oracle Exadata database specifically.
    fields:
      - affected_products
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-07-26/ancpi-romania-dnsc-report-2m-epayment-records-exfiltrated
migrated_from: null
---

Romania's **National Agency for Cadastre and Real Estate Publicity (ANCPI)** — the government body operating the national land-registry and cadastre platforms (the e-Terra cadastral application and RENNS) that citizens, notaries, lawyers, banks and other authorities depend on for property transactions — has had all of its IT systems, including institutional email, offline since Tuesday 14 July 2026, in what it first called a "technical incident" before confirming a cyberattack; as of 17 July the systems remained down pending investigation ([Help Net Security, 2026-07-16](https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/); [Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)). A threat actor using the alias **ByteToBreach** posted ANCPI data for sale on a dark-web forum on 15 July, claiming to hold Romanian-citizen records and various ANCPI databases, a copied GitLab server carrying the source code for e-Terra and RENNS, and to have deployed a ransomware variant ([Help Net Security, 2026-07-16](https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/)); in a screenshot the attacker published, he also states he began deleting the available backups ([Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)). ANCPI states the data it administers "has not been compromised as a result of this incident" — a position not yet reconciled with the attacker's claims.

KELA, which profiles ByteToBreach as a persistent data-leak operator active since June 2025, documents the actor's general initial-access tradecraft as "exploiting known vulnerabilities in cloud and corporate infrastructure, reusing stolen credentials harvested from infostealers and phishing, and at times resorting to brute force," with a victim list spanning government, banking and other sectors across multiple countries — a bank in Poland among the organizations that acknowledged their breaches ([KELA Cyber, 2026-07-17](https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/)). Public Record's investigation reports that ANCPI's ~1.5-million-lei framework contract for cybersecurity services required constant active services — a 24/7 call-centre, at-least-annual technical audits, and ongoing monitoring and intervention over 48 months — yet the contracted vendor's owner now characterises the firm as "just a license provider… like buying Microsoft licences on eMAG" and says he had no contractual obligation to detect an attack, a self-characterisation Public Record reports the contract's own terms directly contradict; the same reporting notes a similar December 2025 cyberattack on Romania's National Water Administration (ANAR, roughly 1,000 systems affected), an agency the same security vendors had also supplied ([Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)).

**Defender takeaway:** the transferable signal for a public-sector defender is twofold. First, ByteToBreach is a tracked actor with a demonstrated appetite for EU-member government registries, and its documented access mix is entirely generic — so the hunt is on the technique classes, not an IOC: anomalous authentication consistent with stolen-credential reuse against internet-facing admin surfaces, brute-force lockout/anomaly patterns on public-facing portals, and unexpected source-control (GitLab) repository or API pulls of whole-repository scope. Second, the reported governance gap is an auditable lesson: ANCPI's contract on paper required 24/7 monitoring, intervention and annual audits, yet the vendor now disclaims that role and any duty to detect an attack — so verify not merely that a third-party security contract exists but that its required monitoring and detection obligations are actually being performed and owned, rather than assuming the vendor's name or the contract's title implies live coverage. Public Record frames the same vendors and the same gap across two Romanian public-sector/critical-infrastructure incidents in seven months (ANCPI now, ANAR in December 2025). **Triage:** a legitimate bulk GitLab clone or backup-management operation is scheduled, runs from a known service account and host, and is logged in change management; the same repository-scope pull or mass backup deletion from an interactive session, an unfamiliar host, or outside a change window is the signal.

## Update — 2026-07-21T04:45:00Z

The still-open ANCPI (Romanian National Agency for Cadastre and Real Estate Publicity) incident developed on two fronts. First, an impact contradiction: on 2026-07-20 ANCPI stated publicly, following completed security verification, that its technical and legal databases had not been affected ([Digi24, 2026-07-20](https://www.digi24.ro/stiri/actualitate/agentia-nationala-de-cadastru-spune-ca-bazele-de-date-nu-au-fost-afectate-cand-se-reiau-serviciile-3870161)) — squarely against extortion operator ByteToBreach's earlier claim, reported by Risky Business News, that the "hacker entered using valid credentials, mapped internal systems, and wiped systems and backups after failing to extort the agency" ([Risky Business News, 2026-07-20](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/)). The agency frames the multi-day e-Terra/RENNS outage (down since 14 July) as deliberate protective isolation and says it is migrating applications to the Romanian Government Cloud, coordinated by the Special Telecommunications Service, expected to complete 22 July before any phased service restoration.

Second, actor context: KELA's updated profile assesses ByteToBreach is likely a single operator based in Oran, Algeria, active since June 2025 across forums, Dread, Telegram and a storefront, with a victim set spanning government, banking, airline and university targets across several countries, and access methods documented as cloud/corporate-infrastructure exploitation, reuse of infostealer/phishing-harvested credentials, and brute force ([KELA, 2026-07-17](https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/)). **Defender takeaway:** the contradiction is unresolved and should be held both ways rather than settled — an agency "databases intact" statement and an attacker "backups wiped" claim can both be partially true (e.g. production preserved, some systems/backups damaged). For CH/EU cantonal and national registries the transferable pattern is concrete: valid-credential entry followed by destructive follow-through after a failed extortion is a documented combined objective against national e-government/cadastre platforms, independent of any software CVE, so identity-plane monitoring and offline, integrity-verified registry backups are the controls that matter for this class of target.

## Update — 2026-07-26T13:55:00Z

The picture of the attack on ANCPI, Romania's national cadastre and land-registration agency, has changed substantially. Earlier coverage recorded the agency's own position that its databases were not affected. Romania's national cybersecurity directorate DNSC has since published an interim technical report, relayed with direct quotation by Romanian technology press, that supersedes that framing on the point that matters most: the attackers extracted approximately two million records concerning users of the payment platform, containing names, e-mail addresses, identifiers and password hashes — in the report's Romanian, "atacatorii au extras aproximativ două milioane de înregistrări privind utilizatori ai platformei de plăți, care conțineau: nume; e-mailuri; identificatori; hash-uri ale parolelor" ([PS News, 2026-07-24](https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/)). The "databases not affected" assurance survives only in a much narrower form — DNSC states there is no indication the main Oracle Exadata database was compromised ([go4it.ro, 2026-07-24](https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/)) — which is a different claim from "no data was taken", since a separate payment-platform datastore demonstrably was.

The intrusion path DNSC describes is the one that makes a virtualized government estate fail all at once. Per the report the attackers compromised the authentication servers, penetrated VMware vCenter — the system administering the entire virtual infrastructure — enumerated all 1,083 virtual machines, executed lateral movement, deleted approximately 100 virtual machines and encrypted ESXi servers with ransomware ([PS News, 2026-07-24](https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/)). Identity compromise first, then the virtualization control plane, then destruction at the hypervisor layer beneath every guest operating system — the per-VM security stack never gets a vote. Source code for the eTerra, GIS, ePayment and security modules was taken from the agency's GitLab as well. DNSC's account of why it worked is unusually blunt for a national authority — the ANCPI infrastructure had no antivirus installed on the servers running its main applications ([go4it.ro, 2026-07-24](https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/)), alongside known unpatched vulnerabilities and a web-application firewall retaining connection logs for only seven minutes — which is also why the forensic picture is partial. DNSC's director had already assessed on 2026-07-18 that the attack exploited already-known vulnerabilities and could have been prevented ([go4it.ro, 2026-07-18](https://www.go4it.ro/securitate-informatica/seful-dnsc-despre-atacul-cibernetic-de-la-cadastru-putea-fi-prevenit-hackerii-au-exploatat-vulnerabilitati-deja-cunoscute-19279543/)).

**Defender takeaway:** for a European public-sector body running a comparable estate, the transferable lessons are the vCenter blast radius and the log-retention gap, not the victim. An administrative account that can reach vCenter is an account that can delete or encrypt every workload behind it, so vCenter and ESXi management interfaces belong on separate authentication and network paths from general server administration; and a WAF that keeps connection logs for seven minutes cannot answer the only question that matters after an incident. Note also the shape of the disclosure timeline: the victim's early "databases not affected" statement was accurate about one database and misleading about the incident, which is the normal pattern for first-week victim communications and a reason to treat them as provisional.

**Triage:** in vCenter and ESXi audit telemetry, the discriminating sequence is not any single administrative action but the ordering — an authentication from an unusual source or service account, followed by a full inventory enumeration of virtual machines, followed by power-off or delete operations across guests that share no application grouping. Routine administration enumerates inventory constantly and backup tooling touches many VMs, so volume alone is noise; the signal is enumeration by a principal that does not normally perform it, immediately followed by destructive operations spanning unrelated workloads.
