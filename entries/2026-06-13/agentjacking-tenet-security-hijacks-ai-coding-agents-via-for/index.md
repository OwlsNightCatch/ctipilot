---
schema: 1
kind: research
title: "\"Agentjacking\": Tenet Security hijacks AI coding agents via forged Sentry error events"
headline: "\"Agentjacking\": Tenet Security hijacks AI coding agents via forged Sentry error events"
summary: "Tenet Security documented an MCP-injection attack class that abuses the implicit trust between AI coding agents and the Sentry error-tracking integration (The Hacker News, 2026-06-12)."
discovered_at: "2026-06-13T05:00:05Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
  - phishing
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:agentjacking-mcp-sentry-injection-2026"
cves: []
sources:
  - url: "https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html"
    publisher: The Hacker News
    role: primary
  - url: "https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/"
    publisher: Tenet Security
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
migrated_from: briefs/2026-06-13.md
---

Tenet Security documented an MCP-injection attack class that abuses the implicit trust between AI coding agents and the Sentry error-tracking integration ([The Hacker News, 2026-06-12](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html)). The attacker needs only a target's Sentry DSN — a write-only credential frequently exposed in client-side JavaScript or committed to GitHub — to publish a crafted error event embedding markdown-formatted instructions. When a developer later asks their coding agent to investigate that Sentry issue, the agent retrieves the injected event over MCP and executes the embedded instructions with the developer's own system privileges. Because every action the agent takes is one the developer nominally authorised, the technique reportedly slips past EDR, WAF, IAM and VPN controls ([Tenet Security, 2026-06-12](https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/)). Sentry acknowledged the disclosure but declined a root-cause fix, deploying only a content filter for a specific payload string; no CVE was assigned because the issue is an architectural trust-model gap in MCP. Maps to T1059 (agent-mediated command execution) and T1195. Defender action: audit MCP server integrations for any external service that can write content later surfaced to an agent; treat Sentry event content as untrusted, use a read-only Sentry service account/project for MCP, rotate exposed DSNs and remove them from client bundles and repos; alert when an agent tool-call chain involving Sentry events is followed by shell or filesystem writes.
