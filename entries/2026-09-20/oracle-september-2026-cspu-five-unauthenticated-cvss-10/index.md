---
schema: 1
kind: vulnerability
title: "Oracle's September 2026 Critical Security Patch Update carries fifty unauthenticated CVSS 9.8+ flaws, concentrated in Fusion Middleware's identity, forms, directory and portal components, plus E-Business Suite, Hyperion, Analytics, Enterprise Manager, Communications and Supply Chain products"
headline: "Fifty credential-free, no-interaction flaws span Oracle's middleware, ERP, BI and telco-assurance lines in an off-quarter patch release"
summary: >
  Oracle's September 2026 Critical Security Patch Update, published 2026-09-15, carries 673 patches of which
  153 are for Fusion Middleware, and Oracle states 78 of those may be exploited over a network without
  credentials. Oracle's own risk matrix lists fifty CVEs at CVSS 9.8-10.0 that are network-reachable without privileges or user interaction and marked remotely exploitable without authentication. Six are CVSS 10.0 flaws in WebLogic Server,
  Access Manager, Forms, Internet Directory, Platform Security for Java and Hyperion Financial Management, and forty-four are CVSS 9.8 flaws across Fusion Middleware (Access Manager,
  Forms, Internet Directory and Platform Security for Java again, plus Data Integrator, Identity Manager,
  JDeveloper, WebCenter Enterprise Capture/Portal/Sites, WebLogic Server and Service Delivery Platform) and other product lines: E-Business Suite, Hyperion Financial Management, Business Intelligence/BI Publisher, Enterprise Manager,
  Communications Unified Assurance and Product Lifecycle Analytics. No exploitation is reported for any of the
  fifty. The release is Oracle's off-quarter patch line, which a calendar built only on the quarterly dates
  will miss.
discovered_at: "2026-09-20T13:38:16Z"
updated_at: "2026-09-29T04:40:00Z"
event_date: "2026-09-15"
run_id: 2026-09-20T1308Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, patch-available, identity]
regions: [global, europe, switzerland]
sectors: [public-sector, finance, healthcare, energy]
entities: []
techniques: [T1190]
affected_products: ["Oracle WebLogic Server", "Oracle Access Manager", "Oracle Forms", "Oracle Internet Directory", "Oracle Platform Security for Java", "Oracle Hyperion Financial Management", "Oracle Fusion Middleware", "Oracle E-Business Suite", "Oracle Business Intelligence Enterprise Edition", "Oracle BI Publisher", "Oracle Enterprise Manager Base Platform", "Oracle Enterprise Manager for Fusion Middleware", "Oracle Communications Unified Assurance", "Oracle Data Integrator", "Oracle Identity Manager", "Oracle JDeveloper", "Oracle WebCenter Enterprise Capture", "Oracle WebCenter Portal", "Oracle WebCenter Sites", "Oracle Service Delivery Platform", "Oracle Product Lifecycle Analytics"]
cves:
  - id: CVE-2026-83021
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, Web Container component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-71133
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83099
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83059
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83020
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Platform Security for Java 12.2.1.4.0, 14.1.2.0.0, centralized third-party jars component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-87230
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Financial Management 11.2.26.0.000, Security component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83327
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3-12.2.15, Applications Framework / Personalization component, reachable over SOAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83452
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3-12.2.15, Document Management and Collaboration / Internal Operations component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83462
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3-12.2.15, Mobile Application Server / MWA Terminal Server component, reachable over TCP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83283
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Business Intelligence Enterprise Edition 12.2.1.4.0, Platform Security component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-41635
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Enterprise Manager Base Platform 13.5 / 24.1, Agent Next Gen (Apache Mina) component, reachable over HTTP; the same patch also addresses CVE-2026-41409 and CVE-2026-42779"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83355
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Enterprise Manager for Fusion Middleware 13.5 / 24.1, Metrics component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-44024
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Communications Unified Assurance 6.1.1-7.0.0, Core/Fluentd component, reachable over HTTP; the same patch also addresses CVE-2026-44025, CVE-2026-44160 and CVE-2026-44161"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-17544
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Communications Unified Assurance 7.0.0, Core/PHP component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73950
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73947
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.0.0, Authentication Engine component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73940
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over T3/IIOP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-47065
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Third Party (Apache Mina) component, reachable over TCP/IP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83232
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Data Integrator 12.2.1.4.0, 14.1.2.0.0, Console / Repository Explorer component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83094
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83095
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83098
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83100
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83108
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-70913
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Identity Manager 12.2.1.4.0, 14.1.2.1.0, Core component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83042
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Identity Manager 12.2.1.4.0, 14.1.2.1.0, OIM Legacy UI component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83054
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83060
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83061
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83062
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83066
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over T3/IIOP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73961
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle JDeveloper 12.2.1.4.0, 14.1.2.0.0, ADF Faces component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-82994
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Platform Security for Java 12.2.1.4.0, 14.1.2.0.0, centralized third-party jars component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-82995
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Platform Security for Java 12.2.1.4.0, 14.1.2.0.0, centralized third-party jars component, reachable over SOAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83339
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Enterprise Capture 12.2.1.4.0, 14.1.2.0.0, Client Bundle component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73956
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Portal 12.2.1.4.0, 14.1.2.0.0, Composer component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73953
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Portal 12.2.1.4.0, 14.1.2.0.0, Portlet Services component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-73963
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Portal 12.2.1.4.0, 14.1.2.0.0, Portlet Services component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83035
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Sites 12.2.1.4.0, 14.1.2.0.0, WebCenter Sites component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83036
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Sites 12.2.1.4.0, 14.1.2.0.0, WebCenter Sites component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83037
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebCenter Sites 12.2.1.4.0, 14.1.2.0.0, WebCenter Sites component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-70756
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, Core component, reachable over T3/IIOP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-70757
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, Core component, reachable over T3/IIOP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-70748
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0, Core component, reachable over T3/IIOP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83000
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Service Delivery Platform 12.2.1.4.0, 14.1.2.0.0, Messaging Enabler component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83151
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Service Delivery Platform 12.2.1.4.0, 14.1.2.0.0, Messaging Enabler component, reachable over SOAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83269
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle BI Publisher 8.2.0.0.0, 12.2.1.4.0, 26.01.0.0.0, BI Platform Security component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-87188
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Financial Management 11.2.26.0.000, Security component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-87184
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Financial Management 11.2.26.0.000, Security component, reachable over SQL"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83261
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Product Lifecycle Analytics 3.6.1, Core component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
sources:
  - url: "https://www.oracle.com/security-alerts/cspusep2026.html"
    publisher: "Oracle"
    date: "2026-09-15"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0372"
    publisher: "NCSC-NL"
    date: "2026-09-16"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/"
    publisher: "BleepingComputer"
    date: "2026-08-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This Critical Security Patch Update contains 153 new security patches for Oracle Fusion Middleware."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspusep2026.html"
  - quote: "78 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspusep2026.html"
  - quote: "A Critical Security Patch Update (CSPU) provides targeted, high-priority security fixes in a smaller, more focused format, making them easier to apply with minimal disruption."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspusep2026.html"
  - quote: "This Critical Security Patch Update contains 159 new security patches for Oracle E-Business Suite.  19 of these vulnerabilities may be remotely exploitable without authentication"
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cspusep2026.html"
verification: single-source
sourcing_note: >
  Oracle is the primary disclosing party for its own products and the origin of every score and
  version string here. All fifty flaws come from its own risk matrix. NCSC-NL relayed the release's
  153 Fusion Middleware fixes with high likelihood and damage ratings, a second severity assessment
  rather than independent confirmation of the facts. No exploitation reporting or KEV listing exists
  for any of the fifty.
confidence: high
references:
  - "2026-08-20/oracle-august-2026-cpu-three-unauthenticated-cvss-10"
  - "2026-06-18/cve-2026-46978-cve-2026-35278-oracle-june-2026-cspu-unauthen"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Apply Oracle's September 2026 Critical Security Patch Update now to every affected Fusion Middleware, Hyperion Financial Management, Analytics, Enterprise Manager, Communications Unified Assurance and Product Lifecycle Analytics deployment. It is an off-quarter release that a quarterly patch calendar does not schedule."
  - "Patch Oracle E-Business Suite 12.2.3-12.2.15 for CVE-2026-83327, CVE-2026-83452 and CVE-2026-83462 in this same release now: Cl0p exploited an earlier Oracle EBS zero-day from August 2025 to steal files from many organizations, and these three flaws need no credential and no user interaction."
updates:
  - at: "2026-09-29T04:40:00Z"
    run_id: 2026-09-29T0405Z-intel
    type: update
    summary: >
      A systematic, full re-verification against Oracle's own September 2026 risk matrix (every row with
      Access Vector Network, Privileges Required None, User Interaction None and "Remote Exploit without
      Auth." Yes) finds forty-four further unauthenticated CVSS 9.8 flaws from the same release, not the
      eight this entry first reported: thirty-two further flaws inside the Fusion Middleware product line
      (Access Manager, Forms, Internet Directory and Platform Security for Java, all previously covered only
      by their single CVSS 10.0 flaw, plus first coverage of Data Integrator, Identity Manager, JDeveloper,
      WebCenter Enterprise Capture, WebCenter Portal, WebCenter Sites, WebLogic Server and Service Delivery
      Platform), three in Oracle E-Business Suite (Applications Framework, Document Management, Mobile
      Application Server), one in Business Intelligence Enterprise Edition plus one in BI Publisher, two more
      in Hyperion Financial Management, two in Enterprise Manager, two in Communications Unified Assurance,
      and one in Product Lifecycle Analytics. Total across the release: fifty, not fourteen. None is reported
      exploited and none is CISA KEV-listed. E-Business Suite remains the highest-priority addition given its
      history as Cl0p's 2025 mass-exploitation target, but the largest share of the exposure by far is inside
      Fusion Middleware's identity, forms, directory and portal components.
    fields: [title, headline, summary, affected_products, cves, evidence, sourcing_note, actions, body]
  - at: "2026-09-30T06:57:52Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The headline, summary, main text and one action now state the release-wide figure of fifty
      unauthenticated CVSS 9.8-10.0 flaws instead of framing the release around six, and the
      2026-09-29 section no longer narrates the counting pass (its tally of flaws outside Fusion
      Middleware is corrected from three to four). An unsupported authentication-bypass class is
      removed from all fifty flaws and the tags, as are a triage line and a takeaway clause that
      assumed an undisclosed mechanism and an unsourced claim about Oracle's advisory practice. The
      release schedule now follows Oracle's monthly calendar, NCSC-NL's scope and ratings are stated
      as published, the 2025 E-Business Suite campaign is sourced to Cl0p alone, two actions that
      restated the takeaway are trimmed, the sourcing note is plain provenance and the verification
      flag is single-source. Priority is lowered to notable because no flaw is exploited and the
      release is Oracle's regular monthly cycle. The count of Fusion Middleware components with a
      CVSS 10.0 flaw is corrected from four to five.
    fields: [headline, summary, actions, body, sourcing_note, tags, cves, verification, sources, priority]
migrated_from: null
---

Oracle published its September 2026 Critical Security Patch Update on 2026-09-15 (Rev 1, initial release) with 673 new security patches across its product families; Oracle Fusion Middleware alone accounts for 153 of them, and Oracle states that "78 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials" ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Six flaws in the release carry a CVSS 3.1 base score of 10.0 in Oracle's own risk matrix with Attack Vector Network, Attack Complexity Low, Privileges Required None, User Interaction None and Scope Changed, meaning an unauthenticated request across the network reaches high confidentiality and integrity impact and crosses a security boundary (the first five also reach high availability impact; Hyperion Financial Management's is rated none): CVE-2026-83021 in the Web Container of Oracle WebLogic Server over HTTP, CVE-2026-71133 in the Authentication Engine of Oracle Access Manager over HTTP, CVE-2026-83099 in Oracle Forms Services over HTTP, CVE-2026-83059 in the OID LDAP Server of Oracle Internet Directory over LDAP, CVE-2026-83020 in the centralized third-party jars of Oracle Platform Security for Java over HTTP, and CVE-2026-87230 in the Security component of Oracle Hyperion Financial Management over HTTP ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). The Netherlands' national cyber-security centre relayed the release's 153 Fusion Middleware fixes as advisory NCSC-2026-0372 on 2026-09-16 and rated both likelihood and damage high ([NCSC-NL, 2026-09-16](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0372)).

The Critical Security Patch Update is Oracle's second, higher-frequency release line, published alongside the quarterly cumulative Critical Patch Update rather than replacing it: Oracle describes it as providing "targeted, high-priority security fixes in a smaller, more focused format, making them easier to apply with minimal disruption" and says these updates "complement Oracle’s existing quarterly cumulative Critical Patch Updates (CPUs)" ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Oracle now releases security patches on the third Tuesday of each month. Its next four dates are the Critical Patch Update of 20 October 2026, Critical Security Patch Updates on 17 November and 15 December 2026, and the Critical Patch Update of 19 January 2027 ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). A patch calendar built only on the quarterly dates misses the releases in between.

Oracle discloses no exploitation technique, no proof-of-concept status and no in-the-wild activity for any of the fifty unauthenticated flaws, and no source names an exploited flaw ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). What forces the timeline is the shape of the flaws: every one is reachable by an unauthenticated network request with no user interaction ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). The six rated CVSS 10.0 sit in components that front other systems or hold what they rely on: WebLogic's web container, Access Manager's authentication engine, an Internet Directory LDAP listener, Forms Services, the shared Java security jars underneath Fusion Middleware, and Hyperion Financial Management's security component ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Where an organization runs its single sign-on, directory or application-server tier on these Fusion Middleware components, a Scope Changed rating on an authentication engine means the compromise does not stay inside the component that carries the flaw. 

**Defender takeaway:** inventory by component rather than by suite name. The affected version strings in Oracle's matrix are narrow and specific, 12.2.1.4.0 and 14.1.1.0.0/14.1.2.0.0 for WebLogic's web container, 12.2.1.4.0 and 14.1.2.1.0 for Access Manager and Internet Directory, 12.2.1.19.0 and 14.1.2.0.0 for Forms, so an estate that tracks only "Fusion Middleware 14c" cannot tell from its own inventory whether it is affected. Until the patch lands, the reachable-surface question is which of these listeners answer from outside the management network at all: an OID LDAP server or a WebLogic web container exposed beyond an administrative segment is the exposure to close first, because these flaws need no credentials and no user interaction ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)).

## Update — 2026-09-29T04:40:00Z

Oracle's September 2026 risk matrix lists eight further unauthenticated CVSS 9.8 flaws (Attack Vector Network, Privileges Required None, User Interaction None) beyond the six CVSS 10.0 flaws, across four further product families
([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Oracle E-Business Suite carries
159 new patches, of which 19 are remotely exploitable without authentication: "This Critical Security Patch
Update contains 159 new security patches for Oracle E-Business Suite. 19 of these vulnerabilities may be
remotely exploitable without authentication"
([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Three of those nineteen reach
CVSS 9.8 with no further precondition: CVE-2026-83327 in the Applications Framework's Personalization component
over SOAP, CVE-2026-83452 in Document Management and Collaboration's Internal Operations component over HTTP,
and CVE-2026-83462 in the Mobile Application Server's MWA Terminal Server component over TCP, all affecting
versions 12.2.3 through 12.2.15. Oracle Business Intelligence Enterprise Edition (Oracle Analytics, 50 new
patches, 8 unauthenticated) carries CVE-2026-83283 in its Platform Security component (version 12.2.1.4.0, over
HTTP). Oracle Enterprise Manager carries CVE-2026-41635 (Agent Next Gen / Apache Mina component, versions
13.5/24.1, over HTTP, the same patch also fixing CVE-2026-41409 and CVE-2026-42779) and CVE-2026-83355
(Enterprise Manager for Fusion Middleware's Metrics component, same versions). Oracle Communications (31 new
patches, 23 unauthenticated) carries CVE-2026-44024 (Unified Assurance's Core/Fluentd component, versions
6.1.1-7.0.0, the same patch also fixing CVE-2026-44025, CVE-2026-44160 and CVE-2026-44161) and CVE-2026-17544
(Unified Assurance's Core/PHP component, version 7.0.0).

On the same bar (Access Vector Network, Privileges Required None, User Interaction None, "Remote Exploit without Auth." Yes), the matrix lists thirty-two further CVSS 9.8 flaws inside the Fusion Middleware product line, beyond the single CVSS 10.0 flaw in each of five of its components. Access Manager carries four more (CVE-2026-73950, CVE-2026-73947, CVE-2026-73940,
CVE-2026-47065, the Authentication Engine and a Third Party/Apache Mina component, over HTTP or T3/IIOP or
TCP/IP). Forms carries five more (CVE-2026-83094, -83095, -83098, -83100, -83108, all in Forms Services/C-S/
Charmode over HTTP). Internet Directory carries five more (CVE-2026-83054, -83060, -83061, -83062, -83066, the
OID LDAP Server over LDAP or T3/IIOP). Platform Security for Java carries two more (CVE-2026-82994 over LDAP,
CVE-2026-82995 over SOAP, both in the centralized third-party jars). WebLogic Server carries three more
(CVE-2026-70756, -70757, -70748, its Core component over T3/IIOP). The remaining thirteen are in other Fusion Middleware components: Data Integrator (CVE-2026-83232, Console/
Repository Explorer, HTTP), Identity Manager (CVE-2026-70913 Core and CVE-2026-83042 OIM Legacy UI, both HTTP),
JDeveloper (CVE-2026-73961, ADF Faces, HTTP), WebCenter Enterprise Capture (CVE-2026-83339, Client Bundle,
HTTP), WebCenter Portal (CVE-2026-73956 Composer and CVE-2026-73953/-73963 Portlet Services, all HTTP),
WebCenter Sites (CVE-2026-83035, -83036, -83037, HTTP) and Service Delivery Platform (CVE-2026-83000 and
-83151, Messaging Enabler, over HTTP or SOAP) ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)).
Outside Fusion Middleware there are four more: two further Hyperion Financial Management flaws
(CVE-2026-87188 over HTTP, CVE-2026-87184 over SQL, alongside the original CVE-2026-87230), one more in Oracle
Analytics (CVE-2026-83269 in BI Publisher's BI Platform Security component, over HTTP, alongside CVE-2026-83283
in Business Intelligence Enterprise Edition), and one in Oracle Supply Chain's Product Lifecycle Analytics (CVE-2026-83261, Core component, HTTP). The total for the release is fifty unauthenticated CVSS 9.8-10.0 flaws.

None of the fifty is reported exploited by Oracle or any other source, and none appears in the CISA Known
Exploited Vulnerabilities catalog. Oracle E-Business Suite deserves early patching despite the absence of exploitation reporting: Cl0p exploited an earlier Oracle EBS zero-day from early August 2025 to steal files from many organizations ([BleepingComputer, 2026-08-17](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)), and an estate running EBS 12.2.3-12.2.15 should treat
its three unauthenticated flaws as an extension of that same exposure class rather than a routine patch-cycle
item. By count, the exposure is dominated by Fusion Middleware: Access Manager, Forms and Internet
Directory alone carry five to six unauthenticated CVSS 9.8-10.0 flaws each, and an estate that patched only the
six CVSS 10.0 components has patched a small fraction of what this release actually
contains.

## Correction — 2026-09-30T06:57:52Z

Oracle's risk matrix lists fifty unauthenticated, no-interaction flaws at CVSS 9.8 to 10.0 in this release, not six, and none is reported exploited ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Oracle gives no vulnerability class for any of them, so the earlier authentication-bypass label and the triage guidance that assumed an exploitation mechanism are withdrawn. Oracle now patches monthly, and its next releases are the Critical Patch Update of 20 October 2026 and Critical Security Patch Updates on 17 November and 15 December 2026 ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). NCSC-NL relayed the 153 Fusion Middleware fixes and rated likelihood and damage high ([NCSC-NL, 2026-09-16](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0372)). The 2025 E-Business Suite campaign was Cl0p's exploitation of an earlier zero-day ([BleepingComputer, 2026-08-17](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)).
