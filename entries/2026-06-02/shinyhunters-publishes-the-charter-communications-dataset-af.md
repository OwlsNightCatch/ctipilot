---
schema: 1
kind: incident
horizon: operational
title: ShinyHunters publishes the Charter Communications dataset after ransom refusal
headline: ShinyHunters publishes the Charter Communications dataset after ransom refusal
summary: "UPDATE (originally covered 2026-05-27): After Charter Communications declined to pay, ShinyHunters published the stolen dataset on 30 May. Have I Been Pwned ingested it as 4.9 million unique email addresses, alongside names, phone numbers and physical addresses (Security Affairs, 2026-05-30 · Have I Been Pwned)."
discovered_at: "2026-06-02T05:00:10Z"
event_date: 2026-05-30
run_id: 2026-06-02-8af85d01
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
regions:
  - us
sectors:
  - telco
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://securityaffairs.com/192907/uncategorized/shinyhunters-leaks-charter-communications-data-potentially-impacting-5-million-customers.html"
    publisher: Security Affairs
    role: primary
  - url: "https://haveibeenpwned.com/Breach/Charter"
    publisher: Have I Been Pwned
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-27/shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-02.md
---

**UPDATE (originally covered 2026-05-27):** After Charter Communications declined to pay, ShinyHunters published the stolen dataset on 30 May. Have I Been Pwned ingested it as 4.9 million unique email addresses, alongside names, phone numbers and physical addresses ([Security Affairs, 2026-05-30](https://securityaffairs.com/192907/uncategorized/shinyhunters-leaks-charter-communications-data-potentially-impacting-5-million-customers.html) · [Have I Been Pwned](https://haveibeenpwned.com/Breach/Charter)).

A subset of roughly 85,000 records originated from an internal employee directory and included job titles. ShinyHunters had originally claimed 42 million records and customer proprietary network information (CPNI); Charter confirmed the incident but stated no sensitive personal information or CPNI was exfiltrated. As established in prior coverage of the broader ShinyHunters Salesforce campaign, the access pattern is vishing-driven compromise of an employee Microsoft Entra account followed by a Salesforce export. The data is now public.
