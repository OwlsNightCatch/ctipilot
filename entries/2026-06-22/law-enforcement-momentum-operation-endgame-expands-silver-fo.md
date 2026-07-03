---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Law-enforcement momentum — Operation Endgame expands, Silver Fox mass-arrest, Conti loader plea"
headline: "Law-enforcement momentum — Operation Endgame expands, Silver Fox mass-arrest, Conti loader plea"
summary: "The week was unusually strong on enforcement follow-through. A coordinated international action on 2026-06-18 expanded Operation Endgame to SocGholish/TA569, dismantling 106 C2 servers and stripping the FakeUpdates loader from 14,971 WordPress sites (Politie, 2026-06-18; daily 06-19)."
discovered_at: "2026-06-22T00:14:53Z"
event_date: 2026-06-18
run_id: 2026-W25-0aacfe65
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - botnet
regions:
  - europe
  - apac
  - global
sectors: []
entities:
  - "campaign:operation-endgame-amadey-stealc"
cves: []
sources:
  - url: "https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html"
    publisher: Politie (NL)
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/"
    publisher: Risky Business
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
migrated_from: briefs/weekly/2026-W25.md
---

The week was unusually strong on enforcement follow-through. A coordinated international action on 2026-06-18 expanded Operation Endgame to SocGholish/TA569, dismantling 106 C2 servers and stripping the FakeUpdates loader from 14,971 WordPress sites ([Politie, 2026-06-18](https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html); [daily 06-19](/briefs/2026-06-19/)). Chinese police arrested 67 members of the Silver Fox (Winos/ValleyRAT) cybercrime network across five provinces ([Risky Business, 2026-06-18](https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/); [daily 06-18](/briefs/2026-06-18/)), and Conti loader developer Oleksii Lytvynenko pleaded guilty in US federal court after extradition from Ireland ([Global Security, 2026-06-12](https://www.globalsecurity.org/security/library/news/2026/06/sec-260612-doj01.htm); [daily 06-14](/briefs/2026-06-14/)). For defenders, the Endgame action is the operationally useful one: SocGholish/FakeUpdates is a standard initial-access broker for ransomware, so the takedown measurably degrades a common entry path — though TA569's history of rebuilding means the relief is likely temporary.
