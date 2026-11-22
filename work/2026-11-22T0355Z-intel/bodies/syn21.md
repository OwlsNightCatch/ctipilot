---
title: Synology_SA_26_21 | Synology Inc.
author: Synology Inc
url: https://www.synology.com/
hostname: synology.com
description: Synology Product Security Advisory
sitename: Synology Inc.
date: "2026-11-19"
fingerprint: "2820cb934f2d1c71"
---
# Synology-SA-26:21 DSM, BeeStation OS

Publish Time: UTC+8

Last Updated: UTC+8

- Severity
- Critical

- Status
- Ongoing

**Abstract**

Synology has released a security update to address a vulnerability:

- CVE-2026-120382 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

**Affected Products**

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| APM 2.0 | Not affected | N/A | 
| APM 1.2 | Not affected | N/A | 
| BeeStation OS 1.5 | Critical | OnGoing | 
| DSM 7.4 | Critical | Upgrade to 7.4.1-90080-2 or above. | 
| DSM 7.3 | Critical | Upgrade to 7.3.2-86009-6 or above. | 
| DSM 7.2.2 | Critical | OnGoing (Upgrading to 7.3.2-86009-6 or above is recommended). | 
| DSM 7.2.1 | Critical | OnGoing (Upgrading to 7.3.2-86009-6 or above is recommended). | 
| DSM 7.1 | Critical | OnGoing | 
| DSM Enterprise 1.0 | Not affected | N/A | 
| SRM 1.3 | Not affected | N/A | 
| SRM 1.2 | Not affected | N/A | 

**Mitigation**

Deactivate the OAuth Service package.

**Detail**

- CVE-2026-120382
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-88: Improper Neutralization of Argument Delimiters in a Command](https://cwe.mitre.org/data/definitions/88.html)
  - An improper neutralization of argument delimiters in a command vulnerability in the OAuth API in Synology DiskStation Manager (DSM) before 6.2.4-25556-9, 7.1.1-42962-10, 7.2.1-69057-14, 7.2.2-72806-11, 7.3.2-86009-6, and 7.4.1-90080-2 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

**Reference**

**Revision**

| Revision | Date | Description | 
|---|---|---|
| 1 | 2026-11-19 | Initial public release. | 
| 2 | 2026-11-20 | Update fix status for DSM 7.3 and DSM 7.4. |
