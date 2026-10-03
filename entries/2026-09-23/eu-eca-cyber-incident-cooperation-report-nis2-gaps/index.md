---
schema: 1
kind: policy
title: "EU Court of Auditors: cyber-incident cooperation framework only partially effective, cross-border notification failed for the 2025 airport ransomware disruption"
headline: "EU auditors find no member state ever formally notified the bloc of the 2025 Collins Aerospace airport ransomware attack"
summary: >
  The European Court of Auditors' Special Report 19/2026 finds the EU's
  cybersecurity-incident cooperation framework only partially effective:
  only two member states met the October 2024 NIS2 transposition deadline,
  national-security law lets states withhold incident information, and,
  per heise online, Germany, Belgium and Ireland reportedly never formally
  notified ENISA of the September 2025 Collins Aerospace ransomware attack
  that disrupted four major European airports.
discovered_at: "2026-09-23T04:43:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: notable
immediate_action: null
tags: [policy]
regions: [europe]
sectors: [public-sector]
entities: ["policy:eu-nis2-directive"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf"
    publisher: "European Court of Auditors"
    date: "2026-09-22"
    role: primary
  - url: "https://www.heise.de/news/Rechnungshof-EU-nicht-genug-gegen-Cyberangriffe-gewappnet-11460919.html"
    publisher: "heise online"
    date: "2026-09-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Yet, no member state treated this incident as being either significant or large-scale cross-border. Therefore, none of the affected member states formally notified ENISA or other member states of the incident. The CSIRTs network did not advise EU-CyCLONe, which therefore did not support the coordinated management of the incident."
    publisher: "European Court of Auditors, Special Report 19/2026"
    source_url: "https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf"
  - quote: "Member states had until October 2024 to transpose the NIS 2 Directive into national law, but only two met the deadline."
    publisher: "European Court of Auditors, Special Report 19/2026"
    source_url: "https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf"
  - quote: "In 2025, only 14 significant cross-border incidents were reported, by seven member states."
    publisher: "European Court of Auditors, Special Report 19/2026"
    source_url: "https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf"
  - quote: "Despite the significant impact of the incident, the affected member states — Germany, Belgium and Ireland — reportedly did not notify the EU cybersecurity agency ENISA or the other member states accordingly, the report criticizes. (translated from German)"
    original: "Trotz der erheblichen Auswirkungen des Vorfalls hätten die betroffenen Mitgliedsländer, also Deutschland, Belgien und Irland, den Vorfall weder der EU-Cybersicherheitsagentur Enisa noch den anderen Mitgliedsländern entsprechend gemeldet, kritisiert der Bericht."
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Rechnungshof-EU-nicht-genug-gegen-Cyberangriffe-gewappnet-11460919.html"
verification: multi-source
sourcing_note: "The European Court of Auditors' report describes the airport case study without naming the affected member states. heise online names them as Germany, Belgium and Ireland."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-29T21:39:57Z"
    run_id: 2026-09-29T2134Z-audit
    type: correction
    summary: >
      The Court's audit scope covers the Commission's cyber situation centre, not the Cyber Blueprint,
      among the five EU-level mechanisms it assessed. Every citation and quoted passage now links the
      report's PDF. The summary states the NIS2 transposition finding as the report does: only two
      member states met the October 2024 deadline. The heise quotation is marked as a translation from
      German. The summary attributes the three-country notification finding to heise online, since the
      Court's report does not name the countries.
    fields: [sources, evidence, sourcing_note, summary, body]
migrated_from: null
---

The European Court of Auditors published Special Report 19/2026 on 2026-09-22, concluding that the EU's cooperation framework for detecting and responding to cybersecurity incidents (the CSIRTs network, EU-CyCLONe, the European Cybersecurity Alert System, the Commission's cyber situation centre and the EU Cybersecurity Reserve) is only partially effective ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)). Three structural gaps drive the finding: NIS2 transposition delays ("member states had until October 2024 to transpose the NIS 2 Directive into national law, but only two met the deadline" ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf))); national-security legislation that lets member states withhold incident information with no obligation to share it; and no EU-wide platform to correlate cross-border incidents in real time. As its case study, the report documents that the September 2025 Collins Aerospace ransomware attack on airport passenger-processing systems — "the disruption was most severe at London Heathrow Airport, Brussels Airport, Berlin Brandenburg Airport, and Dublin Airport" ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)) — was never classified as "significant" or "large-scale cross-border" under NIS2 by the affected member states, named by heise as Germany, Belgium and Ireland ([heise online, 2026-09-22](https://www.heise.de/news/Rechnungshof-EU-nicht-genug-gegen-Cyberangriffe-gewappnet-11460919.html)): "no member state treated this incident as being either significant or large-scale cross-border. Therefore, none of the affected member states formally notified ENISA or other member states of the incident. The CSIRTs network did not advise EU-CyCLONe, which therefore did not support the coordinated management of the incident" ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)). EU-wide, "in 2025, only 14 significant cross-border incidents were reported, by seven member states" ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)), and "no cybersecurity incident has been considered 'large-scale' by any member state since 2016", despite events the report itself cites as comparably severe, including WannaCry and NotPetya ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)). The Court's Recommendation 1, targeted for 2027 (information-sharing analysis and cross-border-incident detection) and 2028 (real-time incident reporting), calls for a Commission/ENISA-led review of national-security restrictions on information sharing and progress toward real-time incident reporting to ENISA ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)).

Switzerland sits outside NIS2's scope but is embedded in the same cross-border supply chains — aviation, finance, cloud — the report's case study concerns. The finding that formal EU cross-notification cannot be relied on for early warning is a direct input to how Swiss public-sector CERTs and GovCERT.ch should weight direct primary-source monitoring of national CERTs and vendor advisories against EU cross-notification channels, since a serious incident affecting an EU supply-chain partner may never surface through the formal EU mechanism at all.

## Correction — 2026-09-29T21:39:57Z

The five EU-level networks and mechanisms the Court assessed are the CSIRTs network, EU-CyCLONe, the European Cybersecurity Alert System, the Commission's cyber situation centre and the EU Cybersecurity Reserve ([European Court of Auditors, Special Report 19/2026, 2026-09-22](https://www.eca.europa.eu/ECAPublications/SR-2026-19/SR-2026-19_EN.pdf)). This entry previously listed the Cyber Blueprint in place of the cyber situation centre. The Blueprint is one of the policy instruments the report describes, not an assessed mechanism.
