---
schema: 1
kind: incident
title: "One compromised contract-logistics processor put ten organisations into breach notification at once — CEVA Logistics, eight European warehouses, and a bank, a retailer and a games platform all learning from their supplier"
headline: "Ten organisations filed Dutch breach reports over one logistics provider's order-processing intrusion"
summary: >
  CEVA Logistics, the contract-logistics arm of CMA CGM, told affected customers on 1 August 2026 that a cyber
  intrusion was affecting part of its European contract-logistics operations, scoping the operational impact to eight
  warehouses. Because CEVA processes fulfilment data on behalf of unrelated clients, the Dutch data-protection
  authority has received breach reports from ten organisations over this one incident. Named downstream parties whose
  customers' shipping data was affected include ING, bol.com, De Bijenkorf, AFC Ajax, Ace & Tate and Valve, whose
  Steam hardware buyers had shipping records held by CEVA for 90 days. bol.com states two order-processing
  systems at one fulfilment centre were involved and that customer data may have been viewed or copied; no source
  names an initial-access vector, a malware family or an actor, CEVA has published no statement of its own, and its
  spokesperson declined to say whether any ransom demand was received.
discovered_at: "2026-08-11T04:50:00Z"
event_date: "2026-08-10"
run_id: 2026-08-11T0411Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain]
regions: [europe]
sectors: [finance, retail, transport, technology]
entities: [incident:ceva-logistics-fulfilment-breach-2026-08]
techniques: [T1005]
affected_products: []
cves: []
sources:
  - url: "https://partnerplatform.bol.com/en/nadp/security-incident-logistics-partner-of-bol"
    publisher: "bol.com"
    date: "2026-08-06"
    role: primary
  - url: "https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/"
    publisher: "TechCrunch"
    date: "2026-08-10"
    role: corroborating
  - url: "https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/"
    publisher: "ICTMagazine.nl"
    date: "2026-08-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The incident involves two systems used for processing orders from one of bol's fulfilment centers. No bol systems were affected. However, data of customers whose orders were processed via this location may have been viewed or copied."
    publisher: "bol.com"
  - quote: "Mark Schenkel, a spokesperson for the Dutch data protection authority, told TechCrunch that the agency has received data breach reports from 10 organizations in relation to the incident."
    publisher: "TechCrunch"
  - quote: "such as if the company knows how much personal data was taken, or if Ceva has received any communication from the hackers, such as a ransom demand"
    publisher: "TechCrunch"
verification: multi-source
sourcing_note: >
  CEVA has issued no public statement of its own; the fullest account of its position is the statement it provided to
  TechCrunch. bol.com's notice is a first-party disclosure about its own customers' data only, and it is the only
  party confirmed to have filed with the Dutch authority — no source identifies which ten organisations filed. Dutch
  reporting records data taken from CEVA being offered for sale on a criminal forum, which CEVA disputes, attributing
  that dataset to an earlier 2025 breach; this entry reports the dispute and adopts neither position. No source states
  an initial-access vector, malware family or actor, so this entry maps no access technique.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

CEVA Logistics — a contract-logistics operator that has been part of the French shipping group CMA CGM since 2019 ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)) — confirmed to affected customers on 1 August 2026 that a cyber intrusion was affecting part of its European contract-logistics operations, telling TechCrunch that its security teams activated protocols and opened an investigation that is still running, and that the operational impact was limited to eight warehouses, with no other CEVA systems globally affected ([TechCrunch, 2026-08-10](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)). That is the whole of what the compromised party has said publicly. Dutch trade reporting records that CEVA itself has given no public reaction of its own to these incidents ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)), and its spokesperson declined to answer whether the company knows how much personal data was taken or whether it has heard from the intruders at all, including on a ransom demand ([TechCrunch, 2026-08-10](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)).

The reason this is an entry rather than one more breach is arithmetic. CEVA processes fulfilment and shipping data for many unrelated clients, so one intrusion at one processor created independent notification duties at each of them simultaneously: the Dutch data-protection authority's spokesperson confirmed to TechCrunch that it has received breach reports from ten organisations in relation to this single incident. The named downstream parties span sectors that share nothing but a logistics contract — ING in banking, bol.com and De Bijenkorf in retail, the football club AFC Ajax, the eyewear retailer Ace & Tate, and Valve, which told customers it learned on 7 August that data was taken from CEVA's systems and alerted customers who had recently bought its Steam hardware, noting CEVA holds their shipping and delivery information for 90 days after an order ([TechCrunch, 2026-08-10](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)); Dutch trade reporting scopes those Steam buyers to Europe ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)).

bol.com's own notice is the most specific account any party has published. It records that it was informed on 1 August, that the incident involves two systems used for processing orders from one of its fulfilment centres, that no bol systems were affected, and that data of customers whose orders were processed via that location may have been viewed or copied ([bol.com, 2026-08-06](https://partnerplatform.bol.com/en/nadp/security-incident-logistics-partner-of-bol)). It also records the containment sequence — the logistics partner moved to stop the unauthorised access and brought in external specialists, and bol proactively halted data exchange with it pending assurance that resuming is safe — and the part that is easy to miss in a data-breach framing: the affected location's stock was taken offline, goods could not be received there, and orders were cancelled or delayed while restoration ran longer than expected. This was an availability incident for the downstream businesses as well as a confidentiality one. Dutch trade reporting adds that CEVA isolated and took the affected systems offline, opened an external investigation and informed regulators ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)).

Two things are conspicuously absent and should stay that way in any internal write-up. No source identifies how CEVA's order-processing systems were reached — no vulnerability, no phishing, no credential theft, no malware family, no actor or extortion brand. And the provenance of data already circulating is disputed: Dutch reporting records that data taken from CEVA is being offered for sale on a criminal forum, while CEVA maintains that dataset is old data from an earlier 2025 breach ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)). Treating the material on offer as this incident's proceeds is therefore not supported, and neither is the converse — no independent party has adjudicated the dispute.

**Defender takeaway:** the transferable lesson is about notification latency and inventory, not about CEVA. Every downstream organisation here learned about its own reportable breach from a supplier, and the intervals were uneven — bol was told on 1 August, Valve found out on 7 August, six days later, and had to notify its own customers from a standing start. For a public-sector or critical-infrastructure body, the equivalent exposure is any shared processor handling personal data at arm's length: parcel and mail fulfilment, hardware provisioning and asset dispatch, print and mailing houses, back-office order processing. Two questions decide how well such an incident goes. Does the processor inventory record *which* categories of personal data, for which populations, sit with each provider — because that is what a notification decision needs on day one and what none of these organisations could answer without asking their supplier. And does the contract oblige notification to the controller within a defined, short window rather than "without undue delay", because the gap between the first and last party learning of this one was measured in days while the regulatory clock ran for all of them. Note also that early customer-facing notices from affected retailers warned about a security incident at an external logistics partner rather than naming CEVA ([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/)), so an organisation that monitors for supplier incidents by watching for its suppliers' names in the press would not reliably have caught this one from the downstream disclosures.
