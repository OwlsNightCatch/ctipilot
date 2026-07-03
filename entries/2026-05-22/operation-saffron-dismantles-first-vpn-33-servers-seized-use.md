---
schema: 1
kind: threat
horizon: operational
title: "Operation Saffron dismantles First VPN — 33+ servers seized, user database captured, Switzerland named JIT participant; Phobos RaaS infrastructure link confirmed"
headline: "Operation Saffron dismantles First VPN — 33+ servers seized, user database captured, Switzerland named JIT participant; Phobos RaaS infrastructure link"
summary: "Operation Saffron seizes First VPN — Europol/Eurojust-coordinated takedown of criminal anonymisation VPN present in \"nearly every major cybercrime investigation\"; 33+ servers seized across 27 countries (server-host), 5,000+ user accounts captured; Switzerland one of seven JIT participants; Phobos RaaS infrastructure link confirmed (Help Net Security, 2026-05-21)."
discovered_at: "2026-05-22T05:00:00Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: high
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - ransomware
regions:
  - europe
  - switzerland
sectors:
  - public-sector
entities:
  - "incident:operation-saffron-first-vpn-takedown-33-servers-27-countri"
cves: []
sources:
  - url: "https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network"
    publisher: "Eurojust, 2026-05-21"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/police-seize-first-vpn-service-used-in-ransomware-data-theft-attacks/"
    publisher: "BleepingComputer, 2026-05-21"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/21/operation-saffron-first-vpn-takedown/"
    publisher: "Help Net Security, 2026-05-21"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-22.md
---

A coordinated international law enforcement action on 2026-05-19–20 took down First VPN, a Russian-language criminal anonymisation service established in 2014 and systematically marketed on cybercrime forums as a no-log, law-enforcement-resistant tool ([Eurojust, 2026-05-21](https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network)). Europol stated the service "appeared in almost every major cybercrime investigation the agency supported" ([BleepingComputer, 2026-05-21](https://www.bleepingcomputer.com/news/security/police-seize-first-vpn-service-used-in-ransomware-data-theft-attacks/)). Led by French and Dutch investigators through a Eurojust joint investigation team established in November 2023, the operation seized more than 33 servers distributed across 27 countries (server-host count); 16 nations participated through Europol's Joint Cybercrime Action Taskforce; 7 nations sat on the Eurojust-led JIT, including Switzerland, France, Netherlands, Luxembourg, Romania, Ukraine, and the UK — signalling fedpol/GovCERT.ch operational involvement. Law enforcement arrested the administrator in Ukraine, captured the full user database (over 5,000 accounts) and cryptographic connection records, and generated 83 intelligence packages covering 506 users distributed to partner agencies; Help Net Security reporting confirms the captured data links to the Phobos ransomware-as-a-service operation and broader ransomware, fraud, and data theft investigations ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/operation-saffron-first-vpn-takedown/)). The primary domains (1vpns.com, 1vpns.net, 1vpns.org) and associated .onion mirrors were seized. Historical network flows to those domains in proxy or firewall logs now constitute potential investigative leads flowing through Europol sharing channels; Phobos affiliates have repeatedly targeted EU public-sector and healthcare organisations.
