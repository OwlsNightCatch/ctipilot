---
schema: 1
kind: vulnerability
title: "CVE-2026-48449 — Adobe Campaign Classic: an authorization flaw gives unauthenticated arbitrary code execution (CVSS 10.0), on-premise and hybrid deployments only"
headline: "Adobe ships a priority-1 fix for a CVSS 10.0 unauthenticated code-execution flaw in Campaign Classic — only self-hosted and hybrid installs need action"
summary: >
  Adobe published APSB26-114 on 2026-07-29 for two critical flaws in Adobe Campaign Classic, the
  campaign-management and customer-data platform, fixed in ACC v7 build 9398. CVE-2026-48449
  (CVSS 3.1 10.0, CWE-863 Incorrect Authorization) allows arbitrary code execution with no
  authentication, no user interaction and a changed scope; CVE-2026-48448 (CVSS 8.6, CWE-89) is an
  unauthenticated SQL injection giving arbitrary file-system read. Adobe assigns the update its
  highest priority rating and states it is not aware of exploitation. The bulletin applies only to
  fully on-premise deployments and to the on-premise components of hybrid deployments — Adobe-hosted
  instances were already remediated and need no customer action, which makes this an exposure
  question about who runs their own ACC rather than a platform-wide event.
discovered_at: "2026-08-02T13:50:00Z"
event_date: "2026-07-29"
run_id: 2026-08-02T1309Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, sqli, auth-bypass, info-disclosure, patch-available]
regions: [global, europe]
sectors: [public-sector, retail, finance, media]
entities: []
techniques: [T1190]
affected_products: ["Adobe Campaign Classic"]
cves:
  - id: CVE-2026-48449
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Read from the affected-versions table of Adobe's own bulletin: Adobe Campaign Classic ACC v7 7.4.3 build 9397 and earlier, on Windows and Linux. The bulletin scopes itself to fully on-premise deployments and the on-premise components of hybrid deployments."
    fixed: "Per the solution table of APSB26-114: ACC v7 7.4.3 build 9398, priority rating 1. Adobe-hosted (cloud) instances were already remediated by Adobe and require no customer action."
  - id: CVE-2026-48448
    cvss: "8.6"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic ACC v7 7.4.3 build 9397 and earlier, Windows and Linux, on-premise and hybrid on-premise components — per the same affected-versions table."
    fixed: "ACC v7 7.4.3 build 9398."
sources:
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-114.html"
    publisher: "Adobe"
    date: "2026-07-29"
    role: primary
closed_sources: []
evidence:
  - quote: "This security bulletin applies only to fully on-premise deployments of Adobe Campaign Classic and to the on-premise components of hybrid deployments"
    publisher: "Adobe"
  - quote: "Adobe is not aware of any exploits in the wild for any of the issues addressed in these updates."
    publisher: "Adobe"
verification: single-source
sourcing_note: "Single-source: Adobe's own PSIRT bulletin is the per-CVE authority for both identifiers, both CVSS base scores, both vectors and the affected/fixed build numbers, all read from the bulletin's structured tables rather than its prose. National-CERT restatements of the same bulletin circulated but carry no independent assessment, so they raise the publisher count without raising corroboration — credibility stays 2. Reliability A: a vendor PSIRT reporting on its own product."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Establish whether your Adobe Campaign Classic is Adobe-hosted or self-hosted before scheduling anything — Adobe states hosted instances are already remediated, so the work is confined to fully on-premise deployments and the on-premise components of hybrid ones; upgrade those to ACC v7 7.4.3 build 9398."
migrated_from: null
---

This is a recovery published by the 2026-08-02 weekly quality audit: the bulletin landed inside the audit window and no entry covered it.

The number that decides the timeline here is not the 10.0 but the vector. Adobe's own table gives CVE-2026-48449 as `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` — network reachable, low complexity, **no privileges required**, no user interaction, scope changed — against an Incorrect Authorization weakness (CWE-863) whose impact Adobe records as arbitrary code execution ([Adobe, 2026-07-29](https://helpx.adobe.com/security/products/campaign/apsb26-114.html)). An authorization flaw reached without credentials on an internet-facing application is the shape that does not wait for the quarterly window, and Adobe agrees to the extent its own scale allows: it assigns priority rating 1, its most urgent. The sibling CVE-2026-48448 is a SQL injection at CVSS 8.6 with the same `PR:N/UI:N` prefix, impact recorded as arbitrary file-system read.

The scoping note is the part most likely to be misread in an estate inventory. Adobe states that "This security bulletin applies only to fully on-premise deployments of Adobe Campaign Classic and to the on-premise components of hybrid deployments" — Adobe-hosted instances were remediated by Adobe and need no customer action. A hybrid deployment is the trap: the hosted half is already fixed while the on-premise half is not, so an organisation whose asset register records Campaign as a SaaS product will conclude wrongly that it has nothing to do. Adobe also states it "is not aware of any exploits in the wild for any of the issues addressed in these updates", which is the correct hedge to carry — this entry is about mechanics and exposure, not about observed attacks.

What makes Campaign Classic worth the attention beyond the score is what it holds and what it touches. It is a campaign-execution platform: marketing and citizen-communication databases, subscriber lists, personal contact data, and an outbound sending capability tied to the organisation's own domain. Code execution on that host is simultaneously a personal-data exposure and a trusted-sender takeover, and public-sector bodies using it for citizen notifications inherit both.

**Defender takeaway:** the first task is inventory rather than patching — determine which Campaign Classic instances are on-premise or hybrid-on-premise, because that is the whole of the affected population and it is a question only the organisation can answer. For those, upgrade to build 9398. Until the upgrade lands, the only structural control available is reachability: an unauthenticated authorization flaw is exploitable by anyone who can reach the application, so restricting the ACC web tier to known administrative and integration networks removes the precondition even though Adobe offers no workaround for the flaw itself.

**Triage:** there is no published exploitation and no proof-of-concept, so there is no attack pattern to match yet. What can be checked now is retrospective and cheap: on an ACC host that was internet-reachable while below build 9398, review the application and web-server logs for requests reaching authenticated functionality without a preceding successful authentication event, and for process creation under the ACC service account with a web-server parent — those are the generic manifestations an authorization bypass reaching code execution would produce, and their absence over the exposure window is a meaningful negative on a host with no other exposure.
