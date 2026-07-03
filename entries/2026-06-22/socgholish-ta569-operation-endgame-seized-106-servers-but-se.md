---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "SocGholish / TA569 — Operation Endgame seized 106 servers, but seven delivery clusters remain operational"
headline: "SocGholish / TA569 — Operation Endgame seized 106 servers, but seven delivery clusters remain operational"
summary: "key: item:operation-endgame-expands-to-socgholish-ta569-106-c2-servers. The Operation Endgame takedown (§ 5) was the headline; Proofpoint's post-action analysis is the status update that matters for the longer arc."
discovered_at: "2026-06-22T00:15:05Z"
event_date: 2026-06-18
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - organized-crime
  - law-enforcement
  - supply-chain
regions:
  - europe
  - global
sectors:
  - technology
entities:
  - "campaign:operation-endgame-amadey-stealc"
  - "campaign:sekoia-errtraffic-clickfix-maas-polygon-c2"
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation"
    publisher: Proofpoint
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W25.md
---

`key: item:operation-endgame-expands-to-socgholish-ta569-106-c2-servers`. The Operation Endgame takedown (§ 5) was the headline; Proofpoint's post-action analysis is the status update that matters for the longer arc. TA569 served for years as a primary distribution layer for WastedLocker (Evil Corp), LockBit and RansomHub, and while law enforcement seized over 100 servers and 14,971 WordPress sites were remediated, **seven FakeUpdates-style clusters remain operational** — TA2726, TA2727, ZPHP, ErrTraffic (the ClickFix MaaS in § 6), LandUpdate808/KongTuke, GeoTDS and tdsshop ([Proofpoint, 2026-06-18](https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation); [daily 06-19](/briefs/2026-06-19/)). Proofpoint also notes WordPress sites frequently reinfect because the underlying credential compromise outlives CMS-level cleanup. The defender consequence: the fake-update initial-access vector is degraded, not closed — keep GPO restrictions on JScript/WSH execution from user-writable paths, browser isolation for email links, and (for WordPress operators) full credential rotation plus FIM after any cleanup, because removing the loader without rotating credentials invites reinfection.
