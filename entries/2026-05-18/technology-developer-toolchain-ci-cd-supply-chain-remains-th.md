---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "Technology / developer toolchain — CI/CD supply chain remains the week's highest-volume attack surface"
headline: "Technology / developer toolchain — CI/CD supply chain remains the week's highest-volume attack surface"
summary: "The Shai-Hulud / Megalodon supply-chain worm went commodity — open-sourced 12 May, it escalated daily across the window: GitHub's own internal repos exfiltrated (~3,800), Microsoft's durabletask PyPI package weaponised, 5,561 repositories mass-poisoned in one ~6-hour Megalodon burst, and SLSA Build Level 3 attestation invalidated as an integrity gate. (daily 2026-05-21; CSA research note)"
discovered_at: "2026-05-18T05:00:18Z"
event_date: null
run_id: 2026-W21-473d6fa5
priority: high
immediate_action: null
tags:
  - supply-chain
  - actively-exploited
  - cloud
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-megalodon-supply-chain-cascade/"
    publisher: Cloud Security Alliance — Shai-Hulud/Megalodon research note
    role: primary
  - url: "https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/"
    publisher: SafeDep — Megalodon
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
migrated_from: briefs/weekly/2026-W21.md
---

The Shai-Hulud/Megalodon waves (§ 2) made the developer toolchain the single most-targeted surface of the week by volume — 5,561 repositories mass-poisoned in one Megalodon burst, GitHub's own internal repos exfiltrated, and the SLSA BL3 trust model invalidated. The cross-cutting lesson for every sector running CI/CD (which is now every sector) is that build-time trust controls — OIDC token scoping, provenance attestation, registry publishing gates — are the contested ground, and the npm staged-publishing GA (§ 8) is the first registry-level structural response.
