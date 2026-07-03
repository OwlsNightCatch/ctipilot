---
schema: 1
kind: research
horizon: operational
title: "GMO Flatt Security: one GitHub issue could hijack any public repo running Anthropic's claude-code-action — and could have poisoned the action itself"
headline: "GMO Flatt Security: one GitHub issue could hijack any public repo running Anthropic's claude-code-action — and could have poisoned the action itself"
summary: "One malicious GitHub issue could hijack any public repo using Anthropic's claude-code-action — and could have poisoned the action itself. A [bot]-suffix actor check trusted any attacker-registered GitHub App, and indirect prompt injection chained to /proc/self/environ secret theft. Fixed in v1.0.94 (GMO Flatt Security, 2026-06-04)."
discovered_at: "2026-06-05T05:00:05Z"
event_date: 2026-06-04
run_id: 2026-06-05-2c6574c4
priority: high
immediate_action: null
tags:
  - supply-chain
  - ai-abuse
  - auth-bypass
  - patch-available
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/"
    publisher: "GMO Flatt Security, 2026-06-04"
    role: primary
  - url: "https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html"
    publisher: "The Hacker News, 2026-06-04"
    role: corroborating
  - url: "https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/"
    publisher: "SecurityWeek, 2026-04-16"
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
migrated_from: briefs/2026-06-05.md
---

Researcher RyotaK (GMO Flatt Security) disclosed a two-part flaw in Anthropic's **claude-code-action** GitHub Actions workflow, remediated in **v1.0.94** ([GMO Flatt Security, 2026-06-04](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/); [The Hacker News, 2026-06-04](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html)). The core bug is in `checkWritePermissions()` (`src/github/validation/permissions.ts`): the function unconditionally returns `true` for any actor whose username ends in `[bot]`, on the assumption that GitHub App bots are admin-installed. But anyone can register a GitHub App, install it on a repo they own, and use its token to open an issue or PR on *any* public repository — so an attacker-controlled `[bot]` actor passes the gate, and `agent` mode lacked the secondary `checkHumanActor()` guard present in `tag` mode. Chained with **indirect prompt injection** (instructions embedded in the issue body that Claude reads during triage), the default read/write workflow token could be steered to read `/proc/self/environ`, exchange the OIDC token for a Claude GitHub App installation token with code/issues/workflows write, and exfiltrate secrets to the issue comment feed. Pointed at `anthropics/claude-code-action` itself, the same chain could have poisoned the action and propagated downstream. A second variant stemmed from Anthropic's own example workflow shipping `allowed_non_write_users: "*"`. Anthropic rated the issues **7.8 (CVSS 4.0)** and paid a bounty; RyotaK notes he has reported roughly 50 separate permission-system bypasses in this class. The underlying problem is not unique to Anthropic: separate "Comment and Control" research by Aonan Guan, reported in April, independently showed Claude Code, Gemini CLI and GitHub Copilot agents are all exposed to prompt injection via issue/PR comments ([SecurityWeek, 2026-04-16](https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/)).

**Why it matters to us:** any team running AI coding agents in CI/CD has imported a new, structural untrusted-input surface. Update claude-code-action to v1.0.94+, audit every `issues`/`pull_request_target`-triggered workflow that grants an AI agent write scope, and never widen `allowed_non_write_users` beyond vetted accounts.
