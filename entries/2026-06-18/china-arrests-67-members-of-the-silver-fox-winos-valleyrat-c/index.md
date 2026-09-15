---
schema: 1
kind: threat
title: China arrests 67 members of the Silver Fox (Winos/ValleyRAT) cybercrime network
headline: China arrests 67 members of the Silver Fox (Winos/ValleyRAT) cybercrime network
summary: "Chinese police arrested 67 suspects across five provinces in a June 2026 operation against Silver Fox — also tracked as Void Arachne, UTG-Q-1000 and TA4922 — assessed as one of the most active crimeware operations targeting Chinese-speaking users (Risky Biz News, 2026-06-17)."
discovered_at: "2026-06-18T05:10:30Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - infostealer
regions:
  - apac
sectors:
  - finance
  - technology
entities:
  - "actor:ta4922"
cves: []
sources:
  - url: "https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/"
    publisher: Risky Biz News
    role: primary
  - url: "https://www.cert.org.cn/publish/main/10/2026/20260522113326926111046/20260522113326926111046_.html"
    publisher: CNCERT/CC
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
migrated_from: briefs/2026-06-18.md
---

Chinese police arrested 67 suspects across five provinces in a June 2026 operation against Silver Fox — also tracked as Void Arachne, UTG-Q-1000 and TA4922 — assessed as one of the most active crimeware operations targeting Chinese-speaking users ([Risky Biz News, 2026-06-17](https://news.risky.biz/risky-bulletin-china-arrests-members-of-silver-fox-cybercrime-group/)). The arrests reportedly span the full criminal supply chain: the primary developer/seller of the Silver Fox (Winos) trojan, a variant developer, phishing-site operators, and fake-app download-site operators, with secondary RATs including ValleyRAT used for credential theft. A CNCERT/CC security alert issued on 2026-05-22 preceded the operation ([CNCERT/CC, 2026-05-22](https://www.cert.org.cn/publish/main/10/2026/20260522113326926111046/20260522113326926111046_.html)).

**Defender takeaway:** Silver Fox's primary targeting is mainland-Chinese and diaspora users, but Winos/ValleyRAT campaigns have extended to other regions and Chinese-language lures reach diaspora communities in Europe. A takedown of operators typically forces infrastructure churn rather than ending the family — expect rebuild attempts and watch for short-term shifts in delivery infrastructure for these loaders.
