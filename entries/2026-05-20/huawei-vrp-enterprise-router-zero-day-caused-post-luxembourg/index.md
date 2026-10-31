---
schema: 1
kind: threat
title: "Previously unknown flaw in Huawei enterprise router software caused POST Luxembourg's nationwide telecom outage of July 2025; no CVE ten months later"
headline: "Crafted traffic exploiting an undisclosed Huawei router flaw took down POST Luxembourg's network for three hours"
summary: >
  Recorded Future News reported on 2026-05-19 that an attack exploiting a previously unknown
  vulnerability in Huawei enterprise router software caused POST Luxembourg's nationwide outage of
  23 July 2025, which cut mobile, landline and emergency communications for more than three hours.
  Specially crafted traffic relayed through POST's network sent the routers into a continuous restart
  loop; investigators found no evidence that POST was the chosen target, and no CVE or public warning had
  been issued ten months later.
discovered_at: "2026-05-20T05:00:05Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - dos
regions:
  - europe
sectors:
  - telco
  - public-sector
entities:
  - "incident:huawei-vrp-enterprise-router-zero-day-post-luxembourg-2025-o"
techniques: [T1499.004]
cves: []
sources:
  - url: "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage"
    publisher: "The Record"
    date: "2026-05-19"
    role: primary
  - url: "https://securityaffairs.com/192431/hacking/alleged-huawei-zero-day-blamed-for-the-2025-luxembourg-telecom-crash.html"
    publisher: "Security Affairs"
    date: "2026-05-20"
    role: corroborating
  - url: "https://en.paperjam.lu/article/huawei-at-the-heart-of-the-post-outage-though-not-necessarily-the-target"
    publisher: "Paperjam"
    date: "2026-05-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An attack exploiting a previously unknown vulnerability in Huawei enterprise router software caused a nationwide telecoms outage in Luxembourg last year, according to multiple sources briefed on the matter, disrupting mobile, landline and emergency communications for more than three hours."
    publisher: "The Record"
    source_url: "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage"
  - quote: "It was caused by specially crafted network traffic that sent Huawei enterprise routers into a continuous restart loop, crashing critical parts of POST’s infrastructure."
    publisher: "The Record"
    source_url: "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage"
  - quote: "no evidence that an attack was specifically directed at POST Luxembourg as a chosen target"
    publisher: "The Record"
    source_url: "https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage"
verification: single-source
sourcing_note: >
  The Record is the original reporting, quoting POST Luxembourg, the public prosecutor and the High
  Commission for National Protection on record and anonymous sources for the zero-day label; Security
  Affairs and Paperjam restate it, and Huawei did not respond.
confidence: high
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
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-10-21T16:08:00Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The flaw behind POST Luxembourg's July 2025 outage is a previously unknown vulnerability in Huawei
      enterprise router software; no source names the VRP operating system, which The Record mentions only
      for unrelated earlier flaws. The no-target finding came from the High Commission for National
      Protection, not prosecutors, the zero-day label rests on anonymous sources, and no source attributes
      the attack to a state.
    fields: [body, classification, entities, evidence, headline, sources, sourcing_note, summary, tags, techniques, title]
---

An attack exploiting a previously unknown vulnerability in Huawei enterprise router software caused POST Luxembourg's nationwide outage on 23 July 2025, according to multiple sources briefed on the matter, disrupting mobile, landline and emergency communications for more than three hours ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)). POST's head of communications Paul Rausch called it a denial-of-service attack on a network device that exploited "a non-public, non-documented behaviour, for which no patch was available at the time", and anonymous sources described it as a zero-day attack ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)). Specially crafted network traffic sent the Huawei enterprise routers into a continuous restart loop: the public prosecutor said corrupted data relayed through POST in its role as internet service provider made its systems stop and reboot instead of relaying it, and a spokesperson for the High Commission for National Protection said investigators found "no evidence that an attack was specifically directed at POST Luxembourg as a chosen target" ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)). POST said neither of the earlier, publicly disclosed denial-of-service flaws in Huawei's VRP operating system was involved, Huawei told POST it had never seen the attack among its customers, and no CVE or public warning has been issued ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)).

**Exposure:** operators running Huawei enterprise routers; it remains unclear whether the flaw was ever fully patched or whether similar Huawei systems remain vulnerable, and Huawei publishes enterprise advisories only through a restricted customer portal ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)).

**Detection:** network device health and availability telemetry: the failure was routers repeatedly stopping and rebooting on transit traffic they should have forwarded, and POST clarified that it was not a volumetric DDoS ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)).

**Defender takeaway:** with no CVE or public advisory to patch against, an operator of Huawei enterprise routers has to ask Huawei, through the restricted customer portal or its account team, whether its router software carries a fix for the Luxembourg failure ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)); without Huawei routers in the network there is no decision to make.

## Correction — 2026-10-21T16:08:00Z

The sources do not name Huawei's VRP operating system as the vulnerable software: The Record reports a previously unknown vulnerability in Huawei enterprise router software and mentions VRP only for earlier denial-of-service flaws that POST says were not involved ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)). The finding that no attack was specifically directed at POST came from a spokesperson for Luxembourg's High Commission for National Protection, not from prosecutors, and the zero-day label rests on anonymous sources; no source attributes the attack to a state actor ([The Record, 2026-05-19](https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage)).
