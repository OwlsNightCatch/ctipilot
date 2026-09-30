---
schema: 1
kind: policy
title: "Finland's NCSC-FI publishes an operational manufacturer checklist for the EU Cyber Resilience Act's 24h/72h/14-day/1-month reporting clock, two weeks before the 11 September 2026 go-live"
headline: "NCSC-FI supplies the CRA reporting deadlines the Commission's own guidance had left unstated"
summary: >
  Finland's national cybersecurity authority (NCSC-FI, part of Traficom) published a manufacturer checklist on
  2026-08-28 ahead of the EU Cyber Resilience Act's mandatory vulnerability/incident-reporting obligation, specifying
  the exact notification clock: a 24-hour early warning, a 72-hour supplemented notification, and a final report due
  14 days after a fix (for a vulnerability) or one month after notification (for a severe incident) — all submitted
  through ENISA's centralised Single Reporting Platform. That obligation is now in legal effect as of 2026-09-11.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: "2026-09-12T04:09:19Z"
event_date: "2026-08-28"
run_id: 2026-08-29T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, policy]
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
  - url: "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting"
    publisher: "European Commission — Shaping Europe's Digital Future"
    date: "2026-07-31"
    role: primary
  - url: "https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp"
    publisher: "ENISA — Single Reporting Platform (SRP) page"
    date: "2026-09-10"
    role: primary
  - url: "https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched"
    publisher: "ENISA"
    date: "2026-09-11"
    role: primary
  - url: "https://www.heise.de/news/Gilt-ab-heute-CRA-setzt-24-Stunden-Frist-fuer-Sicherheitsmeldungen-11450208.html"
    publisher: "heise online"
    date: "2026-09-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For an actively exploited vulnerability or a severe incident, an early warning must be submitted within 24 hours of the manufacturer becoming aware of it. The notification must be supplemented within 72 hours."
    publisher: "NCSC-FI / Traficom"
  - quote: "For a vulnerability, the final report must be submitted within 14 days after a corrective or mitigating measure becomes available. For a severe incident, the final report must be submitted within one month of the incident notification."
    publisher: "NCSC-FI / Traficom"
  - quote: "Notifications are expected to be possible through APIs from spring 2027. After this, notifications can be submitted directly from the organisation's own system."
    publisher: "NCSC-FI / Traficom"
  - quote: "The platform has become operational on 11 September 2026, coinciding with the date on which the CRA reporting obligations under Art.14 are applicable."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "However, no Application Programming Interface (API) will be provided at the initial release of the SRP, so notifications must be submitted through the platform interface."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "ARs whose manufacturer association has not yet been verified may submit up to 20 notifications for that manufacturer before verification becomes mandatory."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "In the current release, the 72-hour counter displays a due date/time 48hrs after submission of the 24-hour Early Warning."
    publisher: "ENISA — Single Reporting Platform (SRP) FAQ"
  - quote: "Notably, the reporting obligations apply from 11 September 2026 to all products with digital elements within the CRA's scope that have been made available on the EU market before full CRA application (Art. 69(3) CRA)."
    publisher: "Hogan Lovells Cadwalader"
  - quote: "As of 11 September 2026, manufacturers are required to report actively exploited vulnerabilities and severe incidents impacting the security of products with digital elements."
    publisher: "European Commission — Shaping Europe's Digital Future"
    source_url: "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting"
  - quote: "ENISA has established the CRA Single Reporting Platform (SRP), operational as of 11 September 2026."
    publisher: "European Commission — Shaping Europe's Digital Future"
    source_url: "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting"
  - quote: "From 11 September 2026, manufacturers are required to submit these mandatory notifications through the SRP."
    publisher: "ENISA — Single Reporting Platform (SRP) page"
    source_url: "https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp"
  - quote: "The EU Agency for Cybersecurity (ENISA) has deployed the initial operating capability of the Single Reporting Platform (SRP)."
    publisher: "ENISA"
    source_url: "https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched"
  - quote: "Der Bitkom kritisiert insbesondere, dass Unternehmen die Meldeplattform vor deren Start nicht registrieren und die Prozesse nicht erproben konnten. Die Plattform ging erst mit Beginn der Meldepflicht online. (translated from German: Bitkom specifically criticizes that companies could not register on the reporting platform or test their processes before its start. The platform only went online with the start of the reporting obligation.)"
    original: "Der Bitkom kritisiert insbesondere, dass Unternehmen die Meldeplattform vor deren Start nicht registrieren und die Prozesse nicht erproben konnten. Die Plattform ging erst mit Beginn der Meldepflicht online."
    publisher: "heise online (relaying a Bitkom survey finding)"
    source_url: "https://www.heise.de/news/Gilt-ab-heute-CRA-setzt-24-Stunden-Frist-fuer-Sicherheitsmeldungen-11450208.html"
verification: multi-source
sourcing_note: >
  NCSC-FI is a national authority acting as primary discloser for its own jurisdiction's implementation guidance.
  ENISA's own SRP FAQ (updated 2026-08-31) now independently corroborates the 24h/72h/14-day/1-month notification
  clock itself, not only the platform's go-live date. The API-submission target of spring 2027 remains NCSC-FI's own
  claim, not independently confirmed by ENISA, whose FAQ states only that no API will be provided "at the initial release of the SRP"
  with no specific date. Credibility on the reporting-clock claim moves from 2 to 1 given this independent
  corroboration; the uncorroborated API-timeline claim keeps the entry at an overall credibility of 2. NCSC-FI's
  checklist and ENISA's FAQ disagree on the Assigned Representative cap (NCSC-FI: two named representatives; ENISA:
  one Primary plus up to 20 Secondary) — the entry surfaces both figures rather than silently picking one, per the
  fake-news/contradiction-handling policy. ENISA's SRP overview page is a continuously-updated hub rather than a
  dated article; its own sub-pages carry explicit "Updated: 9/10 September 2026" labels, which is why this entry
  cites it at 2026-09-10, even though the page's own extracted publication metadata is older. ENISA's
  separate 2026-09-11 news post confirms the platform's operational status directly, resolving the
  open point the prior update recorded; heise online's same-day reporting adds an independent
  preparedness-survey data point (Bitkom) not carried by either primary.
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
  - at: "2026-09-11T04:40:00Z"
    run_id: 2026-09-11T0410Z-intel
    type: update
    summary: >
      The reporting obligation this entry tracked ahead of go-live is now in legal effect: as of
      2026-09-11, CRA Article 14 mandatory reporting binds every in-scope manufacturer, including
      products already on the EU market before this date. Neither the European Commission's own
      page nor ENISA's SRP page states the platform is confirmed live and accepting submissions
      today, only that this was ENISA's operational target — recorded as an open point rather than
      asserted.
    fields: [summary, sourcing_note, body, sources, evidence, tags]
  - at: "2026-09-12T04:09:19Z"
    run_id: 2026-09-12T0409Z-intel
    type: update
    summary: >
      ENISA confirmed on 2026-09-11 that the CRA Single Reporting Platform has deployed its
      initial operating capability, resolving the open point the prior update recorded. A Bitkom
      survey, relayed the same day by heise online, finds only 29% of German firms understand what the
      CRA means for their organization and that manufacturers could not register or test their
      reporting process before the platform went live with the reporting obligation itself.
    fields: [sourcing_note, sources, evidence, body]
  - at: "2026-09-29T21:59:19Z"
    run_id: 2026-09-29T2134Z-audit
    type: improvement
    summary: >
      The European Commission's CRA reporting page now states that ENISA has established the Single
      Reporting Platform, operational as of 11 September 2026, a second authority confirming the
      launch ENISA announced on 2026-09-11. ENISA's FAQ, revised on 17 September, now gives the
      platform address and the EU Login multi-factor requirement, rewords the no-API and
      unverified-representative answers, and warns that the platform's 72-hour counter currently shows
      the deadline 48 hours after the early warning. The main analysis and the cited evidence follow
      both pages' current text instead of the pre-launch wording. The sourcing note quotes the FAQ's
      current wording, and the Commission citation carries the page's 11 September update date.
    fields: [evidence, sourcing_note, body]
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
The SRP became operational on 11 September 2026, the same date the reporting duty started to apply, and is reached
at portal.cra-srp.enisa.europa.eu through a personal EU Login account with multi-factor authentication
([ENISA, updated 2026-09-17](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
NCSC-FI's checklist directs manufacturers to identify in-scope products now — noting that products past end-of-life
and no longer receiving updates remain subject to the reporting obligation — appoint an Assigned Representative (AR)
authorised to submit SRP notifications, document an internal report-intake and triage process, and rehearse it at
least once before the first reportable case
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
ENISA's own FAQ states a manufacturer may register one Primary AR and up to 20 Secondary ARs, and that a
representative whose manufacturer association is not yet verified may still submit up to 20 notifications for that
manufacturer before verification becomes mandatory, so an organisation does not have to wait for verification to
complete before filing its first report under time pressure
([ENISA, updated 2026-09-17](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
NCSC-FI's own checklist instead describes notifications as submittable only through two named representatives, a
narrower figure than ENISA's; the two authorities have not been reconciled, and ENISA's FAQ is treated as the more
current statement of the platform's own rules
([NCSC-FI / Traficom, 2026-08-28](https://www.kyberturvallisuuskeskus.fi/en/news/manufacturers-prepare-advance-reporting-vulnerabilities-and-incidents-under-cyber-resilience-act)).
API-based submission is not expected until spring 2027 per NCSC-FI, and ENISA's own FAQ states only that "no
Application Programming Interface (API) will be provided at the initial release of the SRP" and that one may follow
in a later phase, without a target date —
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
the process has been rehearsed at least once — including for legacy products past end-of-life, which remain subject
to the obligation. The runbook should time the 72-hour notification from the moment of awareness, not from the
platform's own counter, which in its current release can show a report as due or overdue early.

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

## Update — 2026-09-11T04:40:00Z

The obligation this entry has tracked ahead of go-live is now in legal effect: the European Commission's own page states plainly, "as of 11 September 2026, manufacturers are required to report actively exploited vulnerabilities and severe incidents impacting the security of products with digital elements"
([European Commission, 2026-07-31](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)).
This covers every in-scope product already placed on the EU market before today, not only new ones, consistent with Article 69(3) CRA as this entry already recorded. Neither the Commission's page nor ENISA's own SRP page states that the platform is confirmed live and accepting submissions today — the Commission's page says only that "the Single Reporting Platform will be operational by 11 September 2026 (date of entry into application of the CRA reporting requirements)" and that "functional and security testing are under way"
([European Commission, 2026-07-31](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)),
while ENISA's own SRP page states that "from 11 September 2026, manufacturers are required to submit these mandatory notifications through the SRP" without an explicit operational-status confirmation
([ENISA, 2026-09-10](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp)).
This entry therefore scopes its claim to what is independently confirmed — the legal reporting obligation is in effect — rather than to platform operational status, which no source reached has confirmed either way as of today.

## Update — 2026-09-12T04:09:19Z

The open point above is resolved: ENISA confirmed on 2026-09-11 that "the EU Agency for Cybersecurity (ENISA) has deployed the initial operating capability of the Single Reporting Platform (SRP)"
([ENISA, 2026-09-11](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)),
manufacturers and, from 11 December 2027, open-source software stewards submit once through the platform and the receiving CSIRT disseminates the notification to every other Member State CSIRT where the affected product is available, simultaneously to ENISA.
A Bitkom survey of 1,003 German firms, relayed the same day by heise online, found only 29% know what the CRA means for their own organization and a further 38% have heard of it but cannot assess the impact; Bitkom specifically criticizes that manufacturers could not register on the platform or test their reporting process before today, "because the platform only went online with the start of the reporting obligation" (translated from German)
([heise online, 2026-09-11](https://www.heise.de/news/Gilt-ab-heute-CRA-setzt-24-Stunden-Frist-fuer-Sicherheitsmeldungen-11450208.html)).
For a Swiss manufacturer or distributor placing networked products on the EU market, or a Swiss public-sector body procuring from an EU-regulated manufacturer now subject to this clock, the practical takeaway is that the 24-hour/72-hour/14-day-or-1-month reporting chain is a live obligation rather than a target date, and a first submission may hit friction precisely because pre-launch registration and testing were not possible.

## Improvement — 2026-09-29T21:59:19Z

The European Commission's own CRA reporting page now also confirms the launch: "ENISA has established the CRA Single Reporting Platform (SRP), operational as of 11 September 2026" ([European Commission, updated 2026-09-11](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)). The page previously gave 11 September 2026 as the target date with testing under way, which is the wording quoted in the 2026-09-11 section above.

ENISA's FAQ, revised on 17 September, now also answers the questions this entry left open before launch. The platform is at portal.cra-srp.enisa.europa.eu and each Assigned Representative signs in with a personal EU Login account with multi-factor authentication. No API exists at the initial release, and ENISA says only that one may be considered in a future phase. One operational detail matters for the reporting clock: "In the current release, the 72-hour counter displays a due date/time 48hrs after submission of the 24-hour Early Warning", so the platform can mark a notification overdue before 72 hours have passed since the manufacturer became aware. ENISA says a later release will count from the awareness time instead ([ENISA, updated 2026-09-17](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)).
