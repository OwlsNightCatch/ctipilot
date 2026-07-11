---
schema: 1
kind: threat
horizon: operational
title: "DENIC .de DNSSEC outage — faulty key rollover; 3.5 h disruption for German government and public-sector .de domains"
headline: "DENIC .de DNSSEC outage — faulty key rollover; 3.5 h disruption for German government and public-sector .de domains"
summary: "On 2026-05-05 at 21:43 UTC, DENIC (the .de domain registry) began distributing invalid DNSSEC signatures for the .de TLD, making approximately 18 million .de domains unreachable for DNSSEC-validating resolvers for roughly 3.5 hours (DENIC blog post-incident report, 2026-05-08 · DENIC initial report, 2026-05-05)."
discovered_at: "2026-05-09T05:00:02Z"
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
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-09.md
---

On 2026-05-05 at 21:43 UTC, DENIC (the .de domain registry) began distributing invalid DNSSEC signatures for the .de TLD, making approximately 18 million .de domains unreachable for DNSSEC-validating resolvers for roughly 3.5 hours ([DENIC blog post-incident report, 2026-05-08](https://blog.denic.de/en/technical-issue-with-de-domains-resolved/) · [DENIC initial report, 2026-05-05](https://blog.denic.de/en/denic-reports-dnssec-disruption-affecting-de-domains/)). Root cause: a software defect in DENIC's HSM integration code introduced during a March 2026 migration to Knot DNS generated three key pairs sharing keytag 33834, but only one public key was published in the zone; inconsistent signing across name servers followed. Cloudflare deployed a Negative Trust Anchor under RFC 7646 for its resolvers within ~90 minutes; DENIC restored service by 01:15 UTC on 2026-05-06. Crucially, .ch was unaffected ([heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html) · [Cloudflare blog](https://blog.cloudflare.com/de-tld-outage-dnssec/)). This is an operational misconfiguration, not an attacker action.

**Defender takeaway:** DNSSEC registry-side errors are indistinguishable from attacker-induced validation failures from the resolver's perspective. Defenders should maintain RFC 7646 Negative Trust Anchor capability in their validating resolvers for continuity during registry incidents. German public-sector operators relying on .de-hosted services (government portals, MX records, API endpoints) should review their incident runbooks for DNSSEC-induced availability events to separate "registry outage" from "zone-level attack."
