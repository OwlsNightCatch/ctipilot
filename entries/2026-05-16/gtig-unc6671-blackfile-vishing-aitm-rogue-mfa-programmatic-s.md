---
schema: 1
kind: incident
title: "GTIG: UNC6671 \"BlackFile\" vishing → AiTM → rogue-MFA → programmatic SharePoint exfiltration (1M+ files from one victim); DLS shutdown signals possible rebrand"
headline: "GTIG: UNC6671 \"BlackFile\" vishing → AiTM → rogue-MFA → programmatic SharePoint exfiltration (1M+ files from one victim); DLS shutdown signals possible rebrand"
summary: "GTIG analyses UNC6671 \"BlackFile\" vishing-driven AiTM extortion: real-time helpdesk impersonation → attacker-registered lookalike SSO portals → live MFA code capture and rogue MFA device registration → programmatic SharePoint exfiltration (1M+ files from one victim) via Python requests spoofing the Microsoft Office ClientAppId; DLS shutdown signals possible rebrand (Google Threat Intelligence Group, 2026-05-15)."
discovered_at: "2026-05-16T05:00:01Z"
event_date: 2026-05-15
run_id: 2026-05-16-5bc123a0
priority: notable
immediate_action: null
tags:
  - organized-crime
  - phishing
  - identity
  - cloud
  - data-breach
regions:
  - global
sectors: []
entities:
  - "actor:unc6671"
techniques: [T1566, T1566.004, T1557, T1111, T1556, T1098.005, T1539, T1550.004, T1213.002, T1530]
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
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-16.md
updates:
  - at: "2026-09-30T06:54:43Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      GTIG's leak-site assessment is corrected from probable rebrand to a possible transition phase.
      The detection guidance now follows GTIG's own: the spoofed Office ClientAppId sat on
      FileDownloaded records, and new MFA registrations are suspicious after failed or abandoned
      challenges. Reuse of captured session cookies replaces an unsupported token-theft mapping, and
      the title and summary no longer present the one-victim figure of over a million files as a
      norm. An attacker-controlled domain, inline ATT&CK ids, an unsourced conditional-access
      recommendation, the context-only ShinyHunters link and three victim sectors GTIG does not name
      are removed. Priority is lowered to notable because the targeting GTIG reports is in North America, Australia and the UK, and the entry gains an ATT&CK mapping.
    fields: [body, classification, techniques, title, headline, summary, priority, entities, sectors]
---

Google Threat Intelligence Group published on 2026-05-15 an analysis of UNC6671, a financially motivated extortion cluster that adopted the "BlackFile" brand by February 2026 and has targeted dozens of organizations across North America, Australia and the UK ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). Callers hired by the actor phone employees' personal mobile numbers, pose as internal IT or helpdesk staff citing a passkey migration or MFA update, and send the victim to a lookalike single sign-on portal on Tucows-registered domains, lately as organization-named subdomains with "passkey" or "enrollment" themes ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The operator relays the credentials and the MFA code or push approval to the real SSO provider in real time, then immediately registers a new attacker-controlled MFA device for persistence ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). GTIG stresses that these compromises come from social engineering, not a vendor vulnerability ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

After access, the actor moves into connected SaaS applications (SharePoint, OneDrive, Zendesk, Salesforce), searches for strings such as "confidential" and "SSN", and exfiltrates with Python requests and PowerShell scripts through Microsoft Graph and direct HTTP GET requests against document URLs, reusing session cookies (for example FedAuth) captured during the vishing phase ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). In one case the script downloaded more than a million files from SharePoint and OneDrive ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The direct-fetch method is often logged as `FileAccessed` rather than `FileDownloaded`, so it slips past SOCs that treat `FileAccessed` as benign ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). In early intrusions the `FileDownloaded` records carried a spoofed Microsoft Office `ClientAppId`, which GTIG says served to bypass basic conditional access filters, while the user-agent showed `python-requests` or `WindowsPowerShell` ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). In later intrusions the `FileAccessed` records named `python-requests` as the client application in `AppAccessContext` ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The sessions came from commercial VPN exit nodes and hosting providers ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

The BlackFile leak site went offline in late April 2026, came back on 2026-05-11 with a message that BlackFile "is shutting down… under this name", and was inaccessible at publication ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). GTIG reads this as a possible transition phase rather than a permanent cessation, noting that extortion clusters commonly rebrand or disperse after shutdowns ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). GTIG assesses UNC6671 as independent of ShinyHunters (UNC6240), although UNC6671 co-opted the ShinyHunters brand at least once ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

**Detection:** in identity-provider logs, look for new MFA factor registrations (Okta `system.multifactor.factor.setup`) immediately preceded by failed MFA authentications or abandoned challenges ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). In Microsoft 365 audit logs, weigh `FileAccessed` as heavily as `FileDownloaded` when the user-agent is a scripting library or command-line tool, and flag `FileAccessed` bursts faster than a person can browse or whose `AppAccessContext` shows a headless client ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

**Triage:** an Office client identity paired with a scripting-library user-agent is the mismatch GTIG found, and GTIG reads it as scripted access rather than a person using SharePoint ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). A session source on a commercial VPN or hosting provider that is unusual for the user adds weight ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

**Defender takeaway:** move users who can be reached by a fake helpdesk call from SMS and push MFA to FIDO2 security keys or passkeys, which GTIG says resist this AiTM and vishing chain ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).

## Correction — 2026-09-30T06:54:43Z

GTIG describes the leak-site shutdown as a possible transition phase rather than a permanent cessation, not as a probable rebrand ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The detection guidance is corrected to GTIG's own: the spoofed Microsoft Office `ClientAppId` appeared on `FileDownloaded` records, later `FileAccessed` records named `python-requests` as the client, and new MFA factor registrations are suspicious when immediately preceded by failed or abandoned MFA challenges ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The actor reused captured session cookies such as FedAuth, and GTIG does not describe theft of application access tokens ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).
