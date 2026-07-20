---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "Swiss and European public-sector, utility and transport organisations carried the week's home-region incident load — a land registry offline for days, two Swiss utilities/foundations hit through third parties, an EU transit ransomware and a EUR 1.7M telco enforcement"
headline: "W29 home-region incidents — ANCPI Romania offline for days, IWB Basel and Geneva's IFAGE breached, Metro Mondego ransomware, Wind Tre fined EUR 1.7M"
summary: >
  The incidents with a direct Swiss/European home-region or coverage-focus nexus this week clustered squarely on public-sector and critical-infrastructure organisations. Romania's national cadastre authority ANCPI had all IT systems down since 14 July after a confirmed cyberattack, with data-leak operator ByteToBreach claiming data theft, source-code exfiltration and ransomware. Two Swiss organisations were hit through third parties — the Basel canton utility IWB (electricity/gas/water/telecom) lost ~40,000 customer meter records via a compromised service provider, and Geneva adult-education foundation IFAGE was listed by DragonForce (850 GB claimed, unconfirmed). Portugal's Metro Mondego confirmed a 6 July ransomware attack (TheGentlemen claim) that its IT/OT segmentation kept off the transit service. Italy's Garante fined Wind Tre EUR 1.7M for a retail-staff-vishing-to-API-enumeration breach of 365,048 customers, and Ernst & Young disclosed a third-party ITSM-platform breach exposing client tax data. Underneath the incidents, NCSC-CH flagged an unauthenticated RCE (CVSS 9.8) in Abacus ERP — ubiquitous across Swiss SMEs, associations and public-sector-adjacent bodies — as the week's largest latent home-region exposure.
discovered_at: "2026-07-19T23:50:00Z"
event_date: 2026-07-17
run_id: 2026-07-19T2310Z-weekly
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - switzerland
  - europe
sectors:
  - public-sector
  - energy
  - water
  - transport
  - telco
entities:
  - incident:ancpi-romania-cyberattack-2026-07
  - actor:bytetobreach
  - incident:iwb-basel-service-provider-breach-2026-07
  - incident:ifage-geneva-dragonforce-leak-claim-2026-07
  - actor:dragonforce
  - incident:wind-tre-2026-vishing-api-enumeration-breach
  - incident:ey-third-party-itsm-breach-2026
  - actor:thegentlemen
cves: []
techniques:
  - T1486
  - T1190
  - T1199
sources:
  - url: "https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/"
    publisher: "Help Net Security"
    date: "2026-07-16"
    role: primary
  - url: "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10263796"
    publisher: "Garante per la protezione dei dati personali (Provvedimento n.348)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.netzwoche.ch/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel"
    publisher: "Netzwoche"
    date: "2026-07-15"
    role: corroborating
  - url: "https://www.campeaoprovincias.pt/2026/07/17/metro-mondego-foi-alvo-de-ataque-informatico-que-afectou-sistemas-internos/"
    publisher: "Campeão das Províncias (relaying Metro Mondego)"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Confirmed strands (Wind Tre Garante decision, EY breach-notification filing, IWB corroborated across three Swiss outlets, ANCPI's own outage confirmation, Metro Mondego's own statement) sit alongside unconfirmed extortion claims (IFAGE/DragonForce 850 GB and ByteToBreach's ANCPI data-theft claim, both attributed to the group and disputed or unconfirmed by the victim) — hence credibility 2 for the entry as a whole; each strand's status is stated in the body."
confidence: high
update_of: null
references:
  - 2026-07-19/ancpi-romania-cadastre-cyberattack-bytetobreach
  - 2026-07-16/iwb-basel-third-party-provider-breach-40k-customer-records
  - 2026-07-14/dragonforce-leak-claim-ifage-geneva-adult-education
  - 2026-07-18/metro-mondego-thegentlemen-ransomware-portugal-transit
  - 2026-07-17/garante-wind-tre-vishing-api-enumeration-fine
  - 2026-07-19/ernst-young-third-party-itsm-platform-breach-client-tax-data
  - 2026-07-17/abacus-erp-unauth-rce-path-traversal-ncsc-ch
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

The home-region incident load this week fell almost entirely on public administration, utilities and transport — the profiled constituency's core — and split into three recognisable shapes.

**Direct public-sector disruption.** Romania's National Agency for Cadastre and Real Estate Publicity (ANCPI) — the authority running the national land-registry and cadastre systems (e-Terra, RENNS) used by citizens, notaries and banks — had all IT systems offline from 14 July after a confirmed cyberattack; a data-leak operator using the alias ByteToBreach (tracked by KELA) claims to have stolen citizen data and the e-Terra/RENNS source code from a copied GitLab server, deployed ransomware and begun deleting backups, which ANCPI disputes ([Help Net Security, 2026-07-16](https://www.helpnetsecurity.com/2026/07/16/romania-ancpi-cyber-attack/)). Portugal's Metro Mondego confirmed a 6 July ransomware attack on internal systems — claimed by TheGentlemen — that its IT/OT separation kept off the Metrobus service, a clean example of segmentation limiting blast radius ([Campeão das Províncias, 2026-07-17](https://www.campeaoprovincias.pt/2026/07/17/metro-mondego-foi-alvo-de-ataque-informatico-que-afectou-sistemas-internos/)).

**Swiss organisations hit through their suppliers.** The Basel canton utility IWB (electricity, gas, water, telecom) disclosed that a compromised external service provider exfiltrated ~40,000 customer meter records (names, addresses, meter numbers) — IWB's own systems and supply were unaffected and the Basel-Stadt data-protection officer assessed misuse risk as low ([Netzwoche, 2026-07-15](https://www.netzwoche.ch/news/2026-07-15/cyberangriff-auf-dienstleister-trifft-industrielle-werke-basel)). Geneva adult-education foundation IFAGE was listed by DragonForce claiming 850 GB, layered onto a narrower April breach it had already disclosed — single-sourced and unconfirmed, a watch item rather than an established breach.

**Enforcement and cross-border tax-data exposure.** Italy's Garante fined Wind Tre EUR 1,715,600 with an unusually complete technical account: retail-staff vishing led to valid MFA'd access, then a pivot from a protected primary API to an unprotected secondary API and ~2 million sequential `customerId` requests exfiltrating 365,048 customers ([Garante, 2026-07-16](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10263796)). Ernst & Young separately disclosed a third-party ITSM-platform breach exposing client tax data.

**Defender takeaway:** the pattern for a Swiss/EU public-sector or CI defender is that this week's home-region damage came less from novel exploitation than from third-party exposure (IWB, EY), extortion pressure on public bodies (ANCPI, Metro Mondego, IFAGE) and an enumeration-reachable secondary API that testing never exercised (Wind Tre) — and that the largest *latent* Swiss exposure is the unauthenticated Abacus ERP RCE NCSC-CH flagged, given how broadly Abacus is deployed across the SME and public-sector-adjacent estate. The per-incident specifics and the Abacus patch path are in the referenced operational entries.
