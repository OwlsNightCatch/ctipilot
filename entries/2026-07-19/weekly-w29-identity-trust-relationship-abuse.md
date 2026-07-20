---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "The week's identity intrusions all abused a trusted relationship rather than breaking authentication — OAuth consent and secret reuse, forged and unverified tokens, and helpdesk process abuse turned valid trust into valid-account access"
headline: "Identity attacks converged on abusing trust, not breaking it — OAuth/SSO vishing, a client_id oracle, a Moodle JWT forgery, and helpdesk-vishing resets"
summary: >
  Five independent 2026-W29 disclosures describe the same identity-intrusion pattern from different angles: none broke authentication cryptographically — each abused a trusted OAuth grant, token, or human process to obtain valid-account access that sign-in-anomaly detection barely sees. Microsoft mapped a year of ShinyHunters-associated Salesforce OAuth abuse (vishing-driven malicious consent, SaaS supply-chain secret reuse, guest-access Aura abuse), and the same actor's vishing-to-Entra-SSO tradecraft surfaced in the Abbott/Exact Sciences intrusion. Proofpoint documented OAuth client_id spoofing that turns an Entra ID "application not found" error into a credential-validity oracle while leaving a blank application name in the sign-in log. CVE-2026-54733 in Moodle's official Microsoft 365 plugin authenticated forged JWTs without ever verifying the signature — knowing any user's email yielded full site takeover. And the Scattered Spider TfL sentencing put the credential-purchase → helpdesk-vishing → MFA-reset chain into the court record. This extends the M365 auth-flow convergence the prior weekly documented (device-code, ROPC, AiTM) into the OAuth-trust, token-forgery and helpdesk-process layer — the controls that catch it are consent governance, token/grant hardening and helpdesk identity-proofing, not stronger MFA.
discovered_at: "2026-07-19T23:46:00Z"
event_date: 2026-07-18
run_id: 2026-07-19T2310Z-weekly
priority: high
immediate_action: null
tags:
  - identity
  - auth-bypass
  - phishing
  - cloud
  - data-breach
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - healthcare
entities:
  - actor:shinyhunters
  - actor:storm-3138
  - actor:scattered-spider
  - actor:unk-pyreq2323
  - actor:unk-outflareaz
  - incident:tfl-scattered-spider-2024
cves: []
techniques:
  - T1566.004
  - T1550.001
  - T1606.002
  - T1528
  - T1078.004
affected_products:
  - "Salesforce"
  - "Microsoft Entra ID"
  - "Moodle"
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-13"
    role: primary
  - url: "https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy"
    publisher: "Proofpoint Threat Research"
    date: "2026-07-13"
    role: primary
  - url: "https://github.com/microsoft/o365-moodle/security/advisories/GHSA-hqjh-93qv-47v5"
    publisher: "Microsoft o365-moodle GitHub Security Advisory"
    date: "2026-07-06"
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446"
    publisher: "The Register"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Each strand is independently sourced to its own primary (Microsoft TI, Proofpoint, the Microsoft o365-moodle GHSA, NCA/CPS). The Abbott/Exact Sciences strand pairs Abbott's own confirmation of unauthorized access with ShinyHunters' unconfirmed 30M-record extortion claim — the claim is attributed to the group, not stated as fact."
confidence: high
update_of: null
references:
  - 2026-07-14/microsoft-maps-shinyhunters-salesforce-oauth-abuse
  - 2026-07-18/abbott-exact-sciences-shinyhunters-entra-sso-vishing
  - 2026-07-15/proofpoint-oauth-client-id-spoofing-entra-id-evasion
  - 2026-07-18/moodle-local-o365-jwt-forgery-admin-takeover-cve-2026-54733
  - 2026-07-17/scattered-spider-tfl-sentencing-helpdesk-vishing
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The prior weekly documented M365 account-takeover converging on auth flows Conditional Access rarely gates — device-code, ROPC and AiTM. This week the pattern moved one layer up: the intrusions abused **trust that had already been granted** rather than the authentication event itself, and each left detection thin in a different way.

Two strands are the same actor. Microsoft Threat Intelligence documented a year of ShinyHunters-associated (UNC6240) tradecraft against Salesforce-integrated SaaS through three paths — vishing-driven malicious OAuth consent (a fake Data Loader app), SaaS supply-chain OAuth-secret reuse (Salesloft Drift, Gainsight, and Storm-3138's Klue compromise), and guest-access Aura abuse — none of which exploited a Salesforce vulnerability; each instead abused trusted OAuth relationships ([Microsoft, 2026-07-13](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)); the same vishing-to-Entra-SSO tradecraft then appeared in Abbott's confirmed intrusion into its Cancer Diagnostics (Exact Sciences) systems. Proofpoint showed a subtler variant: an attacker POSTing credentials to the Entra ID ROPC token endpoint with an arbitrary unregistered `client_id` reads the differential `AADSTS` errors as a credential-validity oracle — `AADSTS700016` ("application not found") is returned only when both username and password are correct — while the unregistered id leaves a blank application name in the sign-in log, defeating detections that correlate by app ([Proofpoint, 2026-07-13](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy)).

The token-trust failure reached its extreme in Moodle's official Microsoft 365 integration: CVE-2026-54733 authenticated users from a JWT's `upn` claim "without ever verifying the JWT signature," so knowing or enumerating any email — an administrator's included — yielded that user's session and "effectively full site takeover" ([Microsoft o365-moodle GHSA, 2026-07-06](https://github.com/microsoft/o365-moodle/security/advisories/GHSA-hqjh-93qv-47v5)). And the human-process layer got its case-law record: at the Scattered Spider TfL sentencing, the court heard the pair purchased partial TfL credentials from "well-known criminal forums" and socially engineered a TfL helpdesk worker into resetting an employee account's password and, over multiple attempts, its 2FA, then used that access ([The Register, 2026-07-16](https://www.theregister.com/cyber-crime/2026/07/16/brit-scattered-spider-duo-handed-tickets-to-prison-over-transport-for-london-attack/5272446)).

**Defender takeaway:** the common failure is that each intrusion produced authentication telemetry that looks legitimate — a consented OAuth app, a valid token, a successful helpdesk-assisted reset — so the detections that matter this week are not MFA-strength but consent and grant governance (inventory and restrict third-party OAuth app consent; alert on new service-principal secrets and on ROPC use where legacy auth should be off), token integrity (the Moodle case is a reminder to treat any SSO endpoint that trusts an unverified token as full-takeover-equivalent), and helpdesk identity-proofing for password/MFA resets. **Triage:** a consented OAuth app or a token-based sign-in is not itself suspicious — the discriminators are consent to an app your catalog never approved, ROPC sign-ins carrying a blank/absent application name, and account-recovery events (password + MFA reset in short succession) that originate from a helpdesk interaction rather than the user's own device; any one is weak, the sequence against a privileged account is the signal.
