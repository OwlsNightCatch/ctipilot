---
schema: 1
kind: incident
horizon: operational
title: "Romania's national cadastre agency ANCPI hit by a multi-day cyberattack; ByteToBreach claims citizen-data and e-Terra source-code theft plus ransomware"
headline: "Romanian land-registry authority ANCPI down for days after a cyberattack; data-leak operator ByteToBreach claims theft and ransomware"
summary: >
  Romania's National Agency for Cadastre and Real Estate Publicity (ANCPI) — the government authority
  running the national land-registry and cadastre systems (e-Terra, RENNS) used by citizens, notaries,
  banks and other authorities — has had all IT systems down since 14 July 2026 after what it confirmed is
  a cyberattack. A data-leak operator using the alias ByteToBreach, tracked by KELA and with a cross-country
  victimology spanning government, banking and other sectors, claims to have stolen Romanian-citizen
  data and the e-Terra/RENNS source code from a copied GitLab server, deployed ransomware, and begun
  deleting backups; ANCPI disputes that its data was compromised. A live, unresolved EU public-sector incident.
discovered_at: "2026-07-19T04:24:00Z"
event_date: "2026-07-14"
run_id: 2026-07-19T0408Z-intel
priority: notable
immediate_action: null
tags: [data-breach, ransomware, organized-crime]
regions: [europe]
sectors: [public-sector]
entities: ["actor:bytetobreach", "incident:ancpi-romania-cyberattack-2026-07"]
techniques: [T1190, T1078, T1110, T1213, T1486, T1490]
affected_products: []
cves: []
sources:
  - url: "https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/"
    publisher: "Help Net Security"
    date: "2026-07-16"
    role: primary
  - url: "https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/"
    publisher: "Public Record (RO investigative outlet)"
    date: "2026-07-17"
    role: corroborating
  - url: "https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/"
    publisher: "KELA Cyber"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "They claim to have compromised data of Romanian citizens and various ANCPI databases, made a copy of the agency's GitLab servers and the source code contained within, and deployed ransomware."
    publisher: "Help Net Security"
  - quote: "ANCPI stated that the data administered through its IT systems has not been compromised as a result of this incident."
    publisher: "Help Net Security"
  - quote: "Exploiting known vulnerabilities in cloud and corporate infrastructure, reusing stolen credentials harvested from infostealers and phishing, and at times resorting to brute force"
    publisher: "KELA Cyber"
verification: multi-source
sourcing_note: "The cyberattack and the multi-day systems outage are confirmed by ANCPI's own statements as relayed by multiple outlets. The theft, source-code-copy and ransomware-deployment claims are ByteToBreach's dark-web-forum assertions relayed by Help Net Security; the backup-deletion claim and the vendor-contract detail are from Public Record's investigation (the backup-deletion is quoted from a screenshot the attacker himself published). All are unverified and directly contradicted by ANCPI's data-not-compromised position; credibility rated 2 accordingly. The initial-access techniques are KELA's documented profile of the actor's general tradecraft, not a confirmed reconstruction of this intrusion."
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

Romania's **National Agency for Cadastre and Real Estate Publicity (ANCPI)** — the government body operating the national land-registry and cadastre platforms (the e-Terra cadastral application and RENNS) that citizens, notaries, lawyers, banks and other authorities depend on for property transactions — has had all of its IT systems, including institutional email, offline since Tuesday 14 July 2026, in what it first called a "technical incident" before confirming a cyberattack; as of 17 July the systems remained down pending investigation ([Help Net Security, 2026-07-16](https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/); [Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)). A threat actor using the alias **ByteToBreach** posted ANCPI data for sale on a dark-web forum on 15 July, claiming to hold Romanian-citizen records and various ANCPI databases, a copied GitLab server carrying the source code for e-Terra and RENNS, and to have deployed a ransomware variant ([Help Net Security, 2026-07-16](https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/)); in a screenshot the attacker published, he also states he began deleting the available backups ([Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)). ANCPI states the data it administers "has not been compromised as a result of this incident" — a position not yet reconciled with the attacker's claims.

KELA, which profiles ByteToBreach as a persistent data-leak operator active since June 2025, documents the actor's general initial-access tradecraft as "exploiting known vulnerabilities in cloud and corporate infrastructure, reusing stolen credentials harvested from infostealers and phishing, and at times resorting to brute force," with a victim list spanning government, banking and other sectors across multiple countries — a bank in Poland among the organizations that acknowledged their breaches ([KELA Cyber, 2026-07-17](https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/)). Public Record's investigation reports that ANCPI's ~1.5-million-lei framework contract for cybersecurity services required constant active services — a 24/7 call-centre, at-least-annual technical audits, and ongoing monitoring and intervention over 48 months — yet the contracted vendor's owner now characterises the firm as "just a license provider… like buying Microsoft licences on eMAG" and says he had no contractual obligation to detect an attack, a self-characterisation Public Record reports the contract's own terms directly contradict; the same reporting notes a similar December 2025 cyberattack on Romania's National Water Administration (ANAR, roughly 1,000 systems affected), an agency the same security vendors had also supplied ([Public Record, 2026-07-17](https://publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/)).

**Defender takeaway:** the transferable signal for a public-sector defender is twofold. First, ByteToBreach is a tracked actor with a demonstrated appetite for EU-member government registries, and its documented access mix is entirely generic — so the hunt is on the technique classes, not an IOC: anomalous authentication consistent with stolen-credential reuse against internet-facing admin surfaces, brute-force lockout/anomaly patterns on public-facing portals, and unexpected source-control (GitLab) repository or API pulls of whole-repository scope. Second, the reported governance gap is an auditable lesson: ANCPI's contract on paper required 24/7 monitoring, intervention and annual audits, yet the vendor now disclaims that role and any duty to detect an attack — so verify not merely that a third-party security contract exists but that its required monitoring and detection obligations are actually being performed and owned, rather than assuming the vendor's name or the contract's title implies live coverage. Public Record frames the same vendors and the same gap across two Romanian public-sector/critical-infrastructure incidents in seven months (ANCPI now, ANAR in December 2025). **Triage:** a legitimate bulk GitLab clone or backup-management operation is scheduled, runs from a known service account and host, and is logged in change management; the same repository-scope pull or mass backup deletion from an interactive session, an unfamiliar host, or outside a change window is the signal.
