---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Open-source supply-chain wave status: eight vendors converged on one compromise inside 48 hours, and the week's operational order inverts incident-response reflex — hunt and remove the host persistence before rotating any credential, because revocation is its trigger"
headline: "Supply-chain status — the keyv compromise is CHAINDROP, and rotating the stolen token is what fires the dead-man's switch"
summary: >
  Status update on the npm and developer-ecosystem supply-chain wave prior weeklies tracked from
  install-hook evasion through CI/CD trust abuse to poisoned AI-assistant tool configurations. Two week-level
  deltas beyond the operational entries. First, the 2026-08-04 compromise of the keyv and cacheable npm
  namespaces reported independently by Socket, Datadog and others is the same event as CHAINDROP — one wave,
  not two — and Socket documents a host-level dead-man's switch whose watcher polls the GitHub API with the
  stolen token and runs a remote-supplied handler the moment that token starts returning an HTTP 4xx, so
  credential rotation performed before the persistence is removed is itself the trigger. Second, the
  cross-vendor convergence sharpens the strategic lesson: provenance attests build integrity, not source
  integrity.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-04"
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags: [supply-chain, infostealer, cloud, identity]
regions: [global, europe]
sectors: [technology, public-sector, finance]
entities:
  - campaign:shai-hulud-chaindrop-2026-08
  - campaign:flooding-dropper-npm-2026-08
techniques: [T1195.002, T1543.001, T1543.002, T1552.001, T1078.004, T1071.004]
affected_products: ["npm", "GitHub Actions", "Sigstore"]
cves: []
sources:
  - url: "https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain"
    publisher: "Socket Threat Research"
    date: "2026-08-04"
    role: primary
  - url: "https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain"
    publisher: "Elastic Security Labs"
    date: "2026-08-06"
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Before rotating any credential, hunt for and remove the host-level dead-man's switch. Revocation is its trigger: the watcher runs eval on a remote-supplied handler the moment the stolen token returns an HTTP 4xx."
    publisher: "Socket Threat Research"
  - quote: "The lesson is that provenance attests build integrity, not source integrity. The npm and sigstore pipeline did exactly what it is designed to do and still produced a signed, verifiable attestation for malware, because the source it built from was already trojanized."
    publisher: "Socket Threat Research"
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-08-02/weekly-w31-open-source-supply-chain-status
references:
  - 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver
  - 2026-08-08/chaindrop-oidc-runner-memory-theft-valid-slsa-provenance
  - 2026-08-07/flooding-dropper-npm-846-packages-dns-txt-fallback
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Before revoking or rotating any npm, GitHub, cloud or SSH credential on a developer or CI host that installed an affected package, first locate and remove the token-watcher persistence Socket documents — the launch agent, the user-level systemd service and its configuration directory — because revocation is what makes the watcher execute its remote handler."
migrated_from: null
---

**UPDATE (originally covered 2026-08-02):** the wave prior weeklies tracked from install-hook evasion, through abuse of the trust machinery around packages, to poisoned AI coding-assistant tool configurations produced its largest single event this week. Two things changed at week level that the day-by-day entries do not carry.

The first is that what looked like two events is one. The compromise of the keyv and cacheable npm namespaces, reported on 4 August by Socket and independently by several other vendors within roughly 48 hours, is the same wave this pipeline covered as CHAINDROP two days later: Socket traces it to a compromised maintainer account whose packages "were published with a malicious preinstall hook (setup.mjs) that downloads a standalone Bun runtime, executes an obfuscated second stage, harvests cloud and CI credentials, and republishes trojanized versions of other packages the stolen npm token can reach" ([Socket Threat Research, 2026-08-04](https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain)), the same mechanics Elastic and Unit 42 later detailed under the CHAINDROP name. The reach matters because of where these packages sit: keyv resolves as a transitive dependency beneath common tooling rather than as something teams install deliberately, so most affected estates never chose it.

The second delta is an operational order that inverts the standard reflex, and it is the reason this status entry exists rather than a line in the roll-up. Socket documents a host-level dead-man's switch installed alongside the credential theft — a watcher registered as a launch agent on macOS and as a lingering user-level service on Linux, polling the GitHub API with the stolen token roughly once a minute. Its instruction to responders is explicit: "Before rotating any credential, hunt for and remove the host-level dead-man's switch. Revocation is its trigger: the watcher runs eval on a remote-supplied handler the moment the stolen token returns an HTTP 4xx." Every incident-response playbook opens with credential rotation; on this campaign that step executes attacker code on the host. The corollary for anyone who has already rotated is that the switch has already fired, and the host needs treating accordingly.

Alongside that, the cross-vendor convergence hardened the strategic conclusion the operational entries reached from the other direction. Unit 42's analysis found a path that trades a runner OIDC token at npm's trusted-publishing endpoint for a real publish credential and then signs the result through the public transparency infrastructure, producing provenance it is explicit is not forged ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Socket states the general form: "provenance attests build integrity, not source integrity. The npm and sigstore pipeline did exactly what it is designed to do and still produced a signed, verifiable attestation for malware, because the source it built from was already trojanized." An organisation that added provenance verification to its dependency policy in the past year — a reasonable thing to have done — has a control that would have passed this package.

**Defender takeaway:** the two levers this week's evidence supports are both about ordering and neither is new tooling. Sequence the response correctly on any developer or build host that installed an affected package — persistence removal first, credential rotation second, and treat the host as compromised rather than the credential — and adjust what a passing provenance attestation is allowed to conclude in your dependency policy: it establishes that the artefact came from the declared build pipeline, and says nothing about whether the source that pipeline consumed was clean. A release-age cooldown before installs, which a prior weekly already recorded, remains the cheapest control that would have caught this class, because the malicious versions were identified within hours of publication.

**Triage:** the credential-harvesting stage runs at install time from a package manager's process tree, which is the discriminator against ordinary developer activity — build scripts legitimately spawn interpreters, but a package install that downloads and executes a fresh language runtime is not a normal build step. For the persistence, the artefacts Socket names are a user-scoped launch agent and a lingering user-level service whose job is to make an HTTP request on a timer; a periodic outbound API call from a user-level service on a developer laptop is unremarkable in isolation, and is the signal when it appeared in the same window as a package installation.
