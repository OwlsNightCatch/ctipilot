---
schema: 1
kind: vulnerability
title: "CVE-2026-120017, CVE-2026-89126, CVE-2026-76964 and CVE-2026-89103, SAP NetWeaver AS ABAP, Web Dispatcher and Gateway: four unauthenticated network flaws rated CVSS 10.0 in SAP's CVE records of 2026-11-10, published ahead of Patch Day; no exploitation reported"
headline: "SAP's CVE records list four unauthenticated CVSS 10.0 flaws in Web Dispatcher, ICM, Gateway and the ABAP SAML2 service"
summary: >
  SAP, acting as CNA, published CVE records on 2026-11-10 for four flaws it scores CVSS 3.1 10.0, reachable over the network with no privileges or user interaction: an authentication bypass in the SAML2 service provider of NetWeaver AS ABAP and the ABAP Platform that lets an attacker impersonate any user, privileged accounts included, under certain configurations, memory corruption in SAP Web Dispatcher and in the NetWeaver ABAP Internet Communication Manager that could allow arbitrary code execution, and a default access control list in SAP Gateway that treats an external attacker as an internal application server.
  The fixes are SAP Security Notes 3849308, 3778556, 3778530 and 3798345, which need an SAP login, and SAP's November Patch Day page was not yet published when the records were read; no record names exploitation or a public proof of concept.
discovered_at: "2026-11-10T03:53:00Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-10T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:sap-netweaver-as-abap", "product:sap-abap-platform", "product:sap-web-dispatcher", "product:sap-gateway", "product:sap-kernel"]
techniques: [T1190, T1078]
affected_products: ["SAP NetWeaver AS ABAP", "SAP ABAP Platform", "SAP Web Dispatcher", "SAP Gateway", "SAP Kernel"]
cves:
  - id: CVE-2026-120017
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider), under certain configurations: SAP_BASIS 702, 731, 740, 750 to 758, 816, 920, 921, 922"
    fixed: "SAP Security Note 3849308 (login required; fixed releases not publicly stated)"
  - id: CVE-2026-89126
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP Web Dispatcher: WEBDISP 7.53, 7.54, 7.77, 7.93, 9.16, KERNEL 7.53, 9.18, 9.20, KRNL64UC 7.53, HDB 2.00, XS_ADVANCED_RUNTIME 1.00, SAP_EXTENDED_APP_SERVICES 1"
    fixed: "SAP Security Note 3778556 (login required; fixed releases not publicly stated)"
  - id: CVE-2026-76964
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP NetWeaver AS ABAP (Internet Communication Manager): KRNL64UC 7.53, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20"
    fixed: "SAP Security Note 3778530 (login required; fixed releases not publicly stated)"
  - id: CVE-2026-89103
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP Gateway: KRNL64NUC 7.22, 7.22EXT, KRNL64UC 7.22, 7.53, 8.04, KERNEL 7.22, 7.54, 7.77, 7.93, 9.16, 9.20, 9.21"
    fixed: "SAP Security Note 3798345 (login required; fixed releases not publicly stated)"
sources:
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700"
    publisher: "SAP CNA record CVE-2026-120017, via ENISA EUVD"
    date: "2026-11-10"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120674"
    publisher: "SAP CNA record CVE-2026-89126, via ENISA EUVD"
    date: "2026-11-10"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120656"
    publisher: "SAP CNA record CVE-2026-76964, via ENISA EUVD"
    date: "2026-11-10"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120662"
    publisher: "SAP CNA record CVE-2026-89103, via ENISA EUVD"
    date: "2026-11-10"
    role: primary
closed_sources: []
evidence:
  - quote: "An unauthenticated attacker could submit specially crafted data to bypass authentication and impersonate arbitrary users, including privileged accounts."
    publisher: "SAP CNA record CVE-2026-120017, via ENISA EUVD"
    source_url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700"
  - quote: "An unauthenticated attacker could send specially crafted network traffic to trigger a memory corruption condition in the affected functionality."
    publisher: "SAP CNA record CVE-2026-89126, via ENISA EUVD"
    source_url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120674"
  - quote: "SAP Gateway activates the default Access Control List with high privileges allowing categorization of external attacker as internal application server."
    publisher: "SAP CNA record CVE-2026-89103, via ENISA EUVD"
    source_url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120662"
verification: single-source
sourcing_note: >
  The only public detail is SAP's own CVE record text, read through ENISA's vulnerability database, ahead of SAP's Patch Day page, which was not yet published, and its Security Notes are readable only with an SAP login; the fixed releases, SAP's own priority labels and any exploitation statement are therefore not yet visible. The CVSS 3.1 vectors and scores are those SAP assigned.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Pull SAP Security Notes 3849308, 3778556, 3778530 and 3798345 as soon as SAP's Patch Day page lists them and apply the kernel or support-package fix each names, starting with systems whose Web Dispatcher, Internet Communication Manager or Gateway ports are reachable from untrusted networks."
updates: []
migrated_from: null
---

SAP, acting as CNA, published CVE records on 2026-11-10 for four flaws it scores CVSS 3.1 10.0, each reachable over the network without privileges or user interaction and with changed scope. In the SAML2 service provider of NetWeaver AS ABAP and the ABAP Platform, an unauthenticated attacker could submit crafted data, under certain configurations, to bypass authentication and impersonate arbitrary users, privileged accounts included (CVE-2026-120017, note 3849308) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700)). In SAP Web Dispatcher, crafted network traffic triggers a memory corruption that could allow arbitrary code execution and full compromise (CVE-2026-89126, note 3778556) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120674)), and the Internet Communication Manager of NetWeaver AS ABAP has the same class of flaw (CVE-2026-76964, note 3778530) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120656)). SAP Gateway activates its default access control list with high privileges, so an external attacker with network access is treated as an internal application server and can perform unauthorized actions (CVE-2026-89103, note 3798345) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120662)).

The records list SAP_BASIS 702, 731, 740, 750 to 758, 816 and 920 to 922 for the SAML2 flaw ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700)); kernel and Web Dispatcher builds 7.53, 7.54, 7.77, 7.93, 9.16, 9.18 and 9.20 for the Web Dispatcher and Internet Communication Manager flaws, the Web Dispatcher record adding HDB 2.00, XS_ADVANCED_RUNTIME 1.00 and SAP_EXTENDED_APP_SERVICES 1 ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120674); [ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120656)); and kernel 7.22 to 9.21 for the Gateway flaw ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120662)). Each record points to the SAP Security Note that carries the fix; none names exploitation or a public proof of concept, and ENISA shows an EPSS value of 0.0 for each. An anonymous path to code execution or to impersonating a privileged user on a network-facing SAP component forces the timeline by itself, whether or not anyone exploits it yet.

**Exposure:** a system that runs one of the listed components and builds and lets an untrusted network reach its Web Dispatcher, Internet Communication Manager, Gateway or SAML2 endpoint; the SAML2 flaw applies only where the SAML 2.0 service provider is configured ("under certain configurations") ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700)).

**Detection:** the records name no indicators. From the stated mechanisms, the places to look are Web Dispatcher and Internet Communication Manager access logs and process restarts for malformed requests, the SAML2 endpoint for assertions from issuers you do not trust, and Gateway logs for administrative calls from addresses that are not your own application servers.

**Defender takeaway:** read the four SAP Security Notes when SAP's Patch Day page lists them and apply the kernel or support-package fix each names, internet-reachable Web Dispatchers and Gateways first; until then limit network access to these components to the systems that need it.
