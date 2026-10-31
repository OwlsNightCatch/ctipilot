---
schema: 1
kind: vulnerability
title: "CVE-2026-15176 / CVE-2026-93479 / CVE-2026-97205, NGINX Open Source and NGINX Plus: three unauthenticated heap-corruption flaws rated CVSS 4.0 9.2, reachable only in specific configurations and fixed in 1.30.6 and 1.31.7"
headline: "Three configuration-dependent NGINX heap flaws (CVSS 9.2) are fixed in 1.30.6, 1.31.7 and Debian trixie, not bookworm"
summary: >
  The nginx 1.30.6 (stable) and 1.31.7 (mainline) releases of 2026-10-14 fix five security flaws, three of them
  heap-corruption bugs that F5 scores CVSS 4.0 9.2 and an unauthenticated attacker can reach with crafted HTTP requests, but only
  on configurations that combine alias with rewrite and $request_filename, use a regex map whose captures are referenced before
  its output variable, or enable asynchronous file I/O with server-side includes; the other two concern HTTP/3 and TLS session
  ticket key rotation. F5 says the heap flaws restart the worker, with code execution only where ASLR is disabled or bypassed;
  no exploitation or public proof of concept is reported, nginx.org rates all five medium, and Debian fixed trixie with DSA-6575-1
  while its bookworm package is still marked vulnerable.
discovered_at: "2026-10-20T03:55:30Z"
updated_at: "2026-10-25T14:03:33Z"
event_date: "2026-10-14"
run_id: 2026-10-20T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, dos, patch-available]
regions: [global]
sectors: []
entities: []
techniques: [T1190, T1499.004]
affected_products: ["F5 NGINX Open Source", "F5 NGINX Plus"]
cves:
  - id: CVE-2026-15176
    cvss: "9.2 (CVSS 4.0)"
    epss: "0.0052"
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 0.1.29 to 1.30.5 and 1.31.0 to 1.31.6; NGINX Plus R33 to R36, 37.0.0 to 37.0.5 and 37.1.0"
    fixed: "NGINX Open Source 1.30.6 (stable) and 1.31.7 (mainline); NGINX Plus 37.0.5.1 and 37.1.0.1"
  - id: CVE-2026-93479
    cvss: "9.2 (CVSS 4.0)"
    epss: "0.0055"
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 1.30.0 to 1.30.5 and 1.31.2 to 1.31.6, builds that already carry the CVE-2026-42533 fix included; NGINX Plus R33 to R36, 37.0.0 to 37.0.5 and 37.1.0"
    fixed: "NGINX Open Source 1.30.6 (stable) and 1.31.7 (mainline); NGINX Plus 37.0.5.1 and 37.1.0.1"
  - id: CVE-2026-97205
    cvss: "9.2 (CVSS 4.0)"
    epss: "0.0048"
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 0.8.11 to 1.31.6 (nginx.org), only with asynchronous file I/O and SSI enabled; NGINX Plus is listed among the fixed releases; Daily CyberSecurity gives one Plus range for all three advisories (37.0.0 through 37.0.4 and R33 to R36) where CCB gives 37.0.0 to 37.0.5 for the first two"
    fixed: "NGINX Open Source 1.30.6 (stable) and 1.31.7 (mainline); NGINX Plus 37.0.5.1 and 37.1.0.1"
  - id: CVE-2026-95101
    cvss: "medium (nginx.org rating; no score read)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 1.25.0 to 1.31.6, with HTTP/3 in use"
    fixed: "NGINX Open Source 1.30.6 (stable) and 1.31.7 (mainline)"
  - id: CVE-2026-97629
    cvss: "medium (nginx.org rating; no score read)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 1.23.2 to 1.31.6, with TLS session ticket key rotation in use"
    fixed: "NGINX Open Source 1.30.6 (stable) and 1.31.7 (mainline)"
sources:
  - url: "https://nginx.org/en/CHANGES-1.30"
    publisher: "nginx.org (change log for nginx 1.30.6)"
    date: "2026-10-14"
    role: primary
  - url: "https://nginx.org/en/security_advisories.html"
    publisher: "nginx.org (security advisories)"
    date: "2026-10-14"
    role: primary
  - url: "https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited"
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    date: "2026-10-19"
    role: corroborating
  - url: "https://security-tracker.debian.org/tracker/CVE-2026-15176"
    publisher: "Debian Security Tracker"
    date: "2026-10-20"
    role: corroborating
  - url: "https://security-tracker.debian.org/tracker/DSA-6575-1"
    publisher: "Debian Security Tracker (DSA-6575-1, nginx security update)"
    date: "2026-10-25"
    role: corroborating
  - url: "https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/"
    publisher: "Daily CyberSecurity"
    date: "2026-10-14"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/18/ngnix-vulnerability-exploited-cve-2026-42945/"
    publisher: "Help Net Security"
    date: "2026-05-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Security: when using TLS session ticket key rotation, one of the keys"
    publisher: "nginx.org (change log for nginx 1.30.6)"
    source_url: "https://nginx.org/en/CHANGES-1.30"
  - quote: "Not vulnerable: 1.31.7+, 1.30.6+"
    publisher: "nginx.org (security advisories)"
    source_url: "https://nginx.org/en/security_advisories.html"
  - quote: "Use-after-free when using asynchronous file I/O (AIO)"
    publisher: "nginx.org (security advisories)"
    source_url: "https://nginx.org/en/security_advisories.html"
  - quote: "CVE-2026-93479: CVSS 9.2 (CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)"
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    source_url: "https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited"
  - quote: "On systems where Address Space Layout Randomization (ASLR) is disabled or can be bypassed, an attacker could also execute code"
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    source_url: "https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited"
  - quote: "While patching appliances or software to the newest version may protect against future exploitation, it does not remediate historic compromise."
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    source_url: "https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited"
  - quote: "when a location is configured that uses the alias directive together with rewrite and a set or return directive referencing"
    publisher: "F5 (CNA text for CVE-2026-15176, as republished by the Debian Security Tracker)"
    source_url: "https://security-tracker.debian.org/tracker/CVE-2026-15176"
  - quote: "Currently, F5 has confirmed no public proof-of-concept exploit code for any of the three flaws."
    publisher: "Daily CyberSecurity"
    source_url: "https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/"
  - quote: "A critical NGINX vulnerability (CVE-2026-42945) disclosed last week is being exploited by attackers"
    publisher: "Help Net Security"
    source_url: "https://www.helpnetsecurity.com/2026/05/18/ngnix-vulnerability-exploited-cve-2026-42945/"
verification: multi-source
sourcing_note: >
  nginx.org's change log for 1.30.6 is the dated primary, and its advisories page, a rolling index without dates, is the source for the affected and fixed versions and the severity it assigns; F5's advisory pages
  were not readable, so F5's wording is taken from its CNA text as republished by the Debian Security Tracker and as relayed by
  Daily CyberSecurity, and the Belgian CCB restates the same vendor assessment rather than assessing it
  independently. The three CVSS 4.0 scores of 9.2 are F5's as relayed by Daily CyberSecurity, and CCB's warning covers only
  CVE-2026-15176 and CVE-2026-93479. The Debian status was read on 2026-10-20 and again on 2026-10-25. The exploitation of an earlier NGINX flaw
  is background, and no source says these three have an equivalent exploit. CCB lists NGINX Plus 37.0.0 to 37.0.5 where Daily CyberSecurity gives 37.0.0 through 37.0.4.
confidence: high
references:
  - "2026-07-20/cve-2026-42533-nginx-pcre-capture-clobber-preauth-rce"
  - "2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea"
  - "2026-06-19/cve-2026-42530-cve-2026-42055-nginx-http-3-quic-use-after-fr"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Run nginx -T on every internet-facing NGINX reverse proxy, load balancer and ingress and upgrade each one whose configuration uses alias with rewrite and $request_filename, a regex map whose captures are referenced before its output variable, or aio together with ssi, HTTP/3 or TLS session ticket key rotation to nginx 1.30.6 or 1.31.7 (NGINX Plus 37.0.5.1 or 37.1.0.1); where the package comes from Debian trixie, install the DSA-6575-1 update (1.26.3-3+deb13u10); on bookworm, which the tracker still marks vulnerable, apply F5's configuration workaround until the distribution ships a fix."
updates:
  - at: "2026-10-25T14:03:33Z"
    run_id: 2026-10-25T1308Z-audit
    type: update
    summary: >
      Debian fixed the five NGINX flaws in trixie with DSA-6575-1 (1.26.3-3+deb13u10); only bookworm is
      still marked vulnerable. Trixie users install the update; bookworm keeps the configuration
      workaround.
    fields: [headline, summary, sources, sourcing_note, actions, body]
migrated_from: null
---

nginx's change log for 1.30.6, dated 14 October 2026, lists five security fixes, which nginx.org's advisories page ties to 1.30.6 (stable) and 1.31.7 (mainline) ([nginx.org change log, 2026-10-14](https://nginx.org/en/CHANGES-1.30); [nginx.org, 2026-10-14](https://nginx.org/en/security_advisories.html)); three of them are CVE-2026-15176, a heap buffer overflow in the core module that CCB describes as reachable where a location uses alias together with rewrite and a set or return directive referencing $request_filename, or where $request_filename appears in an access-log format; CVE-2026-93479, a heap buffer overflow in script evaluation that affects configurations whose regex map captures are referenced in root or an access-log format before the map's output variable, or that use a non-cacheable variable in a string expression; and CVE-2026-97205, a use-after-free when asynchronous file I/O is enabled, which Daily CyberSecurity relays from F5 as triggered by an SSI page with include virtual commands ([Centre for Cybersecurity Belgium, 2026-10-19](https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited); [Daily CyberSecurity, 2026-10-14](https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/)). Each is scored CVSS 4.0 9.2 and reachable by an unauthenticated network attacker, the first two under conditions beyond the attacker's control, with CCB's warning and vector covering the first two and Daily CyberSecurity all three ([Centre for Cybersecurity Belgium, 2026-10-19](https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited); [Daily CyberSecurity, 2026-10-14](https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/)). F5's CNA text says the overflow may restart the worker process and that attackers can execute code where ASLR is disabled or can be bypassed ([Debian Security Tracker, 2026-10-20](https://security-tracker.debian.org/tracker/CVE-2026-15176)). Daily CyberSecurity reports that F5 has confirmed no public proof of concept for any of the three, and no exploitation is reported ([Daily CyberSecurity, 2026-10-14](https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/)). Help Net Security reports that VulnCheck flagged exploitation attempts against an earlier NGINX flaw, CVE-2026-42945, three days after the flaw and its proof of concept were public ([Help Net Security, 2026-05-18](https://www.helpnetsecurity.com/2026/05/18/ngnix-vulnerability-exploited-cve-2026-42945/)). The other two are CVE-2026-95101 (with HTTP/3, part of an unknown frame might be treated as the request body, bypassing client_max_body_size or injecting data into the proxied request) and CVE-2026-97629 (with TLS session ticket key rotation, one key was left uninitialised, which might allow forging a session) ([nginx.org change log, 2026-10-14](https://nginx.org/en/CHANGES-1.30)); nginx.org rates all five medium ([nginx.org, 2026-10-14](https://nginx.org/en/security_advisories.html)).

**Exposure:** nginx 0.1.29 to 1.31.6 depending on the flaw, with branches older than 1.30 outside the range of CVE-2026-93479, and NGINX Plus R33 to R36 and 37.0.0 to 37.1.0 for the first two ([nginx.org, 2026-10-14](https://nginx.org/en/security_advisories.html); [Centre for Cybersecurity Belgium, 2026-10-19](https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited)). A build is affected only if its configuration matches one of the patterns above, which `nginx -T` prints with every include; the version string alone is not enough, because distribution packages carry their own fixes. Debian fixed trixie with DSA-6575-1 (trixie-security 1.26.3-3+deb13u10) ([Debian Security Tracker, 2026-10-25](https://security-tracker.debian.org/tracker/DSA-6575-1)), while its tracker still marks bookworm (1.22.1-9+deb12u10) vulnerable ([Debian Security Tracker, 2026-10-20](https://security-tracker.debian.org/tracker/CVE-2026-15176)).

**Detection:** F5 says the overflow leads to a worker restart, so process-supervision and error-log telemetry for unexpected worker exits and respawn bursts, matched against the unauthenticated requests to the affected locations in the access log, is the signal ([Debian Security Tracker, 2026-10-20](https://security-tracker.debian.org/tracker/CVE-2026-15176)). Patching does not remediate a compromise that already happened ([Centre for Cybersecurity Belgium, 2026-10-19](https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited)).

**Defender takeaway:** upgrade to 1.30.6 or 1.31.7 (NGINX Plus 37.0.5.1 or 37.1.0.1), starting with internet-facing instances whose configuration matches a pattern above; until a package is fixed, F5's workarounds are aio off or ssi off for CVE-2026-97205, named captures confined to the matching block for CVE-2026-93479, and no alias in the affected locations or no $request_filename reference for CVE-2026-15176 ([Daily CyberSecurity, 2026-10-14](https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/)).

## Update — 2026-10-25T14:03:33Z

Debian fixed the five flaws in trixie with DSA-6575-1, which ships nginx 1.26.3-3+deb13u10 in trixie-security ([Debian Security Tracker, 2026-10-25](https://security-tracker.debian.org/tracker/DSA-6575-1)). Bookworm's package, 1.22.1-9+deb12u10, is still marked vulnerable, so Debian has not shipped a bookworm fix ([Debian Security Tracker, 2026-10-20](https://security-tracker.debian.org/tracker/CVE-2026-15176)).
