---
schema: 1
kind: threat
title: FBI PSA260521 — Kali365 OAuth device-code PhaaS bypasses M365 MFA without credential capture
headline: FBI PSA260521 — Kali365 OAuth device-code PhaaS bypasses M365 MFA without credential capture
summary: "FBI PSA260521 warns on Kali365 — OAuth device-code PhaaS bypassing M365 MFA without credential capture. $250/month Telegram-distributed kit issues device codes via lures impersonating Adobe/DocuSign/SharePoint; secondary AiTM mode proxies session cookies; observed outcomes since April 2026 include mailbox exfiltration, lateral phishing, BEC fraud and ransomware pre-staging (The Register, 2026-05-22 · Help Net Security, 2026-05-22)."
discovered_at: "2026-05-23T05:00:03Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
  - organized-crime
regions:
  - global
sectors:
  - public-sector
  - finance
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.theregister.com/cyber-crime/2026/05/22/fbi-warns-of-kali365-as-device-code-phishing-soars/5245024"
    publisher: The Register
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/05/22/kali365-microsoft-365-phishing-fbi-warning/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://therecord.media/fbi-warns-of-kali365-phishing-attacks"
    publisher: The Record
    role: corroborating
  - url: "https://cyberscoop.com/fbi-phishing-kali365-microsoft365-access-tokens/"
    publisher: CyberScoop
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
migrated_from: briefs/2026-05-23.md
---

The FBI's Internet Crime Complaint Center issued PSA260521 on 2026-05-21 on **Kali365**, a Telegram-distributed Phishing-as-a-Service platform observed since April 2026 that abuses Microsoft's OAuth 2.0 device-code authorization flow (RFC 8628) to capture persistent access and refresh tokens for M365 accounts while completely bypassing multi-factor authentication ([The Register, 2026-05-22](https://www.theregister.com/cyber-crime/2026/05/22/fbi-warns-of-kali365-as-device-code-phishing-soars/5245024) · [Help Net Security, 2026-05-22](https://www.helpnetsecurity.com/2026/05/22/kali365-microsoft-365-phishing-fbi-warning/) · [The Record, 2026-05-22](https://therecord.media/fbi-warns-of-kali365-phishing-attacks) · [CyberScoop, 2026-05-22](https://cyberscoop.com/fbi-phishing-kali365-microsoft365-access-tokens/)). The technique falls under MITRE ATT&CK T1111 (MFA Interception) and T1528 (Steal Application Access Token) but differs structurally from credential phishing: the victim receives a lure impersonating Adobe Acrobat Sign, DocuSign or SharePoint, opens the embedded device code, and enters it on the legitimate `login.microsoftonline.com/common/oauth2/deviceauth` page; the attacker's registered device then receives both an access and a refresh token bound to that device, granting persistent access to Exchange Online, Teams, OneDrive and SharePoint without any further user interaction or MFA challenge.

A secondary AiTM mode proxies the victim's browser through attacker infrastructure to capture session cookies during a real Microsoft authentication flow when device-code is blocked. Subscriptions cost $250/month or $2,000/year per tenant; AI-generated lures are available in 14 languages with automated campaign templates and real-time tracking dashboards, lowering the technical bar for less capable actors. Observed outcomes since April 2026 — per the four outlets corroborating the FBI PSA — include mailbox exfiltration, lateral phishing, business email compromise and ransomware pre-staging. Detection vantage: Entra ID sign-in logs surface `authenticationProtocol = deviceCode` events — alert on those from unfamiliar device names or geographies inconsistent with the user's home location, and look for sign-in activity immediately after a device-code event from a different IP. Hardening: block user-interactive device-code flow via Conditional Access's `Authentication flows` condition (block / require compliant device), enforce FIDO2 phishing-resistant MFA for high-value accounts, and review existing OAuth app consents — public-sector tenants often leave device-code open for legacy device enrolment, and once an attacker holds a refresh token, only `Revoke-MgUserSignInSession` clears it.

**Why it matters to us:** the device-code attack path is the single fastest M365 compromise vector that classic phishing-aware users still walk into; Swiss federal, cantonal and public-administration Entra tenants often leave the flow open for kiosk / shared-device enrolment, and the Kali365 commoditisation means small actors can now run it without M365 expertise.
