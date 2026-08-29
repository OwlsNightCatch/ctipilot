---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-18885 / CVE-2026-18886 / CVE-2026-74820 / CVE-2026-6876 — ServiceNow AI Platform: three unauthenticated CVSS 10.0 flaws plus a related Now Platform sandbox escape"
headline: "ServiceNow patches four unauthenticated flaws in its AI Platform and Now Platform, three of them maximum severity"
summary: >
  ServiceNow's 27 August 2026 advisory (KB3152242) fixes four flaws: three unauthenticated, CVSS4.0 10.0 issues in
  the AI Platform (two code-injection flaws and one SQL injection, per ServiceNow's own classification) plus a
  related CVSS 8.7 sandbox escape in the Now Platform. Hosted instances are already patched; self-hosted and
  partner-hosted customers must apply the fix themselves. No exploitation is reported for any of the four, and no
  public proof-of-concept is reported for the three maximum-severity flaws.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-29T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, sqli, patch-available]
regions: [global]
sectors: [public-sector, finance, healthcare, telco, energy]
entities: []
techniques: [T1190]
affected_products: ["ServiceNow AI Platform", "ServiceNow Now Platform"]
cves:
  - id: CVE-2026-18885
    cvss: "10.0 (CVSS4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ServiceNow AI Platform — Xanadu, Yokohama, Zurich and Australia release lines below the fixed patch/hotfix per ServiceNow's version table"
    fixed: "Xanadu Patch 11 Hotfix 7a; Yokohama Patch 12 Hotfix 3b / Patch 13 Hotfix 4; Zurich Patch 7b Hotfix 3 through Patch 12; Australia Patch 2 Hotfix 3 through Patch 5 — hosted instances already updated, self-hosted/partner-hosted customers apply per the version matrix"
  - id: CVE-2026-18886
    cvss: "10.0 (CVSS4.0)"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ServiceNow AI Platform — same release lines and fixed builds as CVE-2026-18885, except Australia Patch 5's status is recorded as unknown rather than affected"
    fixed: "Same fixed-build matrix as CVE-2026-18885 — hosted instances already updated, self-hosted/partner-hosted customers apply per the version matrix"
  - id: CVE-2026-74820
    cvss: "10.0 (CVSS4.0)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ServiceNow AI Platform — same release lines and fixed builds as CVE-2026-18885"
    fixed: "Same fixed-build matrix as CVE-2026-18885 — hosted instances already updated, self-hosted/partner-hosted customers apply per the version matrix"
  - id: CVE-2026-6876
    cvss: "8.7 (CVSS4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ServiceNow Now Platform — same release lines and fixed builds as CVE-2026-18885"
    fixed: "Same fixed-build matrix as CVE-2026-18885 — hosted instances already updated, self-hosted/partner-hosted customers apply per the version matrix"
sources:
  - url: "https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3152242"
    publisher: "ServiceNow (vendor security advisory KB3152242)"
    date: "2026-08-27"
    role: primary
  - url: "https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html"
    publisher: "The Hacker News"
    date: "2026-08-28"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3060"
    publisher: "BSI CERT-Bund advisory WID-SEC-2026-3060"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "ServiceNow has remediated a code injection vulnerability that was identified in the ServiceNow AI platform. This vulnerability could enable an unauthenticated user, in certain circumstances, to execute arbitrary code in the ServiceNow platform and gain access to, or modify, instance data beyond what was intended."
    publisher: "ServiceNow"
  - quote: "ServiceNow has remediated a SQL injection vulnerability that was identified in the ServiceNow AI platform. This vulnerability could enable an unauthenticated user, in certain circumstances, to execute arbitrary SQL statements against the instance's underlying database"
    publisher: "ServiceNow"
  - quote: "A code injection vulnerability in the GraphQL Composite Data API that could enable an unauthenticated user to execute arbitrary code and gain access to, or modify, instance data"
    publisher: "The Hacker News"
  - quote: "An improper access control vulnerability in the system configuration image upload processor that could enable an unauthenticated user to create or modify instance data, resulting in privilege escalation"
    publisher: "The Hacker News"
  - quote: "None of the four flaws appeared in the catalog as of August 28, 2026, leaving ServiceNow's ratings as the only severity assessment on record."
    publisher: "The Hacker News"
  - quote: "The company said it deployed a security update to hosted instances and provided the update to its partners and self-hosted customers, which leaves organizations that run their own instances to apply the fixes themselves."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: >
  ServiceNow's own advisory text (KB3152242) gives only qualitative risk labels ("critical" / "high") and classifies
  CVE-2026-18885, CVE-2026-18886 and CVE-2026-74820 identically as affecting "the ServiceNow AI platform" (code
  injection / code injection / SQL injection respectively); it does not publish a numeric CVSS score, a CVSS vector,
  a per-CVE technical mechanism, or the "hosted"/"partner-hosted" affected-population framing used in this entry's
  body, for any of the four. The numeric CVSS4.0 scores and vectors, the more specific per-CVE mechanisms (GraphQL
  Composite Data API for CVE-2026-18885, an image-upload-processor access-control bypass for CVE-2026-18886, a
  dynamic-schema ORDER BY clause for CVE-2026-74820, the PR:L vector and CVE-2026-6875 link for CVE-2026-6876), and
  the hosted/partner-hosted framing all trace to The Hacker News's reporting on the same advisory, including a
  ServiceNow spokesperson statement it quotes directly. The Hacker News's own CVE-2026-18886 description ("improper
  access control", "privilege escalation") differs from ServiceNow's "code injection" classification for the same
  id; both readings are carried in the body, attributed to their respective source, with ServiceNow's own
  classification treated as authoritative for `cves[].type`/`affected`. These CVSS4.0 vectors and per-CVE mechanism
  names were independently cross-checked against each CVE's own CNA record in the CVE Program's structured data (the
  CNA submission is ServiceNow's own, filed separately from both KB3152242 and its press engagement) and found to
  match The Hacker News's reporting exactly; that record cannot be cited directly per this pipeline's sourcing rules
  (derived per-CVE data-sheet pages are blocked), but the cross-check materially raises confidence that The Hacker
  News's technical specifics are accurate restatements of ServiceNow's own data rather than aggregator error. Because
  the entry's most load-bearing technical content nonetheless has no citable primary trace independent of The Hacker
  News (rated reliability C — aggregator, not an original-reporting outlet, per `sources/sources.json`), reliability
  is held at B rather than A: ServiceNow's own advisory is fully primary but qualitative-only, and the quantitative
  specifics rest on a corroborated-but-uncitable aggregator restatement. ServiceNow is its own CVE Numbering
  Authority, and NIST enriches only vulnerabilities that appear in CISA's KEV catalogue, affect federal government
  software, or are designated critical under Executive Order 14028 — none of these four currently qualify, so
  ServiceNow's self-assigned severity ratings are the only assessment on record.
confidence: high
references: [2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

ServiceNow's 27 August 2026 advisory (KB3152242) discloses four flaws, found through the vendor's own security
research and responsible-disclosure program rather than external report
([ServiceNow, 2026-08-27](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3152242)). Three —
CVE-2026-18885, CVE-2026-18886 and CVE-2026-74820 — are unauthenticated flaws in the ServiceNow AI Platform that
ServiceNow's own text classifies as critical: CVE-2026-18885 as code injection letting an unauthenticated user
execute arbitrary code and gain access to, or modify, instance data; CVE-2026-74820 as SQL injection letting an
unauthenticated user execute arbitrary SQL against the instance's own database; CVE-2026-18886 also as code
injection, but described as letting an unauthenticated user create or modify instance data, resulting in privilege
escalation
([ServiceNow, 2026-08-27](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3152242)). The
Hacker News reports the same three at a numeric CVSS4.0 score of 10.0 — ServiceNow's own advisory gives only the
qualitative "critical" label, never a numeric score
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)). The
Hacker News, reporting on the same advisory, assigns each a more specific mechanism: CVE-2026-18885 as a code
injection in the GraphQL Composite Data API, CVE-2026-74820 as a SQL injection reached through a dynamic-schema
`ORDER BY` clause, and CVE-2026-18886 as an improper-access-control flaw in the system-configuration image-upload
processor enabling privilege escalation — a classification that differs from ServiceNow's own "code injection"
description of the same id
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)). All
three share the identical CVSS4.0 vector `AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H` per The Hacker
News's reporting — network-reachable, low attack complexity, no privileges, no user interaction, high impact to the
vulnerable component and connected systems
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)). A
fourth, related flaw, CVE-2026-6876, is a sandbox escape ServiceNow's own text describes as letting an
unauthenticated user execute arbitrary code within the Now Platform
([ServiceNow, 2026-08-27](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3152242)). The
Hacker News reports the CVSS4.0 vector ServiceNow assigned to it in fact specifies `PR:L` (low privileges required)
rather than none — an inconsistency with ServiceNow's own "unauthenticated user" prose — scores it 8.7, and connects
it to CVE-2026-6875, a pre-auth ServiceNow sandbox escape Searchlight Cyber reported to ServiceNow on 1 April 2026,
with the vendor's own advisory for it published on 13 July 2026
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)).

ServiceNow deployed the update to hosted instances directly and provided it to partner and self-hosted customers,
who must apply it themselves; those customers should verify their instance version against the vendor's fixed-build
table — spanning the Xanadu, Yokohama, Zurich and Australia release lines, each with its own minimum hotfix
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)). ServiceNow
reports no awareness of exploitation for any of the four flaws, and The Hacker News found no public proof-of-concept
for the three maximum-severity flaws as of 28 August 2026
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)).
Because ServiceNow is its own CVE Numbering Authority and none of the four flaws meet NIST's current
post-April-2026 enrichment criteria (CISA KEV listing, federal-software impact, or an Executive Order 14028 critical
designation), ServiceNow's own severity ratings are the only assessment on record for any of them
([The Hacker News, 2026-08-28](https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html)) — a
vulnerability-management process that ranks purely on NVD-enriched severity will not see the urgency here.

Detection concept: ServiceNow instance and application audit logs, and GraphQL API access logs, for anomalous or
malformed API mutations originating from unauthenticated sessions; database-audit telemetry for dynamic-schema
queries carrying non-schema tokens; system-configuration change-audit records for writes not tied to an
authenticated administrative session. No public exploit code exists yet, so this is patch-priority guidance rather
than an active-exploitation hunt. **Defender takeaway:** ServiceNow is a common ITSM/ITOM platform in public-sector
and critical-infrastructure back-office environments; self-hosted and partner-hosted instances should confirm their
build against ServiceNow's fixed-version table now, since hosted-instance auto-patching does not cover them.
