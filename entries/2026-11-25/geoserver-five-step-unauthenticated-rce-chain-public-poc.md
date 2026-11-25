---
schema: 1
kind: vulnerability
title: "GeoServer 3.0.2, 2.28.6 and 2.27.7: a five-step chain from an anonymous WFS request to code execution (CVE-2026-129244, CVE-2026-129243, CVE-2026-120705, CVE-2026-129245, CVE-2026-129242) works on a default installation, was disclosed in advisories published on 2026-11-23 and has a public proof of concept; no exploitation reported (CVSS 4.0 9.2 for the critical step)"
headline: "GeoServer: five-step unauthenticated chain to code execution has a public PoC; update to 3.0.2, 2.28.6 or 2.27.7"
summary: >
  The GeoServer project published a batch of security advisories on 2026-11-23, most for flaws fixed in 3.0.2, 2.28.6 and 2.27.7, and five of them chain an anonymous WFS request to code execution: a path disclosure, a service-security bypass with a prefixed service name, an XML injection, a predictable remember-me key that forges an administrator session (critical, CVSS 4.0 9.2) and a JDBC deserialization. The reporter, who says it works on a default installation, published a full-chain proof of concept the same night; the project announced the fixed releases on 2026-10-19 and no source reports exploitation.
discovered_at: "2026-11-25T04:49:00Z"
updated_at: null
event_date: "2026-11-23"
run_id: 2026-11-25T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass, default-config, poc-public, patch-available]
regions: [global]
sectors: [technology]
entities: [product:geoserver]
techniques: [T1190, T1606.001, T1005]
affected_products: ["GeoServer"]
cves:
  - id: CVE-2026-129244
    cvss: "6.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "GeoServer 3.0.0 to 3.0.1, 2.28.0 to 2.28.5, 2.27.6 and earlier"
    fixed: "3.0.2, 2.28.6, 2.27.7"
  - id: CVE-2026-129243
    cvss: "8.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "GeoServer 3.0.0 to 3.0.1, 2.28.0 to 2.28.5, 2.27.6 and earlier"
    fixed: "3.0.2, 2.28.6, 2.27.7"
  - id: CVE-2026-120705
    cvss: "8.6"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "GeoServer 3.0.0 to 3.0.1, 2.28.0 to 2.28.5, 2.27.6 and earlier"
    fixed: "3.0.2, 2.28.6, 2.27.7"
  - id: CVE-2026-129245
    cvss: "9.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "GeoServer 3.0.0 to 3.0.1, 2.28.0 to 2.28.5, 2.27.6 and earlier"
    fixed: "3.0.2, 2.28.6, 2.27.7"
  - id: CVE-2026-129242
    cvss: "8.6"
    epss: null
    type: deserialization
    vector: zero-click
    auth: admin-required
    status: [poc-public, patch-available]
    affected: "GeoServer 3.0.0 to 3.0.1, 2.28.0 to 2.28.5, 2.27.6 and earlier"
    fixed: "3.0.2, 2.28.6, 2.27.7"
sources:
  - url: "https://geoserver.org/vulnerability/2026/11/23/cve-update.html"
    publisher: "GeoServer project"
    date: "2026-11-23"
    role: primary
  - url: "https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq"
    publisher: "GeoServer project (GitHub security advisory)"
    date: "2026-11-23"
    role: primary
  - url: "https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/"
    publisher: "CryptoCat (reporter)"
    date: "2026-11-23"
    role: corroborating
  - url: "https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-3-0-2-released.html"
    publisher: "GeoServer project"
    date: "2026-10-19"
    role: corroborating
  - url: "https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-2-27-7-released.html"
    publisher: "GeoServer project"
    date: "2026-10-19"
    role: corroborating
  - url: "https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj"
    publisher: "GeoServer project (GitHub security advisory)"
    date: "2026-11-23"
    role: corroborating
  - url: "https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq"
    publisher: "GeoServer project (GitHub security advisory)"
    date: "2026-11-23"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "The project's advisories and its post are first-party; the reporter's write-up is an independent demonstration of the chain, and its full-chain proof of concept is public. CVSS figures are the project's CNA scores (4.0 for four steps, 3.1 for CVE-2026-120705); the reporter's 9.8 for the whole chain is its own assessment. CVE.org records for some ids were not yet published on 2026-11-25."
confidence: high
references:
  - 2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update every internet-reachable GeoServer to 3.0.2, 2.28.6 or 2.27.7 (2.27 is end of life, so plan the move to a supported line) and, where that waits, remove rememberme from the web filter chain under Security > Authentication, block requests whose service parameter contains a slash at a proxy in front of GeoServer and restrict WFS for anonymous users, because a public proof of concept chains five steps from an anonymous request to code execution on a default installation."
updates: []
migrated_from: null
---

The GeoServer project published a batch of security advisories on 2026-11-23, most for flaws fixed in 3.0.2, 2.28.6 and 2.27.7, which the project had announced on 2026-10-19 as an important upgrade for production systems ([GeoServer, 2026-11-23](https://geoserver.org/vulnerability/2026/11/23/cve-update.html); [GeoServer, 2026-10-19](https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-3-0-2-released.html)). Five chain, in the order the project gives: a WFS stored-query exception that discloses the data directory path (CVE-2026-129244), service-security rules bypassed with a prefixed service name such as x/WFS so anonymous users can create stored queries (CVE-2026-129243), an unauthenticated WFS GetFeatureById XML injection (CVE-2026-120705), a predictable remember-me key that allows administrator session forgery (CVE-2026-129245, critical) and deserialization in the JDBC user and role services (CVE-2026-129242, administrator required) ([GeoServer, 2026-11-23](https://geoserver.org/vulnerability/2026/11/23/cve-update.html); [GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj)). The project says the critical advisory was first reported as step 4 of an unauthenticated remote command execution chain and that each step was given its own CVE at the CVE Numbering Authority's request ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq)).

The reporter says the chain gives unauthenticated remote command execution on a default installation: the service-name bypass lets an anonymous stored query read the files that hold the remember-me key and an administrator password digest, which forges an administrator session ([CryptoCat, 2026-11-23](https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/)). A full-chain proof of concept has been public since the reporter's write-up. Affected are 3.0.0 to 3.0.1, 2.28.0 to 2.28.5 and 2.27.6 and earlier, with 3.0.2, 2.28.6 and 2.27.7 as the fixed releases ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq)); the project says the 2.27 series has reached end of life ([GeoServer, 2026-10-19](https://geoserver.org/announcements/vulnerability/2026/10/19/geoserver-2-27-7-released.html)). No source reports exploitation as of 2026-11-25.

**Exposure:** GeoServer on the affected builds with WFS reachable by anonymous users and the REST API reachable; the reporter says it works on a default installation, with the stock admin account enabled in the default user service and, for its payload, a Linux host, and that the chain read the live key, so it never depended on the shipped value and a rotated key alone does not close it ([CryptoCat, 2026-11-23](https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/)); the fixed releases use a random per-node key and invalidate existing remember-me cookies on upgrade ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq)).

**Detection:** in web access logs, WFS requests whose service parameter contains a slash such as x/WFS, and stored queries you did not create under the data directory's wfs/query and workspaces/*/wfs/query folders ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj)); in REST access logs, an administrator session that uploads a database file and creates a JDBC user group service ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq)). If exposure is suspected the project advises changing administrator passwords, because changing the key does not help when the same file disclosure also reveals it ([GeoServer, 2026-11-23](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq)).

**Defender takeaway:** update internet-reachable GeoServer to a fixed release now rather than at the next cycle, since a public full-chain proof of concept exists and the fixes are weeks old; where it must wait, apply the project's workarounds for steps 2 and 4, and on any instance that ran an older build while reachable, review the stored-query folders and the administrator accounts.
