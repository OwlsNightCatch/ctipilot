---
title: Support Content Notification - Support Portal
url: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39625
hostname: broadcom.com
sitename: Support Portal
date: "2026-11-19"
fingerprint: "51e51adadd494e15"
language: en
pagetype: website
filedate: "2026-11-25"
---
# VMSA-2026-0010: Apache HTTP Server mod\_http2 heap corruption remote code execution vulnerability (CVE-2026-119618)

39625

19 November 2026

19 November 2026

OPEN

CRITICAL

9.8

Yes

CVE-2026-119618

| **Advisory ID:** | VMSA-2026-0010 | 
| **Advisory Severity:** | Critical | 
| **CVSSv3 Range:** | 9.8 | 
| **Synopsis:** | Apache HTTP Server mod\_http2 heap corruption remote code execution vulnerability (CVE-2026-119618) | 
| **Issue date:** | 2026-11-19 | 
| **Updated on:** | 2026-11-19 (Initial Advisory) | 
| **CVE(s)** | CVE-2026-119618 | 


## 1. Impacted Products

- VMware Cloud Foundation
- VMware Aria Operations
- VCF Operations HCX

## 2. Introduction

Apache HTTP Server mod\_http2 heap corruption remote code execution vulnerability. Workarounds are available to remediate this vulnerability in affected Broadcom products.

## 3. Apache HTTP Server mod\_http2 remote code execution vulnerability (CVE-2026-119618)

**Description:**Apache HTTP Server as used in VMware Cloud Foundation Operations, VMware Aria Operations, and VCF Operations HCX contains a remote code-execution vulnerability in mod\_http2. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to VMware Aria Operations or VCF Operations HCX may exploit this issue to execute arbitrary code.

**Resolution:**To mitigate CVE-2026-119618 apply the workarounds listed in the 'Workarounds' column of the 'Response Matrix' found below.

**Workarounds:**See the Response Matrix.

**Additional Documentation:**None

**Acknowledgments:**None.

**Notes:**None.

**Response Matrix:**

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation | VMware Cloud Foundation Operations | 9.x.x.x | Any | CVE-2026-119618 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Patch pending | [KB463005](https://knowledge.broadcom.com/external/article/463005) | None | 
| VMware Aria Operations | N/A | 8.18.x | Any | CVE-2026-119618 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Patch pending | [KB463005](https://knowledge.broadcom.com/external/article/463005) | None | 
| VMware Cloud Foundation | VMware Aria Operations | 5.x | Any | CVE-2026-119618 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Patch pending | [KB463005](https://knowledge.broadcom.com/external/article/463005) | None | 
| VMware Cloud Foundation | VCF Operations HCX | 9.1.x | Any | CVE-2026-119618 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Patch pending | [KB463022](https://knowledge.broadcom.com/external/article/463022) | None | 

## 4. References

**Mitre CVE Dictionary Links:**

[https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-119618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-119618)

**FIRST CVSSv3 Calculator:**CVE-2026-119618:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

## 5. Change Log:

**2026-11-19 VMSA-2026-0010**Initial security advisory.

## 6. Contact:

E-mail:

[\[email protected\]](https://support.broadcom.com/cdn-cgi/l/email-protection#46302b312734236836352f343206243429272225292b6825292b)

PGP key

[https://knowledge.broadcom.com/external/article/321551](https://knowledge.broadcom.com/external/article/321551)

VMware Security Advisories

[https://www.broadcom.com/support/vmware-security-advisories](https://www.broadcom.com/support/vmware-security-advisories)

VMware External Vulnerability Response and Remediation Policy

[https://www.broadcom.com/support/vmware-services/security-response](https://www.broadcom.com/support/vmware-services/security-response)

VMware Lifecycle Support Phases

[https://support.broadcom.com/group/ecx/productlifecycle](https://support.broadcom.com/group/ecx/productlifecycle)

VMware Security Blog

[https://blogs.vmware.com/security](https://blogs.vmware.com/security)

X

[https://x.com/VMwareSRC](https://x.com/VMwareSRC)


Copyright 2026 Broadcom. All rights reserved.
