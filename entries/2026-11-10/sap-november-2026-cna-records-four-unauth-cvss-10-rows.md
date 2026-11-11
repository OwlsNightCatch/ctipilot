---
schema: 1
kind: vulnerability
title: "CVE-2026-120017, CVE-2026-89126, CVE-2026-76964 and CVE-2026-89103, SAP NetWeaver AS ABAP, Web Dispatcher and Gateway: four unauthenticated network flaws rated CVSS 10.0 and fixed on SAP's November 2026 Patch Day; Onapsis, which found three of them, says a working exploit exists and has seen no attacks"
headline: "SAP Patch Day: four unauthenticated CVSS 10.0 flaws; Onapsis names ICM2SHELL and the fixed kernel levels"
summary: >
  SAP's Patch Day of 2026-11-10 fixes four flaws it scores CVSS 3.1 10.0, reachable over the network with no privileges or user interaction: an authentication bypass in the SAML2 service provider of NetWeaver AS ABAP and the ABAP Platform that lets an attacker impersonate any user under certain configurations, memory corruption in SAP Web Dispatcher and in the NetWeaver ABAP Internet Communication Manager that Onapsis calls ICM2SHELL, and a Gateway flaw Onapsis calls ProxyGate in which the default proxy access list treats an external attacker as an internal application server.
  Onapsis gave SAP a working unauthenticated code-execution exploit for ICM2SHELL and has not observed attacks on either; the fixes are SAP Security Notes 3849308, 3778556, 3778530 and 3798345, the kernel patch levels are listed below, and ProxyGate also needs the parameter gw/acl_mode_proxy set to 1.
discovered_at: "2026-11-10T03:53:00Z"
updated_at: "2026-11-11T03:47:20Z"
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
    fixed: "SAP Security Note 3778556; kernel and Web Dispatcher patch levels per Onapsis: 7.53 PL 1616 or 1617, 7.54 PL 710, 7.77 PL 914, 7.93 PL 401 or 420, 9.16 PL 111, 9.18 PL 37 (kernel), 9.20 PL 11 or 13 (kernel); SAP HANA 2.00 and XS Advanced Web Dispatchers per the Onapsis table"
  - id: CVE-2026-76964
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP NetWeaver AS ABAP (Internet Communication Manager): KRNL64UC 7.53, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20"
    fixed: "SAP Security Note 3778530; kernel patch levels per Onapsis: 7.53 PL 1616 or 1617, 7.54 PL 710, 7.77 PL 914, 7.93 PL 401 or 420, 9.16 PL 111, 9.18 PL 37, 9.20 PL 11 or 13"
  - id: CVE-2026-89103
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP Gateway: KRNL64NUC 7.22, 7.22EXT, KRNL64UC 7.22, 7.53, 8.04, KERNEL 7.22, 7.54, 7.77, 7.93, 9.16, 9.20, 9.21"
    fixed: "SAP Security Note 3798345 plus the profile parameter gw/acl_mode_proxy = 1 on most releases; minimum kernel patch levels per Onapsis: 7.22 EXT, EX2 and EX3 PL 1612, 7.53 PL 1625, 7.54 PL 718, 7.77 PL 915, 8.04 PL 244, 9.20 PL 16, 9.21 PL 4"
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
  - url: "https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2026.html"
    publisher: "SAP (Security Patch Day, November 2026)"
    date: "2026-11-10"
    role: primary
  - url: "https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/"
    publisher: "Onapsis Research Labs (ICM2SHELL)"
    date: "2026-11-10"
    role: corroborating
  - url: "https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/"
    publisher: "Onapsis Research Labs (ProxyGate)"
    date: "2026-11-10"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13167"
    publisher: "NCSC Switzerland (Cyber Security Hub post 13167)"
    date: "2026-11-10"
    role: corroborating
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
  - quote: "The Onapsis Research Labs provided SAP a working exploit that achieves full, unauthenticated remote code execution end to end"
    publisher: "Onapsis Research Labs"
    source_url: "https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/"
  - quote: "WebSocket support is enabled by default, whether or not it is used, and SAP S/4HANA systems even ship with ICF services that accept WebSocket connections without authentication."
    publisher: "Onapsis Research Labs"
    source_url: "https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/"
  - quote: "neither a version check nor patching alone tells you whether you are safe"
    publisher: "Onapsis Research Labs"
    source_url: "https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/"
  - quote: "As of the date of this publication, the Onapsis Research Labs have not observed active in-the-wild exploitation of this vulnerability."
    publisher: "Onapsis Research Labs"
    source_url: "https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/"
verification: multi-source
sourcing_note: >
  SAP's Patch Day page lists the four notes with their CVSS 10.0 scores, and SAP's CVE records, read through ENISA's vulnerability database, carry the descriptions; the fixed kernel patch levels, the exploitation statements and the Gateway parameter come from Onapsis, which found and reported the Web Dispatcher, ICM and Gateway flaws and whose tables are not SAP's own, because SAP's Security Notes need an SAP login and were not read. The SAML2 flaw rests on SAP's CVE record alone; its fixed releases are not publicly stated. Onapsis has not observed exploitation and no source reports it; NCSC Switzerland lists the status as unknown.
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
  - "Apply SAP Security Notes 3778556 and 3778530 to every Web Dispatcher and every ABAP application server (kernel 7.40 or higher, including the Web Dispatcher embedded in SAP HANA XS) to at least the fixed patch levels Onapsis lists, internet-facing Web Dispatchers and Internet Communication Managers first, and apply note 3849308 on systems that use the SAML2 service provider, because Onapsis gave SAP a working unauthenticated code-execution exploit."
  - "On every SAP Gateway apply note 3798345 together with gw/acl_mode_proxy = 1 and a restrictive prxyinfo file, because Onapsis says a version check or the kernel patch alone does not show whether the Gateway is safe."
updates:
  - at: "2026-11-11T03:47:20Z"
    run_id: 2026-11-11T0256Z-intel
    type: update
    summary: >
      SAP's Patch Day page of 2026-11-10 is published and Onapsis, which found the Web Dispatcher, ICM and
      Gateway flaws, supplies the fixed kernel patch levels, the Gateway parameter gw/acl_mode_proxy = 1
      and the statement that it gave SAP a working unauthenticated exploit for the Web Dispatcher and ICM
      pair and has seen no attacks, replacing the entry's earlier statement that fixed releases were not
      public.
    fields: [title, headline, summary, cves, sources, evidence, verification, sourcing_note, confidence, actions, body]
migrated_from: null
---

SAP's November Patch Day of 2026-11-10 fixes four flaws that SAP scores CVSS 3.1 10.0, each reachable over the network without privileges or user interaction and with changed scope. In the SAML2 service provider of NetWeaver AS ABAP and the ABAP Platform, an unauthenticated attacker could submit crafted data, under certain configurations, to bypass authentication and impersonate arbitrary users, privileged accounts included (CVE-2026-120017, note 3849308) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700)). SAP Web Dispatcher and the Internet Communication Manager of NetWeaver AS ABAP share a memory corruption that could allow arbitrary code execution (CVE-2026-89126, note 3778556; CVE-2026-76964, note 3778530) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120674); [ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120656)), and SAP Gateway activates its default access control list with high privileges, so an external attacker is treated as an internal application server (CVE-2026-89103, note 3798345) ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120662)).

Onapsis, which found and reported the Web Dispatcher, ICM and Gateway flaws, names the first pair ICM2SHELL: a memory corruption in the shared kernel code that reassembles fragmented WebSocket messages, reachable on the HTTP or HTTPS port with no credentials, and "WebSocket support is enabled by default, whether or not it is used" ([Onapsis, 2026-11-10](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/)). Onapsis provided SAP a working unauthenticated code-execution exploit that runs commands as the system's <sid>adm user, a single connection crashes the process on every kernel it tested, and it has not observed attacks; NCSC Switzerland lists the exploitation status as unknown ([Onapsis, 2026-11-10](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/); [NCSC Switzerland, 2026-11-10](https://security-hub.ncsc.admin.ch/#/posts/13167)). It affects ABAP systems on kernel 7.40 or higher and every Web Dispatcher, the one in SAP HANA XS included; AS Java alone and kernel 7.22 are not affected, and kernels out of maintenance may get no fix. The fixed patch levels are 7.53 PL 1616 or 1617, 7.54 PL 710, 7.77 PL 914, 7.93 PL 401 or 420, 9.16 PL 111, 9.18 PL 37 and 9.20 PL 11 or 13 ([Onapsis, 2026-11-10](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/)).

ProxyGate lets an unauthenticated attacker with network access run operating system commands as `<sid>adm` on the Gateway, and its exploitability depends on the proxy access list: a permissive prxyinfo file, or none with gw/acl_mode_proxy at its default of 0, leaves the system exposed, so "neither a version check nor patching alone tells you whether you are safe"; on most releases SAP's fix combines the kernel patch with gw/acl_mode_proxy = 1, and Onapsis lists the minimum patch level for each kernel release, for example 7.53 PL 1625 and 7.54 PL 718 ([Onapsis, 2026-11-10](https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/)).

**Exposure:** a system that runs one of the components and lets an untrusted network reach its Web Dispatcher, Internet Communication Manager, Gateway or SAML2 endpoint; the SAML2 flaw applies under certain configurations of the SAML 2.0 service provider ([ENISA EUVD, 2026-11-10](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-120700)).

**Detection:** Onapsis expects every exploitation attempt against ICM2SHELL to crash the ICM or Web Dispatcher at least once, so unexpected restarts of either process outside maintenance deserve investigation; requests with status 101 in the ICM or Web Dispatcher HTTP log show whether WebSocket is in use before anyone considers disabling it ([Onapsis, 2026-11-10](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/)). The sources name no indicator for the SAML2 flaw or the Gateway.

**Defender takeaway:** patch internet-facing Web Dispatchers and Internet Communication Managers first and every application server and Web Dispatcher after them, set gw/acl_mode_proxy to 1 on every Gateway, and apply note 3849308 where the SAML2 service provider runs; Onapsis calls the notes the only complete fix.

## Update — 2026-11-11T03:47:20Z

SAP's Security Patch Day page of 2026-11-10 lists 35 new notes and four GitHub security advisories and carries the four CVSS 10.0 notes above ([SAP, 2026-11-10](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2026.html)). Onapsis published threat advisories for the Web Dispatcher and ICM pair, which it names ICM2SHELL, and for the Gateway flaw, which it names ProxyGate, with the fixed kernel patch levels, the Gateway parameter gw/acl_mode_proxy = 1 and the statement that it gave SAP a working unauthenticated exploit for ICM2SHELL and has seen no attacks ([Onapsis, 2026-11-10](https://onapsis.com/blog/icm2shell-cve-2026-76964-cve-2026-89126-sap-netweaver-web-dispatcher-threat-advisory/); [Onapsis, 2026-11-10](https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/)). Five further notes on the page are rated Critical at CVSS 9.1 to 9.9, among them an ABAP application server OS command injection for low-privileged users (CVE-2026-76965, note 3792735) and a code injection in NetWeaver Knowledge Management XML Forms (CVE-2026-109803, note 3809153); they are not covered here ([SAP, 2026-11-10](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/november-2026.html)).
