---
schema: 1
kind: threat
title: "GoCaracal: Dark Caracal's new Go-based malware framework uses an Ethereum smart contract as a resilient fallback channel to deliver replacement C2 addresses without redeploying the implant"
headline: "A malware family reads its own next command-and-control address off the public blockchain — infrastructure no defender or ISP is going to block wholesale"
summary: >
  Arctic Wolf Labs identified GoCaracal, a previously undocumented Go-based modular malware
  framework deployed in a June 2026 intrusion at a Venezuelan communications organisation. Its
  extended build's most notable feature is a blockchain-based resilience mechanism: after
  repeated C2 failures, it reads a replacement address from an Ethereum smart contract's storage
  slot via a public JSON-RPC call, letting operators rotate every deployed implant's C2 through an
  ordinary blockchain transaction with no redeployment. Arctic Wolf attributes the June intrusion
  to Dark Caracal with medium confidence.
discovered_at: "2026-08-28T06:25:00Z"
updated_at: null
event_date: "2026-08-26"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, botnet]
regions: [latam, global]
sectors: [telco]
entities: [actor:dark-caracal, malware:gocaracal]
techniques: [T1102.001, T1071.001, T1041]
affected_products: []
cves: []
sources:
  - url: "https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/"
    publisher: "Arctic Wolf Labs"
    date: "2026-08-26"
    role: primary
closed_sources: []
evidence:
  - quote: "After repeated failures to reach the primary C2, the malware sends an eth_getStorageAt request to a public Ethereum JSON-RPC endpoint and reads a value from the configured contract's storage."
    publisher: "Arctic Wolf Labs"
  - quote: "Operators can update the stored C2 value through a blockchain transaction, and deployed implants can retrieve the new address without receiving an updated binary."
    publisher: "Arctic Wolf Labs"
  - quote: "Arctic Wolf Labs assesses with medium confidence that this intrusion was conducted by Dark Caracal."
    publisher: "Arctic Wolf Labs"
  - quote: "Our assessment is based on the convergence of multiple evidence types, including the use of Bandook, recurring Delphi loader characteristics, Spanish-language financial lures, malicious SVG files, URL-shortening services, document-themed infrastructure, provider preferences, and targeting consistent with the group's established focus on Latin America."
    publisher: "Arctic Wolf Labs"
verification: single-source
sourcing_note: >
  Arctic Wolf Labs is the sole source for this specific malware family and its blockchain C2
  mechanism; the Dark Caracal attribution is the lab's own medium-confidence assessment based on
  convergent evidence rather than a first-party admission or an independently-corroborated claim.
confidence: medium
references: []
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

Arctic Wolf Labs identified GoCaracal, a previously undocumented Go-based modular malware framework, deployed during a June 2026 intrusion at an unnamed communications organisation in Venezuela alongside an updated Bandook variant delivered via a Delphi loader. Analysis of 249 samples traces the framework's development across four phases from January through July 2026 and identifies two operational build profiles: a lightweight implant for initial access and payload delivery, and an extended build for sustained intelligence collection adding browser data theft, keylogging, remote desktop control and SOCKS5 proxying to the lightweight build's remote-shell and payload-execution core.

The extended variant's most notable feature is a blockchain-based C2 resilience mechanism: "after repeated failures to reach the primary C2, the malware sends an eth_getStorageAt request to a public Ethereum JSON-RPC endpoint and reads a value from the configured contract's storage" ([Arctic Wolf Labs, 2026-08-26](https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/)) — reading a replacement C2 address from a smart contract's storage slot when a valid one is returned. "Operators can update the stored C2 value through a blockchain transaction, and deployed implants can retrieve the new address without receiving an updated binary" ([Arctic Wolf Labs, 2026-08-26](https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/)) — a takedown-resilient fallback channel that rides on infrastructure no defender or ISP is going to block wholesale.

"Arctic Wolf Labs assesses with medium confidence that this intrusion was conducted by Dark Caracal", a cyberespionage group associated with Lebanon's General Directorate of General Security ([Arctic Wolf Labs, 2026-08-26](https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/)). "Our assessment is based on the convergence of multiple evidence types, including the use of Bandook, recurring Delphi loader characteristics, Spanish-language financial lures, malicious SVG files, URL-shortening services, document-themed infrastructure, provider preferences, and targeting consistent with the group's established focus on Latin America" ([Arctic Wolf Labs, 2026-08-26](https://arcticwolf.com/resources/blog/dark-caracal-reloaded-new-malware-same-hunting-grounds/)).

Latin America is the confirmed victim region for this specific intrusion, but the technique class — blockchain smart-contract storage as a dead-drop resolver for C2 address rotation — is a genuinely novel resilience pattern transferable to any actor's infrastructure and worth a detection concept regardless of region. **Triage:** outbound JSON-RPC calls (`eth_getStorageAt` or similar Ethereum node RPC methods) from endpoint or server processes that have no legitimate business reason to talk to a blockchain node are a high-signal, low-noise behavioural indicator — most enterprise endpoints never make direct Ethereum RPC calls at all, so a query to any public Ethereum RPC endpoint from a non-blockchain-application process is the discriminator, rather than requiring a specific contract-address blocklist that the operator can trivially rotate away from.
