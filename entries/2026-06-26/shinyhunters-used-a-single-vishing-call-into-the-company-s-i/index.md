---
schema: 1
kind: incident
title: "ShinyHunters used a single vishing call into the company's identity platform to breach Madison Square Garden"
headline: "ShinyHunters used a single vishing call into the company's identity platform to breach Madison Square Garden"
summary: "ShinyHunters breached Madison Square Garden through a single vishing call into the company's identity platform — 404 Media's review of the stolen data confirms a low-level employee was talked into letting the operators into MSG's systems, the same vishing → identity-platform (Entra/Okta) → MFA-enrollment kill chain that works equally well against EU public-sector tenants (404 Media, 2026-06-24)."
discovered_at: "2026-06-26T04:54:39Z"
event_date: 2026-06-24
run_id: 2026-06-26-6bbe4619
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - data-breach
  - organized-crime
regions:
  - us
  - global
sectors:
  - media
  - technology
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.404media.co/how-hackers-broke-into-madison-square-garden/"
    publisher: 404 Media
    role: primary
  - url: "https://thenextweb.com/news/shinyhunters-madison-square-garden-45gb-data-leak-facial-recognition"
    publisher: The Next Web
    role: corroborating
  - url: "https://abnormal.ai/blog/shinyhunters-sso-social-engineering-mfa-identity-compromise"
    publisher: Abnormal Security
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
migrated_from: briefs/2026-06-26.md
---

404 Media's review of the stolen Madison Square Garden data and the attackers' own account confirm the intrusion began with a vishing call — the operators phoned a low-level employee and talked them into letting them into MSG's systems ([404 Media, 2026-06-24](https://www.404media.co/how-hackers-broke-into-madison-square-garden/)). Reporting attributes the breach to ShinyHunters; after MSG missed a 15 June ransom deadline, roughly 45 GB / 26M+ records were published ([The Next Web, 2026-06-16](https://thenextweb.com/news/shinyhunters-madison-square-garden-45gb-data-leak-facial-recognition)). The wider pattern this fits — and the one worth detecting — is the vishing → identity-platform (Entra/Okta) → MFA-enrollment → SSO-pivot chain that Abnormal Security documents generically: an IT-impersonation call manufacturing MFA-reset urgency, real-time credential and one-time-code capture on a tenant-branded phishing page, enrollment of an attacker-controlled MFA device, then a pivot into connected SaaS ([Abnormal Security, 2026-02-06](https://abnormal.ai/blog/shinyhunters-sso-social-engineering-mfa-identity-compromise)). Maps to `T1566.004` (vishing), `T1078.004` (cloud accounts), and `T1556.006` (MFA manipulation).

**Why it matters to us:** the victim is a US private entity, but the kill chain is identity-platform-agnostic and lands the same way against EU public-sector Entra/Okta tenants. Hunt Entra audit logs for new MFA-method registration events correlated with anomalous sign-in geo/user-agent and post-enrollment impossible-travel risk events; the durable control is phishing-resistant FIDO2/passkey MFA that cannot be relayed in real time, plus Conditional Access requiring a compliant device for MFA enrollment.
