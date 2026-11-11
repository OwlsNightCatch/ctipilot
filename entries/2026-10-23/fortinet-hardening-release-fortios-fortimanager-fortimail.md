---
schema: 1
kind: vulnerability
title: "Fortinet coordinated security hardening release: the advisories published on 2026-11-10 show unauthenticated FortiMail code-execution and account-takeover flaws (CVSS up to 9.8), FortiAuthenticator, FortiOS OSPF and FortiManager FGFM flaws among fixes in FortiOS 8.0.2, 7.6.8, 7.4.13 and 7.2.14, FortiManager, FortiAnalyzer, FortiMail and FortiAuthenticator"
headline: "Fortinet's withheld advisories are out: unauthenticated FortiMail RCE (9.8), FortiAuthenticator, OSPF and FGFM flaws"
summary: >
  Fortinet's coordinated hardening release of 2026-10-22 fixed critical and high-severity flaws in FortiOS, FortiManager, FortiAnalyzer, FortiMail and FortiAuthenticator, and the advisories withheld until Patch Tuesday were published on 2026-11-10: unauthenticated FortiMail path traversal and command injection to code execution (CVE-2026-126147 and CVE-2026-126148, CVSS 9.8) and SQL injection (CVE-2026-126164, 9.4), FortiMail IBE webmail account takeover (CVSS 9.1), two FortiAuthenticator authentication bypasses (9.0 and 9.1), a FortiOS OSPF flaw (9.3) and unauthenticated code execution through the FortiManager FGFM port (9.0).
  The October builds fix the new rows too (FortiManager's FGFM flaw also lists lower minimum builds) and no Fortinet page states exploitation; NCSC.ch listed the status as unknown, and the FortiMail builds are also the ones that fix the exploited CVE-2026-104286.
discovered_at: "2026-10-23T03:38:30Z"
updated_at: "2026-11-11T03:50:56Z"
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
    affected: "FortiOS 8.0.0 to 8.0.1, 7.6.0 to 7.6.7, 7.4.0 to 7.4.12 and 7.2.0 to 7.2.13 and FortiSASE, OSPF daemon"
    fixed: "FortiOS 8.0.2, 7.6.8, 7.4.13 or 7.2.14"
  - id: CVE-2026-126261
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiManager 8.0.0, 7.6.0 to 7.6.7, 7.4.0 to 7.4.5 and 7.2.0 to 7.2.8, with the FGFM port reachable"
    fixed: "FortiManager 8.0.1, 7.6.8, 7.4.6 or 7.2.9 (the October builds 8.0.2, 7.6.8, 7.4.12 and 7.2.13 also fix it)"
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
verification: single-source
sourcing_note: >
  Fortinet's own post is the first-party source for the release, the fixed versions and the disclosure schedule, and its PSIRT advisories of 2026-11-10 carry the flaws, scores and version tables; NCSC.ch's advisory and heise restate the post and add reach, not an independent assessment. The CVSS scores are those in Fortinet's advisory feed; the 2026-11-10 feed lists 50 advisories and is capped at 50, so more may exist, and only the unauthenticated rows scored 9.0 or higher are listed here. Fortinet's tables list no row for FortiOS 7.0 or 6.4, which is not a statement about whether those branches are affected. The FortiMail overlap with the exploited CVE-2026-104286 rests on a comparison of Fortinet's two published fix tables.
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
  - "Upgrade every FortiMail to 8.0.2, 7.6.7 or 7.4.9 (a 7.2 unit moves to a fixed release), every FortiAuthenticator to 8.0.4 or 6.6.11, every FortiOS to 8.0.2, 7.6.8, 7.4.13 or 7.2.14, and every FortiManager to 8.0.2, 7.6.8, 7.4.12 or 7.2.13, internet-facing units and FortiMail first, because the advisories now describe unauthenticated code execution and account takeover and Fortinet warns that patch differences show attackers where the weakness sits; where an upgrade has to wait, keep the FortiManager FGFM port and every administrative interface off untrusted networks."
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
migrated_from: null
---

Fortinet announced on 2026-10-21 a coordinated set of security updates for FortiOS, FortiManager and FortiAnalyzer, released on 2026-10-22, with fixes found through its frontier-AI-assisted testing, and urged customers to treat them as a priority change because AI tools can help adversaries diff patches and build exploits within hours or days ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). NCSC.ch described the fixes as ones that might give attackers unauthorized control over affected security infrastructure and listed the exploitation status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13092)).

The worst rows are in FortiMail: an unauthenticated path traversal that may allow code or command execution (CVE-2026-126147, CVSS 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-199)), an unauthenticated command injection through HA join-request packets (CVE-2026-126148, 9.8; 8.0 and 7.6 only) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-200)), an unauthenticated SQL injection (CVE-2026-126164, 9.4), remediated in FortiMail Cloud on 2026-10-05 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-216)), and two IBE webmail flaws, one that lets an unauthenticated attacker take over an arbitrary IBE recipient account (CVE-2026-126156, 9.1) and one that gives an authenticated session as any IBE recipient to read or send their encrypted mail (CVE-2026-126155, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-208); [Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-207)). Two FortiAuthenticator flaws let an attacker bypass authentication: a hard-coded password in certain circumstances (CVE-2026-126257, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-271)) and incorrect authorization (CVE-2026-126251, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-265)). The FortiOS and FortiSASE OSPF daemon lets an unauthenticated attacker on the adjacent network broadcast link-state advertisements (CVE-2026-126253, 9.3) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267)), and FortiManager's FGFM service may allow an unauthenticated attacker who can reach the FGFM port to execute code or commands (CVE-2026-126261, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-275)). No Fortinet page states exploitation.

The fixed versions are FortiOS 8.0.2, 7.6.8, 7.4.13 and 7.2.14; FortiManager and FortiAnalyzer 8.0.2, 7.6.8, 7.4.12 and 7.2.13; FortiMail 8.0.2, 7.6.7 and 7.4.9, with 7.2 migrating to a later branch; and FortiAuthenticator 8.0.4 and 6.6.11 ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)). The FortiMail builds are identical to the fix table for FG-IR-26-175, the unauthenticated IBE path traversal CVE-2026-104286 that Fortinet reports as exploited in the wild, so a FortiMail below them is exposed to that flaw as well ([Fortinet PSIRT, 2026-10-01](https://fortiguard.fortinet.com/psirt/FG-IR-26-175)).

**Exposure:** FortiMail on 8.0.0 to 8.0.1, 7.6.0 to 7.6.6, 7.4.0 to 7.4.8 or any 7.2; FortiAuthenticator 8.0.0 to 8.0.3 and 6.6.0 to 6.6.10; FortiOS on the versions below the fixed ones; and FortiManager with the FGFM port reachable. Fortinet tells customers to inventory every FortiManager and FortiOS instance and to start with those reachable from the internet ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)).

**Detection:** Fortinet advises watching logs for unusual administrative access and unapproved configuration changes before and after patching ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)); for the new rows, FortiMail web logs for unauthenticated requests to the IBE webmail endpoints and the HA join port, FortiAuthenticator logins without a credential check, OSPF events from routers that are not configured neighbours, and FGFM connections from unexpected sources. Because IBE takeover exposes encrypted-mail content, treat IBE recipient mailboxes on an unpatched FortiMail as possibly read.

**Defender takeaway:** upgrade FortiMail, FortiAuthenticator and the internet-facing FortiOS and FortiManager units now; a FortiMail still below the fixed builds is exposed to the exploited flaw as well as the new ones. Where an upgrade has to wait, restrict administrative HTTPS and SSH to trusted addresses, keep FortiManager administration off the internet and enforce MFA for every administrator account ([Fortinet, 2026-10-21](https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products)), and keep the FGFM port unreachable from untrusted networks ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-275)).

## Update — 2026-11-11T03:50:56Z

Fortinet published the advisories it had withheld from the October hardening release on 2026-11-10. They name unauthenticated FortiMail flaws that may allow code or command execution through crafted requests (CVE-2026-126147, CVSS 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-199)) and through HA join-request packets (CVE-2026-126148, 9.8) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-200)), an unauthenticated SQL injection (CVE-2026-126164, 9.4) that Fortinet remediated in FortiMail Cloud on 2026-10-05 ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-216)), and two IBE webmail flaws that let an attacker take over an IBE recipient account (CVE-2026-126156, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-208)) or obtain an authenticated session as one (CVE-2026-126155, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-207)). Two FortiAuthenticator flaws, a hard-coded-password bypass (CVE-2026-126257, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-271)) and an incorrect-authorization authentication bypass (CVE-2026-126251, 9.1) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-265)), a FortiOS and FortiSASE OSPF flaw that lets an unauthenticated attacker on the adjacent network broadcast link-state advertisements (CVE-2026-126253, 9.3) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-267)) and unauthenticated code execution through the FortiManager FGFM port (CVE-2026-126261, 9.0) ([Fortinet PSIRT, 2026-11-10](https://fortiguard.fortinet.com/psirt/FG-IR-26-275)) complete the set. The October builds fix them, FG-IR-26-275 lists lower minimum FortiManager builds (8.0.1, 7.6.8, 7.4.6 and 7.2.9) for the FGFM flaw, and no Fortinet page states exploitation.
