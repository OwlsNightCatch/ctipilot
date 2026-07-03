---
schema: 1
kind: threat
horizon: operational
title: "THORChain GG20 Threshold Signature Scheme vault drain — ~$11M across nine chains; Switzerland-based protocol"
headline: "THORChain GG20 Threshold Signature Scheme vault drain — ~$11M across nine chains; Switzerland-based protocol"
summary: "THORChain — Switzerland-based cross-chain liquidity protocol — drained of ~$11M across nine blockchains via a suspected GG20 Threshold-Signature-Scheme implementation flaw. A malicious newly-churned validator node is reported to have gradually leaked vault key shards over multiple keygen/signing rounds before forging outbound signatures; The Record reports user funds were unaffected and only protocol-owned assets were impacted (The Record, 2026-05-15; TRM Labs, 2026-05-15)."
discovered_at: "2026-05-18T05:00:00Z"
event_date: 2026-05-17
run_id: 2026-05-18-2eabc1cf
priority: high
immediate_action: null
tags:
  - cryptocrime
  - organized-crime
  - supply-chain
  - cloud
regions:
  - switzerland
  - global
sectors:
  - finance
entities:
  - "incident:thorchain-gg20-tss-vault-drain-11m-nine-chains-switzerland"
cves: []
sources:
  - url: "https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain"
    publisher: "The Record, 2026-05-15"
    role: primary
  - url: "https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now"
    publisher: "TRM Labs, 2026-05-15"
    role: corroborating
  - url: "https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/"
    publisher: "CryptoTimes, 2026-05-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "One of THORChain's six vaults was compromised, though the platform's automated systems detected abnormal behavior and halted signing activity, preventing further losses. User funds were reportedly unaffected, with only protocol-owned assets impacted."
    publisher: The Record
  - quote: "At the time of writing, TRM has not attributed the May 15 exploit to any specific actor."
    publisher: TRM Labs
  - quote: "the operator (or a compromised machine acting as the operator) exploited a vulnerability in the GG20 Threshold Signature Scheme implementation. Rather than a single dramatic key compromise, the attack appears to have involved the gradual leakage of vault key material during keygen or signing rounds — the kind of malformed-proof exploitation that the TSSHOCK class of CVEs first put on the industry's radar a few years ago."
    publisher: CryptoTimes
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
migrated_from: briefs/2026-05-18.md
---

On 2026-05-15 a malicious validator node drained approximately $11M in protocol-owned funds from [THORChain](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain), a Switzerland-based decentralised cross-chain liquidity protocol founded in 2018, across Bitcoin, Ethereum, BNB Smart Chain, Base, Avalanche, Dogecoin, Litecoin, Bitcoin Cash, and XRP ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain); [TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). The leading technical hypothesis — reported by Chainalysis, PeckShield and Cyvers via [CryptoTimes's post-mortem synthesis on 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/) — is a GG20 Threshold Signature Scheme (TSS) implementation flaw: a node identified as `thor16ucjv3v695mq283me7esh0wdhajjalengcn84q` joined the active validator set days before the attack, gradually leaked vault key shards during keygen and signing rounds, reconstructed sufficient key material offline, and then forged outbound vault signatures without triggering the protocol's quorum checks. CryptoTimes records verbatim: *"the operator (or a compromised machine acting as the operator) exploited a vulnerability in the GG20 Threshold Signature Scheme implementation. Rather than a single dramatic key compromise, the attack appears to have involved the gradual leakage of vault key material during keygen or signing rounds — the kind of malformed-proof exploitation that the TSSHOCK class of CVEs first put on the industry's radar a few years ago."* Chainalysis shared an on-chain analysis thread on 2026-05-16 linking attacker-controlled wallets to weeks of preparatory infrastructure staging through Monero and Hyperliquid before the vault drain. TRM Labs traced the proceeds to a two-address cluster within hours but has not attributed the exploit to any specific actor as of disclosure; historical THORChain laundering activity has been dominated by North Korean operators (Lazarus Group, including the $1.5B Bybit and ~$300M KelpDAO thefts per TRM Labs), but no Lazarus attribution is confirmed for this event. The Record reports user balances were not directly drained. **Why it matters to us:** the relevance to a Swiss / EU public-sector SOC is the *technique class*, not the cryptocurrency context. Any organisation operating MPC-custody, threshold-signing, or cross-chain bridge validator infrastructure — including FINMA-supervised digital-asset custodians, EU MiCA-regulated DeFi platforms, and any internal HSM-replacement projects that have moved to MPC-TSS — should audit node-admission controls, keygen/signing-round integrity, and whether newly-joined nodes can participate in signing quorums before completing a full security review. The TSSHOCK vulnerability class — [CVE-2023-33241](https://nvd.nist.gov/vuln/detail/CVE-2023-33241) (Fireblocks GG18/GG20 Paillier-ZK-proof flaw) and related GG20/ECDSA-MPC research — showed that malformed or missing zero-knowledge proofs during GG18/GG20 keygen can leak private-key shards across multiple rounds; the THORChain exploit is the second large-scale production demonstration of that theoretical class.
