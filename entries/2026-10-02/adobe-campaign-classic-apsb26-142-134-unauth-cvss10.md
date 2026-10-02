---
schema: 1
kind: vulnerability
title: "Adobe Campaign Classic: eight unauthenticated CVSS 10.0 flaws in APSB26-142 and three more in APSB26-134, with build 9402 as the fix"
headline: "Adobe's 22 September revision grew one Campaign Classic CVE into eighteen, ten unauthenticated; build 9402 closes them"
summary: >
  Adobe's Priority 1 bulletin APSB26-142 for on-premise Adobe Campaign Classic v7 was published on 2026-09-08 with one CVE
  and revised on 2026-09-22 to eighteen Critical CVEs, ten needing no privileges, eight of them CVSS 10.0; builds 9401 and
  earlier are affected and build 9402 is the fix. The earlier bulletin APSB26-134 (build 9401, 2026-08-25) fixed three more
  unauthenticated CVSS 10.0 flaws. Adobe is not aware of exploitation and none of the CVEs is in
  CISA KEV.
discovered_at: "2026-10-02T05:00:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:adobe-campaign-classic"]
techniques: [T1190]
affected_products: ["Adobe Campaign Classic"]
cves:
  - id: CVE-2026-82004
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-73369
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-84412
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-89275
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-75723
    cvss: "10.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-75699
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-75703
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-75721
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-83660
    cvss: "9.9"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-75728
    cvss: "9.1"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9401 and earlier (on-premise deployments and the on-premise components of hybrid deployments)"
    fixed: "ACC v7 7.4.4 build 9402"
  - id: CVE-2026-76197
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9400 and earlier"
    fixed: "ACC v7 7.4.4 build 9401 (build 9402 also carries it)"
  - id: CVE-2026-76195
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9400 and earlier"
    fixed: "ACC v7 7.4.4 build 9401 (build 9402 also carries it)"
  - id: CVE-2026-76193
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic v7 7.4.4 build 9400 and earlier"
    fixed: "ACC v7 7.4.4 build 9401 (build 9402 also carries it)"
sources:
  - url: "https://www.adobe.com/trust/security/products/campaign/apsb26-142.html"
    publisher: "Adobe PSIRT (APSB26-142)"
    date: "2026-09-22"
    role: primary
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-134.html"
    publisher: "Adobe PSIRT (APSB26-134)"
    date: "2026-08-25"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-10-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Adobe is not aware of any exploits in the wild for any of the issues addressed in this update."
    publisher: "Adobe PSIRT (APSB26-142)"
    source_url: "https://www.adobe.com/trust/security/products/campaign/apsb26-142.html"
  - quote: "Adobe-hosted instances have already been remediated and require no customer action."
    publisher: "Adobe PSIRT (APSB26-142)"
    source_url: "https://www.adobe.com/trust/security/products/campaign/apsb26-142.html"
  - quote: "some Adobe-hosted instances may continue to report build 9401 even though the applicable security fixes have already been deployed"
    publisher: "Adobe PSIRT (APSB26-142)"
    source_url: "https://www.adobe.com/trust/security/products/campaign/apsb26-142.html"
verification: single-source
sourcing_note: >
  Adobe is the only assessor: both bulletins are its own, the scores are the bulletin tables' and the entry rests on no
  independent analysis. Adobe's CVE record for CVE-2026-75703 describes arbitrary code execution while the bulletin table
  gives the impact as application denial-of-service; the CVE record is followed here. None of the CVEs is in CISA KEV as
  of the 2026-10-01 catalog.
confidence: high
references:
  - 2026-08-02/adobe-campaign-classic-apsb26-114-cvss10-unauth-rce
  - 2026-08-07/adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  - 2026-08-28/adobe-august-2026-coldfusion-campaign-classic-cvss10
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every on-premise Adobe Campaign Classic v7 server, and the on-premise components of any hybrid deployment, to build 9402; build 9401 fixes only APSB26-134's three flaws, and an Adobe-hosted instance that still reports 9401 is not evidence of exposure."
updates: []
migrated_from: null
---

Adobe's Priority 1 bulletin APSB26-142 covers Adobe Campaign Classic v7 7.4.4 build 9401 and earlier on Windows and Linux and names build 9402 as the fix; it was published on 2026-09-08 with one CVE and revised on 2026-09-22 to add seventeen more, for eighteen, all rated Critical ([Adobe PSIRT, 2026-09-22](https://www.adobe.com/trust/security/products/campaign/apsb26-142.html)). Ten of the eighteen need no privileges: eight are CVSS 10.0 with the vector AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H (CVE-2026-82004, an OS command injection; six code-injection flaws, CVE-2026-73369, -84412, -89275, -75699, -75703 and -75721; and CVE-2026-75723, an incorrect-authorization flaw), plus CVE-2026-83660 (SSRF, 9.9) and CVE-2026-75728 (incorrect authorization, 9.1) ([Adobe PSIRT, 2026-09-22](https://www.adobe.com/trust/security/products/campaign/apsb26-142.html)). The remaining eight require low or high privileges. The earlier bulletin APSB26-134 (Priority 1, 2026-08-25) fixed three more unauthenticated CVSS 10.0 flaws in build 9401, CVE-2026-76197 and CVE-2026-76195 (OS command injection) and CVE-2026-76193 (SSRF) ([Adobe PSIRT, 2026-08-25](https://helpx.adobe.com/security/products/campaign/apsb26-134.html)).

Adobe states it is not aware of exploitation of any issue in APSB26-142, and none of these CVEs is in CISA's KEV catalog as of the 2026-10-01 version ([Adobe PSIRT, 2026-09-22](https://www.adobe.com/trust/security/products/campaign/apsb26-142.html); [CISA KEV, 2026-10-01](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The bulletin applies to fully on-premise deployments and the on-premise components of hybrid deployments; Adobe-hosted instances are already remediated, and because the hosted fixes did not increment the customer-visible build number, some hosted instances still report build 9401 ([Adobe PSIRT, 2026-09-22](https://www.adobe.com/trust/security/products/campaign/apsb26-142.html)). Adobe's table names build 9402 for all eighteen, so estates that moved to it for the single CVE visible on 2026-09-08 already hold every fix; estates that stopped at build 9401 or earlier carry the ten unauthenticated flaws.

**Exposure:** on-premise Campaign Classic v7 servers, and the on-premise tier of hybrid deployments, running build 9401 or earlier; the flaw classes (OS command injection, code injection, incorrect authorization and SSRF) are all network-reachable, so reachability of the Campaign endpoints from outside decides how urgent the update is.

**Detection:** Adobe publishes no detection guidance or compromise check for these flaws; the flaw classes point to web access logs for requests to Campaign endpoints from unexpected sources, process-creation events in which the Campaign server or its web-server parent starts a shell or interpreter, and outbound requests from the Campaign host to internal services.

**Defender takeaway:** update the on-premise tier to build 9402 and check the build on the server itself, since a hosted instance's displayed build is not a reliable signal; an internet-reachable on-premise instance that sat on build 9401 or earlier carried ten unauthenticated paths and warrants a compromise assessment, because Adobe provides none.
