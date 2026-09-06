---
schema: 1
kind: threat
title: PRC UNC6508 ran year-plus espionage through internet-facing REDCap servers and a Google Workspace BCC rule
headline: PRC UNC6508 ran year-plus espionage through internet-facing REDCap servers and a Google Workspace BCC rule
summary: "PRC actor UNC6508 ran year-plus espionage through internet-facing REDCap research servers and abused a Google Workspace content-compliance rule to silently BCC research/defence email to attacker Gmail — REDCap is widely run at Swiss/EU academic medical centres. (Google GTIG, 2026-06-15)"
discovered_at: "2026-06-16T05:08:53Z"
event_date: 2026-06-15
run_id: 2026-06-16-38d638e1
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - identity
  - china-nexus
regions:
  - global
  - europe
sectors:
  - healthcare
  - education
  - defense
entities: []
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research"
    publisher: Google GTIG
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/15/chinese-hackers-redcap-medical-research-institutions-breach/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/"
    publisher: SecurityWeek
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
migrated_from: briefs/2026-06-16.md
---

Google's Threat Intelligence Group attributes a September 2023 – November 2025 espionage campaign to **UNC6508**, a PRC-nexus cluster that compromised North American academic, medical and military-health organisations by exploiting externally-facing **REDCap** (Research Electronic Data Capture) servers, then dropping a bespoke PHP implant tracked as **INFINITERED** ([Google GTIG, 2026-06-15](https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research)). INFINITERED trojanises REDCap's own upgrade mechanism to survive platform updates, harvests credentials from the REDCap login page, and exposes a cookie-gated backdoor for shell, file, SQL and credential operations ([Help Net Security, 2026-06-15](https://www.helpnetsecurity.com/2026/06/15/chinese-hackers-redcap-medical-research-institutions-breach/)). The exfiltration tradecraft is the notable part: after pivoting to a Workspace admin account, the actor created a Google Workspace **content-compliance rule named "Patroit"** that silently BCC-forwarded any message matching ~150 research/defence keywords to an attacker-controlled Gmail address — abusing a legitimate administrative feature rather than dropping exfiltration malware (`T1114.003` Email Forwarding Rule), which evades most DLP that watches for new tooling ([SecurityWeek, 2026-06-15](https://www.securityweek.com/chinese-hackers-target-medical-military-and-ai-research-in-north-america/)). Initial access mapped to `T1190`; web-shell persistence to `T1505.003`; admin credential reuse to `T1078`.

**Why it matters to us:** REDCap is deployed across Swiss and EU university hospitals, cantonal research bodies and clinical-trial coordinators, and the Workspace BCC-rule technique is tenant-agnostic. Hunt now: Google Workspace admin audit logs for content-compliance/BCC rule creation by non-IT-admin accounts (especially rules with external Gmail recipients), and file-integrity-monitor the REDCap upgrade-staging directory and login handlers — standard web-root scanning misses the upgrade-path implant.
