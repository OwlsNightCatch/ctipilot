---
schema: 1
kind: incident
horizon: operational
title: "ICO secures Proceeds-of-Crime confiscation from former RAC employees who sold ~30,000 customer records"
headline: "ICO secures Proceeds-of-Crime confiscation from former RAC employees who sold ~30,000 customer records"
summary: "ICO uses criminal asset-recovery against insider data theft. The UK regulator secured £118,852 in Proceeds-of-Crime confiscation orders from two former RAC employees who sold ~30,000 customer records — a reminder that insider exfiltration of even modest volumes attracts prosecution and clawback years later (POCA orders, Nov 2025 + 29 May 2026; ICO)."
discovered_at: "2026-06-08T05:00:01Z"
event_date: null
run_id: 2026-06-08-1a0ce644
priority: high
immediate_action: null
tags:
  - insider-threat
  - data-breach
  - law-enforcement
regions:
  - uk
sectors: []
entities: []
cves: []
sources:
  - url: "https://ico.org.uk/action-weve-taken/enforcement/2026/05/debbie-okparavero-and-maliha-islam-proceeds-of-crime-act/"
    publisher: ICO
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
actions:
  - "**Review insider-data-theft controls on contact-centre / CRM data** (. Scope access need-to-know, monitor privileged-user bulk-export and anomalous query patterns, and retain audit trails long enough to support prosecution."
migrated_from: briefs/2026-06-08.md
---

The UK Information Commissioner's Office, in an enforcement-action notice surfaced in early June (page last updated 5 June), recorded Proceeds of Crime Act confiscation orders totalling £118,852.32 against two former RAC contact-centre employees: Maliha Islam, ordered to pay £33,125.00 at a hearing in **November 2025**, and Debbie Okparavero, ordered to pay £85,727.32 at a hearing held on **29 May 2026** ([ICO](https://ico.org.uk/action-weve-taken/enforcement/2026/05/debbie-okparavero-and-maliha-islam-proceeds-of-crime-act/)). The pair were convicted in October 2024 of conspiracy under the Computer Misuse Act 1990 and Data Protection Act 2018 for unlawfully copying and selling roughly 30,000 lines of customer personal data (used to fuel nuisance-claims calls); the original sentences were suspended, and the POCA hearings quantified and ordered repayment of the financial benefit. The ICO explicitly framed the action as using "the full range of its enforcement powers" — criminal asset recovery, not just civil penalty.

**Defender takeaway:** insider exfiltration is a low-volume, high-trust threat that DLP and access reviews catch, not perimeter controls. The case is a reminder to scope contact-centre / CRM data on a need-to-know basis, monitor privileged-user query and bulk-export patterns, and retain audit trails long enough to support prosecution — the benefit calculation here rested on demonstrable records of the theft years after the fact. For Swiss/EU practitioners, it is a useful GDPR-comparable benchmark for how a peer regulator escalates against insider data theft.
