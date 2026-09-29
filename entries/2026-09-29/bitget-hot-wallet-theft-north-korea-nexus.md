---
schema: 1
kind: incident
title: "Bitget: an attacker exploited a third-party security product to obtain internal credentials, spoofed wallet-authorization data, and stole $388M in one of 2026's largest crypto-exchange hacks"
headline: "A compromised third-party security tool, not a private-key theft, let an attacker forge Bitget's own withdrawal approvals"
summary: >
  Cryptocurrency exchange Bitget confirms unauthorized transfers of approximately $388M from its hot and warm
  wallet infrastructure on 2026-09-24, after an attacker exploited a vulnerability in a third-party security
  product to obtain high-level internal credentials and spoof wallet-authorization data. Bitget's CEO calls
  North Korean involvement "very likely"; TRM Labs finds the laundering infrastructure overlaps wallets used
  in the 2025 Bybit and AFX Bridge hacks, both linked to the DPRK-nexus TraderTraitor cluster, but states
  attribution is not definitive.
discovered_at: "2026-09-29T05:15:00Z"
updated_at: null
event_date: "2026-09-24"
run_id: 2026-09-29T0405Z-intel
priority: high
immediate_action: null
tags: [organized-crime, north-korea-nexus, cryptocrime]
regions: [global]
sectors: [finance]
entities: ["incident:bitget-hot-wallet-theft-2026-09", "actor:jade-sleet"]
techniques: [T1078, T1565.002, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response"
    publisher: "Bitget (official incident page)"
    date: "2026-09-27"
    role: primary
  - url: "https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack"
    publisher: "TRM Labs"
    date: "2026-09-25"
    role: primary
  - url: "https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html"
    publisher: "The Hacker News"
    date: "2026-09-28"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html"
    publisher: "The Hacker News"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials"
    publisher: "Bitget (official incident page)"
    source_url: "https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response"
  - quote: "The attacker compromised a critical backend system within our wallet infrastructure, used it to spoof transaction data, and triggered our authorization process to move funds out."
    publisher: "Bitget CEO Gracy Chen, via The Hacker News"
    source_url: "https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html"
  - quote: "these onchain links confirm the group laundering these proceeds is the same one used by TraderTraitor in other recent hacks"
    publisher: "TRM Labs"
    source_url: "https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack"
verification: multi-source
sourcing_note: >
  Bitget's own incident page and TRM Labs' independent on-chain forensic analysis are both primary. TRM Labs
  is explicit that attribution is assessed, not confirmed: "TRM has not yet definitively attributed the
  exploit to North Korea" and "another actor carrying out the theft remains technically possible." No formal
  attribution relation to the TraderTraitor cluster was recorded given that explicit hedge.
confidence: high
references: ["2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop"]
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

Cryptocurrency exchange Bitget confirms that, at 18:31 UTC on 2026-09-24, unauthorized transfers occurred from a portion of its hot and warm wallet infrastructure across eleven blockchains: Ethereum, XRP Ledger, TRON, Arbitrum, Optimism, Base, BNB Smart Chain, Avalanche, Algorand, Celestia and Zcash ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)). Per Bitget's own investigation, the attacker did not steal a private key: "the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials," then used those credentials "to impersonate authorized activity and send fraudulent withdrawal commands to the wallet system," bypassing existing risk controls ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)). CEO Gracy Chen described the mechanism directly: "The attacker compromised a critical backend system within our wallet infrastructure, used it to spoof transaction data, and triggered our authorization process to move funds out" ([The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html)). Bitget states private-key compromise was ruled out and cold wallets were unaffected; the vulnerable third-party product's vendor was notified and the affected functionality disabled pending a fix.

Total loss is now estimated at approximately $388M, revised up from an initial roughly $351.6M on-chain estimate, across twelve wallet addresses. Bitget's approximately $464M User Protection Fund will cover the loss, customer account balances, deposits and trading were unaffected, and withdrawals, paused at detection, resumed in phases starting with Bitcoin on 2026-09-28. Bitget revoked and reissued internal login credentials, restructured access to highly sensitive systems, now requires multiple approvals for critical operations, and engaged Mandiant and SlowMist for independent forensics ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)).

Bitget's CEO called North Korean involvement "very likely," based on the team's preliminary investigation linking observed IP addresses to VPN services associated with a North Korean hacking group ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). TRM Labs, an independent blockchain-forensics firm, reports that on-chain tracing shows the wallets laundering Bitget's stolen funds overlap with wallets previously used to launder proceeds from the 2025 Bybit and AFX Bridge hacks, both attributed to the DPRK-linked TraderTraitor cluster (also known as UNC4899/PUKCHONG): "these onchain links confirm the group laundering these proceeds is the same one used by TraderTraitor in other recent hacks" ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). TRM is explicit that this stops short of definitive attribution: "TRM has not yet definitively attributed the exploit to North Korea" and "another actor carrying out the theft remains technically possible."

**Defender takeaway:** the transferable lesson is architectural rather than crypto-specific: a third-party security product with high-privilege internal access became the attack path into a system its presence was meant to protect. Any organization granting a third-party product credential-level or authorization-bypassing access to a high-value backend, a wallet-signing system, a payment-authorization system, or an equivalent control plane, should treat that product's own supply chain and patch status as part of the protected system's own attack surface, not as a trusted external dependency, and require multiple independent approvals for high-value transaction authorization so that a single compromised credential cannot alone trigger a transfer.
