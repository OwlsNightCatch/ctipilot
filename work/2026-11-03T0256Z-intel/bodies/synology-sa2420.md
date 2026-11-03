# extract: served via trafilatura-direct
---
title: Synology_SA_24_20 | Synology Inc.
author: Synology Inc
url: https://www.synology.com/
hostname: synology.com
description: Synology Product Security Advisory
sitename: Synology Inc.
date: "2024-11-05"
fingerprint: bc8097d6dbfdcc50
---
# Synology-SA-24:20 DSM (PWN2OWN 2024)

Publish Time: UTC+8

Last Updated: UTC+8

- Severity
- Critical

- Status
- Resolved

**Abstract**

The vulnerability reported in ZDI-CAN-25403 allows remote attackers to execute arbitrary code.

The vulnerability reported in ZDI-CAN-25613 allows remote attackers to read specific files.

The vulnerability reported in ZDI-CAN-25617 allows adjacent man-in-the-middle attacker to write specific files.

Updates of DSM 7.2.1, DSM 7.1 and DSMUC 3.1 will be published within 30 days.

**Affected Products**

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| DSM 7.2.2 | Critical | Upgrade to 7.2.2-72806-1 or above. | 
| DSM 7.2.1 | Critical | Upgrade to 7.2.1-69057-6 or above. | 
| DSM 7.2 | Critical | Upgrade to 7.2-64570-4 or above. | 
| DSM 7.1 | Critical | Upgrade to 7.1.1-42962-7 or above. | 
| DSM 6.2 | Moderate | Upgrade to 6.2.4-25556-8 or above. | 

**Mitigation**

None

**Detail**

- CVE-2024-10441 
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - Improper encoding or escaping of output vulnerability in the system plugin daemon in Synology BeeStation OS (BSM) before 1.1-65374 and Synology DiskStation Manager (DSM) before 7.2-64570-4, 7.2.1-69057-6 and 7.2.2-72806-1 allows remote attackers to execute arbitrary code via unspecified vectors.
- CVE-2024-50629 
  - Severity: Moderate
  - CVSS3 Base Score: 5.3
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)
  - Improper encoding or escaping of output vulnerability in the webapi component in Synology BeeStation OS (BSM) before 1.1-65374 and Synology DiskStation Manager (DSM) before 7.1.1-42962-7, 7.2-64570-4, 7.2.1-69057-6 and 7.2.2-72806-1 allow remote attackers to read limited files via unspecified vectors.
- CVE-2024-10445 
  - Severity: Moderate
  - CVSS3 Base Score: 4.3
  - CVSS3 Vector: [CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N)
  - Improper certificate validation vulnerability in the update functionality in Synology BeeStation OS (BSM) before 1.1-65374 and Synology DiskStation Manager (DSM) before 6.2.4-25556-8, 7.1.1-42962-7, 7.2-64570-4, 7.2.1-69057-6 and 7.2.2-72806-1 allow remote attackers to write limited files via unspecified vectors.

**Acknowledgement**

- Pumpkin Chang (@u1f383) and Orange Tsai (@orange\_8361) from DEVCORE Research Team
- Ryan Emmons (@the\_emmons)
- Team Smoking Barrels

**Reference**

**Revision**

| Revision | Date | Description | 
|---|---|---|
| 1 | 2024-11-05 | Initial public release. | 
| 2 | 2024-11-12 | Update for DSM 7.2.1 is now available in Affected Products. | 
| 3 | 2024-11-14 | Update for DMSUC 3.1 is now available in Affected Products. | 
| 4 | 2024-11-26 | Update for DSM 7.1 is now available in Affected Products. | 
| 5 | 2024-12-05 | Added DSM 6.2 to Affected Products. | 
| 6 | 2024-12-05 | Update for DSM 6.2 is now available in Affected Products. | 
| 7 | 2025-03-19 | Disclosed vulnerability details. | 
| 8 | 2025-03-20 | Updated detail for vulnerability description. | 
| 9 | 2025-03-27 | Disclosed vulnerability details. |
