---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: DENIC .de DNSSEC outage — 3.5 h registry-side trust failure traced to keytag 33834 collision and an alerting-layer fire-without-page
headline: DENIC .de DNSSEC outage — 3.5 h registry-side trust failure traced to keytag 33834 collision and an alerting-layer fire-without-page
summary: "On 2026-05-05 starting approximately 19:30 UTC (per Cloudflare's recorded incident-start timestamp), DENIC (the .de registry) began distributing invalid DNSSEC signatures for the .de TLD, making .de TLD resolution fail across DNSSEC-validating resolvers for roughly 3.5 hours; Cloudflare's write-up describes potential …"
discovered_at: "2026-05-04T05:00:23Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - dos
  - eu-nexus
regions:
  - europe
  - dach
sectors:
  - public-sector
  - technology
entities:
  - "incident:denic-dnssec-outage-2026"
cves: []
sources:
  - url: "https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/"
    publisher: DENIC analysis blog (German)
    role: primary
  - url: "https://blog.denic.de/en/technical-issue-with-de-domains-resolved/"
    publisher: DENIC post-incident report (English)
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
migrated_from: briefs/weekly/2026-W19.md
---

On 2026-05-05 starting approximately 19:30 UTC (per Cloudflare's recorded incident-start timestamp), DENIC (the .de registry) began distributing invalid DNSSEC signatures for the .de TLD, making .de TLD resolution fail across DNSSEC-validating resolvers for roughly 3.5 hours; Cloudflare's write-up describes potential impact on "millions of domains" without quantifying the count. The 2026-05-08 post-mortem confirmed the root cause: a code defect in DENIC's third-generation custom signing infrastructure (deployed April 2026 atop Knot DNS) generated **three private key pairs all assigned the same Key Tag (33834)** during a routine Zone-Signing-Key rotation, while only one corresponding public DNSKEY record was published to the zone. RRSIG records signed by the two unpublished keys were therefore unvalidatable; resolvers marked all .de delegations as "Bogus", and the bogus NSEC3 trust path also took down resolution for non-DNSSEC-signed .de domains. Cloudflare deployed an RFC 7646 Negative Trust Anchor for its resolvers at 22:17 UTC — a roughly 2-hour-47-minute mitigation gap from the recorded incident start. Critically, DENIC notes the monitoring pipeline detected anomalous resolver behaviour but **the alerting layer did not correctly forward the alerts** — a fire-without-page failure. Knot DNS itself is not implicated; the bug was in DENIC's automation layer ([DENIC analysis blog, 2026-05-08](https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/) · [Cloudflare blog](https://blog.cloudflare.com/de-tld-outage-dnssec/) · [heise online, 2026-05-08](https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html) · [daily 2026-05-09](/briefs/2026-05-09/) · [daily 2026-05-10 post-mortem UPDATE](/briefs/2026-05-10/)). **Defender takeaway:** DNSSEC registry-side errors are indistinguishable from attacker-induced trust failures from a resolver's perspective. Validating-resolver operators in DACH and EU public-sector environments should keep RFC 7646 Negative Trust Anchor capability live for continuity during registry incidents and ensure runbooks separate "registry KSK/ZSK rollover defect" from "zone-level attack on a downstream domain". The cross-finding for incident-response leaders is more general: alerting-pipeline reliability is itself a critical-infrastructure component, and a monitored anomaly that doesn't page is functionally an unmonitored anomaly.
