---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Research: the AI agent and toolchain control plane became a concrete attack-surface class this week"
headline: "Research: the AI agent and toolchain control plane became a concrete attack-surface class this week"
summary: "The AI agent/toolchain control plane became a concrete attack surface — Microsoft's AutoJack (web page → host RCE via an agent's MCP socket) capped a week of LiteLLM, Copilot SearchLeak, Vertex AI and JetBrains-plugin disclosures. (daily 06-20, Microsoft)"
discovered_at: "2026-06-22T00:14:56Z"
event_date: 2026-06-18
run_id: 2026-W25-0aacfe65
priority: high
immediate_action: null
tags:
  - ai-abuse
  - cloud
  - vulnerabilities
  - supply-chain
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:underground-ai-adoption-sophos"
  - "trend:autojack-mcp-websocket-rce"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/"
    publisher: Microsoft Security — AutoJack
    role: primary
  - url: "https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce"
    publisher: Obsidian — LiteLLM
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/"
    publisher: Unit 42 — Vertex AI
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-2473, CVE-2026-42824)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W25.md
---

The week's single most important research synthesis is that the AI developer toolchain — gateways, agents, IDE plugins and the Model Context Protocol — stopped being a theoretical risk and accumulated a cluster of working exploit chains. Microsoft's **AutoJack** showed a single malicious web page can drive host-level RCE through an AI browsing agent's local MCP WebSocket: a three-flaw chain in AutoGen Studio (origin-allowlist bypass, missing auth on `/api/mcp/*`, and OS command injection via `StdioServerParams`) lets an attacker-steered agent reach a privileged localhost socket and execute arbitrary host processes ([Microsoft Security, 2026-06-18](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/); [daily 06-20](/briefs/2026-06-20/)). That sits alongside the week's other AI-surface disclosures: Obsidian Security's three-CVE LiteLLM chain turning any gateway user into root ([Obsidian, 2026-06-16](https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce); [daily 06-16](/briefs/2026-06-16/)), Varonis "SearchLeak" one-click M365 Copilot data exfiltration (CVE-2026-42824) ([Varonis](https://www.varonis.com/blog/searchleak); [daily 06-16](/briefs/2026-06-16/)), Unit 42's "Pickle in the Middle" cross-tenant code execution in Google Vertex AI (CVE-2026-2473) ([Unit 42](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/); [daily 06-17](/briefs/2026-06-17/)), and 15 malicious JetBrains Marketplace plugins exfiltrating AI-provider API keys ([Aikido](https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys); [daily 06-18](/briefs/2026-06-18/)). Sophos X-Ops' underground-AI report ([daily 06-19](/briefs/2026-06-19/)) confirms criminal interest in exactly these agent frameworks. The defender takeaway for CH/EU public-sector teams adopting AI tooling: treat self-hosted AI gateways and agent frameworks as internet-adjacent application servers — bind MCP/agent sockets to loopback behind a host firewall, run them under low-privilege isolated accounts, never on shared or production hosts, and rotate the API keys and cloud credentials these tools concentrate.
