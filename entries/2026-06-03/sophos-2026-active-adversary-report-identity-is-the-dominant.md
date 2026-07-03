---
schema: 1
kind: annual-report
horizon: operational
title: "Sophos 2026 Active Adversary Report: identity is the dominant intrusion root cause"
headline: "Sophos 2026 Active Adversary Report: identity is the dominant intrusion root cause"
summary: "Sophos published its 2026 Active Adversary Report (drawing on 661 IR/MDR cases) on 2026-06-02 (Sophos X-Ops, 2026-06-02)."
discovered_at: "2026-06-03T05:00:05Z"
event_date: 2026-06-02
run_id: 2026-06-03-ee0eae61
priority: notable
immediate_action: null
tags:
  - ransomware
  - identity
  - organized-crime
regions:
  - global
sectors:
  - public-sector
  - finance
  - manufacturing
entities:
  - "report:sophos-active-adversary-2026"
  - "campaign:underground-ai-adoption-sophos"
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report"
    publisher: Sophos X-Ops
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-03.md
---

Sophos published its 2026 Active Adversary Report (drawing on 661 IR/MDR cases) on 2026-06-02 ([Sophos X-Ops, 2026-06-02](https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report)). Per PD-9 this report gets one treatment; the findings that change defender priorities rather than the survey scorecard: identity-based compromise — stolen/valid credentials, brute force, and phishing — was the leading root cause, and missing or misconfigured MFA was present in a majority of incidents. Time from initial access to Active Directory compromise has compressed materially, with `Impacket` among the most frequently observed post-exploitation toolkits and `AnyDesk` the most-abused legitimate remote-access tool. The recurring telemetry blind spots are the actionable part: firewall logs were missing in roughly half of ransomware cases, and a meaningful share of compromised Windows Servers were running end-of-life builds. [SINGLE-SOURCE] (vendor IR telemetry report).

**Why it matters to us:** The hunt targets generalise directly to public-sector AD estates — alert on `Impacket` artefacts (impacket-* tool names in process trees, `secretsdump`-style NTDS access, `SMBExec`/`WMIExec` parent processes), instrument the initial-access-to-DC-compromise window, inventory EOL Windows Servers, and verify firewall log retention before an incident rather than during one.
