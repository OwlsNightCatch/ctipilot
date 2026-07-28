---
schema: 1
kind: threat
horizon: operational
title: "Dysphoria: an IoT botnet that resolves its C2 through Ethereum and Solana name services and turns its own victims into the relay mesh"
headline: "Dysphoria botnet moves C2 resolution onto blockchain name services and rebuilds its infrastructure from victim devices"
summary: >
  A joint CNCERT and QiAnXin XLab report (2026-07-25) tracks Dysphoria, an IoT botnet exceeding 200,000
  bots that descends from the jackskid and fbot lineages and has made two infrastructure changes defenders
  should note: it retrieves C2 addressing from Ethereum ENS and Solana SNS name records rather than DNS,
  with the real IPv4 address hidden inside a decoy IPv6-formatted string, and since late June it fields a
  variant that drops DDoS entirely to serve as a relay node, using UPnP to open roughly 155 port-forwarding
  rules on the local gateway. The relay addresses that DDoS bots ultimately talk to are themselves other
  infected devices, so takedown pressure on domains and hosted infrastructure reaches very little of it.
discovered_at: "2026-07-28T04:53:00Z"
event_date: "2026-07-25"
run_id: 2026-07-28T0409Z-intel
priority: notable
immediate_action: null
tags: [botnet, ddos]
regions: [global]
sectors: [telco, technology]
entities: ["tool:dysphoria-botnet"]
techniques: [T1110.001, T1190, T1568, T1090.003, T1498, T1036.005, T1027]
affected_products: []
cves: []
sources:
  - url: "https://blog.xlab.qianxin.com/dysphoria/"
    publisher: "QiAnXin XLab / CNCERT"
    date: "2026-07-25"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/"
    publisher: "BleepingComputer"
    date: "2026-07-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "该样本不再具备 DDoS 攻击功能，而是纯粹作为中继/代理节点运作"
    publisher: "QiAnXin XLab / CNCERT"
  - quote: "the botnet uses Ethereum ENS and Solana SNS domains to retrieve infrastructure information, while C2 addresses are concealed inside fake IPv6 strings and recovered using a custom byte-transformation algorithm."
    publisher: "BleepingComputer"
verification: single-source
sourcing_note: "The technical primary is a Chinese-language report published jointly by CNCERT, China's national CERT, and QiAnXin XLab, carrying sample-level analysis, the string-decryption routine, the C2 resolution chain and the relay protocol (reliability B — an original research lab publication; the co-sealing national CERT is not acting as an authority for this deployment's jurisdiction). BleepingComputer's same-day write-up is a press account of that report rather than independent corroboration — it attributes every technical and scale claim to XLab and carries no first-hand observation of the family — so this entry is single-source on the XLab/CNCERT research and credibility is 2, not 1. The scale figures are asymmetric and are reported as XLab measures them: 4,401 confirmed active bots inside China for 2026-07-14 to 07-20 against a peak of 239,000 overseas bots seen online in a day, with the roughly 200,000 total drawn from XLab's tracking and a leaked operator-panel screenshot it assesses as consistent with its own telemetry. The primary is two days older than this run's 26-hour window; it is carried on the developing-story window, with the in-window fact being the first independent security-press coverage on 2026-07-27. XLab publishes extensive indicators — hashes, IP addresses, conventional domains and the blockchain names themselves — none of which is reproduced here."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Two design changes in this family are worth a defender's attention, and neither is about the DDoS capability it is nominally built for. The first is where the bots learn who to talk to. Instead of resolving a conventional domain, Dysphoria queries records held in Ethereum's ENS and Solana's SNS decentralised name services; the retrieved text carries decoy IPv6-formatted strings, from which the sample extracts four key bytes and reconstructs the real IPv4 address through a custom permutation routine ([QiAnXin XLab / CNCERT, 2026-07-25](https://blog.xlab.qianxin.com/dysphoria/)). BleepingComputer's account of the same report describes the mechanism in the same terms ([BleepingComputer, 2026-07-27](https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/)). Because the names live on public chains rather than in a registrar's zone, the usual levers — suspension, sinkholing, registry-level takedown — do not apply to that layer at all.

The second change is what the resolved addresses point at. A DDoS sample first reads a distribution-node list from the ENS record, then requests a further list over plain HTTP from those nodes on a high port; XLab's tracing found that the addresses returned as the actual C2 endpoints are themselves other infected devices converted into relays ([QiAnXin XLab / CNCERT, 2026-07-25](https://blog.xlab.qianxin.com/dysphoria/)). A dedicated variant exists only for this purpose: it carries no attack module and instead broadcasts on the LAN for a UPnP-capable gateway, drives the WAN connection service to create roughly 155 port-forwarding rules, listens on those ports, and relays each inbound connection to the same port on a remote host using epoll-driven non-blocking I/O, reporting its availability as a small JSON health record — status, connection count and bandwidth — every few seconds. XLab dates this variant to 2026-06-25 and calls it the start of the family's "relay transformation", without offering an assessment of why the operators made the change ([QiAnXin XLab / CNCERT, 2026-07-25](https://blog.xlab.qianxin.com/dysphoria/)). Propagation remains unglamorous: weak Telnet and SSH credentials brute-forced, plus known IoT remote-code-execution flaws against routers, gateways and cameras — XLab names thirteen identifiers spanning 2013-vintage to 2025-vintage bugs and presents them explicitly as only part of the set it has observed in use. Operators advertise up to roughly 4 Tbps of attack capacity on commercial packages priced from tens to hundreds of US dollars.

**Defender takeaway:** the exposure for a European estate is less about being a DDoS target and more about hosting the infrastructure. Any unmanaged SOHO router, camera or embedded-Linux device on a branch, site or home-working network is a candidate relay node, and a device in that role generates traffic patterns that a NAT boundary would normally suppress — which is precisely what the UPnP step removes. Blocking known C2 addresses and domains buys little here, because the addressing layer is a public-chain record and the endpoints are rotating victim devices.

**Triage:** three observables discriminate this from ordinary IoT noise. A single LAN host requesting on the order of 150 UPnP port mappings in quick succession has no benign counterpart — legitimate applications request one or a few. Name-resolution or HTTP traffic associated with ENS or SNS lookups originating from an embedded device is likewise anomalous by device class, whatever it would mean from a workstation. And both sample classes rewrite their process name at runtime to masquerade as `libdalvikengine.so`, an Android runtime library, so on a Linux-based device with no Android runtime a process presenting that name is the artifact rather than the disguise ([QiAnXin XLab / CNCERT, 2026-07-25](https://blog.xlab.qianxin.com/dysphoria/)). Fixed-length periodic beacons from IoT devices are a supporting signal, not a standalone one.
