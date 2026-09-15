---
schema: 1
kind: threat
title: "ILIAS LMS — nine fixes shipped 2026-05-27, two critical access-control gaps (CVSS 9.8 + 9.3), NCSC.ch flags SOAP interface as primary unauthenticated attack surface"
headline: "ILIAS LMS — nine fixes shipped 2026-05-27, two critical access-control gaps (CVSS 9.8 + 9.3), NCSC.ch flags SOAP interface as primary unauthenticated attack"
summary: "ILIAS LMS — critical patch cluster: unauthenticated TileImageUploadHandler write (CVSS 9.8) plus SOAP access-bypass and multiple SQL-injection bugs. The open-source LMS dominant in Swiss federal training, Swiss/German universities, and DACH public-sector vocational portals shipped nine fixes on 2026-05-27 across the 9.20 / 10.8 / 11.1 branches; NCSC Switzerland published an advisory the same day flagging the SOAP interface as the primary unauthenticated attack surface (ILIAS Security Blog, 2026-05-27; NCSC-CH, 2026-05-27; BSI CERT-Bund WID-SEC-2026-1689, 2026-05-27). Per-bug CVSS not in NVD yet — vendor and BSI advisories are primary."
discovered_at: "2026-05-28T05:00:00Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - rce
  - auth-bypass
  - sqli
regions:
  - switzerland
  - dach
  - europe
sectors:
  - education
  - public-sector
entities:
  - "trend:ilias-lms-nine-fixes-2026-05-27-tileimageupload-unauth-write-soap-access-bypass"
cves: []
sources:
  - url: "https://docu.ilias.de/go/blog/15821"
    publisher: ILIAS Security Blog
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12599"
    publisher: NCSC Switzerland post 12599
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1689"
    publisher: BSI CERT-Bund WID-SEC-2026-1689
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
migrated_from: briefs/2026-05-28.md
---

The ILIAS Security Group released a coordinated nine-issue security update on 2026-05-27 covering the open-source Learning Management System that dominates the CH/DE/AT public-sector e-learning estate: Swiss federal training portals, NATO DEEP ADL, and the majority of Swiss and German university LMS deployments ([ILIAS Security Blog, 2026-05-27](https://docu.ilias.de/go/blog/15821); [NCSC-CH, 2026-05-27](https://security-hub.ncsc.admin.ch/#/posts/12599); [BSI CERT-Bund WID-SEC-2026-1689, 2026-05-27](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1689)). CVE identifiers were not assigned in the BSI CSAF document; the vendor uses internal MantisBT IDs.

Two issues are rated critical by the vendor. MantisBT 0047787 (CVSS 4.0: 9.8) is a missing access-control check in `TileImageUploadHandler`; an attacker with network access to the upload endpoint can write arbitrary files, bypassing authentication entirely — the textbook prerequisite for arbitrary file write to RCE on a PHP application. MantisBT 0047691 (CVSS 4.0: 9.3) is a post-auth SQL injection in the MyStaff module. Companion high-severity findings: MantisBT 0047581 (CVSS 8.7) — broken access-control in the SOAP interface permitting unauthenticated SOAP calls; MantisBT 0047472 (CVSS 7.1) — SQL injection reachable via the SOAP API; MantisBT 0047770 (CVSS 8.5) and 0047778 (CVSS 8.1) — sort-field and SCORM2004-module SQLi paths; MantisBT 0047258 — unauthorized SOAP function calls.

**Why it matters to us:** ILIAS is mission-critical for Swiss federal civil-servant training and Swiss/DACH academic certification — a compromise of the LMS exposes course content, learner PII, certification records, and any HR/IDP integration on the SOAP interface. NCSC.ch's recommended interim mitigation is to disable the SOAP interface on any deployment that does not require it for enterprise HR / SIS integration. Patched branches: 9.20, 10.8, 11.1. Detection concepts: monitor web-server access logs for POSTs to `TileImageUploadHandler` without a valid session cookie; flag any request to `/ilias.php?baseClass=ilSOAPExplorer` or the SOAP WSDL endpoint from non-internal source IPs. Hardening: AppArmor/SELinux profile constraining `php-fpm` writeable paths to content directories; reverse-proxy ACL blocking external access to `/webservice/soap/` until patched.
