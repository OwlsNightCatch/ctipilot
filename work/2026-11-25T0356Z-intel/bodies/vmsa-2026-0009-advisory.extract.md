---
title: Support Content Notification - Support Portal
url: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495
hostname: broadcom.com
sitename: Support Portal
date: "2026-11-19"
fingerprint: f0a7bfd699efce1f
language: en
pagetype: website
filedate: "2026-11-25"
---
# VMSA-2026-0009: VMware vCenter, Tools, and SDDC Manager updates address multiple vulnerabilities (CVE-2026-123890, CVE-2026-123891, CVE-2026-123892, CVE-2026-123893, CVE-2026-123894)

39495

20 November 2026

19 November 2026

OPEN

CRITICAL

9.8

None

CVE-2026-123890, CVE-2026-123891, CVE-2026-123892, CVE-2026-123893, CVE-2026-123894

| **Advisory ID:** | VMSA-2026-0009.1 | 
| **Advisory Severity:** | Critical | 
| **CVSSv3 Range:** | 6.7-9.8 | 
| **Synopsis:** | VMware vCenter, Tools, and SDDC Manager updates address multiple vulnerabilities (CVE-2026-123890, CVE-2026-123891, CVE-2026-123892, CVE-2026-123893, CVE-2026-123894) | 
| **Issue date:** | 2026-11-19 | 
| **Updated on:** | 2026-11-20 | 
| **CVE(s)** | CVE-2026-123890, CVE-2026-123891, CVE-2026-123892, CVE-2026-123893, CVE-2026-123894 | 


## 1. Impacted Products

- VMware vCenter
- VMware Cloud Foundation
- VMware vSphere Foundation
- VMware Tools
- VMware Telco Cloud Platform
- VMware Telco Cloud Infrastructure

## 2. Introduction

Multiple vulnerabilities in VMware vCenter, Tools, and SDDC Manager were privately reported to Broadcom. Updates are available to remediate these vulnerabilities in affected Broadcom products.

## 3a. vCenter authentication-bypass vulnerability (CVE-2026-123890)

**Description:** VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system.

**Resolution:** To remediate CVE-2026-123890 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0009-qna](https://brcm.tech/vmsa-2026-0009-qna)

**Acknowledgments:** Broadcom would like to thank Mandiant for reporting this issue to us.

**Notes:**None

**Response Matrix:**

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.1.x.x | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [9.1.1.0200](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-1-2&appid=vcf-9-1&language=en&format=rendered) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.0.x.x | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [9.0.2.0200](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-0-2-0-2&appid=vcf-9-0&language=en&format=rendered) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware vCenter | N/A | 8.0 | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [8.0 U3m](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html)  | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware vCenter | N/A | 7.0 | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Contact Broadcom Support if you have extended support contract. | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation | vCenter | 5.x | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [5.2.5](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-525-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | vCenter | 3.0, 4.x, 5.0.x, 5.1.x, 5.2 | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [KB463116](https://knowledge.broadcom.com/external/article/463116) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Telco Cloud Infrastructure | vCenter | 3.0 | Any | CVE-2026-123890 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [KB463116](https://knowledge.broadcom.com/external/article/463116) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 

## 

3b. SDDC Manager SQL-injection vulnerability (CVE-2026-123891)

**Description:**SDDC Manager contains an SQL-injection vulnerability due to improper sanitization of user-supplied input. Broadcom has evaluated the severity of this issue to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N).

**Known Attack Vectors:**A malicious authenticated actor may exploit this issue by using a specially crafted SQL query to perform unauthorised read/write operations in the database.

**Resolution:** To remediate CVE-2026-123891 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0009-qna](https://brcm.tech/vmsa-2026-0009-qna)

**Acknowledgments:** Broadcom would like to thank Arnoldas Radisauskas of NATO NCSC

*for reporting this issue to us.*

**Notes:**\[1\] Please note that patches are cumulative, meaning the current version includes all previously released fixes. While CVE-2026-123891 and CVE-2026-123892 were initially addressed in version 9.1.0.0, and CVE-2026-123893 was addressed in 9.1.1.0, version 9.1.1.0200 is the latest available version and contains the fixes for all of these CVEs.

## 3c. SDDC Manager authenticated command-injection vulnerability(CVE-2026-123892)

**Description:**SDDC Manager contains an authenticated command-injection vulnerability due to improper sanitization of user-supplied input.  Broadcom has evaluated the severity of this issue to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious authenticated actor may exploit this issue to execute arbitrary commands on the appliance.

**Resolution:** To remediate CVE-2026-123892 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0009-qna](https://brcm.tech/vmsa-2026-0009-qna)

**Acknowledgments:** Broadcom would like to thank Arnoldas Radisauskas of NATO NCSC

*for reporting this issue to us.*

**Notes:**\[1\] Please note that patches are cumulative, meaning the current version includes all previously released fixes. While CVE-2026-123891 and CVE-2026-123892 were initially addressed in version 9.1.0.0, and CVE-2026-123893 was addressed in 9.1.1.0, version 9.1.1.0200 is the latest available version and contains the fixes for all of these CVEs.

## 3d. SDDC Manager local privilege-escalation vulnerability(CVE-2026-123893)

**Description:** SDDC Manager contains a local privilege-escalation vulnerability. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with administrative privileges on SDDC Manager may exploit this issue to elevate privileges to root.

**Resolution:** To remediate CVE-2026-123893 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0009-qna](https://brcm.tech/vmsa-2026-0009-qna)

**Acknowledgments:** Broadcom would like to thank Arnoldas Radisauskas of NATO NCSC

*for reporting this issue to us.*

**Notes:**\[1\] Please note that patches are cumulative, meaning the current version includes all previously released fixes. While CVE-2026-123891 and CVE-2026-123892 were initially addressed in version 9.1.0.0, and CVE-2026-123893 was addressed in 9.1.1.0, version 9.1.1.0200 is the latest available version and contains the fixes for all of these CVEs.

**Response Matrix 3b, 3c, 3d:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation | SDDC Manager | 9.1.x.x | Any | CVE-2026-123891, CVE-2026-123892 | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N), [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Important | \[1\] [9.1.1.0200](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-1-x/sddc-manager/sddc-manager-9-1-1-0200-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation  | SDDC Manager/ VCF Installer | 9.1.x.x | Any | CVE-2026-123893 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | \[1\] [9.1.1.0200](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-1-x/sddc-manager/sddc-manager-9-1-1-0200-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation | SDDC Manager | 9.0.x.x | Any | CVE-2026-123891, CVE-2026-123892 | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N), [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Important | [9.0.2.0100](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/sddc-manager/sddc-manager-9-0-2-0100-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation  | SDDC Manager / VCF Installer | 9.0.x.x | Any | CVE-2026-123893 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | [9.0.2.0100](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/sddc-manager/sddc-manager-9-0-2-0100-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Cloud Foundation | SDDC Manager | 5.x | Any | CVE-2026-123891, CVE-2026-123892, CVE-2026-123893 | [8.1](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N), [7.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Important | [5.2.5](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-525-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 


## 3e. VMware Tools SAML Token Signature Bypass vulnerability (CVE-2026-123894)

**Description:** VMware Tools for Windows contains a SAML token signature bypass vulnerability. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with access to a local privileged process on a Windows guest VM configured with Guest Alias mapping can exploit this vulnerability to elevate their privileges within the VM.

**Resolution:** To remediate CVE-2026-123894 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0009-qna](https://brcm.tech/vmsa-2026-0009-qna)

**Acknowledgments:** Broadcom would like to thank Noam Pomerantz for reporting this issue to us.

**Notes:**\[1\] VMware Tools 12.4.10 which is part of VMware Tools 12.5.5, also addresses the issue for Windows 32-bit.

**Response Matrix:**

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | VMware Tools | 13.x.x.x | Windows | CVE-2026-123894 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 13.1.5.0 | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Tools | N/A | 13.x.x.x | Windows | CVE-2026-123894 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 13.1.5.0 | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 
| VMware Tools | N/A | 12.3.x, 12.4.x, 12.5.x | Windows | CVE-2026-123894 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | \[1\]12.5.5 | None | [FAQ](https://brcm.tech/vmsa-2026-0009-qna) | 

 

## 4. References

**VMware vCenter 9.1.1.0200**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.1.0&os=&servicePk=545627&language=EN&groupId=545684&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.1.0&os=&servicePk=545627&language=EN&groupId=545684&viewGroup=true)


[https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-1-2&appid=vcf-9-1&language=en&format=rendered](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-1-2&appid=vcf-9-1&language=en&format=rendered)

**VMware vCenter 9.0.2.0200**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true)

[https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-0-2-0-2&appid=vcf-9-0&language=en&format=rendered](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-0-2-0-2&appid=vcf-9-0&language=en&format=rendered)

**VMware vCenter 8.0 U3m**Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16137](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16137)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html)

**VMware Tools 13.1.5**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.1.0&os=&servicePk=545627&language=EN&groupId=545614&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.1.0&os=&servicePk=545627&language=EN&groupId=545614&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-1-0/release-notes/vmware-tools-1315-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-1-0/release-notes/vmware-tools-1315-release-notes.html)

**VMware Tools 12.5.5**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Tools&freeDownloads=true](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Tools&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-5-0/release-notes/vmware-tools-1255-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-5-0/release-notes/vmware-tools-1255-release-notes.html)

**FIRST CVSSv3 Calculator:**CVE-2026-123890:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123891:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N)

CVE-2026-123892:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123893:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123894:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

## 5. Change Log:

**2026-11-19 VMSA-2026-0009**Initial security advisory.

**2026-11-20 VMSA-2026-0009.1**Updated advisory to clarify the impacted VMware Tools versions.

## 6. Contact:

E-mail:

[\[email protected\]](https://support.broadcom.com/cdn-cgi/l/email-protection#ff8992889e8d9ad18f8c968d8bbf9d8d909e9b9c9092d19c9092)

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
