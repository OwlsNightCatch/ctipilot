---
schema: 1
kind: threat
horizon: operational
title: "A compromised crates.io account poisoned three Rust utility crates with a build-script dropper, then yanked the clean releases so the responsible fix resolved to the malicious one"
headline: "Cargo runs build scripts at compile time with the building user's privileges, so one dependency refresh detonated it — the crate's code was never called"
summary: >
  On 2026-08-20 an attacker used a long-standing Rust maintainer's compromised publishing account to
  release poisoned versions of arrayref, internment and append-only-vec within 23 minutes. The library
  source was untouched; each release added one new dependency, a same-day typosquat of a ubiquitous crate,
  whose build script fetched and launched a second stage. Because Cargo compiles and runs build scripts on
  the building machine with that user's full privileges, a single dependency resolution was enough to
  execute it on a developer workstation or CI runner — no call into the crate required, and the build still
  reported success. Twenty-four seconds after publishing, the same account yanked five prior clean releases
  in a scripted burst, so Cargo's own yanked-version warning steered the obvious fix onto the malicious
  release. Lockfile-pinned builds were not exposed; a version range in the manifest was not protection.
discovered_at: "2026-08-22T06:09:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags: [supply-chain, infostealer, organized-crime, no-patch]
regions: [global]
sectors: [public-sector, technology, finance]
entities: [campaign:arrayref-crates-io-build-time-dropper, actor:sapphire-sleet, campaign:mastra-easy-day-js-supply-chain]
techniques: [T1195.001, T1078, T1036.005, T1105, T1027, T1059.001, T1059.005, T1547.001, T1543.001, T1543.002, T1082, T1518, T1217, T1071.001, T1041, T1568.002]
affected_products: ["arrayref (Rust crate)", "internment (Rust crate)", "append-only-vec (Rust crate)", "Cargo", "crates.io"]
cves: []
sources:
  - url: "https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/"
    publisher: "Rust Security Response Team"
    date: "2026-08-20"
    role: primary
  - url: "https://rustsec.org/advisories/RUSTSEC-2026-0260.html"
    publisher: "RustSec Advisory Database"
    date: "2026-08-20"
    role: primary
  - url: "https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack"
    publisher: "StepSecurity"
    date: "2026-08-20"
    role: primary
  - url: "https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns"
    publisher: "Wiz Research"
    date: "2026-08-20"
    role: primary
  - url: "https://rustsec.org/advisories/RUSTSEC-2026-0266.html"
    publisher: "RustSec Advisory Database"
    date: "2026-08-20"
    role: corroborating
  - url: "https://rustsec.org/advisories/RUSTSEC-2026-0262.html"
    publisher: "RustSec Advisory Database"
    date: "2026-08-20"
    role: corroborating
  - url: "https://rustsec.org/advisories/RUSTSEC-2026-0265.html"
    publisher: "RustSec Advisory Database"
    date: "2026-08-20"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/hackers-poison-arrayref-rust-crate-to-push-infostealer-malware/"
    publisher: "BleepingComputer"
    date: "2026-08-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Rust Security Response Team verified this to be the case: the crate had a build script that was downloading a malicious payload."
    publisher: "Rust Security Response Team"
  - quote: "to be acting maliciously, but their computer or credentials are likely compromised, and we are attempting to contact them."
    publisher: "Rust Security Response Team"
  - quote: "Because build scripts run during compilation, building an affected project was sufficient to execute the payload."
    publisher: "Wiz Research"
  - quote: "Rust build scripts compile and run on the machine performing the build, with that user's full privileges, including access to SSH keys, cloud credentials, CI secrets, and signing keys."
    publisher: "StepSecurity"
  - quote: "The attacker turned the registry's own safety feature into the delivery channel."
    publisher: "StepSecurity"
  - quote: "Builds with pre-existing lockfiles pinning clean versions kept compiling the clean, yanked-but-downloadable code, since yanking alone never breaks a locked build."
    publisher: "StepSecurity"
  - quote: "The decisive check is the lockfile, not the registry."
    publisher: "StepSecurity"
  - quote: "Automated tooling will not flag this for you."
    publisher: "StepSecurity"
  - quote: "It was downloaded 2,285 times, which constituted less than"
    publisher: "RustSec Advisory Database (RUSTSEC-2026-0260)"
  - quote: "infrastructure substantially overlaps with operations attributed to recent North Korean actors."
    publisher: "Wiz Research"
verification: multi-source
sourcing_note: >
  Five independent publishers, with the Rust Security Response Team and the RustSec advisory database as
  first-party authorities for the registry and its advisory records — hence reliability A and credibility 1
  for the mechanism, versions, timeline and response. Confidence drops sharply for two sub-claims and the
  entry marks both. The North Korean connection is Wiz's own overlap assessment on infrastructure evidence,
  not an attribution by anyone, and it is recorded in the registry as an overlaps-with edge rather than an
  attribution. The stage-two host-persistence details are third-party-reported and StepSecurity states
  explicitly that it did not independently reproduce them. Two quotes are deliberate mid-sentence fragments
  because inline markup splits the sentence on the page — the Rust team's begins "to be acting maliciously"
  and the RustSec download figure stops before a code tag — and they are left that way rather than
  silently re-joined into text the page does not contain. Wiz self-corrected its own initial claim that
  browser credentials were stolen, stating the payload's queries only enumerate saved logins and do not
  retrieve the encrypted credential material; the technique mapping follows the correction rather than the
  wording another outlet relayed from before it. The compromised maintainer is not named here: the Rust
  team states it does not believe the author was acting maliciously, and the handle adds nothing a defender
  acts on. No European or public-sector consumer or victim is named by any source; the European link is on
  the discovery side, with the Rust team crediting a German research team with finding and reporting it.
confidence: high
update_of: null
references: ["2026-08-08/chaindrop-oidc-runner-memory-theft-valid-slsa-provenance"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Search build logs for jobs that created or refreshed a Cargo lockfile between 07:11 and 09:25 UTC on 2026-08-20 — cargo update, cargo add, a fresh build with no committed lockfile, or any ephemeral or cache-busted runner — and check whether the resolved versions included arrayref 0.3.10, internment 0.8.7, append-only-vec 0.1.9, or any version of the attacker-owned crates (proc-macro1, proc-macro-en, arone, aronenao, aovine, tinymember). A committed lockfile pinning older versions was not exposed; a version range in Cargo.toml was not protection."
  - "On any host that did resolve a poisoned version, treat the build identity as compromised rather than the project: build scripts run with the building user's full privileges, so rotate the SSH keys, cloud credentials, CI secrets and signing keys reachable from that runner or workstation. Then purge the local Cargo registry cache and any committed vendor directory — the malicious releases were deleted from crates.io, which does not clean a warm cache and does not stop an offline build from compiling the payload again."
  - "Re-run dependency auditing against a refreshed advisory database if it was run on 2026-08-20 and came back clean: the malicious versions were deleted rather than yanked and the RustSec records were still pending that day, so a scanner could report a project holding a poisoned pin as clean. The seven RUSTSEC records now exist and carry no patched version, so the remediation is pinning the last clean release, not upgrading."
migrated_from: null
---

On 2026-08-20 an attacker published poisoned releases of three long-lived, low-level Rust utility crates — arrayref, internment and append-only-vec — from the compromised publishing account of a maintainer who has held it for years. The Rust Security Response Team states it does not believe the author was acting maliciously, but that their computer or credentials are likely compromised ([Rust Security Response Team, 2026-08-20](https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/)). The mechanism is the part worth internalising, because it defeats the reflex most teams reach for. Each poisoned release left the crate's own library source untouched and added exactly one thing: a new dependency on a same-day typosquat of one of the most widely used crates in the ecosystem, whose build script reassembled a download URL from encoded fragments, fetched a platform-specific second stage with certificate validation switched off, wrote it to a temporary path named to resemble a Rust toolchain component, and spawned it detached. The Rust team confirms the shape plainly: the crate had a build script that was downloading a malicious payload ([Rust Security Response Team, 2026-08-20](https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/)).

Cargo compiles and runs build scripts as part of the build. Wiz states the consequence directly — because build scripts run during compilation, building an affected project was sufficient to execute the payload ([Wiz Research, 2026-08-20](https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns)) — and StepSecurity states what the payload inherits: Rust build scripts compile and run on the machine performing the build, with that user's full privileges, including access to SSH keys, cloud credentials, CI secrets and signing keys ([StepSecurity, 2026-08-20](https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack)). Nothing in the application ever had to call into the crate. The build step concluded successfully and the compiler exited cleanly. "We do not ship that dependency to production" is not a defence against a compromise that executes at compile time on the machine holding the deployment keys.

The delivery trick deserves its own paragraph because it inverts a safety feature. Twenty-four seconds after publishing the malicious arrayref release, the same account yanked the five preceding clean releases in a scripted burst. Yanking in Cargo does not delete a version; it warns and steers resolution away from it. So a developer who saw the yanked-version warning and did the responsible thing — refresh that dependency — resolved to the one remaining non-yanked release, which was the malicious one. StepSecurity's summary is exact: the attacker turned the registry's own safety feature into the delivery channel ([StepSecurity, 2026-08-20](https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack)), and it reports that this is how the original reporter was hit. The Rust team, alerted at 07:54 UTC, deleted the three malicious versions within roughly an hour and a half of each going live, removed six attacker-owned crates including a spare dropper carrying the same build script, locked the accounts and reversed the yanks.

Exposure is narrower than the download figures suggest, and the reason is the single most transferable fact here. RustSec records that the malicious arrayref release was downloaded 2,285 times, which it puts at less than ten per cent of that crate's download traffic across all versions, because most consumers had older versions pinned in their lockfiles ([RustSec, 2026-08-20](https://rustsec.org/advisories/RUSTSEC-2026-0260.html)). StepSecurity states the mechanism behind that: builds with pre-existing lockfiles pinning clean versions kept compiling the clean, yanked-but-downloadable code, since yanking alone never breaks a locked build ([StepSecurity, 2026-08-20](https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack)) — and its guidance reduces to one line, that the decisive check is the lockfile, not the registry. Two corollaries follow and both cut against intuition: a semver range in the manifest is not protection, because a range like `0.3` matches the malicious `0.3.10`; and deletion from the registry does not help a host that already has the artefact, because a warm local registry cache or a committed vendor directory keeps building the payload offline after the versions no longer exist upstream. One of the three compromised crates depends on another, so a single resolution could pull two poisoned crates into one tree.

**Defender takeaway:** the detection signal is destination novelty during a compile step, not a failed build. StepSecurity reproduced the attack in a monitored continuous-integration job and observed the build step open one outbound connection to a destination never seen in any prior run of that workflow, while the step still concluded success and the job went green; legitimate Rust build traffic in the same run reached only the registry, index, documentation and toolchain endpoints. That makes egress baselining per workflow the highest-yield control, and it is one most teams have never applied to build steps. The second anchor is process lineage that outlives the job: the dropper deliberately abandons its child handle so the spawned process escapes Cargo's job object, so a detached descendant of a build-script process still running after the step completes is the tell — on Windows the observed shape is a script interpreter parented into a build tree launching a script from the user temporary directory with no window, and on Unix a file written to a temporary directory by a build script, made executable and spawned with its standard streams discarded. Third, and cheapest, is manifest review as telemetry rather than as code review: a first-ever dependency appearing in a crate that has had none for a decade, and build-time dependencies that together constitute a downloader — an encoding library, a TLS stack and an HTTP client — in a library with no reason to make network calls. StepSecurity notes the registry metadata alone establishes that capability before anyone reads the script.

**Triage:** build scripts legitimately do surprising things — probe for system libraries, generate code, invoke compilers — so their mere existence discriminates nothing, and neither does a build script making a network call in an ecosystem where some legitimately fetch toolchains. The discriminators are the pairing and the timing: a destination absent from that workflow's own history, a process that survives the build step that spawned it, and a dependency edge that appeared in a release whose library source did not change. The last of those is checkable from registry metadata without executing anything. Note also the window in which tooling could not help: StepSecurity observed that because the malicious versions were deleted rather than yanked and the advisory records were still pending, dependency auditing reported clean for a project pinning a poisoned version — automated tooling will not flag this for you, in its words. The seven RustSec records now exist and close that gap, which is why re-running an audit that came back clean on the day is worth the two minutes.
