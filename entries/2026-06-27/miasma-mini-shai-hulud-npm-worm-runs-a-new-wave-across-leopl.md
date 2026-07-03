---
schema: 1
kind: threat
horizon: operational
title: "Miasma / \"Mini Shai-Hulud\" npm worm runs a new wave across LeoPlatform/RStreams packages"
headline: "Miasma / \"Mini Shai-Hulud\" npm worm runs a new wave across LeoPlatform/RStreams packages"
summary: "\"Miasma/Mini Shai-Hulud\" npm worm runs a new wave across 23+ LeoPlatform/RStreams packages, again using binding.gyp install-time execution to harvest CI and cloud secrets (Socket, 2026-06-25)."
discovered_at: "2026-06-27T05:17:51Z"
event_date: 2026-06-26
run_id: 2026-06-27-40e791d4
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
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
sourcing_note: null
confidence: high
update_of: 2026-06-09/teampcp-open-sources-its-mini-shai-hulud-framework-spawning
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-27.md
---

**UPDATE (originally covered 2026-06-09):** The Miasma / Mini Shai-Hulud / Hades supply-chain worm — last seen backdooring `@redhat-cloud-services` packages and the TeamPCP "Phantom Gyp" framework — ran a fresh wave on 2026-06-24: 23+ malicious versions across the LeoPlatform and RStreams serverless-data-pipeline npm ecosystems (`leo-sdk`, `leo-auth`, `leo-aws`, `leo-cli`) after the `czirker` publisher account was compromised, plus a Go-module compromise of Verana Blockchain ([Socket Security, 2026-06-25](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem)).

The wave reuses the previously documented `binding.gyp`/`node-gyp` install-time execution to stage a Bun runtime that harvests `.env` files, npm/GitHub/cloud tokens, SSH keys and IDE/AI-agent configs, scraping GitHub Actions CI secrets ([JFrog, 2026-06-26](https://research.jfrog.com/post/shai-hulud-miasma-alright-lets-see-if-this-works/)), and again carries the `RevokeAndItGoesKaboom` campaign marker that Socket ties to the earlier `codfish/semantic-release-action` compromise (documented by StepSecurity), where the malicious action searched GitHub commit messages bearing that string as an operator dead-drop channel ([Socket Security, 2026-06-25](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem)). Any CH/EU team consuming these packages in CI should rotate all exposed CI/cloud credentials since 2026-06-20 and alert on `node-gyp` evaluating JavaScript from `binding.gyp`.
