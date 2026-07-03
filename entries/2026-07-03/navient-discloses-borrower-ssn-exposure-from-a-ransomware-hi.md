---
schema: 1
kind: incident
horizon: operational
title: Navient discloses borrower SSN exposure from a ransomware hit on its outside law firm
headline: Navient discloses borrower SSN exposure from a ransomware hit on its outside law firm
summary: "Two US SEC 8-K disclosures reinforce the third-/fourth-party access boundary: AdaptHealth was breached via a social-engineered hijack of a third-party contractor's session into cloud patient-management apps (SEC 8-K, 2026-07-02); Navient disclosed borrower SSN exposure from a ransomware hit on its outside law firm (SEC 8-K, 2026-07-02)."
discovered_at: "2026-07-03T04:48:13Z"
event_date: 2026-07-02
run_id: 2026-07-03-04ba8283
priority: high
immediate_action: null
tags:
  - data-breach
  - ransomware
  - supply-chain
regions:
  - us
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/1593538/000114036126027441/ef20077249_8k.htm"
    publisher: SEC EDGAR — Navient 8-K
    role: primary
closed_sources: []
evidence:
  - quote: "The incident involved a ransomware attack affecting certain of the Firm's information systems."
    publisher: SEC EDGAR — Navient 8-K
  - quote: "Such data includes borrower information such as customer names, date of birth, addresses and Social Security numbers."
    publisher: SEC EDGAR — Navient 8-K
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
migrated_from: briefs/2026-07-03.md
---

Student-loan servicer Navient Corporation (Nasdaq: NAVI) filed a Form 8-K (Item 1.05) on 2026-07-02 disclosing a material incident that did not touch its own systems: on 2026-06-08 it learned a third-party law firm providing services to the company had suffered a ransomware attack against the firm's own systems, and that Company-related borrower data held by the firm — names, dates of birth, addresses and Social Security numbers — was accessed ([SEC 8-K, 2026-07-02](https://www.sec.gov/Archives/edgar/data/1593538/000114036126027441/ef20077249_8k.htm)). Navient found no evidence of access to its own environment and no operational disruption but determined materiality on 2026-06-29 given the volume and sensitivity of the exposed data. No ransomware group is named and no leak-site posting has surfaced; this is the victim's own regulatory disclosure of a fourth-party compromise, and no independent press coverage of the filing was found in-window (single-source.

**Defender takeaway:** the failure surface here is entirely upstream at the vendor. Litigation and collections files are a known high-value ransomware target (bulk PII with minimal relative security investment) — contracts with outside counsel and collections firms that hold SSN-class identifiers (AHV-number-class equivalents) should mandate encryption-at-rest, short breach-notification SLAs, and independent security assessment.
