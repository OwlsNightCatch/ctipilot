---
schema: 1
kind: threat
horizon: operational
title: "CERT-FR CERTFR-2026-ACT-016: Agentic AI tools introduce prompt-injection and supply-chain attack surfaces"
headline: "CERT-FR CERTFR-2026-ACT-016: Agentic AI tools introduce prompt-injection and supply-chain attack surfaces"
summary: "France's CERT-FR published advisory CERTFR-2026-ACT-016 warning that deploying agentic AI orchestration platforms (LLM-driven workflows with tool-calling, MCP server integration, or autonomous execution capabilities) introduces novel attack vectors."
discovered_at: "2026-05-08T05:00:06Z"
event_date: null
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
regions:
  - europe
sectors: []
entities:
  - "campaign:certfr-2026-act-016"
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/"
    publisher: CERT-FR — CERTFR-2026-ACT-016
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-08.md
---

France's CERT-FR published advisory CERTFR-2026-ACT-016 warning that deploying agentic AI orchestration platforms (LLM-driven workflows with tool-calling, MCP server integration, or autonomous execution capabilities) introduces novel attack vectors. The advisory identifies three risk classes: **prompt-injection via processed documents or websites** (attacker embeds instructions in content the agent processes, redirecting its actions); **MCP server supply-chain compromise** (a malicious or compromised Model Context Protocol server can issue instructions to all connected agents); and **insufficient sandboxing** of agent execution environments, where agents with filesystem or network access can be weaponised. CERT-FR recommends input/output guardrails, strict allowlisting of permitted tool calls, human-in-the-loop gates for high-impact actions, and treating all AI agent outputs as untrusted until validated. Relevant for organisations deploying Claude Agents, Microsoft Copilot Studio, AutoGen, or similar agentic frameworks for workflow automation.
