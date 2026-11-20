---
schema: 1
kind: vulnerability
title: "PHP 8.5.13, 8.4.28, 8.3.37 and 8.2.36: CVE-2026-129289 lets an unauthenticated request smuggle a second FastCGI request into PHP-FPM and run PHP code when the front end reuses FastCGI connections; the release also fixes the session flaw left open in October and follow-ups to an incomplete earlier fix (CVSS 4.0 9.2)"
headline: "PHP 8.5.13, 8.4.28, 8.3.37, 8.2.36: FPM request smuggling to code execution; the open session flaw is fixed"
summary: >
  The PHP project released 8.5.13, 8.4.28, 8.3.37, 8.2.36 and 8.6.0 on 2026-11-19 with fixes for up to 18 CVEs per branch. The most direct is CVE-2026-129289: PHP-FPM keeps unread php://input bytes on a persistent FastCGI connection, so an unauthenticated multipart request can plant a second FastCGI request and run PHP code as the worker, but only behind a front end that reuses FastCGI connections, which standard nginx and Apache setups do not. The release also fixes CVE-2026-115560, left open in October, and follow-ups to an incomplete earlier fix; no source reports exploitation or a public proof of concept.
discovered_at: "2026-11-20T05:04:00Z"
updated_at: null
event_date: "2026-11-19"
run_id: 2026-11-20T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: ["product:php"]
techniques: [T1190, T1059, T1068]
affected_products: ["PHP"]
cves:
  - id: CVE-2026-129289
    cvss: "9.2"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP-FPM before 8.2.36, 8.3.37, 8.4.28 and 8.5.13 behind a front end that reuses FastCGI backend connections and an application path that opens php://input without reading it fully; the CNA range has no lower bound, so 8.1 and older are affected"
    fixed: "8.2.36; 8.3.37; 8.4.28; 8.5.13; 8.6.0; no upstream fix for 8.1 and older"
  - id: CVE-2026-115560
    cvss: "9.2"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP before 8.2.36, 8.3.37, 8.4.28 and 8.5.13 with session upload progress enabled and an object gadget chain in the application"
    fixed: "8.2.36; 8.3.37; 8.4.28; 8.5.13; 8.6.0"
  - id: CVE-2026-126714
    cvss: "9.2"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP before 8.2.36, 8.3.37, 8.4.28 and 8.5.13 with the default files session handler and an object gadget chain in the application"
    fixed: "8.2.36; 8.3.37; 8.4.28; 8.5.13; 8.6.0"
  - id: CVE-2026-129481
    cvss: "9.2"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP 8.3 before 8.3.37, 8.4 before 8.4.28 and 8.5 before 8.5.13, where a fatal error interrupts session shutdown; PHP 8.2 does not carry the affected field"
    fixed: "8.3.37; 8.4.28; 8.5.13; 8.6.0"
  - id: CVE-2026-129182
    cvss: "9.2"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP 8.5 before 8.5.13"
    fixed: "8.5.13; 8.6.0"
  - id: CVE-2026-129474
    cvss: "9.2"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP 8.5 before 8.5.13 on the built-in defaults (fatal error backtraces on, arguments included) with an application path that enters a magic method and request control over allocation size; php.ini-production (zend.exception_ignore_args=1) or fatal_error_backtraces=0 prevents the attack"
    fixed: "8.5.13; 8.6.0"
  - id: CVE-2026-129496
    cvss: "9.2"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PHP before 8.2.36, 8.3.37, 8.4.28 and 8.5.13 in non-thread-safe builds that write a startup diagnostic through a file-based error_log"
    fixed: "8.2.36; 8.3.37; 8.4.28; 8.5.13; 8.6.0"
  - id: CVE-2026-129291
    cvss: "8.8"
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "PHP-FPM 8.2.7 to 8.2.35, 8.3 before 8.3.37, 8.4 before 8.4.28 and 8.5 before 8.5.13 with catch_workers_output enabled; 8.1.20 to 8.1.34 is affected with no fix"
    fixed: "8.2.36; 8.3.37; 8.4.28; 8.5.13; 8.6.0; none for 8.1"
sources:
  - url: "https://www.php.net/ChangeLog-8.php"
    publisher: "PHP project (ChangeLog)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6"
    publisher: "PHP project (GHSA-qc49-hpvq-g2w6)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx"
    publisher: "PHP project (GHSA-658j-r8rw-q6mx)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp"
    publisher: "PHP project (GHSA-fm2m-fjf5-v3cp)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-g3vh-838c-65v7"
    publisher: "PHP project (GHSA-g3vh-838c-65v7)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-2fjv-p558-g82m"
    publisher: "PHP project (GHSA-2fjv-p558-g82m)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2"
    publisher: "PHP project (GHSA-8mjj-2r7p-4hg2)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-gr4f-wgx5-jpfv"
    publisher: "PHP project (GHSA-gr4f-wgx5-jpfv)"
    date: "2026-11-19"
    role: primary
  - url: "https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m"
    publisher: "PHP project (GHSA-jm4m-qfqx-967m)"
    date: "2026-11-19"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13212"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-19"
    role: corroborating
  - url: "https://watchtowr.com/intelligence/php-cve-2026-115560-faq/"
    publisher: "watchTowr"
    date: "2026-11-20"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  The PHP project is the disclosing party for its own software and its advisories and changelog are the primary; the CVSS 4.0 numbers come from the PHP CNA records, because the advisory pages show a severity label and a vector and NCSC.ch states that no numeric scores were published in the advisories it references. NCSC.ch and watchTowr restate the release and add the exploitation status.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every PHP-FPM server behind nginx with fastcgi_keep_conn on, Apache mod_proxy_fcgi with enablereuse=on or HAProxy in FastCGI mode, switch FastCGI backend connection reuse off until the server runs 8.2.36, 8.3.37, 8.4.28 or 8.5.13, because CVE-2026-129289 gives an unauthenticated request code execution as the worker wherever a connection is reused and an application path leaves php://input unread."
updates: []
migrated_from: null
---

The PHP project released 8.5.13, 8.4.28, 8.3.37, 8.2.36 and 8.6.0 on 2026-11-19, and the changelogs list up to 18 CVEs per branch ([PHP, 2026-11-19](https://www.php.net/ChangeLog-8.php)). The most direct is CVE-2026-129289: when php://input was opened but not read to the end, PHP-FPM leaves the unread request bytes on a persistent FastCGI connection, so a malformed multipart body can place a second FastCGI request inside the first, and an unauthenticated attacker can bypass front-end routing and execute attacker-controlled PHP code with the privileges of the worker ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6)). It requires a front end that enables persistent backend connections and an application path that opens php://input without reading it fully; standard nginx and Apache configurations that close the FastCGI connection after each request are not affected by the demonstrated attack ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6)).

Two session flaws close the item the October release left open ([watchTowr, 2026-11-20](https://watchtowr.com/intelligence/php-cve-2026-115560-faq/)): CVE-2026-115560, where upload-progress session data is written in one serializer format and read in another, and CVE-2026-126714, where an interrupted write by the default files handler leaves a mixed old and new session file; both end in object injection and need an object gadget chain in the application ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx); [PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp)). The fix for the first disables upload progress by default ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx)). CVE-2026-129481, a use-after-free of a stale session filename after an interrupted session shutdown, is in PHP's words an incomplete fix for CVE-2026-109619 and affects PHP 8.3 and later, and CVE-2026-129182, for PHP 8.5 only, covers further scenarios after the 8.5.12 fix ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-g3vh-838c-65v7); [PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-2fjv-p558-g82m)).

CVE-2026-129474, PHP 8.5 only, is exposed on the built-in defaults, because fatal error backtraces are on in 8.5 and the default includes arguments, and php.ini-production, which sets zend.exception_ignore_args=1, or fatal_error_backtraces=0 prevents the attack; PHP confirmed code execution on 8.5 ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2)). CVE-2026-129496 needs a startup diagnostic written through a file-based error_log in a non-thread-safe build ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-gr4f-wgx5-jpfv)). CVE-2026-129291, an epoll use-after-free in PHP-FPM, gives root from a worker where catch_workers_output is on and the FPM master runs as root ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m)). NCSC.ch lists exploitation as unknown with no public proof of concept referenced, and watchTowr reports none as of 2026-11-20 ([NCSC.ch, 2026-11-19](https://security-hub.ncsc.admin.ch/#/posts/13212); [watchTowr, 2026-11-20](https://watchtowr.com/intelligence/php-cve-2026-115560-faq/)).

**Exposure:** PHP 8.5 without php.ini-production settings is exposed to CVE-2026-129474 on the defaults, when an application path enters a magic method ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2)). For CVE-2026-129289, PHP-FPM servers whose front end keeps FastCGI backend connections open (nginx fastcgi_keep_conn on, Apache mod_proxy_fcgi enablereuse=on, HAProxy in FastCGI mode) and whose applications open php://input without consuming it, which the PHP advisory says some frameworks do; standard nginx and Apache setups are outside the demonstrated attack ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6)). The session flaws need an object gadget chain in the application, and the version is shown by `php -v` on the host or in the container image.

**Detection:** in web and proxy access logs, malformed multipart/form-data bodies sent to endpoints whose application opens php://input without consuming it, followed by PHP execution that no logged request explains; in process telemetry, a shell or network tool spawned by the PHP-FPM worker, which follows from worker-level code execution.

**Defender takeaway:** move the PHP runtime, not the CMS or its plugins, to the fixed build of its branch and restart PHP-FPM; where that waits, turn FastCGI connection reuse off ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6)). PHP 8.1 hosts need a newer branch for CVE-2026-129291 ([PHP, 2026-11-19](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m)).
