---
schema: 1
kind: threat
title: "Mautic 7.1.2 / 6.0.9 — seven authenticated flaws, including two post-auth RCE paths (SSTI and path-traversal-to-PHP-RCE), an SSRF and an API authorization bypass"
headline: "Mautic 7.1.2 / 6.0.9 — seven authenticated flaws, including two post-auth RCE paths (SSTI and path-traversal-to-PHP-RCE), an SSRF and an API authorization"
summary: "Mautic open-source marketing-automation platform ships 7.1.2 / 6.0.9 fixing seven authenticated flaws — including two post-auth remote-code-execution paths (CVE-2026-9558 server-side template injection; CVE-2026-9559 path-traversal-to-PHP-RCE) plus a Focus-component SSRF (CVE-2026-9557) reaching internal services and cloud metadata. BSI CERT-Bund rated the cluster HIGH; the platform is used across European universities, cantonal administrations, NGOs and political parties for GDPR-compliant campaign mail (BSI CERT-Bund WID-SEC-2026-1724, 2026-05-29). No in-the-wild exploitation reported; patch now and tighten Mautic-server egress and role permissions."
discovered_at: "2026-05-31T05:00:00Z"
event_date: 2026-05-29
run_id: 2026-05-31-d742bed9
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - auth-bypass
  - sqli
  - info-disclosure
  - cloud
  - path-traversal
  - patch-available
regions:
  - europe
  - dach
sectors:
  - public-sector
  - education
  - healthcare
entities: []
cves:
  - id: CVE-2026-4776
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9557
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9558
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9559
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9808
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9809
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
  - id: CVE-2026-9811
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status:
      - patch-available
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1724"
    publisher: BSI CERT-Bund WID-SEC-2026-1724
    role: primary
  - url: "https://github.com/mautic/mautic/security/advisories/GHSA-fcmw-wx57-9p75"
    publisher: Mautic GitHub Security Advisory GHSA-fcmw-wx57-9p75
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ein entfernter, authentisierter Angreifer kann mehrere Schwachstellen in Mautic ausnutzen, um SQL-Injection- und Server-Side Request Forgery (SSRF)-Angriffe durchzuführen und um Informationen offenzulegen ... sowie unter Umständen beliebigen Code auf dem Server auszuführen"
    publisher: BSI CERT-Bund WID-SEC-2026-1724
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Upgrade Mautic to 7.1.2 or 6.0.9 now — the cluster includes two post-auth RCE paths.** CVE-2026-9558 (theme-template SSTI) and CVE-2026-9559 (campaign-import path-traversal-to-PHP-RCE) give an authenticated user server-side code execution; the Focus SSRF (CVE-2026-9557) reaches cloud instance-metadata. Until patched, restrict theme-creation and campaign-import permissions to trusted admins and egress-filter the Mautic host (block `169.254.169.254` and internal subnets). Reference: [BSI CERT-Bund WID-SEC-2026-1724](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1724)."
migrated_from: briefs/2026-05-31.md
---

The Mautic project shipped releases 7.1.2 and 6.0.9 on 2026-05-28/29 closing seven vulnerabilities, and BSI CERT-Bund issued advisory WID-SEC-2026-1724 on 2026-05-29 rating the cluster *hoch* (HIGH) ([BSI CERT-Bund WID-SEC-2026-1724, 2026-05-29](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1724); [Mautic GitHub Security Advisory GHSA-fcmw-wx57-9p75, 2026-05-28](https://github.com/mautic/mautic/security/advisories/GHSA-fcmw-wx57-9p75)). All seven require an authenticated session, but several go well beyond information disclosure. CVE-2026-9558 is a server-side template injection in theme templates: an authenticated user with theme-creation permission can execute arbitrary code on the server (all supported branches, 4.x–7.x). CVE-2026-9559 is a path traversal in the campaign-import handler that writes arbitrary PHP into sensitive directories, yielding remote code execution under the web-server user (Mautic 7.x). CVE-2026-9557 is a server-side request forgery in the Focus component: an authenticated user can make the Mautic server issue HTTP requests to internal network resources and cloud instance-metadata endpoints (IMDS) and read local files. CVE-2026-4776 is a SQL injection in the API contact-filtering interface. CVE-2026-9808 is an authorization bypass in the API v2 (Mautic 7.x). CVE-2026-9809 and CVE-2026-9811 are stored XSS in the Projects feature (Mautic 7.x). No in-the-wild exploitation is reported; exploitation status is unknown. Patched in 7.1.2 and 6.0.9 (released 2026-05-28/29).

**Why it matters to us:** Mautic is the dominant self-hosted, GDPR-compliant campaign-mail platform across European universities, cantonal and municipal communications teams, NGOs and political parties — a population that frequently runs it on an internal network segment with reachability to cloud metadata or back-office services. A single compromised authenticated account (the kind harvested in routine credential-stuffing or AiTM phishing) now reaches server-side code execution via the theme-template SSTI or the campaign-import PHP write (`T1190`, `T1059`), while the Focus SSRF reaches internal services and the cloud instance-metadata endpoint (`T1552.005`). Detection: review Mautic logs for theme-template edits and campaign-import operations by non-admin roles, and for Focus requests resolving to RFC-1918 ranges or `169.254.169.254`; alert on the Mautic worker spawning shell / `php` child processes or making outbound connections to internal subnets. Hardening: upgrade to 7.1.2 / 6.0.9; restrict theme-creation and campaign-import permissions to trusted administrators; egress-filter the Mautic host (block link-local metadata and internal subnets); apply CSP headers on the admin UI.
