---
schema: 1
kind: threat
title: "TraderTraitor (Jade Sleet) backdoors resurface on a non-cryptocurrency IT-services firm in a campaign that delivers malware through weaponized Terraform provider lockfiles, resolving C2 through a Nostr-relay dead drop"
headline: "SentinelLabs: the same DPRK backdoors from a $292M crypto theft resurface on a victim with no crypto ties, in a campaign that uses poisoned Terraform lockfiles"
summary: >
  SentinelLabs found the FLATROOF and ROOFDECK macOS backdoors, first documented in April 2026's
  USD 292 million LayerZero/KelpDAO cryptocurrency theft, on an unrelated victim: a small India-based
  IT-services provider with no cryptocurrency ties. The campaign's fake job-interview GitHub
  repositories carry weaponized Terraform provider lockfiles that redirect `terraform init` to
  attacker-controlled provider registries, though SentinelLabs cannot prove how this victim's
  backdoors were delivered. Zscaler ThreatLabz independently reports a July 2026 trojanized Terraform
  provider binary that runs malicious code as soon as Terraform loads it and delivers the same two families
  on macOS, Linux and Windows, which it suspects is TraderTraitor. The second-stage
  backdoor resolves its command-and-control address by reading an operator profile's public "website"
  field from the Nostr decentralized relay network.
discovered_at: "2026-09-21T04:43:00Z"
updated_at: "2026-10-09T03:54:00Z"
event_date: "2026-09-18"
run_id: 2026-09-21T0410Z-intel
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - infostealer
regions:
  - global
sectors: []
entities:
  - "actor:jade-sleet"
  - "tool:macos-gaslight"
  - "malware:roofdeck"
techniques:
  - T1195.002
  - T1204.002
  - T1553.001
  - T1027
  - T1102.001
  - T1555.001
  - T1005
  - T1119
  - T1567
  - T1059.004
  - T1036.005
  - T1036.008
  - T1027.009
  - T1027.013
  - T1553.002
  - T1055.012
  - T1555.004
  - T1552.003
  - T1539
  - T1546.004
  - T1008
  - T1115
  - T1560.001
  - T1059.006
  - T1071.001
  - T1082
  - T1217
affected_products: ["Terraform", "macOS", "Microsoft Windows", "Linux"]
cves: []
sources:
  - url: "https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/"
    publisher: "SentinelOne / SentinelLabs"
    date: "2026-09-18"
    role: primary
  - url: "https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver"
    publisher: "Zscaler ThreatLabz"
    date: "2026-10-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unlike the previous high-profile victim, this target was a much smaller organization in the IT services industry."
    publisher: "SentinelOne / SentinelLabs"
    source_url: "https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/"
  - quote: "When the victim runs terraform init with the weaponized lockfile in place, Terraform treats the custom provider as the source of truth, resulting in Terraform downloading and executing the malicious provider modules."
    publisher: "SentinelOne / SentinelLabs"
    source_url: "https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/"
  - quote: "When found, it reads the website field of the profile and uses that as its C2 URL."
    publisher: "SentinelOne / SentinelLabs"
    source_url: "https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/"
  - quote: "a trojanized Terraform provider that executes malicious code as soon as Terraform loads the provider"
    publisher: "Zscaler ThreatLabz"
    source_url: "https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver"
verification: multi-source
sourcing_note: >
  SentinelLabs is the sole publisher of this victim and of the campaign's lockfile delivery method,
  which it documents for the lure repositories rather than as this victim's proven initial access.
  Zscaler ThreatLabz independently describes the same two malware families delivered through a
  trojanized provider binary, calls the campaign a suspected TraderTraitor operation and does not
  attribute it with high confidence; it also does not know how its provider reached the victim. The FLATROOF and ROOFDECK
  backdoors were first documented in the April 2026 LayerZero incident report, which is background
  context rather than corroboration of the new victim.
confidence: high
references: ["2026-09-08/sekoia-kudelski-dprk-lazarus-umbrella-six-cluster-split"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:18Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from high to notable: a DPRK developer-targeting
      campaign aimed at crypto firms, not Swiss public bodies. A defanged hostname of the public Nostr
      relay-status service in the text is replaced by a description of the service. The sourcing note is rewritten as plain provenance. The title, headline and
      summary no longer present the weaponized Terraform lockfile as this victim's delivery method:
      SentinelLabs cannot prove how the backdoors arrived, which were on disk weeks before the
      victim cloned a lure repository. An evidence quote is trimmed to drop a relay-service
      hostname. A claim that the third-stage implant went silent is narrowed to SentinelLabs' last
      observed beacon, and attacker-chosen lure repository names are removed.
    fields: [priority, body, sourcing_note, title, headline, summary, evidence]
  - at: "2026-10-09T03:54:00Z"
    run_id: 2026-10-09T0255Z-intel
    type: update
    summary: >
      Zscaler ThreatLabz (2026-10-08) independently reports a July 2026 trojanized Terraform provider binary that executes
      at plugin load and delivers FLATROOF and ROOFDECK on macOS, Linux and Windows, with Telegram, GitHub and webhook
      command channels and a signed Pastebin dead drop alongside the Nostr fallback; the Terraform delivery path now has a
      second form, and the malware family a second publisher.
    fields: [summary, techniques, entities, affected_products, sources, evidence, verification, sourcing_note, body]
migrated_from: null
---

SentinelLabs hunted its telemetry for the FLATROOF (also known as macOS.Gaslight) and ROOFDECK macOS backdoors first disclosed in April 2026's USD 292 million LayerZero/KelpDAO cryptocurrency theft, and found an unrelated victim carrying the same implants: a small India-based IT-services provider with no cryptocurrency exposure, compromised through a single Apple Silicon MacBook belonging to a DevOps engineer ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)). The lure follows DPRK's established "Contagious Interview" pattern: fake job-interview GitHub repositories themed as infrastructure-engineering coding challenges each carry a weaponized `.terraform.lock.hcl` pointing to a typosquatted, attacker-controlled Terraform provider registry impersonating HashiCorp's own naming. Because Terraform treats the lockfile's declared provider source as authoritative, running `terraform init` against the poisoned lockfile causes Terraform itself to download and execute the attacker's provider module in place of the genuine HashiCorp one. SentinelLabs cannot prove how this victim's backdoors were delivered: both were on disk by March 18, and the victim cloned a lure repository only on April 13 ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).

On the victim host, both backdoors sat dormant on disk from March 18 to March 29, 2026, then launched the moment the developer opened a specific Cursor IDE workspace: the Cursor process itself spawned both implants directly, which began beaconing to their command-and-control servers within two seconds, before FLATROOF stripped the macOS quarantine attribute from ROOFDECK and set its executable bit moments later, a Gatekeeper bypass. FLATROOF is a Rust ARM64 backdoor supporting shell, kill, upload and stop commands, paired with a Python data-harvesting module that pulls Chrome/Brave/Firefox/Safari data, Terminal history, installed-application lists, `ps aux` output, `system_profiler` output and a raw copy of `login.keychain-db`, exfiltrated via a hardcoded Telegram bot. ROOFDECK is the more capable second-stage implant: on first run it queries a public Nostr relay-status API plus a hardcoded relay list, searches Nostr relays for an operator profile matching a configured public key, and reads that profile's "website" field as its live command-and-control URL, a decentralized dead-drop resolver that survives takedown of any single C2 domain. A third stage later replaced both original implants and beaconed intermittently to a separate C2 until 2026-06-01, the last beacon in SentinelLabs' collected telemetry ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).

**Defender takeaway:** any organization whose engineering staff use Terraform or other HashiCorp tooling and could plausibly be approached through fake technical-recruiting outreach should treat an unfamiliar or newly-cloned repository's lockfile as untrusted input: check the source registry a lockfile's providers resolve to before running `terraform init`, since a lockfile can silently redirect a trusted command to attacker infrastructure. A provider binary can also be trojanized itself, so restrict untrusted Terraform providers and verify provider checksums ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)). Any macOS fleet should alert on `xattr -rd com.apple.quarantine` combined with a `chmod +x` on the same file in immediate succession, and on outbound connections to Nostr relay infrastructure from a host with no legitimate reason to run a Nostr client.

**Triage:** developers legitimately run `terraform init` against new or unfamiliar repositories constantly, so the command itself is not the signal: the discriminator is the lockfile's declared provider source pointing to a domain that is not `registry.terraform.io` or a known private registry the organization operates.

## Correction — 2026-09-30T06:56:18Z

SentinelLabs cannot prove how this victim's backdoors were delivered: both were on disk by March 18 and ran from March 29, while the victim cloned a lure repository only on April 13 ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)). The weaponized Terraform lockfile is the campaign's documented delivery method for its lure repositories, not this victim's proven initial access ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).

## Update — 2026-10-09T03:54:00Z

Zscaler ThreatLabz reports a July 2026 campaign that it suspects is TraderTraitor, citing substantial overlap in tactics and targeting but no code, infrastructure or cryptographic links sufficient for attribution with high confidence, in which a Go-built Terraform provider that poses as an AWS provider executes malicious code the moment Terraform loads the plugin: it writes a run-once marker in the temporary directory, downloads a Bash loader from a lookalike of a HashiCorp domain, starts it through a detached `sh -c` child and keeps behaving like a normal provider ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)). The loader runs on macOS, Linux and Windows with a Unix-like shell, picks a payload by operating system and CPU architecture and recovers an encrypted executable appended after a marker in a file named like a web font; on macOS it removes the quarantine attribute and applies an ad-hoc signature ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)). The delivered FLATROOF is a Rust backdoor with Telegram Bot API, GitHub-polling and HTTP-webhook command channels, persistence as a service on Linux, a `zlogout` entry on macOS and a registry entry on Windows, and Python stealers for browser data, cookies, keychain or Credential Manager entries, shell history and wallet-extension data; it drops ROOFDECK, which finds its server through a local configuration, then an RSA-signed Pastebin dead drop, with Nostr profile metadata only as the fallback, so its order of resolvers differs from the Nostr-first behaviour SentinelLabs describes above ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)). Zscaler does not know how the provider reached the victim, and notes that SentinelLabs independently reported related activity with weaponized Terraform projects ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)).

The telemetry that follows from the provider path is the Terraform provider plugin process making an HTTPS download from a host that is not the Terraform registry, writing a script to the temporary directory and starting it through `sh -c`; Zscaler advises restricting untrusted Terraform providers, verifying provider checksums and monitoring unexpected process activity ([Zscaler ThreatLabz, 2026-10-08](https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)).
