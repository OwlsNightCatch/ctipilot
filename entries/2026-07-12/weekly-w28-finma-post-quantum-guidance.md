---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: FINMA sets post-quantum crypto expectations for the Swiss financial sector — Aufsichtsmitteilung 05/2026 flags 'harvest now, decrypt later' and a missing migration roadmap
headline: FINMA AM 05/2026 — Swiss financial institutions lack a post-quantum migration roadmap; FINMA sets crypto-inventory and crypto-agility expectations
summary: 'FINMA published Aufsichtsmitteilung 05/2026 on 9 July 2026, reporting a survey of 60 Swiss financial institutions on cryptographically-relevant quantum computing risk: institutions are aware of the threat but ''mostly lack a clear roadmap'' for migrating to quantum-safe encryption. FINMA names ''harvest now, decrypt later'' as the operative near-term threat and, under existing operational-risk expectations (not a new binding circular), expects institutions to build a PQC migration strategy, run an institution-specific risk analysis, maintain a cryptographic inventory, adopt crypto-agility, and extend this to outsourced providers. No new mandatory deadline is set — this is expectation-setting ahead of a possible future circular.'
discovered_at: '2026-07-12T23:54:00Z'
event_date: 2026-07-09
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - law-enforcement
regions:
  - switzerland
  - europe
sectors:
  - finance
entities: []
cves: []
sources:
  - url: https://www.finma.ch/news/2026/07/20260709-mm-am-05-26/
    publisher: FINMA (Swiss Financial Market Supervisory Authority)
    role: primary
  - url: https://www.swissinfo.ch/eng/various/finma-to-banks-further-measures-are-needed-to-tackle-quantum-computers/91726878
    publisher: SWI swissinfo.ch
    role: corroborating
closed_sources: []
evidence:
  - quote: Die Institute sind sich der Cyberrisiken von kryptografisch relevanten Quantum Computern bewusst. Meist fehlt aber eine klare Roadmap und eine ausreichend vorausschauende Planung für die Migration zu quantensicherer Verschlüsselung.
    publisher: FINMA
  - quote: Dazu gehört eine klare Strategie und Roadmap für die Migration zu quantensicheren Verschlüsselungen, eine institutsspezifische Risikoanalyse, die Erstellung eines kryptographischen Inventars, der Schutz kritischer Daten vor 'harvest now, decrypt later' Angriffen.
    publisher: FINMA
verification: multi-source
sourcing_note: Primary is FINMA's own supervisory communication (the home financial-sector regulator, authoritative for its own guidance); swissinfo.ch corroborates. Reliability A (FINMA for its own guidance), credibility 1 (the communication's content is directly reported and corroborated).
confidence: high
classification:
  reliability: A
  credibility: 1
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---
FINMA published **Aufsichtsmitteilung (supervisory communication) 05/2026** on 9 July 2026, presenting the results of a November 2025–January 2026 survey of 60 Swiss financial institutions on cryptographically-relevant quantum computing (CRQC) risk. Its core finding: institutions are aware of the threat but "meist fehlt aber eine klare Roadmap und eine ausreichend vorausschauende Planung für die Migration zu quantensicherer Verschlüsselung" — most lack a clear roadmap and sufficiently forward-looking planning for the migration to quantum-safe encryption ([FINMA, 2026-07-09](https://www.finma.ch/news/2026/07/20260709-mm-am-05-26/)). FINMA explicitly names **"harvest now, decrypt later"** — capture-and-store-for-future-decryption of today's encrypted traffic and data — as the operative near-term threat model, and sets, under existing operational-risk-and-resilience supervisory expectations rather than a new binding circular, that institutions should produce a PQC migration strategy and roadmap, run an institution-specific risk analysis, "die Erstellung eines kryptographischen Inventars" (build a cryptographic inventory), adopt crypto-agility, and extend the planning to outsourced service providers. No mandatory deadline accompanies the communication ([swissinfo.ch, 2026-07-10](https://www.swissinfo.ch/eng/various/finma-to-banks-further-measures-are-needed-to-tackle-quantum-computers/91726878)).

**Why this belongs in the strategic view:** it is the home financial-sector regulator setting a direction of travel that a Swiss/EU public-sector or CI reader will encounter next as a compliance expectation, and it reframes post-quantum readiness as a near-term data-protection issue, not a distant cryptographic curiosity — because the "harvest now, decrypt later" risk accrues from *today's* captured traffic regardless of when a CRQC actually arrives.

**Defender takeaway:** the defensible near-term action for finance-sector (and CI) readers is to start the cryptographic inventory now — enumerate which systems, protocols (TLS/VPN/at-rest) and applications use which algorithms and key lengths — because that inventory is the prerequisite for any migration and the only way to reason about HNDL exposure; watch for whether FINMA converts this into a binding circular and whether NCSC-CH or ENISA issue parallel public-sector PQC guidance.
