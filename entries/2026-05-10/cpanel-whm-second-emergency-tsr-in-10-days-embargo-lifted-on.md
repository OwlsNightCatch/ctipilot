---
schema: 1
kind: vulnerability
horizon: operational
title: "cPanel/WHM second emergency TSR in 10 days — embargo lifted on CVE-2026-29202 (post-auth Perl RCE, CVSS 8.8), CVE-2026-29203 (CVSS 8.8), CVE-2026-29201 (CVSS 4.3)"
headline: "cPanel/WHM second emergency TSR in 10 days — embargo lifted on CVE-2026-29202 (post-auth Perl RCE, CVSS 8.8), CVE-2026-29203 (CVSS 8.8), CVE-2026-29201 (CVSS"
summary: "cPanel embargo lifted on second emergency TSR in 10 days — CVE-2026-29202 (CVSS 8.8) is post-auth Perl execution in the create_user API; CVE-2026-29203 (CVSS 8.8) is unsafe symlink chmod abuse; CVE-2026-29201 (CVSS 4.3) is arbitrary feature-file read. No confirmed ITW yet, but the prior CVE-2026-41940 wave compromised ~44 000 hosts across two months, so a freshly recovered fleet now faces fresh CVEs before remediation completes."
discovered_at: "2026-05-10T05:00:10Z"
event_date: 2026-05-09
run_id: 2026-05-10-001
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - patch-available
regions:
  - global
sectors:
  - technology
entities: []
cves:
  - id: CVE-2026-29202
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-29203
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-29201
    cvss: "4.3"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html"
    publisher: "The Hacker News, 2026-05-09"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/api/posts/12550/details"
    publisher: "NCSC-CH Security Hub post 12550, 2026-05-08"
    role: corroborating
  - url: "https://panelica.com/blog/cpanel-cve-2026-29201-29202-29203-may-2026-tsr-advisory"
    publisher: "Panelica technical analysis, 2026-05-08"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
---

**UPDATE (originally noted as embargoed-and-dropped 2026-05-09):** Technical details for the three CVEs cPanel patched on 2026-05-08 emerged on 2026-05-09 ([The Hacker News, 2026-05-09](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html) · [NCSC-CH Security Hub post 12550, 2026-05-08](https://security-hub.ncsc.admin.ch/api/posts/12550/details) · [Panelica technical analysis, 2026-05-08](https://panelica.com/blog/cpanel-cve-2026-29201-29202-29203-may-2026-tsr-advisory)).

**CVE-2026-29202** (CVSS 8.8) is the highest-severity item: insufficient input validation of the `plugin` parameter in the `create_user` API allows an authenticated cPanel user to inject and execute arbitrary Perl code in the context of their system account — *post-authentication RCE for any cPanel user with API access*. **CVE-2026-29203** (CVSS 8.8) is unsafe symlink handling enabling `chmod` abuse on arbitrary files (privilege escalation or denial-of-service). **CVE-2026-29201** (CVSS 4.3) is arbitrary feature-file disclosure. None have confirmed in-the-wild exploitation as of 2026-05-09.

The compounding risk: cPanel hosts that were compromised through the still-recent **CVE-2026-41940** authentication-bypass wave (~44 000 hosting servers exploited over February–May 2026) now face a fresh post-auth Perl-execution primitive. An attacker who already used the auth bypass can pivot to CVE-2026-29202 to escalate privilege or persist. Fixed: cPanel/WHM **11.136.0.9+**, **11.134.0.25+**, **11.132.0.31+**. Operators with auto-update disabled or version-pinned builds must run `/scripts/upcp` manually.
