---
schema: 1
kind: incident
title: "IDC Frontier: ransomware stops four zones of IDCF Cloud for 495 companies and local governments; the provider's seventh report traces it to an open-source flaw in the customer portal's authentication system and says no server data left"
headline: "IDCF Cloud ransomware began with an open-source flaw in the customer portal's login system; no server data left"
summary: >
  IDC Frontier, a SoftBank Group subsidiary, says a ransomware attack from about 3:40 a.m. on 2026-10-07 stopped four zones of its IDCF Cloud
  East Japan Region 1, affecting 495 companies and local governments. Its seventh report of 2026-10-27, which closes the investigation, says an open-source flaw in the
  authentication system of the customer portal was exploited, after which the attacker took administrator rights on the virtualisation
  platform through the management console, stopped customers' virtual servers and encrypted them; it finds no trace of server data leaving,
  says portal registration data of up to 71 customers was queried and that backups are retrievable for 206 customers. The software is not named.
discovered_at: "2026-10-11T03:38:00Z"
updated_at: "2026-10-28T03:44:37Z"
event_date: "2026-10-07"
run_id: 2026-10-11T0256Z-intel
priority: routine
immediate_action: null
tags: [ransomware, cloud]
regions: [apac]
sectors: [technology, public-sector]
entities: ["incident:idc-frontier-idcf-cloud-ransomware-2026-10"]
techniques: [T1190, T1486, T1489]
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
  - url: "https://www.idcf.jp/news/topics/20261027001"
    publisher: "IDC Frontier (seventh report, Japanese)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.idcf.jp/news/topics/20261007002"
    publisher: "IDC Frontier (second report, Japanese)"
    date: "2026-10-07"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/"
    publisher: "BleepingComputer"
    date: "2026-10-08"
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
  - quote: "The third-party unauthorised access occurred because a vulnerability in the open-source software used in the IDCF Cloud Portal was exploited. (translated from Japanese)"
    original: "第三者による不正アクセスは、「IDCFクラウドポータル」で採用しているオープンソースソフトウェアの脆弱性が悪用されたことにより発生しました。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
  - quote: "After entering the authentication system of the IDCF Cloud Portal, the attacker obtained administrator rights on the virtualisation platform via the management console, stopped customers' virtual servers and encrypted the virtual servers themselves. (translated from Japanese)"
    original: "攻撃者は「IDCFクラウドポータル」の認証システムに侵入した後、管理コンソールを経由して仮想化基盤の管理者権限を不正に取得し、お客さまの仮想サーバーを停止するとともに仮想サーバー自体を暗号化しています。"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
  - quote: "restricting connections to the IDCF Cloud Portal to customer IP addresses and making multi-factor authentication mandatory (translated from Japanese)"
    original: "「IDCFクラウドポータル」への接続をお客さまIPアドレスに制限して、多要素認証を必須化"
    publisher: "IDC Frontier"
    source_url: "https://www.idcf.jp/news/topics/20261027001"
verification: single-source-victim
sourcing_note: >
  IDC Frontier, the victim, publishes the facts about its own incident in a numbered series of Japanese-language notices; the
  outage itself, but not the cause or the later counts, is corroborated by BleepingComputer. The conclusion
  that no data left is the provider's own judgement, reached with an external security firm and based on finding no trace. The cause and the
  attack path are the provider's own account in its seventh report, which does not name the software.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
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
  - at: "2026-10-28T03:44:37Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      IDC Frontier's seventh report of 2026-10-27, which closes the investigation, names the cause: an
      open-source flaw in the authentication system of its customer portal, after which the attacker took
      administrator rights on the virtualisation platform through the management console and encrypted the
      virtual servers; it replaces the entry's statement that the intrusion route is not public.
    fields: [title, headline, summary, techniques, sources, evidence, sourcing_note, body, classification, verification]
migrated_from: null
---

IDC Frontier says a ransomware attack that began around 3:40 a.m. on 2026-10-07 stopped four zones of IDCF Cloud East Japan Region 1, affecting 495 companies and local governments, and has suspended customer management consoles in every region; no source names the actor or the ransomware family ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002); [IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001); [BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)). The provider's seventh report of 2026-10-27 gives the route: a flaw in open-source software used in the customer portal's authentication system was exploited, and the attacker then obtained administrator rights on the virtualisation platform through the management console, stopped customers' virtual servers and encrypted them; the software is not named ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)). The lesson is supplier concentration: local governments sat behind one provider whose recovery first depended on copies the customers held, until the fifth report made the provider's own snapshot backups retrievable for 194 of the 495 ([IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001)) and for 206 by 2026-10-20 ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)).

**Exposure:** customers of IDCF Cloud; IDC Frontier lists IDCF Cloud TypeS and its private-cloud offering as outside the incident (translated from Japanese) ([IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)). For any other body, the condition is a website, mail or form service whose hosting and recovery copies depend on one provider.

**Defender takeaway:** check where the recovery copies of hosted websites, mail, forms and line-of-business systems live: IDC Frontier first expected restoration only from copies customers hold themselves ([IDC Frontier, 2026-10-08](https://www.idcf.jp/news/topics/20261008001)), and its own snapshot backups became retrievable for 194 of the 495 customers only a week into the outage ([IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001)), and for 206 by 2026-10-20 ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)); the attacker's console message claims it wiped 554,153 snapshots, which the provider's report does not confirm ([BleepingComputer, 2026-10-08](https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/)). A copy in the provider's own environment is not one to count on for the recovery window. Ask a hosting or cloud supplier in writing how its customer portal authenticates and whether the open-source components behind that login are inventoried and patched, because here the path to the virtualisation platform ran from the portal's login system through the management console; the supplier's own remediation, a rebuilt portal, an external identity provider, access limited to customer IP addresses with mandatory multi-factor authentication and a company-wide software inventory matched automatically against vulnerability data, is the checklist ([IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)).

## Update — 2026-10-16T04:12:00Z

IDC Frontier's fifth report of 2026-10-14 says that, with an external security firm, it confirmed the backup data is safe, so the 194 of the 495 affected customers that used its snapshot function can retrieve it, and that it found no trace of customer data in the affected zones being queried or carried out, so it judges that none left those servers, while confirming improper queries of the registration data of 48 customers in its cloud portal with no trace of it being taken (translated from Japanese; [IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001)). This replaces the third report's expectation that data could be restored only from customers' own backups; the report does not state the intrusion route.

## Update — 2026-10-28T03:44:37Z

IDC Frontier's seventh report of 2026-10-27 says its investigation with an external security firm is complete and names the cause: a third party exploited a vulnerability in open-source software used in the authentication system of the IDCF Cloud Portal, the portal customers use to start virtual servers and check billing, and so entered that system (translated from Japanese; [IDC Frontier, 2026-10-27](https://www.idcf.jp/news/topics/20261027001)). The attacker then obtained administrator rights on the virtualisation platform through the management console, stopped customers' virtual servers and encrypted them; the software is not named. The provider finds no trace of customer data leaving the virtual servers, says the improper queries of portal registration data reached up to 71 customers, up from 48, that up to four customer login passwords were improperly changed and have been reset, and that backups are retrievable for 206 customers. It is rebuilding the portal in a new environment, replacing the affected authentication system with an external identity provider and limiting portal access to customer IP addresses with mandatory multi-factor authentication.
