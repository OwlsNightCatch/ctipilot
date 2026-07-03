---
schema: 1
kind: incident
horizon: operational
title: "Spain arrests doxer who published personal data on INCIBE, prosecutorial and security-service staff"
headline: "Spain arrests doxer who published personal data on INCIBE, prosecutorial and security-service staff"
summary: "Spain's National Police arrested a doxer who published personal data on staff of INCIBE, the State Attorney General, the Civil Guard and the National Security Council (BleepingComputer, 2026-06-01); separately, attackers socially engineered Meta's AI support chatbot into resetting Instagram passwords, bypassing the account-recovery MFA envelope (Krebs on Security, 2026-06-01)."
discovered_at: "2026-06-02T05:00:00Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: high
immediate_action: null
tags:
  - data-breach
  - law-enforcement
  - phishing
regions:
  - europe
sectors:
  - public-sector
  - defense
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/spain-arrests-doxer-leaking-sensitive-data-of-govt-employees/"
    publisher: BleepingComputer
    role: primary
  - url: "https://policia.es/_es/comunicacion_prensa_detalle.php?ID=16895"
    publisher: "Policía Nacional press release"
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
migrated_from: briefs/2026-06-02.md
---

Spain's National Police arrested an individual in Granada on 27 May 2026 for publishing personal data belonging to staff of the State Attorney General's Office (Fiscalía General del Estado), the National Cybersecurity Institute (INCIBE), the National Police, the Civil Guard and the National Security Council; the operation was overseen by Madrid Investigating Court No. 22 ([BleepingComputer, 2026-06-01](https://www.bleepingcomputer.com/news/security/spain-arrests-doxer-leaking-sensitive-data-of-govt-employees/) · [Policía Nacional, 2026-06-01](https://policia.es/_es/comunicacion_prensa_detalle.php?ID=16895)). The data was published on BreachForums under the "Police-ESP-Doxed" handle. INCIBE has previously assessed that no direct compromise of its systems occurred — the dossiers were assembled from older breaches, credential dumps and OSINT, with some records containing names of staff who had left years earlier. The investigation opened after police detected "mass dissemination" of the data, which they assessed as an immediate risk to the named individuals and institutions.

**Why it matters to us:** This is the OSINT-aggregation-plus-prior-breach-enrichment pattern aimed squarely at the personnel of a national cybersecurity authority and security services — a reconnaissance precursor to targeted phishing, vishing and coercion against critical-infrastructure officials. Swiss and EU public-sector security teams should treat circulated staff dossiers as an elevated-phishing trigger and push data-broker opt-out / breach-exposure monitoring for sensitive-role employees.
