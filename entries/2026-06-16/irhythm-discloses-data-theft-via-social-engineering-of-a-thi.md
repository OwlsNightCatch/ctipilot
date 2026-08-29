---
schema: 1
kind: incident
title: iRhythm discloses data theft via social engineering of a third-party-hosted application (SEC 8-K)
headline: iRhythm discloses data theft via social engineering of a third-party-hosted application (SEC 8-K)
summary: "Cardiac-monitoring medtech firm iRhythm filed an SEC Form 8-K Item 1.05 on 2026-06-15 reporting that a threat actor used social engineering against business applications hosted by a third party, exfiltrated PHI, PII and proprietary data, and sent a ransom demand on 9 June; the company made its materiality …"
discovered_at: "2026-06-16T05:08:56Z"
event_date: 2026-06-15
run_id: 2026-06-16-38d638e1
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
  - organized-crime
regions:
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/0001388658/000138865826000055/irtc-20260610.htm"
    publisher: SEC EDGAR — iRhythm Holdings 8-K
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
migrated_from: briefs/2026-06-16.md
---

Cardiac-monitoring medtech firm iRhythm filed an SEC Form 8-K Item 1.05 on 2026-06-15 reporting that a threat actor used **social engineering against business applications hosted by a third party**, exfiltrated PHI, PII and proprietary data, and sent a ransom demand on 9 June; the company made its materiality determination on 10 June ([SEC EDGAR, 2026-06-15](https://www.sec.gov/Archives/edgar/data/0001388658/000138865826000055/irtc-20260610.htm)). iRhythm states clinical and device-monitoring systems were unaffected. `[SINGLE-SOURCE]` — only the SEC primary is available; no independent corroboration yet.

**Defender takeaway:** the access vector — social engineering aimed at SaaS/third-party-hosted business apps rather than the corporate perimeter — continues to dominate healthcare-sector disclosures. Confirm help-desk identity-verification controls and conditional-access on externally-hosted business applications, not just on-network systems.
