---
schema: 1
kind: incident
title: "The Gentlemen ransomware group lists Czech university VSFS and Swiss engineering firm DEVO-Tech AG on its leak site"
headline: "The Gentlemen claims a Czech private university and a Swiss engineering firm on its leak site on 2026-05-18"
summary: >
  The Gentlemen ransomware group claimed the University of Finance and Administration (VSFS) in the
  Czech Republic and the Swiss engineering firm DEVO-Tech AG on its leak site on 2026-05-18, threatening
  to publish stolen data unless the victims made contact or negotiated. The listings carry no technical
  detail; Check Point Research describes the group's usual entry as exposed VPN appliances and firewalls,
  chiefly Fortinet FortiGate and Cisco.
discovered_at: "2026-05-20T05:00:13Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: routine
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - europe
  - switzerland
sectors:
  - education
  - manufacturing
entities:
  - "actor:thegentlemen"
techniques: [T1657]
cves: []
sources:
  - url: "https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/"
    publisher: "DeXpose"
    date: "2026-05-19"
    role: primary
  - url: "https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/"
    publisher: "DeXpose"
    date: "2026-05-19"
    role: corroborating
  - url: "https://ransomware.live/id/REVWTy1UZWNoQHRoZWdlbnRsZW1lbg"
    publisher: "ransomware.live"
    date: "2026-05-18"
    role: corroborating
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: "Check Point Research"
    date: "2026-05-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The full leak will be published soon, unless a university representative contacts us via the channels provided."
    publisher: "DeXpose"
    source_url: "https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/"
  - quote: "The full leak will be published unless DEVO-Tech AG begins negotiations with us."
    publisher: "DeXpose"
    source_url: "https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/"
  - quote: "The group claims to usually gain initial access through exposed edge devices such as VPN appliances, firewalls, and other internet-facing systems, with a particular focus on platforms like Fortinet FortiGate and Cisco."
    publisher: "Check Point Research"
    source_url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
verification: single-source
sourcing_note: >
  The listings are the group's own leak-site claims, republished by DeXpose and ransomware.live, and the
  sources carry no victim or authority statement; the group profile comes from Check Point Research's
  analysis of the group's leaked internal chats.
confidence: medium
update_of: null
references:
  - 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-10-21T20:23:38Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The Gentlemen listed both VSFS and DEVO-Tech AG on 2026-05-18, and the listings carry no technical
      detail. The group profile comes from Check Point Research's analysis of 2026-05-13, which names
      exposed VPN appliances and firewalls, chiefly FortiGate and Cisco, as its usual entry rather than
      SD-WAN gateways; both listings remain unconfirmed leak-site claims.
    fields: [body, classification, confidence, entities, event_date, evidence, headline, priority, references, sources, sourcing_note, summary, tags, techniques, title, verification]
---

The Gentlemen ransomware group claimed the Czech private University of Finance and Administration (VSFS) and the Swiss engineering firm DEVO-Tech AG on its leak site on 2026-05-18, threatening to publish stolen data unless the victims made contact or negotiated ([DeXpose, 2026-05-19](https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/)) ([DeXpose, 2026-05-19](https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/)); DEVO-Tech is a family-owned engineering company from Ziefen ([ransomware.live, 2026-05-18](https://ransomware.live/id/REVWTy1UZWNoQHRoZWdlbnRsZW1lbg)). The listings carry no technical detail. Check Point Research's analysis of the group's leaked internal chats describes a locker written in Go and initial access mostly through exposed VPN appliances, firewalls and other edge devices, chiefly Fortinet FortiGate and Cisco, by brute-forcing credentials, exploiting known vulnerabilities or buying access ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

**Detection:** authentication logs on internet-facing VPN and firewall panels, where the group brute-forces credentials ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

**Defender takeaway:** the listings alone change no decision outside the two victims and their partners; the transferable point is the group's edge-device entry, which puts exposed FortiGate and Cisco VPN and firewall management interfaces at the top of the review ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)).

## Correction — 2026-10-21T20:23:38Z

Both victims were listed on 2026-05-18 ([DeXpose, 2026-05-19](https://www.dexpose.io/thegentlemen-target-university-of-finance-and-administration-in-czech-republic/)) ([DeXpose, 2026-05-19](https://www.dexpose.io/thegentlemen-ransomware-group-targets-swiss-engineering-firm-devo-tech-ag/)). The listings carry no technical detail, so nothing in them shows the group's methods unchanged; the group profile is Check Point Research's analysis of 2026-05-13, which names exposed VPN appliances and firewalls, chiefly FortiGate and Cisco, as the usual entry ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)), not SD-WAN gateways.
