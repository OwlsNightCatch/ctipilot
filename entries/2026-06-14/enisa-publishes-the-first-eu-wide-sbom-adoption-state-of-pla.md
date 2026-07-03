---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: ENISA publishes the first EU-wide SBOM Adoption State of Play — consumption lags generation
headline: ENISA publishes the first EU-wide SBOM Adoption State of Play — consumption lags generation
summary: ENISA released its end-2025 SBOM adoption survey on 9 June — the first EU-wide empirical baseline (ENISA). The report confirms the CRA is the primary accelerant of SBOM adoption and that organisations are investing in SBOM generation and SDLC/CI-CD integration.
discovered_at: "2026-06-14T23:57:40Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - supply-chain
  - eu-nexus
regions:
  - europe
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://www.enisa.europa.eu/publications/sbom-adoption-state-of-play-2026"
    publisher: ENISA — SBOM Adoption State of Play 2026
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W24.md
---

ENISA released its end-2025 SBOM adoption survey on 9 June — the first EU-wide empirical baseline ([ENISA](https://www.enisa.europa.eu/publications/sbom-adoption-state-of-play-2026)). The report confirms the CRA is the primary accelerant of SBOM adoption and that organisations are investing in SBOM *generation* and SDLC/CI-CD integration. The practical gap this creates — generation capability advancing faster than operational *consumption* (ingesting a vendor's SBOM into your own vulnerability-management workflow) — is the operational challenge it implies for Swiss/EU procurers; that framing is this brief's inference, not a stated headline of the report. It lands 94 days before the CRA's 11 September reporting-platform milestone. **What to do differently:** for public-sector procurement, demand SBOM deliverables in tenders now and verify your own consuming capability — generating SBOMs satisfies a producer obligation, but the defensive value (correlating known-bad components against CVE feeds) only materialises if you can ingest supplier SBOMs before the reporting obligation begins. This connects directly to § 6's "technology is the front line" synthesis.
