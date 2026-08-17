---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "UPDATE — the Cyber Resilience Act's conformity route entered formal approval this week: ETSI put 17 draft product-category standards out for Public Enquiry, and the procedure runs past the regulation's first reporting deadline"
headline: "ETSI opens approval on 17 CRA standards covering firewalls, VPNs, SIEM and PKI software — none can be relied on before 11 September"
summary: >
  On 13 August 2026 ETSI announced the availability of 17 vertical final draft standards developed under the
  EU Cyber Resilience Act and currently under Public Enquiry, submitted this summer to 41 member
  organisations across Europe including the national standardisation bodies of the European Economic Area.
  These are the standards intended to become Harmonised Standards, which is what would give manufacturers
  the CRA's presumption of conformity. The product categories are directly relevant to public-sector
  procurement — the EN 304 series covers browsers, password managers, antivirus, VPNs, network management
  systems, SIEM, boot managers, PKI certificate-issuance software, network interfaces, operating systems,
  routers and switches, virtualization and container platforms, firewalls, and four consumer and IoT
  categories. ETSI states the approval procedure runs until mid-September to mid-November 2026 depending on
  the vertical, which places completion at or after the CRA's first hard operational clock: the reporting
  obligations that begin on 11 September 2026. Until then the presumption-of-conformity route is unavailable
  and manufacturers demonstrate compliance by other means.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-13"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [supply-chain, eu-nexus]
regions: [europe, switzerland]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities:
  - policy:eu-cyber-resilience-act
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/"
    publisher: "ETSI"
    date: "2026-08-13"
    role: primary
  - url: "https://docbox.etsi.org/CYBER/EUSR/Open"
    publisher: "ETSI — TC CYBER-EUSR open document store"
    date: "2026-08-13"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/08/14/etsi-cyber-resilience-act-standards/"
    publisher: "Help Net Security"
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "ETSI is pleased to announce the availability of the 17 vertical final draft standards developed in the framework of the EU Cyber Resilience Act (CRA) and currently under Public Enquiry."
    publisher: "ETSI"
  - quote: "The approval procedure will run until mid-September to mid-November 2026, depending on the vertical."
    publisher: "ETSI"
  - quote: "The Cyber Resilience Act lays down what manufacturers, and the market need to achieve, but it does not tell you how."
    publisher: "Sandra Feliciano, Chair of TC CYBER-EUSR, quoted by ETSI"
verification: multi-source
sourcing_note: >
  Carried on ETSI's own announcement as the standards body responsible for the process, corroborated by an
  independent trade outlet. The list of product categories is taken from ETSI's own open document store as
  surfaced during this run's research and is cited to it directly, because the press release names only
  password managers, anti-virus software, smart home assistants, connected toys and wearables; the
  completion timing is ETSI's own stated procedure window. Whether
  any standard is subsequently ratified and cited in the Official Journal is a further step this entry does
  not predict.
confidence: high
update_of: 2026-08-02/weekly-w31-commission-cra-application-guidance
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-02):** a prior weekly recorded the European Commission publishing its first official Cyber Resilience Act application guidance — the interpretive half of the problem, answering which products are in scope and what counts as a substantial modification. This week supplies a delta on the other half, the technical route to demonstrating compliance, and it comes with a timetable worth noting.

On 13 August ETSI announced "the availability of the 17 vertical final draft standards developed in the framework of the EU Cyber Resilience Act (CRA) and currently under Public Enquiry", submitted this summer to 41 member organisations across Europe including the national standardisation bodies of the European Economic Area. The purpose is stated plainly: these standards "aim to become Harmonised Standards, giving manufacturers a recognised way to demonstrate compliance with the legislation, the so-called 'presumption of conformity'". The chair of the responsible technical committee frames the gap they fill in a sentence that also explains why their absence matters — "The Cyber Resilience Act lays down what manufacturers, and the market need to achieve, but it does not tell you how" ([ETSI, 2026-08-13](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)), reported independently the following day ([Help Net Security, 2026-08-14](https://www.helpnetsecurity.com/2026/08/14/etsi-cyber-resilience-act-standards/)).

The EN 304 series categories are not consumer-peripheral, which is what makes this a procurement item rather than a compliance-desk one. Alongside browsers, password managers, antivirus software, smart-home virtual assistants, smart-home security products, connected toys and wearables, the drafts cover VPNs, network management systems, SIEM, boot managers, PKI certificate-issuance software, network interfaces, operating systems, routers, modems and switches, virtualization and container platforms, and firewalls — most of a public-sector security stack ([ETSI TC CYBER-EUSR open document store, 2026-08-13](https://docbox.etsi.org/CYBER/EUSR/Open)). The press release itself names only the consumer-facing subset; the full vertical list comes from the draft filenames in ETSI's own open document store, which the release links. The timing is the constraint: ETSI states "The approval procedure will run until mid-September to mid-November 2026, depending on the vertical", and that window opens at or after the CRA's first hard operational date, the reporting obligations beginning on 11 September 2026 that this pipeline already tracks. So for the coming months there is no harmonised standard a supplier can point to, and conformity has to be demonstrated against the regulation's essential requirements directly, or through third-party conformity assessment for the critical categories.

**Defender takeaway:** the practical consequence sits with procurement and vendor management rather than the SOC, and it is a small, dateable one. A supplier answering a CRA question in the next quarter cannot cite a harmonised standard, because none exists yet in these categories — so a procurement requirement written as "demonstrate conformity with the applicable harmonised standard" is unanswerable today and will become answerable at different times for different product types, somewhere between mid-September and mid-November at the earliest, and only after ratification and citation steps that follow the enquiry. Two things are worth doing with that. First, for anything being specified now in the covered categories — firewalls, VPN gateways, SIEM, PKI issuance software, network management — the draft standard for that vertical is public and is a usable statement of what the essential requirements will mean in practice, which is more concrete than the regulation text and available a year before the CRA's principal obligations apply on 11 December 2027. Second, the 11 September reporting obligation arrives regardless of standards progress, so a supplier's readiness to report actively exploited vulnerabilities and severe incidents is a separate question from its conformity evidence and should be asked separately.
