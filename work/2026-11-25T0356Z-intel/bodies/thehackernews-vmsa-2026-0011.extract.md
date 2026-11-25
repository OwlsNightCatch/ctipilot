---
title: VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation
author: The Hacker News
url: https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html
hostname: thehackernews.com
description: Broadcom patches 23 VMware flaws, including a critical vCenter authentication bypass that could allow unauthorized access to the system.
sitename: The Hacker News
date: "2026-11-24"
categories: ['Article']
tags: ['Authentication bypass', 'enterprise security', 'Virtualization', 'VMware', 'VMware vCenter', 'Vulnerability']
fingerprint: b024bddcbfefc69d
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0zpQTclLnhVQHphFdBZZ_hrxhsZvA5G50sGBz5qq1iOg2B1YLu8rE5e_HM1GZOE24SNpwexwst80NTKP7_Wwexq7EzIl-I7ykIXCtTGQjeZhBGVVuAgzxac5JwaquTQuMNRstBFo8JzMDyqgsNbM_KtxGF3wHPBIM9GfaclNu0OTPlpF5YhNvqoKKytAY/s1700-nu-rw-lo-l85-e365/vmware-exploit.jpg
pagetype: article
filedate: "2026-11-25"
---
Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication.

The critical vulnerability, tracked as **CVE-2026-123903**, is rated 9.8 out of 10.0 on the CVSS scoring system. It resides in the VMware Directory Service ("vmdir").

"A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system," Broadcom [said](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626) in an advisory released today.

The company credited sglab of QiAnXin, Qi Qin (@LeoQ7\_) of depthfirst, and VulTeam and XGTP from ThreatBook for independently reporting the flaw.

Also patched in vCenter are four high-severity flaws, including an arbitrary file write vulnerability while processing certain archives that could be exploited to achieve code execution on the appliance (CVE-2026-123904, CVSS score: 7.5).

The remaining three vulnerabilities relate to denial-of-service in the VMware Directory Service (CVE-2026-123905, CVE-2026-123906, and CVE-2026-123907, CVSS scores: 7.5).

The issues have been addressed in the following versions -

- VMware Cloud Foundation and VMware vSphere Foundation 9.1.x.x - Fixed in 9.1.2
- VMware Cloud Foundation and VMware vSphere Foundation 9.0.x.x - Fixed in 9.0.2.0300
- VMware vCenter 8.0 - Fixed in 8.0 U3m
- VMware vCenter 7.0 (Contact Broadcom Support, if on extended support contract)
- VMware Cloud Foundation 5.x - Fixed in 5.2.5
- VMware Telco Cloud Platform - Fixed in vCenter 8.0 U3m (TCI: 3.0, TCP: 3.0, 4.x, 5.0.x, 5.1.x, 5.2)
- VMware Telco Cloud Infrastructure - Fixed in vCenter 8.0 U3m (TCI: 3.0, TCP: 3.0, 4.x, 5.0.x, 5.1.x, 5.2)

The fixes arrive days after Broadcom shipped updates for [CVE-2026-123890](https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html) (CVSS score: 9.8), another authentication bypass flaw impacting the VMware Directory Service that was exploited as a zero-day by a suspected China-nexus cyber espionage group called Armory Castle. VMware has [noted](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md) that CVE-2026-123903 is a distinct issue and is not related to CVE-2026-123890.

While Broadcom makes no mention of any of the newly disclosed flaws as being exploited in the wild, it's essential that customers apply the updates for optimal protection.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
