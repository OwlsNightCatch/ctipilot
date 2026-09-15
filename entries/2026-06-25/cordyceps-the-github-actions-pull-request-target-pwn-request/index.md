---
schema: 1
kind: research
title: "\"Cordyceps\" — the GitHub Actions pull_request_target pwn-request class is still widely exploitable at scale"
headline: "\"Cordyceps\" — the GitHub Actions pull_request_target pwn-request class is still widely exploitable at scale"
summary: "\"Cordyceps\" shows the GitHub Actions pull_request_target pwn-request class is still widely live — 300+ of 30,000 scanned high-impact repos were fully exploitable from a single unauthenticated PR, including Microsoft Azure Sentinel and Google's ADK; actions/checkout v7 ships safer defaults but pinned older workflows remain exposed (Novee Security, 2026-06-23)."
discovered_at: "2026-06-25T04:59:08Z"
event_date: 2026-06-24
run_id: 2026-06-25-da7fbd23
priority: high
immediate_action: null
tags:
  - supply-chain
  - cloud
  - vulnerabilities
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:cordyceps-github-actions-pwn-request"
cves: []
sources:
  - url: "https://novee.security/blog/cordyceps/"
    publisher: Novee Security — Cordyceps
    role: primary
  - url: "https://www.securityweek.com/exploitable-ci-cd-vulnerabilities-expose-millions-of-repositories-to-hijacking/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/"
    publisher: GitHub Changelog — actions/checkout safer defaults
    role: corroborating
closed_sources: []
evidence:
  - quote: "Scans of 30,000 high-impact repositories flagged 654 vulnerable instances; over 300 were confirmed fully exploitable"
    publisher: Novee Security
  - quote: GitHub updated actions/checkout on June 18 to block common pwn-request patterns
    publisher: GitHub Changelog
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
migrated_from: briefs/2026-06-25.md
---

Novee Security published "Cordyceps", an empirical study of a long-known but persistently unmitigated class of GitHub Actions CI/CD vulnerabilities ([Novee Security, 2026-06-23](https://novee.security/blog/cordyceps/) · [SecurityWeek, 2026-06-24](https://www.securityweek.com/exploitable-ci-cd-vulnerabilities-expose-millions-of-repositories-to-hijacking/)). The pattern: a `pull_request_target` (or comment-triggered) workflow runs with the base repository's write permissions and secrets while checking out or otherwise consuming untrusted fork-PR content, letting an attacker inject code into a privileged CI context (`T1195.002`). Of ~30,000 high-impact repositories scanned, 654 were flagged and 300+ confirmed fully exploitable — including Microsoft (Azure Sentinel), Google (AI Agent Development Kit), Apache (Doris), Cloudflare (Workers SDK) and the Python Software Foundation (Black) — with exploitation requiring only a free GitHub account and a single PR. Successful exploitation can yield the org's GitHub App key, cloud repository authority, or the ability to publish attacker-controlled packages to trusted registries. GitHub shipped `actions/checkout` v7 on 18 June with safer `pull_request_target` defaults that refuse to fetch fork-PR head commits in unsafe patterns ([GitHub Changelog, 2026-06-18](https://github.blog/changelog/2026-06-18-safer-pull_request_target-defaults-for-github-actions-checkout/)), but organisations pinning older action versions or running self-managed Enterprise Server are not yet protected. Audit `.github/workflows/*.yml` for `pull_request_target` triggers that reference any `${{ github.event.pull_request.* }}` context in `run:`/`env:` steps; scope `GITHUB_TOKEN` to `contents: read` by default; and split build/test onto the unprivileged `pull_request` trigger.
