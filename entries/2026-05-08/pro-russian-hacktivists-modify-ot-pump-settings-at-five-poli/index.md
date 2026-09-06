---
schema: 1
kind: threat
title: Pro-Russian hacktivists modify OT pump settings at five Polish water treatment facilities
headline: Pro-Russian hacktivists modify OT pump settings at five Polish water treatment facilities
summary: >
  Pro-Russian hacktivists compromised OT networks of five Polish water treatment facilities,
  modifying pump settings. Manual overrides prevented service disruption. Pattern consistent with
  Cyber Army of Russia Reborn / NoName057(16) campaigns in CEE infrastructure.
discovered_at: "2026-05-08T05:00:02Z"
updated_at: "2026-05-09T05:00:14Z"
event_date: null
run_id: 2026-05-08-migrated
priority: high
immediate_action: null
tags:
  - nation-state
  - hacktivism
  - ot-ics
  - actively-exploited
  - russia-nexus
regions:
  - europe
sectors:
  - water
  - public-sector
entities:
  - "campaign:frostyneighbor-2026-05-campaign"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://abw.gov.pl/pl/cyberbezpieczenstwo/"
    publisher: "ABW — Cybersecurity Alert, Polish Water Sector OT Intrusion"
    role: primary
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a"
    publisher: CISA AA24-207A — Russian GRU targeting critical infrastructure (background reference)
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-09T05:00:14Z"
    run_id: 2026-05-09-migrated
    type: update
    summary: "UPDATE (originally covered 2026-05-08):"
    fields:
      - entities
      - sectors
      - sources
      - body
    merged_from: 2026-05-09/polish-water-ot-intrusions-abw-annual-report-names-five-faci
migrated_from: briefs/2026-05-08.md
---

Poland's Internal Security Agency (ABW) disclosed that pro-Russian hacktivist actors penetrated the operational technology (OT) networks of five water treatment facilities and modified pump control parameters. At least one facility activated manual override procedures to prevent potential service disruption; no compromise of drinking water quality or supply loss was confirmed. ABW attributed the activity to actors operating in support of Russian geopolitical objectives but stopped short of formal state attribution. The attack pattern — IT/OT flat network exploitation leading to HMI manipulation — is consistent with prior campaigns attributed to **NoName057(16)** and **Cyber Army of Russia Reborn** in Central and Eastern European infrastructure. Polish water sector authorities and critical-infrastructure operators have been placed on heightened alert. The ABW advisory is a single-source national CERT/authority disclosure.

## Update — 2026-05-09T05:00:14Z

Poland's Internal Security Agency (ABW) published its 2025 Annual Report on 2026-05-07, providing materially expanded detail beyond the initial reporting. The report names five municipal water facilities targeted in intrusion attempts during H2 2025 and Q1 2026: **Jabłonna Lacka**, **Szczytno**, **Małdyty**, **Tolkmicko**, and **Sierakowo**. All are smaller municipalities (populations 1,500–26,000) with limited IT security staff, consistent with the observed targeting pattern. ABW formally attributes the intrusion campaign to **APT28** (Russian GRU) for the initial-access and persistence phase, **APT29** (Russian SVR) for the intelligence-collection overlay observed at Jabłonna Lacka, and **UNC1151** (Belarusian GRU-affiliated, historically associated with Ghostwriter information operations) for a disinformation component: fabricated leak documents purporting to show contamination data. This represents more granular tri-attribution than the "pro-Russian hacktivist" framing used in initial reporting.

NIS2 Directive context: Poland transposed NIS2 into national law effective 2026-02-01 (Ustawa z dnia 28 listopada 2025 r. o krajowym systemie cyberbezpieczeństwa). Water distribution operators above the 50-employee threshold are now classified as Essential Entities under NIS2, subject to mandatory incident notification to CSIRT GOV (ABW) within 24/72 hours. ABW's annual report explicitly notes that the five named facilities fell below the NIS2 threshold at the time of intrusion, highlighting the coverage gap for small municipal operators. ABW is recommending legislative action to extend NIS2 obligations to critical-function entities regardless of headcount.
