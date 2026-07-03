---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Klue / Icarus Salesforce OAuth-integration breach — from nine named victims to ~24, then the attacker gets hacked"
headline: "Klue / Icarus Salesforce OAuth-integration breach — from nine named victims to ~24, then the attacker gets hacked"
summary: "The Klue/Icarus Salesforce OAuth breach widened to ~24 named firms, then the attacker was itself hacked and a second extortion group emerged listing ~195 organisations — one dormant integration token cascading into multi-tenant CRM theft. (daily 06-27, SecurityWeek)"
discovered_at: "2026-06-29T00:20:55Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - europe
sectors:
  - technology
  - finance
entities: []
cves: []
sources:
  - url: "https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/"
    publisher: "SecurityWeek — victims identified, hackers hacked"
    role: primary
  - url: "https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm"
    publisher: SEC EDGAR — 8x8 Form 8-K
    role: corroborating
  - url: "https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/"
    publisher: SecurityWeek — BeyondTrust/LastPass
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
migrated_from: briefs/weekly/2026-W26.md
---

This is the W25 multi-day item, but the in-window deltas re-shape it materially. At the start of the week the named-victim list stood at nine, mostly cybersecurity vendors (HackerOne, Huntress, Jamf, OneTrust and others, [SecurityWeek 06-23](https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/)). It then accreted through the week: 8x8 [filed an SEC 8-K Item 1.05 on 06-23](https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm) confirming Salesforce exfiltration; [BeyondTrust and LastPass disclosed](https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/) business-contact and sales data theft on 06-25; by 06-27 [roughly two dozen firms](https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/) had notified, and in a twist the Icarus attacker was itself hacked, with a second extortion actor now threatening the stolen data. Salesforce disabled the Klue connected app.

The new lens the dailies could not assemble: this is a single dormant OAuth integration credential at one SaaS vendor cascading into multi-tenant CRM theft across that vendor's entire customer base — the exact failure mode ReliaQuest framed as "integration abused in CRM data theft" in W25. For a Swiss/EU SOC the takeaway is an OAuth-grant inventory exercise: enumerate third-party connected apps with API scopes into your CRM/identity tenants, revoke dormant grants, and alert on bulk REST/Bulk-API reads from integration principals — patching nothing here helps, because no software was vulnerable; a delegated token was. ([daily 06-23](/briefs/2026-06-23/), [daily 06-25](/briefs/2026-06-25/), [daily 06-27](/briefs/2026-06-27/))
