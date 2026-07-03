---
schema: 1
kind: threat
horizon: operational
title: "actions-cool/issues-helper GitHub Action compromised — 53 tags moved to imposter commit reading Runner.Worker /proc/PID/mem; linked to Mini Shai-Hulud"
headline: "actions-cool/issues-helper GitHub Action compromised — 53 tags moved to imposter commit reading Runner.Worker /proc/PID/mem; linked to Mini Shai-Hulud"
summary: "Two more CI/CD supply-chain incidents — actions-cool/issues-helper GitHub Action (exfil infrastructure overlapping with the Mini Shai-Hulud cluster per Socket) and Nx Console VS Code extension (stolen publisher credentials, no cluster attribution). 53 issues-helper tags moved to imposter commit 1c9e803 reading /proc/<PID>/mem of Runner.Worker for secrets exfil (StepSecurity, 2026-05-18). Nx Console 18.95.0 (2.2 M installs) compromised via stolen publisher credentials for an 11-minute window 2026-05-18 12:36–12:47 UTC (The Hacker News, 2026-05-19)."
discovered_at: "2026-05-20T05:00:03Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "incident:actions-cool-issues-helper-github-action-compromised-53-tag"
  - "campaign:mini-shai-hulud"
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials"
    publisher: "StepSecurity, 2026-05-18"
    role: primary
  - url: "https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
  - url: "https://cybersecuritynews.com/compromised-github-action-exfiltrates-workflow-credentials/"
    publisher: "CybersecurityNews, 2026-05-19"
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
migrated_from: briefs/2026-05-20.md
---

StepSecurity disclosed on [2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials) that all 53 existing version tags of the popular `actions-cool/issues-helper` GitHub Action were moved to point to an imposter commit (`1c9e803`) not present in the action's normal branch history, with 15 tags on the companion `actions-cool/maintain-one-comment` action manipulated in the same operation. The malicious payload downloads the Bun JavaScript runtime to the runner, then spawns a Python process that reads the **`/proc/<PID>/mem` address space of the Runner.Worker process** — the GitHub Actions component that holds decrypted workflow secrets during job execution. Captured bytes are filtered via `tr` + `grep` for values marked `isSecret: true` and exfiltrated over HTTPS to `t.m-kosche[.]com`. Socket confirmed the exfiltration domain overlaps with the **Mini Shai-Hulud** npm / PyPI campaign cluster ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)). All 53 imposter commits were created within a 3-minute 16-second window; GitHub has since disabled the repository.

Any workflow that referenced `actions-cool/issues-helper@v*` or a mutable tag during the 2026-05-18 attack window should be treated as a compromised CI/CD pipeline — rotate GitHub PATs, npm tokens, AWS credentials, SSH keys, and any other secret exposed via `${{ secrets.* }}` to that workflow. Maps to T1195.002 (Compromise Software Supply Chain) and T1552.001 (Credentials in Files).

**Why it matters to us:** EU and Swiss developer organisations using GitHub Actions for public-sector software supply chains were directly in scope during the attack window. The mitigation is enforcement of **commit-SHA pinning** for every third-party Action reference (`uses: actions-cool/issues-helper@<full-sha>` rather than `@v2` or `@main`) and runtime enforcement of allow-listed outbound network destinations from runners (StepSecurity Harden-Runner, GitHub-native egress filtering).
