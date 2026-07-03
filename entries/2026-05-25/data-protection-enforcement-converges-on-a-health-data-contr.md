---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "Data-protection enforcement converges on a health-data controls floor — CNIL fines IQVIA €5M; California AG sues over 23andMe"
headline: "Data-protection enforcement converges on a health-data controls floor — CNIL fines IQVIA €5M; California AG sues over 23andMe"
summary: "Two enforcement actions in the window set the same baseline expectation for sensitive-data controllers. CNIL issued Délibération SAN-2026-008 (26 May), fining IQVIA Operations France €5M for security failures across its two authorised health-data warehouses — **no MFA on privileged access to the EMR …"
discovered_at: "2026-05-25T05:00:30Z"
event_date: null
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - data-breach
  - law-enforcement
regions:
  - europe
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.cnil.fr/en/health-data-fine-5-million-euros-against-iqvia"
    publisher: "CNIL — €5M IQVIA fine"
    role: primary
  - url: "https://www.legifrance.gouv.fr/cnil/id/CNILTEXT000054136834"
    publisher: "Légifrance — Délibération SAN-2026-008"
    role: corroborating
  - url: "https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023"
    publisher: California AG — Bonta sues Chrome Holding Co.
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
migrated_from: briefs/weekly/2026-W22.md
---

Two enforcement actions in the window set the same baseline expectation for sensitive-data controllers. **CNIL** issued Délibération **SAN-2026-008** (26 May), fining **IQVIA Operations France €5M** for security failures across its two authorised health-data warehouses — **no MFA on privileged access to the EMR warehouse, and no log monitoring to detect abnormal activity in either warehouse**, both cited explicitly as GDPR Art. 32 failures — with a six-month injunction under a €10,000/day coercive penalty. In parallel, the **California AG** sued the former **23andMe** (28 May) over the 2023 genetic-data breach affecting ~6.9M people, alleging a bulk-enumeration coding error plus **absent credential-stuffing defences and absent MFA**. The convergence is the message: regulators on both sides of the Atlantic are now treating **MFA on privileged access and active log monitoring as a non-negotiable floor** for health and genomic data, and pricing their absence directly. CH/EU health-data controllers should read both as a concrete control checklist, not distant precedent.
