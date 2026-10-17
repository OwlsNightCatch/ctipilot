---
schema: 1
kind: incident
title: "IDC Frontier: ransomware stops four zones of IDCF Cloud for 495 companies and local governments; the provider now says its backups are safe and retrievable for 194 customers and that it found no trace of data taken from customers' virtual servers"
headline: "IDCF Cloud outage: backups now retrievable for 194 of 495 customers; provider finds no trace of server data taken"
summary: >
  IDC Frontier, a SoftBank Group subsidiary, says a ransomware attack from about 3:40 a.m. on 2026-10-07 stopped four zones of
  its IDCF Cloud East Japan Region 1, affecting 495 companies and local governments. Its fifth report (2026-10-14) says its backup
  data is safe and retrievable for the 194 affected customers that used its snapshot function, and that it found no trace of data in
  customers' virtual servers being queried or taken, while confirming improper queries of the portal registration data of 48
  customers; the intrusion route is not public.
discovered_at: "2026-10-11T03:38:00Z"
updated_at: "2026-10-16T04:12:00Z"
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
  - url: "https://www.idcf.jp/news/topics/20261014001"
    publisher: "IDC Frontier (fifth report, Japanese)"
    date: "2026-10-14"
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
  - quote: "Until now we expected retrieval and restoration of customer data to be difficult, but together with an external security firm we have confirmed that the backup data is safe. (translated from Japanese)"
    original: "これまで、お客さまのデータの取り出しや復元は困難と見込んでおりましたが、外部のセキュリティ専門企業と連携してバックアップデータの安全性が確認できました。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261014001"
  - quote: "From these facts, we judge that there was no outflow of data to the outside. (translated from Japanese)"
    original: "これらの事実から、当社としては外部へのデータの流出はなかったと判断しています。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261014001"
  - quote: "IDCF Cloud has proactively disabled customer access to management consoles for all regions while it verifies their security, and will restore access after confirming it is safe to do so."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
verification: multi-source
sourcing_note: >
  IDC Frontier, the victim, publishes the facts about its own incident in a numbered series of Japanese-language notices; the
  outage itself is corroborated by Jiji Press, which reports the downstream website failures, and by BleepingComputer. The conclusion
  that no data left is the provider's own judgement, reached with an external security firm and based on finding no trace.
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
updates:
  - at: "2026-10-16T04:12:00Z"
    run_id: 2026-10-16T0256Z-intel
    type: update
    summary: >
      IDC Frontier's fifth report of 2026-10-14 confirms its backup data is safe and retrievable for the 194 of the 495 affected
      customers that used its snapshot function, reports no trace of data in customers' virtual servers being queried or taken and
      judges that none left, and confirms improper queries of the portal registration data of 48 customers; this replaces the third report's expectation that data could be restored only from customers' own backups.
    fields: [title, headline, summary, sources, evidence, sourcing_note, body]
migrated_from: null
---

IDC Frontier says a ransomware attack that began around 3:40 a.m. on 2026-10-07 stopped four zones of IDCF Cloud East Japan Region 1, affecting 495 companies and local governments, among them the websites of Ibaraki Prefecture and the city of Kodaira, and has suspended customer management consoles in every region; no source names the actor, the ransomware family or the intrusion route ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002); [IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001); [BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/); [Jiji Press via nippon.com, 2026-10-07](https://www.nippon.com/en/news/yjj2026100700867/)). The lesson is supplier concentration: local governments sat behind one provider whose recovery first depended on copies the customers held, until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495.

**Exposure:** customers of IDCF Cloud; IDC Frontier lists IDCF Cloud TypeS and its private-cloud offering as outside the incident (translated from Japanese) ([IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)). For any other body, the condition is a website, mail or form service whose hosting and recovery copies depend on one provider.

**Defender takeaway:** check where the recovery copies of hosted websites, mail, forms and line-of-business systems live: IDC Frontier first expected restoration only from copies customers hold themselves ([IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)), and its own snapshot backups became retrievable for 194 of the 495 customers only a week into the outage ([IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001)); the attacker's console message claims it wiped 554,153 snapshots, which the provider's report does not confirm ([BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)). A copy in the provider's own environment is not one to count on for the recovery window.

## Update — 2026-10-16T04:12:00Z

IDC Frontier's fifth report of 2026-10-14 says that, with an external security firm, it confirmed the backup data is safe, so the 194 of the 495 affected customers that used its snapshot function can retrieve it, and that it found no trace of customer data in the affected zones being queried or carried out, so it judges that none left those servers, while confirming improper queries of the registration data of 48 customers in its cloud portal with no trace of it being taken (translated from Japanese; [IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001)). This replaces the third report's expectation that data could be restored only from customers' own backups; the report does not state the intrusion route.
