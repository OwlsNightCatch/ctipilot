---
schema: 1
kind: vulnerability
title: "Oracle July 2026 CPU — nine unauthenticated CVSS 10.0 flaws in Fusion Middleware, with NCSC-NL assessing large-scale abuse as very likely in the short term"
headline: "Two national CERTs escalated the July Oracle cycle: 219 of the Fusion Middleware fixes need no authentication at all"
summary: >
  Oracle's July 2026 Critical Patch Update carries 1,449 patches, of which Fusion Middleware
  alone accounts for 355 — 219 of them remotely exploitable without authentication and nine
  distinct CVEs at CVSS 10.0, each reachable over a standard network protocol with no
  credentials. NCSC-NL (NCSC-2026-0252) and CERT-FR (CERTFR-2026-AVI-0920) both issued advisories
  inside this window, with NCSC-NL assessing that large-scale abuse in the short term is very
  likely. No exploitation of the new CVEs is confirmed; the CVSS-10.0 set includes Oracle Data
  Integrator (CVE-2026-47056) and Oracle Coherence (CVE-2026-60217), and the exposure that
  matters is internet-reachable Fusion Middleware rather than the patch count.
discovered_at: "2026-07-26T14:11:00Z"
event_date: "2026-07-22"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [europe, global]
sectors: [public-sector, finance]
entities: []
techniques: [T1190]
affected_products: ["Oracle Fusion Middleware", "Oracle Data Integrator", "Oracle Coherence", "Oracle Database Server"]
cves:
  - id: CVE-2026-47056
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Data Integrator 12.2.1.4.0 and 14.1.2.0.0 (Rest Service component, per Oracle's risk matrix)"
    fixed: "July 2026 Critical Patch Update"
  - id: CVE-2026-60217
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Coherence Core 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0 (per Oracle's risk matrix)"
    fixed: "July 2026 Critical Patch Update"
  - id: CVE-2026-61211
    cvss: "9.9"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Oracle Database Server (DBMS_CLOUD) — see the July 2026 CPU matrix"
    fixed: "July 2026 Critical Patch Update"
sources:
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252"
    publisher: "NCSC-NL"
    date: "2026-07-22"
    role: primary
  - url: "https://www.oracle.com/security-alerts/cpujul2026.html"
    publisher: "Oracle"
    date: "2026-07-16"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0920/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-07-23"
    role: corroborating
  - url: "https://www.csoonline.com/article/4200184/oracles-july-update-fixes-ten-10-0-vulnerabilities-in-fusion-middleware.html"
    publisher: "CSOonline"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Door het grote aantal en de ernst van deze kwetsbaarheden acht het NCSC het zeer waarschijnlijk dat grootschalig misbruik op korte termijn plaats gaat vinden."
    publisher: "NCSC-NL (NCSC-2026-0252)"
  - quote: "Fusion Middleware was particularly hard hit, with new security patches for 355 security vulnerabilities, 219 of them remotely exploitable without authentication, meaning they can be exploited over a network without requiring user credentials."
    publisher: "CSOonline"
verification: multi-source
sourcing_note: "Oracle's advisory page predates the window (last updated 2026-07-16); the in-window anchors are the NCSC-NL and CERT-FR advisories of 2026-07-22 and 2026-07-23. Affected-version strings, component names and the CVE-to-product pairing all come from Oracle's own risk matrix, not from NCSC-NL: that advisory lists CVE ids with scores in one section and products in a separate flat list, and gives no version ranges. Two figures diverge between the sources and both are stated in the body: NCSC-NL counts nine CVEs at CVSS 10.0 and a total of 345 Fusion Middleware fixes, while Oracle's matrix shows ten rows at 10.0 (CVE-2026-60365 appears twice, under two components) against a total of 355. Individual CVEs beyond the three listed are not enumerated here because no per-CVE authority page was read for them."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Identify which Oracle Fusion Middleware components in your estate are reachable from the internet — Access Manager, HTTP Server, Platform Security for Java, WebCenter Content, Service Delivery Platform, Unified Directory, the WebLogic Server Proxy Plug-in, Data Integrator and Coherence are the nine families carrying them — and schedule those out of the normal quarterly cycle; unauthenticated network-reachable means an exposed instance needs no credential compromise first."
migrated_from: null
---

Oracle's quarterly Critical Patch Update is normally exactly what the routine patch cycle exists to absorb, and most of the July 2026 release is. What separates this one is a concentration that two national CERTs judged worth their own advisories inside the following week. On Oracle's own account, "This Critical Patch Update contains 355 new security patches , plus additional third party patches noted below, for Oracle Fusion Middleware. 219 of these vulnerabilities may be remotely exploitable without authentication" ([Oracle, 2026-07-16](https://www.oracle.com/security-alerts/cpujul2026.html)); CSOonline reports the same split, noting that "Fusion Middleware was particularly hard hit, with new security patches for 355 security vulnerabilities, 219 of them remotely exploitable without authentication, meaning they can be exploited over a network without requiring user credentials" ([CSOonline, 2026-07-22](https://www.csoonline.com/article/4200184/oracles-july-update-fixes-ten-10-0-vulnerabilities-in-fusion-middleware.html)).

**Two counts differ between the sources, and the difference is worth knowing before you brief anyone.** NCSC-NL states that the most severe vulnerabilities, nine of them, received the highest score of 10.0 ([NCSC-NL, 2026-07-22](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252)), while press coverage says ten. Both are right about their own object: Oracle's Fusion Middleware risk matrix carries ten *rows* at base score 10.0 but only nine distinct CVE identifiers, because CVE-2026-60365 appears twice — once under Oracle HTTP Server and once under the WebLogic Server Proxy Plug-in ([Oracle, 2026-07-16](https://www.oracle.com/security-alerts/cpujul2026.html)). NCSC-NL's total for the component also differs from Oracle's, 345 fixes against Oracle's 355. Nine distinct maximum-severity CVEs is the figure to use.

Each of the nine is reachable over a standard network protocol — HTTP, LDAP, SOAP, or raw TCP in Oracle Coherence's case — with no authentication and no user interaction. NCSC-NL's advisory lists the maximum-severity CVE identifiers, among them CVE-2026-47056 and CVE-2026-60217 ([NCSC-NL, 2026-07-22](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252)); it does not itself pair those identifiers with products, so the pairing, the component names and the affected versions all come from Oracle's risk matrix rather than the advisory — Data Integrator 12.2.1.4.0 and 14.1.2.0.0 in the Rest Service component, and Coherence Core 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0 ([Oracle, 2026-07-16](https://www.oracle.com/security-alerts/cpujul2026.html)). The remaining maximum-severity cases sit across Oracle Access Manager, HTTP Server, Platform Security for Java, WebCenter Content, Service Delivery Platform, Unified Directory and the WebLogic Server Proxy Plug-in. On the database side CVE-2026-61211 (CVSS 9.9) abuses DBMS_CLOUD to reach full server control, though that one is post-authentication.

The escalation is the CERT assessment rather than any observed activity. NCSC-NL's advisory states that "Because of the large number and the severity of these vulnerabilities, the NCSC considers it very likely that large-scale abuse will take place in the short term" ([NCSC-NL, 2026-07-22](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252)), and CERT-FR published its own advisory the following day ([CERT-FR, 2026-07-23](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0920/)). To be precise about what is and is not known: there is no confirmed in-the-wild exploitation of any of the new CVEs, no public proof-of-concept code, and no reported scanning specific to them. This is a forward-looking assessment by two national authorities about an exposure class with a long history of rapid weaponisation, not a report of an active campaign.

**Defender takeaway:** the actionable content is exposure triage, not the patch count. The set of components carrying the nine unauthenticated CVSS-10.0 fixes is small and specific, and the question for each is binary — is an instance reachable from an untrusted network. Oracle Access Manager and the WebLogic proxy plug-in in particular sit at the front door of many public-sector identity and portal deployments, which is precisely the placement that turns a pre-authentication middleware flaw into an initial-access route. Instances behind internal network boundaries can follow the ordinary quarterly cadence; internet-reachable ones should not wait for it.

**Triage:** with no public exploit detail there is no behavioural signature specific to these CVEs, and inventing one would be guesswork. What is available is exposure telemetry: enumerate which Fusion Middleware listeners answer from outside the perimeter, and in web-server and application logs for those hosts, treat unauthenticated requests to administrative or REST service paths from unfamiliar source ranges as the class worth reviewing while patching proceeds. Note that Coherence's cluster protocol is raw TCP rather than HTTP, so HTTP-layer inspection will not see it — that exposure has to be established from network policy rather than from application logs.
