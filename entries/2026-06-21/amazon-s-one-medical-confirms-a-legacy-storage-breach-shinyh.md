---
schema: 1
kind: incident
horizon: operational
title: "Amazon's One Medical confirms a legacy-storage breach; ShinyHunters' 8.8TB claim is unverified and its deadline expires today"
headline: "Amazon's One Medical confirms a legacy-storage breach; ShinyHunters' 8.8TB claim is unverified and its deadline expires today"
summary: "One Medical (Amazon) confirmed on 2026-06-13 that an unauthorised party accessed a legacy third-party file-storage system retaining archived records for One Medical Seniors (formerly Iora Health), during a 2026-06-08 to 2026-06-11 window, affecting demographic and clinical records for patients at nine clinics …"
discovered_at: "2026-06-21T04:54:59Z"
event_date: 2026-06-19
run_id: 2026-06-21-2b75e32c
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
cves: []
sources:
  - url: "https://www.bankinfosecurity.com/shinyhunters-threatens-to-leak-amazon-one-medical-records-a-32027"
    publisher: BankInfoSecurity
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-21.md
---

One Medical (Amazon) confirmed on 2026-06-13 that an unauthorised party accessed a legacy third-party file-storage system retaining archived records for One Medical Seniors (formerly Iora Health), during a 2026-06-08 to 2026-06-11 window, affecting demographic and clinical records for patients at nine clinics ([BankInfoSecurity, 2026-06-19](https://www.bankinfosecurity.com/shinyhunters-threatens-to-leak-amazon-one-medical-records-a-32027)). One Medical states the breach is confined to that legacy system. Separately, ShinyHunters claims theft of 8.8 TB and set a 2026-06-22 negotiation deadline — *today* — but the company has not confirmed ShinyHunters' involvement or the data volume, and no sample has been released to validate the claim. `[SINGLE-SOURCE]`

**Defender takeaway:** ShinyHunters' maximalist-claim-then-short-deadline pattern recurred across multiple victims this week (Kodak, covered 2026-06-20, among them); the *confirmed* subset is consistently smaller than the *claimed* one. Audit legacy and "decommissioned" third-party storage that may still hold archival PII/clinical data outside normal operational scope, and keep those systems inside third-party risk assessments. The passing 06-22 deadline is the near-term monitoring trigger: data release would corroborate the 8.8TB vector, silence suggests a pivot to negotiation.
