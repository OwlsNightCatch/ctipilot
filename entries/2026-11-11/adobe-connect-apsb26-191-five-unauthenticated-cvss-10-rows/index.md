---
schema: 1
kind: vulnerability
title: "Adobe Connect (Windows) APSB26-191: five unauthenticated flaws rated CVSS 10.0 and two more unauthenticated rows among 24 fixes in 12.12 and earlier; Adobe knows of no exploitation"
headline: "Adobe Connect on Windows: five unauthenticated CVSS 10.0 flaws fixed in 12.12.a and earlier; no known exploitation"
summary: >
  Adobe's priority 2 bulletin APSB26-191 of 2026-11-10 fixes 24 CVEs in Adobe Connect on Windows 12.12 and earlier, five of them scored CVSS 3.1 10.0 with no privileges and no user interaction (SSRF, path traversal, incorrect authorization and CRLF injection) and two more unauthenticated rows at 9.4 (SQL injection) and 9.1. The fixed builds are 12.12.a, 12.11.i, 12.10.f, 12.9.a and 12.8.a; Adobe is not aware of exploitation and the bulletin gives no root-cause detail.
discovered_at: "2026-11-11T03:38:00Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, auth-bypass, path-traversal, sqli, patch-available]
regions: [global]
sectors: []
entities: ["product:adobe-connect"]
techniques: [T1190]
affected_products: ["Adobe Connect"]
cves:
  - id: CVE-2026-121356
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121889
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121351
    cvss: "10.0"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121352
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121353
    cvss: "10.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121902
    cvss: "9.4"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
  - id: CVE-2026-121355
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Connect on Windows 12.12 and earlier"
    fixed: "12.12.a, 12.11.i, 12.10.f, 12.9.a, 12.8.a"
sources:
  - url: "https://www.adobe.com/trust/security/products/connect/apsb26-191"
    publisher: "Adobe (security bulletin APSB26-191)"
    date: "2026-11-10"
    role: primary
closed_sources: []
evidence:
  - quote: "Adobe has released a priority 2 security update for Adobe Connect."
    publisher: "Adobe"
    source_url: "https://www.adobe.com/trust/security/products/connect/apsb26-191"
  - quote: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N"
    publisher: "Adobe"
    source_url: "https://www.adobe.com/trust/security/products/connect/apsb26-191"
verification: single-source
sourcing_note: >
  Adobe's bulletin is first-hand for its own product and carries the scores and fixed builds; no second source describes the flaws, and the bulletin gives no root-cause or exploitation detail beyond the vendor's statement that it knows of no exploits. Adobe's own wording for the five 10.0 rows is privilege escalation.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every Adobe Connect server on Windows to the fixed build of its train (12.12.a, 12.11.i, 12.10.f, 12.9.a or 12.8.a), those reachable from the internet first, because five flaws need no privileges and no user interaction and Adobe names no mitigation."
updates: []
migrated_from: null
---

Adobe's priority 2 bulletin APSB26-191, published on 2026-11-10, fixes 24 CVEs in Adobe Connect on Windows 12.12 and earlier ([Adobe, 2026-11-10](https://www.adobe.com/trust/security/products/connect/apsb26-191)). Five of them are scored CVSS 3.1 10.0 with the vector AV:N/AC:L/PR:N/UI:N/S:C, so an attacker needs no account and no user interaction: two server-side request forgeries (CVE-2026-121356, CVE-2026-121889), a path traversal (CVE-2026-121351), an incorrect-authorization flaw (CVE-2026-121352) and a CRLF injection (CVE-2026-121353); Adobe describes the impact of all five as privilege escalation ([Adobe, 2026-11-10](https://www.adobe.com/trust/security/products/connect/apsb26-191)). Two more rows need no privileges either: an SQL injection leading to code execution (CVE-2026-121902, 9.4) and an incorrect-authorization flaw (CVE-2026-121355, 9.1), and a further group of authenticated rows is fixed in the same release ([Adobe, 2026-11-10](https://www.adobe.com/trust/security/products/connect/apsb26-191)). The fixed builds are 12.12.a, 12.11.i, 12.10.f, 12.9.a and 12.8.a ([Adobe, 2026-11-10](https://www.adobe.com/trust/security/products/connect/apsb26-191)). The bulletin gives no root-cause detail, names no workaround, and Adobe says it is not aware of exploitation.

**Exposure:** Adobe Connect on Windows at 12.12 or earlier, the product the bulletin lists.

**Detection:** the bulletin supplies none, so the signal is behavior at the web tier: unauthenticated requests that return content from administrative or API paths, outbound connections from the Connect server to internal addresses that suggest request forgery, and unexpected files in web-served directories.

**Defender takeaway:** patch internet-facing Connect servers to the fixed build of their train now, because five flaws need neither credentials nor a user and the bulletin offers nothing but the update.
