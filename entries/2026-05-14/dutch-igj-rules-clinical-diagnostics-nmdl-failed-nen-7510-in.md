---
schema: 1
kind: incident
horizon: operational
title: "Dutch IGJ rules Clinical Diagnostics/NMDL failed NEN 7510 information-security standard at time of July 2025 ransomware breach; ~941,000 patients affected, cervical-cancer screening data exposed"
headline: "Dutch IGJ rules Clinical Diagnostics/NMDL failed NEN 7510 information-security standard at time of July 2025 ransomware breach; ~941,000 patients affected"
summary: "Dutch IGJ rules Clinical Diagnostics/NMDL failed mandatory NEN 7510 information-security standard at time of July 2025 ransomware breach. The Dutch Health & Youth Care Inspectorate's 2026-05-13 finding cites two specific failures: no independent information-security audit, and no periodic processing-risk assessments — meaning the laboratory could not determine which controls were required. The breach exposed approximately 941,000 patients' records, including results of the national cervical-cancer screening programme (Bevolkingsonderzoek Nederland). IGJ has no fining power but has demanded independent certification and signalled sector-wide enforcement; Autoriteit Persoonsgegevens (AP) holds a parallel GDPR investigation that can. NEN 7510 (Dutch healthcare security baseline) is the structural analogue of Switzerland's EPDG security profile — same gap, same regulator pattern (IGJ, 2026-05-13; Computable, 2026-05-13)."
discovered_at: "2026-05-14T05:00:00Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - europe
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging"
    publisher: "IGJ, 2026-05-13"
    role: primary
  - url: "https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/"
    publisher: "Computable, 2026-05-13"
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
migrated_from: briefs/2026-05-14.md
---

The Dutch Health & Youth Care Inspectorate (Inspectie Gezondheidszorg en Jeugd, IGJ) issued a public finding on 2026-05-13 concluding that Clinical Diagnostics LCPL BV and NMDL BV (Rijswijk) did not meet the mandatory NEN 7510 information-security standard at the time of their July 2025 ransomware breach, and had not fully remediated the deficiencies as of IGJ's December 2025 follow-up inspection ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging); native title: "Clinical Diagnostics voldeed niet aan wettelijke norm voor informatiebeveiliging" — "Clinical Diagnostics did not meet the statutory information-security standard"). NEN 7510 is the Dutch statutory information-security baseline for healthcare organisations under the Wabvpz, structurally aligned with ISO/IEC 27001 but extended for health-data obligations; non-compliance is independently actionable by multiple regulators.

IGJ's two named failures are foundational rather than technical: (1) no independent audit of the laboratory's information security had ever been performed, and (2) the organisation had not periodically assessed its processing risks, leaving it unable to determine which controls were necessary. The July 2025 breach — Computable's prior reporting attributes it to the Nova ransomware group — exposed approximately 941,000 patients' personal and medical records, including cervical-cancer screening results processed for the population-screening programme Bevolkingsonderzoek Nederland ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)). IGJ has no fining power and has demanded short-term independent NEN 7510 certification; Autoriteit Persoonsgegevens (Dutch DPA), whose GDPR enforcement carries fines, is running a parallel investigation. IGJ also signalled sector-wide enforcement intent by publicly calling for all healthcare providers to demonstrate independent certification — a leading indicator of broader inspection cadence.

For a Swiss SOC the parallel is direct: NEN 7510 is the regulatory analogue of the EPDG (Bundesgesetz über das elektronische Patientendossier) security profile, and the two specific failures — absence of third-party audit, absence of periodic risk assessment — are the same hygiene-baseline gaps Swiss healthcare providers face under cantonal supervision. The breach scale (941k records, mass-screening data) is the proximate consequence of those structural gaps; the operationally useful read for defenders is detection of NEN-7510-style baseline gaps via third-party assessment, not signature hunting.
