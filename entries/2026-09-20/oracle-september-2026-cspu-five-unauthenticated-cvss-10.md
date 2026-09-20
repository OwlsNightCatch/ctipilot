---
schema: 1
kind: vulnerability
title: "Oracle's September 2026 Critical Security Patch Update carries six unauthenticated CVSS 10.0 flaws across WebLogic Server, Access Manager, Forms, Internet Directory, Platform Security for Java and Hyperion Financial Management"
headline: "Six CVSS 10.0 flaws needing no credential and no user interaction, in the middleware tier that fronts everything else"
summary: >
  Oracle's September 2026 Critical Security Patch Update, published 2026-09-15, carries 673 patches of which
  153 are for Fusion Middleware, and Oracle states 78 of those may be exploited over a network without
  credentials. Six carry CVSS 3.1 10.0 with Privileges Required and User Interaction both None in Oracle's
  own risk matrix: CVE-2026-83021 (WebLogic Server Web Container), CVE-2026-71133 (Access Manager
  Authentication Engine), CVE-2026-83099 (Forms Services), CVE-2026-83059 (Internet Directory OID LDAP
  Server), CVE-2026-83020 (Platform Security for Java) and CVE-2026-87230 (Hyperion Financial Management).
  No exploitation is reported. The release is Oracle's off-quarter patch line, which a calendar built only
  on the quarterly dates will miss.
discovered_at: "2026-09-20T13:38:16Z"
updated_at: null
event_date: "2026-09-15"
run_id: 2026-09-20T1308Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, auth-bypass, patch-available, identity]
regions: [global, europe, switzerland]
sectors: [public-sector, finance, healthcare, energy]
entities: []
techniques: [T1190]
affected_products: ["Oracle WebLogic Server", "Oracle Access Manager", "Oracle Forms", "Oracle Internet Directory", "Oracle Platform Security for Java", "Oracle Hyperion Financial Management", "Oracle Fusion Middleware"]
cves:
  - id: CVE-2026-83021
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, Web Container component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-71133
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0, 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83099
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Forms 12.2.1.19.0, 14.1.2.0.0, Forms Services / C-S / Charmode component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83059
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Internet Directory 12.2.1.4.0, 14.1.2.1.0, OID LDAP Server component, reachable over LDAP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-83020
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Platform Security for Java 12.2.1.4.0, 14.1.2.0.0, centralized third-party jars component, reachable over HTTP"
    fixed: "September 2026 Critical Security Patch Update"
  - id: CVE-2026-87230
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Hyperion Financial Management 11.2.26.0.000, Security component, reachable over HTTP"
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
verification: multi-source
sourcing_note: >
  Oracle is the primary disclosing party for its own products and is the origin of every score and version
  string here. NCSC-NL republished the Fusion Middleware half of the release as its own advisory and assigned
  it a high priority, which is a second assessment of severity rather than an independent assessment of the
  underlying facts. Recovered by the 2026-09-20 quality audit's coverage
  re-sweep after the release passed the window's intel runs unremarked.
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
  - "Check every Oracle Fusion Middleware and Hyperion deployment against the affected component version strings (WebLogic Server 12.2.1.4.0 / 14.1.1.0.0 / 14.1.2.0.0; Access Manager and Internet Directory 12.2.1.4.0 / 14.1.2.1.0; Forms 12.2.1.19.0 / 14.1.2.0.0; Platform Security for Java 12.2.1.4.0 / 14.1.2.0.0; Hyperion Financial Management 11.2.26.0.000) and apply the September 2026 Critical Security Patch Update, which is an off-quarter release a January/April/July/October patch calendar does not schedule."
  - "Confirm that no Oracle Internet Directory LDAP listener, WebLogic web container or Access Manager authentication endpoint answers from outside its administrative network segment; all six flaws need no credential and no user interaction, so reachability is the whole of the exposure."
updates: []
migrated_from: null
---

Oracle published its September 2026 Critical Security Patch Update on 2026-09-15 (Rev 1, initial release) with 673 new security patches across its product families; Oracle Fusion Middleware alone accounts for 153 of them, and Oracle states that "78 of these vulnerabilities may be remotely exploitable without authentication, i.e., may be exploited over a network without requiring user credentials" ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). Six flaws in the release carry a CVSS 3.1 base score of 10.0 in Oracle's own risk matrix with Attack Vector Network, Attack Complexity Low, Privileges Required None, User Interaction None and Scope Changed, meaning an unauthenticated request across the network reaches high confidentiality and integrity impact and crosses a security boundary (the first five also reach high availability impact; Hyperion Financial Management's is rated none): CVE-2026-83021 in the Web Container of Oracle WebLogic Server over HTTP, CVE-2026-71133 in the Authentication Engine of Oracle Access Manager over HTTP, CVE-2026-83099 in Oracle Forms Services over HTTP, CVE-2026-83059 in the OID LDAP Server of Oracle Internet Directory over LDAP, CVE-2026-83020 in the centralized third-party jars of Oracle Platform Security for Java over HTTP, and CVE-2026-87230 in the Security component of Oracle Hyperion Financial Management over HTTP ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). The Netherlands' national cyber-security centre relayed the Fusion Middleware half of the release as advisory NCSC-2026-0372 on 2026-09-16 and assigned it priority "Hoog", its high rating ([NCSC-NL, 2026-09-16](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0372)).

The Critical Security Patch Update is Oracle's second, higher-frequency release line, published alongside the quarterly cumulative Critical Patch Update rather than replacing it: Oracle describes it as providing "targeted, high-priority security fixes in a smaller, more focused format, making them easier to apply with minimal disruption" and says these updates "complement Oracle’s existing quarterly cumulative Critical Patch Updates (CPUs)" ([Oracle, 2026-09-15](https://www.oracle.com/security-alerts/cspusep2026.html)). A patch calendar built only around the January, April, July and October quarterly dates therefore leaves the September release, and the four other off-quarter releases in the year, unscheduled.

Oracle discloses no exploitation technique, no proof-of-concept status and no in-the-wild activity for any of the six, which is its standing advisory practice; no source in this release names an exploited flaw. What forces the timeline is the shape of the flaws rather than an exploitation report. Each of the six is reachable by an unauthenticated network request against a component that exists to sit in front of other systems or to hold what they rely on: WebLogic's web container, Access Manager's authentication engine, an Internet Directory LDAP listener, Forms Services, the shared Java security jars underneath Fusion Middleware, and Hyperion Financial Management's own security component. Five of them are the single-sign-on, directory and application-server tiers that Swiss federal, cantonal and communal estates run legacy identity services on, and a Scope Changed rating on an authentication engine means the compromise does not stay inside the component that carries the flaw. The sixth sits elsewhere: Hyperion Financial Management is a financial-consolidation application from Oracle's separate Hyperion family, so it is the finance estate rather than the identity estate that needs checking for it.

**Defender takeaway:** inventory by component rather than by suite name. The affected version strings in Oracle's matrix are narrow and specific, 12.2.1.4.0 and 14.1.1.0.0/14.1.2.0.0 for WebLogic's web container, 12.2.1.4.0 and 14.1.2.1.0 for Access Manager and Internet Directory, 12.2.1.19.0 and 14.1.2.0.0 for Forms, so an estate that tracks only "Fusion Middleware 14c" cannot tell from its own inventory whether it is affected. Until the patch lands, the reachable-surface question is which of these listeners answer from outside the management network at all: an OID LDAP server or a WebLogic web container exposed beyond an administrative segment is the exposure that turns a Privileges Required None flaw into a single-request compromise.

**Triage:** exploitation of these components produces authentication and application-tier telemetry, not endpoint telemetry. On the identity tier, look for successful authorization decisions from Access Manager with no preceding credential-validation event, and for LDAP binds or searches against the OID listener from source ranges that no application integration uses. On the application tier, look for requests to WebLogic or Forms endpoints that return successfully without a prior session-establishment request in the same log sequence. Ordinary integrations and health checks produce the same request types, so the discriminator is the missing predecessor event, not the request itself.
