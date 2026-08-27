---
schema: 1
kind: threat
horizon: operational
title: "TeamPCP open-sources its Mini Shai-Hulud framework, spawning a new \"Phantom Gyp\" derivative"
headline: "TeamPCP open-sources its Mini Shai-Hulud framework, spawning a new \"Phantom Gyp\" derivative"
summary: >
  TeamPCP open-sources its Mini Shai-Hulud supply-chain framework on GitHub, spawning a new
  "Phantom Gyp" derivative and underscoring that valid SLSA provenance does not survive a
  subverted build environment (SANS ISC, 2026-06-08).
discovered_at: "2026-06-09T05:00:07Z"
updated_at: "2026-06-27T05:17:51Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: high
immediate_action: null
tags:
  - supply-chain
  - organized-crime
  - cloud
  - infostealer
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
  - "campaign:miasma-redhat-npm-supply-chain"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33060"
    publisher: SANS ISC diary
    role: primary
  - url: "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages"
    publisher: Wiz — Miasma analysis
    role: corroborating
  - url: "https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem"
    publisher: Socket Security
    role: primary
  - url: "https://research.jfrog.com/post/shai-hulud-miasma-alright-lets-see-if-this-works/"
    publisher: JFrog Security Research
    role: corroborating
  - url: "https://thehackernews.com/2026/06/miasma-malware-targets-npm-packages-and.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-06-06)"
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-27T05:17:51Z"
    run_id: 2026-06-27-40e791d4
    type: update
    summary: >
      "Miasma/Mini Shai-Hulud" npm worm runs a new wave across 23+ LeoPlatform/RStreams packages,
      again using binding.gyp install-time execution to harvest CI and cloud secrets (Socket,
      2026-06-25).
    fields:
      - entities
      - sources
      - tags
      - body
    merged_from: 2026-06-27/miasma-mini-shai-hulud-npm-worm-runs-a-new-wave-across-leopl
migrated_from: briefs/2026-06-09.md
---

**UPDATE (originally covered 2026-06-06):** A SANS ISC handler diary tracking the TeamPCP supply-chain campaign through 7 June reports the operators have open-sourced their Mini Shai-Hulud framework on GitHub, triggering a second wave of derivative campaigns ([SANS ISC, 2026-06-08](https://isc.sans.edu/diary/33060)). Beyond the previously-covered Miasma worm — which compromised npm packages including Red Hat's `@redhat-cloud-services` scope ([Wiz, 2026-06-01](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages)) — the diary names a newly-tracked **Phantom Gyp** campaign that abuses `node-gyp` / `binding.gyp` install-time script execution in compromised npm packages; both inject malicious CI/CD hooks ([SANS ISC, 2026-06-08](https://isc.sans.edu/diary/33060)).

The diary's load-bearing detection-engineering point: valid SLSA provenance attestations do not protect against supply-chain injection when the build environment itself is subverted from the inside. The recommended shift is from attestation-verification to build-pipeline integrity — monitor GitHub Actions runner process trees for unexpected outbound network from within a build, alert on `actions/upload-artifact` shipping signed-but-anomalous binaries, and cross-check published package checksums against CI logs via independent transparency ledgers (e.g. Sigstore Rekor). EU/Swiss public-sector teams running npm-based automation or Red Hat tooling should audit CI/CD pipeline definitions for unexpected workflow-step insertions.

## Update — 2026-06-27T05:17:51Z

The Miasma / Mini Shai-Hulud / Hades supply-chain worm — last seen backdooring `@redhat-cloud-services` packages and the TeamPCP "Phantom Gyp" framework — ran a fresh wave on 2026-06-24: 23+ malicious versions across the LeoPlatform and RStreams serverless-data-pipeline npm ecosystems (`leo-sdk`, `leo-auth`, `leo-aws`, `leo-cli`) after the `czirker` publisher account was compromised, plus a Go-module compromise of Verana Blockchain ([Socket Security, 2026-06-25](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem)).

The wave reuses the previously documented `binding.gyp`/`node-gyp` install-time execution to stage a Bun runtime that harvests `.env` files, npm/GitHub/cloud tokens, SSH keys and IDE/AI-agent configs, scraping GitHub Actions CI secrets ([JFrog, 2026-06-26](https://research.jfrog.com/post/shai-hulud-miasma-alright-lets-see-if-this-works/)), and again carries the `RevokeAndItGoesKaboom` campaign marker that Socket ties to the earlier `codfish/semantic-release-action` compromise (documented by StepSecurity), where the malicious action searched GitHub commit messages bearing that string as an operator dead-drop channel ([Socket Security, 2026-06-25](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem)). Any CH/EU team consuming these packages in CI should rotate all exposed CI/cloud credentials since 2026-06-20 and alert on `node-gyp` evaluating JavaScript from `binding.gyp`.
