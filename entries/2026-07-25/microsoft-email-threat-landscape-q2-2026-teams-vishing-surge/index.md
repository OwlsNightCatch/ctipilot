---
schema: 1
kind: annual-report
title: "Microsoft Email Threat Landscape Q2 2026: phishing moves off email into Teams vishing, and attachment lures drift PDF → DOCX"
headline: "Microsoft's quarterly email report flags a sustained shift of social engineering into Teams voice-phishing"
summary: >
  Microsoft's Q2 2026 email-threat report quantifies two operationally relevant shifts for M365 tenants:
  Teams-based voice-phishing (vishing) reached roughly ten times its mid-2025 weekly baseline by quarter-end,
  and phishing attachment delivery drifted from PDF toward DOC/DOCX as a detection-evasion move. Credential
  theft remained the objective of 94-96% of payload-based attacks. Includes two concrete campaigns: an
  automated BEC via Python-scripted Amazon SES and an EML/OAuth-redirect chain delivering a BAT dropper.
discovered_at: "2026-07-25T04:38:26Z"
event_date: "2026-07-23"
run_id: 2026-07-25T0409Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global]
sectors: [public-sector, finance, telco]
entities: [report:microsoft-email-threat-landscape-q2-2026]
techniques: [T1566, T1566.004, T1557, T1528]
affected_products: ["Microsoft Teams", "Microsoft 365", "Microsoft Defender for Office 365"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-23"
    role: primary
closed_sources: []
evidence:
  - quote: "Microsoft Threat Intelligence observed continued growth in Teams-based social engineering, particularly voice phishing (vishing), with weekly malicious call attempts reaching nearly ten times the mid-2025 baseline by the end of the quarter."
    publisher: "Microsoft Threat Intelligence"
  - quote: "Credential phishing continued to dominate the malicious payload landscape throughout Q2, accounting for 94–96% of all payload-based attacks each month."
    publisher: "Microsoft Threat Intelligence"
verification: single-source
sourcing_note: "First-party vendor threat-landscape report drawn from Microsoft's own M365 telemetry; single-source by nature. Framed around the operationally-actionable findings; aggregate volume totals are omitted as vendor-scale metrics."
confidence: medium
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
migrated_from: null
---

Microsoft's quarterly email-threat report for Q2 2026 carries two findings that matter for any M365-heavy public-sector or enterprise tenant, and both are about *where* attacks land rather than raw volume. First, social engineering is migrating out of the inbox into trusted collaboration tooling: "weekly malicious call attempts reaching nearly ten times the mid-2025 baseline by the end of the quarter" in Microsoft Teams-based voice-phishing, concentrated in weekday business hours (roughly 14:00–20:00 UTC, near-zero at weekends) and trading on the implicit trust users place in an internal tool ([Microsoft Threat Intelligence, 2026-07-23](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)). Second, attachment-based phishing drifted from PDF toward DOC/DOCX delivery across the quarter and email-embedded QR codes collapsed to near-zero — a delivery-mechanism shift that is itself an evasion tell, following the disruption of the Tycoon2FA adversary-in-the-middle kit. Credential theft remained the dominant objective, "accounting for 94–96% of all payload-based attacks each month," with traditional malware delivery down to 4–6%.

Two illustrative campaigns show the current tradecraft. An automated business-email-compromise operation generated messages with Python's email-MIME library and dispatched them through the Amazon SES API from a DKIM-configured domain, reaching tens of thousands of role-based mailboxes (`ar`, `payroll`, `hr`) across many organizations in under three hours with open-tracking pixels for follow-up prioritization. A second campaign nested an EML attachment posing as a Teams voicemail; its action button ran a silent sign-in against an attacker-registered multi-tenant Entra application, and the OAuth redirect chain obscured the true destination from scanners and recipients before ultimately delivering a BAT dropper that pulled and ran a hidden second-stage payload ([Microsoft Threat Intelligence, 2026-07-23](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)).

**Defender takeaway:** email gateway controls no longer see the whole picture — the Teams-vishing surge and the OAuth-redirect / multi-tenant-Entra-app pattern both route around inbox scanning, so the durable detection signal is behavioral: month-over-month drift in attachment type (a swing toward DOC/DOCX after a PDF baseline), spikes in inbound Teams calls from external or newly-provisioned tenants against a single user cohort in a short window (vishing at volume leaves a call-frequency anomaly even when call content is unlogged), and consent/sign-in events against unfamiliar multi-tenant Entra applications. **Triage:** legitimate external Teams calls and third-party app consents occur routinely; the discriminators are volume and timing (a burst of external calls to many users in one department inside the weekday-afternoon window) and provenance (a multi-tenant app registered outside the tenant's own directory receiving a sign-in immediately after an emailed link). Microsoft's own hardening guidance for the credential-theft objective these campaigns still overwhelmingly pursue is phish-resistant MFA (FIDO2 / Windows Hello) scoped to privileged accounts and Zero-hour auto purge in Defender for Office 365.
