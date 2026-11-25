---
title: Security Vulnerabilities in Splunk SOAR - November 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1108
hostname: splunk.com
description: Splunk addressed multiple vulnerabilities in Splunk SOAR. See CVE Details for vulnerability-specific and product-specific information.
sitename: Splunk Vulnerability Disclosure
date: "2026-11-18"
fingerprint: fc02c79ec3ec8769
language: en
image: https://advisory.splunk.com/assets/img/logo_color.jpg
filedate: "2026-11-25"
---

# Security Vulnerabilities in Splunk SOAR - November 2026

**Advisory ID:** SVD-2026-1108

**Published:** 2026-11-18

**Highest CVSSv3.1 Score:** 9.9, Critical

**Last Updated:** 2026-11-18

## Description

Splunk addressed multiple vulnerabilities in Splunk SOAR. See CVE Details for vulnerability-specific and product-specific information.

## Solutions

Upgrade Splunk SOAR to version 8.8.0 or higher.

## Product Status

| Product | Base Version | Affected Version | Fix Version | 
|---|---|---|---|
| Splunk SOAR | 8.8 | Below 8.8.0 | 8.8.0 | 

## Vulnerabilities

| CVE | Summary | CWE | Severity | Score | 
|---|---|---|---|---|
| [CVE-2026-131240](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131240) | Denial of Service (DoS) through the Container REST API in Splunk SOAR | [CWE-400](https://cwe.mitre.org/data/definitions/400.html) | Low | [3.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:N/A:L) | 
| [CVE-2026-131241](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131241) | Authorization Bypass Through the REST API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131242](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131242) | Improper Access Control through the REST API in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131243](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131243) | Sensitive Information Disclosure through the REST API in Splunk SOAR | [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | High | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L) | 
| [CVE-2026-131244](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131244) | Authorization Bypass through the Playbook API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131245](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131245) | Information Disclosure through the Approval Detail REST API in Splunk SOAR | [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131246](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131246) | Information Disclosure through REST API External Prompts in Splunk SOAR | [CWE-200](https://cwe.mitre.org/data/definitions/200.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131247](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131247) | Authorization Bypass in the REST API in Splunk SOAR | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131248](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131248) | Improper Access Control through the Tenant REST API in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | High | [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131249](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131249) | Improper Access Control in Child Playbook Callback Handles in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131250](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131250) | Improper Access Control in the REST API in Splunk SOAR | [CWE-915](https://cwe.mitre.org/data/definitions/915.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131251](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131251) | Authorization Bypass through Artifact Creation in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131252](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131252) | Missing Authorization in Cross-Tenant Asset Management through the REST API in Splunk SOAR | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131253](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131253) | Remote Code Execution (RCE) through the App Wizard in Splunk SOAR | [CWE-94](https://cwe.mitre.org/data/definitions/94.html) | Critical | [9.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) | 
| [CVE-2026-131254](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131254) | Improper Access Control through the REST API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131255](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131255) | Privilege Escalation through REST API User Role Assignment in Splunk SOAR | [CWE-706](https://cwe.mitre.org/data/definitions/706.html) | High | [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131256](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131256) | Remote Code Execution (RCE) through the REST API in Splunk SOAR | [CWE-829](https://cwe.mitre.org/data/definitions/829.html) | High | [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131257](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131257) | Improper Access Control through the REST API in Splunk SOAR | [CWE-915](https://cwe.mitre.org/data/definitions/915.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131258](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131258) | Stored Cross-Site Scripting (XSS) through the REST API in Splunk SOAR | [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | High | [8.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N) | 
| [CVE-2026-131259](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131259) | Improper Access Control through the Container REST API in Splunk SOAR | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131260](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131260) | Cross-Site Scripting (XSS) through the REST API in Splunk SOAR | [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | High | [8.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N) | 
| [CVE-2026-131261](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131261) | Remote Code Execution (RCE) through the REST API in Splunk SOAR | [CWE-829](https://cwe.mitre.org/data/definitions/829.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131262](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131262) | Improper Access Control through the REST API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131263](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131263) | Argument Injection during App Installation in Splunk SOAR | [CWE-88](https://cwe.mitre.org/data/definitions/88.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131264](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131264) | Information Exposure through the REST API in Splunk SOAR | [CWE-522](https://cwe.mitre.org/data/definitions/522.html) | Medium | [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | 
| [CVE-2026-131265](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131265) | Improper Access Control through the Ingestion Schedule View in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131266](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131266) | Information Disclosure through the REST API in Splunk SOAR | [CWE-201](https://cwe.mitre.org/data/definitions/201.html) | High | [7.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:L) | 
| [CVE-2026-131267](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131267) | Sensitive Information Disclosure through the REST API in Splunk SOAR | [CWE-522](https://cwe.mitre.org/data/definitions/522.html) | Medium | [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N) | 
| [CVE-2026-131268](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131268) | Remote Code Execution (RCE) through the REST API in Splunk SOAR | [CWE-427](https://cwe.mitre.org/data/definitions/427.html) | High | [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131269](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131269) | Remote Code Execution (RCE) through Python Dependencies in Splunk SOAR | [CWE-427](https://cwe.mitre.org/data/definitions/427.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131270](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131270) | Path Traversal through the REST API in Splunk SOAR | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131271](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131271) | Improper Access Control through the REST API in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131272](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131272) | Path Traversal through the Automation Dependency Wheel REST API in Splunk SOAR | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | High | [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131273](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131273) | Improper Access Control through Splunk Web in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131274](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131274) | Audit Trail Safeguards Bypass in Splunk SOAR REST API | [CWE-778](https://cwe.mitre.org/data/definitions/778.html) | Low | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131275](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131275) | Improper Input Validation of Timestamps through the REST API in Splunk SOAR | [CWE-915](https://cwe.mitre.org/data/definitions/915.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L) | 
| [CVE-2026-131276](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131276) | Improper Access Control in Splunk Web in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131277](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131277) | Path Traversal through the REST API in Splunk SOAR | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | Medium | [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:L) | 
| [CVE-2026-131278](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131278) | Sensitive Information Disclosure through App Editor Debug Actions in Splunk SOAR | [CWE-214](https://cwe.mitre.org/data/definitions/214.html) | High | [7.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131279](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131279) | Improper Handling of Artifact Associations through the REST API in Splunk SOAR | [CWE-697](https://cwe.mitre.org/data/definitions/697.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131280](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131280) | Sensitive Information Disclosure through the REST API in Splunk SOAR | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131281](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131281) | Insecure Default Audit Logging for Asset Approval and Effective User Changes through the REST API in Splunk SOAR | [CWE-778](https://cwe.mitre.org/data/definitions/778.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131282](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131282) | Information Exposure through the REST API in Splunk SOAR | [CWE-532](https://cwe.mitre.org/data/definitions/532.html) | High | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131283](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131283) | Improper Control of Playbook Conversion in Splunk SOAR | [CWE-665](https://cwe.mitre.org/data/definitions/665.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131284](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131284) | Improper Control of Artifact Workflow State through the REST API in Splunk SOAR | [CWE-915](https://cwe.mitre.org/data/definitions/915.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131285](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131285) | Authorization Bypass Through User-Controlled Key in Splunk SOAR Playbook Automation | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | 
| [CVE-2026-131286](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131286) | Improper Access Control through the REST API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131287](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131287) | Remote Code Execution (RCE) through the REST API in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Critical | [9.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:H/A:H) | 
| [CVE-2026-131288](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131288) | \[Flashpoint\] Privilege Escalation through HAProxy Cluster Operations in Splunk SOAR | [CWE-269](https://cwe.mitre.org/data/definitions/269.html) | High | [7.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131289](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131289) | Improper Validation through Playbook Safe Mode in Splunk SOAR | [CWE-345](https://cwe.mitre.org/data/definitions/345.html) | Low | [3.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N) | 
| [CVE-2026-131290](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131290) | Authorization Bypass in Splunk SOAR Playbook Status | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N) | 
| [CVE-2026-131291](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131291) | Authorization Bypass through the REST API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N) | 
| [CVE-2026-131292](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131292) | Improper Authorization in Splunk SOAR Custom-Function Status | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131293](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131293) | Improper Access Control in the Data Management Automation API in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | High | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131294](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131294) | Authorization Bypass through Custom Function Callbacks in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N) | 
| [CVE-2026-131295](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131295) | Improper Authorization in Playbook Execution in Splunk SOAR | [CWE-807](https://cwe.mitre.org/data/definitions/807.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131296](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131296) | Improper Access Control through Playbooks in Splunk SOAR | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L) | 
| [CVE-2026-131297](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131297) | Single Sign-On Authentication Bypass in Splunk SOAR | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | High | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131298](https://advisory.splunk.com/advisories/SVD-2026-1108#cve-2026-131298) | Improper Handling of Workbook Task Service-Level Agreements through the REST API in Splunk SOAR | [CWE-697](https://cwe.mitre.org/data/definitions/697.html) | Medium | [4.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N) | 

## CVE Details

### [CVE-2026-131240](https://www.cve.org/CVERecord?id=CVE-2026-131240): Denial of Service (DoS) through the Container REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user could cause Splunk SOAR to store excessive data in the Ingestion Status history through the Representational State Transfer (REST) API. When another user with permission to view system settings retrieves the Ingestion Status history, Splunk SOAR could use additional resources and return a larger response, which could degrade the availability of administrative monitoring. The vulnerability is possible because Splunk SOAR does not limit the amount of request data that it records for failed container creation before it stores the data in the Ingestion Status history. For more information see [REST Containers](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/6.4.0/container-endpoints/rest-containers), [REST Roles and Permissions](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/6.4.0/role-management-endpoints/rest-roles-and-permissions), and [View ingested container statistics using Ingestion Status](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.4.1/manage-your-splunk-soar-on-premises-system-health-and-performance/view-ingested-container-statistics-using-ingestion-status) in the Splunk documentation.

**Bug ID:** VULN-72014

**CWE:** [CWE-400](https://cwe.mitre.org/data/definitions/400.html)

**CVSSv3.1 Score:** 3.5, Low

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:N/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:N/A:L)

#### Mitigations and Workarounds

None

**Acknowledgments:** Gabriel Nitu, Splunk

### [CVE-2026-131241](https://www.cve.org/CVERecord?id=CVE-2026-131241): Authorization Bypass Through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with edit permission for containers on only a subset of container labels could modify container pins outside the container labels that the role permits. The vulnerability is possible because the Container Pin Representational State Transfer (REST) API does not enforce the container label authorization boundary when handling requests. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.4.1/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93067

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131242](https://www.cve.org/CVERecord?id=CVE-2026-131242): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `containers:view` permission could access automation history for containers outside the label or tenant scope assigned to the user. This could expose action parameters, connector result summaries, and other investigation and response activity. The vulnerability is possible because the Splunk SOAR Representational State Transfer (REST) API checks the permission to view containers but does not restrict automation history to containers within the label or tenant scope assigned to the user. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.7.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) and [Configure multiple tenants on your Splunk SOAR (On-premises) instance](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.7.0/configure-product-settings-for-your-splunk-soar-on-premises-instance/configure-multiple-tenants-on-your-splunk-soar-on-premises-instance) in the Splunk documentation.

**Bug ID:** VULN-93198

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131243](https://www.cve.org/CVERecord?id=CVE-2026-131243): Sensitive Information Disclosure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view an affected container could query the Representational State Transfer (REST) API for approvals to retrieve a live external prompt link belonging to another user. Using this link, the user could read the approval prompt without authentication and submit a response, potentially disrupting or altering the automated workflow governed by that approval. The vulnerability is possible because the REST API for approvals exposes the live external prompt link without verifying that the requester owns the approval.

**Bug ID:** VULN-94016

**CWE:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

**CVSSv3.1 Score:** 7.6, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131244](https://www.cve.org/CVERecord?id=CVE-2026-131244): Authorization Bypass through the Playbook API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to edit and run playbooks could modify a child playbook callback handle associated with another playbook run, which could alter the callback behavior of that run. The vulnerability exists because the Playbook API does not verify that callback-handle updates belong to the related parent and child playbook runs.

**Bug ID:** VULN-94688

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131245](https://www.cve.org/CVERecord?id=CVE-2026-131245): Information Disclosure through the Approval Detail REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with edit permission for the container label of a pending external prompt could obtain the external prompt link through the Representational State Transfer (REST) API and use the link to view and resolve the associated approval. The vulnerability is possible because the approval detail REST API includes the external prompt link in responses outside the assigned approval scope. For more information see [REST Approval](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/6.3.1/approval-endpoints/rest-approval), [REST External Prompt](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/7.1.0/external-prompt-endpoints/rest-external-prompt), and [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.5.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93932

**CWE:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131246](https://www.cve.org/CVERecord?id=CVE-2026-131246): Information Disclosure through REST API External Prompts in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with edit permission for the container label on a pending approval could read an external-prompt capability through an Approval details Representational State Transfer (REST) API response and use it to view the prompt content, change the pending approval decision, and modify its action parameters. The vulnerability is possible because an Approval details response exposes the external-prompt capability without checking approval ownership. For more information see [REST External Prompt](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/8.5.0/external-prompt-endpoints/rest-external-prompt) and [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.5.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93950

**CWE:** [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131247](https://www.cve.org/CVERecord?id=CVE-2026-131247): Authorization Bypass in the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated Splunk SOAR user with permission to edit and run playbooks could read action status and callback state from a playbook run outside the authorized container-label or tenant scope for that user. The vulnerability is possible because the playbook API uses mutable runtime context to identify a playbook run instead of preserving the server-provided context.

**Bug ID:** VULN-94798

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131248](https://www.cve.org/CVERecord?id=CVE-2026-131248): Improper Access Control through the Tenant REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` edit permission and restricted tenant access could modify settings for a tenant outside the role scope through the Representational State Transfer (REST) API. With this access, the user could expose confidential tenant environment values, alter tenant settings and automation behavior, or take the tenant out of operation. The vulnerability is possible because the Tenant REST API checks the `System Settings` edit permission but does not enforce the tenant restrictions for the role before it updates the selected tenant. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises), [Configure multiple tenants on your Splunk SOAR (On-premises) instance](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.7.0/configure-product-settings-for-your-splunk-soar-on-premises-instance/configure-multiple-tenants-on-your-splunk-soar-on-premises-instance), and [REST Tenant](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/8.5.0/multi-tenancy-endpoints/rest-tenant) in the Splunk documentation.

**Bug ID:** VULN-96231

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 7.2, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131249](https://www.cve.org/CVERecord?id=CVE-2026-131249): Improper Access Control in Child Playbook Callback Handles in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view, edit, and run playbooks and access to at least one container label could retrieve a callback handle from a playbook run outside the container-label scope granted to that account. The vulnerability is possible because Splunk SOAR does not verify that the requested callback handle belongs to the parent playbook run that launched the child playbook. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) and [Data access automation API](https://help.splunk.com/en/splunk-soar/soar-on-premises/python-playbook-api-reference/8.8.0/automation-api/data-access-automation-api) in the Splunk documentation.

**Bug ID:** VULN-94795

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131250](https://www.cve.org/CVERecord?id=CVE-2026-131250): Improper Access Control in the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to edit containers for an allowed label could forge the author attribution of container pins and access limited user details outside the expected authorization boundary. The Container Pin Representational State Transfer (REST) API does not prevent caller-provided author fields from reaching generic model binding, which lets the request reassign a pin author or query user-related data outside the expected authorization scope. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.3.1/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-98284

**CWE:** [CWE-915](https://cwe.mitre.org/data/definitions/915.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131251](https://www.cve.org/CVERecord?id=CVE-2026-131251): Authorization Bypass through Artifact Creation in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to view and modify containers with an allowed label could add artifacts to containers that the user cannot view or modify. The vulnerability is possible because the Representational State Transfer (REST) API artifact-creation workflow does not preserve the authorization boundary for the selected container.

**Bug ID:** VULN-96328

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131252](https://www.cve.org/CVERecord?id=CVE-2026-131252): Missing Authorization in Cross-Tenant Asset Management through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `Assets` edit or delete permission and access to one or more tenants could change or delete assets assigned to other tenants through the Representational State Transfer (REST) API. With this access, the user could redirect connector traffic and expose the credentials and operational data associated with an asset, or disrupt integrations and data ingestion for other tenants. The vulnerability is possible because Splunk SOAR verifies the `Assets` edit or delete permission but does not verify that the user can access every tenant assigned to the target asset before Splunk SOAR changes or deletes the asset. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises), [Configure multiple tenants on your Splunk SOAR (On-premises) instance](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.7.0/configure-product-settings-for-your-splunk-soar-on-premises-instance/configure-multiple-tenants-on-your-splunk-soar-on-premises-instance), [Add and configure apps and assets to provide actions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.6.0/manage-your-splunk-soar-on-premises-apps-and-assets/add-and-configure-apps-and-assets-to-provide-actions-in-splunk-soar-on-premises), and [Using the REST API reference for Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/8.5.0/using-the-splunk-soar-rest-api/using-the-rest-api-reference-for-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-96358

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131253](https://www.cve.org/CVERecord?id=CVE-2026-131253): Remote Code Execution (RCE) through the App Wizard in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the `Apps` edit, `Containers` edit, and `Playbooks` execute permissions could use the App Wizard to execute arbitrary code as the user account that runs Splunk SOAR. This could compromise the confidentiality, integrity, and availability of the Splunk SOAR instance. The vulnerability exists because the App Wizard does not validate user-supplied identifiers before incorporating them into generated connector code.

**Bug ID:** VULN-103662

**CWE:** [CWE-94](https://cwe.mitre.org/data/definitions/94.html)

**CVSSv3.1 Score:** 9.9, Critical

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131254](https://www.cve.org/CVERecord?id=CVE-2026-131254): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to create containers on one label could use the Representational State Transfer (REST) API to create a container with a parent relationship to a container that the user cannot access. This could let the user alter incident lineage across authorization boundaries and identify existing restricted containers. The vulnerability is possible because the REST API accepts a customer-supplied parent relationship when creating a container without authorizing access to the referenced container. For more information see [REST Containers](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference/8.6.0/container-endpoints/rest-containers) and [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-100592

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131255](https://www.cve.org/CVERecord?id=CVE-2026-131255): Privilege Escalation through REST API User Role Assignment in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an unauthenticated user could gain administrator privileges through a user account that receives an unintended role. A user that holds a role with permission to create or modify users and assign roles must assign the target account a role with a numeric name through the user-management Representational State Transfer (REST) API. The vulnerability is possible because the API resolves a numeric role name as a role identifier instead of preserving the requested role name.

**Bug ID:** VULN-96813

**CWE:** [CWE-706](https://cwe.mitre.org/data/definitions/706.html)

**CVSSv3.1 Score:** 7.5, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131256](https://www.cve.org/CVERecord?id=CVE-2026-131256): Remote Code Execution (RCE) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the `System Settings` edit permission could execute arbitrary code on the host that runs Splunk SOAR. The vulnerability is possible because the Representational State Transfer (REST) API accepts package references from untrusted sources and passes them to the dependency installer.

**Bug ID:** VULN-93389

**CWE:** [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

**CVSSv3.1 Score:** 7.2, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131257](https://www.cve.org/CVERecord?id=CVE-2026-131257): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to view and edit containers and at least one container label could set misleading user and app provenance on containers that the user creates and learn whether user IDs and installed app identifiers exist. The vulnerability is possible because the Representational State Transfer (REST) API accepts client-supplied values for server-managed container fields.

**Bug ID:** VULN-98406

**CWE:** [CWE-915](https://cwe.mitre.org/data/definitions/915.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131258](https://www.cve.org/CVERecord?id=CVE-2026-131258): Stored Cross-Site Scripting (XSS) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with edit permission for a container or workbook task could store attacker-controlled Hypertext Markup Language (HTML) in a note. When another user with view permission for the affected container and its notes opens the affected note in Mission Control, the note could run unauthorized JavaScript code in the browser of that user, expose data available through the authenticated session, and perform actions available through the authenticated session. The vulnerability is possible because Splunk SOAR does not neutralize active content in all notes before Mission Control renders them.

**Bug ID:** VULN-93220

**CWE:** [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

**CVSSv3.1 Score:** 8.7, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131259](https://www.cve.org/CVERecord?id=CVE-2026-131259): Improper Access Control through the Container REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to create and view containers for a label could use the Representational State Transfer (REST) API to create a container that references a workbook phase in a case the user cannot view, disclosing the phase name and creating an inconsistent phase association. The vulnerability exists because the Container REST API does not enforce the same case-scoped authorization when it accepts a workbook-phase reference during container creation.

**Bug ID:** VULN-102089

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131260](https://www.cve.org/CVERecord?id=CVE-2026-131260): Cross-Site Scripting (XSS) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with the `containers:edit` permission could import a container that includes a malicious Hypertext Markup Language (HTML) note. When another user views the imported note, Splunk SOAR could run unauthorized JavaScript in the browser of that user, exposing data and allowing actions available to that user. The vulnerability is possible because Splunk SOAR does not sanitize HTML note content during container import before it renders the content in Mission Control.

**Bug ID:** VULN-96788

**CWE:** [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

**CVSSv3.1 Score:** 8.7, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131261](https://www.cve.org/CVERecord?id=CVE-2026-131261): Remote Code Execution (RCE) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `Apps` edit permission could execute arbitrary code as the user account that runs Splunk SOAR by installing a malicious app. The vulnerability is possible because Splunk SOAR does not restrict app dependencies to validated binary packages before installing them.

**Bug ID:** VULN-93411

**CWE:** [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131262](https://www.cve.org/CVERecord?id=CVE-2026-131262): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user who can view and edit containers in at least one container label could create artifacts with parent relationships to containers and artifacts outside those labels. This could expose fields from restricted artifacts and modify incident lineage. The vulnerability is possible because Splunk SOAR does not verify access to the selected parent container and parent artifact when it creates an artifact.

**Bug ID:** VULN-100669

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131263](https://www.cve.org/CVERecord?id=CVE-2026-131263): Argument Injection during App Installation in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with only the `apps:edit` permission could install a connector app that causes Splunk SOAR to write attacker-controlled files outside the app directory. This could let the user modify files used by Splunk SOAR and execute arbitrary code as the user account that runs Splunk SOAR. The vulnerability is possible because Splunk SOAR constructs the dependency installation command from app-supplied metadata without preventing that metadata from changing its arguments. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) and [Add and configure apps and assets to provide actions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.6.0/manage-your-splunk-soar-on-premises-apps-and-assets/add-and-configure-apps-and-assets-to-provide-actions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93377

**CWE:** [CWE-88](https://cwe.mitre.org/data/definitions/88.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131264](https://www.cve.org/CVERecord?id=CVE-2026-131264): Information Exposure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` edit permission could cause Splunk SOAR to send the stored root credential for an external credential store to a host that the user controls. Depending on the configuration, the exposed credential could include an access token, application secret, account password, or client certificate. The vulnerability is possible because Splunk SOAR reuses the stored credential when the user changes the external credential store endpoint without supplying replacement credentials.

**Bug ID:** VULN-93428

**CWE:** [CWE-522](https://cwe.mitre.org/data/definitions/522.html)

**CVSSv3.1 Score:** 6.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131265](https://www.cve.org/CVERecord?id=CVE-2026-131265): Improper Access Control through the Ingestion Schedule View in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` view permission but not the `Assets` view permission could view asset names, asset identifiers, app names, tenant names, and ingestion schedule settings for polling assets in the ingestion schedule view. The vulnerability is possible because the ingestion schedule view does not verify the `Assets` view permission before it returns data derived from assets.

**Bug ID:** VULN-93393

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131266](https://www.cve.org/CVERecord?id=CVE-2026-131266): Information Disclosure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` edit permission could cause Splunk SOAR to send a stored Elasticsearch password to a host that the user controls. The vulnerability is possible because Splunk SOAR reuses a stored Elasticsearch password for a changed Search Settings endpoint without requiring a replacement password.

**Bug ID:** VULN-93392

**CWE:** [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

**CVSSv3.1 Score:** 7.7, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131267](https://www.cve.org/CVERecord?id=CVE-2026-131267): Sensitive Information Disclosure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` view and edit permissions could test a Lightweight Directory Access Protocol authentication provider and cause Splunk SOAR to send a stored directory service account bind password to a host that the user controls. The vulnerability is possible because Splunk SOAR reuses a stored directory service provider credential when an authentication test uses a different directory service connection destination.

**Bug ID:** VULN-93427

**CWE:** [CWE-522](https://cwe.mitre.org/data/definitions/522.html)

**CVSSv3.1 Score:** 6.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131268](https://www.cve.org/CVERecord?id=CVE-2026-131268): Remote Code Execution (RCE) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` edit permission could use a customer automation dependency to execute arbitrary code as the user account that runs Splunk SOAR. The vulnerability is possible because Splunk SOAR does not properly separate customer automation dependencies from trusted product code.

**Bug ID:** VULN-93380

**CWE:** [CWE-427](https://cwe.mitre.org/data/definitions/427.html)

**CVSSv3.1 Score:** 7.2, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131269](https://www.cve.org/CVERecord?id=CVE-2026-131269): Remote Code Execution (RCE) through Python Dependencies in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `Apps` edit permission could cause Splunk SOAR to execute arbitrary code on the host when the user validates an installed app. The vulnerability is possible because the app validation workflow does not isolate untrusted code from the trusted environment.

**Bug ID:** VULN-93404

**CWE:** [CWE-427](https://cwe.mitre.org/data/definitions/427.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131270](https://www.cve.org/CVERecord?id=CVE-2026-131270): Path Traversal through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with repository edit access could cause Splunk SOAR to write files outside the configured repository, which lets the user modify files that the user account running Splunk SOAR can write to. The vulnerability is possible because Splunk SOAR does not require source control repository paths to remain inside the configured repository.

**Bug ID:** VULN-93372

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131271](https://www.cve.org/CVERecord?id=CVE-2026-131271): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view and edit containers for one label could use a slash command through the Representational State Transfer (REST) API to access sensitive product data and credentials outside the authorized container scope. The vulnerability is possible because Splunk SOAR does not enforce authorization for related objects that slash commands access from an authorized artifact.

**Bug ID:** VULN-93357

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131272](https://www.cve.org/CVERecord?id=CVE-2026-131272): Path Traversal through the Automation Dependency Wheel REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `System Settings` edit permission could use the Automation Dependency Wheel Representational State Transfer (REST) API to write arbitrary files outside the intended directory, which could lead to arbitrary code execution. The vulnerability is possible because Splunk SOAR does not restrict uploaded automation dependency wheel filenames to the intended storage directory.

**Bug ID:** VULN-93373

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 7.2, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131273](https://www.cve.org/CVERecord?id=CVE-2026-131273): Improper Access Control through Splunk Web in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user who holds a role with permission to view system settings but not assets could view asset, app, and container-label metadata in Ingestion filters. The vulnerability is possible because Splunk SOAR returns Ingestion filter metadata without applying asset authorization and tenant restrictions. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.5.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93559

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131274](https://www.cve.org/CVERecord?id=CVE-2026-131274): Audit Trail Safeguards Bypass in Splunk SOAR REST API

#### Description

In Splunk SOAR versions below 8.8.0, a user with the `system_settings` permission could change event custom field definitions without the changes appearing in the audit trail, reducing forensic visibility and change accountability. The issue occurs because Splunk SOAR does not audit custom field definition changes.

**Bug ID:** VULN-100710

**CWE:** [CWE-778](https://cwe.mitre.org/data/definitions/778.html)

**CVSSv3.1 Score:** 2.7, Low

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131275](https://www.cve.org/CVERecord?id=CVE-2026-131275): Improper Input Validation of Timestamps through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with container edit permission could supply timestamps when creating containers and artifacts through the Representational State Transfer (REST) API. This could alter the timeline shown to analysts and cause configured data retention strategies to delete affected records earlier than intended. The vulnerability is possible because the REST API accepts client-supplied values for timestamps that Splunk SOAR uses to order records and apply data retention. The early deletion impact requires an applicable data retention strategy; the timeline impact does not. For more information see [Manage your PostgreSQL database with data retention strategies](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.4.0/manage-your-splunk-soar-on-premises-system-health-and-performance/manage-your-postgresql-database-with-data-retention-strategies) in the Splunk documentation.

**Bug ID:** VULN-96734

**CWE:** [CWE-915](https://cwe.mitre.org/data/definitions/915.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131276](https://www.cve.org/CVERecord?id=CVE-2026-131276): Improper Access Control in Splunk Web in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user that holds a role with the `System Settings` view permission but not the `Assets` view permission could view asset and tenant metadata in the ingestion history view. The ingestion history view does not restrict summary results to assets and tenants that the user can view.

**Bug ID:** VULN-93886

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131277](https://www.cve.org/CVERecord?id=CVE-2026-131277): Path Traversal through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with permission to edit playbooks and repositories could store a modified utility block in a playbook. If a user that holds a role with permission to edit playbook code later opens and saves the playbook in the Visual Playbook Editor, a subsequent playbook run could send a Representational State Transfer (REST) API delete request to a resource outside the intended data list. The user account that runs the playbook must have permission to delete the target resource. The vulnerability is possible because Splunk SOAR does not prevent a utility block from changing the intended REST API request path. For more information see [Data management automation API](https://help.splunk.com/en/splunk-soar/soar-on-premises/python-playbook-api-reference/6.3.0/automation-api/data-management-automation-api) and [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-93523

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 6.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131278](https://www.cve.org/CVERecord?id=CVE-2026-131278): Sensitive Information Disclosure through App Editor Debug Actions in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with local access to the affected host could obtain a live Splunk SOAR session token or decrypted asset configuration when another user starts an App Editor debug action. The vulnerability is possible because App Editor debug actions expose sensitive runtime information to other local users on the affected host.

**Bug ID:** VULN-94711

**CWE:** [CWE-214](https://cwe.mitre.org/data/definitions/214.html)

**CVSSv3.1 Score:** 7.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131279](https://www.cve.org/CVERecord?id=CVE-2026-131279): Improper Handling of Artifact Associations through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to edit artifacts could cause indicator correlation data to retain stale field associations, which can produce incorrect correlation results and event counts. The vulnerability is possible because Splunk SOAR does not remove stale indicator associations when an artifact changes.

**Bug ID:** VULN-100702

**CWE:** [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131280](https://www.cve.org/CVERecord?id=CVE-2026-131280): Sensitive Information Disclosure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user whose role grants `system_settings:view` but not `assets:view` could access asset and application inventory, tenant identifiers, connector run messages, and stored configuration snapshots through the ingestion status Representational State Transfer (REST) API. The vulnerability is possible because the ingestion status REST API checks the `system_settings:view` permission but does not enforce `assets:view` or tenant restrictions before it returns asset-derived ingestion records. For more information see [Manage roles and permissions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.3.1/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises), [Add and configure apps and assets to provide actions in Splunk SOAR (On-premises)](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.4.0/manage-your-splunk-soar-on-premises-apps-and-assets/add-and-configure-apps-and-assets-to-provide-actions-in-splunk-soar-on-premises), and [Configure multiple tenants on your Splunk SOAR (On-premises) instance](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/6.4.1/configure-product-settings-for-your-splunk-soar-on-premises-instance/configure-multiple-tenants-on-your-splunk-soar-on-premises-instance) in the Splunk documentation.

**Bug ID:** VULN-93726

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131281](https://www.cve.org/CVERecord?id=CVE-2026-131281): Insecure Default Audit Logging for Asset Approval and Effective User Changes through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with asset edit permission could change the approval requirements and effective automation user for an asset without Splunk SOAR recording field-level audit details for those changes. This could weaken investigation and accountability for changes to security-sensitive asset settings. The vulnerability is possible because Splunk SOAR does not include the asset approval voting fields and effective automation user field in its field-level audit coverage.

**Bug ID:** VULN-100707

**CWE:** [CWE-778](https://cwe.mitre.org/data/definitions/778.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131282](https://www.cve.org/CVERecord?id=CVE-2026-131282): Information Exposure through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user who holds the “Observer” Splunk SOAR role could access a password-reset credential in a diagnostic log bundle and reset the password for an active local account. The vulnerability is possible because Splunk SOAR does not redact password-reset email bodies before it logs communications between product processes.

**Bug ID:** VULN-96431

**CWE:** [CWE-532](https://cwe.mitre.org/data/definitions/532.html)

**CVSSv3.1 Score:** 8.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131283](https://www.cve.org/CVERecord?id=CVE-2026-131283): Improper Control of Playbook Conversion in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with playbook edit permission could cause later playbook conversions to include spurious branch conditions. This can prevent downstream blocks from running in affected converted playbooks. The vulnerability is possible because the playbook converter retains branch conditions from previous conversions.

**Bug ID:** VULN-101076

**CWE:** [CWE-665](https://cwe.mitre.org/data/definitions/665.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131284](https://www.cve.org/CVERecord?id=CVE-2026-131284): Improper Control of Artifact Workflow State through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to view and edit containers could import a container archive that makes artifacts appear to be part of a case or have notes when no corresponding case associations or notes exist. This could cause Representational State Transfer (REST) API clients and filters to use incorrect artifact state. The vulnerability is possible because container archive import accepts artifact workflow state from the archive instead of deriving that state from associated cases and notes. For more information see [Splunk SOAR REST API reference](https://help.splunk.com/en/splunk-soar/soar-on-premises/rest-api-reference) in the Splunk documentation.

**Bug ID:** VULN-101023

**CWE:** [CWE-915](https://cwe.mitre.org/data/definitions/915.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131285](https://www.cve.org/CVERecord?id=CVE-2026-131285): Authorization Bypass Through User-Controlled Key in Splunk SOAR Playbook Automation

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user who can edit and run playbooks could cause automation batches for other events to stop running. The vulnerability occurs because Splunk SOAR does not bind playbook API requests to the server-provided execution context.

**Bug ID:** VULN-94700

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131286](https://www.cve.org/CVERecord?id=CVE-2026-131286): Improper Access Control through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to author and run playbooks could view action data outside the authorized scope for that user and change the status and message of another playbook run. The vulnerability is possible because the playbook API does not verify that the requested playbook run is within the authorized scope of the authenticated user.

**Bug ID:** VULN-94689

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131287](https://www.cve.org/CVERecord?id=CVE-2026-131287): Remote Code Execution (RCE) through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user that holds a role with the `Playbooks` view, edit, execute, and delete permissions could cause existing cross-repository playbook references to run attacker-controlled playbook code. The vulnerability is possible because Splunk SOAR can bind existing cross-repository playbook references to a different source control repository when a deleted repository name is reused.

**Bug ID:** VULN-102282

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 9.6, Critical

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131288](https://www.cve.org/CVERecord?id=CVE-2026-131288): \[Flashpoint\] Privilege Escalation through HAProxy Cluster Operations in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with access to the configured load balancer account could replace a load balancer helper that Splunk SOAR later runs with root privileges during cluster lifecycle operations. If a Splunk SOAR administrator performs a cluster lifecycle operation, Splunk SOAR could execute arbitrary code with root privileges on the load balancer. The vulnerability is possible because Splunk SOAR does not verify the integrity or ownership of the load balancer helper before running it with root privileges.

**Bug ID:** VULN-94693

**CWE:** [CWE-269](https://cwe.mitre.org/data/definitions/269.html)

**CVSSv3.1 Score:** 7.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131289](https://www.cve.org/CVERecord?id=CVE-2026-131289): Improper Validation through Playbook Safe Mode in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user who holds a role that can edit and run playbooks in Splunk SOAR could cause Splunk SOAR to run non-read-only actions from a Safe Mode playbook, resulting in unauthorized state changes. The vulnerability is possible because Splunk SOAR does not verify that the playbook run context in an action request matches the context that the server provided.

**Bug ID:** VULN-94752

**CWE:** [CWE-345](https://cwe.mitre.org/data/definitions/345.html)

**CVSSv3.1 Score:** 3.1, Low

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131290](https://www.cve.org/CVERecord?id=CVE-2026-131290): Authorization Bypass in Splunk SOAR Playbook Status

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to edit and run playbooks could view child playbook status and loop-state metadata for playbook runs outside the authorized scope for that user. The vulnerability is possible because the playbook status API does not bind the requested run to the current execution context before it returns metadata.

**Bug ID:** VULN-94775

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131291](https://www.cve.org/CVERecord?id=CVE-2026-131291): Authorization Bypass through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a Splunk SOAR user who can edit and run playbooks for a permitted container label could associate action and callback state with a running playbook outside that container label. This could affect playbook automation for containers that the user cannot view. The vulnerability is possible because the Playbook Automation API accepts a supplied playbook run identifier without verifying that it is bound to the server-provided playbook execution context. The vulnerability requires a running playbook on a container label that the user cannot view.

**Bug ID:** VULN-95115

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131292](https://www.cve.org/CVERecord?id=CVE-2026-131292): Improper Authorization in Splunk SOAR Custom-Function Status

#### Description

In Splunk SOAR versions below 8.8.0, a user who can edit and run a playbook on a permitted label could cause Splunk SOAR to return custom-function status and callback state from another playbook run. The issue results from insufficient binding between a custom-function-status request and the playbook run that initiates it.

**Bug ID:** VULN-94805

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131293](https://www.cve.org/CVERecord?id=CVE-2026-131293): Improper Access Control in the Data Management Automation API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to edit and run playbooks could read or overwrite persisted data for playbook runs outside the authorized label, or ownership scope for that user. The affected data can include playbook inputs, prompt and block results, outputs, and secrets that playbooks save in run data. Overwriting the data could corrupt results that paused, scheduled, or parent playbook runs later use. The vulnerability is possible because the playbook automation APIs do not bind data operations to the active playbook run.

**Bug ID:** VULN-94849

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 8.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131294](https://www.cve.org/CVERecord?id=CVE-2026-131294): Authorization Bypass through Custom Function Callbacks in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user who can edit and run playbooks on a container label could associate a custom-function callback with another playbook run. The callback could modify the state of a container outside the authorized scope for that user. The vulnerability is possible because Splunk SOAR does not bind playbook API requests to the trusted playbook run and container context.

**Bug ID:** VULN-95182

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131295](https://www.cve.org/CVERecord?id=CVE-2026-131295): Improper Authorization in Playbook Execution in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with permission to create and run playbooks could start child playbooks on containers outside the authorized label, or repository scope for that user. This could expose container data and affect automation outside that scope. The vulnerability is possible because Splunk SOAR does not bind the identity used to authorize the child playbook run to the parent playbook execution context.

**Bug ID:** VULN-95185

**CWE:** [CWE-807](https://cwe.mitre.org/data/definitions/807.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131296](https://www.cve.org/CVERecord?id=CVE-2026-131296): Improper Access Control through Playbooks in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, a user with permission to author and run playbooks could add messages to a different playbook run log and cause that run to fail, including runs outside the labels that the user could access. The vulnerability is possible because Splunk SOAR does not verify that playbook API requests use the trusted runtime context for the current playbook run.

**Bug ID:** VULN-94782

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131297](https://www.cve.org/CVERecord?id=CVE-2026-131297): Single Sign-On Authentication Bypass in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an operator of a configured identity provider could authenticate as an existing user associated with another configured identity provider. If that account has the “Administrator” Splunk SOAR role, the operator could control the Splunk SOAR deployment. Splunk SOAR does not bind external user accounts to the identity provider that provisions them and authenticates accounts by username without verifying provider ownership. The vulnerability requires more than one configured external identity provider with distinct trust domains and a target username that an operator of a configured identity provider can authenticate through a different provider. For more information see [Configure single sign-on authentication](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.7.0/manage-your-splunk-soar-on-premises-users-and-accounts/configure-single-sign-on-authentication-for-splunk-soar-on-premises) and [Manage roles and permissions](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/8.8.0/manage-your-splunk-soar-on-premises-users-and-accounts/manage-roles-and-permissions-in-splunk-soar-on-premises) in the Splunk documentation.

**Bug ID:** VULN-94864

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 8.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

### [CVE-2026-131298](https://www.cve.org/CVERecord?id=CVE-2026-131298): Improper Handling of Workbook Task Service-Level Agreements through the REST API in Splunk SOAR

#### Description

In Splunk SOAR versions below 8.8.0, an authenticated user with edit permission on a workbook could configure a service-level agreement at only the workbook phase or task level. Splunk SOAR then flags the task as overdue immediately and does not display the configured deadline in the work queue. The incorrect deadline status could obscure genuine deadline breaches. The vulnerability is possible because Splunk SOAR treats an absent phase-level or task-level service-level agreement as immediately due when it compares the configured due times. For more information see [Define tasks using workbooks](https://help.splunk.com/en/splunk-soar/soar-on-premises/administer-soar-on-premises/7.0.0/configure-product-settings-for-your-splunk-soar-on-premises-instance/define-tasks-using-workbooks) in the Splunk documentation.

**Bug ID:** VULN-100693

**CWE:** [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

**CVSSv3.1 Score:** 4.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

#### Mitigations and Workarounds

None
