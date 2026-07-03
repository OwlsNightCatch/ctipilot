---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "CERT-FR CERTFR-2026-ACT-016 — agentic AI three-risk-class advisory; defender obligations explicit"
headline: "CERT-FR CERTFR-2026-ACT-016 — agentic AI three-risk-class advisory; defender obligations explicit"
summary: "CERT-FR's advisory (dated 13 April 2026, surfaced in this week's daily on 2026-05-08) names three operational risk classes for organisations deploying agentic AI orchestration platforms (Claude Agents, Microsoft Copilot Studio, AutoGen, MCP-server architectures): **prompt injection via processed documents or …"
discovered_at: "2026-05-04T05:00:43Z"
event_date: 2026-05-08
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
  - vulnerabilities
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
migrated_from: briefs/weekly/2026-W19.md
---

CERT-FR's advisory (dated 13 April 2026, surfaced in this week's daily on 2026-05-08) names three operational risk classes for organisations deploying agentic AI orchestration platforms (Claude Agents, Microsoft Copilot Studio, AutoGen, MCP-server architectures): **prompt injection via processed documents or websites** (attacker embeds instructions in content the agent processes, redirecting its actions); **MCP server supply-chain compromise** (a malicious or compromised Model Context Protocol server can issue instructions to all connected agents); and **insufficient sandboxing** of agent execution environments. CERT-FR recommendations: input/output guardrails, strict allowlisting of permitted tool calls, human-in-the-loop gates for high-impact actions, and treating all AI agent outputs as untrusted until validated ([CERT-FR — CERTFR-2026-ACT-016, 2026-05-08](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/) · [daily 2026-05-08](/briefs/2026-05-08/)). **Why this is obligations-changing rather than routine advisory:** for French public-sector entities deploying agentic AI, CERT-FR advisories establish the baseline a defendable-control posture is measured against. The Microsoft Semantic Kernel CVE-2026-26030 / CVE-2026-25592 pair (§ 3 deep dive) is the worked-example of CERT-FR's first and third risk classes manifesting as concrete vendor CVEs — defenders deploying any agentic-AI framework should treat the CERT-FR advisory as defining the question-set, not the answer-set.
