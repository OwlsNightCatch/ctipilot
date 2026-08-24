---
schema: 1
kind: annual-report
horizon: operational
title: "Check Point State of Ransomware Q2 2026: the active-group count reached 93 while the top ten's share of victims fell to 57.6% — and a leaked chat log shows a RaaS panel built with AI coding assistants in about three days"
headline: "The ecosystem's tail widened faster than its head shrank, which breaks any triage process that watches a top-ten list of leak sites"
summary: >
  Check Point Research published its quarterly ransomware report on 2026-08-13. The structural finding is
  fragmentation: the top ten groups accounted for 57.6% of leak-site victims, down from 71% in Q1, while the number of
  active groups rose from 71 to 93, a new high for the tracked period, with total victim volume essentially flat
  quarter-on-quarter. Qilin stayed the most prolific operator for a fourth consecutive quarter at 279 victims, but The
  Gentlemen grew 62% to 269 and outpaced it during June. An internal leak of The Gentlemen's own chat logs and platform
  data exposed a core team of roughly nine operators and confirmed the group used AI coding assistants to build its
  ransomware management panel in about three days — first-party evidence rather than vendor inference. Ransom-payment
  rates fell to a multi-year low near 23%.
discovered_at: "2026-08-14T05:08:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - ai-abuse
regions:
  - global
  - europe
sectors: []
entities:
  - report:check-point-state-of-ransomware-q2-2026
  - actor:qilin
  - actor:thegentlemen
techniques:
  - T1657
  - T1587.001
affected_products: []
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/"
    publisher: "Check Point Research"
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report."
    publisher: "Check Point Research"
  - quote: "Chat logs and platform data exposed a core team of roughly nine operators supported by a broader affiliate base, along with confirmation that the group used AI coding assistants to build its ransomware management panel in about three days, genuine first party evidence of AI accelerating malicious tooling development."
    publisher: "Check Point Research"
verification: single-source
sourcing_note: "Check Point Research is the sole source and the report is its own telemetry, so every figure here is one vendor's measurement of leak-site postings — a proxy for victimisation that counts what groups choose to publish, not what happened. Reported as Check Point's counts throughout."
confidence: medium
update_of: null
references: []
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

Check Point Research published its quarterly ransomware report on 2026-08-13. Its headline measurement is about the shape of the ecosystem rather than its size: ["The top 10 groups accounted for 57.6% of all victims, down from 71% in Q1, while the number of active groups climbed from 71 to 93, a new high for the period tracked in this report"](https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/), with leak-site victim counts essentially flat quarter-on-quarter. The same volume of harm is being produced by materially more groups, and Check Point's framing is that the leaders are still winning but the path to joining them has got much shorter.

**Why fragmentation is an operational problem, not a market observation.** A great deal of ransomware triage — leak-site monitoring, brand-based enrichment, playbooks keyed to a named group's known tradecraft — implicitly assumes that knowing the dominant operators covers most of what a defender will meet. At 93 active groups with the top ten accounting for barely more than half of victims, a watchlist of familiar brands now misses close to half the field, and the groups a defender has no playbook for are the fastest-growing part of it. The practical consequence for anyone whose queue ingests leak-site feeds is that an unrecognised brand name carries no inference of low capability, and that enrichment has to fall back on observed tradecraft rather than reputation. The report reinforces the point at the top of the table: Qilin remained the most prolific operator for a fourth straight quarter at 279 victims even as its own count fell 17%, while The Gentlemen — a group this pipeline first recorded as a self-propagating encryptor rather than a market leader — grew 62% to 269 victims and outpaced Qilin during June alone.

**The AI finding is first-party for once.** Claims that criminals are using AI to build tooling faster have generally rested on vendor inference from artefacts. Here the evidence is the group's own: ["Chat logs and platform data exposed a core team of roughly nine operators supported by a broader affiliate base, along with confirmation that the group used AI coding assistants to build its ransomware management panel in about three days, genuine first party evidence of AI accelerating malicious tooling development"](https://research.checkpoint.com/2026/the-state-of-ransomware-q2-2026/). What that supports is narrow and worth stating precisely: it evidences the *management panel* — affiliate-facing infrastructure — being assembled in days by a small team, not the encryptor or the intrusion tradecraft. Read alongside the ecosystem numbers it explains part of them: the operational overhead of standing up a ransomware-as-a-service brand has fallen, which is the mechanism behind a rising count of active groups at flat total volume.

**Two further figures with defender consequences.** Check Point records ransom-payment rates falling to a multi-year low near 23%, continuing a decline from 85% in 2019, while noting that the payer market is splitting — average payments rising while the median falls, which it reads as large enterprises continuing to pay heavily while the mid-market increasingly refuses. And the geographic distribution moved: the US share of victims fell from 50% to 42% quarter-on-quarter, which Check Point attributes largely to the quarter's fastest-growing groups targeting the US less often than the ecosystem average. For European exposure planning that is the line to watch — a shrinking US share at flat global volume means the remainder is landing elsewhere, and the groups driving the shift are the newer ones with the thinnest public tradecraft record.

**Defender takeaway:** the actionable content of this report is a scoping correction rather than a new threat. Group-name-driven detection and response coverage should be assumed incomplete by roughly half; extortion-response planning should assume the counterpart may be a group with no published negotiation history, no known affiliate discipline and no reputational stake in honouring an agreement, which is the practical risk in a fragmenting market. Per this pipeline's standing practice, this report is covered once and referenced thereafter rather than re-summarised.
