---
schema: 1
kind: annual-report
title: "Microsoft Email Threat Landscape Q3 2026: tenant and user overrides delivered spoofed business-service mail that failed authentication, SVG attachments return as CAPTCHA-phishing carriers, and Teams impersonators move to ordinary personal names"
headline: "Microsoft Q3 email report: overrides let authentication-failing spoofed mail through; SVG CAPTCHA phishing returns"
summary: >
  Microsoft's Q3 2026 email-threat report finds that many malicious messages spoofing the sender domains of business services were delivered despite failing authentication because tenant-
  or user-level overrides applied, 63% of the messages with a recorded security outcome in September. It also reports SVG attachments leading CAPTCHA-gated phishing at quarter end, Teams
  impersonators shifting from help-desk display names to ordinary personal names, and an August device-code phishing campaign that used a QR code in a Word document against legal organisations.
discovered_at: "2026-11-06T03:48:00Z"
updated_at: null
event_date: "2026-11-05"
run_id: 2026-11-06T0255Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global]
sectors: []
entities: ["report:microsoft-email-threat-landscape-q3-2026", "product:microsoft-365", "product:microsoft-teams", "product:microsoft-defender-for-office-365"]
techniques: [T1566.001, T1566.002, T1566.004, T1528]
affected_products: ["Microsoft 365", "Microsoft Teams", "Microsoft Defender for Office 365"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-11-05"
    role: primary
closed_sources: []
evidence:
  - quote: "In September, overrides applied to 63% of messages with a recorded security outcome, with tenant-level overrides accounting for most of them."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/"
  - quote: "The figures do not establish that recipients opened the messages or that accounts were compromised."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/"
verification: single-source
sourcing_note: >
  First-party vendor threat-landscape report drawn from Microsoft's own telemetry, single-source by nature; the shares are share-of-month figures from that sample. Aggregate volume totals are left out as vendor-scale metrics, and the mitigations are Microsoft's own.
confidence: medium
references:
  - 2026-07-25/microsoft-email-threat-landscape-q2-2026-teams-vishing-surge
  - 2026-11-05/vaud-m365-device-code-phishing-campaign-romandie
  - 2026-10-23/m365-token-spray-replay-rogue-entra-devices-mfa-wipe
  - 2026-10-31/teams-help-desk-impersonation-quick-assist-ad-cs-esc1-esc8
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Microsoft Threat Intelligence's report on Q3 2026 draws four points that matter to a Microsoft 365 defender ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)). First, malicious messages that spoof the sender domains of business services, such as document-signing and survey platforms, were often delivered because tenant- or user-level overrides applied, even after the messages failed email authentication and were identified as malicious: in September overrides applied to 63% of messages with a recorded security outcome, most of them tenant-level ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)). Microsoft says the figures do not show that recipients opened the messages and that an overly broad exception made for a legitimate workflow can weaken protection against messages impersonating it ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)).

Second, CAPTCHA-gated phishing recovered while QR-code phishing kept falling, with SVG attachments central to the recovery: they carried 65% of CAPTCHA-gated attacks in August and 49% in September ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)). Third, in Teams, ordinary personal-name display names rose from 46% of the observed July sample to 88% in September while explicit help-desk identities fell from 17% to 2%; Microsoft notes a personal name can accompany a help-desk claim while the account address keeps technical wording, and that more targeted attempts used domains resembling the victim organisation's ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)). Fourth, an August campaign against legal organisations sent a Word document with a personalised QR code that led to a device-code phishing page and the genuine Microsoft device sign-in portal; completing the sign-in would have transferred a valid session token that gave persistent access without exposing the password or re-triggering MFA ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)).

**Exposure:** a Microsoft 365 tenant that has tenant- or user-level allow or override entries covering the sender domains of widely used business services, since a message that fails authentication and is detected as malicious can still be delivered when such an override applies.

**Detection:** in mail-flow and message-trace telemetry, delivered messages that claim a business service's domain but fail SPF, DKIM and DMARC, together with the override that applied; in mail-gateway logs, SVG attachments that lead to a CAPTCHA page; in Teams audit, first-contact chats and calls from external tenants whose display name is a personal name but whose account address carries help-desk or service wording; in sign-in logs, device-code flow sign-ins.

**Defender takeaway:** review the tenant and user overrides in your mail protection for entries that cover well-known service sender domains, because the override, not the detection, decided delivery; Microsoft's own advice is to check its recommended settings for Exchange Online Protection and Defender for Office 365 ([Microsoft Threat Intelligence, 2026-11-05](https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/)).
