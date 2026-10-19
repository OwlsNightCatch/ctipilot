---
title: JVN#88474777 SiteGuard Server Edition vulnerable to OS command injection Critical
url: https://jvn.jp/en/jp/JVN88474777/index.html
hostname: jvn.jp
description: Japan Vulnerability Notes
sitename: jvn.jp
date: "2026-10-14"
tags: ['Japan Vulnerability Notes']
fingerprint: "9f811dd269f36fc1"
---
# JVN#88474777

SiteGuard Server Edition vulnerable to OS command injection

Critical

## Overview

SiteGuard Server Edition provided by EG Secure Solutions Inc. contains an OS command injection vulnerability.

## Products Affected

- SiteGuard Server Edition Ver2.20 and later versions
	
  - For IIS: versions from Ver3.10 to Ver4.00 Update 4 are not affected.

The product is affected by this vulnerability when the statistics feature is enabled. The feature is enabled by default.

## Description

SiteGuard Server Edition provided by EG Secure Solutions Inc. is a host-based Web Application Firewall (WAF) designed to be integrated into a web server. The statistics feature of SiteGuard Server Edition contains the following vulnerability:

- **OS command injection ([CWE-78](https://cwe.mitre.org/data/definitions/78.html))**
  - CVSS:4.0/AV:L/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N Base Score 8.5
  - CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H Base Score 7.8
  - CVE-2026-106931

Note that the vulnerability has been confirmed to be exploited in the wild.

## Impact

An attacker may be able to execute arbitrary OS commands with root or SYSTEM privileges on the system running the affected product.

## Solution

**Update the Software**

Update the software to the latest version according to the information provided by the developer.

This vulnerability has been fixed in the following versions:

- For Apache httpd, Nginx, IIS: Ver8.00 Update 5
- For Apache httpd and Nginx on FreeBSD: Ver7.00 Update 6

**Apply the patch**

For users who are unable to upgrade, the developer provides a patch that replaces the files used in statistical processing. The patch is available even for end-of-life (EOL) versions.

The developer notified customers with direct support contracts of this vulnerability and the available countermeasures on September 29, 2026.

For more details, refer to the information provided by the developer.

## Vendor Status

| Vendor | Link | 
| EG Secure Solutions Inc. | [SiteGuard Server Edition vulnerable to OS command injection(Critical) (Text in Japanese)](https://www.eg-secure.co.jp/siteguard/news/alert-202610-1) | 

## References


## JPCERT/CC Addendum

## Vulnerability Analysis by JPCERT/CC

## Credit

The developer reported this vulnerability to IPA.

JPCERT/CC coordinated with the developer under Information Security Early Warning Partnership.

## Other Information


| JPCERT Alert | [JPCERT-AT-2026-0032](https://www.jpcert.or.jp/at/2026/at260032.html) Security Advisory Regarding an OS Command Injection Vulnerability (CVE-2026-106931) in SiteGuard Server Edition (Text in Japanese) | 
| JPCERT Reports |  | 
| CERT Advisory |  | 
| CPNI Advisory |  | 
| TRnotes |  | 
| CVE | [CVE-2026-106931](https://www.cve.org/CVERecord?id=CVE-2026-106931) | 
| JVN iPedia | [JVNDB-2026-000148](https://jvndb.jvn.jp/jvndb/JVNDB-2026-000148) | 

## Update History


- 2026/10/14
- Information under the section "Other Information" was updated
