---
schema: 1
kind: research
title: "AutoJack — Microsoft shows a single web page can drive host RCE through an AI agent's local MCP server"
headline: "AutoJack — Microsoft shows a single web page can drive host RCE through an AI agent's local MCP server"
summary: "Microsoft Security researchers disclosed AutoJack on 2026-06-18, a three-weakness chain against AutoGen Studio's Model Context Protocol (MCP) WebSocket surface that lets a malicious web page rendered by a local AI browsing agent execute arbitrary commands on the host (Microsoft Security Blog, 2026-06-18)."
discovered_at: "2026-06-20T05:12:17Z"
event_date: 2026-06-19
run_id: 2026-06-20-4cfd00ef
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - ai-abuse
  - rce
  - poc-public
regions:
  - global
sectors:
  - technology
entities:
  - "trend:autojack-mcp-websocket-rce"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/"
    publisher: Microsoft Security Blog
    role: primary
  - url: "https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html"
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
migrated_from: briefs/2026-06-20.md
---

Microsoft Security researchers disclosed AutoJack on 2026-06-18, a three-weakness chain against AutoGen Studio's Model Context Protocol (MCP) WebSocket surface that lets a malicious web page rendered by a local AI browsing agent execute arbitrary commands on the host ([Microsoft Security Blog, 2026-06-18](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/)). The chain: (1) the WebSocket origin allowlist accepts a locally-running browsing agent's localhost identity (CWE-1385 missing origin validation); (2) the auth middleware exempts all `/api/mcp/*` paths (CWE-306 missing authentication); (3) the MCP handler base64-decodes a `server_params` URL query parameter and passes it to OS process execution (CWE-78 OS command injection). The flaw existed only in pre-release PyPI builds `0.4.3.dev1`/`0.4.3.dev2` — the stable `0.4.2.2` was never affected — and was fixed before public release; no in-the-wild exploitation was observed ([The Hacker News, 2026-06-19](https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html)).

**Why it matters to us:** The specific package never shipped, but the pattern — origin-bypass → unauthenticated local API → executable parameter — generalises to any agentic framework exposing a local WebSocket/MCP endpoint to browsing agents. Teams piloting MCP-based tooling should validate Origin headers on all localhost WebSocket servers, require authentication on every path, refuse executable parameters via URL query strings, and run agent frameworks in sandboxes rather than on developer workstations.
