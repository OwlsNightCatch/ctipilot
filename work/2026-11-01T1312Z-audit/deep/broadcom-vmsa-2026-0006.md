# extract: served via trafilatura-direct
---
title: Support Content Notification - Support Portal - Broadcom support portal
url: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
hostname: broadcom.com
sitename: Support Portal
date: "2026-07-29"
fingerprint: f1e7bfdfff6fce19
---
VMSA-2026-0006.1: VMware ESX, vCenter, Workstation, and Fusion updates address multiple vulnerabilities (CVE-2026-59309, CVE-2026-59310, CVE-2026-47876, CVE-2026-41703, CVE-2026-41709)

38017

19 August 2026

29 July 2026

OPEN

CRITICAL

2.7-9.8

None

CVE-2026-59309, CVE-2026-59310, CVE-2026-47876, CVE-2026-41703, CVE-2026-41709

| **Advisory ID:** | VMSA-2026-0006.2 | 
| **Advisory Severity:** | Critical | 
| **CVSSv3 Range:** | 2.7-9.8 | 
| **Synopsis:** | VMware ESX, vCenter, Workstation, and Fusion updates address multiple vulnerabilities (CVE-2026-59309, CVE-2026-59310, CVE-2026-47876, CVE-2026-41703, CVE-2026-41709) | 
| **Issue date:** | 2026-07-29 | 
| **Updated on:** | 2026-08-19 | 
| **CVE(s)** | CVE-2026-59309, CVE-2026-59310, CVE-2026-47876, CVE-2026-41703, CVE-2026-41709 | 


## 1. Impacted Products

- VMware ESX
- VMware vCenter
- VMware Workstation
- VMware Fusion
- VMware Cloud Foundation
- VMware vSphere Foundation
- VMware Telco Cloud Platform
- VMware Telco Cloud Infrastructure

## 2. Introduction

Multiple vulnerabilities in VMware ESX, vCenter, Workstation, and Fusion were privately reported to Broadcom. Updates are available to remediate these vulnerabilities in affected Broadcom products.

## 3a. vCenter authentication-bypass vulnerability (CVE-2026-59309)

**Description:** VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system.

**Resolution:** To remediate CVE-2026-59309 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0006](https://brcm.tech/vmsa-2026-0006)

**Acknowledgments:** Broadcom would like to thank Phil Brass and Matt South of Atredis Partners

*for reporting this issue to us.*

**Notes:**

**\[1\]**Please note that patches are cumulative, meaning the current version includes all previously released fixes. While CVE-2026-59309 was addressed in 9.1.0.0200 first, version 9.1.0.0300 is the most recent version currently available which includes the fix for this CVE.

## 

3b. vCenter directory-traversal vulnerability (CVE-2026-59310)

**Description:** VMware vCenter contains a directory traversal vulnerability in the Syslog server. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to vCenter may exploit this issue to execute arbitrary code.

**Resolution:** To remediate CVE-2026-59310 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0006](https://brcm.tech/vmsa-2026-0006)

**Acknowledgments:** Broadcom would like to thank Phil Brass and Matt South of Atredis Partners

*for reporting this issue to us.*

**Notes:**None.

**Response Matrix 3a and 3b:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.1.x.x | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | **\[1\]** [9.1.0.0300](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-0-3&appid=vcf-9-1&language=en&format=rendered) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.0.x.x | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [9.0.2.0100](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=9-0-2-0-1&appid=vcf-9-0&language=en&format=rendered) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware vCenter | N/A | 8.0 | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [8.0 U3k](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3k-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware vCenter | N/A | 8.0 | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [8.0 U2f](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u2f-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware vCenter | N/A | 7.0 | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Contact Broadcom Support if you have extended support contract. | None | [FAQ](https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2026-0006#33-does-this-impact-vmware-vsphere-70) | 
| VMware Cloud Foundation | vCenter | 5.x | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | Async patch to [8.0 U3k](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3k-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | vCenter | 3.0, 4.x, 5.0.x, 5.1.x | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [KB449886](https://knowledge.broadcom.com/external/article/449886) | None | None | 
| VMware Telco Cloud Infrastructure | vCenter | 3.0 | Any | CVE-2026-59309, CVE-2026-59310 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [KB449886](https://knowledge.broadcom.com/external/article/449886) | None | None | 

**\[1\]** Please note that patches are cumulative, meaning the current version includes all previously released fixes. While CVE-2026-59309 was addressed in 9.1.0.0200 first, version 9.1.0.0300 is the most recent version currently available which includes the fix for this CVE.

## 

3c. VMXNET3 out-of-bounds write vulnerability (CVE-2026-47876)

**Description:** VMware ESX contains an out-of-bounds write vulnerability in the VMXNET3 virtual network adapter. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with local administrative privileges on a virtual machine with VMXNET3 virtual network adapter may exploit this issue to execute code on the host. Non VMXNET3 virtual adapters are not affected by this issue.

**Resolution:** To remediate CVE-2026-47876 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0006](https://brcm.tech/vmsa-2026-0006)

**Acknowledgments:** Broadcom would like to thank Nguyen Hoang Thach (@hi\_im\_d4rkn3ss) of STARLabs SG working with the Pwn2Own held by Zero day initiative for reporting this issue to us.

**Notes:**None.

**Response Matrix:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.1.x.x | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | [ESXi-9.1.0.0200-25557999](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x/vsphere/esx/esx-9-1-0-0200-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.0.x.x | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | [ESXi-9.0.2.0100-25595025](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0100-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | [ESXi80U3k-25595708](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3k-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | [ESXi80U2f-25626445](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u2f-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware ESX | N/A | 7.0 | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | Contact Broadcom Support if you have extended support contract. | None | [FAQ](https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2026-0006#33-does-this-impact-vmware-vsphere-70) | 
| VMware Cloud Foundation | ESX | 5.x | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | None | [FAQ](https://brcm.tech/vmsa-2026-0006) | 
| VMware Telco Cloud Platform | ESX | 5.0.x, 5.1.x | Any | CVE-2026-47876 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | Critical | [KB449886](https://knowledge.broadcom.com/external/article/449886) | None | None | 

 

## 3d. Out-of-bounds read vulnerability (CVE-2026-41703)

**Description:** VMware ESX, Workstation, and Fusion contain an out-of-bounds read vulnerability. Broadcom has evaluated the severity of this issue to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L).

**Known Attack Vectors:** A malicious actor with VM deployment privileges could trigger an out-of-bounds read, potentially leading to information disclosure or more likely a Denial-of-Service (DoS) condition of the host process. On Workstation and Fusion, the impact of this vulnerability is restricted to information disclosure.

**Resolution:** To remediate CVE-2026-41703 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**None.

**Acknowledgments:** Broadcom would like to thank Maxim Suhanov (@errno\_fail)

*for reporting this issue to us.*

**Notes:**None.

**Response Matrix:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.1.x.x | Any | CVE-2026-41703 | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L) | Important | [ESXi-9.1.0.0-25370933](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-0-0-release-notes.html) | None | None | 
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.0.x.x | Any | CVE-2026-41703 | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L) | Important | [ESXi-9.0.2.0100-25595025](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=esx-9-0-2-1&appid=vcf-9-0&language=en&format=rendered) | None | None | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-41703 | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L) | Important | [ESXi80U3i-25205845](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3i-release-notes.html) | None | None | 
| VMware Workstation | N/A | 25H2 | Any | CVE-2026-41703 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:N/A:N) | Low | 26H1 | None | None | 
| VMware Fusion | N/A | 25H2 | Any | CVE-2026-41703 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:N/A:N) | Low | 26H1 | None | None | 
| VMware Cloud Foundation | ESX | 5.x | Any | CVE-2026-41703 | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L) | Important | [5.2.3](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-523-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | ESX | 5.0.x, 5.1.x | Any | CVE-2026-41703 | [7.6](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L) | Important | [KB449886](https://knowledge.broadcom.com/external/article/449886) | None | None | 

 

## 3e. ESX insufficient logging vulnerability (CVE-2026-41709)

**Description:** VMware ESX contains an insufficient logging vulnerability. Broadcom has evaluated the severity of this issue to be in the

[Low severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N).

**Known Attack Vectors:**A malicious administrator could exploit this issue to perform certain operations without them being logged.

**Resolution:** To remediate CVE-2026-41709 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgments:** Broadcom would like to thank Ian Barton of CrowdStrike

*for reporting this issue to us.*

**Notes:**None.

**Response Matrix:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.1.x.x | Any | CVE-2026-41709 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | Low | [ESXi-9.1.0.0-25370933](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-0-0-release-notes.html) | None | None | 
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.0.x.x | Any | CVE-2026-41709 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | Low | [ESXi-9.0.2.0100-25595025](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=esx-9-0-2-1&appid=vcf-9-0&language=en&format=rendered) | None | None | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-41709 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | Low | [ESXi80U3j-25429389](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3j-release-notes.html) | None | None | 
| VMware Cloud Foundation | ESX | 5.x | Any | CVE-2026-41709 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | Low | [5.2.4](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-524-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | ESX | 5.0.x, 5.1.x | Any | CVE-2026-41709 | [2.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N) | Low | [KB449886](https://knowledge.broadcom.com/external/article/449886) | None | None | 


## 4. References

**VMware Cloud Foundation 9.1.0.x**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x.html)

**VMware Cloud Foundation 9.0.x**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Cloud%20Foundation&displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x.html)

**VMware vSphere Foundation 9.1.0.x**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20vSphere%20Foundation&displayGroup=VMware%20vSphere%20Foundation%209&release=9.1.0.0&os=&servicePk=542815&language=EN](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20vSphere%20Foundation&displayGroup=VMware%20vSphere%20Foundation%209&release=9.1.0.0&os=&servicePk=542815&language=EN)

**VMware vSphere Foundation 9.0.x**
Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20vSphere%20Foundation&displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.2.0&os=&servicePk=537838&language=EN](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20vSphere%20Foundation&displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.2.0&os=&servicePk=537838&language=EN)


**VMware Cloud Foundation 5.2.4**Downloads and Documentation:

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-524-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-524-release-notes.html)

**VMware Cloud Foundation 5.2.3**
Downloads and Documentation:

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-523-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-523-release-notes.html)


**VMware vCenter 9.1.0.0300**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN&groupId=540509&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN&groupId=540509&viewGroup=true)

[https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-0-3&appid=vcf-9-1&language=en&format=rendered](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcenter-9-1-0-3&appid=vcf-9-1&language=en&format=rendered)


**VMware vCenter 9.0.2.0100**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true)

[https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=9-0-2-0-1&appid=vcf-9-0&language=en&format=rendered](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=9-0-2-0-1&appid=vcf-9-0&language=en&format=rendered)

**VMware ESX 9.1.0.0200**

Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN&groupId=540591&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.0.0&os=&servicePk=540528&language=EN&groupId=540591&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x/vsphere/esx/esx-9-1-0-0200-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/patch-releases-9-1-0-x/vsphere/esx/esx-9-1-0-0200-release-notes.html)

**VMware ESX 9.0.2.0100**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537810&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537810&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0100-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0100-release-notes.html)

**VMware vCenter 8.0 U3k**Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16109](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16109)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3k-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3k-release-notes.html)

**VMware vCenter 8.0 U2f**

Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16108](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16108) 

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u2f-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u2f-release-notes.html)

**VMware ESX 8.0 U3k**Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16106](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16106)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3k-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3k-release-notes.html)

**VMware ESX 8.0 U3j**Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16046](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16046)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3j-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3j-release-notes.html)

**VMware ESX 8.0 U3i**Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16046](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16046)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3i-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3i-release-notes.html)

**VMware ESX 8.0 U2f**
Downloads and Documentation:

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16107](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16107)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u2f-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u2f-release-notes.html)

**VMware Workstation 26H1**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/26H1.html](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/26H1.html)

**VMware Fusion 26H1**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Fusion&displayGroup=VMware%20Fusion%2026H1&release=26H1&os=&servicePk=543219&language=EN&freeDownloads=true](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Fusion&displayGroup=VMware%20Fusion%2026H1&release=26H1&os=&servicePk=543219&language=EN&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1.html](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1.html)

**FIRST CVSSv3 Calculator:**CVE-2026-59309:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-59310:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-47876:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)

CVE-2026-41703:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L)

CVE-2026-41709:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N)


## **5. Change Log:**

**2026-07-29 VMSA-2026-0006**Initial security advisory.

**2026-08-03 VMSA-2026-0006.1** ESX 8.0 U2f and vCenter 8.0 U2f express patches are available.

**2026-08-19 VMSA-2026-0006.2**

Added ESX/vCenter 7.0 patch guidance for Critical severity issues.

## **6. Contact:**


[\[email protected\]](https://support.broadcom.com/cdn-cgi/l/email-protection#196f746e786b7c37696a706b6d597b6b76787d7a7674377a7674)

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
