---
schema: 1
kind: research
title: "Sekoia and Kudelski Security split the 'Lazarus umbrella' into six named DPRK clusters, and document two of them adopting commodity ransomware-as-a-service within two months of each other"
headline: "A Swiss research lab co-publishes the DPRK actor-tracking update: two nominally-espionage clusters rented commodity ransomware in the same window"
summary: >
  Sekoia and Kudelski Security (a Switzerland-based firm) jointly reassessed DPRK's offensive-cyber
  organization on 2026-09-07, replacing the historical "Lazarus umbrella" with six tracked
  sub-clusters and documenting that Andariel and Moonstone Sleet each adopted a commodity
  ransomware-as-a-service (Play and Qilin respectively) within two months of one another — a single
  observed timing overlap the authors call notable, consistent with the general possibility that
  nominally espionage-focused DPRK units rent criminal ransomware infrastructure alongside bespoke
  tooling.
discovered_at: "2026-09-08T04:41:00Z"
updated_at: null
event_date: "2026-09-07"
run_id: 2026-09-08T0411Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, ransomware, cryptocrime, north-korea-nexus]
regions: [global]
sectors: []
entities: ["actor:kimsuky", "actor:purpledelta", "actor:scarcruft", "actor:qilin", "actor:temp-hermit", "actor:citrine-sleet", "actor:cryptocore", "actor:jade-sleet", "actor:moonstone-sleet", "actor:andariel"]
techniques: [T1657, T1486]
affected_products: []
cves: []
sources:
  - url: "https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities"
    publisher: "Kudelski Security (Switzerland)"
    date: "2026-09-07"
    role: primary
  - url: "https://www.sekoia.com/blog/beyond-lazarus-organization-of-dprk-cyber-capabilities"
    publisher: "Sekoia"
    date: "2026-09-07"
    role: primary
closed_sources: []
evidence:
  - quote: "We notably made our clustering evolved by splitting the Lazarus umbrella into six distinct sub-clusters: TEMP.Hermit, Citrine Sleet, CryptoCore, Jade Sleet, Moonstone Sleet, and Famous Chollima."
    publisher: "Sekoia TDR team / Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities"
  - quote: "Of note, Andariel is particular as it used custom ransomware (Maui and H0lyGh0st) for financial theft, as well as ransomware-as-a-service (RaaS) developed by an operator of the Russian cybercrime ecosystem. It was notably observed collaborating with Play in 2024. Another DPRK cluster, Moonstone Sleet, acted similarly by deploying its custom malware FakePenny in 2024, but also the Qilin RaaS in 2025. It is interesting to note that the two clusters integrated RaaS in their campaigns within two months of each other."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities"
  - quote: "Kudelski Security observed that fake IT workers and offensive teams often share the same VPN exit nodes."
    publisher: "Kudelski Security"
    source_url: "https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities"
verification: single-source
sourcing_note: >
  Sekoia and Kudelski Security co-published identical content on the same day; this is one joint
  assessor's own novel clustering framework, not independently corroborated by a third party.
  Individual component facts (Andariel's Maui/H0lyGh0st ransomware, Moonstone Sleet's FakePenny)
  trace to prior third-party reporting the authors cite, but the consolidated six-cluster
  taxonomy itself is this publication's new claim.
confidence: medium
references: [2026-08-28/kudelski-bismarck-dprk-it-worker-gambling-fakecalls-overlap, 2026-09-03/kimsuky-seafood-invoice-lnk-backblaze-b2-c2, 2026-09-07/rapid7-ted-backdoor-curlrat-dprk-haproxy]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Sekoia's TDR team and Kudelski Security, a Switzerland-based research firm, jointly published a reassessment of how North Korea's offensive-cyber apparatus is organized ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)). The authors now track the historical "Lazarus umbrella" as six distinct sub-clusters — TEMP.Hermit, Citrine Sleet, CryptoCore, Jade Sleet, Moonstone Sleet, and Famous Chollima, the last already tracked here as an alias of the North Korean fraudulent-IT-worker cluster — each carrying a different primary mandate spanning strategic espionage, dual espionage-and-revenue operations, and pure financially motivated crime ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)). The espionage-focused clusters under GRIB (formerly RGB), TEMP.Hermit among them, are the authors' own described inheritors of both the historical Lazarus umbrella and the Kimsuky cluster's lineage, even where their precise bureau affiliation is debated within the CTI community ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)). The authors date the Lazarus umbrella's internal reorganization into specialized sub-clusters to a 2018–2023 transition phase alongside the global expansion of the cryptocurrency market, out of which APT38 itself emerged as the financially-motivated sub-cluster; APT38 has since, per the authors' own current research, further split into two of these — CryptoCore and Jade Sleet — both exclusively financially motivated and focused on cryptocurrency, Web3 and blockchain targets, though the authors do not date this more recent split.

The most defender-relevant finding is a documented pattern of commodity-ransomware adoption by nominally espionage-focused units: Andariel, a dual-mandate cluster, used its own custom ransomware (Maui, H0lyGh0st) and separately collaborated with the criminal Play ransomware-as-a-service operation in 2024, citing prior reporting from Unit 42; Moonstone Sleet deployed its own custom malware (FakePenny) the same year and then adopted the Qilin ransomware-as-a-service in 2025 — within two months of Andariel's own RaaS adoption ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)). The authors note it is "interesting" that the two clusters integrated RaaS into their campaigns within two months of each other — a single observed timing overlap, not a claimed broader trend, though it is consistent with the general possibility that DPRK clusters rent commodity ransomware infrastructure alongside, or instead of, running only bespoke tooling.

The report also states that "Reaper" — already tracked here as an alias of ScarCruft/APT37 — is the cluster aligned with North Korea's newly renamed National Intelligence Agency (formerly the Ministry of State Security, renamed June 2026), tasked with surveillance of defectors and South Korean NGOs and activists. Kudelski Security's own separate prior research, cited in this report, found that DPRK fake-IT-worker infrastructure and offensive-APT infrastructure share the same VPN exit nodes — a concrete pivot point for correlating IT-worker-fraud indicators against APT intrusion infrastructure ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)). Separately, the report documents a Cambodia-based money-laundering hub, the Huione Group — flagged by the US Treasury's FinCEN as a primary money-laundering concern — whose executives the authors say have shown indications of direct ties to North Korean actors, with an estimated USD 37.6 million in DPRK-linked cryptocurrency laundered through it between 2021 and 2025 via stablecoins and technical tooling that let North Korea convert illicit proceeds into ostensibly legitimate assets ([Kudelski Security, 2026-09-07](https://kudelskisecurity.com/research/beyond-lazarus-organization-of-dprk-cyber-capabilities)).

**Defender takeaway:** organizations maintaining DPRK actor-tracking — threat-intel feeds, indicator allow/deny lists keyed to vendor cluster names — should map internal designations against this consolidated six-way split, and should treat ransomware-as-a-service indicators (Play, Qilin) as potentially DPRK-nexus rather than purely criminal when other DPRK tradecraft is present in the same intrusion, given the authors' documented cross-over between the two clusters.
