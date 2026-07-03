---
schema: 1
kind: incident
horizon: operational
title: "Maine's breach-notification portal abused for fraudulent filings against VRChat and Discord — both companies deny any breach"
headline: "Maine's breach-notification portal abused for fraudulent filings against VRChat and Discord — both companies deny any breach"
summary: "Maine's Attorney-General breach-notification portal published fraudulent data-breach filings — one claiming a 2.4-million-user VRChat cloud compromise, another a 10-million-user Discord breach — because submissions are published without filer-identity verification (BleepingComputer, 2026-06-11)."
discovered_at: "2026-06-12T05:00:04Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - disinformation
  - data-breach
regions:
  - us
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/maine-breach-portal-abused-to-publish-fake-data-breach-disclosures/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-12.md
---

Maine's Attorney-General breach-notification portal published fraudulent data-breach filings — one claiming a 2.4-million-user VRChat cloud compromise, another a 10-million-user Discord breach — because submissions are published without filer-identity verification ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/maine-breach-portal-abused-to-publish-fake-data-breach-disclosures/)). VRChat stated: "VRChat did not submit this Notice of Data Incident, and the employee/email cited does not exist. We have no reason to believe that our data or systems have been compromised." Discord likewise denied filing. The Maine AG's office acknowledged the fraudulent notices and moved to remove them. [SINGLE-SOURCE — BleepingComputer.]

**Why it matters to us:** CTI teams routinely treat state breach portals as authoritative collection sources — this incident shows they can be poisoned. Require victim confirmation or regulator follow-up before acting on (or republishing) portal-only breach claims; the same trust-exploitation pattern would work against any unauthenticated notification channel.
