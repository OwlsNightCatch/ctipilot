---
title: Releases · Cacti/cacti
url: https://github.com/Cacti/cacti/releases
hostname: github.com
description: Cacti ™. Contribute to Cacti/cacti development by creating an account on GitHub.
sitename: GitHub
date: "2026-02-01"
categories: ['repository:29455529']
fingerprint: e0467f1eda3c5dd8
language: en
image: https://repository-images.githubusercontent.com/29455529/565e5980-aa45-11e9-9ab9-b4d418e35dcd
pagetype: object
filedate: "2026-11-28"
---
## Repository navigation

# Releases

## v1.2.31

# Release of Cacti 1.2.31

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

# Project Updates

This release is marked by the loss of a valued core member of the Cacti family, **Jeff Pasnak** (aka linegod). Jeff was one of our longest-serving core contributors, and his dedication, knowledge, and countless hours of work helped shape the project over many years. His contributions left a lasting impact on both the codebase and the community that surrounds it. While his legacy can be measured in commits, fixes, and features, his influence extended far beyond the software itself.

**TheWitness:** "*Learning of Jeff's passing was humbling and sad moment for us at The Cacti Group.  Jeff was always that salty kind of guy who injected his rare form of humor into any conversation.  There is this saying that we have here in the US, that it's better to be picked on then left alone, cause if you are being picked on, at least you know that that someone still cares.  That was Jeff to the tee.  He introduced us to Strongbow Cider as the only good Cider and Shepherds Pie in our team meetings in San Francisco in the late 2000's.  He had a quick whit, and his encyclopedic mind on all things "every movie ever made" that kept us laughing.  He was a good friend to all of us.  We always knew that if we went to him, we would get the naked truth.  It was up to us to be prepared and accept it.  He will be missed by the entire team.  Rest in peace buddy!*"

**cigamit:** "*His quick wit made us laugh, his kindness made us better, and his presence turned ordinary moments into lasting traditions that will outlive us all. We will miss him dearly, until we share another cider again, good buddy.*"

**netniV:** "*His knowledge and eagle eyes would always find the many typos we managed to introduce into documentation and code. His honest opinions, attention to detail, and helpful nature will be deeply missed.*"

On behalf of the entire project, we extend our gratitude for everything Jeff contributed and our deepest condolences to his family, friends, and colleagues. His work will continue to live on through the project he helped build, and he will be remembered with great respect and appreciation.

# Security and Platform Updates

Security remains a fundamental priority for the Cacti project. Throughout this release cycle, the development team has continued to invest in code reviews, vulnerability assessments, dependency maintenance, and quality assurance efforts designed to identify and address potential security concerns before they impact users. Protecting the integrity, availability, and reliability of Cacti installations remains central to our development philosophy, and we encourage the community to continue reporting issues responsibly so they can be addressed promptly.

This release includes fixes for a number of vulnerabilities that were responsibly disclosed by external researchers. We would like to thank those individuals and organizations for reporting issues privately and for their patience while the team completed remediation, testing, and validation. Responsible disclosure plays an important role in strengthening open-source software, and we greatly value the collaboration of the security community in helping keep Cacti secure.

As part of our ongoing commitment to security and maintainability, the minimum supported PHP version has now been raised to ***PHP 8.1***. While we recognize that some deployments continue to run on older PHP releases, those versions have long since reached end-of-life and no longer receive security updates. Moving to a modern supported platform allows us to continue improving Cacti while meeting current security and development requirements.

Finally, we would like to thank the many contributors, testers, users, and community members who continue to support Cacti. Open-source software is a collective effort, and the strength of this community ensures that the project will continue to grow and evolve for years to come.

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-23g4-vf2j-94w4](https://github.com/Cacti/cacti/security/advisories/GHSA-23g4-vf2j-94w4): CVE-2026-39894 RRDtool metric shift via LC\_NUMERIC locale comma decimal formatting
- security #[GHSA-273r-qr93-wgcp](https://github.com/Cacti/cacti/security/advisories/GHSA-273r-qr93-wgcp): CVE-2026-40082 Session Fixation via missing session\_regenerate\_id() after login
- security #[GHSA-274c-97hj-pv2v](https://github.com/Cacti/cacti/security/advisories/GHSA-274c-97hj-pv2v): CVE-2026-40941 Package Import Signature Validation Bypass allows self-signed packages
- security #[GHSA-2j98-xfjq-gw39](https://github.com/Cacti/cacti/security/advisories/GHSA-2j98-xfjq-gw39): CVE-2026-39897 Reflected XSS in html\_auth\_footer error message output
- security #[GHSA-34rf-frc3-v48r](https://github.com/Cacti/cacti/security/advisories/GHSA-34rf-frc3-v48r): CVE-2026-39900 Reflected XSS via tab parameter in auth\_profile.php JavaScript context
- security #[GHSA-37jj-rx8x-4wf2](https://github.com/Cacti/cacti/security/advisories/GHSA-37jj-rx8x-4wf2): CVE-2026-46531 SQL Injection in automation\_tree\_rules.php
- security #GHSA-3vj5-jqr9-q8hg: CVE-2026-44481 Pre-auth Open Redirect via link.php Referer header
- security #GHSA-6233-v5hc-6gvf: CVE-2026-39952 Stored XSS in Report Tree expansion titles
- security #[GHSA-69gg-mjfm-jjpc](https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc): CVE-2026-39893 Pre-authentication SQL injection via rfilter RLIKE clause in graph\_view.php
- security #GHSA-6rvg-2vm8-5wrf: CVE-2026-22802 Authentication Bypass leads to information disclosure
- security #[GHSA-6gr7-53g8-vchq](https://github.com/Cacti/cacti/security/advisories/GHSA-6gr7-53g8-vchq): CVE-2026-40080 Open Redirect via HTTP\_REFERER substring check in auth\_login\_redirect
- security #GHSA-84q3-92xc-c3pf: CVE-2026-40078 Backend ORDER BY SQL Injection
- security #GHSA-8522-5p3m-754c: CVE-2026-39949 Authenticated Remote Code Execution via Host Variable Injection
- security #GHSA-8p2f-6jvx-j75j: CVE-2026-40081 Reports IDOR allows any authenticated user to modify other users' reports (CWE-639)
- security #[GHSA-9jqv-4cpm-vm2c](https://github.com/Cacti/cacti/security/advisories/GHSA-9jqv-4cpm-vm2c): CVE-2026-39948 SQL Injection via rfilter parameter in RLIKE clauses
- security #[GHSA-c4qp-j9r9-fq24](https://github.com/Cacti/cacti/security/advisories/GHSA-c4qp-j9r9-fq24): CVE-2026-39902 Authenticated RCE on Data Input
- security #GHSA-fwh3-8c8r-378r: CVE-2026-39898 Reflected XSS via rfilter parameter in aggregate\_graphs.php input value
- security #GHSA-g37j-39f4-6r4j: CVE-2026-41884 Arbitrary File Read via Reports format\_file path traversal
- security #[GHSA-gp82-qhrg-crv7](https://github.com/Cacti/cacti/security/advisories/GHSA-gp82-qhrg-crv7): CVE-2026-39955 Pre-Authentication SQL Injection via unanchored FILTER\_VALIDATE\_REGEXP in graph\_view.php
- security #GHSA-hr82-h9vr-587w: CVE-2026-39896 TOCTOU race in auth\_process\_lockout allows brute-force lockout bypass
- security #GHSA-j696-m433-87qq: CVE-2026-39950 Arbitrary PHP file write via Plugin Archive extraction leading to RCE
- security #[GHSA-j9jv-6xjq-9hhj](https://github.com/Cacti/cacti/security/advisories/GHSA-j9jv-6xjq-9hhj): CVE-2026-40083 SQL Injection in managers.php via uncast array values in IN clauses
- security #[GHSA-m7v2-f3xw-3qh7](https://github.com/Cacti/cacti/security/advisories/GHSA-m7v2-f3xw-3qh7): User Enumeration via Error Messages
- security #[GHSA-mjvw-mhj5-9jcj](https://github.com/Cacti/cacti/security/advisories/GHSA-mjvw-mhj5-9jcj): CVE-2026-40084 Arbitrary File Read via path traversal in Report format\_file parameter
- security #[GHSA-pf37-v86f-5xwp](https://github.com/Cacti/cacti/security/advisories/GHSA-pf37-v86f-5xwp): CVE-2026-39951 Stored SQL Injection via graph\_name\_regexp in Reports feature
- security #[GHSA-pr9x-34w8-4mf7](https://github.com/Cacti/cacti/security/advisories/GHSA-pr9x-34w8-4mf7): CVE-2026-39899 Path traversal via filename parameter in package\_import.php
- security #[GHSA-rm7p-qcqm-x5m6](https://github.com/Cacti/cacti/security/advisories/GHSA-rm7p-qcqm-x5m6): CVE-2026-39938 Unauthenticated LFI via graph\_theme and rrdtool IPC serialization hardening
- security #GHSA-vp35-4h28-r883: CVE-2026-39939 Path traversal in Package Import file write allows arbitrary file creation in webroot
- security #GHSA-w47c-53f9-w47g: CVE-2026-39947 RRDtool IPC pipe poisoning via is\_numeric newline bypass in rrdtool\_function\_update
- security #GHSA-wpjq-m269-mghj: CVE-2026-39895 Second-order RCE via unescaped log path in exec\_background shell redirection
- security #[GHSA-xq98-376r-hv9j](https://github.com/Cacti/cacti/security/advisories/GHSA-xq98-376r-hv9j): CVE-2026-40079 Command Injection via escape\_command() no-op in RRDtool execution
- security: [CVE-2026-40194](https://github.com/advisories/GHSA-r854-jrxh-36qx), [CVE-2026-32935](https://github.com/advisories/GHSA-94g3-g5v7-q4jg) in phpseclib - This is breaking change for RRDProxy
- security: [CVE-2026-1513](https://github.com/advisories/GHSA-rpc5-pm7q-hjmp) billboard.js before 3.18.0 Improper Input Sanitization Allows Remote JavaScript Execution
- issue [#6168](https://github.com/Cacti/cacti/issues/6168): When purging RRD files, paths are not correctly handled
- issue [#6202](https://github.com/Cacti/cacti/issues/6202): When using automation, devices may not be added as expected
- issue [#6204](https://github.com/Cacti/cacti/issues/6204): Attempting to match a field in automation may cause unexpected errors
- issue [#6210](https://github.com/Cacti/cacti/issues/6210): Ensure column names are escaped to prevent reserved word issues
- issue [#6240](https://github.com/Cacti/cacti/issues/6240): Improve sort order for incorrect RRA's
- issue [#6249](https://github.com/Cacti/cacti/issues/6249): Unable to send Email to users without a domain name
- issue [#6251](https://github.com/Cacti/cacti/issues/6251): When viewing a graph, do not produce unnecessary errors if graph has been removed
- issue [#6253](https://github.com/Cacti/cacti/pull/6253): When i18n formatting numbers, assume null means 0 by xmacan
- issue [#6257](https://github.com/Cacti/cacti/pull/6257): When data sources are removed, ensure only RRD files are removed by xmacan
- issue [#6262](https://github.com/Cacti/cacti/issues/6262): When the database connection drops during query, retry to ensure success
- issue [#6270](https://github.com/Cacti/cacti/issues/6270): Incorrect escaping may prevent drop downs working as intended
- issue [#6271](https://github.com/Cacti/cacti/issues/6271): When validation errors occur, provide more information to help diagnosis
- issue [#6283](https://github.com/Cacti/cacti/issues/6283): When calculating total pages, ensure math errors do not occur
- issue [#6292](https://github.com/Cacti/cacti/issues/6292): When validating null request variables, fatal errors may occur
- issue [#6294](https://github.com/Cacti/cacti/issues/6294): Automation may produce unexpected warnings when detecting the OS
- issue [#6296](https://github.com/Cacti/cacti/issues/6296): Process timeouts may not end processes as expected
- issue [#6297](https://github.com/Cacti/cacti/issues/6297): Improve support for Secure SMTP
- issue [#6299](https://github.com/Cacti/cacti/issues/6299): Improve email address handling to support UTF8
- issue [#6313](https://github.com/Cacti/cacti/issues/6313): When editing multiple devices, unexpected errors may be recorded
- issue [#6314](https://github.com/Cacti/cacti/issues/6314): When editing an Aggregation Graph, total count may not reflect number of items correctly
- issue [#6315](https://github.com/Cacti/cacti/issues/6315): When duplicating a Data Input Method, unexpected errors may occur
- issue [#6326](https://github.com/Cacti/cacti/issues/6326): Improve SNMP v3 support for Cisco devices
- issue [#6327](https://github.com/Cacti/cacti/issues/6327): Implement Autocomplete standards for Login and Change Password
- issue [#6329](https://github.com/Cacti/cacti/issues/6329): When using LDAP, checking a user's g...

[Read more](https://github.com/Cacti/cacti/releases/tag/release%2F1.2.31)

## v1.2.30

# Release of Cacti 1.2.30

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- issue [#6089](https://github.com/Cacti/cacti/issues/6089): Unable to add new users
- issue [#6090](https://github.com/Cacti/cacti/issues/6090): When using Automation Rules, specifying graph criteria may cause issues
- issue [#6099](https://github.com/Cacti/cacti/issues/6099): When transferring a system from a backup if the poller has not run recently rrdtool issues are found
- issue [#6172](https://github.com/Cacti/cacti/issues/6172): When translating, quotes may cause incorrect text to appear
- issue [#6173](https://github.com/Cacti/cacti/issues/6173): When using Boost for the first time, warnings may appear
- issue [#6183](https://github.com/Cacti/cacti/pull/6183): When refreshing forms, items may be checked incorrectly by xmacan

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.29

# Release of Cacti 1.2.29

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-c5j8-jxj3-hh36](https://github.com/Cacti/cacti/security/advisories/GHSA-c5j8-jxj3-hh36): Authenticated RCE via multi-line SNMP responses
- security #[GHSA-f9c7-7rc3-574c](https://github.com/Cacti/cacti/security/advisories/GHSA-f9c7-7rc3-574c): SQL Injection vulnerability when using tree rules through Automation API
- security #[GHSA-fh3x-69rr-qqpp](https://github.com/Cacti/cacti/security/advisories/GHSA-fh3x-69rr-qqpp): SQL Injection vulnerability when request automation devices
- security #[GHSA-fxrq-fr7h-9rqq](https://github.com/Cacti/cacti/security/advisories/GHSA-fxrq-fr7h-9rqq): Arbitrary File Creation leading to RCE
- security #[GHSA-pv2c-97pp-vxwg](https://github.com/Cacti/cacti/security/advisories/GHSA-pv2c-97pp-vxwg): Local File Inclusion (LFI) Vulnerability via Poller Standard Error Log Path
- security #[GHSA-vj9g-p7f2-4wqj](https://github.com/Cacti/cacti/security/advisories/GHSA-vj9g-p7f2-4wqj): SQL Injection vulnerability when view host template
- issue [#5843](https://github.com/Cacti/cacti/issues/5843): Temporary table names may incorrectly think they have a schema
- issue [#5847](https://github.com/Cacti/cacti/issues/5847): When using Preset Time to view graphs, it is using a fixed point rather than relative time
- issue [#5848](https://github.com/Cacti/cacti/issues/5848): Fix issue where RRA files are not automatically removed
- issue [#5856](https://github.com/Cacti/cacti/issues/5856): Fix invalid help link for Automation Networks
- issue [#5867](https://github.com/Cacti/cacti/issues/5867): Unable to disable a tree within the GUI
- issue [#5868](https://github.com/Cacti/cacti/issues/5868): When removing graphs, RRA files may be left behind
- issue [#5869](https://github.com/Cacti/cacti/pull/5869): Improve compatibility with ping under FreeBSD
- issue [#5870](https://github.com/Cacti/cacti/issues/5870): Improve compatibility wtih Slice RRD tool under PHP 8.x
- issue [#5874](https://github.com/Cacti/cacti/issues/5874): Allow IPv6 formats to use colons without port
- issue [#5884](https://github.com/Cacti/cacti/pull/5884): Update Fortigate, Aruba OSCX and Clearpass templates
- issue [#5927](https://github.com/Cacti/cacti/issues/5927): When a plugin is disabled, unable to use GUI to enable it again
- issue [#5932](https://github.com/Cacti/cacti/issues/5932): When upgrading, ensure that replication only runs as necessary
- issue [#5961](https://github.com/Cacti/cacti/issues/5961): Improve caching and syncing issues with replication
- issue [#5963](https://github.com/Cacti/cacti/issues/5963): Improve caching techniques for database calls
- issue [#5986](https://github.com/Cacti/cacti/issues/5986): Improve compatibility for Error constants under PHP 8.4
- issue [#5987](https://github.com/Cacti/cacti/issues/5987): When running the upgrade database script, cursor is left in the middle of the row
- issue [#6065](https://github.com/Cacti/cacti/issues/6065): Guest page does not automatically refresh
- issue [#6078](https://github.com/Cacti/cacti/issues/6078): When installing, conversion of tables may produce collation errors
- feature [#5921](https://github.com/Cacti/cacti/pull/5921): Add HPE Nimble/Alletra template
- feature [#5933](https://github.com/Cacti/cacti/issues/5933): When installing, only convert core cacti tables

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.28

# Release of Cacti 1.2.28

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-49f2-hwx9-qffr](https://github.com/Cacti/cacti/security/advisories/GHSA-49f2-hwx9-qffr): XSS vulnerability when creating external links with the consolenewsection parameter
- security #[GHSA-fgc6-g8gc-wcg5](https://github.com/Cacti/cacti/security/advisories/GHSA-fgc6-g8gc-wcg5): XSS vulnerability when creating external links with the title parameter
- security #[GHSA-gxq4-mv8h-6qj4](https://github.com/Cacti/cacti/security/advisories/GHSA-gxq4-mv8h-6qj4): RCE vulnerability can be executed via Log Poisoning
- security #[GHSA-wh9c-v56x-v77c](https://github.com/Cacti/cacti/security/advisories/GHSA-wh9c-v56x-v77c): XSS vulnerability when creating external links with the fileurl parameter
- issue [#5636](https://github.com/Cacti/cacti/issues/5636): When using LDAP authentication the first time, warnings may appear in logs
- issue [#5754](https://github.com/Cacti/cacti/issues/5754): When installing, a replication loop for plugin\_realms may occur
- issue [#5759](https://github.com/Cacti/cacti/issues/5759): When installing, remote poller may attempt to sync with other pollers
- issue [#5768](https://github.com/Cacti/cacti/issues/5768): When a Data Query has a space, indexes may not be properly escaped
- issue [#5771](https://github.com/Cacti/cacti/issues/5771): Boost does not always order data source records properly
- issue [#5772](https://github.com/Cacti/cacti/pull/5772): Add IP address to the login audit for successful logins by xmacan
- issue [#5773](https://github.com/Cacti/cacti/pull/5773): Undefined variable error may sometimes occur when dealing with RRD output by MSS970
- issue [#5777](https://github.com/Cacti/cacti/issues/5777): When export to CSV, only the first line of notes is included
- issue [#5780](https://github.com/Cacti/cacti/issues/5780): When rendering forms, missing default value can cause errors
- issue [#5782](https://github.com/Cacti/cacti/issues/5782): Allow hosted content to be executable for the links page
- issue [#5783](https://github.com/Cacti/cacti/issues/5783): When closing database connections, some may linger incorrectly
- issue [#5785](https://github.com/Cacti/cacti/pull/5785): When changing passwords, an infinite loop may occur by ddb4github
- issue [#5790](https://github.com/Cacti/cacti/issues/5790): When using Cacti Daemon, a "Cron out of sync" message may be reported
- issue [#5791](https://github.com/Cacti/cacti/issues/5791): Add ability to filter/sort users by group or last login time
- issue [#5792](https://github.com/Cacti/cacti/issues/5792): When using List View, unable to add Graphs to a Report
- issue [#5797](https://github.com/Cacti/cacti/issues/5797): When using SNMPv3, some devices may show polling issues
- issue [#5802](https://github.com/Cacti/cacti/issues/5802): Limit table conversion to Cacti core tables
- issue [#5806](https://github.com/Cacti/cacti/issues/5806): Fix issues with posix-based kills on Windows
- issue [#5813](https://github.com/Cacti/cacti/issues/5813): When installing, password changes may fail on new installations
- issue [#5814](https://github.com/Cacti/cacti/issues/5814): When using structured RRD folders, permission issues may be flagged incorrectly
- issue [#5823](https://github.com/Cacti/cacti/issues/5823): When unable to locate a valid theme, new default will be Modern
- issue [#5824](https://github.com/Cacti/cacti/issues/5824): Properly cache the data source information for dsstats processing
- issue [#5840](https://github.com/Cacti/cacti/issues/5840): When reindexing, verify all fields may not work as intended
- feature [#5784](https://github.com/Cacti/cacti/issues/5784): Add ability to log database connections/disconnections
- feature [#5796](https://github.com/Cacti/cacti/issues/5796): Add Ping Method where connection refused assumes host is up
- feature [#5819](https://github.com/Cacti/cacti/issues/5819): When displaying graphs, default end time does not show full 24 hour period
- feature [#5825](https://github.com/Cacti/cacti/issues/5825): Add --id to remove\_device.php
- feature [#5828](https://github.com/Cacti/cacti/issues/5828): Add Location and Site to Graph List View
- feature [#5830](https://github.com/Cacti/cacti/issues/5830): Add more verbose logging to Boost
- feature: Update jQuery to 3.7.1
- feature: Update jQueryUI to 1.14.0
- feature: Update Purify.js to 3.1.6
- feature: Update billboard.js to 3.13.0
- feature: Improve the performance of the repopulation of the poller cache

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.27

# Release of Cacti 1.2.27

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

**IMPORTANT:** *There have been a number of security issues that have been addressed in this release.  It is advised to upgrade all existing platforms to this release as soon as possibly to avoid possible issues.*

Along with the release of Cacti 1.2.27, several plugins have been updated/added so please check out

Thold (v1.8), MacTrack (v4.7) and the new ServCheck (v0.1) on their github repositories.

We would personally like to thank [@xmacan](https://github.com/xmacan) for all his efforts, especially with the new ServCheck, as well

as all the users of Cacti who are contributing to the community on GitHub and in the forums. You know who

you are.

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-37x7-mfjv-mm7m](https://github.com/Cacti/cacti/security/advisories/GHSA-37x7-mfjv-mm7m): Authentication Bypass when using using older password hashes
- security #[GHSA-7cmj-g5qc-pj88](https://github.com/Cacti/cacti/security/advisories/GHSA-7cmj-g5qc-pj88): RCE vulnerability when importing packages
- security #[GHSA-cx8g-hvq8-p2rv](https://github.com/Cacti/cacti/security/advisories/GHSA-cx8g-hvq8-p2rv): RCE vulnerability when plugins include files
- security #[GHSA-gj3f-p326-gh8r](https://github.com/Cacti/cacti/security/advisories/GHSA-gj3f-p326-gh8r): SQL Injection vulnerability when using tree rules through Automation API
- security #[GHSA-grj5-8fcj-34gh](https://github.com/Cacti/cacti/security/advisories/GHSA-grj5-8fcj-34gh): XSS vulnerability when using JavaScript based messaging API
- security #[GHSA-jrxg-8wh8-943x](https://github.com/Cacti/cacti/security/advisories/GHSA-jrxg-8wh8-943x): SQL Injection vulnerability when using form templates
- security #[GHSA-p4ch-7hjw-6m87](https://github.com/Cacti/cacti/security/advisories/GHSA-p4ch-7hjw-6m87): XSS vulnerability when reading tree rules with Automation API
- security #[GHSA-rqc8-78cm-85j3](https://github.com/Cacti/cacti/security/advisories/GHSA-rqc8-78cm-85j3): XSS vulnerability when managing data queries
- security #[GHSA-vjph-r677-6pcc](https://github.com/Cacti/cacti/security/advisories/GHSA-vjph-r677-6pcc): SQL Injection vulnerability when retrieving graphs using Automation API
- issue [#5622](https://github.com/Cacti/cacti/issues/5622): Improve PHP 8.3 support
- issue [#5628](https://github.com/Cacti/cacti/issues/5628): When importing packages via command line, data source profile could not be selected
- issue [#5629](https://github.com/Cacti/cacti/issues/5629): When changing password, returning to previous page does not always work
- issue [#5636](https://github.com/Cacti/cacti/issues/5636): When using LDAP authentication the first time, warnings may appear in logs
- issue [#5638](https://github.com/Cacti/cacti/pull/5638): When editing/viewing devices, add IPv6 info to hostname tooltip
- issue [#5645](https://github.com/Cacti/cacti/pull/5645): Improve speed of polling when Boost is enabled
- issue [#5648](https://github.com/Cacti/cacti/issues/5648): Improve support for Half-Hour time zones
- issue [#5649](https://github.com/Cacti/cacti/issues/5649): Improve support of ping on Windows
- issue [#5655](https://github.com/Cacti/cacti/issues/5655): When user session not found, device lists can be incorrectly returned
- issue [#5660](https://github.com/Cacti/cacti/issues/5660): On import, legacy templates may generate warnings
- issue [#5661](https://github.com/Cacti/cacti/issues/5661): Improve support for alternate locations of Ping
- issue [#5662](https://github.com/Cacti/cacti/issues/5662): Improve PHP 8.1 support for Installer
- issue [#5669](https://github.com/Cacti/cacti/pull/5669): Fix issues with number formatting
- issue [#5677](https://github.com/Cacti/cacti/pull/5677): Improve PHP 8.1 support when SpikeKill is run first time
- issue [#5693](https://github.com/Cacti/cacti/pull/5693): Improve PHP 8.1 support for SpikeKill
- issue [#5696](https://github.com/Cacti/cacti/issues/5696): When using Chinese to search for graphics, garbled characters appear.
- issue [#5701](https://github.com/Cacti/cacti/issues/5701): When importing templates, preview mode will not always load
- issue [#5720](https://github.com/Cacti/cacti/issues/5720): When remote poller is installed, MySQL TimeZone DB checks are not performed
- issue [#5723](https://github.com/Cacti/cacti/issues/5723): When Remote Poller installation completes, no finish button is shown
- issue [#5725](https://github.com/Cacti/cacti/issues/5725): Unauthorized agents should be recorded into logs
- issue [#5726](https://github.com/Cacti/cacti/issues/5726): Poller cache may not always update if hostname changes
- issue [#5727](https://github.com/Cacti/cacti/issues/5727): When using CMD poller, Failure and Recovery dates may have incorrect values
- issue [#5731](https://github.com/Cacti/cacti/issues/5731): Saving a Tree can cause the tree to become unpublished
- issue [#5732](https://github.com/Cacti/cacti/issues/5732): Web Basic Authentication does not record user logins
- issue [#5733](https://github.com/Cacti/cacti/issues/5733): When using Accent-based languages, translations may not work properly
- issue [#5743](https://github.com/Cacti/cacti/issues/5743): Fix automation expressions for device rules
- issue [#5748](https://github.com/Cacti/cacti/issues/5748): Improve PHP 8.1 Support during fresh install with boost
- feature [#5692](https://github.com/Cacti/cacti/issues/5692): Add a device "enabled/disabled" indicator next to the graphs
- feature [#5710](https://github.com/Cacti/cacti/issues/5710): Notify the admin periodically when a remote data collector goes into heartbeat status
- feature [#5716](https://github.com/Cacti/cacti/pull/5716): Add template for Aruba Clearpass
- feature [#5730](https://github.com/Cacti/cacti/issues/5730): Add fliter/sort of Device Templates by Graph Templates

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.26

# Release of Cacti 1.2.26

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

Please note, with this release there have been a couple of security issues addressed. For more information see the CHANGELOG and GitHub

Finally, Christmas is approaching and hopefully you are all enjoying your rare free time with family and/or friends. The Cacti Team wishes you all the best in this holiday period and have a happy new year!

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-xwqc-7jc4-xm73](https://github.com/Cacti/cacti/security/advisories/GHSA-xwqc-7jc4-xm73): XSS vulnerability when importing a template file
- security #[GHSA-pfh9-gwm6-86vp](https://github.com/Cacti/cacti/security/advisories/GHSA-pfh9-gwm6-86vp): RCE vulnerability when managing links
- security #[GHSA-vr3c-38wh-g855](https://github.com/Cacti/cacti/security/advisories/GHSA-vr3c-38wh-g855): SQL Injection vulnerability when managing poller devices
- security #[GHSA-wc73-r2vw-59pr](https://github.com/Cacti/cacti/security/advisories/GHSA-wc73-r2vw-59pr): XSS vulnerability when adding new devices
- security #[GHSA-q7g7-gcf6-wh4x](https://github.com/Cacti/cacti/security/advisories/GHSA-q7g7-gcf6-wh4x): XSS vulnerability when viewing data sources in debug mode
- security #[GHSA-w85f-7c4w-7594](https://github.com/Cacti/cacti/security/advisories/GHSA-w85f-7c4w-7594): SQL Injection vulnerability when managing SNMP Notification Receivers
- issue [#5464](https://github.com/Cacti/cacti/issues/5464): When viewing data sources, an undefined variable error may be seen
- issue [#5478](https://github.com/Cacti/cacti/pull/5478): Improvements for Poller Last Run Date
- issue [#5481](https://github.com/Cacti/cacti/issues/5481): Attempting to edit a Data Query that does not exist throws warnings and not an GUI error
- issue [#5483](https://github.com/Cacti/cacti/issues/5483): Improve PHP 8.1 support when adding devices
- issue [#5485](https://github.com/Cacti/cacti/issues/5485): Viewing Data Query Cache can cause errors to be logged
- issue [#5489](https://github.com/Cacti/cacti/issues/5489): Preserve option is not properly honoured when removing devices at command line
- issue [#5490](https://github.com/Cacti/cacti/issues/5490): Infinite recursion is possible during a database failure
- issue [#5492](https://github.com/Cacti/cacti/issues/5492): Monitoring Host CPU's does not always work on Windows endpoints
- issue [#5493](https://github.com/Cacti/cacti/issues/5493): Multi select drop down list box not rendered correctly in Chrome and Edge
- issue [#5494](https://github.com/Cacti/cacti/issues/5494): Selective Plugin Debugging may not always work as intended
- issue [#5495](https://github.com/Cacti/cacti/issues/5495): During upgrades, Plugins may be falsely reported as incompatible
- issue [#5496](https://github.com/Cacti/cacti/issues/5496): Plugin management at command line does not work with multiple plugins
- issue [#5502](https://github.com/Cacti/cacti/issues/5502): Improve PHP 8.1 support for incrementing only numbers
- issue [#5503](https://github.com/Cacti/cacti/issues/5503): Allow the renaming of guest and template accounts
- issue [#5514](https://github.com/Cacti/cacti/issues/5514): DS Stats issues warnings when the RRDfile has not been initialized
- issue [#5527](https://github.com/Cacti/cacti/issues/5527): When upgrading, missing data source profile can cause errors to be logged
- issue [#5534](https://github.com/Cacti/cacti/issues/5534): When deleting a single Data Source, purge historical debug data
- issue [#5542](https://github.com/Cacti/cacti/issues/5542): Improvements to form element warnings
- issue [#5554](https://github.com/Cacti/cacti/issues/5554): Some interface aliases do not appear correctly
- issue [#5555](https://github.com/Cacti/cacti/issues/5555): Aggregate graph does not show other percentiles
- issue [#5561](https://github.com/Cacti/cacti/issues/5561): Settings table updates for large values reverted by database repair
- issue [#5564](https://github.com/Cacti/cacti/pull/5564): When obtaining graph records, error messages may be recorded
- issue [#5565](https://github.com/Cacti/cacti/issues/5565): Unable to change a device's community at command line
- issue [#5572](https://github.com/Cacti/cacti/pull/5572): Increase timeout for RRDChecker
- issue [#5573](https://github.com/Cacti/cacti/issues/5573): When viewing a graph, option to edit template may lead to incorrect URL
- issue [#5581](https://github.com/Cacti/cacti/issues/5581): When upgrading, failures may occur due to missing color table keys
- issue [#5583](https://github.com/Cacti/cacti/issues/5583): On installation, allow a more appropriate template to be used as the default
- issue [#5585](https://github.com/Cacti/cacti/issues/5585): When data input parameters are allowed to be null, allow null
- issue [#5586](https://github.com/Cacti/cacti/pull/5586): CSV Exports may not always output data correctly
- issue [#5589](https://github.com/Cacti/cacti/issues/5589): When debugging a graph, long CDEF's can cause undesirable scrolling
- issue [#5590](https://github.com/Cacti/cacti/issues/5590): Secondary LDAP server not evaluated when the first one has failed
- issue [#5602](https://github.com/Cacti/cacti/issues/5602): When adding a device, using the bulk walk option can make version information appear
- issue [#5609](https://github.com/Cacti/cacti/issues/5609): When parsing a Data Query resource, an error can be reported if no direction is specified
- issue [#5612](https://github.com/Cacti/cacti/issues/5612): Database reconnection can cause errors to be reported incorrectly
- issue [#5613](https://github.com/Cacti/cacti/pull/5613): fix returned value if $sau is empty
- feature [#5577](https://github.com/Cacti/cacti/pull/5577): Add Aruba switch, Aruba controller and HPE iLO templates
- feature [#5597](https://github.com/Cacti/cacti/pull/5597): Add OSCX 6x00 templates

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.25

# Release of Cacti 1.2.25

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

Following on from our previous release, Cacti has been receiving extra eyes across the code base. This has meant a delay in the release of 1.2.25 as we work with various parties to improve Cacti and provide better protection from potential malicious actors.

Windows users can find a beta version of the latest Windows installer via our forum thread [http://forums.cacti.net/viewtopic.php?p=292797#p292797](http://forums.cacti.net/viewtopic.php?p=292797#p292797) which will be updated as the beta is updated.  There has been a major re-working of the installer including having Apache installed using the Windows Service Virtual Account to help improve security, and updated versions of PHP, RRDtool, Net-SNMP.  It also introduces a change from MySQL to MariaDB as the default database engine that is installed.

As we focus more work on trying to get 1.3 ready for testing, we have also added extra device packages that can be installed during the normal web installer, or added manually afterwards (see the install/packages folder).

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security #[GHSA-77rf-774j-6h3p](https://github.com/Cacti/cacti/security/advisories/GHSA-77rf-774j-6h3p): Protect against Insecure deserialization of filter data
- security #[GHSA-gx8c-xvjh-9qh4](https://github.com/Cacti/cacti/security/advisories/GHSA-gx8c-xvjh-9qh4): Protect against Cross-Site Scripting vulnerability when creating new graphs
- security #[GHSA-6r43-q2fw-5wrg](https://github.com/Cacti/cacti/security/advisories/GHSA-6r43-q2fw-5wrg): Protect against Unauthenticated SQL Injection when viewing graphs
- security #[GHSA-6jhp-mgqg-fhqg](https://github.com/Cacti/cacti/security/advisories/GHSA-6jhp-mgqg-fhqg): Protect against SQL Injection when saving data with sql\_save()
- security #[GHSA-g6ff-58cj-x3cp](https://github.com/Cacti/cacti/security/advisories/GHSA-g6ff-58cj-x3cp): Protect against Authenticated command injection when using SNMP options
- security #[GHSA-q4wh-3f9w-836h](https://github.com/Cacti/cacti/security/advisories/GHSA-q4wh-3f9w-836h): Protect against Authenticated SQL injection vulnerability when managing graphs
- security #[GHSA-gj95-7xr8-9p7g](https://github.com/Cacti/cacti/security/advisories/GHSA-gj95-7xr8-9p7g): Protect against Authenticated SQL injection vulnerability when managing reports
- security #[GHSA-v5w7-hww7-2f22](https://github.com/Cacti/cacti/security/advisories/GHSA-v5w7-hww7-2f22): Protect against SQL Injection when using regular expressions
- security #[GHSA-4pjv-rmrp-r59x](https://github.com/Cacti/cacti/security/advisories/GHSA-4pjv-rmrp-r59x): Protect against Open redirect in change password functionality
- security #[GHSA-rwhh-xxm6-vcrv](https://github.com/Cacti/cacti/security/advisories/GHSA-rwhh-xxm6-vcrv): Protect against Cross-Site Scripting vulnerability with Device Name when managing Data Sources
- security #[GHSA-24w4-4hp2-3j8h](https://github.com/Cacti/cacti/security/advisories/GHSA-24w4-4hp2-3j8h): Protect against Cross-Site Scripting vulnerability with Device Name when administrating Reports
- security #[GHSA-5hpr-4hhc-8q42](https://github.com/Cacti/cacti/security/advisories/GHSA-5hpr-4hhc-8q42): Protect against Cross-Site Scripting vulnerability with Device Name when editing Graphs whilst managing Reports
- security #[GHSA-vqcc-5v63-g9q7](https://github.com/Cacti/cacti/security/advisories/GHSA-vqcc-5v63-g9q7): Protect against Cross-Site Scripting vulnerability with Device Name when managing Data Sources
- security #[GHSA-9fj7-8f2j-2rw2](https://github.com/Cacti/cacti/security/advisories/GHSA-9fj7-8f2j-2rw2): Protect against Cross-Site Scripting vulnerability with Device Name when debugging data queries
- security #[GHSA-6hrc-2cfc-8hm7](https://github.com/Cacti/cacti/security/advisories/GHSA-6hrc-2cfc-8hm7): Protect against Cross-Site Scripting vulnerability with Data Source Name when managing Graphs
- security #[GHSA-hrg9-qqqx-wc4h](https://github.com/Cacti/cacti/security/advisories/GHSA-hrg9-qqqx-wc4h): Protect against Cross-Site Scripting vulnerability with Data Source Name when debugging Data Queries
- security #[GHSA-r8qq-88g3-hmgv](https://github.com/Cacti/cacti/security/advisories/GHSA-r8qq-88g3-hmgv): Protect against Cross-Site Scripting vulnerability with Data Source Information when managing Data Sources
- security #[GHSA-rf5w-pq3f-9876](https://github.com/Cacti/cacti/security/advisories/GHSA-rf5w-pq3f-9876): Protect against Privilege escalation when Cacti installed using Windows Installer defaults
- issue [#2959](https://github.com/Cacti/cacti/issues/2959): When rebuilding the Poller Cache from command line, allow it to be multi-threaded
- issue [#4045](https://github.com/Cacti/cacti/issues/4045): When searching tree or list views, the URL does not update after changes
- issue [#5254](https://github.com/Cacti/cacti/issues/5254): When creating a Data Source Template with a specific snmp port, the port is not always applied
- issue [#5255](https://github.com/Cacti/cacti/issues/5255): When a Data Query references a file, the filename should be trimmed to remove spurious spaces
- issue [#5258](https://github.com/Cacti/cacti/issues/5258): THold plugin may not always install or upgrade properly
- issue [#5259](https://github.com/Cacti/cacti/issues/5259): RRD file structures are not always updated properly, if there are more Data Sources in the Data Template than the Graph Template
- issue [#5263](https://github.com/Cacti/cacti/issues/5263): When reindexing devices, errors may sometimes be shown
- issue [#5272](https://github.com/Cacti/cacti/issues/5272): Boost may loose data when the database server is overloaded
- issue [#5275](https://github.com/Cacti/cacti/issues/5275): Boost can sometimes output unexpected or invalid values
- issue [#5277](https://github.com/Cacti/cacti/issues/5277): Boost should not attempt to start if there are no items to process
- issue [#5279](https://github.com/Cacti/cacti/issues/5279): Rebuilding the poller cache does not always work as expected
- issue [#5282](https://github.com/Cacti/cacti/issues/5282): Host CPU items may not work poll as expected when on a remote data collector where hmib is also enabled
- issue [#5283](https://github.com/Cacti/cacti/issues/5283): When creating new graphs, invalid offset errors may be generated
- issue [#5291](https://github.com/Cacti/cacti/issues/5291): When importing packages, SQL errors may be generated
- issue [#5298](https://github.com/Cacti/cacti/issues/5298): When managing plugins from command line, the --plugin option is not properly handled
- issue [#5299](https://github.com/Cacti/cacti/issues/5299): When automating an install of Cacti, error messages can be appear
- issue [#5300](https://github.com/Cacti/cacti/issues/5300): When performing automated install of a plugin, warnings can be thrown
- issue [#5315](https://github.com/Cacti/cacti/issues/5315): Automation references the wrong table name causing errors
- issue [#5317](https://github.com/Cacti/cacti/issues/5317): Data Source Info Mode produces invalid recommendations
- issue [#5319](https://github.com/Cacti/cacti/issues/5319): Data Source Debug 'Run All' generates too many log messages
- issue [#5323](https://github.com/Cacti/cacti/issues/5323): The description of rebuild poller cache in utilities does not display properly
- issue [#5324](https://github.com/Cacti/cacti/issues/5324): When reindexing a device, debug information may not always display properly
- issue [#5329](https://github.com/Cacti/cacti/issues/5329): Upon displaying a form with errors, the session error fields variable isn't cleared
- issue [#5333](https://github.com/Cacti/cacti/issues/5333): MariaDB clusters will no longer support exclusive locks
- issue [#5336](https://github.com/Cacti/cacti/issues/5336): RRDtool can fail to update when sources in Data Template and Graph Template data sources do not match
- issue [#5338](https://github.com/Cacti/cacti/issues/5338): Compatibility improvements for Boost under PHP 8.x
- issue [#5342](https://github.com/Cacti/cacti/issues/5342): When searching the tree, increase the time before querying for items
- issue [#5347](https://github.com/Cacti/cacti/issues/5347): Device Location drop down does not always populate correctly
- issue [#5354](https://github.com/Cacti/cacti/issues/5354): When viewing Realtime graphs, undefined variable errors may be reported
- issue [#5355](https://github.com/Cacti/cacti/issues/5355): SNMP Uptime is not always ignored for spikekills
- issue [#5356](https://github.com/Cacti/cacti/issues/5356): Improve detection of downed Devices
- issue [#5360](https://github.com/Cacti/cacti/issues/5360): When reporting missing functions from Plugins, ensure messages do not occur too often
- issue [#5364](https://github.com/Cacti/cacti/issues/5364): When starting the Cacti daemon, database errors may be reported when there is no problem
- issue [#5366](https://github.com/Cacti/cacti/issues/5366): When reporting from RRDcheck, ensure prefix is in the correct casing
- issue [#5371](https://github.com/Cacti/cacti/issues/5371): Improve Orphaned Data Source options and display
- issue [#5372](https://github.com/Cacti/cacti/issues/5372): Parsing the PHP Configuration may sometimes produce errors
- issue [#5376](https://github.com/Cacti/cacti/issues/5376): Security processes attempt to check for a user lockout even if there is no user logged in
- issue [#5377](https://github.com/Cacti/cacti/issues/5377): When attempting to edit a tree, the search filter for Graphs remains disabled
- issue [#5381](https://github.com/Cacti/cacti/issues/5381): When reindexing, a Data Source that could be un-orphaned may not always be unorphaned
- issue [#5382](https://github.com/Cacti/cacti/pull/5382): When parsing a date value, there could be more than 30 chars
- issue [#5384](https://github.com/Cacti/cacti/issues/5384): Untemplated Data Sources can fail to update due to lack of an assigned Graph
- issue [#5386](https://github.com/Cacti/cacti/pull/5386): When processing items to check, do not include disabled hosts
- issue [#5390](https://github.com/Cacti/cacti/pull/5390): When saving a Data Source Template, SQL errors may be reported
- issue [#5392](https://github.com/Cacti/cacti/issues/5392): When importing a Template, errors may be recorded
- issue [#5402](https://github.com/Cacti/cacti/issues/5402): Some display strings have invalid formatting that cannot be parsed
- issue [#5403](https://github.com/Cacti/cacti/issues/5403): When filtering with regular expressions, the 'does not match' option does not always function as expected
- issue [#5409](https://github.com/Cacti/cacti/issues/5409): When enabling a plugin, sometimes it can appear as if nothing happens
- issue [#5413](https://github.com/Cacti/cacti/issues/5413): Ensure the Rows Per Page option shows limitations set by configuration
- issue [#5414](https://github.com/Cacti/cacti/issues/5414): Plugins are unable to modify fields in the setting 'Change Device Settings'
- issue [#5417](https://github.com/Cacti/cacti/issues/5417): When reporting emails being sent, ensure BCC addresses are also included
- issue [#5420](https://github.com/Cacti/cacti/issues/5420): Improve compatibility of SNMP class trim handling under PHP 8.x
- issue [#5426](https://github.com/Cacti/cacti/issues/5426): When importing legacy Data Query Templates, the Template can become unusable
- issue [#5427](https://github.com/Cacti/cacti/issues/5427): Provide ability to raise an event when extending the settings form
- issue [#5434](https://github.com/Cacti/cacti/issues/5434): Prevent unsupported SQL Mode flags from being set
- issue [#5439](https://github.com/Cacti/cacti/issues/5439): The DSStats summary does not always display expected values
- issue [#5440](https://github.com/Cacti/cacti/pull/5440): When performing a fresh install, device classification may be missing.
- issue [#5446](https://github.com/Cacti/cacti/issues/5446): Duplication functions for Graph/Template and Data Source/Template do not return and id
- issue [#5447](https://github.com/Cacti/cacti/issues/5447): Duplication of Device Templates should be an API call
- issue [#5450](https://github.com/Cacti/cacti/issues/5450): Unable to convert database to latin1 instead of utf8 if desired
- issue [#5451](https://github.com/Cacti/cacti/issues/5451): When creating Graphs, the process may become slower over time as more items exist
- issue [#5452](https://github.com/Cacti/cacti/issues/5452): When a bulk walk size is set to automatic, this is not always set to the optimal value
- issue [#5453](https://github.com/Cacti/cacti/pull/5453): Update copyright notice on import packages
- issue [#5454](https://github.com/Cacti/cacti/issues/5454): When viewing Orphan Graphs, SQL errors may be reported
- issue [#5457](https://github.com/Cacti/cacti/pull/5457): When reindexing hosts from command line, ensure only one process runs at once
- issue [#5458](https://github.com/Cacti/cacti/issues/5458): When a Data Query has no Graphs, it may not be deletable
- issue [#5459](https://github.com/Cacti/cacti/issues/5459): When duplicating a Graph Template, provide an option to not duplicate Data Query association
- issue [#5460](https://github.com/Cacti/cacti/issues/5460): When duplicating a Data Template errors can appear in the Cacti log
- issue [#5462](https://github.com/Cacti/cacti/issues/5462): When importing a Package, previewing makes unexpected changes to Cacti Templates
- issue [#5466](https://github.com/Cacti/cacti/issues/5466): When enabling boost on a fresh install, an error may be reported
- issue [#5467](https://github.com/Cacti/cacti/issues/5467): Improve compatibility for backtrace logging under PHP 8.x
- issue [#5475](https://github.com/Cacti/cacti/issues/5475): Improve compatibility for Advanced Ping under PHP 8.x
- feature [#5375](https://github.com/Cacti/cacti/pull/5375): Provide new templates for Fortigate and Aruba Cluster to be available during install
- feature [#5393](https://github.com/Cacti/cacti/pull/5393): Provide new template for SNMP Printer to be available during install
- feature [#5418](https://github.com/Cacti/cacti/pull/5418): When importing devices, allow a device classification to be known
- feature [#5442](https://github.com/Cacti/cacti/pull/5442): Extend length o...

[Read more](https://github.com/Cacti/cacti/releases/tag/release%2F1.2.25)

## v1.2.24

# Release of Cacti 1.2.24

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

Please note, that in the previous release, we added extra security around the

use of http headers for remote agent calls.  This release now enforces that

change to require admins to set which headers are allowed from a predefined

set and no longer assumes that all of them should be checked.

See **$proxy\_headers** in the **config.php.dist** include file for more

information.  These must b set in the **include/config.php** if they are

required.

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- issue [#5127](https://github.com/Cacti/cacti/issues/5127): Unable to import Local Linux Machine template
- issue [#5134](https://github.com/Cacti/cacti/issues/5134): Maximum Memory shows -1 instead of Unlimited
- issue [#5135](https://github.com/Cacti/cacti/issues/5135): RRDcleaner and RRDcheck share the same filter details causing errors
- issue [#5136](https://github.com/Cacti/cacti/pull/5136): When passed a null value, number\_format\_i18n() can return a invalid number by ddb4github
- issue [#5137](https://github.com/Cacti/cacti/issues/5137): When attempting to update structured paths, SQL errors can occur
- issue [#5140](https://github.com/Cacti/cacti/issues/5140): Compatibility changes for SNMP under PHP 8.2
- issue [#5142](https://github.com/Cacti/cacti/issues/5142): Fix issues with permission model and warnings
- issue [#5143](https://github.com/Cacti/cacti/issues/5143): When a Device has zero Graphs or Data Sources, it does not display a value
- issue [#5145](https://github.com/Cacti/cacti/issues/5145): Changing SNMP settings to None leaves Bulk Walk Maximum Repititions visible
- issue [#5147](https://github.com/Cacti/cacti/issues/5147): Language handlers may not always be loaded properly
- issue [#5150](https://github.com/Cacti/cacti/issues/5150): Wrong parameters are shown for the Import Package script
- issue [#5151](https://github.com/Cacti/cacti/issues/5151): Templates appear to lose their suggested name values
- issue [#5159](https://github.com/Cacti/cacti/issues/5159): When editing a tree, the tree can not be set to published
- issue [#5160](https://github.com/Cacti/cacti/issues/5160): Translations on debian 'bookworm' systems may cause server errors
- issue [#5161](https://github.com/Cacti/cacti/issues/5161): Switching language in the settings does not immediately become active
- issue [#5166](https://github.com/Cacti/cacti/pull/5166): Plugin permissions may sometimes appear in the wrong section by ddb4github
- issue [#5167](https://github.com/Cacti/cacti/issues/5167): Graph template for NetSNMP lmsensors missing
- issue [#5168](https://github.com/Cacti/cacti/issues/5168): Import Package is misleading when reviewing Device Template Changes
- issue [#5169](https://github.com/Cacti/cacti/issues/5169): Device failure and recovery dates can be misleading
- issue [#5170](https://github.com/Cacti/cacti/issues/5170): Prevent remote polling functionality from running on main poller
- issue [#5174](https://github.com/Cacti/cacti/issues/5174): When adding a new device, location is not being saved
- issue [#5180](https://github.com/Cacti/cacti/issues/5180): Audit Database has issues with storage engine compare
- issue [#5181](https://github.com/Cacti/cacti/issues/5181): When working with remote data collectors, some errors may be logged
- issue [#5182](https://github.com/Cacti/cacti/issues/5182): Graph Image does not have check for Remote Agent
- issue [#5184](https://github.com/Cacti/cacti/issues/5184): When a user has been deleted, checking permissions can cause errors
- issue [#5185](https://github.com/Cacti/cacti/issues/5185): Repair Database does not prune old Poller Item Records
- issue [#5187](https://github.com/Cacti/cacti/issues/5187): When calling plugin functions, errors can appear if they are not present
- issue [#5188](https://github.com/Cacti/cacti/issues/5188): When filtering Device Templates, valid matches are not always shown
- issue [#5190](https://github.com/Cacti/cacti/issues/5190): When using Gradient Support GPRINT Text Format is misaligned
- issue [#5194](https://github.com/Cacti/cacti/issues/5194): CSRF directory needs to be writeable for creating the csrf-secret.php file
- issue [#5195](https://github.com/Cacti/cacti/issues/5195): When removing spikes, errors can be recorded for NaN samples
- issue [#5196](https://github.com/Cacti/cacti/issues/5196): Gradient support can break Graphs containing special characters
- issue [#5197](https://github.com/Cacti/cacti/issues/5197): Unable to obtain realtime graph from remote poller
- issue [#5198](https://github.com/Cacti/cacti/issues/5198): Compability Improvements for PHP Diff under PHP 8.x
- issue [#5199](https://github.com/Cacti/cacti/issues/5199): When trying to obtain data, cacti should not long Transport Read errors
- issue [#5200](https://github.com/Cacti/cacti/issues/5200): Compatibility improvements for Classic Tab images under PHP 8.x
- issue [#5201](https://github.com/Cacti/cacti/issues/5201): Weathermaps can have issues rendering with some themes
- issue [#5202](https://github.com/Cacti/cacti/issues/5202): When importing packages, Graph Size does not get updated to Graph Templates
- issue [#5203](https://github.com/Cacti/cacti/issues/5203): Host Mib Device package can cause errors with NetSNMP scripts
- issue [#5204](https://github.com/Cacti/cacti/issues/5204): Compatibility improvements for Audit Database under PHP 8.x
- issue [#5205](https://github.com/Cacti/cacti/issues/5205): When using Diff Viewer, rendering is not always correct under certain themes
- issue [#5207](https://github.com/Cacti/cacti/issues/5207): Compatibility improvements for Installer under PHP 8.x
- issue [#5208](https://github.com/Cacti/cacti/issues/5208): Some i18n strings are not properly translated
- issue [#5209](https://github.com/Cacti/cacti/pull/5209): When disabling a user, no log is recorded by xmacan
- issue [#5211](https://github.com/Cacti/cacti/issues/5211): When creating a new graph, undefined variable errors may be recorded
- issue [#5214](https://github.com/Cacti/cacti/issues/5214): Basic Auth is timing out and logging users off automatically
- issue [#5223](https://github.com/Cacti/cacti/issues/5223): When using callback form functions, name and id field may not be correctly set
- issue [#5224](https://github.com/Cacti/cacti/issues/5224): When poller runtime is exceeded, time should be display as a rounded number
- issue [#5227](https://github.com/Cacti/cacti/issues/5227): When debugging a data source, errors may be shown if no RRDfile created yet
- issue [#5232](https://github.com/Cacti/cacti/issues/5232): Polling can appear delayed due to early statistics gathering
- issue [#5236](https://github.com/Cacti/cacti/issues/5236): When viewing a graph, Edit Graph Template link may open wrong url
- issue [#5238](https://github.com/Cacti/cacti/issues/5238): Searching for Poller Items can generates SQL Errors
- issue [#5239](https://github.com/Cacti/cacti/issues/5239): Bulk Walk Maximum Repetitions may sometimes be ignored
- issue [#5241](https://github.com/Cacti/cacti/issues/5241): Balance Process Load does not always apply properly
- issue [#5243](https://github.com/Cacti/cacti/issues/5243): Template Export missing Graph Template columns `multiple` and `test_source`
- issue [#5245](https://github.com/Cacti/cacti/pull/5245): Add additional security to the unserialize function by TheWitness
- issue [#5247](https://github.com/Cacti/cacti/issues/5247): Rebuilding Poller Cache from Utilities does not respect poller interval due to lack or ordering

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## v1.2.23

# Release of Cacti 1.2.23

Thank you to everyone who is using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

**IMPORTANT:** A security issue was identified that could allow remote attackers to bypass IP restrictions to the remote agent service when proxy headers are defined.

Starting with 1.2.23, it is the admins responsibility to define which proxy headers are valid. However, to ensure that access to systems are not lost, until these are explicitly configured, the full list of proxy headers will be allowed and a warning will be displayed in the system logs daily.

**If you see this warning, please set the desired headers or false within `include/config.php` immediately**

In the 1.3.0 (development) version, no headers are configured and must be manually set.  If you are using a proxy server, ensure these are configured within `include/config.php`

For more information, refer to issue security#5119

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork, and pull requests!

# Cacti Change Log

- security [#4920](https://github.com/Cacti/cacti/issues/4920): Add .htaccess file to scripts folder
- security [#5119](https://github.com/Cacti/cacti/issues/5119): CVE-2022-46169 Unauthenticated Command Injection in Remote Agent
- issue [#4418](https://github.com/Cacti/cacti/issues/4418): When using Single Sign-on Frameworks, revocation is not always detected in callbacks
- issue [#4682](https://github.com/Cacti/cacti/issues/4682): New templates are not installed during the update
- issue [#4738](https://github.com/Cacti/cacti/pull/4738): Improve PHP 8.1 support for Installer CLI
- issue [#4888](https://github.com/Cacti/cacti/issues/4888): The database audit script fails to run properly on MySQL 8.0.29
- issue [#4889](https://github.com/Cacti/cacti/issues/4889): Increase host query performance by removing check for NULL
- issue [#4892](https://github.com/Cacti/cacti/issues/4892): When many hosts go offline, Recache Event can be constantly logged
- issue [#4893](https://github.com/Cacti/cacti/issues/4893): Real Time Counter can become stuck and does not count down
- issue [#4896](https://github.com/Cacti/cacti/issues/4896): When remote poller is in offline mode, GUI can become inaccesible and poller can timeout
- issue [#4897](https://github.com/Cacti/cacti/issues/4897): Technical support page on remote poller shows max connections of Main poller
- issue [#4903](https://github.com/Cacti/cacti/issues/4903): Correct incompatibility between MySQL 8.x and Automation regular expressions
- issue [#4904](https://github.com/Cacti/cacti/issues/4904): The recommendation for innodb\_buffer\_pool\_instances is incorrect for MySQL 8 and MariaDB \< 10.5
- issue [#4905](https://github.com/Cacti/cacti/issues/4905): Using colons in labels can break graphs with gradients
- issue [#4917](https://github.com/Cacti/cacti/issues/4917): Real Time Counter can become stuck and does not count down
- issue [#4921](https://github.com/Cacti/cacti/issues/4921): Some Aggregate graphs can be denied access incorrectly
- issue [#4923](https://github.com/Cacti/cacti/issues/4923): Unable to duplicate a Graph template
- issue [#4927](https://github.com/Cacti/cacti/issues/4927): Unable to audit the database if database password contains a bracket
- issue [#4934](https://github.com/Cacti/cacti/issues/4934): Upgrade phpseclib to 2.0.37
- issue [#4935](https://github.com/Cacti/cacti/issues/4935): The 'Net-SNMP - Device I/O' template incorrectly sets a maximum value of zero
- issue [#4940](https://github.com/Cacti/cacti/issues/4940): When sorting by hostname, database errors can be reported
- issue [#4941](https://github.com/Cacti/cacti/issues/4941): When boost is running, graphs can appear broken
- issue [#4944](https://github.com/Cacti/cacti/issues/4944): Packages should be signed with SHA256 as SHA1 is considered deprecated
- issue [#4947](https://github.com/Cacti/cacti/issues/4947): When creating a Data Template, ensure that the default max value is always 'U' and not '0'
- issue [#4951](https://github.com/Cacti/cacti/issues/4951): Plugins may not work correctly with Multi-Poller setups
- issue [#4960](https://github.com/Cacti/cacti/issues/4960): Setting context for connections throws error in PHP 8.x
- issue [#4963](https://github.com/Cacti/cacti/issues/4963): Wen calculating 95th percentile, floor() maybe used instead of ceil() incorrectly
- issue [#4964](https://github.com/Cacti/cacti/issues/4964): Tree search does not correct hide non-matching tree objects
- issue [#4966](https://github.com/Cacti/cacti/issues/4966): Device Template filters should show on used templates
- issue [#4971](https://github.com/Cacti/cacti/issues/4971): MIB Parser can sometimes cause errors in later PHP versions
- issue [#4978](https://github.com/Cacti/cacti/issues/4978): Boost may sometimes lose the Time Zone unexpectedly
- issue [#4980](https://github.com/Cacti/cacti/issues/4980): Setting business hours can cause PHP errors
- issue [#4988](https://github.com/Cacti/cacti/issues/4988): When creating RRD File, more data sources than expected may be defined
- issue [#4990](https://github.com/Cacti/cacti/issues/4990): When viewing Links, errors can be generated
- issue [#4991](https://github.com/Cacti/cacti/issues/4991): Updating a Data Template does not switch rrd\_heartbeat properly for all sources leading to empty graphs
- issue [#4993](https://github.com/Cacti/cacti/issues/4993): Data Debug Troubleshooter does not pick up invalid RRD\_heartbeat settings
- issue [#4996](https://github.com/Cacti/cacti/issues/4996): When managing graphs, Graphs can be listed multiple times incorrectly
- issue [#5001](https://github.com/Cacti/cacti/issues/5001): Data Debug troubleshooter reports false positives with Missing Data Sources
- issue [#5006](https://github.com/Cacti/cacti/issues/5006): Errors can occur when attempting to remove items from CDEF or VDEF's
- issue [#5012](https://github.com/Cacti/cacti/pull/5012): When upgrading database at command line, some PHP errors may be seen
- issue [#5013](https://github.com/Cacti/cacti/issues/5013): Automatically set Bulk Walk size when missing on a host
- issue [#5015](https://github.com/Cacti/cacti/issues/5015): Upgrade for 1.2.21 reporting unknown status
- issue [#5017](https://github.com/Cacti/cacti/issues/5017): SNMP Agent can cause unexpected errors due to implicit rounding
- issue [#5018](https://github.com/Cacti/cacti/issues/5018): When using 'Remember me', session can still be forced to end unexpectedly
- issue [#5024](https://github.com/Cacti/cacti/pull/5024): Escape char not properly replaced in snmp strings
- issue [#5028](https://github.com/Cacti/cacti/issues/5028): Cacti User Stats script can throw errors unexpectedly
- issue [#5029](https://github.com/Cacti/cacti/issues/5029): Searching for a plugin by name does not always work
- issue [#5030](https://github.com/Cacti/cacti/issues/5030): Installer shows innodb unset in MariaDB 10.10+
- issue [#5033](https://github.com/Cacti/cacti/issues/5033): Improve PHP 8.1 support with Installer
- issue [#5034](https://github.com/Cacti/cacti/issues/5034): RRD Proxy Server not supported by CLI script "structure\_rra\_paths.php"
- issue [#5041](https://github.com/Cacti/cacti/issues/5041): Custom themes may cause errors if they do not contain all required CSS/JS files
- issue [#5057](https://github.com/Cacti/cacti/issues/5057): When adding a device rule in automation, depreciated filters may be reported
- issue [#5066](https://github.com/Cacti/cacti/issues/5066): Graph watermark is not escaped properly, leading to broken graphs
- issue [#5068](https://github.com/Cacti/cacti/issues/5068): Improve PHP 8.2 support with Installer
- issue [#5084](https://github.com/Cacti/cacti/issues/5084): When viewing trees, runtime errors may be recorded
- issue [#5088](https://github.com/Cacti/cacti/issues/5088): When running script host\_update\_template.php, reindex method may incorrectly be changed to uptime
- issue [#5089](https://github.com/Cacti/cacti/issues/5089): When numeric regex validation fails, no backtrace is logged
- issue [#5096](https://github.com/Cacti/cacti/issues/5096): When the SNMP Agent is enabled, certain objects can result in errors appearing
- issue [#5097](https://github.com/Cacti/cacti/issues/5097): RRDtool Utilities should not appear on Remote Data Collectors
- issue [#5101](https://github.com/Cacti/cacti/issues/5101): When a remote poller fails, the recovery process may also fail
- issue [#5102](https://github.com/Cacti/cacti/issues/5102): When in Recovery Mode, plugins that are designed to work remotely stop working
- issue [#5103](https://github.com/Cacti/cacti/issues/5103): When Remote Data Collector changes status, a full page refresh or logout should occur
- issue [#5105](https://github.com/Cacti/cacti/issues/5105): ss\_host\_disk.php php issue after upgrade PHP 8.1 (from 7.4)
- issue [#5107](https://github.com/Cacti/cacti/issues/5107): Block installation if PHP has session.auto\_start enabled
- issue [#5111](https://github.com/Cacti/cacti/issues/5111): During boost processing, some DS Stats functions can cause errors
- feature [#1100](https://github.com/Cacti/cacti/issues/1100): Structured path not created when using remote poller and Update On-Demand
- feature [#1392](https://github.com/Cacti/cacti/issues/1392): Notify Admins that page errors exist even when using dynamic callbacks
- feature [#2239](https://github.com/Cacti/cacti/issues/2239): Allow Import and Export to be more selective
- feature [#2485](https://github.com/Cacti/cacti/issues/2485): Importing Template requires you to upload the same file after previewing
- feature [#2548](https://github.com/Cacti/cacti/issues/2548): Add Head/Tail filtering of log for more efficient searches
- feature [#2567](https://github.com/Cacti/cacti/issues/2567): The innodb sort buffer should be optimized for large tables
- feature [#2747](https://github.com/Cacti/cacti/issues/2747): Allow more sorting options when managing Graphs
- feature [#2871](https://github.com/Cacti/cacti/issues/2871): Report when RRA's heartbeat is below the data source profile's interval
- feature [#3131](https://github.com/Cacti/cacti/issues/3131): Add utility feature to reindex hosts with bad indexes
- feature [#3578](https://github.com/Cacti/cacti/issues/3578): Allow Re-indexing of Devices to be Scheduled
- feature [#4025](https://github.com/Cacti/cacti/issues/4025): When importing a Template or Package, allow the user to ignore template and use the system default dimensions
- feature [#4239](https://github.com/Cacti/cacti/issues/4239): On "Graph Utility View" add the name of and a link to the graph template which the graph is based on
- feature [#4417](https://github.com/Cacti/cacti/issues/4417): Support execution of custom functions at poller bottom for remote pollers
- feature [#4754](https://github.com/Cacti/cacti/issues/4754): The script ss\_fping.php should timeout based on the host
- feature [#4762](https://github.com/Cacti/cacti/issues/4762): Allow Package Import to be selective
- feature [#4786](https://github.com/Cacti/cacti/issues/4786): Windows install does not support SVG rendering
- feature [#4820](https://github.com/Cacti/cacti/issues/4820): When importing, make it possible to only import certain components
- feature [#4841](https://github.com/Cacti/cacti/issues/4841): Move the `cactid` function `db_check_reconnect()` to `lib/database.php` for other service oriented scripts
- feature [#4874](https://github.com/Cacti/cacti/issues/4874): Add support for Business Hours
- feature [#4890](https://github.com/Cacti/cacti/issues/4890): Add multi threading for Poller recache script
- feature [#4899](https://github.com/Cacti/cacti/issues/4899): Allow script server to be told when the main database when offline or in recovery
- feature [#4901](https://github.com/Cacti/cacti/issues/4901): Make the script server accept arguments in the standard way
- feature [#4902](https://github.com/Cacti/cacti/issues/4902): Increase compatibility with MySQL 8.x
- feature [#4907](https://github.com/Cacti/cacti/issues/4907): Add lmSensors to the Net-SNMP Device Template
- feature [#4926](https://github.com/Cacti/cacti/issues/4926): Allow the user to override Cacti's built-in Time Zone detection
- feature [#4943](https://github.com/Cacti/cacti/pull/4943): Add ability to periodically check RRDfiles for errors in batch
- feature [#4948](https://github.com/Cacti/cacti/issues/4948): When security cookie times out, redirection does not always occur properly
- feature [#4955](https://github.com/Cacti/cacti/issues/4955): Provide memory tuning based upon MySQL Tuner recommendations
- feature [#4956](https://github.com/Cacti/cacti/issues/4956): The function `db_check_reconnect()` should be able to work with any connection
- feature [#4957](https://github.com/Cacti/cacti/issues/4957): Add Device Template categories to match the classes of the Package Plugin
- feature [#4965](https://github.com/Cacti/cacti/issues/4965): When unlocking a tree, entire page should not need rebuilding
- feature [#4967](https://github.com/Cacti/cacti/issues/4967): Make adding Associated Graph Templates and Data Queries easier to use
- feature [#4989](https://github.com/Cacti/cacti/issues/4989): Improve table performance by caching 'Total Rows' using a hash
- feature [#5009](https://github.com/Cacti/cacti/pull/5009): Allow SNMP Value OIDs to be parsed using regular expressions
- feature: Adding ESXi Device Template
- feature: Upgrade jQuery to version 3.6.1
- feature: Upgrade jQueryUI to version 1.13.2
- feature: Upgrade billboard.js to version 3.6
- feature: Introduce exec() function with timeout

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group

## What's Changed

[Read more](https://github.com/Cacti/cacti/releases/tag/release%2F1.2.23)

## v1.2.22

# Release of Cacti 1.2.22

Thank you everyone who are using Cacti and especially those helping to make Cacti better!

For additional details check out the [README](https://github.com/Cacti/cacti/blob/develop/README.md) located on [GitHub](https://github.com/Cacti/).

# Contribute

Active development of Cacti is located on [GitHub](https://github.com/Cacti/)!  Join us in making Cacti better, submit issues, fork and submit pull requests!

# Cacti Change Log

- security [#4834](https://github.com/Cacti/cacti/issues/4834): When creating new graphs, cross site injection is possible
- issue [#4768](https://github.com/Cacti/cacti/issues/4768): When creating user from template, multiple Domain FullName and Mail are not propagated
- issue [#4791](https://github.com/Cacti/cacti/issues/4791): Nectar Aggregate 95th emailed report broken
- issue [#4796](https://github.com/Cacti/cacti/issues/4796): Boost may not find archive tables correctly
- issue [#4802](https://github.com/Cacti/cacti/issues/4802): Users may be unable to change their password when forced during a login
- issue [#4803](https://github.com/Cacti/cacti/issues/4803): Net-SNMP Memory Graph Template has Wrong GPRINT
- issue [#4806](https://github.com/Cacti/cacti/issues/4806): Search in tree view unusable on larger installations
- issue [#4808](https://github.com/Cacti/cacti/issues/4808): Increased bulk insert size to avoid partial inserts and potential data loss.
- issue [#4810](https://github.com/Cacti/cacti/issues/4810): Call to undefined function boost\_debug in Cacti log
- issue [#4814](https://github.com/Cacti/cacti/issues/4814): When no guest template is set, login cookies are not properly set
- issue [#4817](https://github.com/Cacti/cacti/issues/4817): Later RRDtool releases do not need to check last\_update time
- issue [#4818](https://github.com/Cacti/cacti/issues/4818): Regex filters are not always long enough
- issue [#4819](https://github.com/Cacti/cacti/issues/4819): Domains based LDAP and AD Fullname and Email not auto-populated
- issue [#4822](https://github.com/Cacti/cacti/issues/4822): Cacti polling and boost report the wrong number of Data Sources when Devices are disabled
- issue [#4823](https://github.com/Cacti/cacti/issues/4823): When editing Graph Template Items there are cases where VDEF's are hidden when they should be shown
- issue [#4831](https://github.com/Cacti/cacti/issues/4831): Database SSL setting lacks default value
- issue [#4837](https://github.com/Cacti/cacti/pull/4837): Update default path cacti under \*BSD by xmacan
- issue [#4840](https://github.com/Cacti/cacti/issues/4840): Web Basic authentication not creating template user
- issue [#4846](https://github.com/Cacti/cacti/issues/4846): Unable to change the Heartbeat of a Data Source Profile
- issue [#4849](https://github.com/Cacti/cacti/issues/4849): Tree Search Does Not Properly Search All Trees
- issue [#4850](https://github.com/Cacti/cacti/issues/4850): When structured paths are setup, RRDfiles may not always be created when possible
- issue [#4851](https://github.com/Cacti/cacti/issues/4851): When parsing the logs, caching would help speed up processing
- issue [#4853](https://github.com/Cacti/cacti/issues/4853): Deprecation warnings when attempting real-time Graphs with PHP8.1
- issue [#4860](https://github.com/Cacti/cacti/issues/4860): Custom Timespan is lost when clicking other tree branches
- issue [#4863](https://github.com/Cacti/cacti/issues/4863): Non device based Data Sources not being polled
- issue [#4865](https://github.com/Cacti/cacti/issues/4865): When Resource XML file inproperly formatted, graph creation can fail with errors
- issue [#4866](https://github.com/Cacti/cacti/issues/4866): Update code style to support PHP 8 requirements
- issue [#4867](https://github.com/Cacti/cacti/issues/4867): In Graph Management, filtering for "Device: None" shows all graphs
- issue [#4871](https://github.com/Cacti/cacti/issues/4871): Realtime popup window experiences issues on some browsers
- issue [#4873](https://github.com/Cacti/cacti/pull/4873): Auth settings do not always properly reflect the options selected by ddb4github
- issue [#4880](https://github.com/Cacti/cacti/issues/4880): MySQL can cause cacti to become stalled due to locking issues
- issue [#4882](https://github.com/Cacti/cacti/issues/4882): Boost process can get hung under rare conditions until the poller times out
- issue [#4884](https://github.com/Cacti/cacti/issues/4884): Exporting graphs under PHP 8 can cause errors
- issue [#4887](https://github.com/Cacti/cacti/issues/4887): Host table has wrong default for disabled and deleted columns
- feature [#4533](https://github.com/Cacti/cacti/issues/4533): RRD storage paths do not scale properly
- feature [#4820](https://github.com/Cacti/cacti/issues/4820): When importing, make it possible to only import certain components
- feature [#4825](https://github.com/Cacti/cacti/pull/4825): Update change\_device script to include new features by bmfmancini
- feature [#4827](https://github.com/Cacti/cacti/issues/4827): Make help pages use latest online version wherever possible
- feature [#4832](https://github.com/Cacti/cacti/issues/4832): Cacti should show PHP INI locations during install
- feature [#4833](https://github.com/Cacti/cacti/issues/4833): Detect PHP INI values that are different in the INI vs running config
- feature [#4870](https://github.com/Cacti/cacti/pull/4870): Added Gradient Color support for AREA charts by thurban
- feature [#4872](https://github.com/Cacti/cacti/issues/4872): Update CDEF functions for RRDtool
- feature [#4881](https://github.com/Cacti/cacti/issues/4881): When boost is running, it's not clear which processes are running and how long they have to complete

# Reporting Issues

[http://www.cacti.net/issues.php](http://www.cacti.net/issues.php)

# Download Cacti

[http://www.cacti.net/download\_cacti.php](http://www.cacti.net/download_cacti.php)

# Download Spine

[http://www.cacti.net/spine\_download.php](http://www.cacti.net/spine_download.php)

Thanks!

The Cacti Group
