---
schema: 1
kind: threat
horizon: operational
title: "TeamPCP open-sources its Mini Shai-Hulud framework, spawning a new \"Phantom Gyp\" derivative"
headline: "TeamPCP open-sources its Mini Shai-Hulud framework, spawning a new \"Phantom Gyp\" derivative"
summary: "TeamPCP open-sources its Mini Shai-Hulud supply-chain framework on GitHub, spawning a new \"Phantom Gyp\" derivative and underscoring that valid SLSA provenance does not survive a subverted build environment (SANS ISC, 2026-06-08)."
discovered_at: "2026-06-09T05:00:07Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: high
immediate_action: null
tags:
  - supply-chain
  - organized-crime
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33060"
    publisher: SANS ISC diary
    role: primary
  - url: "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages"
    publisher: Wiz — Miasma analysis
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-06-06)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-09.md
---

**UPDATE (originally covered 2026-06-06):** A SANS ISC handler diary tracking the TeamPCP supply-chain campaign through 7 June reports the operators have open-sourced their Mini Shai-Hulud framework on GitHub, triggering a second wave of derivative campaigns ([SANS ISC, 2026-06-08](https://isc.sans.edu/diary/33060)). Beyond the previously-covered Miasma worm — which compromised npm packages including Red Hat's `@redhat-cloud-services` scope ([Wiz, 2026-06-01](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages)) — the diary names a newly-tracked **Phantom Gyp** campaign that abuses `node-gyp` / `binding.gyp` install-time script execution in compromised npm packages; both inject malicious CI/CD hooks ([SANS ISC, 2026-06-08](https://isc.sans.edu/diary/33060)).

The diary's load-bearing detection-engineering point: valid SLSA provenance attestations do not protect against supply-chain injection when the build environment itself is subverted from the inside. The recommended shift is from attestation-verification to build-pipeline integrity — monitor GitHub Actions runner process trees for unexpected outbound network from within a build, alert on `actions/upload-artifact` shipping signed-but-anomalous binaries, and cross-check published package checksums against CI logs via independent transparency ledgers (e.g. Sigstore Rekor). EU/Swiss public-sector teams running npm-based automation or Red Hat tooling should audit CI/CD pipeline definitions for unexpected workflow-step insertions.
