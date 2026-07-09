---
schema: 1
kind: incident
horizon: operational
title: 8x8 confirms Klue/Icarus Salesforce exfiltration in an SEC 8-K Item 1.05 filing
headline: 8x8 confirms Klue/Icarus Salesforce exfiltration in an SEC 8-K Item 1.05 filing
summary: "UPDATE (originally covered 2026-06-19; campaign delta 2026-06-23): US cloud-communications provider 8x8 (NASDAQ: EGHT) filed a Form 8-K Item 1.05 on 2026-06-23 disclosing that an unauthorised party accessed its Salesforce environment on 2026-06-11/12 via a **third-party integration — the Klue …"
discovered_at: "2026-06-24T05:11:56Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
  - cloud
regions:
  - us
  - global
sectors:
  - telco
  - technology
entities:
  - "campaign:icarus-klue-salesforce-oauth"
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm"
    publisher: SEC EDGAR — 8x8 Inc Form 8-K Item 1.05
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: 2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-24.md
---

**UPDATE (originally covered 2026-06-19; campaign delta 2026-06-23):** US cloud-communications provider 8x8 (NASDAQ: EGHT) filed a Form 8-K Item 1.05 on 2026-06-23 disclosing that an unauthorised party accessed its Salesforce environment on 2026-06-11/12 via a **third-party integration — the Klue competitive-intelligence platform** — the OAuth-integration vector behind the Icarus extortion campaign already tracked in prior briefs ([SEC EDGAR — 8x8 Form 8-K, 2026-06-23](https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm)).

The filing states the accessed data is limited to contract information, internal sales notes and business contact data (names, business emails, phone numbers, mailing addresses). As a publicly-listed company's mandatory material-incident disclosure, it is the formal confirmation that 8x8 is a named Klue-integration victim, extending the campaign's confirmed-victim list.

Defender takeaway for anyone running SaaS-to-Salesforce OAuth integrations (including EU public-sector users of competitive-intel tooling): audit Connected Apps in Salesforce Setup → App Manager for unexpected or stale OAuth grants, scope connected-app permissions to least privilege, and monitor `EventType=OAuthToken` in Salesforce Event Monitoring for anomalous token use (`T1078.004` Valid Accounts: Cloud, `T1550.001` token abuse).
