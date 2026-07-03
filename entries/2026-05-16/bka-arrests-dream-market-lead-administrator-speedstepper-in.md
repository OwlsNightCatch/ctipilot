---
schema: 1
kind: threat
horizon: operational
title: "BKA arrests Dream Market lead administrator \"Speedstepper\" in Germany — cryptocurrency-to-physical-gold OPSEC failure after seven years at large"
headline: "BKA arrests Dream Market lead administrator \"Speedstepper\" in Germany — cryptocurrency-to-physical-gold OPSEC failure after seven years at large"
summary: "Owe Martin Andresen, a 49-year-old German national alleged by US and German prosecutors to be \"Speedstepper\" — the lead administrator of the Dream Market darknet narcotics marketplace from 2013 until its 2019 voluntary shutdown — was arrested in Germany on 2026-05-07 and publicly identified on 2026-05-13–14 (The …"
discovered_at: "2026-05-16T05:00:03Z"
event_date: 2026-05-14
run_id: 2026-05-16-5bc123a0
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - cryptocrime
  - organized-crime
regions:
  - europe
  - dach
  - us
sectors:
  - legal-services
entities: []
cves: []
sources:
  - url: "https://therecord.media/dream-market-admin-arrested-in-germany"
    publisher: "The Record, 2026-05-14"
    role: primary
  - url: "https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet"
    publisher: "US DEA, 2026-05-13"
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
migrated_from: briefs/2026-05-16.md
---

Owe Martin Andresen, a 49-year-old German national alleged by US and German prosecutors to be "Speedstepper" — the lead administrator of the Dream Market darknet narcotics marketplace from 2013 until its 2019 voluntary shutdown — was arrested in Germany on 2026-05-07 and publicly identified on 2026-05-13–14 ([The Record, 2026-05-14](https://therecord.media/dream-market-admin-arrested-in-germany) · [US DEA, 2026-05-13](https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet)). The action was a coordinated multi-agency operation: the Bundeskriminalamt and the Zentrale Kriminalinspektion Oldenburg for the German side, with the US DEA Miami, IRS-CI Cyber Crimes Unit, FBI, USPIS, and HSI executing in parallel. A US federal grand jury in the Northern District of Georgia had returned a sealed indictment on 2026-01-13 charging Andresen with six counts of international concealment money laundering and six counts of concealment money laundering (240 years aggregate maximum); German charges carry up to five years. The OPSEC failures that closed the seven-year gap were operational, not technical: in late 2022 Andresen allegedly accessed Dream Market's dormant cryptocurrency wallets — an action only the holder of the original private keys could perform — and consolidated the contents into a single wallet, providing prosecutors with a definitive on-chain link; and in August 2023 he used an Atlanta-based cryptocurrency-to-physical-asset service to purchase gold bars that were shipped directly to his home address in Germany, providing the geographic and identity link. At arrest, German authorities seized approximately USD 1.7 million in gold bars, USD 23,000 in cash, and approximately USD 1.2 million in cryptocurrency. Three Dream Market co-administrators ("Oxymonster", "KITT3N", "GOWRON") had been convicted previously. The case is operationally interesting to public-sector intelligence liaisons because it illustrates that long-tail attribution of darknet operators is increasingly driven by post-cessation financial behaviour — wallet reactivation, regulated-service touchpoints, physical-asset conversion — rather than on-platform OPSEC; the seven-year delay between the marketplace's closure and the arrest is the operational signal.
