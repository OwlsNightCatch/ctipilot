---
schema: 1
kind: threat
title: "Suspected Dream Market main administrator \"Speedstepper\" arrested in Germany; US indictment traces reactivated marketplace wallets and gold purchases"
headline: "Suspected Dream Market administrator \"Speedstepper\" arrested in Germany; US prosecutors allege he reactivated dormant wallets"
summary: "Owe Martin Andresen, 49, whom a US indictment accuses of being the main administrator of the Dream Market darknet marketplace that shut down in 2019, was arrested on German money-laundering charges on 2026-05-07 in a coordinated German and US operation announced on 2026-05-13. US prosecutors allege he moved the marketplace's dormant commission wallets into new consolidated wallets in late 2022 and laundered over $2 million between August 2023 and April 2025, partly by buying gold bars shipped to his home in Germany."
discovered_at: "2026-05-16T05:00:03Z"
event_date: 2026-05-13
run_id: 2026-05-16-5bc123a0
priority: routine
immediate_action: null
tags:
  - law-enforcement
  - cryptocrime
  - organized-crime
regions:
  - europe
  - dach
  - us
sectors: []
entities:
  - "incident:dream-market-admin-arrest-2026-05"
techniques: [T1597.002]
cves: []
sources:
  - url: "https://therecord.media/dream-market-admin-arrested-in-germany"
    publisher: "The Record"
    date: "2026-05-13"
    role: primary
  - url: "https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet"
    publisher: "US DEA"
    date: "2026-05-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On May 7, 2026, in a coordinated effort by both German and U.S. law enforcement, Andresen was arrested on German charges, and his residence and two other locations were searched."
    publisher: US DEA
    source_url: "https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet"
  - quote: "Law enforcement also located information identifying several bank accounts and cryptocurrency wallets containing approximately $1.2 million of funds believed to be proceeds of the Dream Market."
    publisher: US DEA
    source_url: "https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet"
  - quote: "An indictment unsealed this week by the DOJ accused Andresen of being the main administrator of Dream Market."
    publisher: The Record
    source_url: "https://therecord.media/dream-market-admin-arrested-in-germany"
verification: multi-source
sourcing_note: >
  The DEA release, published in the same words by IRS-CI, is the prosecuting side's account of its own indictment, and The Record reports from it and from the court documents;
  every statement about wallets, purchases and amounts is an allegation not yet proven in court.
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
actions: []
migrated_from: briefs/2026-05-16.md
updates:
  - at: "2026-10-21T16:04:38Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The suspected Dream Market main administrator was arrested in Germany on German money-laundering
      charges in a coordinated German and US effort, with IRS-CI and DEA Miami investigating and the BKA
      Cybercrime Unit and ZKI Oldenburg assisting; the FBI, USPIS and HSI belonged to the 2016-2022 task
      force. Only the US indictment ties him to the administrator role, the 2022 transfers went into new
      consolidated wallets, and the searches located about $1.2 million in identified accounts and wallets
      rather than seizing that sum in cryptocurrency.
    fields: [body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, title, sectors, techniques, priority]
---

On 2026-05-07, in a coordinated effort by German and US law enforcement, Owe Martin Andresen, 49, was arrested in Germany on German charges, and his residence and two other locations were searched ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). A US federal grand jury had indicted him on 2026-01-13 on six counts of international concealment money laundering and six counts of concealment money laundering, each carrying up to 20 years, and Germany has charged him with several counts of concealment money laundering, each punishable by up to five years ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). The DOJ indictment, unsealed in the week The Record reported it, accuses him of being the main administrator of Dream Market, a darknet marketplace launched in 2013 that announced its shutdown in 2019 ([The Record, 2026-05-13](https://therecord.media/dream-market-admin-arrested-in-germany)); the release calls him the suspected main administrator, the role whose holder used the moniker "Speedstepper" and was not identified in the earlier prosecutions ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). The case is investigated by the IRS-CI Cyber Crimes Unit and the DEA Miami Counternarcotic Cyber Investigations Task Force with substantial assistance from the Bundeskriminalamt Cybercrime Unit and the Zentrale Kriminalinspektion Oldenburg; the FBI, USPIS and HSI were part of the task force that investigated the marketplace between 2016 and 2022, whose prosecutions convicted the administrators "Oxymonster" and "KITT3N" in the US and the mid-level administrator "GOWRON" in the UK ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)).

Prosecutors allege that in November and December 2022 Andresen moved funds from the marketplace's dormant commission wallets into new consolidated wallets, activity that could only have been initiated by someone holding Dream Market's original private keys, and that in August 2023 he used an Atlanta-based cryptocurrency service provider to buy gold bars that were shipped to his home address in Germany; in total he is alleged to have laundered over $2 million between August 2023 and April 2025 ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). The US Attorney says the commissions came from selling illegal drugs, stolen personally identifiable information, counterfeit identification documents and other items ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). US agencies had kept watching the marketplace's wallets after the shutdown and found them untouched until then ([The Record, 2026-05-13](https://therecord.media/dream-market-admin-arrested-in-germany)). The searches located about $1.7 million of gold bars and over $23,000 in cash, along with information identifying bank accounts and cryptocurrency wallets holding about $1.2 million believed to be Dream Market proceeds ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)).

**Defender takeaway:** no change for enterprise defenders, since the sources describe the laundering of marketplace proceeds and no intrusion technique. For financial-crime and cryptocurrency-tracing teams the case shows that wallets left untouched for three years stayed under watch, and IRS-CI draws the lesson that "illicit actors may hide in the shadows, but their financial footprints remain" ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)).

## Correction — 2026-10-21T16:04:38Z

The arrest on 2026-05-07 was a coordinated German and US effort on German charges rather than a BKA arrest: the case is investigated by the IRS-CI Cyber Crimes Unit and DEA Miami with substantial assistance from the Bundeskriminalamt Cybercrime Unit and the Zentrale Kriminalinspektion Oldenburg, while the FBI, USPIS and HSI belonged to the task force that investigated the marketplace from 2016 to 2022 ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). Only the US indictment accuses Andresen of being the main administrator; the German charges are concealment money laundering ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet); [The Record, 2026-05-13](https://therecord.media/dream-market-admin-arrested-in-germany)). The 2022 transfers went into new consolidated wallets, not a single wallet, and the searches located about $1.7 million of gold bars and over $23,000 in cash and identified bank accounts and wallets holding about $1.2 million, rather than seizing $1.2 million in cryptocurrency ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). The marketplace commissions behind the laundering came, the US Attorney says, from selling illegal drugs, stolen personally identifiable information, counterfeit identification documents and other items ([US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)).
