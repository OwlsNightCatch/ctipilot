---
schema: 1
kind: threat
title: "THORChain vault drain, about $10.7M from one vault: a newly joined validator exploited GG20 threshold signing (Switzerland-based protocol)"
headline: "Switzerland-based THORChain lost about $10.7M when a newly joined validator broke its GG20 threshold signing"
summary: "THORChain, a Switzerland-based cross-chain liquidity protocol, lost about $10.7M on 2026-05-15 from one of its five vaults by its own count (The Record reported one of six vaults, TRM Labs more than USD 11M across nine chains). THORChain says a validator churned in two days earlier exploited its GG20 threshold-signature implementation: a malformed multi-prime Paillier key planted at setup and 864 deliberately failed signing rounds leaked other validators' key shares until the attacker could sign alone, a chain of three weaknesses in its fork of Binance's tss-lib that upstream had fixed by 2024. THORChain said initial indications were that only protocol-owned funds were affected, and TRM Labs had not attributed the theft as of 2026-05-15."
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
techniques: [T1212, T1657]
cves: []
sources:
  - url: "https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain"
    publisher: "The Record"
    date: "2026-05-15"
    role: primary
  - url: "https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now"
    publisher: "TRM Labs"
    date: "2026-05-15"
    role: corroborating
  - url: "https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/"
    publisher: "CryptoTimes"
    date: "2026-05-17"
    role: corroborating
  - url: "https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report"
    publisher: "Fireblocks"
    date: "2023-08-09"
    role: corroborating
  - url: "https://www.verichains.io/tsshock/"
    publisher: "Verichains"
    date: "2023-08-10"
    role: corroborating
  - url: "https://blog.thorchain.org/thorchain-exploit-report-1"
    publisher: "THORChain (Exploit Report #1)"
    date: "2026-05-20"
    role: primary
  - url: "https://blog.thorchain.org/thorchain-exploit-report-2"
    publisher: "THORChain (Exploit Report #2, post-mortem)"
    date: "2026-07-03"
    role: primary
closed_sources: []
evidence:
  - quote: "THORChain officials said the investigation into the incident is ongoing but explained that one of their six vaults was compromised, leading to a loss of about $10.7 million."
    publisher: The Record
  - quote: "At the time of writing, TRM has not attributed the May 15 exploit to any specific actor."
    publisher: TRM Labs
  - quote: "the operator (or a compromised machine acting as the operator) exploited a vulnerability in the GG20 Threshold Signature Scheme implementation. Rather than a single dramatic key compromise, the attack appears to have involved the gradual leakage of vault key material during keygen or signing rounds — the kind of malformed-proof exploitation that the TSSHOCK class of CVEs first put on the industry's radar a few years ago."
    publisher: CryptoTimes
  - quote: "On May 15, 2026, THORChain was the victim of a targeted exploit that drained approximately $10.7M from a single vault (out of five)."
    publisher: THORChain
    source_url: "https://blog.thorchain.org/thorchain-exploit-report-1"
  - quote: "The attacker was a newly churned node operator who entered the network two days prior and exploited a vulnerability in the GG20 Threshold Signature Scheme."
    publisher: THORChain
    source_url: "https://blog.thorchain.org/thorchain-exploit-report-1"
  - quote: "After 864 repetitions over two and a half days, the attacker had accumulated enough material to sign transactions unilaterally, bypassing TSS."
    publisher: THORChain
    source_url: "https://blog.thorchain.org/thorchain-exploit-report-2"
  - quote: "The only thing that reveals the pattern is the aggregate: a single validator responsible for a wildly disproportionate share of signing failures over a short period of time."
    publisher: THORChain
    source_url: "https://blog.thorchain.org/thorchain-exploit-report-2"
verification: multi-source
sourcing_note: >
  THORChain is the victim and the source of the loss figure, the vault count and the exploit mechanics; The Record (six vaults) and TRM Labs (more than USD 11M)
  give different figures from the early reporting, and the Chainalysis funding trail is cited from CryptoTimes' account of it.
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
  - at: "2026-10-20T08:46:34Z"
    run_id: 2026-10-20T0835Z-audit
    type: correction
    summary: >
      THORChain's own reports count one of five vaults drained for about $10.7M (later about $10M), not
      the six vaults and about $11M taken from The Record and TRM Labs, and confirm the GG20
      threshold-signature exploit that had been described as suspected. The analysis is rewritten from
      THORChain's post-mortem of 2026-07-03, which describes a malformed multi-prime Paillier key and 864
      deliberately failed signing rounds, with exposure, detection and triage guidance for other GG20
      deployments.
    fields: [body, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

On 2026-05-15 an attacker drained about $10.7M from one of THORChain's five vaults, and the other four were unaffected ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)); THORChain's post-mortem of 2026-07-03 puts the loss at about $10M ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)). The Record reported one of six vaults and about $10.7M ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain)), and TRM Labs more than USD 11M across nine chains ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). THORChain, a cross-chain liquidity protocol founded in 2018 and based in Switzerland, said initial indications were that user funds were safe and only protocol-owned funds were affected ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain)).

THORChain confirmed on the evening of 2026-05-15 that the attack exploited its GG20 threshold-signature (TSS) implementation to leak key material progressively, and that the attacker was a node operator churned into the validator set two days earlier ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)). Its post-mortem describes the chain: at vault setup the attacker published a Paillier key built from several small primes instead of two large ones, which passed because the library only screened out a handful of tiny factors; it then deliberately failed the MTA step of signing 864 times over two and a half days, each failure looking like routine node flakiness while leaking a fragment of other validators' key shares, until it could sign outbound transactions alone ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)). Two further weaknesses made the leak deterministic, a range proof whose two halves were never tied together and a blinding value drawn from far too small a range; all three sat in THORChain's fork (v0.1.6) of Binance's tss-lib, which upstream had fixed as individually minor issues in v2.0.0 (August 2023) and v3.0.0 (2024) ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)). THORChain says only the Paillier-modulus condition matches public research, the class documented in 2023 as BitForge and TSSHOCK ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)); the 2023 disclosures include Fireblocks' CVE-2023-33241 on unchecked Paillier moduli ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report)) and Verichains' TSSHOCK attacks on threshold-signing proofs and their encoding ([Verichains, 2023-08-10](https://www.verichains.io/tsshock/)).

The solvency checker halted signing and trading on several chains within about 52 minutes, but only after the funds had left, because the attacker signed with the reconstructed key ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)). Chainalysis traced attacker-linked funds through Monero, Hyperliquid and Arbitrum from late April, including the ETH that bonded the malicious validator, CryptoTimes reports ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). TRM Labs had not attributed the theft to any actor as of 2026-05-15, while calling THORChain the bridge of choice for laundering North Korea's largest thefts ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)). Every validator has since upgraded to v3.19.1, and THORChain plans to replace GG20 with DKLS or Schnorr-based signing ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)).

**Exposure:** ECDSA threshold-signing deployments running GG20 code derived from Binance's tss-lib from before its v2.0.0 and v3.0.0 fixes, wherever a party that could be malicious joins the signing committee, which on THORChain is anyone who bonds a validator; EdDSA signing, as on Solana, is not exposed ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)).

**Detection:** per-participant signing-protocol telemetry: THORChain names a single validator responsible for a disproportionate share of signing failures over a short period as the signal it missed, and is adding monitoring of key-sign failures per validator ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)). Balance-based solvency checks fire only after the funds move once the key has been rebuilt ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)).

**Triage:** failed signing rounds are routine, since validators go offline or miss timing windows; the discriminator is the aggregate, one recently admitted participant failing the same signing step far more often than its peers over days ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)).

**Defender takeaway:** for any GG20 threshold-signing deployment built on tss-lib, confirm the library carries tss-lib's v2.0.0 and v3.0.0 fixes, including verification that each party's Paillier modulus is well formed, and alert on each participant's share of signing failures ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)). Organisations without threshold-signing infrastructure have no decision to make.

## Correction — 2026-09-30T07:16:56Z

The analysis above described CVE-2023-33241 as part of the TSSHOCK class. CVE-2023-33241 is Fireblocks' GG18/GG20 Paillier-key disclosure ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report)), and TSSHOCK is Verichains' separate set of key-extraction attacks ([Verichains, 2023-08-10](https://www.verichains.io/tsshock/)). Fireblocks' flaw lies in an unchecked Paillier modulus, which it recommends detecting with a suitable zero-knowledge proof, while TSSHOCK exploits weak or insecurely implemented zero-knowledge proofs. Both let a single malicious participant extract key material ([Fireblocks, 2023-08-09](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report); [Verichains, 2023-08-10](https://www.verichains.io/tsshock/)).

The account of the attack above was also narrowed to its sources. The Record reports a compromised vault. The malicious validator node was the vector THORChain's first incident update confirmed, according to CryptoTimes, and the GG20 flaw was then the working theory CryptoTimes reported, supported by PeckShield, Cyvers and security teams working with THORChain rather than Chainalysis ([CryptoTimes, 2026-05-17](https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/)). TRM Labs calls THORChain the bridge of choice for laundering North Korea's largest thefts without naming the Lazarus Group or saying such activity dominates ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)).

## Correction — 2026-10-20T08:46:34Z

The loss came from one of THORChain's five vaults, not six, and THORChain puts it at about $10.7M ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)) and in its post-mortem at about $10M ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)); six vaults is The Record's figure ([The Record, 2026-05-15](https://therecord.media/more-than-10-million-stolen-crypto-platform-thorchain)) and more than USD 11M is TRM Labs' ([TRM Labs, 2026-05-15](https://www.trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now)), so the six vaults and about $11M stated earlier came from those outlets, not from THORChain. The GG20 flaw was not a suspicion: THORChain confirmed on 2026-05-15 that the attack exploited its GG20 TSS implementation to leak key material progressively ([THORChain, 2026-05-20](https://blog.thorchain.org/thorchain-exploit-report-1)), and its post-mortem of 2026-07-03 sets out the exploit chain, a malformed multi-prime Paillier key and 864 deliberately failed signing rounds combined with two further weaknesses in its tss-lib fork ([THORChain, 2026-07-03](https://blog.thorchain.org/thorchain-exploit-report-2)).
