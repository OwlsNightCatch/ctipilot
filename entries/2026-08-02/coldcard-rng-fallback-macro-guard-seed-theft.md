---
schema: 1
kind: vulnerability
horizon: operational
title: "COLDCARD: a preprocessor guard that tested whether a macro was defined rather than what it was set to routed key generation to a software PRNG for five years, and the keys are now being emptied"
headline: "A build-time macro check silently disabled a hardware TRNG in shipped firmware, and the vendor assumes an AI code review is what found it"
summary: >
  Coinkite has disclosed that a 2021 migration in its COLDCARD hardware-wallet firmware bound key generation to
  MicroPython's software PRNG instead of the intended hardware TRNG, because the guarding preprocessor directive
  tested whether the enabling macro was defined rather than whether its value was non-zero — and the vendor had
  set it to zero. The defect survived five years and an AI-assisted code review the vendor ran weeks ago, and is
  now under mass exploitation: Galaxy Research puts the running total at 1,367.05 BTC across 4,585 addresses.
  The transferable finding is an assurance failure, not a crypto failure — review confirmed the correct code was
  in the binary but never confirmed which implementation the key-generation path actually reached.
discovered_at: "2026-08-02T04:09:57Z"
event_date: "2026-07-30"
run_id: 2026-08-02T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cryptocrime, actively-exploited, supply-chain, patch-available]
regions: [global]
sectors: [finance, technology]
entities: [incident:coldcard-rng-fallback-seed-theft-2026]
techniques: [T1110, T1657]
affected_products: ["Coinkite COLDCARD Mk2", "Coinkite COLDCARD Mk3", "Coinkite COLDCARD Mk4", "Coinkite COLDCARD Mk5", "Coinkite COLDCARD Q"]
cves: []
sources:
  - url: "https://blog.coinkite.com/entropy-technical-backgrounder/"
    publisher: "Coinkite"
    date: "2026-07-30"
    role: primary
  - url: "https://www.cryptotimes.io/2026/08/02/coldcard-hack-tops-88-6m-as-galaxy-finds-third-attack-wave/"
    publisher: "CryptoTimes"
    date: "2026-08-01"
    role: corroborating
  - url: "https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware"
    publisher: "Block Engineering"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The guard used #ifndef, which tests whether MICROPY_HW_ENABLE_RNG is defined, rather than whether its value is nonzero. We defined that macro as zero, so the #error did not stop the build."
    publisher: "Coinkite"
  - quote: "Existing review confirmed that the intended TRNG implementation was present in the firmware binary, but did not verify which rng_get() implementation the wallet seed-generation path actually reached across the two submodules."
    publisher: "Coinkite"
  - quote: "The COLDCARD source code has always been open and publicly available, so we have to assume that someone used AI to review previous versions of our firmware and stumbled upon this issue. A few weeks ago, we used one of the best available AI models to review our code for security issues, and it did not find this bug or anything serious."
    publisher: "Coinkite"
verification: multi-source
sourcing_note: >
  The root cause, the affected version ranges, the entropy estimates and the AI-discovery assumption are all
  Coinkite's own account of its own product. Block Engineering's independent reverse-engineering is cited as
  corroboration of the same defect class. The theft figures are Galaxy Research's estimates as relayed by
  CryptoTimes; Galaxy's own post was not fetched, so the numbers are attributed to that relay and stated as
  estimates.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

This is out of the constituency's usual nexus — a consumer Bitcoin hardware wallet, not public-sector or critical-infrastructure equipment — and is carried on two grounds: the confirmed scale of exploitation now under way (a running estimate of 1,367.05 BTC across 4,585 addresses over three waves), and a root cause that is an embedded-firmware assurance anti-pattern applying to any device whose cryptographic quality depends on a build-time switch.

In 2021 Coinkite moved COLDCARD's elliptic-curve operations onto Bitcoin Core's libsecp256k1, which required adding an embedded MicroPython library, and during that migration wallet-seed generation moved from the vendor's own `ckcc.rng_bytes()` to `ngu.random.bytes()`. That path resolved `rng_get()` to MicroPython's software fallback rather than COLDCARD's hardware RNG implementation ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)). The reason nothing broke is the part worth reading twice: "The guard used #ifndef, which tests whether MICROPY_HW_ENABLE_RNG is defined, rather than whether its value is nonzero. We defined that macro as zero, so the #error did not stop the build." — and because the fallback provided a function with the same signature as the intended implementation, "the build completed without identifying the wrong implementation" ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)). The vendor's own summary of why review missed it is the generalisable finding: "Existing review confirmed that the intended TRNG implementation was present in the firmware binary, but did not verify which rng_get() implementation the wallet seed-generation path actually reached across the two submodules." ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)).

The consequence is a reduced key search space rather than a leaked key. On Mk2 and Mk3 the active PRNG was seeded primarily from device and timing state, and Coinkite estimates the effective search space at about 40 bits; Mk4, Mk5 and Q mixed in entropy from two secure elements as a backup, which it estimates leaves about 72 bits. The vendor labels both as preliminary estimates under current attack assumptions that may change as analysis continues, and states plainly that for funded wallets without either at least 50 independent private dice rolls or a strong unique passphrase, "the reduced search space is a direct security risk, not a theoretical possibility" ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)). Block Engineering reached the same defect independently, framing it as a predictable RNG fallback compounded by a 32-bit reseed ([Block Engineering, 2026-07-30](https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware)). The affected Mk2/Mk3 firmware range is 4.0.1 through 4.1.9, corrected in 4.2.0; the other fixed builds are 5.6.0 for Mk4 and Mk5, 1.5.0Q for Q, and Edge releases 6.6.0X and 6.6.0QX. Updating does not repair a seed generated by affected firmware — those seeds must be replaced and funds migrated ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)).

Exploitation is live and escalating. Galaxy Research reported a third wave on 2026-08-01 in which a further 207.7294 BTC was drained, putting its estimate of the total at 1,367.05 BTC across 4,585 addresses; it assesses waves 1 and 2 as likely one operator on shared collector addresses and identical destination-address types roughly 27 hours apart, while wave 3 used per-victim destination addresses, a different output type, batched victims and only the default derivation path — differences Galaxy says could mean either new evasion tradecraft from the same actor or a second actor exploiting the same flaw. All the attacker-controlled funds remain unspent, which Galaxy calls unusual for a theft of this size, and every compromised address was created after the vulnerable firmware shipped in March 2021 ([CryptoTimes, 2026-08-01](https://www.cryptotimes.io/2026/08/02/coldcard-hack-tops-88-6m-as-galaxy-finds-third-attack-wave/)).

The discovery route is the vendor's assumption, not an established fact, and it cuts in two directions at once. Coinkite writes that because its source has always been public, "we have to assume that someone used AI to review previous versions of our firmware and stumbled upon this issue" — and in the same paragraph that "A few weeks ago, we used one of the best available AI models to review our code for security issues, and it did not find this bug or anything serious.", concluding that "Both attackers and defenders have the same AI tools, but today it did not help us, and only helped the bad guys." ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)). No source establishes how the flaw was actually found.

**Defender takeaway:** for anyone responsible for embedded or operational-technology firmware assurance in the energy, water, transport or healthcare estates this pipeline covers, the reusable control is a build-time reachability check rather than a code review. Coinkite's own hotfix is the pattern: the build now fails unless the board-specific object defines the global `rng_get()` symbol and the upstream fallback object defines none ([Coinkite, 2026-07-30](https://blog.coinkite.com/entropy-technical-backgrounder/)). Two review criteria generalise directly — a preprocessor guard on a security-relevant macro must test the macro's *value*, not merely its presence, and any assurance claim about a cryptographic primitive must be evidenced by end-to-end symbol resolution from the calling path, not by confirming the intended implementation is somewhere in the binary. Where two implementations share a function signature, the compiler will not tell you which one shipped.
