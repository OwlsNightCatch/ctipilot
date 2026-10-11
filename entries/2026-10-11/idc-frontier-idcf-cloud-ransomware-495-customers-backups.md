---
schema: 1
kind: incident
title: "IDC Frontier: ransomware stops four zones of IDCF Cloud for 495 companies and local governments, and the provider says customer data there can be restored only from customers' own backups"
headline: "IDCF Cloud ransomware hits 495 customers incl. local governments; provider says only their own backups restore"
summary: >
  IDC Frontier, a SoftBank Group subsidiary, says a ransomware attack from about 3:40 a.m. on 2026-10-07 stopped four zones of
  its IDCF Cloud East Japan Region 1, affecting 495 companies and local governments whose virtual servers stopped and cannot be
  restarted. Its third report (2026-10-08) says customer data in those zones is expected to be difficult to retrieve or restore
  and, in its current view, can be recovered only from customers' own backups; management consoles are suspended in every
  region and the intrusion route is not public. Municipal and prefectural websites were among those that went down.
discovered_at: "2026-10-11T03:38:00Z"
updated_at: null
event_date: "2026-10-07"
run_id: 2026-10-11T0256Z-intel
priority: routine
immediate_action: null
tags: [ransomware, cloud]
regions: [apac]
sectors: [technology, public-sector]
entities: ["incident:idc-frontier-idcf-cloud-ransomware-2026-10"]
techniques: [T1486]
affected_products: ["IDC Frontier IDCF Cloud"]
cves: []
sources:
  - url: "https://www.idcf.jp/news/topics/20261008001"
    publisher: "IDC Frontier (third report, Japanese)"
    date: "2026-10-08"
    role: primary
  - url: "https://www.idcf.jp/news/topics/20261007002"
    publisher: "IDC Frontier (second report, Japanese)"
    date: "2026-10-07"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
    publisher: "BleepingComputer"
    date: "2026-10-08"
    role: corroborating
  - url: "https://www.nippon.com/en/news/yjj2026100700867/"
    publisher: "Jiji Press via nippon.com"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In our current view, data can be restored only from backup data that customers hold themselves. (translated from Japanese)"
    original: "現時点での当社の見解では、データの復元はお客さま自身が保持しているバックアップデータからのみ可能となります。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261008001"
  - quote: "IDCF Cloud has proactively disabled customer access to management consoles for all regions while it verifies their security, and will restore access after confirming it is safe to do so."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
verification: multi-source
sourcing_note: >
  IDC Frontier, the victim, publishes the facts about its own incident in a numbered series of Japanese-language notices; the
  outage itself is corroborated by Jiji Press, which reports the downstream website failures, and by BleepingComputer.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

IDC Frontier says a ransomware attack by a third party that began around 3:40 a.m. on 2026-10-07 stopped four zones of IDCF Cloud East Japan Region 1, affecting 495 companies and local governments, and that, in its current view, data in those zones can be restored only from backups customers hold themselves (translated from Japanese) ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002); [IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)). The provider has suspended customer management consoles in every region ([BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)), and Jiji Press reports that websites of Ibaraki Prefecture and the city of Kodaira were among those that went down ([Jiji Press via nippon.com, 2026-10-07](https://www.nippon.com/en/news/yjj2026100700867/)). No source names the actor, the ransomware family or the intrusion route. The lesson is supplier concentration: local governments sat behind one provider whose recovery depended on copies the customers held.

**Exposure:** customers of IDCF Cloud; IDC Frontier lists IDCF Cloud TypeS and its private-cloud offering as outside the incident (translated from Japanese) ([IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)). For any other body, the condition is a website, mail or form service whose hosting and recovery copies depend on one provider.

**Defender takeaway:** check where the recovery copies of hosted websites, mail, forms and line-of-business systems live. IDC Frontier says restoration is possible only from copies customers hold themselves and has shut customer consoles in every region, so a copy that sits in the provider's own environment, or behind its console, is not one to count on.
