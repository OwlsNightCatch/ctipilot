---
schema: 1
kind: incident
title: "Six German university hospitals lose ~97,600+ patient records to a breach at billing processor Unimed"
headline: "Six German university hospitals lose ~97,600+ patient records to a breach at billing processor Unimed"
summary: "Attackers exfiltrated ~97,600+ patient records from six German university hospitals (Cologne, Freiburg, Heidelberg, Tübingen, Ulm, Mannheim) via Saarland billing processor Unimed — GDPR Art. 9 health data plus bank-account data in some cases, no clinical-system encryption. The Unimed perpetrator is unattributed; the pattern echoes the Kairos-linked ARWINI breach covered 2026-05-19, but that overlap is an analyst observation, not a sourced attribution (The Record, 2026-05-22)."
discovered_at: "2026-05-24T05:00:00Z"
event_date: 2026-05-22
run_id: 2026-05-24-f1fd8070
priority: high
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
  - url: "https://www.uniklinik-freiburg.de/presse/pressemitteilungen/detailansicht/6807-cyberangriff-auf-externen-dienstleister-betrifft-auch-daten-von-patientinnen-des-universitaetsklinikums-freiburg.html"
    publisher: "Uniklinik Freiburg, 2026-05-21"
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
migrated_from: briefs/2026-05-24.md
---

Unimed, a Saarland-based billing-service provider that handles private-insurance and self-payer invoicing for an estimated 95% of German university hospitals, was breached in mid-April 2026; attackers exfiltrated patient data and an attempted full encryption of Unimed's infrastructure was reportedly averted ([heise online, 2026-05-22](https://www.heise.de/en/news/Patient-data-affected-Cyberattack-on-billing-service-provider-for-clinics-11305015.html)). On 2026-05-21 at least six state-funded *Universitätsklinikum* hospitals — Cologne, Freiburg, Heidelberg, Tübingen, Ulm and Mannheim — disclosed that their patients' data was among the stolen records ([The Record, 2026-05-22](https://therecord.media/hackers-steal-patient-billing-data-german-hospitals)). University Hospital Freiburg states master data for ~54,000 patients (names, addresses, dates of birth) was taken, with billing records for ~900 patients additionally exposing diagnoses and treatment methods, and bank-account data in a small number of those cases ([Uniklinik Freiburg, 2026-05-21](https://www.uniklinik-freiburg.de/presse/pressemitteilungen/detailansicht/6807-cyberangriff-auf-externen-dienstleister-betrifft-auch-daten-von-patientinnen-des-universitaetsklinikums-freiburg.html)); Cologne reports ~30,000 affected ([Uniklinik Köln, 2026-05-21](https://www.uk-koeln.de/uniklinik-koeln/aktuelles/detailansicht/cyberkriminelle-entwenden-patientendaten-bei-externem-abrechnungs-dienstleister/)). The exposed categories include GDPR Article 9 special-category health data (diagnoses, treatment codes) and financial data (IBANs). Attribution is open: heise states it is "not yet known who is responsible" for the Unimed attack, and The Record likewise reports no actor had publicly claimed responsibility at its publication. The intrusion does rhyme with the earlier ARWINI Lower-Saxony statutory-billing breach (covered 2026-05-19) — which the Hannover Police Directorate attributed to the **Kairos** ransomware group per heise — but that resemblance is an analyst pattern-overlap, not a sourced attribution of the Unimed breach.

**Defender takeaway:** This is the recurring "shared-service processor as the soft underbelly of healthcare" pattern — the hospitals' own clinical systems held, but a third-party billing aggregator concentrated Art. 9 data for dozens of institutions and became the single point of failure. heise notes encryption was attempted but blocked while exfiltration over the same access succeeded, the classic gap where endpoint controls stop the ransomware payload but not the prior data theft. CH/EU hospitals running outsourced billing should inventory which processors hold Art. 9 data on their behalf, confirm a data-protection impact assessment and Art. 32 technical measures are in place, and hunt for large outbound transfers from billing/ERP systems with no corresponding inbound job trigger and for service-account authentication outside business hours.
