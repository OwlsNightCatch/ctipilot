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
  backdoors were delivered. The second-stage backdoor resolves its command-and-control address by
  reading an operator profile's public "website" field from the Nostr decentralized relay network.
discovered_at: "2026-09-21T04:43:00Z"
updated_at: null
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
affected_products: ["Terraform", "macOS"]
cves: []
sources:
  - url: "https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/"
    publisher: "SentinelOne / SentinelLabs"
    date: "2026-09-18"
    role: primary
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
verification: single-source
sourcing_note: >
  SentinelLabs is the sole publisher of this victim and of the campaign's lockfile delivery method,
  which it documents for the lure repositories rather than as this victim's proven initial access. The
  FLATROOF and ROOFDECK backdoors were first documented in the April 2026 LayerZero incident report,
  which is background context rather than corroboration of the new victim.
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
migrated_from: null
---

SentinelLabs hunted its telemetry for the FLATROOF (also known as macOS.Gaslight) and ROOFDECK macOS backdoors first disclosed in April 2026's USD 292 million LayerZero/KelpDAO cryptocurrency theft, and found an unrelated victim carrying the same implants: a small India-based IT-services provider with no cryptocurrency exposure, compromised through a single Apple Silicon MacBook belonging to a DevOps engineer ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)). The lure follows DPRK's established "Contagious Interview" pattern: fake job-interview GitHub repositories themed as infrastructure-engineering coding challenges each carry a weaponized `.terraform.lock.hcl` pointing to a typosquatted, attacker-controlled Terraform provider registry impersonating HashiCorp's own naming. Because Terraform treats the lockfile's declared provider source as authoritative, running `terraform init` against the poisoned lockfile causes Terraform itself to download and execute the attacker's provider module in place of the genuine HashiCorp one. SentinelLabs cannot prove how this victim's backdoors were delivered: both were on disk by March 18, and the victim cloned a lure repository only on April 13 ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).

On the victim host, both backdoors sat dormant on disk from March 18 to March 29, 2026, then launched the moment the developer opened a specific Cursor IDE workspace: the Cursor process itself spawned both implants directly, which began beaconing to their command-and-control servers within two seconds, before FLATROOF stripped the macOS quarantine attribute from ROOFDECK and set its executable bit moments later, a Gatekeeper bypass. FLATROOF is a Rust ARM64 backdoor supporting shell, kill, upload and stop commands, paired with a Python data-harvesting module that pulls Chrome/Brave/Firefox/Safari data, Terminal history, installed-application lists, `ps aux` output, `system_profiler` output and a raw copy of `login.keychain-db`, exfiltrated via a hardcoded Telegram bot. ROOFDECK is the more capable second-stage implant: on first run it queries a public Nostr relay-status API plus a hardcoded relay list, searches Nostr relays for an operator profile matching a configured public key, and reads that profile's "website" field as its live command-and-control URL, a decentralized dead-drop resolver that survives takedown of any single C2 domain. A third stage later replaced both original implants and beaconed intermittently to a separate C2 until 2026-06-01, the last beacon in SentinelLabs' collected telemetry ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).

**Defender takeaway:** any organization whose engineering staff use Terraform or other HashiCorp tooling and could plausibly be approached through fake technical-recruiting outreach should treat an unfamiliar or newly-cloned repository's lockfile as untrusted input — check the source registry a lockfile's providers resolve to before running `terraform init`, since a lockfile can silently redirect a trusted command to attacker infrastructure. Any macOS fleet should alert on `xattr -rd com.apple.quarantine` combined with a `chmod +x` on the same file in immediate succession, and on outbound connections to Nostr relay infrastructure from a host with no legitimate reason to run a Nostr client.

**Triage:** developers legitimately run `terraform init` against new or unfamiliar repositories constantly, so the command itself is not the signal — the discriminator is the lockfile's declared provider source pointing to a domain that is not `registry.terraform.io` or a known private registry the organization operates.

## Correction — 2026-09-30T06:56:18Z

SentinelLabs cannot prove how this victim's backdoors were delivered: both were on disk by March 18 and ran from March 29, while the victim cloned a lure repository only on April 13 ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)). The weaponized Terraform lockfile is the campaign's documented delivery method for its lure repositories, not this victim's proven initial access ([SentinelOne SentinelLabs, 2026-09-18](https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/)).
