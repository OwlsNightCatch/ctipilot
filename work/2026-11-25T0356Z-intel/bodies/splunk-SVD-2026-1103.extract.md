---
title: Security Vulnerabilities in Splunk Enterprise - November 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1103
hostname: splunk.com
description: Splunk addressed multiple vulnerabilities in Splunk Enterprise. See CVE Details for vulnerability-specific and product-specific information.
sitename: Splunk Vulnerability Disclosure
date: "2026-11-18"
fingerprint: ec82c59cc3fc81ca
language: en
image: https://advisory.splunk.com/assets/img/logo_color.jpg
filedate: "2026-11-25"
---

# Security Vulnerabilities in Splunk Enterprise - November 2026

**Advisory ID:** SVD-2026-1103

**Published:** 2026-11-18

**Highest CVSSv3.1 Score:** 9.4, Critical

**Last Updated:** 2026-11-18

## Description

Splunk addressed multiple vulnerabilities in Splunk Enterprise. See CVE Details for vulnerability-specific and product-specific information.

## Solutions

Upgrade Splunk Enterprise versions 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17 or higher.

## Product Status

| Product | Base Version | Affected Version | Fix Version | 
|---|---|---|---|
| Splunk Enterprise | 10.6 | 10.6.0.5 | 10.6.1 | 
| Splunk Enterprise | 10.4 | 10.4.0 to 10.4.4 | 10.4.5 | 
| Splunk Enterprise | 10.2 | 10.2.0 to 10.2.8 | 10.2.9 | 
| Splunk Enterprise | 10.0 | 10.0.0 to 10.0.11 | 10.0.12 | 
| Splunk Enterprise | 9.4 | 9.4.0 to 9.4.16 | 9.4.17 | 

## Vulnerabilities

| CVE | Summary | CWE | Severity | Score | 
|---|---|---|---|---|
| [CVE-2026-76532](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76532) | Sensitive Information Disclosure through the Saved Searches REST API in Splunk Enterprise | [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-76533](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76533) | Improper Authentication Handling after Splunk Web Logout in Splunk Enterprise | [CWE-613](https://cwe.mitre.org/data/definitions/613.html) | Medium | [4.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-76534](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76534) | Improper Input Validation during User Account Creation through the REST API in Splunk Enterprise for Windows | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Medium | [4.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L) | 
| [CVE-2026-76535](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76535) | Authentication Bypass through the RapidDiag REST API in Splunk Enterprise | [CWE-287](https://cwe.mitre.org/data/definitions/287.html) | Critical | [9.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-76536](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76536) | Authentication Bypass through the Cluster Configuration REST API in Splunk Enterprise | [CWE-287](https://cwe.mitre.org/data/definitions/287.html) | Critical | [9.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H) | 
| [CVE-2026-76537](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76537) | Sensitive Information Disclosure through the Cluster Manager Bundle REST API in Splunk Enterprise | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-76538](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76538) | SPL Injection through the REST API in Splunk Enterprise | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-76539](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76539) | Improper Access Control through the REST API in Splunk Enterprise | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-76540](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76540) | Improper Authorization through the REST API in Splunk Enterprise | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-76541](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76541) | SPL Injection through Data Model Calculations in Splunk Enterprise | [CWE-77](https://cwe.mitre.org/data/definitions/77.html) | Medium | [4.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N) | 
| [CVE-2026-76542](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76542) | SPL Injection through Splunk Web Field Reports in Splunk Enterprise | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-76543](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76543) | SPL Injection through Data Model Regular Expression Field Preview in Splunk Enterprise | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-76544](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76544) | SPL Injection through Metric Alert Filters in Splunk Enterprise | [CWE-77](https://cwe.mitre.org/data/definitions/77.html) | High | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-76545](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-76545) | Information Disclosure through the REST API and Splunk Web in Splunk Enterprise | [CWE-204](https://cwe.mitre.org/data/definitions/204.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L) | 
| [CVE-2026-131174](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131174) | Missing Authorization when Restoring Archived Indexed Data through the REST API in Splunk Enterprise | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L) | 
| [CVE-2026-131175](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131175) | SPL Injection through Analytics Workspace Metric Alerts in Splunk Enterprise | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131176](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131176) | Missing Authorization for HTML-Based Views through the REST API in Splunk Enterprise | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131177](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131177) | SPL Injection through Saved Search Dispatch in Splunk Enterprise | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131178](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131178) | SPL Injection through Classic Dashboard Searches in Splunk Enterprise | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | High | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131179](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131179) | Search Processing Language (SPL) Injection through Splunk Web in Splunk Enterprise | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | High | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131180](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131180) | SPL Injection through the rename Command in Splunk Enterprise | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Medium | [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131181](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131181) | Search Processing Language (SPL) Injection in Data Model Acceleration in Splunk Enterprise | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:L) | 
| [CVE-2026-131182](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131182) | SPL Injection through Shared Dashboards in Splunk Enterprise | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | High | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131183](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131183) | SPL Injection through Classic Dashboard in Splunk Enterprise | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131184](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131184) | Stored Cross-Site Scripting (XSS) through Monitoring Console Platform Alerts in Splunk Enterprise | [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | Medium | [6.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131185](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131185) | Denial of Service (DoS) through the Apps Backup and Restore REST API in Splunk Enterprise | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | 
| [CVE-2026-131186](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131186) | Path Traversal in Deployment Server Remote Input Listing in Splunk Enterprise | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131187](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131187) | Sensitive Information Disclosure through Knowledge Bundle Replication in Splunk Enterprise | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131188](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131188) | SPL Command Safeguards Bypass through Cross-Site Request Forgery (CSRF) in Portable Document Format (PDF) Generation in Splunk Enterprise | [CWE-352](https://cwe.mitre.org/data/definitions/352.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131189](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131189) | Audit Log Injection through the REST API in Splunk Enterprise | [CWE-117](https://cwe.mitre.org/data/definitions/117.html) | Medium | [5.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131190](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131190) | Authentication Bypass through the RapidDiag REST API in Splunk Enterprise | [CWE-798](https://cwe.mitre.org/data/definitions/798.html) | High | [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131191](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131191) | Sensitive Information Disclosure through the Deployment Server REST API in Splunk Enterprise | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131192](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131192) | Authentication Bypass through the REST API in Splunk Enterprise | [CWE-305](https://cwe.mitre.org/data/definitions/305.html) | High | [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131193](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131193) | Improper Input Validation through HTTP Event Collector Token Names in Splunk Enterprise | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131194](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131194) | Stored Cross-Site Scripting (XSS) through Splunk Web Views in Splunk Enterprise | [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | Medium | [4.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131195](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131195) | Denial of Service (DoS) through HTTP PubSub Channel Subscriptions in Splunk Enterprise | [CWE-401](https://cwe.mitre.org/data/definitions/401.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H) | 
| [CVE-2026-131196](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131196) | Denial of Service (DoS) through Splunk-to-Splunk Data Forwarding in Splunk Enterprise | [CWE-476](https://cwe.mitre.org/data/definitions/476.html) | High | [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | 
| [CVE-2026-131197](https://advisory.splunk.com/advisories/SVD-2026-1103#cve-2026-131197) | Privilege Escalation through Splunk Web Dashboards in Splunk App for Splunk Observability Cloud | [CWE-732](https://cwe.mitre.org/data/definitions/732.html) | Medium | [6.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N) | 

## CVE Details

### [CVE-2026-76532](https://www.cve.org/CVERecord?id=CVE-2026-76532): Sensitive Information Disclosure through the Saved Searches REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who does not hold the “admin” or “power” Splunk roles could view credentials configured for email notifications in a saved search shared with that user. The vulnerability is possible when email notifications use authentication credentials because the Saved Searches Representational State Transfer (REST) API returns those credentials in clear text. For more information see [Search endpoint descriptions](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.6/search-endpoints/search-endpoint-descriptions), [Manage knowledge object permissions](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.6/get-started-with-knowledge-objects/manage-knowledge-object-permissions), and [Email notification action](https://help.splunk.com/en/splunk-enterprise/alert-and-respond/alerting-manual/10.6/configure-alert-actions/email-notification-action) in the Splunk documentation.

**Bug ID:** VULN-83518

**CWE:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-76533](https://www.cve.org/CVERecord?id=CVE-2026-76533): Improper Authentication Handling after Splunk Web Logout in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17 on Ubuntu and AlmaLinux, an unauthenticated user who obtains a valid Splunk Web session cookie before the affected user logs out could continue using the cookie after logout to access data and perform actions available to that user. The vulnerability is possible because the logout flow does not invalidate the associated session token on affected deployments. The attacker must obtain the valid session cookie before the affected user logs out of Splunk Web. The issue was reproduced in Splunk Enterprise installations on Ubuntu and AlmaLinux.

**Bug ID:** VULN-59389

**CWE:** [CWE-613](https://cwe.mitre.org/data/definitions/613.html)

**CVSSv3.1 Score:** 4.2, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-76534](https://www.cve.org/CVERecord?id=CVE-2026-76534): Improper Input Validation during User Account Creation through the REST API in Splunk Enterprise for Windows

#### Description

In Splunk Enterprise for Windows versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, a user that holds a role with the `edit_user` capability could create multiple user accounts that share the same user directory. This could expose user-specific configuration between those accounts, let one account modify configuration used by another account, or disrupt features that depend on separate user directories. The vulnerability is caused by improper validation of usernames before Splunk Enterprise performs Windows filesystem operations. Windows removes trailing periods from directory names, so distinct usernames can resolve to the same user directory. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-65729

**CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

**CVSSv3.1 Score:** 4.7, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L)

#### Mitigations and Workarounds

None

**Acknowledgments:** Gabriel Nitu, Splunk

### [CVE-2026-76535](https://www.cve.org/CVERecord?id=CVE-2026-76535): Authentication Bypass through the RapidDiag REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could run arbitrary Search Processing Language (SPL) searches through RapidDiag task collection as an authenticated user. With this access, the user could read or modify data and configuration available to that authenticated user. The vulnerability is possible because Splunk Enterprise accepts an empty shared secret when it authenticates RapidDiag task-collection requests. For more information see [Using RapidDiag](https://help.splunk.com/en/splunk-enterprise/administer/troubleshoot/9.3/contact-splunk-support/using-rapiddiag) in the Splunk documentation.

**Bug ID:** VULN-88197

**CWE:** [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

**CVSSv3.1 Score:** 9.1, Critical

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off requests authenticated with an empty shared secret by setting `pass4SymmKey = <non-empty value>` in the `server.conf` configuration file if you do not use an empty shared secret. Use the same value on each node that participates in the service and restart Splunk Enterprise after the change. For more information see [Secure Splunk Enterprise services with pass4SymmKey](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/secure-distributed-and-clustered-splunk-environments/secure-splunk-enterprise-services-with-pass4symmkey) in the Splunk documentation.

### [CVE-2026-76536](https://www.cve.org/CVERecord?id=CVE-2026-76536): Authentication Bypass through the Cluster Configuration REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could use an empty clustering shared secret to read and modify clustering configuration through the cluster configuration Representational State Transfer (REST) API endpoint on a standalone instance. This could expose clustering configuration, persist attacker-controlled clustering settings, and disrupt clustering operations. The vulnerability is possible because Splunk Enterprise accepts the empty clustering shared secret as a shared-authentication candidate on a standalone instance when clustering is turned off.

**Bug ID:** VULN-88731

**CWE:** [CWE-287](https://cwe.mitre.org/data/definitions/287.html)

**CVSSv3.1 Score:** 9.4, Critical

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:H)

#### Mitigations and Workarounds

If you cannot immediately upgrade to a fixed version, set a strong, unique `pass4SymmKey` value in the `[clustering]` stanza in the `server.conf` configuration file, including on standalone instances. The `pass4SymmKey` value must contain at least 12 characters. The file is at `etc/system/local/server.conf` under the Splunk Enterprise installation directory. Restart Splunk Enterprise for the change to take effect. For more information see [Secure Splunk Enterprise services with pass4SymmKey](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/secure-distributed-and-clustered-splunk-environments/secure-splunk-enterprise-services-with-pass4symmkey) in the Splunk documentation.

### [CVE-2026-76537](https://www.cve.org/CVERecord?id=CVE-2026-76537): Sensitive Information Disclosure through the Cluster Manager Bundle REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.0, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who does not hold a role with either the `list_indexer_cluster` capability or the `edit_indexer_cluster` capability could download the cluster manager configuration bundle through the Representational State Transfer (REST) API and access configuration and app files that the cluster manager stages for indexer distribution. The vulnerability is possible because the REST API does not require the `list_indexer_cluster` or `edit_indexer_cluster` capability before it sends the configuration bundle. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation. For more information see [Cluster endpoint descriptions](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.6/cluster-endpoints/cluster-endpoint-descriptions) in the Splunk documentation.

**Bug ID:** VULN-89743

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-76538](https://www.cve.org/CVERecord?id=CVE-2026-76538): SPL Injection through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could cause Splunk Enterprise to run arbitrary Search Processing Language (SPL) searches with elevated privileges through data model acceleration. The vulnerability is possible because Splunk Enterprise does not correctly neutralize caller-supplied data model acceleration values before it places them into generated summarization searches.

**Bug ID:** VULN-89763

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-76539](https://www.cve.org/CVERecord?id=CVE-2026-76539): Improper Access Control through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could use the search jobs Representational State Transfer (REST) API to access indexed events that the `srchFilter` setting for the role should hide. The same user could also run internal Search Processing Language (SPL) commands and bypass SPL safeguards for risky commands within indexes that the role can search. The vulnerability is possible because Splunk Enterprise does not correctly escape required field values before it includes them in an internally generated search. For more information, see [Search endpoint descriptions](https://help.splunk.com/en/splunk-enterprise/rest-api-reference/9.4/search-endpoints/search-endpoint-descriptions), [authorize.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.5-configuration-file-reference/authorize.conf), and [SPL safeguards for risky commands](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/best-practices-for-splunk-platform-security/spl-safeguards-for-risky-commands).

**Bug ID:** VULN-89714

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-76540](https://www.cve.org/CVERecord?id=CVE-2026-76540): Improper Authorization through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 9.4.17, 10.0.12, 10.2.9, and 10.4.5, a user who does not hold the “admin” or “power” Splunk roles can configure a metric alert through the Representational State Transfer (REST) API that runs a search with elevated privileges. The vulnerability lets the user access or modify data and disrupt the Splunk Enterprise instance. The vulnerability occurs because Splunk Enterprise does not enforce the required role-based authorization when it processes metric alert configuration through the REST API. Splunk Enterprise schedules the resulting search with elevated authorization and runs attacker-controlled search processing with that authorization. For more information see [About configuring role-based user access](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/manage-splunk-platform-users-and-roles/about-configuring-role-based-user-access) in the Splunk documentation.

**Bug ID:** VULN-89702

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-76541](https://www.cve.org/CVERecord?id=CVE-2026-76541): SPL Injection through Data Model Calculations in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.0, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could store attacker-controlled Search Processing Language (SPL) in a shared data model calculation. When a user who can run a search against the shared data model runs one, the injected SPL can run using the permissions of the user who ran the search. This could expose sensitive credentials to the user who created the shared data model. The vulnerability is possible because Splunk Enterprise does not safely neutralize data model calculation fields before it includes them in generated searches. For more information see [About data models](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/build-a-data-model/about-data-models) in the Splunk documentation. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-80538

**CWE:** [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

**CVSSv3.1 Score:** 4.8, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-76542](https://www.cve.org/CVERecord?id=CVE-2026-76542): SPL Injection through Splunk Web Field Reports in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could trick a user who has an active Splunk Web session into selecting the Top values by time field report on the Search page. The selection could run arbitrary Search Processing Language (SPL) searches and potentially expose stored credentials and indexed data. The vulnerability is possible because Splunk Web does not correctly neutralize user-controlled data when it generates an SPL search for a field report. The vulnerability requires the attacker to phish the user by tricking them into opening a link that the attacker creates. The unauthenticated user should not be able to exploit the vulnerability at will.

**Bug ID:** VULN-89718

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-76543](https://www.cve.org/CVERecord?id=CVE-2026-76543): SPL Injection through Data Model Regular Expression Field Preview in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could store attacker-controlled Search Processing Language (SPL) in a shared data model. The vulnerability is possible because the Data Model Editor does not properly neutralize data model field names when it builds a preview search. The vulnerability requires the attacker to phish the affected user by tricking them into initiating a request within their browser. The attacker should not be able to exploit the vulnerability at will. For more information see [Add a regular expression field](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/define-data-model-dataset-fields/add-a-regular-expression-field), [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities), and [About the search language](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.4/search-overview/about-the-search-language) in the Splunk documentation.

**Bug ID:** VULN-89758

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.4-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-76544](https://www.cve.org/CVERecord?id=CVE-2026-76544): SPL Injection through Metric Alert Filters in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could cause scheduled metric alert searches to run arbitrary Search Processing Language (SPL) commands and access credentials stored in cleartext. This requires at least one non-internal metric index on the instance. The vulnerability is possible because Splunk Enterprise does not fully validate metric alert filter input before using it in a scheduled search.

**Bug ID:** VULN-81808

**CWE:** [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

**CVSSv3.1 Score:** 8.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-76545](https://www.cve.org/CVERecord?id=CVE-2026-76545): Information Disclosure through the REST API and Splunk Web in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could determine whether a username exists through the Representational State Transfer (REST) API or Splunk Web and lock out existing user accounts through repeated login attempts. The vulnerability is possible because Splunk Enterprise returns different login failure responses for locked existing user accounts and nonexistent usernames.

**Bug ID:** VULN-91638

**CWE:** [CWE-204](https://cwe.mitre.org/data/definitions/204.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131174](https://www.cve.org/CVERecord?id=CVE-2026-131174): Missing Authorization when Restoring Archived Indexed Data through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could make unauthorized changes when restoring archived indexed data or cause a Denial of Service (DoS) on the Splunk Enterprise instance. The vulnerability is possible because the Representational State Transfer (REST) API does not require the `indexes_edit` capability for archived-data restoration actions. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation. For more information see [Restore archived indexed data](https://help.splunk.com/en/splunk-enterprise/administer/manage-indexers-and-indexer-clusters/10.6/back-up-and-archive-your-indexes/restore-archived-indexed-data) in the Splunk documentation.

**Bug ID:** VULN-89820

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131175](https://www.cve.org/CVERecord?id=CVE-2026-131175): SPL Injection through Analytics Workspace Metric Alerts in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, a user who holds the “power” Splunk role could create and share a metric alert that causes Analytics Workspace to run a malicious Search Processing Language (SPL) when another authenticated user opens a link to the alert. The malicious SPL could expose data, modify data, or disrupt services available in the affected session. The vulnerability is possible because Analytics Workspace does not fully neutralize metric alert names before including the names in SPL. The vulnerability requires the attacker to phish the user by tricking them into opening a link that the attacker creates. The user who holds the “power” Splunk role should not be able to exploit the vulnerability at will. For more information see [Alerts in the Analytics Workspace](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/analytics-workspace/10.4/using-the-analytics-workspace/alerts-in-the-analytics-workspace) and [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-91360

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 7.6, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131176](https://www.cve.org/CVERecord?id=CVE-2026-131176): Missing Authorization for HTML-Based Views through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.17, a user that holds a role with the `edit_own_objects` capability but does not hold the `edit_view_html` capability could create or modify a private Hypertext Markup Language (HTML) view through the Representational State Transfer (REST) API. The vulnerability is possible because the REST API applies the `edit_own_objects` capability when it creates or modifies private HTML-based views instead of requiring the `edit_view_html` capability. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-89807

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131177](https://www.cve.org/CVERecord?id=CVE-2026-131177): SPL Injection through Saved Search Dispatch in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could run arbitrary Search Processing Language (SPL) searches with elevated privileges through saved search dispatch and access stored credentials and indexed data or modify lookup data. The vulnerability is possible because Splunk Enterprise does not correctly neutralize caller-supplied saved search dispatch values before it places the values into an SPL search. For more information see [Search endpoint descriptions](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.4/search-endpoints/search-endpoint-descriptions) in the Splunk documentation.

**Bug ID:** VULN-89816

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131178](https://www.cve.org/CVERecord?id=CVE-2026-131178): SPL Injection through Classic Dashboard Searches in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could craft a shared Classic Dashboard that runs arbitrary Search Processing Language (SPL) commands for another authenticated user. Exploitation requires the dashboard viewer to open the shared dashboard. The injected commands could access data available to the dashboard viewer, modify data available to the dashboard viewer, and partially disrupt Splunk Enterprise. For more information see [Add sparklines to search results](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.6/calculate-statistics/add-sparklines-to-search-results), [Configure dashboard permissions](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.6/manage-and-share-dashboards/configure-dashboard-permissions), and [SPL safeguards for risky commands](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/best-practices-for-splunk-platform-security/spl-safeguards-for-risky-commands) in the Splunk documentation.

**Bug ID:** VULN-89786

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 7.6, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131179](https://www.cve.org/CVERecord?id=CVE-2026-131179): Search Processing Language (SPL) Injection through Splunk Web in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could add attacker-controlled Search Processing Language (SPL) to a shared dashboard. When another user opens the dashboard in Splunk Web, Splunk Enterprise could run the attacker-controlled SPL using the permissions of that dashboard viewer. The attacker-controlled SPL could expose stored credentials, modify indexed data, and reduce availability. The vulnerability is possible because Splunk Enterprise does not neutralize special elements in search filter values before it builds optimized search jobs. The vulnerability requires the attacker to phish the affected user by tricking them into initiating a request within their browser. The attacker should not be able to exploit the vulnerability at will.

**Bug ID:** VULN-89794

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 7.6, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131180](https://www.cve.org/CVERecord?id=CVE-2026-131180): SPL Injection through the rename Command in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could create and share a dashboard that contains attacker-controlled Search Processing Language (SPL). The SPL could run using the permissions of the user who opens the dashboard. With this access, the user who created the dashboard could expose stored credentials and write data to an index. The vulnerability is possible because Splunk Enterprise does not correctly escape field names in searches that use the `rename` command. For more information see [rename](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.4/search-commands/rename) and [SPL safeguards for risky commands](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/best-practices-for-splunk-platform-security/spl-safeguards-for-risky-commands) in the Splunk documentation.

**Bug ID:** VULN-89792

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 6.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131181](https://www.cve.org/CVERecord?id=CVE-2026-131181): Search Processing Language (SPL) Injection in Data Model Acceleration in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.16, a user who does not hold the “admin” or “power” Splunk roles could use Data Model Acceleration to run malicious Search Processing Language (SPL) commands and perform actions through the Representational State Transfer (REST) API that the user cannot perform directly. The vulnerability is possible because Splunk Enterprise does not neutralize user-provided data before it adds that data to a generated search. For more information, see [Accelerate data models](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.2/use-data-summaries-to-accelerate-searches/accelerate-data-models), [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities), and [About the search language](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.6/search-overview/about-the-search-language).

**Bug ID:** VULN-89771

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131182](https://www.cve.org/CVERecord?id=CVE-2026-131182): SPL Injection through Shared Dashboards in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who holds the “power” Splunk role could store malicious Search Processing Language (SPL) in a shared dashboard. The malicious SPL could run using the permissions of the user who opened the dashboard and could access or modify data available to that user and disrupt Splunk Enterprise availability. The vulnerability is possible because Splunk Enterprise does not preserve quoted search argument boundaries when it processes a dashboard search. The vulnerability requires the attacker to phish the affected user by tricking them into initiating a request within their browser. The attacker, a user who holds the “power” Splunk role, should not be able to exploit the vulnerability at will.

**Bug ID:** VULN-89775

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 7.6, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131183](https://www.cve.org/CVERecord?id=CVE-2026-131183): SPL Injection through Classic Dashboard in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a low-privileged user who holds the “power” Splunk role could inject arbitrary Search Processing Language (SPL) commands into a Classic Dashboard search. When another user opens the affected dashboard in Splunk Web, those injected commands execute with the viewing user’s permissions, potentially allowing the low-privileged user to access stored credentials and write data to indexes. The vulnerability is possible because Splunk Enterprise does not correctly escape user-supplied content when it rewrites a search, which lets the rewritten search include additional SPL commands. The vulnerability requires another user to open the dashboard in Splunk Web. Consequently, a user who holds the “power” Splunk role should not be able to exploit the vulnerability at will. For more information see [SPL safeguards for risky commands](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/best-practices-for-splunk-platform-security/spl-safeguards-for-risky-commands) and [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-89797

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131184](https://www.cve.org/CVERecord?id=CVE-2026-131184): Stored Cross-Site Scripting (XSS) through Monitoring Console Platform Alerts in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a low-privileged user who does not hold the “admin” or “power” Splunk roles could inject a malicious script into the name of a private saved search. If another user subsequently enables, disables, or edits the corresponding platform alert in the Monitoring Console, the injected script executes within that user’s browser session, potentially allowing the low-privileged user to view sensitive information or modify data in Splunk Enterprise. The vulnerability is possible because the Monitoring Console does not safely handle saved-search names in the platform alert workflow. For more information see [Enable and configure platform alerts](https://help.splunk.com/en/splunk-enterprise/administer/monitor/10.4/configure-the-monitoring-console/enable-and-configure-platform-alerts) and [About configuring role-based user access](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/about-configuring-role-based-user-access) in the Splunk documentation.

**Bug ID:** VULN-91736

**CWE:** [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

**CVSSv3.1 Score:** 6.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131185](https://www.cve.org/CVERecord?id=CVE-2026-131185): Denial of Service (DoS) through the Apps Backup and Restore REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who does not hold the “admin” or “power” Splunk roles could use the apps backup and restore Representational State Transfer (REST) API to prevent subsequent apps backup or restore operations until Splunk Enterprise restarts. This could result in a Denial of Service (DoS). The vulnerability is possible because the apps backup and restore REST API handlers do not correctly enforce authorization.

**Bug ID:** VULN-91801

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131186](https://www.cve.org/CVERecord?id=CVE-2026-131186): Path Traversal in Deployment Server Remote Input Listing in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user that holds a role with the `list_deployment_server` capability could access sensitive information from `inputs.conf` files outside the intended deployment app directory through the Representational State Transfer (REST) API. The vulnerability is possible because the REST API does not restrict a deployment app name to an existing deployment app before reading input configurations. For more information see [authorize.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.4-configuration-file-reference/authorize.conf), [Deployment server architecture](https://help.splunk.com/en/splunk-enterprise/administer/update-your-deployment/9.0/deployment-server-and-forwarder-management/deployment-server-architecture), and [inputs.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/9.4/configuration-file-reference/9.4.16-configuration-file-reference/inputs.conf) in the Splunk documentation.

**Bug ID:** VULN-91830

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131187](https://www.cve.org/CVERecord?id=CVE-2026-131187): Sensitive Information Disclosure through Knowledge Bundle Replication in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, and 10.2.9, a low-privileged user who does not hold the “admin” or “power” Splunk roles could access file path and metadata listings from search head knowledge bundles via the Representational State Transfer (REST) API. This unauthorized access could expose sensitive metadata, including Splunk platform usernames, private knowledge-object configuration file names, installed application directories, and the file path names of security-sensitive configuration and key files. The vulnerability is possible because the REST API actions that list bundle contents and denied files use a capability available to the “user” role instead of requiring distributed-search administration capabilities. For more information see [Knowledge bundle replication overview](https://help.splunk.com/en/splunk-enterprise/administer/distributed-search/10.6/knowledge-bundle-replication/knowledge-bundle-replication-overview) in the Splunk documentation. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-91829

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

If users without the `list_dist_peer` capability do not require access to these endpoints, add capability = `list_dist_peer` under the `[admin:dist-handlers]` stanza in `$SPLUNK_HOME/etc/system/local/restmap.conf` and restart Splunk Enterprise. This restricts access to all endpoints within that handler group to users who hold the `list_dist_peer` capability. For more information see [settings in the restmap.conf configuration file](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/restmap.conf) in the Splunk documentation.

### [CVE-2026-131188](https://www.cve.org/CVERecord?id=CVE-2026-131188): SPL Command Safeguards Bypass through Cross-Site Request Forgery (CSRF) in Portable Document Format (PDF) Generation in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, an unauthenticated user could craft a malicious link that, if opened by an authenticated user, executes arbitrary Search Processing Language (SPL) searches with the victim’s permissions. Successful exploitation could allow the unauthenticated user to access or modify data, alter Splunk platform configurations, and disrupt operations available to the affected user. The vulnerability is possible because the Portable Document Format (PDF) generation component processes request data before it rejects deprecated GET requests and does not apply SPL safeguards for risky commands to subsearches. For more information see [Generate PDFs of your reports and dashboards](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/reporting-manual/10.4/report-management/generate-pdfs-of-your-reports-and-dashboards) and [SPL safeguards for risky commands](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/best-practices-for-splunk-platform-security/spl-safeguards-for-risky-commands) in the Splunk documentation.

**Bug ID:** VULN-91778

**CWE:** [CWE-352](https://cwe.mitre.org/data/definitions/352.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131189](https://www.cve.org/CVERecord?id=CVE-2026-131189): Audit Log Injection through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could inject arbitrary fields into Splunk Enterprise audit records via the Representational State Transfer (REST) API. Successful exploitation could allow the unauthenticated user to forge audit evidence, compromising the integrity of audit reviews and security detections that rely on legacy audit-field parsing. The vulnerability exists because Splunk Enterprise does not neutralize field delimiters in user-supplied data before writing the data to a legacy audit record. The affected workflow also does not create a corresponding structured audit record. For more information see [Auditing activities in a Splunk platform instance](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.0/audit-activity-in-splunk-enterprise/auditing-activities-in-a-splunk-platform-instance) and [About structured audit trail logs](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/audit-activity-in-splunk-enterprise/about-structured-audit-trail-logs) in the Splunk documentation.

**Bug ID:** VULN-91932

**CWE:** [CWE-117](https://cwe.mitre.org/data/definitions/117.html)

**CVSSv3.1 Score:** 5.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131190](https://www.cve.org/CVERecord?id=CVE-2026-131190): Authentication Bypass through the RapidDiag REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could access RapidDiag process metadata and log file inventory information through the Representational State Transfer (REST) API. The vulnerability is possible because certain RapidDiag REST API endpoints accept a factory-default shared key for node authentication, which lets requests bypass Splunk user authentication. For more information see [Using RapidDiag](https://help.splunk.com/en/splunk-enterprise/administer/troubleshoot/9.0/contact-splunk-support/using-rapiddiag) and [Secure Splunk Enterprise services with pass4SymmKey](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.0/secure-distributed-and-clustered-splunk-environments/secure-splunk-enterprise-services-with-pass4symmkey) in the Splunk documentation.

**Bug ID:** VULN-112484

**CWE:** [CWE-798](https://cwe.mitre.org/data/definitions/798.html)

**CVSSv3.1 Score:** 7.5, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

Turn off or remove the RapidDiag app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

**Acknowledgments:** Jason Storm, Splunk; Gabriel Nitu, Splunk

### [CVE-2026-131191](https://www.cve.org/CVERecord?id=CVE-2026-131191): Sensitive Information Disclosure through the Deployment Server REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user who does not hold the “admin” or “power” Splunk roles could read private index configuration values for other users through the deployment server Representational State Transfer (REST) API. The deployment server REST API does not limit a supplied repository location to configured deployment repositories before it reads `indexes.conf` stanzas.

**Bug ID:** VULN-91831

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131192](https://www.cve.org/CVERecord?id=CVE-2026-131192): Authentication Bypass through the REST API in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.6.1, 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could access live event data from the indexing pipeline through the Representational State Transfer (REST) API on a standalone instance or a search head that is not an indexer cluster member. The vulnerability is possible because Splunk Enterprise accepts an empty shared key during service authentication.

**Bug ID:** VULN-91881

**CWE:** [CWE-305](https://cwe.mitre.org/data/definitions/305.html)

**CVSSv3.1 Score:** 7.5, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

Set `pass4SymmKey` to a strong value in the `server.conf` configuration file under the `[clustering]` stanza. For more information see [Secure Splunk Enterprise services with pass4SymmKey](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/secure-distributed-and-clustered-splunk-environments/secure-splunk-enterprise-services-with-pass4symmkey) in the Splunk documentation.

### [CVE-2026-131193](https://www.cve.org/CVERecord?id=CVE-2026-131193): Improper Input Validation through HTTP Event Collector Token Names in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, a user holding a role with the edit\_token\_http capability could create a persistent HTTP Event Collector (HEC) token that cannot be disabled or deleted via the Representational State Transfer (REST) API or Splunk Web. As a result, the token remains active and can continue ingesting events even after administrative attempts to revoke it. The vulnerability is possible because HTTP Event Collector token creation accepts names that later management operations cannot process. For more information see [authorize.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.5-configuration-file-reference/authorize.conf) and [Set up and use HTTP Event Collector in Splunk Web](https://help.splunk.com/en/splunk-enterprise/get-data-in/get-started-with-getting-data-in/10.6/get-data-with-http-event-collector/set-up-and-use-http-event-collector-in-splunk-web) in the Splunk documentation.

**Bug ID:** VULN-91935

**CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

Turn off HTTP Event Collector if you do not use it. For more information see [Set up and use HTTP Event Collector in Splunk Web](https://docs.splunk.com/Documentation/Splunk/9.4.2/Data/UsetheHTTPEventCollector) in the Splunk documentation.

### [CVE-2026-131194](https://www.cve.org/CVERecord?id=CVE-2026-131194): Stored Cross-Site Scripting (XSS) through Splunk Web Views in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.4, 10.2.8, 10.0.11, and 9.4.16, a low-privileged user who holds the “power” Splunk role could inject malicious content into a Splunk Web view. When another authenticated user opens the affected view in Splunk Web, the injected content executes unauthorized JavaScript code within the viewing user’s browser session. The vulnerability is possible because Splunk Web does not properly validate content in a view definition before rendering the view. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) in the Splunk documentation.

**Bug ID:** VULN-91835

**CWE:** [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

**CVSSv3.1 Score:** 4.6, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with [Splunk Web](https://docs.splunk.com/Documentation/Splunk/latest/Security/DisableunnecessarySplunkcomponents) turned on. You could turn Splunk Web off as a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://docs.splunk.com/Documentation/Splunk/latest/Security/DisableunnecessarySplunkcomponents) and the [web.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Webconf) configuration specification file for more information on turning Splunk Web off.

### [CVE-2026-131195](https://www.cve.org/CVERecord?id=CVE-2026-131195): Denial of Service (DoS) through HTTP PubSub Channel Subscriptions in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user could send repeated HTTP PubSub channel subscription requests that cause a Denial of Service (DoS) by permanently increasing memory usage until Splunk Enterprise exhausts available memory. The vulnerability affects instances that turn on the `[pubsubsvr-http]` stanza in `server.conf` because the HTTP PubSub broker does not release memory associated with a channel after the client disconnects.

**Bug ID:** VULN-107692

**CWE:** [CWE-401](https://cwe.mitre.org/data/definitions/401.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H)

#### Mitigations and Workarounds

Turn off the HTTP PubSub broker by setting `disabled` = `true` in the `server.conf` configuration file if you do not use agent management over HTTP. For more information see [server.conf configuration specification file](https://help.splunk.com/en/data-management/splunk-enterprise-admin-manual/10.4/configuration-file-reference/10.4.4-configuration-file-reference/server.conf) in the Splunk documentation.

**Acknowledgments:** Pedro Cardoso (tvmpt)

### [CVE-2026-131196](https://www.cve.org/CVERecord?id=CVE-2026-131196): Denial of Service (DoS) through Splunk-to-Splunk Data Forwarding in Splunk Enterprise

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, 10.0.12, and 9.4.17, an unauthenticated user who can connect to a Splunk-to-Splunk (S2S) data forwarding receiver could cause the Splunk daemon to terminate unexpectedly. The unexpected termination interrupts data indexing and access to the management API and Splunk Web until the Splunk Enterprise process restarts. The vulnerability is possible because the S2S data forwarding receiver does not validate an optional field in forwarded event data, which results in a null pointer dereference when the field is missing. For more information see [Intermediate data routing using universal and heavy forwarders](https://help.splunk.com/en/splunk-enterprise/get-started/splunk-validated-architectures/getting-data-in-forwarding-and-preprocessing/intermediate-data-routing-using-universal-and-heavy-forwarders) in the Splunk documentation.

**Bug ID:** VULN-117328

**CWE:** [CWE-476](https://cwe.mitre.org/data/definitions/476.html)

**CVSSv3.1 Score:** 7.5, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

#### Mitigations and Workarounds

None

**Acknowledgments:** TBD

### [CVE-2026-131197](https://www.cve.org/CVERecord?id=CVE-2026-131197): Privilege Escalation through Splunk Web Dashboards in Splunk App for Splunk Observability Cloud

#### Description

In Splunk Enterprise versions below 10.4.5, 10.2.9, and 10.0.12, a low-privileged user who holds the “power” Splunk role could overwrite shared application dashboard views with arbitrary Search Processing Language (SPL) commands. When another authenticated user opens an affected dashboard in Splunk Web, Splunk Enterprise executes the injected SPL using the viewing user’s permissions, potentially allowing the low-privileged user to access or modify data available to that user. The vulnerability is possible because the affected app grants the “power” Splunk role write access to shared dashboard views that should be writable only by the “admin” Splunk role. The vulnerability is possible because the Splunk App for Splunk Observability Cloud grants the “power” Splunk role write access to shared dashboard views that should be writable only by the “admin” Splunk role

**Bug ID:** VULN-102937

**CWE:** [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

**CVSSv3.1 Score:** 6.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for Splunk Observability Cloud. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.
