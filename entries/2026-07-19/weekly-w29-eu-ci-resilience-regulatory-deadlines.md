---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "EU critical-entity and product-resilience regulation reached concrete operator-facing milestones this week — ENISA shipped a CRA readiness self-assessment ahead of the 11 September reporting clock, and Germany's KRITIS-Dachgesetz opened its first CER-Directive registration window"
headline: "Two EU CI-resilience clocks advanced — ENISA's SME CRA maturity model ahead of the 11 Sept Article 14 duty, and Germany's KRITIS-Dachgesetz registration window"
summary: >
  Two EU critical-infrastructure resilience regulatory milestones landed inside 2026-W29, both moving from text to operator action. ENISA published (2026-07-13) a free SME Cyber Resilience Maturity Assessment Model — a diagnostic self-scoring tool across governance, risk management/secure-by-design, vulnerability management, product lifecycle and skills — explicitly timed ahead of the Cyber Resilience Act's first hard clock: from 11 September 2026, CRA Article 14 requires manufacturers of products with digital elements to issue a CSIRT/ENISA early warning within 24 hours of awareness of an actively exploited vulnerability, a fuller notification within 72 hours, and a final report within 14 days. Separately, Germany's KRITIS-Dachgesetz — the national transposition of the EU Critical Entities Resilience (CER) Directive — opened its first operator-registration window on 17 July 2026, requiring ~1,300 identified critical operators across ten sectors to register on a BBK/BSI platform within three months, starting clocks on a risk analysis (nine months) and a resilience plan (ten months). For a Swiss federal SOC both matter through the constituency's supplier and cross-border tail: EU-market suppliers of connected products to Swiss/European public-sector and CI customers are now on the CRA reporting clock, and Swiss organisations with German CI subsidiaries or CER-equivalent reporting relationships are inside the KRITIS-Dachgesetz scope.
discovered_at: "2026-07-19T23:56:00Z"
event_date: 2026-07-17
run_id: 2026-07-19T2310Z-weekly
priority: notable
immediate_action: null
tags:
  - law-enforcement
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - energy
  - water
  - transport
  - finance
  - telco
entities: []
cves: []
techniques: []
affected_products: []
sources:
  - url: "https://www.enisa.europa.eu/publications/sme-cyber-resilience-maturity-assessment-model"
    publisher: "ENISA"
    date: "2026-07-13"
    role: primary
  - url: "https://www.cyberresilienceact.eu/news/enisa-sme-cra-maturity-assessment-model.html"
    publisher: "cyberresilienceact.eu (CRA compliance tracker)"
    date: "2026-07-16"
    role: corroborating
  - url: "https://www.bbk.bund.de/DE/Themen/Kritische-Infrastrukturen/Strategien-und-rechtlicher-Rahmen/KRITISDachG/kritisdachg_node.html"
    publisher: "BBK (Bundesamt für Bevölkerungsschutz und Katastrophenhilfe)"
    date: "2026-03-17"
    role: primary
  - url: "https://www.channelpartner.de/article/4179709/die-zweite-kritis-frist-naht-was-jetzt-zu-tun-ist.html"
    publisher: "ChannelPartner (German IT trade press)"
    date: "2026-06-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "reaching a higher maturity level does not replace compliance with the CRA"
    publisher: "ENISA (via cyberresilienceact.eu account of the ENISA model)"
  - quote: "Das KRITIS-Dachgesetz (kurz: KRITISDachG) ist am 17.03.2026 in Kraft getreten"
    publisher: "BBK"
verification: multi-source
sourcing_note: "ENISA and BBK are authoritative primaries (A); the KRITIS-Dachgesetz registration-window opening (17 July 2026) is corroborated across BBK plus three independent German trade-press sources, but the specific administrative-fine figures diverge across secondary reporting (EUR 100,000 vs EUR 500,000 for a bare registration failure) and the BBK page's JS-rendered body did not yield the statutory amount — so fine amounts should be confirmed against the Bundesgesetzblatt text before being treated as exact. Reliability B / credibility 2 reflects that fine-figure uncertainty; the milestone events themselves are solid."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

The EU's two parallel resilience regimes — the product-side Cyber Resilience Act and the critical-entity-side CER Directive — both produced concrete, operator-facing milestones this week, extending the NIS2-transposition thread the prior two weeklies tracked into the product and physical-resilience tracks.

On the **CRA** side, ENISA published a free, Excel-based SME Cyber Resilience Maturity Assessment Model letting micro/small/medium manufacturers of products with digital elements self-score readiness across five domains (governance and documentation, risk management and secure-by-design/-by-default, vulnerability management, product lifecycle, and skills), explicit that it is diagnostic and that "reaching a higher maturity level does not replace compliance with the CRA" ([ENISA via cyberresilienceact.eu, 2026-07-16](https://www.cyberresilienceact.eu/news/enisa-sme-cra-maturity-assessment-model.html); [ENISA, 2026-07-13](https://www.enisa.europa.eu/publications/sme-cyber-resilience-maturity-assessment-model)). The timing is the point: from 11 September 2026, CRA Article 14 puts manufacturers on a 24-hour early-warning / 72-hour notification / 14-day final-report clock for actively exploited vulnerabilities in their products.

On the **CER** side, Germany's KRITIS-Dachgesetz — in force since 17 March 2026 ("Das KRITIS-Dachgesetz ... ist am 17.03.2026 in Kraft getreten," [BBK](https://www.bbk.bund.de/DE/Themen/Kritische-Infrastrukturen/Strategien-und-rechtlicher-Rahmen/KRITISDachG/kritisdachg_node.html)) — opened its first operator-registration window on 17 July 2026 ([ChannelPartner, 2026-06-05](https://www.channelpartner.de/article/4179709/die-zweite-kritis-frist-naht-was-jetzt-zu-tun-ist.html)). Roughly 1,300 identified critical operators across ten sectors must register on a joint BBK/BSI platform within three months, which starts clocks on a risk analysis (nine months) and a documented resilience plan (ten months). Reported fine figures for a registration failure diverge across secondary German trade press (EUR 100,000 vs EUR 500,000) and should be confirmed against the statutory text before being quoted as exact.

**Defender takeaway:** neither item is a threat, but both change defender/operator obligations the constituency will feel through its edges. The concrete, non-hypothetical actions already in motion: any EU-market product supplier serving Swiss/European public-sector or CI customers should map its products to the CRA Article 14 reporting duty before 11 September and can use ENISA's model as the starting self-assessment; and any Swiss-domiciled organisation with a German CI subsidiary or CER-equivalent reporting relationship is inside a live registration clock that opened this week. This is the EU's product- and physical-resilience regulation reaching the same operator-action stage the NIS2 transposition items did.
