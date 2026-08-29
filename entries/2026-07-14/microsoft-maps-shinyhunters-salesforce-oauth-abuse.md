---
schema: 1
kind: research
title: "Microsoft maps three ShinyHunters-tradecraft OAuth-abuse paths against Salesforce customers — none exploiting a Salesforce vulnerability"
headline: "Microsoft maps a year of Salesforce OAuth abuse — vishing consent, supply-chain secret reuse, guest-access Aura abuse — invisible to sign-in detection"
summary: >
  Microsoft Threat Intelligence documented a year (mid-2025 to mid-2026) of campaigns using ShinyHunters-associated
  tradecraft (registry alias UNC6240) against Salesforce-integrated SaaS environments via three intrusion paths:
  vishing-driven malicious-OAuth-consent (a fake Data Loader app), SaaS supply-chain OAuth-secret reuse
  (Salesloft Drift, Gainsight, and Storm-3138's June 2026 Klue compromise), and guest-access Aura abuse. None
  exploited a Salesforce flaw — all abuse trusted OAuth relationships, so sign-in-anomaly detection gives limited
  visibility.
discovered_at: "2026-07-14T20:22:57Z"
event_date: "2026-07-13"
run_id: 2026-07-14T2009Z-intel
priority: notable
immediate_action: null
tags: [identity, cloud, phishing, supply-chain, data-breach]
regions: [global]
sectors: [public-sector, finance, retail, education, manufacturing]
entities: [actor:shinyhunters, actor:storm-3138]
techniques: [T1566.004, T1528, T1199, T1567]
affected_products: ["Salesforce", "Salesloft Drift", "Gainsight", "Klue"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-13"
    role: primary
  - url: "https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html"
    publisher: "The Hacker News"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Threat actors socially engineered employees into authorizing attacker-controlled connected apps within their Salesforce tenant."
    publisher: "Microsoft Threat Intelligence"
  - quote: "This activity was not the result of a vulnerability inherent to Salesforce."
    publisher: "Microsoft Threat Intelligence"
  - quote: "malicious activity often appeared indistinguishable from legitimate Salesforce usage because threat actors operated through trusted identities, approved OAuth applications, and authorized integrations."
    publisher: "Microsoft Threat Intelligence"
verification: multi-source
sourcing_note: "Microsoft Threat Intelligence is the primary substantive source; The Hacker News corroborates. The Storm-3138/Klue and Salesloft/Gainsight supply-chain details are Microsoft's attribution. ShinyHunters is referenced by its registry key; Storm-3138 is Microsoft's designation for the June 2026 Klue-compromise actor within the same tradecraft account."
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
actions:
  - "Audit Salesforce connected apps for unrecognized or over-privileged OAuth grants — specifically apps posing as legitimate integration tooling (e.g. a Data Loader lookalike) and any connected app inactive for 90+ days — and revoke them; this is the trust relationship the campaign abuses, and it is invisible to sign-in-anomaly detection."
migrated_from: null
---

Microsoft Threat Intelligence documented a year-long (mid-2025 to mid-2026) set of campaigns using tradecraft commonly associated with ShinyHunters (registry alias UNC6240) against Salesforce-integrated environments, through three distinct paths rather than any Salesforce product vulnerability ([Microsoft Threat Intelligence, 2026-07-13](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)). First, vishing-driven OAuth-consent abuse: attackers impersonating IT support socially engineer employees through the OAuth authorization workflow into granting a malicious connected app — disguised as the legitimate Salesforce Data Loader — full API access inherited from the victim's own privileges, letting them enumerate and exfiltrate CRM data through sanctioned application access that never trips a sign-in anomaly. Second, SaaS supply-chain compromise: compromised Salesloft Drift credentials (August 2025) exposed OAuth connection secrets reused across customer tenants; a November 2025 campaign abused Gainsight-published Salesforce apps the same way; and in June 2026 an actor Microsoft tracks as Storm-3138 compromised the Klue competitive-intelligence platform and reused harvested Salesforce credentials to query and exfiltrate customer CRM data. Third, guest-access abuse: requests chained against Salesforce's Aura framework via misconfigured guest-user accounts pulled far more data than a guest session should reach ([The Hacker News, 2026-07-14](https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html)). Microsoft observed the activity across retail, education and manufacturing tenants and states existing authentication-focused detections gave "limited visibility" because the traffic is indistinguishable from legitimate integration.

**Defender takeaway:** for CH/EU public-sector and enterprise orgs running Salesforce for case-management or citizen-service workloads, the lesson is that OAuth-consent and connected-app trust — not credentials or malware — is the attack surface here, and it evades sign-in-based detection; visibility requires OAuth/connected-app and data-access telemetry (Microsoft points to Defender for Cloud Apps real-time event monitoring and Salesforce Shield). **Triage:** the discriminator is *pattern*, not any single authentication event — bulk or systematic SOQL querying and report exports, connected-app activity from a new IP or user-agent for an established app, anomalous OAuth-scope combinations, and guest-user access reaching non-public objects; a legitimate integration exhibits a stable client fingerprint and a bounded query profile, so the deviation in volume and client identity is the signal.
