---
schema: 1
kind: threat
horizon: operational
title: "DENIC .de DNSSEC outage post-mortem — three private keys generated with the same Key Tag (33834); only one DNSKEY published"
headline: "DENIC .de DNSSEC outage post-mortem — three private keys generated with the same Key Tag (33834); only one DNSKEY published"
summary: "UPDATE (originally covered 2026-05-09): DENIC published its formal technical post-mortem on 2026-05-08 (DENIC analysis blog (German), 2026-05-08 · heise online, 2026-05-08)."
discovered_at: "2026-05-10T05:00:11Z"
event_date: 2026-05-08
run_id: 2026-05-10-001
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
cves: []
sources:
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
update_of: 2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
---

**UPDATE (originally covered 2026-05-09):** DENIC published its formal technical post-mortem on 2026-05-08 ([DENIC analysis blog (German), 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/) · [heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html)).

Confirmed root cause: a code defect in DENIC's third-generation custom signing infrastructure (deployed April 2026 atop Knot DNS). During a routine Zone-Signing-Key rotation the code generated **three private key pairs all assigned the same Key Tag (33834)** rather than a unique tag per key — and only one corresponding public DNSKEY record was published to the zone. The RRSIG records signed by the two unpublished keys were therefore unvalidatable; DNSSEC-validating resolvers marked all .de delegations as "Bogus", which through the bogus NSEC3 trust path also took down resolution for non-DNSSEC-signed .de domains.

The outage ran 2026-05-05 21:43 UTC → 2026-05-06 ~01:15 UTC (~3.5 h). Critically, DENIC notes the monitoring pipeline detected anomalous resolver behaviour but **the alerting layer did not correctly forward the alerts** — the SIEM-rule equivalent of a fire-but-don't-page failure. Knot DNS itself is not implicated; the bug was in DENIC's automation layer atop Knot.

Defender takeaway: DNSSEC registry-side errors are indistinguishable from attacker-induced trust failures from a resolver's perspective. Validating-resolver operators in DACH and EU public-sector environments should keep RFC 7646 Negative Trust Anchor capability live for continuity during registry incidents and ensure runbooks separate "registry KSK/ZSK rollover defect" from "zone-level attack on a downstream domain".
