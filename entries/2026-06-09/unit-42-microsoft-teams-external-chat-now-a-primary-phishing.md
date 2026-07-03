---
schema: 1
kind: research
horizon: operational
title: "Unit 42: Microsoft Teams external-chat now a primary phishing surface for APT29 and UNC6692"
headline: "Unit 42: Microsoft Teams external-chat now a primary phishing surface for APT29 and UNC6692"
summary: "Microsoft Teams external chat is now ~42% of phishing alerts in Cortex, driven by APT29 (Cloaked Ursa) and UNC6692 IT-support impersonation — a configuration-hardening problem, not a patch (Unit 42, 2026-06-08)."
discovered_at: "2026-06-09T05:00:04Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: high
immediate_action: null
tags:
  - phishing
  - nation-state
  - identity
  - espionage
  - russia-nexus
regions:
  - global
sectors:
  - public-sector
  - finance
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/microsoft-teams-phishing/"
    publisher: Unit 42 — Microsoft Teams phishing
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/unc6692-social-engineering-custom-malware"
    publisher: Mandiant — UNC6692
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
migrated_from: briefs/2026-06-09.md
---

Unit 42 reports that collaboration-platform phishing reached 42% of all phishing alerts in Cortex in the first four months of 2026, up from 30% in the preceding period, with Microsoft Teams external messaging the dominant vector ([Unit 42, 2026-06-08](https://unit42.paloaltonetworks.com/microsoft-teams-phishing/)). Two clusters dominate: Cloaked Ursa (APT29 / Midnight Blizzard) uses previously-compromised M365 tenants — often small-business accounts — to stand up IT-support-styled domains, then sends Teams messages requesting MFA approval or credential re-entry under an account-maintenance pretext. UNC6692 floods inboxes to manufacture urgency, then poses as IT support over Teams, ultimately delivering the SNOW suite — SNOWBELT (browser-extension backdoor), SNOWGLAZE (WebSocket tunneler) and SNOWBASIN (persistent backdoor) — after dumping LSASS via Task Manager (T1003.001) and moving laterally with Pass-the-Hash (T1550.002) ([Mandiant, 2026-04-23](https://cloud.google.com/blog/topics/threat-intelligence/unc6692-social-engineering-custom-malware)). The root enabler is the default Teams configuration permitting unrestricted external-tenant messaging.

**Why it matters to us:** Hardening is configuration, not patching — restrict external access in the Teams Admin Center to explicitly-allowed partner domains and disable unmanaged/consumer-account chat. Detection concepts: Entra ID sign-in logs for logons originating from external M365 tenants; Teams activity logs for `ExternalUserJoined` events followed by rapid file/link shares; MDI alerts on MFA anomalies after cross-tenant contact. Extend AiTM-aware Conditional Access to Teams sign-in contexts.
