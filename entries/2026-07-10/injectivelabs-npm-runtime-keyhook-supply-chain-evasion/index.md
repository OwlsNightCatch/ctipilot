---
schema: 1
kind: research
title: "npm supply-chain payload hides as runtime 'telemetry' with no install hook — defeating install-time dependency scanners"
headline: "Aikido: compromised @injectivelabs npm package hooks key-derivation at runtime, carries no postinstall script, and exfiltrates disguised as normal SDK traffic"
summary: >
  Aikido Security dissected a malicious npm release of @injectivelabs/sdk-ts (~50k weekly downloads)
  whose stealer runs no install-time (postinstall) script at all — so install-time scanners and
  sandboxes that only watch lifecycle scripts saw a clean package. Instead it inserts one-line hooks
  into the SDK's own key-derivation functions that fire on every legitimate call at runtime, encodes
  the captured secret to defeat plaintext string search, and exfiltrates it inside a request header
  crafted to mimic the SDK's normal API traffic. The attacker also republished the poisoned version
  number across 17 sibling packages so dependents pulled it transitively. The transferable lesson is
  the evasion pattern, not the crypto package: runtime-triggered credential hooking blinds the
  install-time SCA scanning most dependency-security programmes rely on.
discovered_at: "2026-07-10T12:53:00Z"
event_date: "2026-06-08"
run_id: 2026-07-10T1228Z-intel
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
regions:
  - global
sectors:
  - public-sector
  - finance
  - technology
entities:
  - incident:injectivelabs-npm-sdk-ts-supply-chain-2026
techniques: [T1195.002, T1056.004, T1132.001, T1041]
affected_products: ["@injectivelabs/sdk-ts (npm)"]
cves: []
sources:
  - url: "https://www.aikido.dev/blog/compromised-injectivelabs-exfiltrates-keys"
    publisher: "Aikido Security"
    date: "2026-07-09"
    role: primary
closed_sources: []
evidence:
  - quote: "Because the trigger is key derivation at runtime and not a lifecycle script, install-time scanners and sandboxes that only watch postinstall see a clean package."
    publisher: "Aikido Security"
  - quote: "Each hook fires before the real derivation runs, so the secret is captured on every legitimate call"
    publisher: "Aikido Security"
  - quote: "The malicious `1.20.21`was published at 22:59 GMT+2 on June 8, 2026, the maintainer reverted the change at 23:18, and a clean version was published at 23:48."
    publisher: "Aikido Security"
verification: single-source
sourcing_note: >
  Single-source (Aikido Security, a dependency-security research vendor — reliability B). The
  underlying compromise (2026-06-08) was contained by the maintainer within ~50 minutes; this Aikido
  write-up (2026-07-09) is the first public technical teardown and the in-window signal. No independent
  corroboration located in-window; included on the strength of the primary technical analysis of a
  transferable evasion technique. Classification B2.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Do not treat a clean install-time (postinstall) scan as sufficient for npm dependencies — this payload had no lifecycle hook. Add build-artifact-vs-source diffing (compare the shipped dist/ output against the repository source) to catch code injected only into the compiled artifact."
  - "Audit transitive dependencies, not just direct ones: 17 of the 18 affected packages carried no malicious code of their own but pinned the poisoned SDK, so a project could pull the stealer without ever naming it. Pin exact versions and verify via build provenance/attestation (npm provenance, Sigstore) rather than trusting the registry alone."
  - "Add runtime egress monitoring for dependency processes making outbound calls to hosts that merely resemble a vendor's real API domain, and for unusual data carried in custom HTTP request headers rather than the body."
migrated_from: null
---

Aikido Security published (2026-07-09) a teardown of a compromised npm release of **@injectivelabs/sdk-ts** — an SDK pulling ~50,000 weekly downloads — that is notable less for its payload's purpose than for how it hid ([Aikido Security, 2026-07-09](https://www.aikido.dev/blog/compromised-injectivelabs-exfiltrates-keys)). Introduced via what Aikido assesses as a GitHub account takeover (commits from an account with an established history), the malicious version was live for under an hour on 2026-06-08 before the maintainer reverted it, but in that window the attacker also republished the same version number across 17 other packages in the scope, each pinning the poisoned SDK — so any project depending on one of them resolved the stealer transitively without naming it directly.

The payload runs no install-time script. Diffed against the clean build, the artifacts differ by one injected block and two one-line hooks placed inside the SDK's own key-derivation entry points; each hook "fires before the real derivation runs, so the secret is captured on every legitimate call" during normal application use ([Aikido, 2026-07-09](https://www.aikido.dev/blog/compromised-injectivelabs-exfiltrates-keys)). Because "the trigger is key derivation at runtime and not a lifecycle script, install-time scanners and sandboxes that only watch postinstall see a clean package" — the single most important detail for defenders, since it defeats the exact control (install-hook / postinstall inspection) that most software-composition-analysis programmes lean on. The exfiltration was built to blend in: the destination host was stored as an array of character codes and reassembled at runtime to defeat plaintext string search, the captured material was base64-batched and sent inside an HTTP request header (not the body) with a content type matching the SDK's own gRPC-web API calls, and every failure path swallowed errors silently. The injected block was even documented in its own comment as "anonymized usage metrics for SDK optimization".

**Defender takeaway:** the specific package is blockchain-wallet tooling with limited public-sector footprint, but the tradecraft generalises to any npm consumer — a supply-chain payload that carries no lifecycle hook, triggers only on genuine runtime use of the library's own API, and exfiltrates over a channel shaped like the library's normal traffic will pass install-time scanning and plaintext IOC search. The durable controls are artifact-vs-source diffing, transitive-dependency auditing with pinned versions and build provenance, and runtime egress monitoring keyed on protocol-mimicking destinations rather than known-bad strings.
