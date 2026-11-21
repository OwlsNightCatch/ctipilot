---
schema: 1
kind: threat
title: Two concurrent npm dependency-confusion campaigns target internal corporate namespaces
headline: Two concurrent npm dependency-confusion campaigns target internal corporate namespaces
summary: "**Two concurrent npm dependency-confusion campaigns target internal corporate package namespaces** — Microsoft (45 packages across nine organisational scopes) and Sonatype (176 packages) document recon/staging payloads that win npm's version race against private registries when .npmrc is not scope-locked (Microsoft, 2026-05-30 · Sonatype, 2026-05-28). Distinct from the Mini Shai-Hulud / TrapDoor activity covered last week."
discovered_at: "2026-06-01T05:00:01Z"
event_date: 2026-05-30
run_id: 2026-06-01-7f55e064
priority: high
immediate_action: null
tags:
  - supply-chain
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/"
    publisher: Microsoft Threat Intelligence
    role: primary
  - url: "https://www.sonatype.com/blog/inside-a-176-package-npm-campaign-built-to-beat-your-internal-dependencies"
    publisher: Sonatype
    role: corroborating
closed_sources: []
evidence: []
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
migrated_from: briefs/2026-06-01.md
---

Microsoft Threat Intelligence and Sonatype each documented coordinated npm dependency-confusion campaigns in the window, both distinct from the Mini Shai-Hulud / TrapDoor typosquat activity covered last week. Microsoft (published 2026-05-30) detailed malicious packages pushed in two bursts on 28–29 May by three maintainer aliases (`mr.4nd3r50n`, `ce-rwb`, `t-in-one`) — its post is titled for the initial 33, while the body enumerates 45 across the two waves (26 + 7 + 12 by alias) — impersonating internal packages across nine organisational scopes and spoofing internal-infrastructure URLs (GitHub Enterprise, Jira, docs portals) in `package.json` `homepage`/`repository`/`bugs` fields to survive manual review ([Microsoft Threat Intelligence, 2026-05-30](https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/)). The vector is classic dependency confusion: packages published to the public registry under inflated versions (`100.100.100`, `3.5.22`) win npm's resolution race against private-registry equivalents whenever the consuming project's `.npmrc` is not scope-locked. The `postinstall` stager (obfuscator.io, ~7–13 KB across the two waves) carries a kill switch (`T_IN_ONE_NO_TELEMETRY`) and a run-once marker (`~/.cache/._t-in-one_init/`), fingerprints OS, and specifically detects CI/CD environments before pulling a second-stage reconnaissance payload — a two-phase design that profiles before any credential theft, frustrating payload-signature detection. Microsoft reports the offending repositories and accounts were taken down.

Separately, Sonatype documented a larger 176-package campaign (tracked `Sonatype-2026-003429`) using version `99.99.99` to beat private-registry precedence, with `postinstall` scripts likewise targeting developer and CI/CD environments; Sonatype reported Russian-language comments and coordinated infrastructure across the package set ([Sonatype, 2026-05-28](https://www.sonatype.com/blog/inside-a-176-package-npm-campaign-built-to-beat-your-internal-dependencies)). The language artefact is Sonatype's observation, not an attribution. Mapped to `T1195.002 Compromise Software Supply Chain` with discovery TTPs (`T1082`, `T1083`, `T1614`) in the recon payload.

**Why it matters to us:** Any organisation that consumes private npm packages internally and has not scope-locked `.npmrc` is in scope — Swiss/EU eGovernment software factories and research institutions maintaining internal Node.js tooling included, and the CI/CD-detection logic specifically flags build pipelines as higher-value follow-on targets.
