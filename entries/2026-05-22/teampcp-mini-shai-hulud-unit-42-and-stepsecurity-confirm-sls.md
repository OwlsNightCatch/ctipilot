---
schema: 1
kind: threat
horizon: operational
title: TeamPCP Mini Shai-Hulud — Unit 42 and StepSecurity confirm SLSA Build Level 3 attestation invalidated as integrity gate
headline: TeamPCP Mini Shai-Hulud — Unit 42 and StepSecurity confirm SLSA Build Level 3 attestation invalidated as integrity gate
summary: "UPDATE (originally covered 2026-05-19, updated 2026-05-21): Unit 42 (Palo Alto Networks) and StepSecurity published concurrent technical analyses on 2026-05-21 of the TeamPCP Mini Shai-Hulud npm supply-chain campaign, establishing the defining novelty of this wave: the first documented case of malicious npm …"
discovered_at: "2026-05-22T05:00:06Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: notable
immediate_action: null
tags:
  - supply-chain
  - nation-state
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/"
    publisher: "Unit 42, 2026-05-21"
    role: primary
  - url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
    publisher: "StepSecurity, 2026-05-21"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-19/teampcp-shai-hulud-first-copycat-wave-phantom-bot-ssh-cloud
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-22.md
---

**UPDATE (originally covered 2026-05-19, updated 2026-05-21):** Unit 42 (Palo Alto Networks) and StepSecurity published concurrent technical analyses on 2026-05-21 of the TeamPCP Mini Shai-Hulud npm supply-chain campaign, establishing the defining novelty of this wave: the first documented case of malicious npm packages carrying valid SLSA Build Level 3 provenance attestations ([Unit 42, 2026-05-21](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)). Attackers compromised TanStack's legitimate GitHub Actions CI/CD pipeline's trusted OIDC identity mid-workflow — without stealing developer credentials — making the SLSA attestation genuine while the package payload was malicious. This invalidates "package carries valid provenance attestation" as a sufficient supply-chain integrity gate.

The execution chain runs `tanstack_runner.js` under the Bun JavaScript runtime, enumerating stored credentials including `gh auth token` capture (`T1552.001 Unsecured Credentials: Credentials In Files`); stolen npm tokens and GitHub PATs are used to backdoor every package the victim account can publish (`T1650 Acquire Access`), making the worm self-propagating across the npm ecosystem. By end of the 2026-05-11 wave, 373 malicious package versions across 169 npm packages and PyPI mirrors were active ([Unit 42, 2026-05-21](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)).

Defender actions from this technical update: (a) SLSA attestation verification is now insufficient as a sole gate — add runtime behavioural scanning of npm install scripts alongside provenance checks; (b) Pin GitHub Actions to commit SHAs, not mutable tags, to prevent mid-workflow OIDC identity hijack; (c) If pipelines ran `npm publish` during 2026-05-11 to 2026-05-12, rotate npm tokens and GitHub PATs and audit owned packages for unauthorised versions; (d) In environments where Bun is not an approved runtime, flag any `bun` or `bun.js` process execution from a CI runner context (Sysmon EID 1 process-name filter).
