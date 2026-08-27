---
schema: 1
kind: policy
horizon: strategic
title: >
  The European Commission published its first official Cyber Resilience Act application guidance
  six weeks before the regulation's reporting obligations begin — clarifying which products are in
  scope, including remote data processing and free and open-source software
headline: >
  Commission issues first CRA application guidance, six weeks before the CRA reporting obligations
  start
summary: >
  On 2026-07-27 the European Commission published its first official practical guidance on
  applying the Cyber Resilience Act, as Communication C(2026) 5252 with a detailed annex carrying
  67 worked examples. The guidance is non-binding but is the Commission's authoritative
  interpretive position on the questions vendors and public-sector procurement teams have been
  raising: which products fall in scope — remote data processing solutions and free and
  open-source software among them — what constitutes a substantial modification that restarts
  conformity obligations, how support periods should be determined, and how the reporting
  obligations work in practice. It lands six weeks ahead of the CRA's first hard operational
  clock: the reporting obligations begin on 2026-09-11, more than a year before the regulation's
  principal obligations apply on 2027-12-11. For this constituency the effect is on the supplier
  tail, not on the SOC.
discovered_at: "2026-08-02T23:59:30Z"
updated_at: "2026-08-16T23:59:00Z"
event_date: 2026-07-27
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - supply-chain
  - eu-nexus
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - technology
  - energy
  - water
  - transport
  - healthcare
  - finance
  - telco
entities:
  - "policy:eu-cyber-resilience-act"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation"
    publisher: "European Commission — Shaping Europe's Digital Future"
    date: 2026-07-27
    role: primary
  - url: "https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act"
    publisher: Hunton Andrews Kurth
    date: 2026-07-29
    role: corroborating
  - url: "https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/"
    publisher: ETSI
    date: 2026-08-13
    role: primary
  - url: "https://docbox.etsi.org/CYBER/EUSR/Open"
    publisher: ETSI — TC CYBER-EUSR open document store
    date: 2026-08-13
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/08/14/etsi-cyber-resilience-act-standards/"
    publisher: Help Net Security
    date: 2026-08-14
    role: corroborating
closed_sources: []
evidence:
  - quote: "Clarifying when certain products fall within the scope of the Cyber Resilience Act, including remote data processing solutions and free and open source software"
    publisher: European Commission
  - quote: "Particular attention has been paid to microenterprises and SMEs, with 67 practical examples, a range of use cases, flowcharts and graphs"
    publisher: European Commission
  - quote: "Although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026."
    publisher: Hunton Andrews Kurth
  - quote: ETSI is pleased to announce the availability of the 17 vertical final draft standards developed in the framework of the EU Cyber Resilience Act (CRA) and currently under Public Enquiry.
    publisher: ETSI
  - quote: "The approval procedure will run until mid-September to mid-November 2026, depending on the vertical."
    publisher: ETSI
  - quote: "The Cyber Resilience Act lays down what manufacturers, and the market need to achieve, but it does not tell you how."
    publisher: "Sandra Feliciano, Chair of TC CYBER-EUSR, quoted by ETSI"
verification: multi-source
sourcing_note: >
  The scope clarifications and the SME framing are quoted from the Commission's own publication
  page; the split between the September 2026 reporting duty and the December 2027 principal
  obligations is cited to the corroborating legal analysis that states both dates together. The
  Commission communication C(2026) 5252 and its annex are reachable from that page only through
  newsroom redirection-tracked document links rather than stable direct URLs, so the citable
  source is the Commission library entry. This entry deliberately does NOT state the 24-hour
  actively-exploited-vulnerability notification window or cite the CRA article number: neither
  cited source carries either, and prior weeklies' record of that detail is not a source fetched
  by this run. What is stated is what the sources state — that reporting obligations begin
  2026-09-11 and the principal obligations on 2027-12-11.
confidence: high
references: []
weekly_section: weekly-policy
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-16T23:59:00Z"
    run_id: 2026-08-16T2315Z-weekly
    type: update
    summary: >
      On 13 August 2026 ETSI announced the availability of 17 vertical final draft standards developed
      under the EU Cyber Resilience Act and currently under Public Enquiry, submitted this summer to
      41 member organisations across Europe including the national standardisation bodies of the
      European Economic Area. These are the standards intended to become Harmonised Standards, which
      is what would give manufacturers the CRA's presumption of conformity. The product categories are
      directly relevant to public-sector procurement — the EN 304 series covers browsers, password
      managers, antivirus, VPNs, network management systems, SIEM, boot managers, PKI
      certificate-issuance software, network interfaces, operating systems, routers and switches,
      virtualization and container platforms, firewalls, and four consumer and IoT categories. ETSI
      states the approval procedure runs until mid-September to mid-November 2026 depending on the
      vertical, which places completion at or after the CRA's first hard operational clock: the
      reporting obligations that begin on 11 September 2026. Until then the presumption-of-conformity
      route is unavailable and manufacturers demonstrate compliance by other means.
    fields:
      - evidence
      - sectors
      - sources
      - body
    merged_from: 2026-08-16/weekly-w33-etsi-cra-harmonised-standards-approval
migrated_from: null
---

The Cyber Resilience Act's first operational deadline has been on defenders' calendars for months without an authoritative account of who it applies to. The Commission published one on 2026-07-27, as Communication C(2026) 5252 with an annex, and the parts that resolve real ambiguity are the scope boundaries: the guidance covers "clarifying when certain products fall within the scope of the Cyber Resilience Act, including remote data processing solutions and free and open source software" ([European Commission, 2026-07-27](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)). Those two categories are exactly where suppliers have been arguing they fall outside the regulation — a hosted component with a device-side client, and an open-source dependency with no commercial vendor behind it. The document is built for practical application rather than legal argument, with "particular attention has been paid to microenterprises and SMEs, with 67 practical examples, a range of use cases, flowcharts and graphs" ([European Commission, 2026-07-27](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)). It also addresses what counts as a substantial modification — the change that restarts conformity obligations — and how support-period duration should be determined.

The timing is the point. Legal analysis of the guidance sets out the sequence plainly: "although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026." ([Hunton Andrews Kurth, 2026-07-29](https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act)). So the first thing the CRA actually requires of manufacturers is incident and vulnerability reporting, and it starts in roughly six weeks, more than a year before the bulk of the regulation binds. Guidance clarifying scope arriving now is guidance about who has to stand up a reporting capability before mid-September.

For a Swiss federal SOC the CRA creates no direct obligation, and the honest framing of its relevance is indirect but real. It runs through the supplier tail: EU-market suppliers of connected products to Swiss and European public-sector and critical-infrastructure customers are the regulated parties, and the scope clarifications determine which of them are inside the reporting regime. Two consequences are worth tracking rather than acting on. First, a supplier newly understanding itself to be in scope — particularly one shipping a remote data processing solution it had assumed was a service rather than a product — will be standing up an incident-reporting process on a six-week timeline, which is a period in which disclosure behaviour tends to be inconsistent. Second, the substantial-modification clarification bears on when a supplier's own update and patch practice re-triggers conformity assessment, which is a plausible source of future friction between a customer wanting a fix quickly and a vendor facing a re-assessment to ship it.

**Defender takeaway:** this is a procurement and vendor-management input rather than a detection or response one, and it should be routed accordingly rather than absorbed into a security backlog. The concrete use is in supplier assurance: for connected products bought from EU-market manufacturers, the guidance is now the reference for asking whether a given supplier considers itself in scope and what its notification path will be after 11 September. The scope clarifications on remote data processing and open-source components are the two places where a supplier's answer is most likely to differ from the buyer's assumption, and therefore the two worth asking about explicitly.

## Update — 2026-08-16T23:59:00Z

A prior weekly recorded the European Commission publishing its first official Cyber Resilience Act application guidance — the interpretive half of the problem, answering which products are in scope and what counts as a substantial modification. This week supplies a delta on the other half, the technical route to demonstrating compliance, and it comes with a timetable worth noting.

On 13 August ETSI announced "the availability of the 17 vertical final draft standards developed in the framework of the EU Cyber Resilience Act (CRA) and currently under Public Enquiry", submitted this summer to 41 member organisations across Europe including the national standardisation bodies of the European Economic Area. The purpose is stated plainly: these standards "aim to become Harmonised Standards, giving manufacturers a recognised way to demonstrate compliance with the legislation, the so-called 'presumption of conformity'". The chair of the responsible technical committee frames the gap they fill in a sentence that also explains why their absence matters — "The Cyber Resilience Act lays down what manufacturers, and the market need to achieve, but it does not tell you how" ([ETSI, 2026-08-13](https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/)), reported independently the following day ([Help Net Security, 2026-08-14](https://www.helpnetsecurity.com/2026/08/14/etsi-cyber-resilience-act-standards/)).

The EN 304 series categories are not consumer-peripheral, which is what makes this a procurement item rather than a compliance-desk one. Alongside browsers, password managers, antivirus software, smart-home virtual assistants, smart-home security products, connected toys and wearables, the drafts cover VPNs, network management systems, SIEM, boot managers, PKI certificate-issuance software, network interfaces, operating systems, routers, modems and switches, virtualization and container platforms, and firewalls — most of a public-sector security stack ([ETSI TC CYBER-EUSR open document store, 2026-08-13](https://docbox.etsi.org/CYBER/EUSR/Open)). The press release itself names only the consumer-facing subset; the full vertical list comes from the draft filenames in ETSI's own open document store, which the release links. The timing is the constraint: ETSI states "The approval procedure will run until mid-September to mid-November 2026, depending on the vertical", and that window opens at or after the CRA's first hard operational date, the reporting obligations beginning on 11 September 2026 that this pipeline already tracks. So for the coming months there is no harmonised standard a supplier can point to, and conformity has to be demonstrated against the regulation's essential requirements directly, or through third-party conformity assessment for the critical categories.

**Defender takeaway:** the practical consequence sits with procurement and vendor management rather than the SOC, and it is a small, dateable one. A supplier answering a CRA question in the next quarter cannot cite a harmonised standard, because none exists yet in these categories — so a procurement requirement written as "demonstrate conformity with the applicable harmonised standard" is unanswerable today and will become answerable at different times for different product types, somewhere between mid-September and mid-November at the earliest, and only after ratification and citation steps that follow the enquiry. Two things are worth doing with that. First, for anything being specified now in the covered categories — firewalls, VPN gateways, SIEM, PKI issuance software, network management — the draft standard for that vertical is public and is a usable statement of what the essential requirements will mean in practice, which is more concrete than the regulation text and available a year before the CRA's principal obligations apply on 11 December 2027. Second, the 11 September reporting obligation arrives regardless of standards progress, so a supplier's readiness to report actively exploited vulnerabilities and severe incidents is a separate question from its conformity evidence and should be asked separately.
