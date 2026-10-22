---
schema: 1
kind: incident
title: "BKA and ZIT shut down the relaunched Crimenetwork darknet marketplace; suspected German operator arrested in Mallorca on a European Arrest Warrant"
headline: "German police shut down the relaunched Crimenetwork marketplace; suspected operator arrested in Mallorca"
summary: "Germany's BKA and the Frankfurt prosecutors' cybercrime unit ZIT shut down the relaunched Crimenetwork darknet marketplace, and a Spanish National Police special unit arrested its suspected 35-year-old German operator in Mallorca on a European Arrest Warrant. The relaunch, built a few days after the December 2024 takedown, had more than 22,000 users and over 100 vendors and an estimated revenue of more than €3.6 million; about €194,000 in assets were preliminarily seized."
discovered_at: "2026-05-12T05:00:01Z"
event_date: 2026-05-08
run_id: 2026-05-12-cd1ab844
priority: routine
immediate_action: null
tags:
  - organized-crime
  - law-enforcement
  - cryptocrime
  - data-breach
regions:
  - dach
  - europe
sectors:
  - legal-services
  - public-sector
entities:
  - "incident:bka-crimenetwork-takedown-2026"
techniques: [T1597.002]
cves: []
sources:
  - url: "https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2026/Presse2026/260508_PM_Crimenetwork.html"
    publisher: "Bundeskriminalamt press release (\"Deutscher Betreiber von 'Crimenetwork' auf Mallorca verhaftet\", German operator of 'Crimenetwork' arrested in Mallorca)"
    date: "2026-05-08"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/"
    publisher: "Help Net Security"
    date: "2026-05-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A special unit of the Spanish National Police arrested the suspected 35-year-old German operator at his residence in Mallorca under a European Arrest Warrant."
    publisher: "Help Net Security"
    source_url: "https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/"
  - quote: "Authorities state the suspect allegedly created and operated a new technical infrastructure for Crimenetwork a few days after the previous version was shut down and its administrator was arrested in December 2024."
    publisher: "Help Net Security"
    source_url: "https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/"
  - quote: "User and transaction data obtained during the operation are expected to support further investigations into the platform’s users and operators, who are believed to be mainly located in German-speaking countries."
    publisher: "Help Net Security"
    source_url: "https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/"
verification: multi-source
sourcing_note: >
  The facts are the BKA's, as Help Net Security reports and quotes them from the BKA press release.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
updates:
  - at: "2026-10-21T20:39:01Z"
    run_id: 2026-10-21T1148Z-audit
    type: improvement
    summary: >
      A Spanish National Police special unit made the Mallorca arrest in the operation with the BKA and
      ZIT, and the relaunch was built a few days after the December 2024 takedown of one of the central
      German-speaking underground marketplaces. About €194,000 in assets were preliminarily seized, and
      the seized user and transaction data are expected to support further investigations into users and
      operators mainly in German-speaking countries; the takedown asks no defender decision.
    fields: [body, classification, confidence, entities, event_date, evidence, headline, priority, sources, sourcing_note, summary, title, techniques]
---

A special unit of the Spanish National Police arrested the suspected 35-year-old German operator of the relaunched Crimenetwork marketplace at his residence in Mallorca under a European Arrest Warrant, in an operation with Germany's Federal Criminal Police Office (BKA) and the Frankfurt am Main Public Prosecutor's Office's Central Office for Combating Internet Crime (ZIT); he is accused under Section 127 of the German Criminal Code of operating criminal trading platforms, and of narcotics trafficking ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)). Authorities say he built new infrastructure for Crimenetwork a few days after the previous version was shut down and its administrator arrested in December 2024; the BKA calls the marketplace one of the central marketplaces of the German-speaking underground economy for many years ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)). The relaunched platform offered stolen data, drugs, forged documents and other illegal services to more than 22,000 users and over 100 vendors, took payment in Bitcoin, Litecoin and Monero and earned an estimated more than €3.6 million in commissions and vendor fees; about €194,000 in assets were preliminarily seized ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)).

**Defender takeaway:** no defender decision follows; the seized user and transaction data are expected to support further investigations into the platform's users and operators, who are believed to be mainly in German-speaking countries ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)).

## Improvement — 2026-10-21T20:39:01Z

The arrest in Mallorca was made by a special unit of the Spanish National Police in the operation with the BKA and ZIT, and the BKA describes Crimenetwork as one of the central marketplaces of the German-speaking underground economy, relaunched a few days after its December 2024 takedown ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)). The only forward-looking statement in the reporting is that the seized user and transaction data are expected to support further investigations into the platform's users and operators, believed to be mainly in German-speaking countries ([Help Net Security, 2026-05-11](https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/)); it gives defenders no expected wave of leaked-credential checks and no change in how relaunched markets behave.
