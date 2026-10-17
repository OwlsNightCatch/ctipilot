---
schema: 1
kind: incident
title: "CNIL fines IQVIA Operations France €5M for health data warehouse security failures: no MFA, no log monitoring, no network segmentation"
headline: "CNIL fines IQVIA Operations France €5M for health data warehouse security failures: no MFA, no log monitoring, no network segmentation"
summary: "France's CNIL fined IQVIA Operations France €5 million on 26 May 2026 for systematic GDPR violations across two authorised health data warehouses, LRX (fed by ~14,000 pharmacies) and EMR (fed by thousands of GPs) (CNIL, 2026-05-28)."
discovered_at: "2026-05-30T05:00:00Z"
event_date: 2026-05-28
run_id: 2026-05-30-aca445cc
priority: notable
immediate_action: null
tags:
  - data-breach
  - law-enforcement
  - eu-nexus
regions:
  - europe
sectors:
  - healthcare
  - technology
entities: []
cves: []
sources:
  - url: "https://www.cnil.fr/en/health-data-fine-5-million-euros-against-iqvia"
    publisher: CNIL enforcement notice
    role: primary
  - url: "https://ppc.land/cnil-fines-iqvia-eur5m-for-health-data-warehouse-breaches/"
    publisher: PPC.land
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
migrated_from: briefs/2026-05-30.md
---

France's CNIL fined IQVIA Operations France €5 million on 26 May 2026 for systematic GDPR violations across two authorised health data warehouses, LRX (fed by ~14,000 pharmacies) and EMR (fed by thousands of GPs) ([CNIL, 2026-05-28](https://www.cnil.fr/en/health-data-fine-5-million-euros-against-iqvia)). The CNIL enumerated five control failures: (1) IQVIA operated the warehouses outside the scope of its CNIL authorizations — deliberations 2018-289 and 2021-015 approved specific study types, and IQVIA conducted studies beyond those terms (Art. 66 of the French Data Protection Act); (2) patients were not informed that IQVIA acted as a data controller for their prescription data, violating GDPR Art. 14 information obligations; (3) multi-factor authentication was absent from all warehouse access paths; (4) no automated connection-log monitoring or alerting was in place — IQVIA confirmed retrospective deployment only after the CNIL investigation commenced; (5) no network segmentation between the health data warehouse and other IQVIA corporate infrastructure. The fine magnitude reflects the scope — "several tens of millions" of individuals — and IQVIA's market position. A compliance order with a €10,000/day penalty period accompanies the fine. For defenders this ruling operationalises baseline controls now explicitly expected for health data warehouse operations: MFA on all warehouse access paths, automated log alerting, network segmentation between sensitive-data stores and corporate infrastructure, and strict compliance with CNIL authorization scope for each study type conducted.
