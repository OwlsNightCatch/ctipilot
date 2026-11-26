---
schema: 1
kind: vulnerability
title: "Drupal core: SA-CORE-2026-017 and SA-CORE-2026-019 (CVE-2026-132165, CVE-2026-136716, both Highly critical) let an attacker use the installer to reinstall a site and take it over or run code, Drupal reports both exploited on live sites, and 11.4.14, 11.3.23 and 10.6.23 are the fixed releases that close both"
headline: "Drupal installer flaws SA-CORE-2026-017 and -019 exploited; update to 11.4.14, 11.3.23, 10.6.23 and run update.php"
summary: >
  Drupal published SA-CORE-2026-017 (CVE-2026-132165) and SA-CORE-2026-018 (CVE-2026-132166, Moderately critical, not directly exploitable) on 2026-11-18 and SA-CORE-2026-019 (CVE-2026-136716, Highly critical 21 of 25) on 2026-11-25: under specific conditions an attacker can use the installer to reinstall Drupal, which can lead to site takeover or remote code execution, and sites in unusual or incomplete install states stay open after the first fix. Drupal says both installer flaws are exploited on live sites (SA-CORE-2026-017 from 2026-11-19 19:00 UTC) and CISA listed CVE-2026-132165 as exploited on 2026-11-24; the fixed releases are 11.4.14, 11.3.23 and 10.6.23, update.php must be run, and securing the installer is strongly recommended.
discovered_at: "2026-11-18T05:09:00Z"
updated_at: "2026-11-26T05:06:50Z"
event_date: "2026-11-18"
run_id: 2026-11-18T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, pre-auth, rce, patch-available]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["Drupal Core"]
cves:
  - id: CVE-2026-132165
    cvss: "n/a"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "<10.6.22 || >=11.0.0 <11.3.22 || >=11.4.0 <11.4.13"
    fixed: "11.4.13, 11.3.22, 10.6.22"
  - id: CVE-2026-132166
    cvss: "n/a"
    epss: null
    type: deserialization
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: "<10.6.22 || >=11.0.0 <11.3.22 || >=11.4.0 <11.4.13"
    fixed: "11.4.13, 11.3.22, 10.6.22"
  - id: CVE-2026-136716
    cvss: "n/a"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "<10.6.23 || >=11.0.0 <11.3.23 || >=11.4.0 <11.4.14"
    fixed: "11.4.14, 11.3.23, 10.6.23"
sources:
  - url: "https://www.drupal.org/psa-2026-11-16"
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    date: "2026-11-16"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13196"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-17"
    role: corroborating
  - url: "https://www.drupal.org/sa-core-2026-017"
    publisher: "Drupal Security Team (SA-CORE-2026-017)"
    date: "2026-11-18"
    role: primary
  - url: "https://www.drupal.org/sa-core-2026-018"
    publisher: "Drupal Security Team (SA-CORE-2026-018)"
    date: "2026-11-18"
    role: primary
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0507.html"
    publisher: "NCSC-NL"
    date: "2026-11-18"
    role: corroborating
  - url: "https://www.drupal.org/sa-core-2026-019"
    publisher: "Drupal Security Team (SA-CORE-2026-019)"
    date: "2026-11-25"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-11-24"
    role: corroborating
  - url: "https://www.slcyber.io/research/fail2install-system-limits-pre-auth-rce-drupal"
    publisher: "Searchlight Cyber"
    date: "2026-11-24"
    role: corroborating
  - url: "https://www.stepsecurity.io/blog/fail2install-cve-2026-132165"
    publisher: "StepSecurity"
    date: "2026-11-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Drupal Security Team urges you to reserve time for core updates at that time because exploits might be developed within hours or days."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "The vulnerabilities are currently rated as critical and at least one can be exploited by anonymous users."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "Neither the Security Team nor any other party is able to release any more information about this vulnerability until the announcement is made."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "Under specific conditions, an attacker can use the installer to attempt to reinstall Drupal. This can lead to a site takeover or remote code execution."
    publisher: "Drupal Security Team (SA-CORE-2026-017)"
    source_url: "https://www.drupal.org/sa-core-2026-017"
  - quote: "Update: the Security Team has received a report this was exploited on live sites as early as 2026-11-19 19:00 UTC."
    publisher: "Drupal Security Team (SA-CORE-2026-017)"
    source_url: "https://www.drupal.org/sa-core-2026-017"
  - quote: "This issue is not directly exploitable."
    publisher: "Drupal Security Team (SA-CORE-2026-018)"
    source_url: "https://www.drupal.org/sa-core-2026-018"
  - quote: "This is being exploited in the wild. Any site that left its installer remotely accessible following SA-CORE-2026-017 may still have been compromised."
    publisher: "Drupal Security Team (SA-CORE-2026-019)"
    source_url: "https://www.drupal.org/sa-core-2026-019"
verification: multi-source
sourcing_note: >
  The Drupal Security Team is the disclosing party and the source for both exploitation reports (SA-CORE-2026-017 from 2026-11-19 and SA-CORE-2026-019); CISA's catalogue lists CVE-2026-132165 as exploited and names no actor or victim. StepSecurity reproduced the installer re-entry in its own lab on 11.4.12 and not on 11.4.13, and Searchlight Cyber's write-up gives the technique; neither reports observing exploitation itself. StepSecurity's statement that the stock .htaccess rule is unchanged in the fixed releases is one lab's test, and no source tests it on 11.4.14, 11.3.23 or 10.6.23. StepSecurity says no CVSS score exists yet, so none is recorded.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update every Drupal site to 11.4.14, 11.3.23 or 10.6.23 (a site on 11.4.13, 11.3.22 or 10.6.22 is still open to the second installer flaw) and run update.php, then on any site that ran an affected build with the installer reachable check the user 1 account, the administrators and settings.php for changes nobody made, because Drupal reports both installer flaws exploited on live sites."
updates:
  - at: "2026-11-19T05:02:14Z"
    run_id: 2026-11-19T0355Z-intel
    type: update
    summary: >
      Drupal published the announced core security release on 2026-11-18: SA-CORE-2026-017
      (CVE-2026-132165, Critical, installer reinstall leading to site takeover or remote code execution)
      and SA-CORE-2026-018 (CVE-2026-132166, not directly exploitable), fixed in 11.4.13, 11.3.22 and
      10.6.22. No exploitation is reported.
    fields: [actions, body, cves, event_date, evidence, headline, priority, sources, sourcing_note, summary, tags, title, updated_at]
  - at: "2026-11-22T14:46:42Z"
    run_id: 2026-11-22T1407Z-audit
    type: update
    summary: >
      Drupal revised SA-CORE-2026-017 to Highly critical (20 of 25, exploit status Exploit) and reports
      exploitation of CVE-2026-132165 on live sites from 2026-11-19 19:00 UTC; the fixed releases and the
      installer workaround are unchanged.
    fields: [actions, body, cves, evidence, headline, priority, sourcing_note, summary, tags, title]
  - at: "2026-11-26T05:06:50Z"
    run_id: 2026-11-26T0356Z-intel
    type: update
    summary: >
      Drupal published SA-CORE-2026-019 on 2026-11-25 (CVE-2026-136716, Highly critical 21 of 25), a second installer flaw
      under which sites in unusual or incomplete install states stay open after the first fix, exploited in the wild
      according to Drupal; the fixed releases move to 11.4.14, 11.3.23 and 10.6.23 and update.php must be run. CISA listed
      CVE-2026-132165 as exploited on 2026-11-24, and Searchlight Cyber and StepSecurity published the technique and a
      reproduction.
    fields: [title, headline, summary, tags, cves, sources, evidence, verification, sourcing_note, classification, actions, body, updated_at]
migrated_from: null
---

Drupal shipped its core security release on 2026-11-18 and added a second installer advisory on 2026-11-25. SA-CORE-2026-017 (CVE-2026-132165, Highly critical 20 of 25) says that under specific conditions an attacker can use the installer to attempt to reinstall Drupal, which can lead to a site takeover or remote code execution ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)); SA-CORE-2026-018 (CVE-2026-132166, Moderately critical 14 of 25) is a gadget chain that Drupal says is not directly exploitable ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-018)). SA-CORE-2026-019 (CVE-2026-136716, Highly critical 21 of 25) says certain sites in unusual or incomplete install states remain open to takeover after the first fix, that the user interface does not show whether a site is in that state, and that it is being exploited in the wild ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)). Drupal reports SA-CORE-2026-017 exploited on live sites from 2026-11-19 19:00 UTC ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)), and CISA listed CVE-2026-132165 as exploited on 2026-11-24 ([CISA, 2026-11-24](https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog)).

Affected are core before 10.6.23, from 11.0.0 before 11.3.23 and from 11.4.0 before 11.4.14, with 11.4.14, 11.3.23 and 10.6.23 as the fixed releases, so a site on 11.4.13, 11.3.22 or 10.6.22, the fixed releases of the first advisory, is still open to the second; update.php must be run because an update hook repairs sites already in that state ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)). Drupal says a site that has secured the installer is not vulnerable and strongly recommends securing it everywhere, that Drupal 8 and 9, 10.5.x and below and 11.2.x and below are end of life with no fix, and that Drupal Steward covers both advisories ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)). Searchlight Cyber's write-up turns database or source-port exhaustion into installer re-entry and code execution on Drupal's official images ([Searchlight Cyber, 2026-11-24](https://www.slcyber.io/research/fail2install-system-limits-pre-auth-rce-drupal)), while Drupal rates the target distribution Uncommon ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)). StepSecurity reproduced the re-entry on 11.4.12 and not on 11.4.13 and says the stock .htaccess rule blocking direct PHP requests is unchanged, so code execution survives for an attacker who can write a PHP file into a code directory; no source tests the newest builds ([StepSecurity, 2026-11-26](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165)).

**Exposure:** any Drupal site on core before 11.4.14, 11.3.23 or 10.6.23 whose /core/install.php can be requested from outside, and every site on an end-of-life line, which has no fix; patched Drupal publishes only its major version, so check the installer path and the drupal/core version the site was built from ([StepSecurity, 2026-11-26](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165)). NCSC-NL says the condition arises when the installer is not correctly secured or removed after the initial installation (translated from Dutch) ([NCSC-NL, 2026-11-18](https://advisories.ncsc.nl/2026/ncsc-2026-0507.html)).

**Detection:** web access logs for requests to the installer on a site that is already installed and, as StepSecurity describes, a burst of database connection-refusal errors together with a burst of HTTP 500 responses and requests to install.php; on a site that ran an affected build, changes to settings.php, a later install time or a changed user 1 ([StepSecurity, 2026-11-26](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165)). Drupal advises checking logs for unexpected changes to or by the user 1 account ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)).

**Defender takeaway:** update each site to 11.4.14, 11.3.23 or 10.6.23 out of cycle, run update.php, secure the installer and move end-of-life sites to a supported branch; on any site that ran an affected build with the installer reachable, check user 1, the administrators and settings.php, since patching does not undo a takeover ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)).

## Update — 2026-11-19T05:02:14Z

The release the pre-announcement described is out. Drupal published SA-CORE-2026-017 (CVE-2026-132165, Critical 18 of 25) and SA-CORE-2026-018 (CVE-2026-132166, Moderately critical 14 of 25, not directly exploitable) on 2026-11-18, fixed in Drupal 11.4.13, 11.3.22 and 10.6.22 ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017), [Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-018)). SA-CORE-2026-017 says an attacker can use the installer to attempt to reinstall Drupal, which can lead to a site takeover or remote code execution, and the only workaround is to secure the installer ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). The 18 of 25 rating in the pre-announcement is SA-CORE-2026-017's; neither advisory reports exploitation.

## Update — 2026-11-22T14:46:42Z

Drupal revised SA-CORE-2026-017 after the release: it now rates CVE-2026-132165 Highly critical 20 of 25, with exploit status Exploit, and says the Security Team received a report that the flaw was exploited on live sites as early as 2026-11-19 19:00 UTC ([Drupal Security Team, 2026-11-18](https://www.drupal.org/sa-core-2026-017)). The fixed releases (11.4.13, 11.3.22, 10.6.22) and the installer workaround are unchanged.

## Update — 2026-11-26T05:06:50Z

Drupal published SA-CORE-2026-019 on 2026-11-25: CVE-2026-136716, Highly critical 21 of 25, a second installer flaw under which sites in unusual or incomplete install states stay open to takeover after the first fix, exploited in the wild according to Drupal, with 11.4.14, 11.3.23 and 10.6.23 as the fixed releases and a required update.php run ([Drupal Security Team, 2026-11-25](https://www.drupal.org/sa-core-2026-019)). CISA added CVE-2026-132165 to its Known Exploited Vulnerabilities catalogue on 2026-11-24, and the newer flaw is not on the list ([CISA, 2026-11-24](https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog)). Searchlight Cyber published the technique on 2026-11-24 and StepSecurity published its reproduction of the installer re-entry on 2026-11-26, and neither reports observing exploitation itself (their statements repeat Drupal's report) ([Searchlight Cyber, 2026-11-24](https://www.slcyber.io/research/fail2install-system-limits-pre-auth-rce-drupal); [StepSecurity, 2026-11-26](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165)).
