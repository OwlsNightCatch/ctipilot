---
schema: 1
kind: policy
title: "DENIC .de DNSSEC outage: a faulty key rollover made all .de domains unresolvable for validating resolvers for more than three hours on 5 May 2026"
headline: "DENIC's new signing system made one key pair per HSM, so most .de signatures failed validation for over three hours"
summary: >
  A routine DNSSEC key rollover on 2026-05-05 left the .de zone with signatures validating resolvers could
  not verify, from an onset the sources place between about 19:30 and 19:57 UTC until DENIC restored normal
  operation at 23:15 UTC. DENIC's new
  signing system generated one key pair per HSM instead of one shared pair, so only one matched the
  published DNSKEY; unverifiable NSEC3 signatures broke even unsigned .de domains.
discovered_at: "2026-05-09T05:00:02Z"
updated_at: "2026-05-10T05:00:11Z"
event_date: "2026-05-05"
run_id: 2026-05-09-migrated
priority: routine
immediate_action: null
tags:
  - eu-nexus
regions:
  - europe
  - dach
sectors: []
entities:
  - "incident:denic-dnssec-outage-2026"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://blog.denic.de/en/technical-issue-with-de-domains-resolved/"
    publisher: "DENIC"
    date: "2026-05-06"
    role: primary
  - url: "https://blog.denic.de/en/denic-reports-dnssec-disruption-affecting-de-domains/"
    publisher: "DENIC"
    date: "2026-05-05"
    role: corroborating
  - url: "https://blog.cloudflare.com/de-tld-outage-dnssec/"
    publisher: "Cloudflare"
    date: "2026-05-06"
    role: corroborating
  - url: "https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/"
    publisher: "DENIC analysis"
    date: "2026-05-08"
    role: primary
  - url: "https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html"
    publisher: "heise online"
    date: "2026-05-08"
    role: corroborating
  - url: "https://blog.denic.de/en/final-report-dns-outage-of-5-may-2026/"
    publisher: "DENIC final report"
    date: "2026-06-11"
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
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
  - at: "2026-05-10T05:00:11Z"
    run_id: 2026-05-10-001
    type: update
    summary: >
      UPDATE (originally covered 2026-05-09): DENIC published its formal technical post-mortem on
      2026-05-08 (DENIC analysis blog (German), 2026-05-08 · heise online, 2026-05-08).
    fields:
      - sources
      - body
    merged_from: 2026-05-10/denic-de-dnssec-outage-post-mortem-three-private-keys-genera
  - at: "2026-10-11T14:30:46Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The times were local time labelled UTC: the outage began between about 19:30 and 19:57 UTC, depending on the source, and ended at 23:15 UTC, about three and a half hours. Cloudflare's mitigation came about 2 hours 45 minutes after onset through an override rule, not an RFC 7646 negative trust anchor within 90 minutes; the 18 million domains, the government focus and the statement that .ch was unaffected had no source. DENIC's later addendum of 11 May replaces the key-tag collision account: one key pair per HSM instead of a shared pair. The signing system went live in April, not March. The entry is recorded as a non-adversarial resilience item with a rating and priority routine, and both sections are corrected in place.
    fields: [kind, title, headline, summary, priority, tags, techniques, sources, classification, body, sectors]
  - at: "2026-10-21T12:11:29Z"
    run_id: 2026-10-21T1149Z-audit
    type: correction
    summary: >
      The outage date is 5 May 2026; 8 May is the date of DENIC's initial analysis, and Cloudflare's
      account is dated 6 May. DENIC's final report of 11 June 2026 is added: it confirms the initial
      analysis, rules out compromise and Knot or HSM malfunctions, explains why the single-HSM test
      environment missed the defect, and lists DENIC's measures. The account dated 10 May now gives only
      what DENIC had published by then; the 11 May addendum stays in the later section. The title and
      headline now give the duration as more than three hours, matching the 19:57 to 23:15 UTC timeline.
    fields: [event_date, sources, body, headline, title]
migrated_from: briefs/2026-05-09.md
---

During a routine, scheduled DNSSEC key rollover on the evening of 2026-05-05, DENIC distributed signatures for the `.de` zone that validating resolvers could not verify, so they treated responses for all `.de` domains as bogus ([DENIC, 2026-05-06](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/)). DENIC dates the incident from 21:57, began distributing a correct zone at 00:08 and had fully restored normal operation by 01:15 on 2026-05-06, giving no time zone; read as CEST, that is 19:57 to 23:15 UTC ([DENIC, 2026-05-06](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/)); Cloudflare saw SERVFAILs from about 19:30 UTC and rolled out its own mitigation at 22:17 UTC through an existing override rule, having no native negative trust anchor mechanism ([Cloudflare, 2026-05-06](https://blog.cloudflare.com/de-tld-outage-dnssec/)); heise gives 21:43 for the first disruption, which read as CEST is 19:43 UTC ([heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html)), so the three sources give three onsets. DENIC's analysis traces the fault to in-house code around its hardware security modules in the third-generation signing system it put into operation in April 2026: instead of one key pair stored on three HSMs, the software generated three different key pairs, one per HSM, and only one of them matched the pre-published DNSKEY ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)). Because signatures over NSEC3 records were also unverifiable, even second-level domains without DNSSEC failed to resolve, and DENIC's three permanent validation tools detected the anomaly but their alerts were not processed correctly ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)). DENIC's final report of 2026-06-11 confirms that initial analysis, rules out any compromise of the signing system and any malfunction of Knot or the HSMs, and explains that the test environment, a single HSM at one location, did not fully execute the rollover-agent code, which misbehaves only when several HSMs are connected ([DENIC final report, 2026-06-11](https://blog.denic.de/en/final-report-dns-outage-of-5-may-2026/)).

**Defender takeaway:** a TLD-side DNSSEC failure looks the same as an attack to a validating resolver; operators of validating resolvers should have a tested way to mark a broken TLD as insecure and should rely on serve-stale to absorb the first hours, as Cloudflare did ([Cloudflare, 2026-05-06](https://blog.cloudflare.com/de-tld-outage-dnssec/)).

## Update — 2026-05-10T05:00:11Z

DENIC published its initial analysis on 2026-05-08 ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)) ([heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html)). A faulty piece of code in its in-house development generated three different key pairs instead of one for the same key tag, 33834, and only one of their public keys was in the DNSKEY record, so only about a third of the signatures could be validated ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)). Knot itself is standard software in the process; the defect was in DENIC's own code ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)). DENIC's validation tools detected the faulty signatures as designed, but their alerts were not processed correctly ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)).

## Correction — 2026-10-11T14:30:46Z

DENIC gives 21:57 and 01:15 without a time zone; read as CEST, the incident ran from 19:57 UTC until normal operation returned at 23:15 UTC ([DENIC, 2026-05-06](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/)), and Cloudflare dates the onset to about 19:30 UTC and its own mitigation, an override rule rather than a native negative trust anchor, to 22:17 UTC ([Cloudflare, 2026-05-06](https://blog.cloudflare.com/de-tld-outage-dnssec/)). DENIC's addendum of 11 May 2026 says no key-tag collision occurred; the software generated one key pair per HSM, and only one matched the published DNSKEY ([DENIC analysis, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)). No source gives 18 million affected domains, singles out government domains, or mentions `.ch`.

## Correction — 2026-10-21T12:11:29Z

The outage began on the evening of 2026-05-05 ([DENIC, 2026-05-06](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/)). DENIC's final report of 2026-06-11 confirms the findings of its initial analysis of 2026-05-08 and lists its short-term measures: additional alerts based on better visibility of errors, including those in the continuously running testing and validation tools; an accelerated procedure to provide a valid zone backup in an emergency; partial validation of the zone before deployment; no further ZSK rollover until further measures are complete, including a more secure software development process and a test environment with higher coverage; and an external security and process analysis ([DENIC final report, 2026-06-11](https://blog.denic.de/en/final-report-dns-outage-of-5-may-2026/)).
