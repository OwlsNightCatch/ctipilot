---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "Public administration & identity (CH / DACH lead) — the LMS, SSO and e-government estate under multi-product pressure"
headline: "Public administration & identity (CH / DACH lead) — the LMS, SSO and e-government estate under multi-product pressure"
summary: "The week put the public-sector identity and web estate under pressure from several directions at once, with a direct Swiss nexus. ILIAS LMS — the open-source learning platform deployed across German and Swiss public-sector and university estates — shipped nine fixes on 2026-05-27 including two critical …"
discovered_at: "2026-05-25T05:00:11Z"
event_date: 2026-05-29
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - auth-bypass
  - pre-auth
regions:
  - switzerland
  - dach
  - europe
sectors:
  - public-sector
  - education
entities:
  - "trend:ilias-lms-nine-fixes-2026-05-27-tileimageupload-unauth-write-soap-access-bypass"
cves: []
sources:
  - url: "https://docu.ilias.de/go/blog/15821"
    publisher: ILIAS Security Blog
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12599"
    publisher: NCSC.ch Security Hub post 12599
    role: corroborating
  - url: "https://apereo.github.io/2026/05/27/oidc-vuln/"
    publisher: Apereo CAS — OIDC disclosure
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
migrated_from: briefs/weekly/2026-W22.md
---

The week put the public-sector identity and web estate under pressure from several directions at once, with a direct Swiss nexus. **ILIAS LMS** — the open-source learning platform deployed across German and Swiss public-sector and university estates — shipped nine fixes on 2026-05-27 including two critical access-control gaps (CVSS 9.8 and 9.3), with **NCSC.ch flagging the SOAP interface as the primary unauthenticated attack surface** ([2026-05-28](/briefs/2026-05-28/)). In parallel, **Apereo CAS** patched an OIDC-provider flaw that was **reported by Coop Switzerland**, with CERT-FR issuing CERTFR-2026-AVI-0654 ([2026-05-29](/briefs/2026-05-29/)) — relevant to any CH/EU entity running CAS as an OpenID Connect IdP. Further afield in the same estate class, **Lithuania's Centre of Registers** lost ~600,000 state-register records to abused institutional credentials with a foreign state suspected ([2026-05-27](/briefs/2026-05-27/)), and Poland's **Szafir SDK** signature-verification bypass (CVE-2026-9058) struck e-government signing ([2026-05-26](/briefs/2026-05-26/)). The cross-cutting takeaway: the contested surface for public administration this week was the *identity and document/learning-platform middleware* (SOAP endpoints, OIDC providers, signature SDKs), not the citizen-facing front ends.
