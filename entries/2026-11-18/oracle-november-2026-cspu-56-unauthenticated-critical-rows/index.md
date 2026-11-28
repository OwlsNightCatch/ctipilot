---
schema: 1
kind: vulnerability
title: "Oracle's November 2026 Critical Security Patch Update: 56 of its 62 rows at CVSS 9.0 or above are reachable over the network without authentication, six of them at CVSS 10.0 in Access Manager, WebLogic Server, Platform Security for Java and Business Intelligence Enterprise Edition; Oracle flags no row as exploited, but CISA lists the Brotli flaw behind three of them"
headline: "Oracle CSPU: 56 unauthenticated rows at CVSS 9.0+, six at 10.0 in Access Manager, WebLogic, BI; Brotli rows on KEV"
summary: >
  Oracle's Critical Security Patch Update of 2026-11-17 carries 655 patches, and its risk matrices mark 56 of the 62 rows scoring CVSS 3.1 9.0 or above as remotely exploitable without authentication. Six are CVSS 10.0 with changed scope, in Oracle Access Manager (three rows), WebLogic Server TopLink Integration, Platform Security for Java and Business Intelligence Enterprise Edition, and WebLogic Server and E-Business Suite carry further unauthenticated rows at 9.8. The only exploited flaw among them is the Brotli decoder flaw CVE-2026-111497, which CISA has listed as exploited since 2026-10-27 and which fills three of the unauthenticated rows; for attacks that need no privileges Oracle's interim measure is blocking the network protocols an attack needs.
discovered_at: "2026-11-18T05:10:30Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, patch-available, identity]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["Oracle Access Manager", "Oracle WebLogic Server", "Oracle Platform Security for Java", "Oracle Business Intelligence Enterprise Edition", "Oracle E-Business Suite", "Oracle APEX", "Oracle Communications Diameter Signaling Router", "Oracle Communications Unified Assurance", "Oracle PeopleSoft PeopleTools"]
cves:
  - id: CVE-2026-114835
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Admin Console component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91500
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91510
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91507
    cvss: "9.3"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91569
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, TopLink Integration component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91470
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, Core component, reachable over T3 and IIOP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91456
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, Core component, reachable over SOAP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91570
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, TopLink Integration component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91583
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, TopLink Integration component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-91585
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, TopLink Integration component, reachable over TCP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114824
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Platform Security for Java 12.2.1.4.0, 14.1.2.0.0, Centralized Thirdparty Jars component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114784
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Business Intelligence Enterprise Edition 8.2.0.0.0, 26.01.0.0.0, Platform Security component, reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114880
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Document Management and Collaboration (Attachments), reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114924
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Application Object Library (Core), reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114925
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Applications Framework (REST Services), reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114863
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Universal Work Queue (Media Integration issues), reachable over HTTP"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114849
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle APEX 24.1.22, 24.2.21, 26.1.5, 26.2.0 and Oracle REST Data Services 24.2.0 to 26.3.0, reachable over HTTPS"
    fixed: "November 2026 Critical Security Patch Update"
  - id: CVE-2026-114850
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle APEX 24.1.22, 24.2.21, 26.1.5, 26.2.0, reachable over HTTPS"
    fixed: "November 2026 Critical Security Patch Update"
sources:
  - url: "https://www.oracle.com/security-alerts/cspunov2026.html"
    publisher: "Oracle Critical Security Patch Update, November 2026 (risk matrices)"
    date: "2026-11-17"
    role: primary
  - url: "https://www.oracle.com/security-alerts/cspunov2026verbose.html"
    publisher: "Oracle Critical Security Patch Update, November 2026 (text version of the risk matrices)"
    date: "2026-11-17"
    role: primary
  - url: "https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938"
    publisher: "Tenable"
    date: "2026-11-17"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-11-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This Critical Security Patch Update contains 655 new security patches across the product families listed below."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspunov2026.html"
  - quote: "Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspunov2026verbose.html"
  - quote: "This month's update includes 62 critical patches across 57 CVEs."
    publisher: "Tenable"
    source_url: "https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938"
verification: single-source
sourcing_note: >
  Oracle is the disclosing vendor and its risk matrices carry every row; the counts here are tallied from the matrices' own columns (CVSS 3.1 score, remote exploit without authentication, privileges required), and Tenable's 62 critical patches across 57 CVEs matches the tally. Oracle's matrices carry no exploited or publicly disclosed flag and the page has no exploitation statement about these rows beyond a generic note on attacks against already-patched flaws; the only exploitation claimed here is CISA's listing of the Brotli flaw CVE-2026-111497, whose three rows are among the 56, and no third-party write-up of the other rows was found at the time of writing. Patch numbers sit in My Oracle Support notes that need a login. The Java SE rows of the same release, including Java4Shell, are covered in their own entry.
confidence: high
references: ["2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce", "2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Apply the November 2026 CSPU first to Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools, whose Brotli rows are the KEV-listed CVE-2026-111497, then block T3 and IIOP to every WebLogic Server from networks that untrusted hosts can reach and patch internet-reachable Access Manager, WebLogic Server, E-Business Suite and APEX or REST Data Services instances, because Oracle marks 56 rows at CVSS 9.0 or above as exploitable without authentication and names blocking the required network protocols as its interim measure for attacks that need no privileges."
updates:
  - at: "2026-11-22T14:49:46Z"
    run_id: 2026-11-22T1407Z-audit
    type: correction
    summary: >
      Three of the release's unauthenticated 9.8 rows, in Communications Diameter Signaling Router,
      Communications Unified Assurance and PeopleSoft PeopleTools, are the Brotli flaw CVE-2026-111497,
      which CISA has listed as exploited since 2026-10-27; those products move to the front of the patch
      order. Oracle flags no row, and no exploitation of the other rows is reported.
    fields: [body, headline, sourcing_note, summary, title, actions, affected_products]
migrated_from: null
---

Oracle's Critical Security Patch Update of 2026-11-17 carries 655 new patches ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)). Its risk matrices score 62 rows at CVSS 3.1 9.0 or above, 56 of them marked remotely exploitable without authentication and without privileges ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)); Tenable counts 62 critical patches across 57 CVEs ([Tenable, 2026-11-17](https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938)). Six of them score 10.0 with changed scope: Oracle Access Manager 12.2.1.4.0 and 14.1.2.1.0 in the Admin Console (CVE-2026-114835) and twice in the Authentication Engine (CVE-2026-91500, CVE-2026-91510), WebLogic Server TopLink Integration (CVE-2026-91569), Platform Security for Java (CVE-2026-114824) and Business Intelligence Enterprise Edition Platform Security (CVE-2026-114784), all over HTTP ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)).

WebLogic Server 12.2.1.4.0 to 15.1.1.0.0 carries further unauthenticated rows at 9.8: Core over T3 and IIOP (CVE-2026-91470) and over SOAP (CVE-2026-91456), and TopLink Integration over HTTP (CVE-2026-91570, CVE-2026-91583) and TCP (CVE-2026-91585); Oracle words the T3 and IIOP row as an easily exploitable flaw that lets an unauthenticated attacker with network access compromise WebLogic Server ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026verbose.html)). E-Business Suite 12.2.3 to 12.2.15 has four unauthenticated HTTP rows at 9.8 in Attachments (CVE-2026-114880), Application Object Library (CVE-2026-114924), Applications Framework REST Services (CVE-2026-114925) and Universal Work Queue (CVE-2026-114863), and APEX and REST Data Services have two at 9.8 over HTTPS (CVE-2026-114849, CVE-2026-114850) ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)). Oracle's footnote says the patch for the E-Business Suite row CVE-2026-114918 also addresses CVE-2025-61882 ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)), which CISA lists as exploited with known ransomware use ([CISA, 2026-11-17](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The release also carries three unauthenticated 9.8 rows for the Brotli flaw CVE-2026-111497 in Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)), a flaw CISA has listed as exploited since 2026-10-27 ([CISA, 2026-11-17](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

Oracle's matrices carry no exploitation flag of their own, and its interim relief is blocking the network protocols an attack requires or, for attacks that need certain privileges or package access, removing those; patches exist only for versions under Premier or Extended Support, and Oracle says earlier versions are likely affected too ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)).

**Exposure:** Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools instances reachable over HTTP, whose Brotli rows are the KEV-listed CVE-2026-111497 ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)), and Access Manager, WebLogic Server, E-Business Suite, APEX or REST Data Services, Platform Security for Java and Business Intelligence Enterprise Edition instances on the listed versions that untrusted networks can reach over HTTP, HTTPS, SOAP, TCP, T3 or IIOP ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)).

**Defender takeaway:** patch Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools first, since their Brotli rows are the KEV-listed CVE-2026-111497, then internet-reachable identity, middleware, ERP and APEX instances, and until then block the protocols a row needs, T3 and IIOP for the WebLogic Core row ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)). Oracle names no per-flaw workaround, so unsupported versions have no vendor fix.

## Correction — 2026-11-22T14:49:46Z

The headline and summary said none of the unauthenticated critical rows was exploited. Three of them, in Communications Diameter Signaling Router, Communications Unified Assurance and PeopleSoft PeopleTools, are the Brotli decoder flaw CVE-2026-111497 at 9.8 ([Oracle, 2026-11-17](https://www.oracle.com/security-alerts/cspunov2026.html)), which CISA has listed as exploited since 2026-10-27 ([CISA, 2026-11-17](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Oracle's matrices still mark no row as exploited, and no exploitation of the other rows is reported.
