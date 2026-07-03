---
schema: 1
kind: research
horizon: operational
title: "\"Underminr\": a multi-tenant-CDN domain-fronting variant that blinds DNS-layer filtering"
headline: "\"Underminr\": a multi-tenant-CDN domain-fronting variant that blinds DNS-layer filtering"
summary: "\"Underminr\" is a new domain-fronting variant that defeats DNS-layer filtering on multi-tenant CDNs — ADAMnetworks showed an attacker can present an allow-listed domain's SNI/Host while the shared CDN edge routes the request to a different tenant's (attacker) origin on the same IP, blinding DNS filtering and edge-terminated TLS inspection. No CVE (architectural); ~88M domains on shared infrastructure are potentially in scope (SecurityWeek, 2026-05-23)."
discovered_at: "2026-05-25T05:00:02Z"
event_date: 2026-05-23
run_id: 2026-05-25-d675ef38
priority: high
immediate_action: null
tags:
  - cloud
regions:
  - global
sectors:
  - public-sector
  - technology
  - telco
entities: []
cves: []
sources:
  - url: "https://support.adamnet.works/t/underminr-information-share-official-release/1584"
    publisher: "ADAMnetworks, 2026-05-21"
    role: primary
  - url: "https://www.securityweek.com/underminr-vulnerability-lets-attackers-hide-malicious-connections-behind-trusted-domains/"
    publisher: "SecurityWeek, 2026-05-23"
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
migrated_from: briefs/2026-05-25.md
---

ADAMnetworks disclosed **Underminr**, a structural evolution of domain fronting that abuses the shared-IP, multi-tenant architecture of modern CDN edges rather than a single-CDN misconfiguration ([ADAMnetworks, 2026-05-21](https://support.adamnet.works/t/underminr-information-share-official-release/1584)). Classic domain fronting — overriding the HTTP `Host` header behind a permitted SNI — was largely closed by the major CDNs in 2021–2022 by enforcing SNI/Host consistency. Underminr instead presents the SNI and HTTP `Host` of a legitimate, allow-listed domain hosted on a shared edge while forcing the request to the IP of a *different* tenant — the attacker's origin — on the same edge, exploiting the fact that the CDN's internal tenant routing is decoupled from the network-visible `Host`/SNI ([SecurityWeek, 2026-05-23](https://www.securityweek.com/underminr-vulnerability-lets-attackers-hide-malicious-connections-behind-trusted-domains/)). As SecurityWeek frames it, "the detection gap appears when DNS decisions, edge IPs, SNI, Host headers, and CDN tenant routing are not correlated." No CVE was assigned — this is an architectural property of shared-edge multi-tenancy, not a software bug. SecurityWeek reports roughly 88 million domains on shared infrastructure are potentially in scope, with US, UK and Canadian infrastructure most affected; the technique does not require compromising the legitimate domain, only co-tenancy on the same edge IP range.

**Why it matters to us:** this maps to ATT&CK [`T1090.004`](https://attack.mitre.org/techniques/T1090/004/) (Proxy: Domain Fronting) and is squarely a C2 / exfiltration-evasion concern for the many CH/EU public-sector networks whose egress control leans on DNS-layer filtering (DNS RPZ, recursive-resolver allow-lists) or that treat a CDN's published IP range as a proxy for the actual destination — both of which Underminr defeats, because the FQDN legitimately resolves to the shared edge IP and edge-terminated TLS inspection never sees the origin-routing decision. Defenders should stop treating DNS/domain allow-listing as a sufficient egress control on its own; correlate SNI, `Host`, the resolved edge IP and (where available) CDN tenant identity per flow, and prefer per-flow identity verification (ZTNA) over perimeter-DNS-filter trust. Specific vulnerable CDN providers are not named in the public reporting.
