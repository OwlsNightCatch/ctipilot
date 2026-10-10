---
schema: 1
kind: threat
title: "AudiA6 ransomware crypto-laundering service dismantled — two charged, Switzerland among the participating countries"
headline: "AudiA6 ransomware crypto-laundering service dismantled — two charged, Switzerland among the participating countries"
summary: "AudiA6, a major ransomware crypto-laundering service, dismantled in a US/Europol operation with Swiss participation; two operators charged over ~$389 M in laundered Bitcoin (US Secret Service, 2026-06-11)."
discovered_at: "2026-06-12T05:00:00Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: high
immediate_action: null
tags:
  - law-enforcement
  - ransomware
  - cryptocrime
  - organized-crime
regions:
  - europe
  - switzerland
  - us
sectors: []
entities: []
cves: []
sources:
  - url: "https://www.secretservice.gov/newsroom/releases/2026/06/two-charged-connection-cryptocurrency-money-laundering-service-allegedly"
    publisher: US Secret Service
    role: primary
  - url: "https://www.europol.europa.eu/media-press/newsroom/news/ransomware-gangs-cut-eur-336-million-audia6-crypto-laundering-pipeline"
    publisher: Europol
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/legal/authorities-dismantle-audia6-ransomware-crypto-laundering-service/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-12.md
---

A coordinated operation led by the US Secret Service, IRS-CI, Europol and Eurojust — with participation from Australia, Canada, France, Georgia, Germany, Iceland, Japan, Poland, **Switzerland** and the United Kingdom — dismantled AudiA6 on 11 June, a crypto-laundering service trusted by ransomware operations since 2021 ([US Secret Service, 2026-06-11](https://www.secretservice.gov/newsroom/releases/2026/06/two-charged-connection-cryptocurrency-money-laundering-service-allegedly)). Two men resident in Batumi, Georgia — Ruslan Igorevich Tkachuk (37) and Alexander Vladimirovich Ledenev (25) — were arrested and charged in the Eastern District of Pennsylvania with conspiracy to launder monetary instruments and sting money laundering. Blockchain analysis traced roughly 10,333 BTC (~$389.7 M at transaction-time value) through AudiA6 wallets, with ~393 BTC directly attributable to darknet markets, ransomware crews and cybercrime services; the service charged 3–10 % commission and returned "cleaned" funds within about an hour through chains of fraudulent exchange accounts opened with stolen identities. Europol links AudiA6 to more than 15 international cybercrime investigations and reports infrastructure seizures in the US, Iceland, Germany and France, alongside the seizure of the Dark2Web forum where the service advertised ([Europol, 2026-06-11](https://www.europol.europa.eu/media-press/newsroom/news/ransomware-gangs-cut-eur-336-million-audia6-crypto-laundering-pipeline)).

**Why it matters to us:** the takedown removes a monetisation layer used by ransomware groups that target EU and Swiss organisations, and seized transaction records may retrospectively attribute earlier ransom payments — IR teams with open extortion cases should watch for law-enforcement follow-up requests.
