---
title: Synology_SA_26_20 | Synology Inc.
author: Synology Inc
url: https://www.synology.com/
hostname: synology.com
description: Synology Product Security Advisory
sitename: Synology Inc.
date: "2026-11-19"
fingerprint: "3c20a3934ea58c54"
---
# Synology-SA-26:20 NGINX2Root

Publish Time: UTC+8

Last Updated: UTC+8

- Severity
- Critical

- Status
- Ongoing

**Abstract**

Synology has released a security update to address a vulnerability:

- CVE-2026-123007 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.

**Affected Products**

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| APM 2.0 | Critical | OnGoing | 
| APM 1.2 | Critical | OnGoing | 
| BeeStation OS 1.5 | Critical | OnGoing | 
| DSM 7.4 | Critical | Upgrade to 7.4.1-90080-2 or above. | 
| DSM 7.3 | Critical | Upgrade to 7.3.2-86009-6 or above. | 
| DSM 7.2.2 | Critical | OnGoing (Upgrading to 7.3.2-86009-6 or above is recommended). | 
| DSM 7.2.1 | Critical | OnGoing (Upgrading to 7.3.2-86009-6 or above is recommended). | 
| DSM 7.1 | Critical | OnGoing | 
| DSM Enterprise 1.0 | Critical | OnGoing | 
| SRM 1.3 | Not affected | N/A | 
| SRM 1.2 | Not affected | N/A | 

**Mitigation**

Disable HTTP/2 under Control Panel > Network > Connectivity.

**Detail**

- CVE-2026-123007
  - Severity: Important
  - CVSS3 Base Score: 8.1
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-787: Out-of-bounds Write](https://cwe.mitre.org/data/definitions/787.html)
  - This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed threshold, potentially resulting in a heap buffer overflow typically followed by an NGINX worker segmentation fault. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR. Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or potentially execute code remotely. There is no control plane exposure; this is a data plane issue only. Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.

**Reference**

[https://my.f5.com/manage/s/article/K000163926](https://my.f5.com/manage/s/article/K000163926)

**Revision**

| Revision | Date | Description | 
|---|---|---|
| 1 | 2026-11-19 | Initial public release. | 
| 2 | 2026-11-20 | Update fix status for DSM 7.3 and DSM 7.4. |
