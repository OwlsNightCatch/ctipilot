---
schema: 1
kind: research
title: "Check Point chains SQL injection to RCE in LangGraph's checkpointer (CVE-2025-67644 + CVE-2026-28277)"
headline: "Check Point chains SQL injection to RCE in LangGraph's checkpointer (CVE-2025-67644 + CVE-2026-28277)"
summary: "Check Point Research disclosed a vulnerability chain in LangGraph, the open-source stateful-agent framework published under LangChain (Check Point Research, 2026-06-11)."
discovered_at: "2026-06-13T05:00:04Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - supply-chain
  - ai-abuse
  - rce
  - sqli
regions:
  - global
sectors:
  - technology
entities: []
cves:
  - id: CVE-2025-67644
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-28277
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
  - id: CVE-2026-27022
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - patch-available
sources:
  - url: "https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/"
    publisher: Check Point Research
    role: primary
  - url: "https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html"
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
migrated_from: briefs/2026-06-13.md
---

Check Point Research disclosed a vulnerability chain in LangGraph, the open-source stateful-agent framework published under LangChain ([Check Point Research, 2026-06-11](https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/)). CVE-2025-67644 is a SQL injection in the SQLite checkpointer's `get_state_history()` function, which interpolates user-controlled metadata filter keys directly into SQL without sanitisation. Chained with CVE-2026-28277, an unsafe msgpack deserialization in checkpoint loading, an attacker injects a crafted checkpoint row via the SQLi and triggers arbitrary Python module import and command execution when the application later loads that checkpoint — full server-side RCE ([The Hacker News, 2026-06-12](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)). A parallel SQLi in the Redis checkpointer is tracked as CVE-2026-27022. Exploitation requires a self-hosted deployment using the SQLite or Redis checkpointer that exposes `get_state_history()` to user-controlled filter input; PostgreSQL-backed deployments and LangChain's managed LangSmith cloud are not affected. Per Check Point, the fixes shipped in `langgraph-checkpoint-sqlite` 3.0.1 (CVE-2025-67644), `langgraph` 1.0.10 (CVE-2026-28277) and `langgraph-checkpoint-redis` 1.0.2 (CVE-2026-27022). Maps to T1190 and T1059.006. This is the substantive technical disclosure behind the agentic-AI attack surface that Swiss/EU public-sector AI pilots are increasingly building on. Defender action: pin the fixed versions, treat `get_state_history()` filter input as untrusted even in internal tooling, and never expose the state-history API unauthenticated.
