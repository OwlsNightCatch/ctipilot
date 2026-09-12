---
schema: 1
kind: research
title: "One-click GitHub OAuth-token theft via github.dev, full-disclosed with PoC; Microsoft patched 3 June"
headline: "One-click GitHub OAuth-token theft via github.dev, full-disclosed with PoC; Microsoft patched 3 June"
summary: "Independent researcher Ammar Askar published full details and a PoC for a one-click attack on GitHub's browser editor github.dev that extracts the victim's full-scope GitHub OAuth token (read/write to all repos, including private) (Ammar Askar, 2026-06-02 · The Hacker News, 2026-06-04)."
discovered_at: "2026-06-04T05:00:11Z"
event_date: 2026-06-04
run_id: 2026-06-04-51b23ffa
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - supply-chain
  - patch-available
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://blog.ammaraskar.com/github-token-stealing/"
    publisher: Ammar Askar
    role: primary
  - url: "https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-06-04.md
---

Independent researcher Ammar Askar published full details and a PoC for a one-click attack on GitHub's browser editor `github.dev` that extracts the victim's full-scope GitHub OAuth token (read/write to all repos, including private) ([Ammar Askar, 2026-06-02](https://blog.ammaraskar.com/github-token-stealing/) · [The Hacker News, 2026-06-04](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html)). The attack abuses github.dev's embedded VSCode: a crafted page simulates synthetic keyboard events (keydown injection) to drive the editor into silently installing a malicious workspace extension, which then reads and exfiltrates the OAuth token the editor holds (`T1528`); Askar notes the technique does not rely on bypassing `postMessage` origin validation. The token is not scoped to the repo in use. Askar disclosed one hour before publishing, citing prior silent-fix experience with Microsoft; Microsoft shipped a fix on 3 June. Until updated clients are confirmed, avoid github.dev with untrusted extensions installed and watch GitHub audit logs for token use from unexpected IPs/user-agents.
