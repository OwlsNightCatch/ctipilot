---
schema: 1
kind: incident
horizon: operational
title: "GTIG: UNC6671 \"BlackFile\" vishing → AiTM → rogue-MFA → programmatic SharePoint exfiltration of 1M+ files per victim; DLS shutdown signals probable rebrand"
headline: "GTIG: UNC6671 \"BlackFile\" vishing → AiTM → rogue-MFA → programmatic SharePoint exfiltration of 1M+ files per victim; DLS shutdown signals probable rebrand"
summary: "GTIG analyses UNC6671 \"BlackFile\" vishing-driven AiTM extortion: real-time helpdesk impersonation → attacker-registered lookalike SSO portals → MFA token capture and rogue MFA device registration → programmatic SharePoint exfiltration of 1M+ files per victim via Python requests spoofing the Microsoft Office ClientAppId; DLS shutdown signals probable rebrand (Google Threat Intelligence Group, 2026-05-15)."
discovered_at: "2026-05-16T05:00:01Z"
event_date: 2026-05-15
run_id: 2026-05-16-5bc123a0
priority: high
immediate_action: null
tags:
  - organized-crime
  - phishing
  - identity
  - cloud
  - data-breach
regions:
  - global
sectors:
  - finance
  - technology
  - healthcare
entities:
  - "report:gtig-europe-2025"
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/"
    publisher: "Google Threat Intelligence Group, 2026-05-15"
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
migrated_from: briefs/2026-05-16.md
---

Google Threat Intelligence Group published on 2026-05-15 an analysis of UNC6671 — a financially-motivated extortion cluster operating under the "BlackFile" brand since February 2026 — documenting a real-time vishing + adversary-in-the-middle chain that bypasses traditional MFA and pivots to mass SharePoint exfiltration ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The chain starts with a phone call placed to a victim's personal mobile number in which an operator impersonates internal IT helpdesk and directs the target to an attacker-registered lookalike single sign-on portal (Tucows-registered hostnames in the `<org>.enrollms[.]com` and `<org>.passkeyms[.]com` namespaces); the operator captures credentials and TOTP / push approvals live and **immediately registers a new attacker-controlled MFA device** for persistent post-vishing access, mapping to [T1556](https://attack.mitre.org/techniques/T1556/) Modify Authentication Process. Post-compromise, BlackFile uses Python `requests` and PowerShell scripts against the Microsoft Graph API and direct SharePoint file-stream URLs to exfiltrate, with single-victim file counts exceeding one million; the API requests surface Microsoft Office's `ClientAppId` (`d3590ed6-52b3-4102-aeff-aad2292ab01c`) in the M365 audit log `AppAccessContext` field — the same value legitimate Office clients carry — to blend in with normal Office activity. The detection break is the underlying user-agent: legitimate Office clients do not present `python-requests/2.28.1` or `WindowsPowerShell/5.1` as the user-agent header against Graph or SharePoint endpoints. GTIG also notes that the `FileAccessed` audit event distinguishes the bulk-API extraction pattern from interactive `FileDownloaded` events. Geographic focus is North America, Australia, and the UK — but the playbook is language-agnostic; any European helpdesk-fronted M365 / Okta environment is one successful call away from the same outcome. The BlackFile data-leak site went offline in late April 2026 and relaunched on 2026-05-11 with a shutdown announcement, which GTIG assesses as probable rebrand rather than cessation. GTIG explicitly distinguishes UNC6671 from ShinyHunters (UNC6240). MITRE ATT&CK additionally: [T1566.004](https://attack.mitre.org/techniques/T1566/004/) Spearphishing Voice, [T1557](https://attack.mitre.org/techniques/T1557/) Adversary-in-the-Middle, [T1528](https://attack.mitre.org/techniques/T1528/) Steal Application Access Token. Detection priorities: alert on Okta `system.multifactor.factor.setup` events not preceded by a user-initiated session; flag M365 audit `FileAccessed` events with `AppAccessContext.ClientAppId == d3590ed6-52b3-4102-aeff-aad2292ab01c` AND a user-agent containing `python-requests` or `PowerShell`; require Conditional Access compliant-device for Graph API access from administrative accounts; and move helpdesk-privileged accounts to FIDO2 phishing-resistant MFA.
