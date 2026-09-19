---
schema: 1
kind: incident
title: "Grafana Labs CoinbaseCartel breach — victim confirms source-code-only theft, no customer data, ransom rejected"
headline: "Grafana Labs CoinbaseCartel breach — victim confirms source-code-only theft, no customer data, ransom rejected"
summary: "UPDATE (originally covered 2026-W21): Grafana Labs issued an official 2026-05-18 confirmation of the GitHub Pwn-Request breach previously reported in the 2026-W21 weekly summary (SecurityWeek, 2026-05-18; BleepingComputer, 2026-05-18; The Register, 2026-05-18)."
discovered_at: "2026-05-19T05:00:08Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - europe
  - global
sectors:
  - technology
  - public-sector
entities:
  - "actor:shinyhunters"
  - "incident:grafana-labs-coinbasecartel-pwn-request-github-actions-breac"
cves: []
sources:
  - url: "https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.theregister.com/cyber-crime/2026/05/18/grafana-labs-admits-attackers-downloaded-its-codebase-from-github/5241686"
    publisher: The Register
    role: corroborating
closed_sources: []
evidence:
  - quote: no personal or customer information was stolen and the incident has not impacted customer systems or operations
    publisher: Grafana via SecurityWeek
  - quote: "the attackers demanded a ransom to prevent the source code from being leaked, but it has decided not to pay up"
    publisher: SecurityWeek
verification: multi-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
---

**UPDATE (originally covered 2026-W21):** Grafana Labs issued an official 2026-05-18 confirmation of the GitHub Pwn-Request breach previously reported in the 2026-W21 weekly summary ([SecurityWeek, 2026-05-18](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/); [BleepingComputer, 2026-05-18](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/); [The Register, 2026-05-18](https://www.theregister.com/cyber-crime/2026/05/18/grafana-labs-admits-attackers-downloaded-its-codebase-from-github/5241686)). The material new disclosures in the 2026-05-18 confirmation: Grafana explicitly states (a) only source code was accessed — "no personal or customer information was stolen"; (b) the incident has not impacted customer systems or operations; (c) the ransom was refused. The technical-mechanism details (`pull_request_target` workflow misconfiguration, forked-PR injection of a `curl` command, harvested write-scoped GitHub token, canary-token detection) were previously reported in the 2026-W21 weekly summary citing THN's earlier coverage ([The Hacker News, 2026-05-17](https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html)); they are repeated here as context for defenders who did not catch the weekly. CoinbaseCartel is assessed by THN as an offshoot of the ShinyHunters / Scattered Spider / LAPSUS$ ecosystem and has accumulated ~170 victims since September 2025.

Defender takeaway: Grafana OSS is the de facto monitoring/observability platform in EU/CH public-sector SOC and NOC environments; defenders should monitor non-official Grafana plugin updates and unsigned Grafana agent builds for the next 30 days as a potential supply-chain trojanisation follow-on. The Pwn-Request attack pattern is the same class of CI/CD misconfiguration covered by SentinelOne's *Living off the Pipeline* taxonomy (referenced 2026-05-16); audit every `pull_request_target` workflow to ensure no privileged steps run on untrusted-fork code, set `permissions: read-all` at workflow level and elevate only as needed, and separate privilege-requiring steps into a second `workflow_run` workflow gated on merged code. MITRE T1195.002 / T1552.004 / T1567.
