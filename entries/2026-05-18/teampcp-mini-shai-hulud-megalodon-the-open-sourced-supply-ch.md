---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: TeamPCP / Mini Shai-Hulud / Megalodon — the open-sourced supply-chain worm became commodity infrastructure this week
headline: TeamPCP / Mini Shai-Hulud / Megalodon — the open-sourced supply-chain worm became commodity infrastructure this week
summary: "This is the week's defining chain. After the worm framework was open-sourced on 2026-05-12, the window saw it move from a single operator's tool to commodity capability, escalating almost daily:"
discovered_at: "2026-05-18T05:00:05Z"
event_date: 2026-05-24
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - supply-chain
  - actively-exploited
  - infostealer
  - cloud
  - identity
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-megalodon-supply-chain-cascade/"
    publisher: Cloud Security Alliance — Shai-Hulud/Megalodon research note
    role: primary
  - url: "https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/"
    publisher: GitHub Security Blog — internal-repo access
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

This is the week's defining chain. After the worm framework was open-sourced on 2026-05-12, the window saw it move from a single operator's tool to commodity capability, escalating almost daily:

- **2026-05-18 → 19** — First copycat wave: TeamPCP imitators deploy Phantom Bot plus SSH/cloud stealers, the Checkmarx Jenkins plugin is re-trojanised, and a rival "PCPJack" worm appears, per [Ox Security](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/) ([daily 2026-05-19](/briefs/2026-05-19/)). Same window: the Nx Console VS Code extension (2.2M installs) is pushed malicious for an 11-minute window (12:36–12:47 UTC, 2026-05-18) via stolen publisher credentials, and all 53 tags of `actions-cool/issues-helper` are moved to an imposter commit reading `/proc/PID/mem` of the Runner.Worker ([daily 2026-05-20](/briefs/2026-05-20/)).
- **2026-05-21** — Escalation to platform scale: GitHub itself is named in a breach claim, Microsoft's official `durabletask` PyPI package is weaponised (propagating via AWS SSM and `kubectl exec`), and Grafana confirms a missed-token-rotation root cause ([The Hacker News](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html); [daily 2026-05-21](/briefs/2026-05-21/)).
- **2026-05-22** — Unit 42 and StepSecurity publish concurrent analyses establishing that **SLSA Build Level 3 provenance attestation is invalidated as an integrity gate** for these waves — the malicious build step runs inside the legitimately-attested pipeline ([Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/); [daily 2026-05-22](/briefs/2026-05-22/)).
- **2026-05-23 (disclosure; event 2026-05-18)** — SafeDep and OX Security disclose the *Megalodon* sub-campaign, which mass-poisoned 5,561 GitHub repositories in a ~6-hour window on 18 May using forged CI-bot identities and templated commit messages, harvesting cloud credentials and OIDC tokens ([SafeDep](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/); [daily 2026-05-23](/briefs/2026-05-23/)). A further Packagist/Laravel-Lang compromise is reported the same day ([daily 2026-05-24](/briefs/2026-05-24/)).

Two in-window synthesis documents consolidate the picture. The **Cloud Security Alliance** research note (2026-05-22) frames the whole event as a two-wave attack: Wave 1 (Mini Shai-Hulud, 29 Apr – 12 May) hijacked TanStack's GitHub Actions runner via a `pull_request_target` trigger plus Actions cache poisoning, extracted a live OIDC token from runner process memory via `/proc/PID/mem`, obtained a Sigstore signing certificate from Fulcio, and produced **SLSA BL3 provenance attestations for 404 malicious package versions across 172 packages** (CVE-2026-45321, CVSS 9.6) — the first publicly-documented hijack of trusted build pipelines to generate attestation-bearing malicious artefacts. Wave 2 (Megalodon, from 18 May) pushed 5,718 commits to 5,561 repos in under six hours, harvesting AWS IAM, GCP/Azure IMDS, SSH, Docker auth, `.npmrc`, `.netrc`, Kubernetes configs, Vault tokens and Terraform state. Separately, **GitHub's official post-incident blog** (2026-05-20) confirmed an employee device was compromised via the poisoned Nx Console extension (GHSA-c9j4-9m59-847w) and ~3,800 GitHub-internal repositories were exfiltrated, with no customer-data impact found as of publication and a fuller report still outstanding.

Defender takeaways: set `permissions: id-token: none` on workflows that do not need OIDC; disable or isolate `pull_request_target` for fork PRs (`permissions: contents: read`); treat Git commit author/committer fields as unverified free text (use contributor allow-lists / push-rule bypass-actor audit events to catch Megalodon-style forged identities); audit Sigstore Rekor for unexpected signing events from your own pipeline identity; and do not accept SLSA BL3 attestation alone as a clean-package signal.
