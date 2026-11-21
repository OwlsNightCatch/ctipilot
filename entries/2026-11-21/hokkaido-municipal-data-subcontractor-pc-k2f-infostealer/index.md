---
schema: 1
kind: incident
title: "Hokkaido: resident-register, support-needed and tax data of the cities of Rumoi and Iwamizawa and the town of Shintoku sat on a subcontractor's development PC infected with the K2F information stealer, which GIS Hokkaido links to the NIKKE game launcher; Rumoi's data was still there after its contract ended"
headline: "Hokkaido: municipal data on a subcontractor's PC hit by K2F stealer via a game launcher; Rumoi's contract had ended"
summary: >
  On 2026-11-18 and 2026-11-19 the Hokkaido municipalities Iwamizawa, Rumoi and Shintoku disclosed that data they gave their contractor GIS Hokkaido was stored on a development terminal of its subcontractor Rimgate that the K2F information stealer infected overnight on 2 to 3 November: up to 71,002 resident-register and 4,503 support-needed records for Rumoi, whose personal data was still on the terminal after its contract ended, 6,001 resident-register and 986 evacuation-support records for Shintoku, and fixed-asset-tax land and building data for Iwamizawa. GIS Hokkaido told ITmedia that the PC launcher of the game NIKKE is involved and would not say whether Rimgate staff ran the game on the work PC; no leak or misuse is confirmed, and none of the data contains the national My Number.
discovered_at: "2026-11-21T04:48:00Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-21T0355Z-intel
priority: routine
immediate_action: null
tags: [data-breach, supply-chain, infostealer]
regions: [apac]
sectors: [public-sector]
entities: ["incident:hokkaido-municipal-data-subcontractor-k2f-infostealer-2026-11", "malware:k2f-infostealer"]
techniques: [T1195.002, T1555]
affected_products: []
cves: []
sources:
  - url: "https://www.e-rumoi.jp/soumu/page11_00252.html"
    publisher: "Rumoi City (municipal notice, Japanese)"
    date: "2026-11-19"
    role: primary
  - url: "https://www.city.iwamizawa.hokkaido.jp/soshiki/zeimu/zei/2/3/18234.html"
    publisher: "Iwamizawa City (municipal notice, Japanese)"
    date: "2026-11-18"
    role: primary
  - url: "https://www.shintoku-town.jp/oshirase/3675/"
    publisher: "Shintoku Town (municipal notice, Japanese)"
    date: "2026-11-18"
    role: primary
  - url: "https://www.itmedia.co.jp/news/article/2611/19/2000003351/"
    publisher: "ITmedia NEWS (Japanese)"
    date: "2026-11-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "there is a risk that personal information that was still stored on the same terminal after the contract ended has leaked (translated from Japanese)"
    original: "契約終了後も同端末に保存されていた個人情報の漏えいのおそれがある"
    publisher: "Rumoi City (municipal notice, Japanese)"
    source_url: "https://www.e-rumoi.jp/soumu/page11_00252.html"
  - quote: "K2F is malware with functions to remotely control an infected PC and to steal information such as passwords. (translated from Japanese)"
    original: "K2Fは、感染したPCを遠隔操作したり、パスワードなどの情報を盗み出したりする機能を持つマルウェア。"
    publisher: "ITmedia NEWS (Japanese)"
    source_url: "https://www.itmedia.co.jp/news/article/2611/19/2000003351/"
  - quote: "admitted that the PC launcher (startup application) of the popular game NIKKE is involved (translated from Japanese)"
    original: "人気ゲーム「勝利の女神：NIKKE」のPC版ランチャー（起動用アプリ）が関係していると認めた"
    publisher: "ITmedia NEWS (Japanese)"
    source_url: "https://www.itmedia.co.jp/news/article/2611/19/2000003351/"
verification: multi-source
sourcing_note: >
  The three municipalities' own notices agree on the dates and the subcontractor, and ITmedia carries GIS Hokkaido's statement about the NIKKE launcher; all sources were read in Japanese. No source says the data was exfiltrated; the municipalities say a leak is possible and none is confirmed. ITmedia's account that the launcher was tampered with by a third party comes from its own background paragraph, not from the municipalities.
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
updates: []
migrated_from: null
---

Three Hokkaido municipalities disclosed on 2026-11-18 and 2026-11-19 that personal data they had handed to their contractor GIS Hokkaido was stored on a development terminal of GIS Hokkaido's subcontractor Rimgate, on which traces of the information stealer K2F were found: the terminal was infected overnight on 2 to 3 November, Rimgate found the traces on 4 November and cut it from the network, and GIS Hokkaido told the municipalities between 13 and 16 November ([Rumoi City, 2026-11-19](https://www.e-rumoi.jp/soumu/page11_00252.html); [Iwamizawa City, 2026-11-18](https://www.city.iwamizawa.hokkaido.jp/soshiki/zeimu/zei/2/3/18234.html); [Shintoku Town, 2026-11-18](https://www.shintoku-town.jp/oshirase/3675/)). The data at risk is up to 71,002 resident-register records (as of February 2022) and 4,503 records of people needing support, with disability category and care level, for Rumoi, whose personal data was still on the terminal after its contract ended; 6,001 resident-register and 986 disaster-evacuation-support records for Shintoku; and up to 10,348 land parcels and 7,037 buildings of fixed-asset-tax data for Iwamizawa; none contains the national My Number and no leak or misuse is confirmed (translated from Japanese) ([Rumoi City, 2026-11-19](https://www.e-rumoi.jp/soumu/page11_00252.html); [Iwamizawa City, 2026-11-18](https://www.city.iwamizawa.hokkaido.jp/soshiki/zeimu/zei/2/3/18234.html); [Shintoku Town, 2026-11-18](https://www.shintoku-town.jp/oshirase/3675/)). GIS Hokkaido told ITmedia that the PC launcher of the game NIKKE is involved and declined to say whether Rimgate staff ran the game on the work PC; ITmedia adds that a third-party tampering with that launcher, which could deliver K2F on start, became public on 5 November (translated from Japanese) ([ITmedia NEWS, 2026-11-19](https://www.itmedia.co.jp/news/article/2611/19/2000003351/)). This is municipal public-sector data held through a supplier chain.

**Exposure:** any administration whose resident, social-care or tax data went to a contractor that subcontracts, and any supplier endpoint where consumer software such as a game launcher can run next to project data; the check is which supplier terminals still hold extracts from finished projects ([Rumoi City, 2026-11-19](https://www.e-rumoi.jp/soumu/page11_00252.html); [ITmedia NEWS, 2026-11-19](https://www.itmedia.co.jp/news/article/2611/19/2000003351/)).

**Detection:** the infection path is the observable: a consumer game launcher on a workstation that holds project data, and, because K2F steals passwords and allows remote control, password-store reads by non-browser processes and unexplained remote sessions on such machines; the sources give no more specific indicator ([ITmedia NEWS, 2026-11-19](https://www.itmedia.co.jp/news/article/2611/19/2000003351/)).

**Defender takeaway:** ask each supplier and its subcontractors which of your extracts they still hold, have them delete data of finished contracts and confirm it, and keep consumer software off the machines that handle it; Rumoi's contract had ended yet its data was still on the infected terminal ([Rumoi City, 2026-11-19](https://www.e-rumoi.jp/soumu/page11_00252.html)).
