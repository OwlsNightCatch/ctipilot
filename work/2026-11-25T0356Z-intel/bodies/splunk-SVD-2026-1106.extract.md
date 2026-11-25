---
title: Security Vulnerabilities in Splunk Enterprise Security - November 2026
url: https://advisory.splunk.com/advisories/SVD-2026-1106
hostname: splunk.com
description: Splunk addressed multiple vulnerabilities in Splunk Enterprise Security. See CVE Details for vulnerability-specific and product-specific information.
sitename: Splunk Vulnerability Disclosure
date: "2026-11-18"
fingerprint: ec83d59cc3fcc38b
language: en
image: https://advisory.splunk.com/assets/img/logo_color.jpg
filedate: "2026-11-25"
---

# Security Vulnerabilities in Splunk Enterprise Security - November 2026

**Advisory ID:** SVD-2026-1106

**Published:** 2026-11-18

**Highest CVSSv3.1 Score:** 9.1, Critical

**Last Updated:** 2026-11-18

## Description

Splunk addressed multiple vulnerabilities in Splunk Enterprise Security. See CVE Details for vulnerability-specific and product-specific information.

## Solutions

Upgrade Splunk Enterprise Security and Splunk App for PCI Compliance to version 8.7.0 or higher.

## Product Status

| Product | Base Version | Affected Version | Fix Version | 
|---|---|---|---|
| Splunk Enterprise Security | 8.7 | Below 8.7.0 | 8.7.0 | 
| Splunk App for PCI Compliance | 8.7 | Below 8.7.0 | 8.7.0 | 

## Vulnerabilities

| CVE | Summary | CWE | Severity | Score | 
|---|---|---|---|---|
| [CVE-2026-131198](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131198) | SPL Injection through the Mission Control REST API in Splunk Enterprise Security | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | High | [7.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131199](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131199) | SPL Injection through the Risk Event Timeline REST API in Splunk Enterprise Security | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131200](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131200) | Privilege Escalation through Threat Matching Searches in Splunk Enterprise Security | [CWE-863](https://cwe.mitre.org/data/definitions/863.html) | High | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131201](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131201) | Cross-Site Scripting (XSS) through Mission Control PDF Previews in Splunk Enterprise Security | [CWE-829](https://cwe.mitre.org/data/definitions/829.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131202](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131202) | Remote Code Execution (RCE) through REST API Path Traversal in Splunk Enterprise Security | [CWE-22](https://cwe.mitre.org/data/definitions/22.html) | Critical | [9.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H) | 
| [CVE-2026-131203](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131203) | Privilege Escalation through Search Macro Permissions in Splunk Enterprise Security | [CWE-732](https://cwe.mitre.org/data/definitions/732.html) | High | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131204](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131204) | Authorization Bypass through Mission Control in Splunk Enterprise Security | [CWE-639](https://cwe.mitre.org/data/definitions/639.html) | Medium | [4.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:L) | 
| [CVE-2026-131205](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131205) | SPL Injection through Asset Center Drilldowns in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131206](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131206) | Privilege Escalation through One-Time Data Migrations in Splunk Enterprise Security | [CWE-250](https://cwe.mitre.org/data/definitions/250.html) | Medium | [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131207](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131207) | Missing Authorization in the Detection Test Mode REST API in Splunk Enterprise Security | [CWE-862](https://cwe.mitre.org/data/definitions/862.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L) | 
| [CVE-2026-131208](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131208) | SPL Injection through Splunk Web Workbench Artifact Values in Splunk Enterprise Security | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131209](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131209) | SPL Injection through the REST API in Splunk Enterprise Security | [CWE-94](https://cwe.mitre.org/data/definitions/94.html) | High | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131210](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131210) | SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) | High | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131211](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131211) | SPL Injection through the Primary Functions Report in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [7.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131212](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131212) | Search Processing Language (SPL) Injection through Malware Activity Dashboard Drilldowns in the Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131213](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131213) | SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Medium | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131214](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131214) | SPL Injection through Legacy Investigation Timeline Search Actions in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131215](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131215) | SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | High | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131216](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131216) | Stored Cross-Site Scripting (XSS) through Legacy Investigation Workbench Panel Titles in Splunk Enterprise Security | [CWE-79](https://cwe.mitre.org/data/definitions/79.html) | Medium | [5.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131217](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131217) | SPL Injection through System Misconfigurations Report Drilldowns in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131218](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131218) | SPL Injection through the Mission Control REST API in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [8.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L) | 
| [CVE-2026-131219](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131219) | SPL Injection through the Network Traffic Activity Report in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Low | [3.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131220](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131220) | Search Processing Language (SPL) Injection through Dashboard Studio Drilldowns in Splunk Enterprise Security | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:L) | 
| [CVE-2026-131221](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131221) | SPL Injection through the Intrusion Detection and Prevention System Alert Activity Report in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131222](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131222) | Privilege Escalation through Asset and Identity Management in Splunk Enterprise Security | [CWE-99](https://cwe.mitre.org/data/definitions/99.html) | Medium | [6.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131223](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131223) | Search Processing Language (SPL) Injection through the Lookup Editor in Splunk Enterprise Security | [CWE-77](https://cwe.mitre.org/data/definitions/77.html) | Medium | [5.9](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131224](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131224) | SPL Injection through the Endpoint Changes Report in Splunk Enterprise Security | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Low | [3.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131225](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131225) | SPL Injection through the Malware Search Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131226](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131226) | Search Processing Language (SPL) Injection through Intrusion Search Dashboard Drilldowns in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [6.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131227](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131227) | Search Processing Language (SPL) Injection through the Domain Name System Search Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131228](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131228) | SPL Injection through the Search Audit Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131229](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131229) | SPL Injection through Splunk Web Vulnerability Search Dashboard Drilldowns in Splunk Enterprise Security | [CWE-74](https://cwe.mitre.org/data/definitions/74.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131230](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131230) | Search Processing Language Injection through Splunk Web in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.0](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L) | 
| [CVE-2026-131231](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131231) | Search Processing Language Injection through the Managed Lookups Audit Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131232](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131232) | SPL Injection through the Vulnerability Scan Details Splunk Web Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [6.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131233](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131233) | SPL Injection through Time Center Dashboard Drilldowns in Splunk Enterprise Security | [CWE-116](https://cwe.mitre.org/data/definitions/116.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131234](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131234) | SPL Injection through the Entity Analysis Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N) | 
| [CVE-2026-131235](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131235) | SPL Injection through the Credit Card Data Found Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [4.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N) | 
| [CVE-2026-131236](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131236) | SPL Injection through Splunk Web Workflow Actions in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [8.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H) | 
| [CVE-2026-131237](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131237) | Search Processing Language Injection through Weak Encrypted Communication Drilldowns in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [5.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N) | 
| [CVE-2026-131238](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131238) | Search Processing Language (SPL) Injection through the Secure Sockets Layer Search Dashboard in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | Medium | [6.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N) | 
| [CVE-2026-131239](https://advisory.splunk.com/advisories/SVD-2026-1106#cve-2026-131239) | SPL Injection through the System Update Status Report in Splunk Enterprise Security | [CWE-943](https://cwe.mitre.org/data/definitions/943.html) | High | [7.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N) | 

## CVE Details

### [CVE-2026-131198](https://www.cve.org/CVERecord?id=CVE-2026-131198): SPL Injection through the Mission Control REST API in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `mc_view_im_data` capability could cause the Mission Control incident mapping Representational State Transfer (REST) API to run arbitrary Search Processing Language (SPL) commands with elevated permissions. With this access, the user could expose all data in Splunk indexes and all stored credentials and modify protected indexes and lookup data. The vulnerability is possible because the Mission Control incident mapping REST API does not validate incident identifiers before including them in SPL searches. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) and [Overview of Mission Control in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/mission-control/overview-of-mission-control-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-81572

**CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

**CVSSv3.1 Score:** 7.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

**Acknowledgments:** David Kim

### [CVE-2026-131199](https://www.cve.org/CVERecord?id=CVE-2026-131199): SPL Injection through the Risk Event Timeline REST API in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `mc_investigation_read` capability could cause the Risk Event Timeline Representational State Transfer (REST) API to run arbitrary Search Processing Language (SPL) commands with elevated permissions. With this access, the user could expose stored credentials and modify indexes and lookup data available to those permissions. The vulnerability is possible because the affected REST API does not validate request values before including them in search macro arguments. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) and [Risk analysis](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/risk-analysis) in the Splunk documentation.

**Bug ID:** VULN-81573

**CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

None

**Acknowledgments:** David Kim

### [CVE-2026-131200](https://www.cve.org/CVERecord?id=CVE-2026-131200): Privilege Escalation through Threat Matching Searches in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_analyst” Splunk Enterprise Security role could create an attacker-controlled saved search. Threat intelligence lookup generation could later run the saved search with elevated permissions, which could let the user who created the saved search run arbitrary Search Processing Language (SPL) commands with those permissions. The vulnerability is possible because Splunk Enterprise Security does not restrict threat intelligence lookup generation to the intended saved searches. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and [Turn on threat matching searches in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.0/threat-intelligence/turn-on-threat-matching-searches-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-87022

**CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

**CVSSv3.1 Score:** 8.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131201](https://www.cve.org/CVERecord?id=CVE-2026-131201): Cross-Site Scripting (XSS) through Mission Control PDF Previews in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user with network-path interception capability could cause attacker-controlled JavaScript to run in the browser of a security analyst who previews a Portable Document Format (PDF) attachment in Mission Control. The JavaScript could expose data and perform actions available to the security analyst. The vulnerability is possible because Mission Control loads the PDF rendering worker from an external content delivery network. The vulnerability requires the unauthenticated user to intercept the network path to the external content delivery network and a security analyst to preview a PDF attachment in Mission Control. The unauthenticated user should not be able to exploit the vulnerability at will. For more information see [Collaborate on investigations in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/investigations/collaborate-on-investigations-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91123

**CWE:** [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/9.0/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.8-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131202](https://www.cve.org/CVERecord?id=CVE-2026-131202): Remote Code Execution (RCE) through REST API Path Traversal in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_admin” Splunk Enterprise Security role could execute arbitrary code on the search head as the user account running Splunk Enterprise by combining lookup file upload and Configuration Checker functionality. The vulnerability is possible because Splunk Enterprise Security does not restrict lookup upload file types or keep Configuration Checker module paths within the intended directory. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and [Create and manage lookups in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/managing-security-content/create-and-manage-lookups-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-84159

**CWE:** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)

**CVSSv3.1 Score:** 9.1, Critical

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

**Acknowledgments:** Klevis Luli, Flashpoint

### [CVE-2026-131203](https://www.cve.org/CVERecord?id=CVE-2026-131203): Privilege Escalation through Search Macro Permissions in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_analyst” Splunk Enterprise Security role could modify a search macro associated with risk exclusions. Scheduled Risk data model acceleration searches could later run attacker-controlled Search Processing Language (SPL) commands from that macro with elevated permissions. With this access, the user who modified the search macro could expose stored credentials and modify indexes or lookup data available to those searches. The vulnerability is possible because the Splunk Enterprise Security app metadata grants the “ess\_analyst” role write access to the risk exclusion search macro. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security), [Finding exclusions in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.3/user-and-entity-behavior-analytics/finding-exclusions-in-splunk-enterprise-security), and [Use search macros in searches](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.4/search-macros/use-search-macros-in-searches) in the Splunk documentation.

**Bug ID:** VULN-88784

**CWE:** [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

**CVSSv3.1 Score:** 8.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131204](https://www.cve.org/CVERecord?id=CVE-2026-131204): Authorization Bypass through Mission Control in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `mc_investigation_read` capability could overwrite Mission Control preference records for other users and remove saved filters and analyst queue settings from those records. The vulnerability is possible because the Mission Control user preferences Representational State Transfer (REST) API does not bind an update to the preference record that passes the authorization check. The attack requires the user to obtain a preference record identifier that the product does not normally expose to that user. The user should not be able to exploit the vulnerability at will. For more information see [Overview of Mission Control in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/mission-control/overview-of-mission-control-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91094

**CWE:** [CWE-639](https://cwe.mitre.org/data/definitions/639.html)

**CVSSv3.1 Score:** 4.2, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131205](https://www.cve.org/CVERecord?id=CVE-2026-131205): SPL Injection through Asset Center Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_user” Splunk Enterprise Security role could store attacker-controlled asset data in an asset source lookup. A user that holds a role with the `mc_assets_read` capability could later open the Asset Center dashboard and select that value in the `Asset Information` table. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of that user. With this access, the user who stored the asset data could expose or modify data available to the user who selected the value. The vulnerability is possible because Asset Center does not escape asset values before adding them to drilldown searches. The vulnerability requires Asset Center to process the asset data and another user to select the value. The user who stored the data should not be able to exploit the vulnerability at will. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security), [Add asset and identity data to Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/asset-and-identity-management/add-asset-and-identity-data-to-splunk-enterprise-security), and [Asset and identity dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/asset-and-identity-dashboards) in the Splunk documentation.

**Bug ID:** VULN-89865

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131206](https://www.cve.org/CVERecord?id=CVE-2026-131206): Privilege Escalation through One-Time Data Migrations in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `edit_modinput_data_migrator` capability could cause the data migration input to run arbitrary Search Processing Language (SPL) commands with elevated permissions. With this access, the user could read data outside the assigned role scope and write data to indexes and lookup tables. The vulnerability is possible because the data migration input does not restrict configured searches to product-supplied migration tasks before it runs them with elevated permissions. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91091

**CWE:** [CWE-250](https://cwe.mitre.org/data/definitions/250.html)

**CVSSv3.1 Score:** 5.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131207](https://www.cve.org/CVERecord?id=CVE-2026-131207): Missing Authorization in the Detection Test Mode REST API in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an authenticated user who does not hold the `edit_correlationsearches` capability could set `Status` to `Testing` for a versioned detection or clear that setting. This could affect the integrity and availability of detection testing. The vulnerability is possible because the Test Mode Representational State Transfer (REST) API does not require the `edit_correlationsearches` capability before it creates or deletes scheduled test copies of detections. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) and [Test detections on production data using Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/detections/test-detections-on-production-data-using-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91423

**CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131208](https://www.cve.org/CVERecord?id=CVE-2026-131208): SPL Injection through Splunk Web Workbench Artifact Values in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user could create and deliver a crafted Investigation Workbench link to an authenticated Splunk Enterprise Security user. If the authenticated user opens the link, Investigation Workbench could run arbitrary Search Processing Language (SPL) commands using the permissions of the authenticated user. With this access, the unauthenticated user could expose or modify data available to the authenticated user. The vulnerability is possible because Investigation Workbench does not safely neutralize special characters in artifact values before adding the values to searches. The vulnerability requires the attacker to phish the affected user by tricking them into initiating a request within their browser. The unauthenticated user should not be able to exploit the vulnerability at will. For more information see [Investigate a potential security incident on the investigation workbench in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-7/user-guide/7.3/investigations/investigate-a-potential-security-incident-on-the-investigation-workbench-in-splunk-enterprise-security) and [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-86611

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131209](https://www.cve.org/CVERecord?id=CVE-2026-131209): SPL Injection through the REST API in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `ueba_ers_execution_post` capability could cause the User and Entity Behavior Analytics (UEBA) Content App to run arbitrary Search Processing Language (SPL) commands with elevated permissions through an Entity Risk Score calculation. With this access, the user could expose stored credentials and other data outside the permissions assigned to that role. The vulnerability is possible because the UEBA Content App does not validate Entity Risk Score calculation values before including them in SPL searches. For more information see [Installing the UEBA Content App for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.5/user-and-entity-behavior-analytics/installing-the-ueba-content-app-for-splunk-enterprise-security), [Entity risk scoring in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.4/risk-based-alerting/entity-risk-scoring-in-splunk-enterprise-security), and [Roles and knowledge objects in UEBA for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.8/user-and-entity-behavior-analytics/ueba-content-app-for-on-premises/roles-and-knowledge-objects-in-ueba-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-86606

**CWE:** [CWE-94](https://cwe.mitre.org/data/definitions/94.html)

**CVSSv3.1 Score:** 8.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

Turn off or remove the UEBA Content App. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131210](https://www.cve.org/CVERecord?id=CVE-2026-131210): SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `ueba_finding_exclusion_edit` capability could create a finding exclusion rule that references an attacker-controlled lookup definition if the role also grants write access to globally shared lookup definitions, as the “ess\_analyst” Splunk Enterprise Security role does. The User and Entity Behavior Analytics (UEBA) Content App could later include the lookup name in a search and run arbitrary Search Processing Language (SPL) commands with elevated permissions. With this access, the user who created the finding exclusion rule could expose stored credentials and other data outside the permissions assigned to the “ess\_analyst” role. The vulnerability is possible because UEBA finding exclusion processing does not safely quote lookup names before including them in SPL searches. For more information see [Finding exclusions in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.3/user-and-entity-behavior-analytics/finding-exclusions-in-splunk-enterprise-security) and [Roles and knowledge objects in UEBA for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.8/user-and-entity-behavior-analytics/ueba-content-app-for-on-premises/roles-and-knowledge-objects-in-ueba-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-87004

**CWE:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

**CVSSv3.1 Score:** 8.1, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

None

### [CVE-2026-131211](https://www.cve.org/CVERecord?id=CVE-2026-131211): SPL Injection through the Primary Functions Report in Splunk Enterprise Security

#### Description

In Splunk App for Payment Card Industry Compliance versions below 8.7.0, a user who holds the “ess\_user” Splunk Enterprise Security role could add attacker-controlled values to lookup data used by the Primary Functions report. If another authenticated user later selects the value in the `Primary Function Summary` panel, the Splunk App for Payment Card Industry Compliance could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selected the value. With this access, the first user could expose or modify data available to the user who selected the value. The vulnerability is possible because the Primary Functions report does not safely escape report values before including them in drilldown searches. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and [Reports](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/user-manual/8.7/using-the-splunk-app-for-pci-compliance/reports) in the Splunk documentation.

**Bug ID:** VULN-91750

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 7.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for Payment Card Industry Compliance. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131212](https://www.cve.org/CVERecord?id=CVE-2026-131212): Search Processing Language (SPL) Injection through Malware Activity Dashboard Drilldowns in the Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in data that populates the Malware Activity report. Another user with access to the report could later click a related row. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who clicked the row. The commands could access data and perform actions available to that user. The vulnerability is possible because the Malware Activity report does not treat values from the Malware data model as literal search values when it builds drilldown searches. For more information see [Malware Activity](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/malware-activity) in the Splunk documentation.

**Bug ID:** VULN-89627

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.6, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for PCI Compliance. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131213](https://www.cve.org/CVERecord?id=CVE-2026-131213): SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_analyst” Splunk Enterprise Security role could store attacker-controlled data in finding exclusion rule metadata. Another authenticated user could later open the Finding Exclusion Rules page. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who opened the page. The first user could access data and perform actions available to the later user. The vulnerability is possible because Splunk Enterprise Security does not escape backslashes in finding exclusion rule metadata before adding the values to a page search. For more information see [Finding exclusions in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/user-and-entity-behavior-analytics/finding-exclusions-in-splunk-enterprise-security) and [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-87115

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 6.7, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131214](https://www.cve.org/CVERecord?id=CVE-2026-131214): SPL Injection through Legacy Investigation Timeline Search Actions in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `edit_timeline` capability could store attacker-controlled Search Processing Language (SPL) in a legacy investigation timeline entry. Another user that holds a role with the `manage_all_investigations` capability could later open the investigation and select `Run Search` from the timeline. Splunk Enterprise Security could then run the SPL stored by the first user using the permissions of the user who selected `Run Search`. The SPL stored by the first user could access data or perform actions available to the user who selected `Run Search`. The vulnerability is possible because Splunk Enterprise Security does not treat stored investigation search content as a literal search before building the Search page link. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.3/installation/capability-reference-for-splunk-enterprise-security) and [Add details to an investigation in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-7/user-guide/7.3/investigations/add-details-to-an-investigation-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-88679

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.8, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131215](https://www.cve.org/CVERecord?id=CVE-2026-131215): SPL Injection through Finding Exclusion Rules in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `ueba_finding_exclusion_edit` capability could store attacker-controlled values in a User and Entity Behavior Analytics (UEBA) finding exclusion rule. Splunk Enterprise Security could later run attacker-controlled Search Processing Language (SPL) commands from the rule with elevated permissions. With this access, the user could cause Splunk Enterprise Security to read stored credentials and modify lookups and knowledge objects. The vulnerability is possible because the UEBA finding exclusion workflow does not escape user-controlled rule values before using them in generated SPL. For more information see [Create a finding exclusion rule using UEBA configuration page](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/user-and-entity-behavior-analytics/finding-exclusions-in-splunk-enterprise-security/create-a-finding-exclusion-rule-using-ueba-configuration-page) and [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-87111

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 8.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

None

### [CVE-2026-131216](https://www.cve.org/CVERecord?id=CVE-2026-131216): Stored Cross-Site Scripting (XSS) through Legacy Investigation Workbench Panel Titles in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `manage_all_investigations` capability could store attacker-controlled script content in a legacy investigation workbench panel title. Another authenticated user could later open a legacy investigation workbench that renders the panel. The script could then run in the browser of the user who opened the workbench and expose data or actions available through Splunk Web to the user who opened the workbench. The vulnerability is possible because Splunk Enterprise Security does not escape legacy investigation workbench panel titles before rendering them in Splunk Web. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) and [Review and finish existing legacy investigations in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.4/investigations/review-and-finish-existing-legacy-investigations-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-88780

**CWE:** [CWE-79](https://cwe.mitre.org/data/definitions/79.html)

**CVSSv3.1 Score:** 5.7, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131217](https://www.cve.org/CVERecord?id=CVE-2026-131217): SPL Injection through System Misconfigurations Report Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in data that populates the System Misconfigurations report. Another user with access to the report could later select a related row. The System Misconfigurations report could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selected the row. The commands could access or modify data available to the user who selected the row. The vulnerability is possible because the System Misconfigurations report does not treat values from the Vulnerabilities data model as literal search values when it builds drilldown searches. For more information see [System Misconfigurations](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/system-misconfigurations) and [Configure users and roles](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-the-app/configure-users-and-roles) in the Splunk documentation.

**Bug ID:** VULN-89633

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.6, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.8-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131218](https://www.cve.org/CVERecord?id=CVE-2026-131218): SPL Injection through the Mission Control REST API in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `mc_investigation_read` capability could inject arbitrary Search Processing Language (SPL) into Mission Control dashboard search requests. Mission Control could then run the injected SPL with elevated permissions. With this access, the user could cause Mission Control to read stored credentials and write data to indexes and lookups. The vulnerability is possible because Mission Control does not validate reserved search filters before adding them to dashboard searches. For more information see [Overview of Mission Control in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.1/mission-control/overview-of-mission-control-in-splunk-enterprise-security) and [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.2/installation/capability-reference-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-89701

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 8.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131219](https://www.cve.org/CVERecord?id=CVE-2026-131219): SPL Injection through the Network Traffic Activity Report in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in network traffic data. Another user who holds the “pci\_user” role could later click the corresponding row in the Traffic Detail panel of the Network Traffic Activity report. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who clicked the row. The commands could access data and perform actions available to that user. The vulnerability is possible because the Network Traffic Activity report does not treat network traffic values as literal search values when it builds the Traffic Detail drilldown search. For more information see [Network Traffic Activity](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/network-traffic-activity) and [Configure users and roles](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-the-app/configure-users-and-roles) in the Splunk documentation.

**Bug ID:** VULN-89631

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 3.7, Low

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for PCI Compliance. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

**Acknowledgments:** Flashpoint Research Team

### [CVE-2026-131220](https://www.cve.org/CVERecord?id=CVE-2026-131220): Search Processing Language (SPL) Injection through Dashboard Studio Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who can influence event values that populate an affected data model based on the Common Information Model could cause attacker-controlled values to appear in an affected Dashboard Studio view. Another authenticated user could later click a corresponding row in that view. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who clicked the row. The commands could access or modify some data available to the user who clicked the row. The vulnerability is possible because affected Dashboard Studio drilldowns do not safely quote data model values before including them in searches. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and [Create a dashboard in Dashboard Studio](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/dashboard-studio/10.2/create-a-dashboard-in-dashboard-studio/create-a-dashboard-in-dashboard-studio) in the Splunk documentation.

**Bug ID:** VULN-89639

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:L)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.8-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131221](https://www.cve.org/CVERecord?id=CVE-2026-131221): SPL Injection through the Intrusion Detection and Prevention System Alert Activity Report in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in intrusion detection data. Another user who holds the “pci\_user” role could later select the corresponding row in the Intrusion Detection and Prevention System Alert Activity Details panel. The report could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selected the row. The commands could access data and perform actions available to the user who selected the row. The vulnerability is possible because the Intrusion Detection and Prevention System Alert Activity report does not treat intrusion detection values as literal search values when it builds the details drilldown search. For more information see [Reports](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/user-manual/8.7/using-the-splunk-app-for-pci-compliance/reports) and [Configure users and roles](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-the-app/configure-users-and-roles) in the Splunk documentation.

**Bug ID:** VULN-89630

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.6, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the [Splunk App for PCI Compliance](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/introduction/about-splunk-app-for-pci-compliance). For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131222](https://www.cve.org/CVERecord?id=CVE-2026-131222): Privilege Escalation through Asset and Identity Management in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `edit_modinput_identity_manager` capability could use Asset and Identity Management to modify protected saved searches and role capabilities. With this access, the user could obtain full administrator access to the Splunk platform. The vulnerability is possible because Asset and Identity Management does not validate the app namespace before sending a Representational State Transfer (REST) API request with a system authentication token. For more information see [Capability reference for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/capability-reference-for-splunk-enterprise-security) and [Add asset and identity data to Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/asset-and-identity-management/add-asset-and-identity-data-to-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91089

**CWE:** [CWE-99](https://cwe.mitre.org/data/definitions/99.html)

**CVSSv3.1 Score:** 6.5, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131223](https://www.cve.org/CVERecord?id=CVE-2026-131223): Search Processing Language (SPL) Injection through the Lookup Editor in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user could trick an authenticated user into opening a link that the unauthenticated user creates. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the authenticated user. The commands could access data and perform actions available to that user. The vulnerability is possible because the Lookup Editor does not validate lookup identifiers from URL parameters before adding them to searches. The vulnerability requires the attacker to phish the user by tricking them into opening a link that the attacker creates. The unauthenticated user should not be able to exploit the vulnerability at will. For more information see [Create and manage lookups in Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.0/managing-security-content/create-and-manage-lookups-in-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91100

**CWE:** [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

**CVSSv3.1 Score:** 5.9, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131224](https://www.cve.org/CVERecord?id=CVE-2026-131224): SPL Injection through the Endpoint Changes Report in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in data that populates the Endpoint Changes report. Another user who holds the “pci\_analyst” role could later click a corresponding table row. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who clicked the row. The commands could access or modify data available to that user. The vulnerability is possible because the Endpoint Changes report does not treat dynamic report values as literal search values when it builds table-row drilldown searches. For more information see [Reports](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/user-manual/8.7/using-the-splunk-app-for-pci-compliance/reports) and [Configure users and roles](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-the-app/configure-users-and-roles) in the Splunk documentation.

**Bug ID:** VULN-91103

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 3.7, Low

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for PCI Compliance. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131225](https://www.cve.org/CVERecord?id=CVE-2026-131225): SPL Injection through the Malware Search Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in the Malware data model. Another authenticated user with access to the Malware Search dashboard could later select a table row containing those values. Splunk Enterprise Security could then run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selected the row. The commands could expose data available to the user who selected the row and add attacker-controlled records to an index. The vulnerability is possible because the Malware Search dashboard does not safely quote row values before adding them to drilldown searches. For more information see [Endpoint dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.4/analytics/endpoint-dashboards) and [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) in the Splunk documentation.

**Bug ID:** VULN-91106

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131226](https://www.cve.org/CVERecord?id=CVE-2026-131226): Search Processing Language (SPL) Injection through Intrusion Search Dashboard Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in Intrusion Detection data. If another user who can access the Intrusion Search dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify data available to the user who selects the row. The vulnerability is possible because the Intrusion Search dashboard encodes data-model field values for the drilldown link but does not escape the values as SPL search literals before inserting the values into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Network dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/network-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91109

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 6.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131227](https://www.cve.org/CVERecord?id=CVE-2026-131227): Search Processing Language (SPL) Injection through the Domain Name System Search Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in Network Resolution data. If another user who can access the Domain Name System Search dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify some data available to the user who selects the row. The vulnerability is possible because the Domain Name System Search dashboard encodes data-model field values for the drilldown link but does not escape the values as SPL search literals before inserting the values into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Protocol intelligence dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/protocol-intelligence-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91110

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 6.3, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131228](https://www.cve.org/CVERecord?id=CVE-2026-131228): SPL Injection through the Search Audit Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user who holds the “ess\_user” Splunk Enterprise Security role could run a search that causes attacker-controlled Search Processing Language (SPL) text to appear in the Search Audit dashboard. If another user who can access the dashboard selects the affected search, Splunk Enterprise Security could run attacker-controlled SPL commands using the permissions of the user who selects the search. The user who runs the first search could then access sensitive data and modify some data available to the user who selects the affected search. The vulnerability is possible because the Search Audit dashboard does not safely escape logged search text before inserting it into drilldown searches. For more information see [Users and roles for Splunk Enterprise Security](https://help.splunk.com/en/splunk-enterprise-security-8/install/8.7/installation/users-and-roles-for-splunk-enterprise-security) and [Audit dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/audit-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91113

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131229](https://www.cve.org/CVERecord?id=CVE-2026-131229): SPL Injection through Splunk Web Vulnerability Search Dashboard Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in vulnerability data. If another user who can access the Vulnerability Search dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify some data available to the user who selects the row. The vulnerability is possible because the Vulnerability Search dashboard encodes data-model field values for the drilldown link but does not escape the values as SPL search literals before inserting the values into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Network dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/network-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91111

**CWE:** [CWE-74](https://cwe.mitre.org/data/definitions/74.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131230](https://www.cve.org/CVERecord?id=CVE-2026-131230): Search Processing Language Injection through Splunk Web in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user could trick a user that holds a role with the `ueba_can_view_ui` capability into opening a link that the unauthenticated user creates for the User and Entity Behavior Analytics (UEBA) Overview dashboard. When the user opens the link, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who opens the link. The commands could expose or modify some data available to the user who opens the link and partially disrupt search processing. The vulnerability is possible because the User and Entity Behavior Analytics Overview dashboard does not escape dashboard filter values from the link before substituting the values into SPL searches. The vulnerability requires the attacker to phish the user by tricking them into opening a link that the attacker creates. The unauthenticated user should not be able to exploit the vulnerability at will. For more information see [UEBA dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.8/analytics/ueba-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91117

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.0, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L)

#### Mitigations and Workarounds

Turn off or remove the User and Entity Behavior Analytics app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131231](https://www.cve.org/CVERecord?id=CVE-2026-131231): Search Processing Language Injection through the Managed Lookups Audit Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in managed-lookup audit data. If another user who can access the Managed Lookups Audit dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify some data available to the user who selects the row. The vulnerability is possible because the Managed Lookups Audit dashboard does not safely escape audit data before inserting it into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Audit dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/audit-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91112

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131232](https://www.cve.org/CVERecord?id=CVE-2026-131232): SPL Injection through the Vulnerability Scan Details Splunk Web Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in vulnerability scan data. If another user who can access the Vulnerability Scan Details dashboard selects an affected value, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the value. The user who stores the values could then access sensitive data and modify data available to the user who selects the affected value. The vulnerability is possible because the Vulnerability Scan Details dashboard does not validate destination values before inserting them into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Vulnerability Scan Details](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/vulnerability-scan-details) in the Splunk documentation.

**Bug ID:** VULN-91124

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 6.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131233](https://www.cve.org/CVERecord?id=CVE-2026-131233): SPL Injection through Time Center Dashboard Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in endpoint summary data. If another user who can access the Time Center dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify some data available to the user who selects the row. The vulnerability is possible because the Time Center dashboard does not safely escape endpoint summary values before inserting them into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Endpoint dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/endpoint-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91121

**CWE:** [CWE-116](https://cwe.mitre.org/data/definitions/116.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configuration-file-reference/10.4.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131234](https://www.cve.org/CVERecord?id=CVE-2026-131234): SPL Injection through the Entity Analysis Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user could create and deliver an Entity Analysis dashboard link to a Splunk Enterprise Security user. If the Splunk Enterprise Security user opens the link, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the Splunk Enterprise Security user. The commands could expose or modify some data available to the Splunk Enterprise Security user. The vulnerability is possible because the Entity Analysis dashboard inserts entity values from a link that an unauthenticated user creates into SPL searches without safely escaping the values. The vulnerability requires the attacker to phish the affected user by tricking them into initiating a request within their browser. The unauthenticated user should not be able to exploit the vulnerability at will. For more information see [Entity analysis dashboard](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/exposure-analytics-and-ueba/entity-analysis-dashboard) in the Splunk documentation.

**Bug ID:** VULN-91118

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.2, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.2/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/configuration-file-reference/10.2.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131235](https://www.cve.org/CVERecord?id=CVE-2026-131235): SPL Injection through the Credit Card Data Found Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in data used by the Credit Card Data Found dashboard. If another user who can access the dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data available to the user who selects the row. The vulnerability is possible because the Credit Card Data Found dashboard does not validate source and destination values before inserting them into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Credit Card Data Found](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/credit-card-data-found) in the Splunk documentation.

**Bug ID:** VULN-91126

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 4.8, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:N/A:N)

#### Mitigations and Workarounds

Turn off or remove the [Splunk App for PCI Compliance](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/credit-card-data-found). For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131236](https://www.cve.org/CVERecord?id=CVE-2026-131236): SPL Injection through Splunk Web Workflow Actions in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, an unauthenticated user who can influence indexed event data could store attacker-controlled values in event fields. If another authenticated user who reviews the event selects the View Adaptive Response Invocations or View Adaptive Response Results workflow action from Event Actions, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the action. The unauthenticated user could then access or modify sensitive data and disrupt services available to the user who selects the action. The vulnerability is possible because the affected Common Information Model workflow actions insert the `orig_sid` and `orig_rid` event-field values directly into searches without safely validating or quoting the values. For more information see [About workflow actions in Splunk Web](https://help.splunk.com/en/splunk-enterprise/manage-knowledge-objects/knowledge-management-manual/10.2/workflow-actions/about-workflow-actions-in-splunk-web) in the Splunk documentation.

**Bug ID:** VULN-91420

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 8.8, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131237](https://www.cve.org/CVERecord?id=CVE-2026-131237): Search Processing Language Injection through Weak Encrypted Communication Drilldowns in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in data used by the Weak Encrypted Communication report. If another user who can access the report selects an affected drilldown, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the drilldown. The user who stores the values could then access sensitive data and modify some data available to the user who selects the drilldown. The vulnerability is possible because the Weak Encrypted Communication report does not validate source, destination, and Secure Sockets Layer version values before inserting them into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Weak Encrypted Communication](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/weak-encrypted-communication) in the Splunk documentation.

**Bug ID:** VULN-91127

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 5.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk App for Payment Card Industry Compliance. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.

### [CVE-2026-131238](https://www.cve.org/CVERecord?id=CVE-2026-131238): Search Processing Language (SPL) Injection through the Secure Sockets Layer Search Dashboard in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled certificate values. If another user who can access the Secure Sockets Layer Search dashboard selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify data available to the user who selects the row. The vulnerability is possible because the Secure Sockets Layer Search dashboard encodes certificate values for the drilldown link but does not escape the values as SPL search literals before inserting the values into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [Protocol intelligence dashboards](https://help.splunk.com/en/splunk-enterprise-security-8/user-guide/8.7/analytics/protocol-intelligence-dashboards) in the Splunk documentation.

**Bug ID:** VULN-91107

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 6.4, Medium

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

The vulnerability affects instances with Splunk Web turned on. Turning Splunk Web off is a possible workaround. See [Disable unnecessary Splunk Enterprise components](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/install-splunk-enterprise-securely/disable-unnecessary-splunk-enterprise-components) and the [web.conf](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.6/configuration-file-reference/10.6.0-configuration-file-reference/web.conf) configuration specification file for more information on turning off Splunk Web.

### [CVE-2026-131239](https://www.cve.org/CVERecord?id=CVE-2026-131239): SPL Injection through the System Update Status Report in Splunk Enterprise Security

#### Description

In Splunk Enterprise Security versions below 8.7.0, a user that holds a role with the `run_collect` capability could store attacker-controlled values in Updates data. If another user who can access the System Update Status report selects an affected row, Splunk Enterprise Security could run attacker-controlled Search Processing Language (SPL) commands using the permissions of the user who selects the row. The user who stores the values could then access sensitive data and modify data available to the user who selects the row. The vulnerability is possible because the System Update Status report does not validate destination, signature, and vendor-product values before inserting them into drilldown searches. For more information see [Define roles on the Splunk platform with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities) and [System Update Status](https://help.splunk.com/en/splunk-enterprise-security-8/splunk-app-for-pci-compliance/installation-and-configuration-manual/8.7/configure-reports/system-update-status) in the Splunk documentation.

**Bug ID:** VULN-91128

**CWE:** [CWE-943](https://cwe.mitre.org/data/definitions/943.html)

**CVSSv3.1 Score:** 7.3, High

**CVSSv3.1 Vector:** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N)

#### Mitigations and Workarounds

Turn off or remove the Splunk Enterprise Security app. For more information see [Manage app and add-on objects](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.2/meet-splunk-apps/manage-app-and-add-on-objects) in the Splunk documentation.
