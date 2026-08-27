---
schema: 1
kind: threat
horizon: operational
title: >
  DENIC .de DNSSEC outage — faulty key rollover; 3.5 h disruption for German government and
  public-sector .de domains
headline: >
  DENIC .de DNSSEC outage — faulty key rollover; 3.5 h disruption for German government and
  public-sector .de domains
summary: >
  On 2026-05-05 at 21:43 UTC, DENIC (the .de domain registry) began distributing invalid DNSSEC
  signatures for the .de TLD, making approximately 18 million .de domains unreachable for
  DNSSEC-validating resolvers for roughly 3.5 hours (DENIC blog post-incident report, 2026-05-08 ·
  DENIC initial report, 2026-05-05).
discovered_at: "2026-05-09T05:00:02Z"
updated_at: "2026-05-10T05:00:11Z"
event_date: 2026-05-08
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - eu-nexus
regions:
  - europe
  - dach
sectors:
  - public-sector
entities:
  - "incident:denic-dnssec-outage-2026"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://blog.denic.de/en/technical-issue-with-de-domains-resolved/"
    publisher: "DENIC post-incident report, 2026-05-08"
    role: primary
  - url: "https://blog.denic.de/en/denic-reports-dnssec-disruption-affecting-de-domains/"
    publisher: "DENIC initial report, 2026-05-05"
    role: corroborating
  - url: "https://blog.cloudflare.com/de-tld-outage-dnssec/"
    publisher: Cloudflare blog — .de TLD outage
    role: corroborating
  - url: "https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/"
    publisher: "DENIC analysis blog (German), 2026-05-08"
    role: primary
  - url: "https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html"
    publisher: "heise online, 2026-05-08"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
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
migrated_from: briefs/2026-05-09.md
---

On 2026-05-05 at 21:43 UTC, DENIC (the .de domain registry) began distributing invalid DNSSEC signatures for the .de TLD, making approximately 18 million .de domains unreachable for DNSSEC-validating resolvers for roughly 3.5 hours ([DENIC blog post-incident report, 2026-05-08](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/) · [DENIC initial report, 2026-05-05](https://blog.denic.de/en/denic-reports-dnssec-disruption-affecting-de-domains/)). Root cause: a software defect in DENIC's HSM integration code introduced during a March 2026 migration to Knot DNS generated three key pairs sharing keytag 33834, but only one public key was published in the zone; inconsistent signing across name servers followed. Cloudflare deployed a Negative Trust Anchor under RFC 7646 for its resolvers within ~90 minutes; DENIC restored service by 01:15 UTC on 2026-05-06. Crucially, .ch was unaffected ([heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html) · [Cloudflare blog](https://blog.cloudflare.com/de-tld-outage-dnssec/)). This is an operational misconfiguration, not an attacker action.

**Defender takeaway:** DNSSEC registry-side errors are indistinguishable from attacker-induced validation failures from the resolver's perspective. Defenders should maintain RFC 7646 Negative Trust Anchor capability in their validating resolvers for continuity during registry incidents. German public-sector operators relying on .de-hosted services (government portals, MX records, API endpoints) should review their incident runbooks for DNSSEC-induced availability events to separate "registry outage" from "zone-level attack."

## Update — 2026-05-10T05:00:11Z

DENIC published its formal technical post-mortem on 2026-05-08 ([DENIC analysis blog (German), 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/) · [heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html)).

Confirmed root cause: a code defect in DENIC's third-generation custom signing infrastructure (deployed April 2026 atop Knot DNS). During a routine Zone-Signing-Key rotation the code generated **three private key pairs all assigned the same Key Tag (33834)** rather than a unique tag per key — and only one corresponding public DNSKEY record was published to the zone. The RRSIG records signed by the two unpublished keys were therefore unvalidatable; DNSSEC-validating resolvers marked all .de delegations as "Bogus", which through the bogus NSEC3 trust path also took down resolution for non-DNSSEC-signed .de domains.

The outage ran 2026-05-05 21:43 UTC → 2026-05-06 ~01:15 UTC (~3.5 h). Critically, DENIC notes the monitoring pipeline detected anomalous resolver behaviour but **the alerting layer did not correctly forward the alerts** — the SIEM-rule equivalent of a fire-but-don't-page failure. Knot DNS itself is not implicated; the bug was in DENIC's automation layer atop Knot.

Defender takeaway: DNSSEC registry-side errors are indistinguishable from attacker-induced trust failures from a resolver's perspective. Validating-resolver operators in DACH and EU public-sector environments should keep RFC 7646 Negative Trust Anchor capability live for continuity during registry incidents and ensure runbooks separate "registry KSK/ZSK rollover defect" from "zone-level attack on a downstream domain".
