---
schema: 1
kind: policy
title: "Finland's NCSC-FI publishes an operational manufacturer checklist for the EU Cyber Resilience Act's 24h/72h/14-day/1-month reporting clock, two weeks before the 11 September 2026 go-live"
headline: "NCSC-FI supplies the CRA reporting deadlines the Commission's own guidance had left unstated"
summary: >
  With the EU Cyber Resilience Act's mandatory vulnerability/incident-reporting obligation taking effect on
  11 September 2026, Finland's national cybersecurity authority (NCSC-FI, part of Traficom) published a manufacturer
  checklist on 2026-08-28 specifying the exact notification clock: a 24-hour early warning, a 72-hour supplemented
  notification, and a final report due 14 days after a fix (for a vulnerability) or one month after notification (for
  a severe incident) — all submitted through ENISA's centralised Single Reporting Platform, which itself only goes
  live on 11 September 2026.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-28"
run_id: 2026-08-29T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, eu-nexus]
regions: [europe]
sectors: [public-sector, technology, energy, water, transport, healthcare, finance, telco]
entities:
  - policy:eu-cyber-resilience-act
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act"
    publisher: "NCSC-FI / Traficom (Finnish Transport and Communications Agency)"
    date: "2026-08-28"
    role: primary
  - url: "https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp"
    publisher: "ENISA — Single Reporting Platform (SRP)"
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For an actively exploited vulnerability or a severe incident, an early warning must be submitted within 24 hours of the manufacturer becoming aware of it. The notification must be supplemented within 72 hours."
    publisher: "NCSC-FI / Traficom"
  - quote: "For a vulnerability, the final report must be submitted within 14 days after a corrective or mitigating measure becomes available. For a severe incident, the final report must be submitted within one month of the incident notification."
    publisher: "NCSC-FI / Traficom"
  - quote: "Notifications are expected to be possible through APIs from spring 2027. After this, notifications can be submitted directly from the organisation's own system."
    publisher: "NCSC-FI / Traficom"
verification: multi-source
sourcing_note: >
  NCSC-FI is a national authority acting as primary discloser for its own jurisdiction's implementation guidance.
  ENISA's own SRP page independently confirms only the platform's 2026-09-11 go-live date; the specific 24h/72h/14-
  day/1-month notification-clock detail is NCSC-FI's alone and not independently corroborated by ENISA or any other
  source. NCSC-FI is not on this deployment's national-CERT single-source carve-out list, so credibility reflects an
  authoritative but uncorroborated primary disclosure rather than a fully confirmed report.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The EU Cyber Resilience Act's reporting obligations bind from 11 September 2026, requiring manufacturers of
"products with digital elements" placed on the EU market to report actively exploited vulnerabilities and severe
incidents through ENISA's centralised Single Reporting Platform (SRP)
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
On 2026-08-28, with two weeks left before the obligation binds, NCSC-FI published a manufacturer checklist
supplying the concrete notification clock: an early warning within 24 hours of the manufacturer becoming aware of an
actively exploited vulnerability or severe incident, supplemented within 72 hours; for a vulnerability, a final
report within 14 days after a corrective or mitigating measure becomes available; for a severe incident, a final
report within one month of the incident notification
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
The SRP itself only becomes live on 2026-09-11 — the same date the reporting duty starts to apply
([ENISA, 2026-08-14](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp)). NCSC-FI's
checklist directs manufacturers to identify in-scope products now — noting that products past end-of-life and no
longer receiving updates remain subject to the reporting obligation — appoint a primary and backup "Assigned
Representative" (AR) authorised to submit SRP notifications, document an internal report-intake and triage process,
and rehearse it at least once before the first reportable case
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
API-based submission is not expected until spring 2027; until then, only the two named Assigned Representatives per
manufacturer can file, which is a concrete operational bottleneck for any organisation planning its incident-response
workflow around the deadline
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).

**Defender takeaway:** any organisation manufacturing or supplying products with digital elements into the EU market
— including Swiss suppliers exporting into it — should confirm now that an Assigned Representative and backup are
registered or ready to register on the SRP, that the 24-hour/72-hour/14-day/1-month clock is built into the
organisation's own incident-response runbook, and that the process has been rehearsed at least once before
11 September 2026.
