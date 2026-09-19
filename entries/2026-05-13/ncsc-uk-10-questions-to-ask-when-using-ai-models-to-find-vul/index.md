---
schema: 1
kind: research
title: "NCSC-UK — \"10 questions to ask when using AI models to find vulnerabilities\""
headline: "NCSC-UK — \"10 questions to ask when using AI models to find vulnerabilities\""
summary: "NCSC-UK published an operational 10-question checklist on 2026-05-11 (authored by Ruth C, Head of Vulnerability Management Group) for organisations evaluating or deploying AI / LLM tooling for vulnerability discovery (NCSC-UK blog, 2026-05-11)."
discovered_at: "2026-05-13T05:00:10Z"
event_date: 2026-05-11
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - vulnerabilities
regions:
  - uk
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities"
    publisher: "NCSC-UK blog, 2026-05-11"
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
migrated_from: briefs/2026-05-13.md
---

NCSC-UK published an operational 10-question checklist on 2026-05-11 (authored by Ruth C, Head of Vulnerability Management Group) for organisations evaluating or deploying AI / LLM tooling for vulnerability discovery ([NCSC-UK blog, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)). The guidance is substantively different from the previously-covered NCSC-CH BACS strategic assessment: it is process- and infrastructure-flavoured rather than landscape-flavoured. The ten questions interrogate (a) **process prerequisites** — is there a triage / remediation pipeline that can absorb what the AI surfaces, or will the backlog simply grow while team capacity stays flat; (b) **data governance** — what code, infrastructure and secrets is the model being given access to; (c) **infrastructure security** — is the AI agent sandboxed from production; (d) **permissions blast-radius** — has the model been granted excessive permissions that magnify attacker reach if the agent itself is compromised; (e) legal / data-retention; (f) false-positive overhead on the blue team. The piece explicitly warns that **AI-accelerated vulnerability discovery without matching remediation capacity makes the organisation worse off, not better** — a direct critique of "buy the AI tool" patterns. [SINGLE-SOURCE]
