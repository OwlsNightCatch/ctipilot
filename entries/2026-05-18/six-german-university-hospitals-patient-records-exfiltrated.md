---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: Six German university hospitals — patient records exfiltrated via billing processor Unimed
headline: Six German university hospitals — patient records exfiltrated via billing processor Unimed
summary: "Unimed, a Saarland-based billing-service provider that handles private-insurance and self-payer invoicing for an estimated 95% of German university hospitals, was breached in mid-April 2026; patient billing data for at least six university hospitals — including Uniklinikum Freiburg and Uniklinik Köln, which issued …"
discovered_at: "2026-05-18T05:00:19Z"
event_date: 2026-05-24
run_id: 2026-W21-473d6fa5
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - dach
  - europe
sectors:
  - healthcare
  - public-sector
entities: []
cves: []
sources:
  - url: "https://therecord.media/hackers-steal-patient-billing-data-german-hospitals"
    publisher: "The Record, 2026-05-22"
    role: primary
  - url: "https://www.heise.de/en/news/Patient-data-affected-Cyberattack-on-billing-service-provider-for-clinics-11305015.html"
    publisher: "heise online, 2026-05-22"
    role: corroborating
  - url: "https://www.uk-koeln.de/uniklinik-koeln/aktuelles/detailansicht/cyberkriminelle-entwenden-patientendaten-bei-externem-abrechnungs-dienstleister/"
    publisher: "Uniklinik Köln, 2026-05-21"
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
migrated_from: briefs/weekly/2026-W21.md
---

Unimed, a Saarland-based billing-service provider that handles private-insurance and self-payer invoicing for an estimated 95% of German university hospitals, was breached in mid-April 2026; patient billing data for at least six university hospitals — including Uniklinikum Freiburg and Uniklinik Köln, which issued their own notifications on 2026-05-21 — was stolen; The Record tallies ~96,600 records across four named hospitals, with further hospitals affected per heise's per-hospital breakdown, as of [2026-05-24](/briefs/2026-05-24/). The defender lesson is the concentration multiplier: one processor breach simultaneously becomes a GDPR Art. 33/34 event for every covered hospital. CH/EU healthcare entities should inventory which billing, lab, and imaging processors hold their patient data and confirm each processor's breach-notification SLA.
