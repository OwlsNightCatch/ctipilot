---
schema: 1
kind: threat
title: "THORChain vault drain, about $11M across nine chains, GG20 Threshold Signature Scheme flaw suspected (Switzerland-based protocol)"
headline: "Switzerland-based THORChain loses about $11M across nine chains from a compromised vault, with a GG20 TSS flaw the reported working theory"
summary: "THORChain, a Switzerland-based cross-chain liquidity protocol, lost about $11M across nine blockchains after one of its six vaults was compromised (The Record, 2026-05-15; TRM Labs, 2026-05-15). CryptoTimes reports that THORChain's first incident update confirmed a malicious, newly churned validator node as the vector, and that the working theory is a GG20 Threshold Signature Scheme implementation flaw through which that node gradually leaked vault key material over keygen and signing rounds before forging outbound signatures (CryptoTimes, 2026-05-17). THORChain said initial indications were that user funds were safe and only protocol-owned funds were affected (The Record, 2026-05-15)."
discovered_at: "2026-05-18T05:00:00Z"
event_date: 2026-05-15
run_id: 2026-05-18-2eabc1cf
priority: notable
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
techniques: [T1657]
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
  - url: "https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report"
    publisher: "Fireblocks"
    date: "2023-08-09"
    role: corroborating
  - url: "https://www.verichains.io/tsshock/"
    publisher: "Verichains"
    date: "2023-08-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "THORChain officials said the investigation into the incident is ongoing but explained that one of their six vaults was compromised, leading to a loss of about $10.7 million."
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
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-18.md
updates:
  - at: "2026-09-30T07:16:56Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      CVE-2023-33241 is Fireblocks' own finding and TSSHOCK is Verichains' separate set of attacks,
      so the text names both with their own sources, describes each weakness as its source does, and
      drops an unsupported claim that this was a second large-scale production case. The title, headline, summary
      and main text give the malicious node as the vector THORChain's first incident update
      confirmed and the GG20 flaw as the working theory CryptoTimes reports, and no longer credit
      Chainalysis for it or name the Lazarus Group. The node address is removed as an indicator, the
      event date moves to the 2026-05-15 drain, and the priority moves from high to notable because
      a crypto-protocol vault drain asks no decision of Swiss public bodies within seven days. An
      uncited relevance paragraph is replaced by a cited takeaway, which sets CryptoTimes' view of
      CGGMP21 against Verichains' findings.
    fields: [sources, body, classification, techniques, summary, evidence, event_date, priority, title, headline]
---

On 2026-05-15 an attacker drained approximately $11M, by THORChain's initial indications protocol-owned funds only, from [THORChain](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain), a Switzerland-based decentralised cross-chain liquidity protocol founded in 2018, after one of its six vaults was compromised, across Bitcoin, Ethereum, BNB Smart Chain, Base, Avalanche, Dogecoin, Litecoin, Bitcoin Cash, and XRP ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain); [TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). The leading technical hypothesis, supported by analysis from PeckShield, Cyvers and security teams collaborating with THORChain's core developers according to [CryptoTimes's post-mortem synthesis on 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/), is a GG20 Threshold Signature Scheme (TSS) implementation flaw: a validator node that had joined the active set only days before the attack is flagged as the likely entry point, suspected of gradually leaking vault key shards during keygen and signing rounds until enough key material could be reconstructed offline to forge outbound vault signatures without triggering normal quorum checks ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). THORChain's Incident Update #1 on 2026-05-16 confirmed the malicious-node vector, CryptoTimes reports ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). CryptoTimes records verbatim: *"the operator (or a compromised machine acting as the operator) exploited a vulnerability in the GG20 Threshold Signature Scheme implementation. Rather than a single dramatic key compromise, the attack appears to have involved the gradual leakage of vault key material during keygen or signing rounds — the kind of malformed-proof exploitation that the TSSHOCK class of CVEs first put on the industry's radar a few years ago."* Chainalysis shared an on-chain analysis thread on 2026-05-16 linking attacker-controlled wallets to weeks of preparatory infrastructure staging through Monero and Hyperliquid before the vault drain ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). TRM Labs traced the proceeds to a two-address cluster within hours but has not attributed the exploit to any specific actor as of disclosure ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). TRM notes that THORChain has become the bridge of choice for laundering North Korea's largest thefts, including the $1.5B Bybit and nearly $300M KelpDAO hacks, but no North Korean attribution is confirmed for this event ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). THORChain said initial indications were that user funds were safe and only protocol-owned funds were affected ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain)). Two related but separate 2023 disclosures showed that a single malicious participant in GG18/GG20 threshold signing can extract other parties' key material. Fireblocks' CVE-2023-33241 rests on parties not checking that a participant's Paillier modulus is well formed, which Fireblocks recommends detecting with a suitable zero-knowledge proof ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report)). Verichains' TSSHOCK attacks exploit weak or insecurely implemented zero-knowledge proofs, such as ambiguous transcript encoding and a reduced number of proof iterations, in most GG18, GG20 and CGGMP21 implementations by Verichains' account ([Verichains, 2023-08-10](https://www.verichains.io/tsshock/)). If the working theory holds, the THORChain exploit is that class of weakness in production, though CryptoTimes says only that the attack "appears to have involved" key-material leakage ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)).

**Defender takeaway:** for any threshold-signing, MPC-custody or cross-chain validator deployment, the question this incident raises is whether a newly admitted node gets the same signing trust as an established one. CryptoTimes points to validator vetting, hardware isolation and the churn-process assumption that a node that has just joined the active set deserves the same trust as one running cleanly for months, and notes that newer protocols such as CGGMP21 offer stronger guarantees against malformed-proof attacks ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). Verichains, however, found most CGGMP21 implementations vulnerable to its TSSHOCK attacks, as it did most GG18 and GG20 ones ([Verichains, 2023-08-10](https://www.verichains.io/tsshock/)).

## Correction — 2026-09-30T07:16:56Z

The analysis above described CVE-2023-33241 as part of the TSSHOCK class. CVE-2023-33241 is Fireblocks' GG18/GG20 Paillier-key disclosure ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report)), and TSSHOCK is Verichains' separate set of key-extraction attacks ([Verichains, 2023-08-10](https://www.verichains.io/tsshock/)). Fireblocks' flaw lies in an unchecked Paillier modulus, which it recommends detecting with a suitable zero-knowledge proof, while TSSHOCK exploits weak or insecurely implemented zero-knowledge proofs. Both let a single malicious participant extract key material ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report); [Verichains, 2023-08-10](https://www.verichains.io/tsshock/)).

The account of the attack above was also narrowed to its sources. The Record reports a compromised vault. The malicious validator node is the vector THORChain's first incident update confirmed, according to CryptoTimes, and the GG20 flaw is the working theory CryptoTimes reports, supported by PeckShield, Cyvers and security teams working with THORChain rather than Chainalysis ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). TRM Labs calls THORChain the bridge of choice for laundering North Korea's largest thefts without naming the Lazarus Group or saying such activity dominates ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)).
