---
schema: 1
kind: vulnerability
title: "FreeRADIUS before 3.0.29 and 3.2.11: a Critical use-after-free in the default-enabled EAP-TTLS module can be started by an unauthenticated user and code execution may be possible; 21 issues fixed in all, among them TEAP bugs that return Access-Accept to an unauthenticated peer; no exploitation stated and no proof of concept for the Critical flaw"
headline: "FreeRADIUS 3.2.11, 3.0.29: Critical unauthenticated use-after-free in default EAP-TTLS, TEAP bypasses; upgrade"
summary: >
  FreeRADIUS announced 3.0.29 and 3.2.11 on 2026-11-25; the project's page lists 21 fixed issues, one rated Critical: an unauthenticated use-after-free in the EAP-TTLS module, which is enabled in the default configuration and where code execution may be possible. Eight issues rated High sit mostly in modules the project says are off by default, and three Medium TEAP issues let an unauthenticated peer obtain an Access-Accept on 3.2.x; the project states no exploitation and no proof of concept for the Critical flaw. CERT-FR restated the release on 2026-11-27, and 3.0.29 is planned as the last 3.0 release.
discovered_at: "2026-11-28T04:57:00Z"
updated_at: null
event_date: "2026-11-25"
run_id: 2026-11-28T0355Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, auth-bypass, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:freeradius"]
techniques: [T1190]
affected_products: ["FreeRADIUS"]
cves: []
sources:
  - url: "https://freeradius.org/security/"
    publisher: "FreeRADIUS project (security notifications)"
    date: "2026-11-25"
    role: primary
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1632/"
    publisher: "CERT-FR (CERTFR-2026-AVI-1632)"
    date: "2026-11-27"
    role: corroborating
  - url: "https://github.com/FreeRADIUS/freeradius-server/releases/tag/release_3_0_29"
    publisher: "FreeRADIUS 3.0.29 release notes"
    date: "2026-11-26"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124536"
    publisher: "ENISA EUVD (CVE-2026-127030)"
    date: "2026-11-12"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124535"
    publisher: "ENISA EUVD (CVE-2026-127029)"
    date: "2026-11-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have released 3.0.29 and 3.2.11 to fix various overflows and memory leaks. We recommend that everyone using earlier versions of FreeRADIUS upgrade to one of these new releases."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "The TTLS module is enabled in the default configuration."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "An unauthenticated user could start an EAP-TTLS session, then send invalid “inner-tunnel” data. This could cause a “use after free” issue in the TTLS module."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "With heap shaping, an attacker can cause a write of a heap pointer to a chosen address. Code execution may be possible."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "TEAP is not enabled in the default configuration."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "We recommend keeping your RADIUS server on a management VLAN, and not exposed to the Internet. We recommend disabling all features which you are not using."
    publisher: "FreeRADIUS project"
    source_url: "https://freeradius.org/security/"
  - quote: "Some of them allow an attacker to cause remote arbitrary code execution, remote denial of service and a breach of data confidentiality."
    original: "Certaines d'entre elles permettent à un attaquant de provoquer une exécution de code arbitraire à distance, un déni de service à distance et une atteinte à la confidentialité des données."
    publisher: "CERT-FR"
    source_url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1632/"
verification: single-source
sourcing_note: >
  The FreeRADIUS project is the disclosing party for its own product and CERT-FR restates its release without adding an assessment. The project page prints no total, no CVE ids and no CVSS scores; the count of 21 issues and the severity split are read off the page. ENISA's database lists two Red Hat-assigned ids published on 2026-11-12, CVE-2026-127030 and CVE-2026-127029, whose records cite commits that the project lists among its fixes, but neither the project nor CERT-FR links an id to an issue, so no CVE record is carried here. CERT-FR's wording covers versions before 3.0.29 without saying that the TEAP and TOTP fixes are listed on 3.2.x only.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

FreeRADIUS announced 3.0.29 and 3.2.11 on its security page of 2026-11-25 (GitHub release pages: 2026-11-26), fixing various overflows and memory leaks, and recommends that everyone on earlier versions upgrade ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). The page lists 21 issues: one Critical, eight High, five Medium and seven Low ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). The Critical issue is a use-after-free in the TTLS module, which the project says is enabled in the default configuration: an unauthenticated user could start an EAP-TTLS session and send invalid inner-tunnel data, and with heap shaping an attacker can cause a write of a heap pointer to a chosen address, so code execution may be possible ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). The page states no exploitation and no proof of concept for this flaw, mentions a proof of concept that Ada Logics wrote for two High EAP-FAST issues, and says a system whose affected module is not enabled is not vulnerable to that module's issues ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)).

The High issues in DHCP, EAP-FAST, EAP-SIM and TEAP are in modules the project says are not enabled by default, among them an unauthenticated out-of-bounds write in the DHCP option encoder ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). Three Medium TEAP issues let an unauthenticated peer that starts a TEAP session obtain an Access-Accept, through skipped Basic-Password checks, a Crypto-Binding check missing in production builds and an unexpected Crypto-Binding TLV; their fixes are listed on 3.2.x only, and TEAP is off by default ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). CERT-FR restated the release on 2026-11-27, saying some of the flaws allow remote code execution, remote denial of service and a breach of data confidentiality (translated from French) ([CERT-FR, 2026-11-27](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1632/)). The project page lists no CVE ids; ENISA's database lists CVE-2026-127030, an EAP-FAST session-ticket stack overflow, and CVE-2026-127029, an EAP-SIM identity-length stack overflow, both published on 2026-11-12 and scored CVSS 3.1 7.5 for availability impact only ([ENISA EUVD, 2026-11-12](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124536); [ENISA EUVD, 2026-11-12](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-124535)).

**Exposure:** FreeRADIUS before 3.0.29 or 3.2.11 with the TTLS module enabled, as it is in the default configuration, for the Critical flaw; the project says EAP-TLS, TTLS and PEAP are enabled by default, and it states no default for the EAP-MSCHAPv2 module of a High issue, which a PEAP-only site should check; the issues in TEAP, EAP-FAST, EAP-SIM and DHCP apply only where those modules are enabled ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)). The project's standing advice on the same page, from its earlier 2026-06-01 announcement, is to keep the RADIUS server on a management VLAN and off the internet ([FreeRADIUS, 2026-11-25](https://freeradius.org/security/)).

**Detection:** radiusd crashes and restarts, as service-manager events or core dumps, that follow EAP-TTLS handshakes, and on servers with TEAP enabled, Access-Accept replies for TEAP sessions with no completed inner authentication in the authentication detail log; both follow from the mechanisms the project describes, which publishes no indicator. A heap-corruption attack may leave only a crash, so review radiusd restarts in the days before the upgrade.

**Defender takeaway:** upgrade to 3.2.11, or to 3.0.29 on a 3.0 server and then migrate, because the release notes call 3.0.29 the planned last 3.0 release and tell everyone to move to 3.2.11 or later ([FreeRADIUS 3.0.29, 2026-11-26](https://github.com/FreeRADIUS/freeradius-server/releases/tag/release_3_0_29)); check which EAP methods the server enables and switch off those in use by nobody, and keep the listener reachable only from network access servers and proxies. The Critical flaw sits in a method that is on by default, though no exploitation is stated.
