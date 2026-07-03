---
schema: 1
kind: incident
horizon: operational
title: "Klue/Icarus OAuth-token breach — named victim list expands to nine firms, mostly cybersecurity vendors"
headline: "Klue/Icarus OAuth-token breach — named victim list expands to nine firms, mostly cybersecurity vendors"
summary: "UPDATE (originally covered 2026-06-21): At least nine Klue customers have now publicly confirmed Salesforce-CRM data impact from the 11–12 June Icarus intrusion: HackerOne, Huntress, Jamf, OneTrust, Recorded Future, Snyk, Tanium, Insurity and Sprout Social (SecurityWeek, 2026-06-22)."
discovered_at: "2026-06-23T04:52:51Z"
event_date: 2026-06-22
run_id: 2026-06-23-165387f6
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
regions:
  - global
  - europe
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/"
    publisher: SecurityWeek
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
migrated_from: briefs/2026-06-23.md
---

**UPDATE (originally covered 2026-06-21):** At least nine Klue customers have now publicly confirmed Salesforce-CRM data impact from the 11–12 June Icarus intrusion: HackerOne, Huntress, Jamf, OneTrust, Recorded Future, Snyk, Tanium, Insurity and Sprout Social ([SecurityWeek, 2026-06-22](https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/)). Exposed data is sales-account and contact information — names, business emails, job titles, phone numbers and addresses — exfiltrated via OAuth tokens from a dormant Klue→Salesforce integration; the actor (Icarus, also tracked as UNC6395) had set a 22 June publication deadline.

The concentration of cybersecurity vendors in the victim list is the notable delta: contact data for security-operations staff at those firms' customers now sits in a threat-actor corpus and is prime material for precision spear-phishing aimed at security roles. The structural lesson is unchanged from first coverage — enumerate and revoke unused third-party OAuth grants in Salesforce (`Setup → Identity → OAuth Usage`), scope active grants to minimum-necessary objects, and alert via Salesforce Event Monitoring on a connected app pulling thousands of account records in a single short session.
