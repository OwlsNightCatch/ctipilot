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
  a severe incident) — all submitted through ENISA's centralised Single Reporting Platform, which its own FAQ still
  had no published URL for eight days before go-live.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: "2026-09-03T05:06:30Z"
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
  - url: "https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions"
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
    date: "2026-08-31"
    role: corroborating
  - url: "https://www.hlc.com/en/publications/eu-cyber-resilience-act-preparing-for-vulnerability-and-incident-reporting"
    publisher: "Hogan Lovells Cadwalader (legal analysis)"
    date: "2026-06-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For an actively exploited vulnerability or a severe incident, an early warning must be submitted within 24 hours of the manufacturer becoming aware of it. The notification must be supplemented within 72 hours."
    publisher: "NCSC-FI / Traficom"
  - quote: "For a vulnerability, the final report must be submitted within 14 days after a corrective or mitigating measure becomes available. For a severe incident, the final report must be submitted within one month of the incident notification."
    publisher: "NCSC-FI / Traficom"
  - quote: "Notifications are expected to be possible through APIs from spring 2027. After this, notifications can be submitted directly from the organisation's own system."
    publisher: "NCSC-FI / Traficom"
  - quote: "The platform is scheduled to be operational by 11 September 2026."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "however no Application Programming Interfaces will be provided at this stage"
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "Non-validated ARs will be able to submit up to 20 notifications for one manufacturer before validation becomes mandatory."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "Notably, the reporting obligations apply from 11 September 2026 to all products with digital elements within the CRA's scope that have been made available on the EU market before full CRA application (Art. 69(3) CRA)."
    publisher: "Hogan Lovells Cadwalader"
verification: multi-source
sourcing_note: >
  NCSC-FI is a national authority acting as primary discloser for its own jurisdiction's implementation guidance.
  ENISA's own SRP FAQ (updated 2026-08-31) now independently corroborates the 24h/72h/14-day/1-month notification
  clock itself, not only the platform's go-live date. The API-submission target of spring 2027 remains NCSC-FI's own
  claim, not independently confirmed by ENISA, whose FAQ states only that no API will be provided "at this stage"
  with no specific date. Credibility on the reporting-clock claim moves from 2 to 1 given this independent
  corroboration; the uncorroborated API-timeline claim keeps the entry at an overall credibility of 2. NCSC-FI's
  checklist and ENISA's FAQ disagree on the Assigned Representative cap (NCSC-FI: two named representatives; ENISA:
  one Primary plus up to 20 Secondary) — the entry surfaces both figures rather than silently picking one, per the
  fake-news/contradiction-handling policy.
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
updates:
  - at: "2026-09-03T05:06:30Z"
    run_id: 2026-09-03T0410Z-intel
    type: update
    summary: >
      ENISA's own Single Reporting Platform FAQ (updated 31 August 2026) independently confirms the 24h/72h/14-day/
      1-month notification clock this entry previously attributed to NCSC-FI alone, and corrects the Assigned
      Representative cap from "two" to one Primary plus up to 20 Secondary ARs. Eight days before the 11 September
      go-live, the FAQ still gives no published platform URL and confirms no API will exist at launch, so an
      automated reporting pipeline must still terminate at a manual web-portal boundary within the 24-hour window.
    fields: [sources, evidence, sourcing_note, summary, body]
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
ENISA's own FAQ for the platform independently states the identical clock
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
The SRP itself is only "scheduled to be operational by 11 September 2026" — the same date the reporting duty starts
to apply — and, eight days before that go-live, ENISA's FAQ still gives no published platform URL, stating only that
it "will be communicated and published in due course"
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
NCSC-FI's checklist directs manufacturers to identify in-scope products now — noting that products past end-of-life
and no longer receiving updates remain subject to the reporting obligation — appoint an Assigned Representative (AR)
authorised to submit SRP notifications, document an internal report-intake and triage process, and rehearse it at
least once before the first reportable case
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
ENISA's own FAQ states a manufacturer may register one Primary AR and up to 20 Secondary ARs, and that a
non-validated AR may still submit up to 20 notifications before validation becomes mandatory, so an organisation
does not have to wait for validation to complete before filing its first report under time pressure
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
NCSC-FI's own checklist instead describes notifications as submittable only through two named representatives, a
narrower figure than ENISA's; the two authorities have not been reconciled, and ENISA's FAQ is treated as the more
current statement of the platform's own rules
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
API-based submission is not expected until spring 2027 per NCSC-FI, and ENISA's own FAQ confirms only that "no
Application Programming Interfaces will be provided at this stage," without independently stating a target date —
so any automated vulnerability-management or SBOM-correlation pipeline still has to terminate at a manual web-portal
boundary for every notification filed before that changes
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act);
[ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
The reporting duty is not limited to products launched after 11 September 2026: legal analysis of Article 69(3) CRA
confirms it applies from that date to every in-scope product already placed on the EU market
([Hogan Lovells Cadwalader, 2026-06-10](https://www.hlc.com/en/publications/eu-cyber-resilience-act-preparing-for-vulnerability-and-incident-reporting)),
and NCSC-FI's own checklist states products past end-of-life and no longer receiving updates remain subject to the
obligation regardless
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).

**Defender takeaway:** any organisation manufacturing or supplying products with digital elements into the EU market
— including Swiss suppliers exporting into it — should confirm now that a Primary Assigned Representative (and,
where useful, Secondary ARs) is registered or ready to register on the SRP, that the 24-hour/72-hour/14-day/1-month
clock is built into the organisation's own incident-response runbook as a manual, portal-only filing step, and that
the process has been rehearsed at least once before 11 September 2026 — including for legacy products past
end-of-life, which remain subject to the obligation.

## Update — 2026-09-03T05:06:30Z

ENISA's own Single Reporting Platform FAQ, updated 31 August 2026, now independently states the same 24-hour/
72-hour/14-day/1-month notification clock this entry previously sourced to NCSC-FI alone
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
The Assigned Representative cap this entry previously described as "two" is corrected: ENISA's FAQ states a
manufacturer may register exactly one Primary AR and up to 20 Secondary ARs, and that a non-validated AR can submit
up to 20 notifications before validation becomes mandatory
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
Eight days before the 11 September go-live, the platform still has no published URL and the FAQ confirms no API will
exist at launch, without stating a specific date for one — the spring-2027 API target remains NCSC-FI's own claim,
not independently corroborated
([ENISA, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
Legal analysis of Article 69(3) CRA confirms the reporting duty applies from 11 September 2026 to every in-scope
product already on the EU market
([Hogan Lovells Cadwalader, 2026-06-10](https://www.hlc.com/en/publications/eu-cyber-resilience-act-preparing-for-vulnerability-and-incident-reporting)),
consistent with NCSC-FI's own checklist, which states products past end-of-life and no longer receiving updates
remain subject to the obligation regardless
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
The SRP will be available in English only at launch
([ENISA — Single Reporting Platform (SRP) FAQ, 2026-08-31](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
