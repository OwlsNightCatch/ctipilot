---
title: Craft CMS 4.0.0 before 4.18.9 SQL Injection via Element Search Endpoint
url: https://www.vulncheck.com/advisories/craft-cms-4.0.0-before-4.18.9-sql-injection-via-element-search-endpoint
hostname: vulncheck.com
description: "CVE-2026-123488 | null | Affecting cms >= 4.0.0, < 4.18.9, cms >= 5.0.0, < 5.11.2 | Severity: CRITICAL | CVSS: 9.3"
sitename: VulnCheck
date: "2026-11-06"
fingerprint: a8993c9d8bffde93
---
Advisories

- Severity
- critical
- Date
- Affecting
  - cms >= 4.0.0, \< 4.18.9
  - cms >= 5.0.0, \< 5.11.2
- CWE
  - CWE-89 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- CVSS
- 9.3
- CVSS V4 Vector
- CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
- Description
- Craft CMS 4.0.0 before 4.18.9 and 5.0.0 before 5.11.2 contains an unauthenticated SQL injection vulnerability in the element search endpoint because the attribute parameter is concatenated into the query unsanitized and emulated PDO prepares allow stacked statements. Remote attackers can read and write the database, setting the admin flag or overwriting password hashes in the users table to gain administrator access.
- VulnCheck KEV
- [This advisory is in the VulnCheck KEV database](https://api.vulncheck.com/v3/index/vulncheck-kev?cve=CVE-2026-123488)

Explore VulnCheck, a next-generation Cyber Threat Intelligence platform, which provides exploit and vulnerability intelligence to help you prioritize and remediate vulnerabilities that matter.

- Vulnerability PrioritizationPrioritize vulnerabilities that matter based on the threat landscape and defer vulnerabilities that don't.
- Early Warning SystemReal-time alerting of changes in the vulnerability landscape so that you can take action before the attacks start.
