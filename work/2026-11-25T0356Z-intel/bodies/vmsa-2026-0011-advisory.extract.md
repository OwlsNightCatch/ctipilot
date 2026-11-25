---
title: Support Content Notification - Support Portal
url: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626
hostname: broadcom.com
sitename: Support Portal
date: "2010-01-13"
fingerprint: e5e73bd6d9fdce1b
language: en
pagetype: website
filedate: "2026-11-25"
---
# VMSA-2026-0011: VMware ESX, vCenter, Workstation, Fusion, and, Avi Load Balancer updates address multiple vulnerabilities

39626

24 November 2026

24 November 2026

OPEN

CRITICAL

3.4-9.8

No

CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909, CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916, CVE-2026-123918, CVE-2026-123919, CVE-2026-123920, CVE-2026-123921, CVE-2026-123922, CVE-2026-123923, CVE-2026-123924, CVE-2026-123925, CVE-2026-123926

| **Advisory ID:** | VMSA-2026-0011 | 
| **Advisory Severity:** | Critical | 
| **CVSSv3 Range:** | 3.4-9.8 | 
| **Synopsis:** | VMware ESX, vCenter, Workstation, Fusion, Tools, and, Avi Load Balancer updates address multiple vulnerabilities (CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909, CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916, CVE-2026-123918, CVE-2026-123919, CVE-2026-123920, CVE-2026-123921, CVE-2026-123922, CVE-2026-123923, CVE-2026-123924, CVE-2026-123925, CVE-2026-123926) | 
| **Issue date:** | 2026-11-24 | 
| **Updated on:** | 2026-11-24 (Initial Advisory) | 
| **CVE(s)** | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909, CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916, CVE-2026-123918, CVE-2026-123919, CVE-2026-123920, CVE-2026-123921, CVE-2026-123922, CVE-2026-123923, CVE-2026-123924, CVE-2026-123925, CVE-2026-123926 | 

## 1. Impacted Products

- VMware ESX
- VMware vCenter
- VMware Workstation
- VMware Fusion
- VMware Tools
- VMware Cloud Foundation
- VMware vSphere Foundation
- VMware Telco Cloud Platform
- VMware Telco Cloud Infrastructure
- VMware Avi Load Balancer

## 2. Introduction

Multiple vulnerabilities in VMware ESX, vCenter, Workstation, Fusion, Tools, and Avi Load Balancer were privately reported to Broadcom. Updates are available to remediate these vulnerabilities in affected Broadcom products.

## 3a. vCenter authentication-bypass vulnerability (CVE-2026-123903)

**Description:** VMware vCenter contains an authentication bypass vulnerability in the VMware Directory Service. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system.

**Resolution:** To remediate CVE-2026-123903 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank mochazz of sglab of Qianxin, Qi Qin (@LeoQ7\_) of depthfirst, and VulTeam, XGTP from ThreatBook for independently reporting this issue to us.

**Notes:**None

## 3b. vCenter arbitrary file write vulnerability (CVE-2026-123904)

**Description:** VMware vCenter contains an arbitrary file write vulnerability while processing certain archives. Broadcom has evaluated the severity of this issue to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with access to the backup repository may exploit this issue to write files to arbitrary locations as root, which may lead to code execution on the appliance.

**Resolution:** To remediate CVE-2026-123904 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Mateusz Gierblinski of Curios for reporting this issue to us.

**Notes:**None.

## 3c. vCenter vmdir *multiple* denial-of-service vulnerabilities  (CVE-2026-123905, CVE-2026-123906, CVE-2026-123907)

**Description:** VMware vCenter contains multiple denial-of-service vulnerabilities in the VMware Directory Service. Broadcom has evaluated the severity of these issues to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H).

**Known Attack Vectors:**A malicious actor with network access to vCenter may exploit these issues to cause a denial-of-service to the vmdir service.

**Resolution:** To remediate CVE-2026-123905, CVE-2026-123906, and CVE-2026-123907 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Phil Brass and Matt South of Atredis Partners

*for reporting these issues to us.*

**Notes:**None.

## 3d. vCenter local privilege-escalation vulnerability (CVE-2026-123908)

**Description:** 

VMware vCenter contains a local privilege escalation vulnerability due to a flaw in a vpxd service script. Broadcom has evaluated the severity of this issue to be in the [Important severity range](https://www.vmware.com/support/policies/security_response.html) with a maximum CVSSv3 base score of [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor who has compromised the vpxd service account may exploit this issue to escalate privileges to root on the appliance.

**Resolution:** To remediate CVE-2026-123908 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Phil Brass and Matt South of Atredis Partners

*for reporting this issue to us.*

**Notes:**None.

## 3e. vCenter vDS security policy enforecement failure (CVE-2026-123909)

**Description:** VMware vCenter contains a vulnerability due to a policy enforcement failure in vDS (vSphere Distributed Switch). Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N).

**Known Attack Vectors:**A local actor on a VM may exploit this issue to operate with certain capabilities which may expose the environment to elevated risk.

**Resolution:** To remediate CVE-2026-123909 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Joao Bernardo Vieira Gomes, Carlos Frederico Liberato Lopes, and Sergio Fellipe Ferreira de Araújofor for reporting this issue to us.

**Notes:**None.

**Response Matrix 3a-3e:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.1.x.x | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [9.1.2](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation | vCenter | 9.0.x.x | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [9.0.2.0300](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/vcenter/vcenter-9-0-2-0300-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware vCenter | N/A | 8.0 | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [8.0 U3m](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware vCenter | N/A | 7.0 | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | Contact Broadcom Support if you have extended support contract. | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Cloud Foundation | vCenter | 5.x | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [5.2.5](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-525-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | vCenter | 3.0, 4.x, 5.0.x, 5.1.x, 5.2 | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [KB463501](https://knowledge.broadcom.com/external/article/463501) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Telco Cloud Infrastructure | vCenter | 3.0 | Any | CVE-2026-123903, CVE-2026-123904, CVE-2026-123905, CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [7.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [5.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N) | Critical | [KB463501](https://knowledge.broadcom.com/external/article/463501) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 

**Please note that patches are cumulative, meaning the current version includes all previously released fixes. While some CVEs were initially addressed in the older releases, the versions mentioned in the response matrix are the latest available and contain all the fixes.**

## 

3f. ESX heap out-of-bounds write vulnerability (CVE-2026-123910)

**Description:** ESX contains a heap out-of-bounds write vulnerability in the I/O filter service. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to ESX may execute code on the host.

**Resolution:** To remediate CVE-2026-123910 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**Please see the response matrix.

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Dylan Barker, Marco Ortisi, Patrick Bennett, James Spencer of CrowdStrike

*for reporting this issue to us.*

**Notes:**None.

## 3g. ESX use-after-free vulnerability (CVE-2026-123911)

**Description:** ESX contains a use-after-free vulnerability in the I/O filter service. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access to ESX may execute code on the host.

**Resolution:** To remediate CVE-2026-123911 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**Please see the response matrix.

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank NiNi (@terrynini38514) of DEVCORE Research Team working with TrendAI Zero Day Initiative

*for reporting this issue to us.*

**Notes:**None.

## 3h. Out-of-bounds write vulnerability in XHCI USB controller (CVE-2026-123912)

**Description:** VMware ESXi, Workstation, and Fusion contain an out-of-bounds write vulnerability in the XHCI USB controller. Broadcom has evaluated the severity of this issue to be in the

[Critical severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with local administrative privileges on a virtual machine may exploit this issue to execute code as the virtual machine's VMX process running on the host. On ESX, the exploitation is contained within the VMX sandbox whereas, on Workstation and Fusion, this may lead to code execution on the machine where Workstation or Fusion is installed.

**Resolution:**
To remediate CVE-2026-123912 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Jaeyeong Lee and Stan S

*for independently reporting this issue to us.*

**Response Matrix:** 

## 3i. ESX VMkernel stack-based buffer-overflow vulnerability (CVE-2026-123913)

**Description:** VMware ESX contains a stack-based buffer-overflow vulnerability in the VMkernel. Broadcom has evaluated the severity of this issue to be in the

[Important severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with

*privileges*within the VMX process, may trigger this vulnerability to elevate privileges.

**Resolution:** To remediate CVE-2026-123913 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Gwangun Jung (@pr0ln) of Theori, with Xint Code working with TrendAI Zero Day Initiative for reporting this issue to us.

**Notes:**None.

## 3j. ESX security bypass vulnerability (CVE-2026-123914)

**Description:** VMware ESX contains a security bypass vulnerability due to improper protection of the host configuration store. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with root privileges on an ESX host that has Secure Boot enabled may tamper the host's configuration store to perform certain unauthorized actions.

**Resolution:** To remediate CVE-2026-123914 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Anders Olsson of Truesec and Austin Gadient of Vali Cyber for reporting this issue to us.

**Notes:**None.

## 3k. ESX signature verification bypass vulnerability (CVE-2026-123915)

**Description:** VMware ESX contains a signature verification bypass vulnerability allowing persistence of malicious files across reboots. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L).

**Known Attack Vectors:**A malicious actor may utilize this vulnerability to obtain persistence of malicious files across reboots.

**Resolution:** To remediate CVE-2026-123915 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Anders Olsson of Truesec and Austin Gadient of Vali Cyber

*for reporting this issue to us.*

**Notes:**None.

## 3l. Guest RPC denial-of-service vulnerability (CVE-2026-123916)

**Description:** VMware ESX, Workstation, and Fusion contains a denial-of-service vulnerability in guest RPC. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of 5.5.

**Known Attack Vectors:**A malicious actor with non-administrative privileges on a VM may exploit this issue by send a specially crafted RPC command to crash the VMX process resulting in a denial of service of the VM.

**Resolution:** To remediate CVE-2026-123916 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank DEVCORE team

*for reporting this issue to us.*

**Notes:**None.

**Response Matrix 3f-3l:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.1.x.x | Any | CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | [ESXi-9.1.2.0-25946735](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/esx-9-1-2-0-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.0.x.x | Any | CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123916 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | [ESXi-9.0.2.0200-25953133](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0200-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Cloud Foundation, VMware vSphere Foundation | ESX | 9.0.x.x | Any | CVE-2026-123914, CVE-2026-123915 | [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L) | Moderate | Patch Pending | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-123910, CVE-2026-123911 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Critical | [ESXi80U3m-25926933](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3m-release-notes.html) | [KB463535](https://knowledge.broadcom.com/external/article/463535) | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware ESX | N/A | 8.0 | Any | CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916 | [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Important | [ESXi80U3m-25926933](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3m-release-notes.html) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware ESX | N/A | 7.0 | Any | CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | Contact Broadcom Support if you have extended support contract. | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Workstation | N/A | 25H2 | Any | CVE-2026-123912, CVE-2026-123916 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | 26H1u1 | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Fusion | N/A | 25H2 | Any | CVE-2026-123912, CVE-2026-123916 | [9.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | 26H1u1 | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Cloud Foundation | ESX | 5.x | Any | CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | [5.2.5](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-525-release-notes.html) | None | Async Patching Guide: [KB88287](https://knowledge.broadcom.com/external/article?legacyId=88287) | 
| VMware Telco Cloud Platform | ESX | 5.0.x, 5.1.x | Any | CVE-2026-123910, CVE-2026-123911, CVE-2026-123912, CVE-2026-123913, CVE-2026-123914, CVE-2026-123915, CVE-2026-123916 | [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [9.8](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.4](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), [8.2](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H), [6.7](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.3](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L), [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Critical | [KB463501](https://knowledge.broadcom.com/external/article/463501) | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 

**Please note that patches are cumulative, meaning the current version includes all previously released fixes. While some CVEs were initially addressed in the older releases, the versions mentioned in the response matrix are the latest available and contain all the fixes.**

## 3m. VMware Avi Load Balancer insecure deserialization vulnerability (CVE-2026-123919)

**Description:**VMware Avi Load Balancer contains an insecure deserialization vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Moderate severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with local administrative privileges on the Avi Controller may exploit this issue to execute arbitrary code as root.

**Resolution:**To remediate CVE-2026-123919 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3n. VMware Avi Load Balancer local privilege escalation vulnerability (CVE-2026-123920)

**Description:**VMware Avi Load Balancer contains a local privilege escalation vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Moderate severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with local administrative privileges on the Avi Controller may exploit this issue to escalate privileges to root.

**Resolution:**To remediate CVE-2026-123920 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Lang Khuong Duy (Viettel IDC) for reporting this issue to us.

**Notes:**None.

## 3o. VMware Avi Load Balancer command injection vulnerability (CVE-2026-123921)

**Description:**VMware Avi Load Balancer contains a command injection vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Moderate severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[6.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H).

**Known Attack Vectors:**A malicious actor with network access and administrative privileges on VMware Avi Load Balancer may exploit this issue to execute arbitrary commands on the Avi Controller.

**Resolution:**To remediate CVE-2026-123921 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3p. VMware Avi Load Balancer sensitive information disclosure vulnerability (CVE-2026-123922)

**Description:**VMware Avi Load Balancer contains a sensitive information disclosure vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Moderate severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[4.9](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N).

**Known Attack Vectors:**A malicious actor with network access and administrative privileges on VMware Avi Load Balancer may exploit this issue to read the password hashes.

**Resolution:**To remediate CVE-2026-123922 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3q. VMware Avi Load Balancer sensitive information disclosure vulnerability (CVE-2026-123923)

**Description:**VMware Avi Load Balancer contains a sensitive information disclosure vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Low severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[3.4](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N).

**Known Attack Vectors:**A malicious actor with administrative privileges to a Service Engine may exploit this issue to access its routing management interface using a credential that is the same on every installation.

**Resolution:**To remediate CVE-2026-123923 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3r. VMware Avi Load Balancer sensitive information disclosure vulnerability (CVE-2026-123924)

**Description:**

VMware Avi Load Balancer contains a sensitive information disclosure vulnerability. Broadcom has evaluated the severity of the issue to be in the [Low severity range](https://www.broadcom.com/support/vmware-services/security-response) with a maximum CVSSv3 base score of [3.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N).

**Known Attack Vectors:**A malicious actor with administrative privileges to the Avi Controller may exploit this issue to access resources beyond their intended privileges.

**Resolution:**To remediate CVE-2026-123924 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3s. VMware Avi Load Balancer directory traversal vulnerability (CVE-2026-123925)

**Description:**VMware Avi Load Balancer contains a directory traversal vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Low severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[3.8](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L).

**Known Attack Vectors:**A malicious actor with network access and administrative privileges on VMware Avi Load Balancer may exploit this issue to delete and access files outside the intended directory.

**Resolution:**To remediate CVE-2026-123925 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**Broadcom would like to thank Filip Waeytens (NATO NCSC) for reporting this issue to us.

**Notes:**None.

## 3t. VMware Avi Load Balancer sensitive information disclosure vulnerability (CVE-2026-123926)

**Description:**VMware Avi Load Balancer contains a sensitive information disclosure vulnerability. Broadcom has evaluated the severity of the issue to be in the

[Moderate severity range](https://www.broadcom.com/support/vmware-services/security-response)with a maximum CVSSv3 base score of

[6.5](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N).

**Known Attack Vectors:**A malicious authenticated actor with network access on VMware Avi Load Balancer may exploit this issue to access resources beyond their intended privileges.

**Resolution:**To remediate CVE-2026-123926 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None.

**Additional Documentation:**None.

**Acknowledgements:**None.

**Notes:**None

**Response Matrix 3m-3t:**

| VMware Product | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|
| VMware Avi Load Balancer | 32.1.1-32.1.3 | Any | CVE-2026-123919, CVE-2026-123920, CVE-2026-123921, CVE-2026-123922, CVE-2026-123925, CVE-2026-123924, CVE-2026-123923 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H),[6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H), [4.9](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N), [3.8](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L), [3.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N), [3.4](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N) | Moderate | 32.1.4 | None | None | 
| VMware Avi Load Balancer | 31.1.1–31.2.2 | Any | CVE-2026-123919, CVE-2026-123921 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 31.2.3 | None | None | 
| VMware Avi Load Balancer | 31.1.1–31.2.3 | Any | CVE-2026-123920, CVE-2026-123922, CVE-2026-123925, CVE-2026-123924, CVE-2026-123923 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [4.9](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N), [3.8](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L), [3.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N), [3.4](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N) | Moderate | 32.1.4 | None | None | 
| VMware Avi Load Balancer | 30.1.1–30.2.6 | Any | CVE-2026-123920 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 30.2.7 | None | None | 
| VMware Avi Load Balancer | 30.1.1–30.2.7 | Any | CVE-2026-123919, CVE-2026-123921 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 31.2.3 | None | None | 
| VMware Avi Load Balancer | 30.1.1–30.2.7 | Any | CVE-2026-123922, CVE-2026-123925, CVE-2026-123924, CVE-2026-123923 | [4.9](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N), [3.8](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L), [3.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N), [3.4](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N) | Moderate | 32.1.4 | None | None | 
| VMware Avi Load Balancer | 22.1.1–22.1.7 | Any | CVE-2026-123919, CVE-2026-123921 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [6.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H) | Moderate | 31.2.3 | None | None | 
| VMware Avi Load Balancer | 22.1.1–22.1.7 | Any | CVE-2026-123920, CVE-2026-123922, CVE-2026-123925, CVE-2026-123924, CVE-2026-123923 | [6.7](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H), [4.9](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N), [3.8](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L), [3.6](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N), [3.4](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N) | Moderate | 32.1.4 | None | None | 
| VMware Avi Load Balancer | 32.1.3 | Any | CVE-2026-123926 | [6.5](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | Moderate | 32.1.3-2p1 | None | None | 
| VMware Avi Load Balancer | 32.1.1–32.1.2 | Any | CVE-2026-123926 | [6.5](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | Moderate | 32.1.2-2p3 | None | None | 
| VMware Avi Load Balancer | 30.x | Any | CVE-2026-123926 | [6.5](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | Moderate | Not Impacted | None | None | 
| VMware Avi Load Balancer | 22.x | Any | CVE-2026-123926 | [6.5](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N) | Moderate | Not Impacted | None | None | 

 

## 3u. VMware Tools VGAuth denial-of-service vulnerability (CVE-2026-123918)

**Description:** VMware Tools contains a denial-of-service vulnerability in VGAuth service. Broadcom has evaluated the severity of this issue to be in the

[Moderate severity range](https://www.vmware.com/support/policies/security_response.html)with a maximum CVSSv3 base score of

[5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H).

**Known Attack Vectors:**A malicious actor with non-administrative privileges on a VM may exploit this issue by send a specially crafted RPC command to crash the VMX process resulting in a denial of service of the VM.

**Resolution:** To remediate CVE-2026-123918 apply the patches listed in the 'Fixed Version' column of the 'Response Matrix' found below.

**Workarounds:**None

**Additional Documentation:**A supplemental FAQ was created for clarification. Please see:

[https://brcm.tech/vmsa-2026-0011-qna](https://brcm.tech/vmsa-2026-0011-qna)

**Acknowledgments:** Broadcom would like to thank Lian

*for reporting this issue to us.*

**Notes:**\[1\] VMware Tools 12.4.11 which is part of VMware Tools 12.5.6, also addresses the issue for Windows 32-bit.

\[2\] A version of open-vm-tools that addresses CVE-2026-123918 will be distributed by Linux vendors.

**Response Matrix 3u:** 

| VMware Product | Component | Version | Running On | CVE | **CVSSv3** | Severity | Fixed Version | Workarounds | Additional Documentation | 
|---|---|---|---|---|---|---|---|---|---|
| VMware Cloud Foundation, VMware vSphere Foundation  | VMware Tools | 13.x.x.x | Windows, Linux | CVE-2026-123918 | [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Moderate | 13.1.10.0 | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Tools | N/A | 13.x.x.x | Windows, Linux | CVE-2026-123918 | [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Moderate | \[2\] 13.1.10.0 | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 
| VMware Tools | N/A | 12.x.x, 11.x.x | Windows, Linux | CVE-2026-123918 | [5.5](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | Moderate | \[1\] \[2\] 12.5.6.0 | None | [FAQ](https://brcm.tech/vmsa-2026-0011-qna) | 

**Fixed versions may differ based on the Linux distribution version and the distribution vendor..**

## 4. References

**VMware ESX 9.1.2 Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547650&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547650&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/esx-9-1-2-0-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/esx-9-1-2-0-release-notes.html)


**VMware vCenter 9.1.2 Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547661&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547661&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html)

**VMware ESX 9.0.2.0200 Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537810&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537810&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0200-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/esx/esx-9-0-2-0200-release-notes.html)

**VMware vCenter 9.0.2.0300
Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.2.0&os=&servicePk=537791&language=EN&groupId=537830&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/vcenter/vcenter-9-0-2-0300-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/vcenter/vcenter-9-0-2-0300-release-notes.html)

**VMware ESX 80U3m
Downloads and Documentation:**

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16136](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16136)


[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3m-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3m-release-notes.html)


**VMware vCenter 8.0 U3m Downloads and Documentation:**

[https://support.broadcom.com/web/ecx/solutiondetails?patchId=16137](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16137)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html)

**VMware Workstation 26H1u1**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/26H1/release-notes/vmware-workstation-pro-26h1u1-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/26H1/release-notes/vmware-workstation-pro-26h1u1-release-notes.html)

**VMware Fusion 26H1u1**Downloads and Documentation:

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Fusion&displayGroup=VMware%20Fusion%2026H1&release=26H1&os=&servicePk=543219&language=EN&freeDownloads=true](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Fusion&displayGroup=VMware%20Fusion%2026H1&release=26H1&os=&servicePk=543219&language=EN&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/release-notes/vmware-fusion-26h1u1-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/release-notes/vmware-fusion-26h1u1-release-notes.html)

**VMware Tools 13.1.10.0 Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547585&viewGroup=true](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.1.2.0&os=&servicePk=547583&language=EN&groupId=547585&viewGroup=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-1-0/release-notes/vmware-tools-13110-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-1-0/release-notes/vmware-tools-13110-release-notes.html)


**VMware Tools 12.5.6.0 Downloads and Documentation:**

[https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Tools&displayGroup=VMware%20Tools%2012.x&release=12.5.6&os=&servicePk=549964&language=EN&freeDownloads=true](https://support.broadcom.com/group/ecx/productfiles?subFamily=VMware%20Tools&displayGroup=VMware%20Tools%2012.x&release=12.5.6&os=&servicePk=549964&language=EN&freeDownloads=true)

[https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-5-0/release-notes/vmware-tools-1256-release-notes.html](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-5-0/release-notes/vmware-tools-1256-release-notes.html)

**VMware Avi Load Balancer 32.1.4
Downloads and Documentation:**

[https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-4.html](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-4.html)

**VMware Avi Load Balancer 31.2.3 Downloads and Documentation:**

[https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/31-2/vmware-avi-load-balancer-release-notes/Release-notes-for-avi-load-balancer-version-31-2-3.html](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/31-2/vmware-avi-load-balancer-release-notes/Release-notes-for-avi-load-balancer-version-31-2-3.html)

**VMware Avi Load Balancer 30.2.7 Downloads and Documentation:**

[https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/30-2/vmware-avi-load-balancer-release-notes/Release-Notes-for-Avi-Load-Balancer-Version-30-2-7.html](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/30-2/vmware-avi-load-balancer-release-notes/Release-Notes-for-Avi-Load-Balancer-Version-30-2-7.html)

**VMware Avi Load Balancer 32.1.3-2p1
Downloads and Documentation:**

[https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-3.html#:\~:text=Notes%20for%2032.1.3-,32.1.3%2D2p1,-Release%20Date%3A%2024](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-3.html#:~:text=Notes%20for%2032.1.3-,32.1.3%2D2p1,-Release%20Date%3A%2024)

**VMware Avi Load Balancer 32.1.2-2p3 Downloads and Documentation:**

[https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-2.html#:\~:text=a%20single%20SE.-,32.1.2%2D2p3,-Release%20Date%3A%2008](https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer/avi-load-balancer/32-1/vmware-avi-load-balancer-release-notes/release-notes-for-avi-load-balancer-version-32-1-2.html#:~:text=a%20single%20SE.-,32.1.2%2D2p3,-Release%20Date%3A%2008)

**FIRST CVSSv3 Calculator:**CVE-2026-123903:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123904:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H)

CVE-2026-123905:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

CVE-2026-123906:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

CVE-2026-123907:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

CVE-2026-123908:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123909:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:L/A:N)

CVE-2026-123910:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123911:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123912: (WS/Fusion)-

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)

ESX-

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123913:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H)

CVE-2026-123914:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123915:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123916:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L)

CVE-2026-123918:

[https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H)

CVE-2026-123919:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123920:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123921:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H)

CVE-2026-123922:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N)

CVE-2026-123923

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N)

CVE-2026-123924:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N)

CVE-2026-123925:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:L)

CVE-2026-123926:

[https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3-1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)

## 5. Change Log:

**2026-11-24 VMSA-2026-0011**Initial security advisory.

## 6. Contact:

E-mail:

[\[email protected\]](https://support.broadcom.com/cdn-cgi/l/email-protection#6e1803190f1c0b401e1d071c1a2e0c1c010f0a0d0103400d0103)

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
