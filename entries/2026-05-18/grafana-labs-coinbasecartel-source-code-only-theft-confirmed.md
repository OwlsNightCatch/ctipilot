---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Grafana Labs / CoinbaseCartel — source-code-only theft confirmed; ransom rejected; detected by canary token"
headline: "Grafana Labs / CoinbaseCartel — source-code-only theft confirmed; ransom rejected; detected by canary token"
summary: "Grafana Labs confirmed on 2026-05-18 that the CoinbaseCartel data-extortion group used a compromised GitHub token granting access to Grafana's GitHub environment to exfiltrate private source code only — no customer data, no production systems — and that it rejected the ransom."
discovered_at: "2026-05-18T05:00:22Z"
event_date: 2026-05-18
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html"
    publisher: The Hacker News — CoinbaseCartel / Grafana breach
    role: primary
  - url: "https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/"
    publisher: SecurityWeek — Grafana confirms breach
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

Grafana Labs confirmed on [2026-05-18](/briefs/2026-05-19/) that the CoinbaseCartel data-extortion group used a compromised GitHub token granting access to Grafana's GitHub environment to exfiltrate private source code only — no customer data, no production systems — and that it rejected the ransom. (Earlier reporting attributed the entry to a `pull_request_target` GitHub Actions misconfiguration and credited a canary token with detection; the in-window victim-confirmation sources cited here state only the compromised-token vector, so those mechanism specifics are not asserted as fact.) The defender takeaway the sources do support: audit GitHub token scopes and lifetimes aggressively, restrict `pull_request_target` workflows as general hardening, and seed canary artefacts in private repositories as a low-cost detection layer for source-code exfiltration.
