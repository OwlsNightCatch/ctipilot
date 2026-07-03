---
schema: 1
kind: threat
horizon: operational
title: "Mini Shai-Hulud — TeamPCP worm hits TanStack, UiPath, Mistral AI, OpenSearch (160+ package versions)"
headline: "Mini Shai-Hulud — TeamPCP worm hits TanStack, UiPath, Mistral AI, OpenSearch (160+ package versions)"
summary: "Mini Shai-Hulud worm re-detonates. TeamPCP poisoned 160+ npm package versions including @tanstack/ (42 packages, ~12M weekly downloads), @uipath/ (60+), @mistralai/* and @opensearch-project/opensearch via a pull_request_target → pnpm-cache poisoning → /proc/<pid>/mem OIDC-token theft chain that produced valid SLSA Build Level 3 provenance on the trojanised tarballs. UiPath is widely used in EU public-sector RPA; SAP HotNews #3747787 acknowledges CAP-package impact (StepSecurity, 2026-05-11; TanStack post-mortem, 2026-05-12)."
discovered_at: "2026-05-13T05:00:11Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
    publisher: "StepSecurity, 2026-05-11"
    role: primary
  - url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
    publisher: "TanStack post-mortem, 2026-05-12"
    role: corroborating
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: "Wiz, 2026-05-12"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12558"
    publisher: "NCSC-CH Security Hub #12558, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-10/pcpjack-modular-cloud-credential-theft-worm-displaces-teampc
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
---

**UPDATE (originally covered 2026-05-10):** Between 19:20 and 19:26 UTC on 2026-05-11, TeamPCP's Mini Shai-Hulud self-propagating worm executed its largest campaign to date, compromising 160+ malicious versions across `@tanstack/*` (42 packages including `@tanstack/react-router` at ~12M weekly downloads), `@uipath/*` (60+ packages), `@mistralai/*`, `@opensearch-project/opensearch`, `@squawk/*`, `@draftlab/*` and `@tallyui/*`, plus two PyPI packages ([StepSecurity analysis, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem); [TanStack post-mortem, 2026-05-12](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem); [Wiz, 2026-05-12](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised); [NCSC-CH Security Hub #12558, 2026-05-12](https://security-hub.ncsc.admin.ch/#/posts/12558)).

The novel attack chain (decomposed in § 5) is materially different from the 2026-05-10 SAP-CAP campaign: the operator (`voicproducoes`, GitHub account ID 269549300) submitted a poisoned PR to a target repository that triggered a `pull_request_target` workflow, used that privileged workflow to seed a malicious pnpm store into the GitHub Actions cache, then waited for legitimate maintainer merges to main — the release workflow restored the poisoned cache, attacker-controlled binaries extracted GitHub Actions OIDC tokens from `/proc/<pid>/mem`, and the worm used npm's token-exchange endpoint to publish trojanised package versions **with valid SLSA Build Level 3 provenance attestations**. The provenance bypass is the most significant evolution — SLSA L3 was the supply-chain assurance many EU public-sector procurement frameworks were starting to rely on, and this campaign demonstrates it is forgeable without abusing the package's own publish step.

Operational delta for defenders: SAP Note #3747787 (HotNews) acknowledges CAP-package impact and ships a clean version list. UiPath impact is the highest-priority public-sector signal — UiPath RPA is widely deployed in Swiss federal e-government automation and EU agency back-offices; review `package-lock.json` / `pnpm-lock.yaml` in every UiPath-using pipeline against the StepSecurity / Wiz package-version manifest. **Before revoking any GitHub PAT or npm token, sanitise the developer machine first** — token revocation triggers the worm's `gh-token-monitor` dead-man's switch that executes `rm -rf ~/` on the affected workstation. Mapped to `T1195.002 Supply Chain Compromise: Compromise Software Supply Chain`, `T1552.001 Unsecured Credentials: Credentials in Files`, `T1078.004 Cloud Accounts`.
