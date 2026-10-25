# extract: served via trafilatura-direct
---
title: Synology_SA_26_14 | Synology Inc.
author: Synology Inc
url: https://www.synology.com/
hostname: synology.com
description: Synology Product Security Advisory
sitename: Synology Inc.
date: "2026-10-22"
fingerprint: b8018791caa98961
---
# Synology-SA-26:14 PHP2Shell

Publish Time: UTC+8

Last Updated: UTC+8

- Severity
- Critical

- Status
- Resolved

**Abstract**

Multiple vulnerabilities allow remote attackers to execute arbitrary code via susceptible versions of the following packages in DSM:

- PHP 7.3, PHP 7.4, PHP 8.0, PHP 8.1, PHP 8.2, PHP 8.3, and PHP 8.4
- Mail Station
- Synology Calendar

Please refer to the ‘Affected Products’ table for the corresponding updates.

**Affected Products**

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| Synology Calendar | Critical | Upgrade to 3.0.4-21435 or above. | 
| Mail Station | Critical | Upgrade to 30000002.3.19-20333 or above. | 
| PHP 7.3 | Critical | No fix will be provided as this version has reached end of life. | 
| PHP 7.4 | Critical | Upgrade to 7.4.33-0131 or above. | 
| PHP 8.0 | Critical | Upgrade to 8.0.30-0122 or above. | 
| PHP 8.1 | Critical | Upgrade to 8.1.34-0120 or above. | 
| PHP 8.2 | Critical | Upgrade to 8.2.35-0171 or above. | 
| PHP 8.3 | Critical | Upgrade to 8.3.36-0051 or above. | 
| PHP 8.4 | Critical | Upgrade to 8.4.27-0051 or above. | 

**Mitigation**

https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w

https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp

The built-in PHP in OS is not exposed to external attack surfaces, and the risk of exploitation is considered very low.

**Detail**

- CVE-2026-109618 
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-1325: Improperly Controlled Sequential Memory Allocation](https://cwe.mitre.org/data/definitions/1325.html)
  - PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).
- CVE-2026-109619 
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-1325: Improperly Controlled Sequential Memory Allocation](https://cwe.mitre.org/data/definitions/1325.html)
  - PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

**Reference**

**Revision**

| Revision | Date | Description | 
|---|---|---|
| 1 | 2026-10-22 | Initial public release. |
