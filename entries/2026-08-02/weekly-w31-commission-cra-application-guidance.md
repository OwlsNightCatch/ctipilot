---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "The European Commission published its first official Cyber Resilience Act application guidance six weeks before the regulation's reporting obligations begin — clarifying which products are in scope, including remote data processing and free and open-source software"
headline: "Commission issues first CRA application guidance, six weeks before the CRA reporting obligations start"
summary: >
  On 2026-07-27 the European Commission published its first official practical guidance on applying the Cyber
  Resilience Act, as Communication C(2026) 5252 with a detailed annex carrying 67 worked
  examples. The guidance is non-binding but is the Commission's authoritative interpretive position on
  the questions vendors and public-sector procurement teams have been raising: which products fall in scope —
  remote data processing solutions and free and open-source software among them — what constitutes a
  substantial modification that restarts conformity obligations, how support periods should be determined, and
  how the reporting obligations work in practice. It lands six weeks ahead of the CRA's first hard operational
  clock: the reporting obligations begin on 2026-09-11, more than a year before the regulation's principal
  obligations apply on 2027-12-11. For this constituency the effect is on the supplier tail, not on the SOC.
discovered_at: "2026-08-02T23:59:30Z"
event_date: "2026-07-27"
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, eu-nexus]
regions: [europe, switzerland]
sectors: [public-sector, technology]
entities:
  - policy:eu-cyber-resilience-act
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation"
    publisher: "European Commission — Shaping Europe's Digital Future"
    date: "2026-07-27"
    role: primary
  - url: "https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act"
    publisher: "Hunton Andrews Kurth"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Clarifying when certain products fall within the scope of the Cyber Resilience Act, including remote data processing solutions and free and open source software"
    publisher: "European Commission"
  - quote: "Particular attention has been paid to microenterprises and SMEs, with 67 practical examples, a range of use cases, flowcharts and graphs"
    publisher: "European Commission"
  - quote: "Although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026."
    publisher: "Hunton Andrews Kurth"
verification: multi-source
sourcing_note: >
  The scope clarifications and the SME framing are quoted from the Commission's own publication page; the
  split between the September 2026 reporting duty and the December 2027 principal obligations is cited to the
  corroborating legal analysis that states both dates together. The Commission communication C(2026) 5252 and
  its annex are reachable from that page only through newsroom redirection-tracked document links rather than
  stable direct URLs, so the citable source is the Commission library entry. This entry deliberately does NOT
  state the 24-hour actively-exploited-vulnerability notification window or cite the CRA article number:
  neither cited source carries either, and prior weeklies' record of that detail is not a source fetched by
  this run. What is stated is what the sources state — that reporting obligations begin 2026-09-11 and the
  principal obligations on 2027-12-11.
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
migrated_from: null
---

The Cyber Resilience Act's first operational deadline has been on defenders' calendars for months without an authoritative account of who it applies to. The Commission published one on 2026-07-27, as Communication C(2026) 5252 with an annex, and the parts that resolve real ambiguity are the scope boundaries: the guidance covers "clarifying when certain products fall within the scope of the Cyber Resilience Act, including remote data processing solutions and free and open source software" ([European Commission, 2026-07-27](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)). Those two categories are exactly where suppliers have been arguing they fall outside the regulation — a hosted component with a device-side client, and an open-source dependency with no commercial vendor behind it. The document is built for practical application rather than legal argument, with "particular attention has been paid to microenterprises and SMEs, with 67 practical examples, a range of use cases, flowcharts and graphs" ([European Commission, 2026-07-27](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)). It also addresses what counts as a substantial modification — the change that restarts conformity obligations — and how support-period duration should be determined.

The timing is the point. Legal analysis of the guidance sets out the sequence plainly: "although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026." ([Hunton Andrews Kurth, 2026-07-29](https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act)). So the first thing the CRA actually requires of manufacturers is incident and vulnerability reporting, and it starts in roughly six weeks, more than a year before the bulk of the regulation binds. Guidance clarifying scope arriving now is guidance about who has to stand up a reporting capability before mid-September.

For a Swiss federal SOC the CRA creates no direct obligation, and the honest framing of its relevance is indirect but real. It runs through the supplier tail: EU-market suppliers of connected products to Swiss and European public-sector and critical-infrastructure customers are the regulated parties, and the scope clarifications determine which of them are inside the reporting regime. Two consequences are worth tracking rather than acting on. First, a supplier newly understanding itself to be in scope — particularly one shipping a remote data processing solution it had assumed was a service rather than a product — will be standing up an incident-reporting process on a six-week timeline, which is a period in which disclosure behaviour tends to be inconsistent. Second, the substantial-modification clarification bears on when a supplier's own update and patch practice re-triggers conformity assessment, which is a plausible source of future friction between a customer wanting a fix quickly and a vendor facing a re-assessment to ship it.

**Defender takeaway:** this is a procurement and vendor-management input rather than a detection or response one, and it should be routed accordingly rather than absorbed into a security backlog. The concrete use is in supplier assurance: for connected products bought from EU-market manufacturers, the guidance is now the reference for asking whether a given supplier considers itself in scope and what its notification path will be after 11 September. The scope clarifications on remote data processing and open-source components are the two places where a supplier's answer is most likely to differ from the buyer's assumption, and therefore the two worth asking about explicitly.
