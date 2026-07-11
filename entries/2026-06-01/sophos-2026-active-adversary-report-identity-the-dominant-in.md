---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "Sophos 2026 Active Adversary Report — identity the dominant intrusion root cause; Impacket and AnyDesk most-observed post-exploitation"
headline: "Sophos 2026 Active Adversary Report — identity the dominant intrusion root cause; Impacket and AnyDesk most-observed post-exploitation"
summary: "Published 2 June (Sophos X-Ops; drawing on 661 IR/MDR cases; daily 2026-06-03)."
discovered_at: "2026-06-01T05:00:17Z"
event_date: 2026-06-03
run_id: 2026-W23-9118e7bd
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
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report"
    publisher: Sophos X-Ops 2026 Active Adversary Report
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
migrated_from: briefs/weekly/2026-W23.md
---

Published 2 June ([Sophos X-Ops](https://www.sophos.com/en-us/blog/2026-sophos-active-adversary-report); drawing on 661 IR/MDR cases; [daily 2026-06-03](/briefs/2026-06-03/)). The findings that directly shift defender priorities: identity-based compromise — stolen/valid credentials, brute force, phishing — is the **leading intrusion root cause**, with missing or misconfigured MFA present in a majority of incidents. Time from initial access to Active Directory compromise has compressed materially. **Impacket** is among the most frequently observed post-exploitation toolkits; **AnyDesk** is the most-abused legitimate remote-access tool, consistent with this week's Luna Moth tradecraft. The recurring telemetry blind spots are the load-bearing findings: firewall logs were missing in roughly **half** of ransomware cases, and a meaningful share of compromised Windows Servers were running end-of-life builds. Practical hunt targets: alert on Impacket artefacts (impacket-named tool processes, `secretsdump`-style NTDS access, `SMBExec`/`WMIExec` parent processes); instrument the initial-access-to-DC-compromise window; inventory EOL Windows Servers; verify firewall log retention is complete before an incident, not during one. This is a single-vendor IR report; treat findings as directionally correct rather than statistically definitive without independent corroboration. `[SINGLE-SOURCE]`
