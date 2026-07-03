---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "Europol shadow-IT — LIBE committee MEPs call for mandate-expansion pause; EDPS sanctioning toolkit identified as binary"
headline: "Europol shadow-IT — LIBE committee MEPs call for mandate-expansion pause; EDPS sanctioning toolkit identified as binary"
summary: "The Correctiv / Solomon / Computer Weekly joint investigation (2026-05-05; first covered 2026-05-07) drove a material EU-legislative response within the window."
discovered_at: "2026-05-04T05:00:46Z"
event_date: 2026-05-08
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - insider-threat
  - law-enforcement
  - data-breach
  - eu-nexus
regions:
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.computerweekly.com/news/366642721/MEPs-call-for-greater-scrutiny-of-Europol-following-concerns-over-Shadow-IT"
    publisher: Computer Weekly — MEPs call for greater scrutiny of Europol
    role: primary
  - url: "https://correctiv.org/en/europe/2026/05/05/they-protect-the-law-while-breaking-it-inside-europols-shadow-it-system/"
    publisher: Correctiv — Europol shadow IT
    role: corroborating
  - url: "https://www.computerweekly.com/news/366642525/They-protect-the-law-while-breaking-it-Inside-Europols-shadow-IT-system"
    publisher: Computer Weekly investigation
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
migrated_from: briefs/weekly/2026-W19.md
---

The Correctiv / Solomon / Computer Weekly joint investigation (2026-05-05; first covered 2026-05-07) drove a material EU-legislative response within the window. On 8 May the LIBE committee met to discuss the disclosure; multiple MEPs — German Left MEP Özlem Alev Demirel, Belgian Green MEP Saskia Bricmont, German S&D MEP Birgit Sippel — called on the Commission to **pause any expansion of Europol's mandate** until parliamentary intervention powers and independent supervision are strengthened ([Computer Weekly, 2026-05-08](https://www.computerweekly.com/news/366642721/MEPs-call-for-greater-scrutiny-of-Europol-following-concerns-over-Shadow-IT)). EDPS chief Wojciech Wiewiórowski told the LIBE meeting that EDPS enforcement has a binary-only toolkit — soft admonishments or hard processing-cessation orders — with no intermediate sanctions, and that enlarging Europol without strengthening EDPS sanctioning power would be counterproductive. **Why this is obligations-changing:** the European Commission's 2026 work programme envisages a new Europol Regulation proposal in Q2 2026, meaning the parliamentary backlash lands directly in the legislative window. Per Correctiv's investigation, the EDPS closed monitoring of the CFN platform in February 2026 despite 15 of 150 remediation recommendations remaining unimplemented — a decision now facing retrospective scrutiny ([Correctiv investigation, 2026-05-05](https://correctiv.org/en/europe/2026/05/05/they-protect-the-law-while-breaking-it-inside-europols-shadow-it-system/)).

Background, restated from § 5: a Correctiv / Solomon / Computer Weekly joint investigation revealed that Europol's CFN (Computer Forensic Network, since 2012) and "Pressure Cooker" (Internet Referral Unit) data-processing platforms — holding ≥ 2 PB — operated outside EU data-protection oversight for over a decade ([Correctiv, 2026-05-05](https://correctiv.org/en/europe/2026/05/05/they-protect-the-law-while-breaking-it-inside-europols-shadow-it-system/) · [Computer Weekly investigation, 2026-05-05](https://www.computerweekly.com/news/366642525/They-protect-the-law-while-breaking-it-Inside-Europols-shadow-IT-system) · [daily 2026-05-07](/briefs/2026-05-07/)). Multiple categorised security deficiencies were identified in the 2019 internal assessment including absent administrative usage logs and inability to track data access or detect unauthorised modifications. **What defenders need to do differently:** agencies contributing intelligence to Europol-adjacent information-sharing chains (SIE, SIENA, Europol Platform for Experts) should treat the documented control deficiencies (absent audit logs, missing event monitoring, inability to track data access or detect unauthorised modifications, ineffective role assignment) as an ongoing data-integrity and confidentiality risk rather than a closed historical finding; internal audit functions should re-confirm closure evidence on regulator-mandated remediation tasks rather than rely on regulator monitoring termination as confirmation of remediation completeness.
