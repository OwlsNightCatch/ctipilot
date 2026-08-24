---
schema: 1
kind: threat
horizon: operational
title: "A hijacked crates.io account added the first dependency arrayref has taken in ten years, and that dependency ran a backdoor at compile time — every machine that built an affected project during a ninety-minute window must be treated as compromised"
headline: "Build scripts execute before the crate's own code, so `cargo build` was the whole exploit; Wiz ties the infrastructure to two DPRK-linked npm campaigns"
summary: >
  On 2026-08-20 an attacker holding a compromised crates.io publisher account pushed malicious versions
  of three widely used Rust crates — arrayref, internment and append-only-vec — each declaring a new
  build-time dependency on a freshly published typosquat impersonating the standard proc-macro2 crate.
  That dependency's build script runs automatically during compilation, before any of the parent
  crate's own code, so building an affected project was sufficient to execute the payload: it
  reconstructs a command-and-control URL from encoded fragments, disables certificate validation for
  its own callback, and downloads a platform-specific implant for Linux, Windows and macOS that
  persists via a registry run key, a launch agent or a user systemd service and falls back to a domain
  generation algorithm if its primary channel is unreachable. The Rust Security Response Team removed
  everything within 86 to 107 minutes per crate and locked the account, and states it does not believe
  the maintainer acted maliciously. Wiz reports the infrastructure substantially overlaps operations
  attributed to North Korean actors.
discovered_at: "2026-08-23T05:08:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: high
immediate_action: null
tags: [supply-chain, nation-state, infostealer, north-korea-nexus]
regions: [global, europe]
sectors: [public-sector, finance, telco, technology]
entities: [actor:sapphire-sleet, campaign:rust-crates-arrayref-dprk-overlap-2026-08, campaign:mastra-easy-day-js-supply-chain]
techniques: [T1195.002, T1547.001, T1543.001, T1543.002, T1217, T1140, T1568.002]
affected_products: ["arrayref (Rust crate)", "internment (Rust crate)", "append-only-vec (Rust crate)"]
cves: []
sources:
  - url: "https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/"
    publisher: "The Rust Project (Rust Security Response Team)"
    date: "2026-08-20"
    role: primary
  - url: "https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns"
    publisher: "Wiz Research"
    date: "2026-08-20"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/"
    publisher: "Microsoft Security Blog"
    date: "2026-06-17"
    role: corroborating
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package"
    publisher: "Google Threat Intelligence Group"
    date: "2026-03-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On August 20, 2026, malicious versions of three Rust crates were published to crates.io: arrayref@0.3.10, internment@0.8.7, and append-only-vec@0.1.9. The malicious crates added a typosquatted dependency (proc-macro1) whose build script downloads and executes a remote binary. Notably, proc-macro1 was the first dependency added to arrayref in its ten-year history."
    publisher: "Wiz Research"
  - quote: "arrayref@0.3.10: published at 2026-08-20T07:15:00Z, deleted at 2026-08-20T08:41:40Z. Online for 86 minutes."
    publisher: "The Rust Project"
  - quote: "We do not believe the author of arrayref to be acting maliciously"
    publisher: "The Rust Project"
  - quote: "any developer workstation or CI runner that built an affected project must be treated as compromised."
    publisher: "Wiz Research"
  - quote: "The arrayref infrastructure substantially overlaps with operations attributed to recent North Korean actors."
    publisher: "Wiz Research"
  - quote: "Falls back to a Domain Generation Algorithm if the primary C2 is unreachable, generating 10 algorithmic .com domains every 5 days. Currently, the relevant domains do not appear to be registered."
    publisher: "Wiz Research"
  - quote: "Microsoft assesses with high confidence that this activity is attributable to Sapphire Sleet, a North Korean state actor that primarily targets the financial sector."
    publisher: "Microsoft Security Blog"
verification: multi-source
sourcing_note: >
  Two independent assessors: the Rust Security Response Team for the timeline, removal and account
  handling, and Wiz Research for the payload analysis and the infrastructure overlap. The attribution
  chain is attributed per claim rather than collectively — Microsoft attributes the Mastra campaign to
  Sapphire Sleet at high confidence, Google Threat Intelligence Group attributes the axios campaign to
  UNC1069, and Wiz's own contribution is the observation that arrayref's infrastructure overlaps both.
  UNC1069 is already a registered alias of the same tracked cluster in this store, so the two vendor
  attributions point at one entity rather than two. Wiz's article carries a published correction
  narrowing its own browser claim from credential theft to enumeration of saved logins, and this entry
  follows the corrected version. Wiz's reach figures are quoted with its own unscoped wording because
  the article does not define the population they are measured over.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Search build and CI logs for any `cargo build` between 07:15 and 09:26 UTC on 2026-08-20 that resolved arrayref 0.3.10, internment 0.8.7 or append-only-vec 0.1.9, and treat every workstation and runner that did as compromised rather than merely as needing a dependency bump — the payload ran at compile time and persistence outlives the rollback."
  - "Check `~/.cargo/registry/cache` on developer and build hosts for cached copies of the withdrawn versions; deletion from crates.io does not clear a local cache, and a cached copy will still build."
migrated_from: null
---

The mechanism here is the whole story, and it is one Rust shares with every ecosystem that lets packages run code at install or build time. Build scripts execute during compilation, ahead of the parent crate's own code, so there is no "use the library carefully" defence: compiling was execution.

On 2026-08-20 an attacker with a compromised crates.io publisher account pushed malicious releases of three widely used crates. Wiz's summary: *"On August 20, 2026, malicious versions of three Rust crates were published to crates.io: arrayref@0.3.10, internment@0.8.7, and append-only-vec@0.1.9. The malicious crates added a typosquatted dependency (proc-macro1) whose build script downloads and executes a remote binary. Notably, proc-macro1 was the first dependency added to arrayref in its ten-year history"* ([Wiz Research, 2026-08-20](https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns)). That last clause is the tell that this was an account takeover rather than a maintainer turning hostile — a crate that has taken no dependency in a decade suddenly taking one, and taking one whose name is a single character away from the ubiquitous proc-macro2. The Rust Security Response Team reached the same conclusion: *"We do not believe the author of arrayref to be acting maliciously"* ([The Rust Project, 2026-08-20](https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/)), and credits discovery to the research team at Nextron Systems.

The exposure windows were short and are published per crate — *"arrayref@0.3.10: published at 2026-08-20T07:15:00Z, deleted at 2026-08-20T08:41:40Z. Online for 86 minutes."* — with internment online 90 minutes and append-only-vec 107 minutes, the three publications staggered across about 23 minutes rather than landing together. The team also removed the typosquat dependency and five further attacker-controlled crates, and locked the publisher account.

**What ran.** The build script reconstructs its command-and-control URL from encoded fragments, disables certificate validation for its own callback, and pulls a platform-specific second stage for 64-bit Linux, Windows and macOS including Apple silicon. The implant beacons over HTTPS, collects host and user details, enumerates installed applications, and queries the SQLite stores Chrome, Brave and Edge use for saved logins. That last point deserves precision, because Wiz corrected itself on it: *"Edit: A prior version of this piece mistakenly stated that browser credentials were stolen. The queries only enumerate saved logins, they do not retrieve the encrypted credential material."* Enumeration of which sites a developer has credentials for is materially different from taking the credentials, and this entry follows the corrected claim. Persistence is a registry run key on Windows, a launch agent on macOS or a user-scoped systemd service on Linux, and the command set covers reconfiguring the channel, running scripts synchronously or in the background, and terminating. Its resilience feature is worth noting for hunting: *"Falls back to a Domain Generation Algorithm if the primary C2 is unreachable, generating 10 algorithmic .com domains every 5 days. Currently, the relevant domains do not appear to be registered."* Unregistered today means the sinkhole opportunity is open and the blocking opportunity is not.

**Attribution, per claiming vendor.** Wiz states *"The arrayref infrastructure substantially overlaps with operations attributed to recent North Korean actors"*, resting it on a beacon endpoint previously seen in the Mastra npm campaign, a shared TLS certificate issuer with Mastra infrastructure, a victim-reported address appearing in Google's analysis of the axios npm compromise, and both campaigns sitting in one hosting provider's address range. The attributions themselves belong to other vendors and should be carried as theirs: Microsoft says of Mastra that *"Microsoft assesses with high confidence that this activity is attributable to Sapphire Sleet, a North Korean state actor that primarily targets the financial sector"* ([Microsoft Security Blog, 2026-06-17](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)), while Google Threat Intelligence Group attributes the axios compromise to UNC1069 ([Google Threat Intelligence Group, 2026-03-31](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)). Those two designations resolve to the same cluster this store already tracks, so the overlap is with one actor seen twice rather than two whose relationship is itself unproven — which strengthens the read. Wiz's contribution is the infrastructure linkage, not the attribution.

**Scope.** Wiz puts arrayref's reach at *"over 35% of all environments"* and *"used in ¾ of all environments where Rust is present"* — figures worth carrying with the caveat that the article does not say what population it measures, so they are best read as its own scanning estate rather than a universal claim. Either way the crate is a near-ubiquitous transitive dependency, which is what makes a ninety-minute window consequential.

Detection concepts, telemetry class first. The distinctive signal is in **build-time process telemetry**: a compiler or package-manager process spawning a network client, or a toolchain process executing a freshly downloaded binary out of a temporary directory. Neither has a legitimate counterpart in most builds, and both are cheap to alert on in CI. Correlate with **persistence-creation telemetry** in the minutes after a build — a new registry run key, launch agent or user systemd unit appearing on a build host is close to definitive. In **egress telemetry**, build agents reaching hosts that are not package registries or artefact stores is the broader pattern worth baselining, since CI runners generally have a small and enumerable set of legitimate destinations.

**Defender takeaway:** the remediation is not a dependency bump. Wiz is explicit — *"any developer workstation or CI runner that built an affected project must be treated as compromised"* — because the payload executed and persisted independently of the crate version now resolved, and a lockfile rollback removes the dependency without touching the run key. The two things to check are the build logs for the window, and the local cargo cache, which retains withdrawn versions that will still build. **Triage:** ordinary Rust builds do fetch from the registry, so registry traffic itself is not the signal; the separators are network egress from the compiler process rather than the package manager, execution of a binary the build did not produce, and any persistence artefact created on a host whose job is to be ephemeral.
