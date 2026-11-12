---
schema: 1
kind: vulnerability
title: "Fortinet coordinated security hardening release: the advisories published on 2026-11-10 carry unauthenticated FortiMail, FortiAnalyzer, FortiManager, FortiOS and FortiAuthenticator flaws rated CVSS up to 9.8; FortiAnalyzer and FortiManager 8.0 have no fixed build for the JSON API flaw, FortiOS 7.0 and FortiMail 7.2 are left out of the October fixes"
headline: "Fortinet advisories: FortiAnalyzer and FortiManager 8.0 have no fix for a 9.8 JSON API flaw; FortiMail RCE rows too"
summary: >
  Fortinet's coordinated hardening release of 2026-10-22 fixed critical and high-severity flaws in FortiOS, FortiManager, FortiAnalyzer, FortiMail and FortiAuthenticator, and the advisories withheld until Patch Tuesday were published on 2026-11-10 with critical rows in FortiMail (unauthenticated code execution, SQL injection and IBE account takeover, CVSS up to 9.8), FortiAnalyzer and FortiManager (an unauthenticated JSON API flaw at 9.8, oftp port flaws, FGFM code execution), FortiOS, FortiAuthenticator and FortiClient. The October builds fix most rows, but FortiAnalyzer and FortiManager 8.0.0 through 8.0.2 have no fixed build for CVE-2026-126170 until the upcoming 8.0.3 (workaround: set rpc-permit none), and FortiOS 7.0, FortiMail 7.2 and FortiAnalyzer and FortiManager 7.2 and 7.0 are left to migrate or wait; none of the 2026-11-10 advisories states exploitation.
discovered_at: "2026-10-23T03:38:30Z"
updated_at: "2026-11-12T04:20:00Z"
event_date: "2026-10-22"
run_id: 2026-10-23T0256Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:fortinet-fortios", "product:fortinet-fortimanager", "product:fortinet-fortianalyzer", "product:fortinet-fortimail", "product:fortinet-fortiauthenticator"]
techniques: [T1190]
affected_products: ["Fortinet FortiOS", "Fortinet FortiManager", "Fortinet FortiAnalyzer", "Fortinet FortiMail", "Fortinet FortiAuthenticator"]
cves:
  - id: CVE-2026-126147
    cvss: "9.8"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 and 7.2"
    fixed: "FortiMail 8.0.2, 7.6.7 or 7.4.9; 7.2 migrates to a fixed release"
  - id: CVE-2026-126148
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0 to 8.0.1 and 7.6.0 to 7.6.6 (command injection through HA join-request packets; 7.4 not affected)"
    fixed: "FortiMail 8.0.2 or 7.6.7"
  - id: CVE-2026-126164
    cvss: "9.4"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 and 7.2"
    fixed: "FortiMail 8.0.2, 7.6.7 or 7.4.9; 7.2 migrates to a fixed release; FortiMail Cloud remediated on 2026-10-05"
  - id: CVE-2026-126156
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail IBE webmail on 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 and 7.2 (account takeover of an arbitrary IBE recipient)"
    fixed: "FortiMail 8.0.2, 7.6.7 or 7.4.9; 7.2 migrates to a fixed release"
  - id: CVE-2026-126155
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail IBE webmail on 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 and 7.2 (an authenticated session as any IBE recipient)"
    fixed: "FortiMail 8.0.2, 7.6.7 or 7.4.9; 7.2 migrates to a fixed release"
  - id: CVE-2026-126257
    cvss: "9.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiAuthenticator 8.0.0 to 8.0.3 and 6.6.0 to 6.6.10 (hard-coded password, in certain circumstances outside the attacker's control)"
    fixed: "FortiAuthenticator 8.0.4 or 6.6.11"
  - id: CVE-2026-126251
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiAuthenticator 8.0.0 to 8.0.3 and 6.6.0 to 6.6.10 (incorrect authorization, CWE-863)"
    fixed: "FortiAuthenticator 8.0.4 or 6.6.11"
  - id: CVE-2026-126253
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiOS 8.0.0 to 8.0.1, 7.6.0 to 7.6.7, 7.4.0 to 7.4.12, 7.2.0 to 7.2.13 and 7.0.1 to 7.0.19 and FortiSASE, OSPF daemon"
    fixed: "FortiOS 8.0.2, 7.6.8, 7.4.13 or 7.2.14; FortiOS 7.0 migrates to a fixed release"
  - id: CVE-2026-126261
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiManager 8.0.0, 7.6.0 to 7.6.7, 7.4.0 to 7.4.5 and 7.2.0 to 7.2.8, with the FGFM port reachable"
    fixed: "FortiManager 8.0.1, 7.6.8, 7.4.6 or 7.2.9 (the October builds 8.0.2, 7.6.8, 7.4.12 and 7.2.13 also fix it)"
  - id: CVE-2026-126170
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available, mitigation-only]
    affected: "FortiAnalyzer, FortiManager and their Cloud variants 8.0.0 through 8.0.2 (only when the JSON API is enabled on an admin profile, off by default) and 7.6.0 through 7.6.7; FortiAnalyzer-BigData 7.6.0 through 7.6.2"
    fixed: "7.6.8 on FortiAnalyzer and FortiManager 7.6; no fixed 8.0 build, upcoming 8.0.3, workaround set rpc-permit none on every admin profile with the JSON API enabled; FortiAnalyzer-BigData upcoming 7.6.3"
  - id: CVE-2026-126262
    cvss: "9.3"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiAnalyzer 8.0.0 through 8.0.1, FortiManager 8.0.0, and FortiAnalyzer and FortiManager 7.6.0 through 7.6.7, 7.4.0 through 7.4.11 and 7.2.0 through 7.2.12, with the oftp port reachable"
    fixed: "FortiAnalyzer 8.0.2, FortiManager 8.0.1, 7.6.8, 7.4.12 or 7.2.13"
  - id: CVE-2026-126260
    cvss: "9.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiAnalyzer and FortiManager 8.0.0, 7.6.0 through 7.6.7 and 7.4.0 through 7.4.11, with the oftp port reachable"
    fixed: "8.0.1, 7.6.8 or 7.4.12"
  - id: CVE-2026-126229
    cvss: "9.1"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "FortiAnalyzer, FortiManager and their Cloud variants 8.0.0 through 8.0.1, 7.6.0 through 7.6.7, 7.4.0 through 7.4.11, and all 7.2 and 7.0 (an authenticated administrator reaches other VDOMs)"
    fixed: "8.0.2, 7.6.8 or 7.4.12; 7.2 and 7.0 migrate to a fixed release"
  - id: CVE-2026-126259
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiOS 8.0.0, 7.6.0 through 7.6.7, 7.4.0 through 7.4.12, 7.2.0 through 7.2.13 and all 7.0, in HA FGSP with standalone-config-sync or autoscale (adjacent network, crafted HA packets, commands as super admin)"
    fixed: "8.0.1, 7.6.8, 7.4.13 or 7.2.14; 7.0 migrates to a fixed release; virtual patch FG-VD-61445.0day"
  - id: CVE-2026-126254
    cvss: "9.6"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "FortiOS bgp daemon 8.0.0 through 8.0.1, 7.6.0 through 7.6.7, 7.4.0 through 7.4.12 and 7.2.0 through 7.2.13 (a configured iBGP neighbour sends malformed attributes to all connected routers)"
    fixed: "8.0.2, 7.6.8, 7.4.13 or 7.2.14"
  - id: CVE-2026-126263
    cvss: "9.4"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0 through 8.0.1, 7.6.0 through 7.6.4 and 7.4.0 through 7.4.6 (the page summary says authenticated, its metadata says unauthenticated)"
    fixed: "8.0.2, 7.6.7 or 7.4.7"
  - id: CVE-2026-126157
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0 through 8.0.1, 7.6.0 through 7.6.6, 7.4.0 through 7.4.8 and all 7.2 and 7.0 (access to other users' secure email accounts)"
    fixed: "8.0.2, 7.6.7 or 7.4.9; 7.2 and 7.0 migrate to a fixed release"
  - id: CVE-2026-126150
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiMail 8.0.0, 7.6.0 through 7.6.5, 7.4.0 through 7.4.7 and 7.2.0 through 7.2.9 (password reset and takeover of an arbitrary IBE webmail user)"
    fixed: "8.0.1, 7.6.6 or 7.4.8; FortiMail 7.2 awaits the upcoming 7.2.10"
  - id: CVE-2026-121529
    cvss: "9.1"
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "FortiClient Mac, Windows and Windows PAM 7.4.0 through 7.4.7; FortiClient Windows and Windows PAM 7.2.0 through 7.2.14 (origin validation error, victim interaction required)"
    fixed: "7.4.8 or 7.2.15"
sources:
  - url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
    publisher: "Fortinet (CISO Collective blog)"
    date: "2026-10-21"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13092"
    publisher: "NCSC.ch Security Hub (advisory 13092)"
    date: "2026-10-22"
    role: corroborating
  - url: "https://www.heise.de/news/Ausserplanmaessige-Fortinet-Updates-Details-Fehlanzeige-aber-dringend-11497171.html"
    publisher: "heise online"
    date: "2026-10-22"
    role: corroborating
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-175"
    publisher: "Fortinet PSIRT (FG-IR-26-175)"
    date: "2026-10-01"
    role: corroborating
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-199"
    publisher: "Fortinet PSIRT (FG-IR-26-199, CVE-2026-126147)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-200"
    publisher: "Fortinet PSIRT (FG-IR-26-200, CVE-2026-126148)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-216"
    publisher: "Fortinet PSIRT (FG-IR-26-216, CVE-2026-126164)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-208"
    publisher: "Fortinet PSIRT (FG-IR-26-208, CVE-2026-126156)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-207"
    publisher: "Fortinet PSIRT (FG-IR-26-207, CVE-2026-126155)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-271"
    publisher: "Fortinet PSIRT (FG-IR-26-271, CVE-2026-126257)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-265"
    publisher: "Fortinet PSIRT (FG-IR-26-265, CVE-2026-126251)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-267"
    publisher: "Fortinet PSIRT (FG-IR-26-267, CVE-2026-126253)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-275"
    publisher: "Fortinet PSIRT (FG-IR-26-275, CVE-2026-126261)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-219"
    publisher: "Fortinet PSIRT (FG-IR-26-219, CVE-2026-126170)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-274"
    publisher: "Fortinet PSIRT (FG-IR-26-274, CVE-2026-126260)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-276"
    publisher: "Fortinet PSIRT (FG-IR-26-276, CVE-2026-126262)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-273"
    publisher: "Fortinet PSIRT (FG-IR-26-273, CVE-2026-126259)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-268"
    publisher: "Fortinet PSIRT (FG-IR-26-268, CVE-2026-126254)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-277"
    publisher: "Fortinet PSIRT (FG-IR-26-277, CVE-2026-126263)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-209"
    publisher: "Fortinet PSIRT (FG-IR-26-209, CVE-2026-126157)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-202"
    publisher: "Fortinet PSIRT (FG-IR-26-202, CVE-2026-126150)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-244"
    publisher: "Fortinet PSIRT (FG-IR-26-244, CVE-2026-126229)"
    date: "2026-11-10"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-194"
    publisher: "Fortinet PSIRT (FG-IR-26-194, CVE-2026-121529)"
    date: "2026-11-10"
    role: primary
closed_sources: []
evidence:
  - quote: "We strongly urge every customer to plan and promptly complete these upgrades as soon as the releases are available, prioritizing internet-facing devices."
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
  - quote: "These releases include critical and high-severity fixes."
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
  - quote: "public advisories will be made available at the next Patch Tuesday on November 10"
    publisher: "Fortinet (CISO Collective blog)"
    source_url: "https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products"
  - quote: "may allow an unauthenticated attacker to execute unauthorized code or commands via crafted requests"
    publisher: "Fortinet PSIRT (FG-IR-26-199, CVE-2026-126147)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-199"
  - quote: "may allow an unauthenticated attacker that can reach the FGFM port to execute code or commands via crafted FGFM packets"
    publisher: "Fortinet PSIRT (FG-IR-26-275, CVE-2026-126261)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-275"
  - quote: "to take over an arbitrary IBE recipient account via crafted HTTP requests"
    publisher: "Fortinet PSIRT (FG-IR-26-208, CVE-2026-126156)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-208"
  - quote: "may allow an unauthenticated attacker to bypass credential validation in certain circumstances outside of the attacker's control and gain unauthorized access"
    publisher: "Fortinet PSIRT (FG-IR-26-271, CVE-2026-126257)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-271"
  - quote: "The vulnerability exists only when the JSON API is enabled (Disabled by default)"
    publisher: "Fortinet PSIRT (FG-IR-26-219, CVE-2026-126170)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-219"
  - quote: "may allow an unauthenticated attacker to execute unauthorized code or commands via a specially crafted HTTP request"
    publisher: "Fortinet PSIRT (FG-IR-26-219, CVE-2026-126170)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-219"
verification: single-source
sourcing_note: >
  Fortinet's own post is the first-party source for the release, the fixed versions and the disclosure schedule, and its PSIRT advisories of 2026-11-10 carry the flaws, scores and version tables; NCSC.ch's advisory and heise restate the post and add reach, not an independent assessment. The CVSS scores are those in Fortinet's advisory pages. Every critical row (CVSS 9.0 or higher) in the 2026-11-10 advisory pages is listed. FortiOS 7.0 appears in two of the advisory tables as a branch to migrate away from. Several pages contradict themselves between summary and metadata: FG-IR-26-277 calls the attacker authenticated in its summary and unauthenticated in its metadata, and FG-IR-26-202, FG-IR-26-207, FG-IR-26-216 and FG-IR-26-219 describe account takeover, webmail session access, SQL injection or code execution in their summaries while listing denial of service as the impact. The FortiMail overlap with the exploited CVE-2026-104286 rests on a comparison of Fortinet's two published fix tables.
confidence: high
references: ["2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager", "2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every FortiMail to 8.0.2, 7.6.7 or 7.4.9 (a 7.2 unit moves to a fixed release; 7.2.10 for CVE-2026-126150 is not released), every FortiAuthenticator to 8.0.4 or 6.6.11, every FortiOS to 8.0.2, 7.6.8, 7.4.13 or 7.2.14 (a 7.0 unit migrates), and every FortiManager and FortiAnalyzer on 7.6 or 7.4 to 7.6.8 or 7.4.12 (7.2 and 7.0 migrate), internet-facing units and FortiMail first, because the advisories describe unauthenticated code execution and account takeover and Fortinet warns that patch differences show attackers where the weakness sits; keep the FGFM and oftp ports and every administrative interface off untrusted networks."
  - "On every FortiAnalyzer and FortiManager (Cloud variants included) on 8.0.0 through 8.0.2, set rpc-permit none on every administrator profile that has the JSON API enabled until Fortinet releases 8.0.3, because no 8.0 build fixes the unauthenticated 9.8 flaw CVE-2026-126170 and 8.0.2 is affected."
updates:
  - at: "2026-11-11T03:50:56Z"
    run_id: 2026-11-11T0256Z-intel
    type: update
    summary: >
      Fortinet's withheld advisories were published on 2026-11-10 and name unauthenticated FortiMail
      code-execution, SQL-injection and IBE account-takeover flaws (CVSS up to 9.8), two
      FortiAuthenticator authentication bypasses (9.0 and 9.1), a FortiOS OSPF flaw reachable from the
      adjacent network and unauthenticated code execution through the FortiManager FGFM port; the fixed
      versions are unchanged and no exploitation is stated.
    fields: [title, headline, summary, tags, cves, sources, evidence, sourcing_note, actions, body]
  - at: "2026-11-12T04:20:00Z"
    run_id: 2026-11-12T0255Z-intel
    type: update
    summary: >
      Fortinet's advisories of 2026-11-10 carry ten more critical rows than the nine first listed across FortiAnalyzer, FortiManager, FortiOS, FortiMail and FortiClient, and the October builds do not fix every row: FortiAnalyzer and FortiManager 8.0 have no fixed build for CVE-2026-126170 until 8.0.3, FortiMail 7.2 awaits 7.2.10 for CVE-2026-126150, and FortiOS 7.0 and FortiAnalyzer and FortiManager 7.2 and 7.0 must migrate.
    fields: [title, headline, summary, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

Fortinet announced on 2026-10-21 coordinated security updates for FortiOS, FortiManager and FortiAnalyzer, released on 2026-10-22, and urged customers to treat them as a priority change because AI tools can help adversaries diff patches and build exploits within hours or days ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). The advisories withheld until Patch Tuesday were published on 2026-11-10; none of the 2026-11-10 advisories states exploitation, and NCSC.ch listed the status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13092)).

The critical rows (CVSS 9.0 or higher) by product. FortiMail: unauthenticated path traversal and command injection that may give code or command execution (CVE-2026-126147 and CVE-2026-126148, 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-199); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-200)), two SQL injections (CVE-2026-126164 and CVE-2026-126263, 9.4; the second is authenticated in its page summary and unauthenticated in its metadata) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-216); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-277)) and three IBE webmail takeover or access flaws (CVE-2026-126156, CVE-2026-126150 and CVE-2026-126155, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-208); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-202); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-207)) and an unauthenticated access flaw in other users' secure email accounts (CVE-2026-126157, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-209)). FortiAnalyzer and FortiManager: an unauthenticated GUI flaw that may allow code or command execution only when the JSON API is enabled, which is off by default (CVE-2026-126170, 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-219)), oftp port SQL injection and SSRF (CVE-2026-126262, 9.3; CVE-2026-126260, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-276); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-274)), an administrator's access to other VDOMs (CVE-2026-126229, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-244)) and FGFM code execution (CVE-2026-126261, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-275)). FortiOS: the OSPF daemon (CVE-2026-126253, 9.3), HA FGSP command execution (CVE-2026-126259, 9.0) and iBGP (CVE-2026-126254, 9.6) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-273); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-268)). FortiAuthenticator: two authentication bypasses (CVE-2026-126257, 9.0; CVE-2026-126251, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-271); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-265)). FortiClient: an origin-validation flaw that needs victim interaction (CVE-2026-121529, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-194)).

The October builds fix most rows: FortiOS 8.0.2, 7.6.8, 7.4.13 and 7.2.14; FortiManager and FortiAnalyzer 8.0.2, 7.6.8, 7.4.12 and 7.2.13; FortiMail 8.0.2, 7.6.7 and 7.4.9; FortiAuthenticator 8.0.4 and 6.6.11 ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). Not every row: no 8.0 build fixes CVE-2026-126170 until the upcoming 8.0.3, with rpc-permit none on admin profiles that have the JSON API enabled as the workaround ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-219)); FortiMail 7.2 awaits 7.2.10 for CVE-2026-126150 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-202)); FortiAnalyzer and FortiManager 7.2 and 7.0 and FortiOS 7.0 must migrate ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-244); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-273)). The FortiMail builds also fix the exploited CVE-2026-104286 ([Fortinet PSIRT, 2026-10-01](https://fortiguard.fortinet.com/psirt/FG-IR-26-175)).

**Exposure:** FortiMail 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 or any 7.2; FortiAuthenticator 8.0.0 to 8.0.3 and 6.6.0 to 6.6.10; FortiOS below the fixed builds and any 7.0; FortiAnalyzer and FortiManager 8.0.0 to 8.0.2 with the JSON API, oftp or FGFM port reachable; FortiClient 7.4.0 to 7.4.7 and 7.2.0 to 7.2.14.

**Detection:** Fortinet advises watching logs for unusual administrative access and unapproved configuration changes ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)); for the new rows, FortiMail web logs for unauthenticated IBE webmail and HA join requests, FortiAnalyzer and FortiManager JSON API, oftp and FGFM connections from unexpected sources, and OSPF advertisements from unexpected hosts and unusual updates from iBGP neighbours.

**Defender takeaway:** upgrade FortiMail, FortiAuthenticator and the internet-facing FortiOS, FortiManager and FortiAnalyzer units now; an unpatched FortiMail is exposed to the exploited flaw too. On FortiAnalyzer and FortiManager 8.0 apply the rpc-permit workaround until 8.0.3 ships, plan the migration off branches with no fix, and keep administrative interfaces and the FGFM and oftp ports off untrusted networks.

## Update — 2026-11-11T03:50:56Z

Fortinet published the advisories it had withheld from the October hardening release on 2026-11-10. They name unauthenticated FortiMail flaws that may allow code or command execution through crafted requests (CVE-2026-126147, CVSS 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-199)) and through HA join-request packets (CVE-2026-126148, 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-200)), an unauthenticated SQL injection (CVE-2026-126164, 9.4) that Fortinet remediated in FortiMail Cloud on 2026-10-05 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-216)), and two IBE webmail flaws that let an attacker take over an IBE recipient account (CVE-2026-126156, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-208)) or obtain an authenticated session as one (CVE-2026-126155, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-207)). Two FortiAuthenticator flaws, a hard-coded-password bypass (CVE-2026-126257, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-271)) and an incorrect-authorization authentication bypass (CVE-2026-126251, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-265)), a FortiOS and FortiSASE OSPF flaw that lets an unauthenticated attacker on the adjacent network broadcast link-state advertisements (CVE-2026-126253, 9.3) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267)) and unauthenticated code execution through the FortiManager FGFM port (CVE-2026-126261, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-275)) are the other rows that page named. The October builds fix most of them but not on every branch (FortiMail 7.2 and FortiOS 7.0 are told to migrate for some rows, as the update below sets out), FG-IR-26-275 lists lower minimum FortiManager builds (8.0.1, 7.6.8, 7.4.6 and 7.2.9) for the FGFM flaw, and none of the 2026-11-10 advisories states exploitation.


## Update — 2026-11-12T04:20:00Z

The advisory pages carry ten more critical rows (CVSS 9.0 or higher), shown above, and the October builds do not fix every row: FortiAnalyzer and FortiManager 8.0.0 through 8.0.2 have no fixed build for CVE-2026-126170 until the upcoming 8.0.3 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-219)), FortiMail 7.2 awaits 7.2.10 for CVE-2026-126150 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-202)), FortiAnalyzer and FortiManager 7.2 and 7.0 must migrate for CVE-2026-126229 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-244)), and FortiOS 7.0 must migrate for CVE-2026-126253 and CVE-2026-126259 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267)) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-273)).
