---
schema: 1
kind: vulnerability
title: GLPI CERTFR-2026-AVI-0551 — Seven CVEs including SSRF and XSS in EU ITSM platform (advisory 2026-04-29)
headline: GLPI CERTFR-2026-AVI-0551 — Seven CVEs including SSRF and XSS in EU ITSM platform (advisory 2026-04-29)
summary: "France's CERT-FR published CERTFR-2026-AVI-0551 (April 29, 2026) covering seven CVEs in GLPI, the open-source IT Service Management platform widely deployed in European public-sector organisations and healthcare networks."
discovered_at: "2026-05-08T05:00:10Z"
event_date: null
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - patch-available
regions:
  - europe
sectors: []
entities: []
cves:
  - id: CVE-2026-32312
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-40108
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-42317
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-42318
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-42320
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-42321
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-5385
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0551/"
    publisher: CERT-FR — CERTFR-2026-AVI-0551
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-08.md
---

France's CERT-FR published CERTFR-2026-AVI-0551 (April 29, 2026) covering seven CVEs in GLPI, the open-source IT Service Management platform widely deployed in European public-sector organisations and healthcare networks. Vulnerability types include SSRF (CVE-2026-32312), stored and reflected XSS (CVE-2026-42317, CVE-2026-42318, CVE-2026-42320, CVE-2026-42321), security policy bypass (CVE-2026-5385), and data integrity compromise (CVE-2026-40108). CVSS scores are not published in the advisory. No exploitation in the wild is confirmed. GLPI administrators should upgrade to version ≥ 10.0.25 (10.0.x branch) or ≥ 11.0.7 (11.x branch). Swiss federal and cantonal administrations and hospitals using GLPI as their ITSM are advised to schedule patching within the standard change window.
