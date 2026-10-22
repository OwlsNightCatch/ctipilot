---
schema: 1
kind: vulnerability
title: "cPanel & WHM security update of 2026-05-08: CVE-2026-29202 Perl code injection, CVE-2026-29203 symlink chmod and CVE-2026-29201 arbitrary file read"
headline: "cPanel patches authenticated Perl code injection (CVE-2026-29202) and two file-permission flaws across cPanel & WHM"
summary: "cPanel released fixes on 2026-05-08 for three cPanel & WHM and WP Squared flaws: CVE-2026-29202 lets an authenticated account run arbitrary Perl code as its system user through the create_user API, CVE-2026-29203 lets a user chmod an arbitrary file through a symlink, and CVE-2026-29201 makes an arbitrary file world-readable. Every supported branch is patched, and no exploitation was reported at disclosure."
discovered_at: "2026-05-10T05:00:10Z"
event_date: 2026-05-08
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - patch-available
regions:
  - global
sectors:
  - technology
entities: []
techniques: [T1059, T1068, T1005]
affected_products: ["cPanel & WHM", "WP Squared"]
cves:
  - id: CVE-2026-29202
    cvss: "5.3 (CVSS 4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "cPanel & WHM versions before the fixed release of each supported branch; WP Squared before version 11.136.1.11"
    fixed: "cPanel & WHM version 11.136.0.9, 11.134.0.25, 11.132.0.31, 11.130.0.22, 11.126.0.58, 11.124.0.37, 11.118.0.66, 11.110.0.117, 11.102.0.41, 11.94.0.30 or 11.86.0.43; WP Squared version 11.136.1.11; version 11.110.0.116 for CentOS 6 and CloudLinux 6"
  - id: CVE-2026-29203
    cvss: "5.3 (CVSS 4.0)"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "cPanel & WHM versions before the fixed release of each supported branch; WP Squared before version 11.136.1.11"
    fixed: "cPanel & WHM version 11.136.0.9, 11.134.0.25, 11.132.0.31, 11.130.0.22, 11.126.0.58, 11.124.0.37, 11.118.0.66, 11.110.0.117, 11.102.0.41, 11.94.0.30 or 11.86.0.43; WP Squared version 11.136.1.11; version 11.110.0.116 for CentOS 6 and CloudLinux 6"
  - id: CVE-2026-29201
    cvss: "8.6 (CVSS 3.1)"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "cPanel & WHM versions before the fixed release of each supported branch; WP Squared before version 11.136.1.11"
    fixed: "cPanel & WHM version 11.136.0.9, 11.134.0.25, 11.132.0.31, 11.130.0.22, 11.126.0.58, 11.124.0.37, 11.118.0.66, 11.110.0.117, 11.102.0.41, 11.94.0.30 or 11.86.0.43; WP Squared version 11.136.1.11; version 11.110.0.116 for CloudLinux 6"
sources:
  - url: "https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html"
    publisher: "The Hacker News"
    date: "2026-05-09"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/api/posts/12550/details"
    publisher: "NCSC-CH Security Hub post 12550"
    date: "2026-05-08"
    role: corroborating
  - url: "https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026"
    publisher: "cPanel (CVE-2026-29202 advisory)"
    date: "2026-05-08"
    role: primary
  - url: "https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026"
    publisher: "cPanel (CVE-2026-29203 advisory)"
    date: "2026-05-08"
    role: primary
  - url: "https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026"
    publisher: "cPanel (CVE-2026-29201 advisory)"
    date: "2026-05-08"
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28811"
    publisher: "ENISA EUVD (EUVD-2026-28811, CVE-2026-29202)"
    date: "2026-05-08"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28812"
    publisher: "ENISA EUVD (EUVD-2026-28812, CVE-2026-29203)"
    date: "2026-05-08"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28810"
    publisher: "ENISA EUVD (EUVD-2026-28810, CVE-2026-29201)"
    date: "2026-05-08"
    role: corroborating
  - url: "https://support.cpanel.net/hc/en-us/articles/40073787579671-Security-CVE-2026-41940-cPanel-WHM-WP2-Security-Update-04-28-2026"
    publisher: "cPanel (CVE-2026-41940 advisory)"
    date: "2026-04-28"
    role: corroborating
  - url: "https://www.securityweek.com/critical-cpanel-whm-vulnerability-exploited-as-zero-day-for-months/"
    publisher: "SecurityWeek"
    date: "2026-04-30"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html"
    publisher: "The Hacker News"
    date: "2026-05-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A Perl code injection method was found in the `create_user` API call, relating to the `plugin` parameter."
    publisher: "cPanel (CVE-2026-29202 advisory)"
    source_url: "https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026"
  - quote: "An unsafe symlink handling error was found that allows a user to `chmod` an arbitrary file, allowing for denial of service and possible privilege escalation."
    publisher: "cPanel (CVE-2026-29203 advisory)"
    source_url: "https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026"
  - quote: "A relative path may be passed as the argument to this call, causing an arbitrary file to be made world-readable."
    publisher: "cPanel (CVE-2026-29201 advisory)"
    source_url: "https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026"
  - quote: "that could result in arbitrary Perl code execution on behalf of the already authenticated account's system user."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html"
  - quote: "While there is no evidence that the vulnerabilities have been exploited in the wild"
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html"
  - quote: "Per data from the Shadowserver Foundation, at least 44,000 IP addresses likely compromised via CVE-2026-41940 are said to have"
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html"
verification: multi-source
sourcing_note: >
  cPanel's per-CVE advisories carry the flaws and the fixed releases, and the scores are the CVE records', assigned by HackerOne as numbering authority, as
  ENISA's EUVD records them. The Hacker News reports different CVSS 3.1 scores (8.8 for CVE-2026-29202 and CVE-2026-29203, 4.3 for
  CVE-2026-29201).
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-10-21T20:29:26Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The CVE records, assigned by HackerOne as numbering authority, score CVE-2026-29202 and
      CVE-2026-29203 at 5.3 under CVSS 4.0 and CVE-2026-29201 at 8.6, while The Hacker News reports 8.8,
      8.8 and 4.3; only CVE-2026-29202 is code execution, CVE-2026-29203 is a symlink chmod flaw and
      CVE-2026-29201 an arbitrary file read. Every supported branch from 11.86 to 11.136 and WP Squared is
      patched as of 2026-05-08, and no source describes chaining the flaws with the earlier CVE-2026-41940
      bypass, which Shadowserver tied to at least 44,000 likely compromised IP addresses on one day rather
      than to 44,000 hosts over two months.
    fields: [affected_products, body, classification, cves, event_date, evidence, headline, priority, sources, sourcing_note, summary, techniques, title]
---

cPanel published patches and one advisory per CVE for three cPanel & WHM and WP Squared vulnerabilities on 2026-05-08 ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)). CVE-2026-29202 is a Perl code-injection flaw in the plugin parameter of the create_user API call ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)) that gives arbitrary Perl code execution as the already authenticated account's system user ([The Hacker News, 2026-05-09](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html)). CVE-2026-29203 is an unsafe symlink handling error that lets a user chmod an arbitrary file, allowing denial of service and possible privilege escalation ([cPanel, CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)). CVE-2026-29201 is an arbitrary file read in the feature::LOADFEATUREFILE adminbin call, where a relative path in the feature file name makes an arbitrary file world-readable ([cPanel, CVE-2026-29201](https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026)). The CVE records, as ENISA's EUVD carries them, score CVE-2026-29202 and CVE-2026-29203 at 5.3 under CVSS 4.0 ([EUVD-2026-28811](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28811); [EUVD-2026-28812](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28812)) and CVE-2026-29201 at 8.6 under CVSS 3.1 with no privileges required ([EUVD-2026-28810](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28810)); The Hacker News reports 8.8, 8.8 and 4.3, and no evidence of exploitation in the wild as of 2026-05-09 ([The Hacker News, 2026-05-09](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html)).

The fixed releases are cPanel & WHM version 11.136.0.9, 11.134.0.25, 11.132.0.31, 11.130.0.22, 11.126.0.58, 11.124.0.37, 11.118.0.66, 11.110.0.117, 11.102.0.41, 11.94.0.30 and 11.86.0.43 or higher, WP Squared version 11.136.1.11 or higher, and version 11.110.0.116 as a direct update for CentOS 6 and CloudLinux 6 ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)). The update followed by ten days cPanel's advisory for CVE-2026-41940, an authentication bypass ([cPanel, CVE-2026-41940](https://support.cpanel.net/hc/en-us/articles/40073787579671-Security-CVE-2026-41940-cPanel-WHM-WP2-Security-Update-04-28-2026)) that hosting provider KnownHost reported exploited in the wild since 2026-02-23 ([SecurityWeek, 2026-04-30](https://www.securityweek.com/critical-cpanel-whm-vulnerability-exploited-as-zero-day-for-months/)); Shadowserver counted at least 44,000 IP addresses likely compromised through it scanning its honeypots on 2026-04-30 ([The Hacker News, 2026-05-04](https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html)).

**Exposure:** every cPanel & WHM and WP Squared server below the fixed release of its branch; CVE-2026-29202 needs an authenticated account ([The Hacker News, 2026-05-09](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html)) and CVE-2026-29203 a user on the server ([cPanel, CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)). The patch ships through the standard automatic update, so servers with automatic updates disabled or version-pinned in the update configuration are the ones left behind ([NCSC-CH, 2026-05-08](https://security-hub.ncsc.admin.ch/api/posts/12550/details)), and the running version is read with /usr/local/cpanel/cpanel -V ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)).

**Detection:** file-permission telemetry on the server: the two file flaws show as system files made world-readable through the adminbin call ([cPanel, CVE-2026-29201](https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026)) or chmod'ed through a symlink by a user account ([cPanel, CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)).

**Defender takeaway:** no out-of-band action where automatic updates run; on pinned or manually updated servers run /scripts/upcp --force and confirm the version afterwards, as cPanel instructs ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)).

## Correction — 2026-10-21T20:29:26Z

The CVE records, as ENISA's EUVD carries them, score 5.3 under CVSS 4.0 for CVE-2026-29202 and CVE-2026-29203 ([EUVD-2026-28811](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28811); [EUVD-2026-28812](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28812)) and 8.6 under CVSS 3.1 for CVE-2026-29201 ([EUVD-2026-28810](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28810)); the 8.8, 8.8 and 4.3 figures are The Hacker News's ([The Hacker News, 2026-05-09](https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html)). Only CVE-2026-29202 yields code execution: CVE-2026-29203 lets a user chmod an arbitrary file ([cPanel, CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)) and CVE-2026-29201 makes an arbitrary file world-readable ([cPanel, CVE-2026-29201](https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026)). The patch and the advisories were published together on 2026-05-08, and the fix covers eleven cPanel & WHM branches from 11.86 to 11.136 and WP Squared, not three ([cPanel, CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)). For CVE-2026-41940, Shadowserver counted at least 44,000 likely compromised IP addresses scanning its honeypots on 2026-04-30 ([The Hacker News, 2026-05-04](https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html)), and KnownHost reported exploitation since 2026-02-23 ([SecurityWeek, 2026-04-30](https://www.securityweek.com/critical-cpanel-whm-vulnerability-exploited-as-zero-day-for-months/)); no source describes attackers chaining it with CVE-2026-29202.
