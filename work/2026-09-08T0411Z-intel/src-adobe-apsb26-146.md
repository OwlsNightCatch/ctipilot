# extract: served via trafilatura-direct
---
title: Adobe Security Bulletin
url: https://helpx.adobe.com/content/help/en/security/products/magento/apsb26-146.html
hostname: adobe.com
description: Security Updates Available for Adobe Commerce | APSB26-146
sitename: helpx.adobe.com
date: "2026-09-07"
---
Bulletin ID

Security update available for Adobe Commerce | APSB26-146


|  | Date Published | Priority | 
|---|---|---|
| APSB26-146 | September 7, 2026 | 1 | 

## Summary

Adobe has released a security update for Adobe Commerce and Magento Open Source. This update resolves a [critical](https://helpx.adobe.com/security/severity-ratings.html) vulnerability that could result in arbitrary code execution.

Adobe is aware of CVE-2026-75650 being exploited in the wild.

## Affected Versions

| **Product** | **Version** | **Platform** | 
|---|---|---|
| Adobe Commerce | 2.4.9-2026-aug and earlier 2.4.8-2026-aug and earlier 2.4.7-2026-aug and earlier 2.4.6-2026-aug and earlier 2.4.5-2026-aug and earlier 2.4.4-2026-aug and earlier | All | 
| Adobe Commerce B2B | 1.5.3-2026-aug and earlier 1.5.2-2026-aug and earlier 1.4.2-2026-aug and earlier 1.3.4-2026-aug and earlier 1.3.3-2026-aug and earlier | All | 
| Magento Open Source | 2.4.9-2026-aug and earlier 2.4.8-2026-aug and earlier 2.4.7-2026-aug and earlier 2.4.6-2026-aug and earlier | All | 


## Solution

Adobe categorizes these updates with the following [priority ratings](https://helpx.adobe.com/security/severity-ratings.html) and recommends users update their installation to the newest version.

| Product | Updated Version | Platform | Priority Rating | Installation Instructions | 
|---|---|---|---|---|
| Adobe Commerce and Magento Open Source | Hotfix for CVE-2026-75650 | All | 1 | [Release Notes for hotfix on CVE-2026-75650](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146) | 

Adobe categorizes these updates with the following [priority ratings](https://helpx.adobe.com/security/severity-ratings.html) and recommends users update their installation to the newest version.

## Vulnerability Details

| Vulnerability Category | Vulnerability Impact | Severity | [Authentication required to exploit?] | **CVSS base score** | [**CVSS vector**](https://www.first.org/cvss/v3.1/specification-document) | CVE number(s) | Notes | 
|---|---|---|---|---|---|---|---|
| Improper Neutralization of Special Elements Used in a Template Engine ([CWE-1336](https://cwe.mitre.org/data/definitions/1336.html) ) | Arbitrary code execution | Critical | No | 10.0 | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | CVE-2026-75650 |  | 

*Effective August 11, 2026, Adobe may assign a single CVE identifier to internally discovered vulnerabilities with the same severity rating and CWE category when a release includes systemic fixes.*

Authentication required to exploit: The vulnerability is (or is not) exploitable without credentials.

## Acknowledgements

Adobe would like to thank the following researchers for reporting these issues and working with Adobe to help protect our customers:

- 0x0.eth (0x0doteth) — CVE-2026-76200, CVE-2026-76201, CVE-2026-77109
- wohlie — CVE-2026-77108
- e0x1337 (e0x1337) — CVE-2026-76202

For more information, visit [https://helpx.adobe.com/security.html](https://helpx.adobe.com/security.html), or email PSIRT@adobe.com.
