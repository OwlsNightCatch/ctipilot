---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "ShinyHunters — DentaQuest: 234 GB HIPAA claims data published after ransom refusal, 2.6 M Medicaid and dental-benefit records"
headline: "ShinyHunters — DentaQuest: 234 GB HIPAA claims data published after ransom refusal, 2.6 M Medicaid and dental-benefit records"
summary: "DentaQuest (Sun Life subsidiary, administering dental/vision benefits for ~35 M US Medicaid and Medicare members) confirmed on 1 June that ShinyHunters published 234 GB of stolen data after ransom negotiations broke down (BleepingComputer, 2026-06-04; BankInfoSecurity; daily 2026-06-05)."
discovered_at: "2026-06-01T05:00:13Z"
event_date: 2026-06-05
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - us
sectors:
  - healthcare
entities:
  - "actor:shinyhunters"
  - "incident:dentaquest-shinyhunters-2026"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883"
    publisher: BankInfoSecurity
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
migrated_from: briefs/weekly/2026-W23.md
---

DentaQuest (Sun Life subsidiary, administering dental/vision benefits for ~35 M US Medicaid and Medicare members) confirmed on 1 June that ShinyHunters published 234 GB of stolen data after ransom negotiations broke down ([BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/dentaquest-data-breach-exposed-info-of-26-million-accounts/); [BankInfoSecurity](https://www.bankinfosecurity.com/shinyhunters-leaks-234gb-dentaquest-data-trove-a-31883); [daily 2026-06-05](/briefs/2026-06-05/)). The dataset — published by late May per BankInfoSecurity — is in HIPAA-format ASC X12 claims interchange; names, postal and email addresses, dates of birth, phone numbers, health-insurance details and Medicaid IDs across 2.6 million unique email addresses. DentaQuest has not confirmed the specific attack vector; the extortion pattern (no encryption, hard deadline, publish-on-refusal) is consistent with the broader ShinyHunters vishing-driven SaaS-access campaign that earlier claimed Charter, Carnival, 7-Eleven, Instructure and Wynn Resorts. The operational reminder: this actor has no backup-based leverage — detection must land at the bulk-export stage (anomalous off-hours claims-system bulk downloads; SaaS API token generation; volume spikes on outbound archive transfers).
