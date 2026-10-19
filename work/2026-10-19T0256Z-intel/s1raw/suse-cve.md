---
title: CVE-2026-99999 Common Vulnerabilities and Exposures | SUSE
url: https://www.suse.com/security/cve/CVE-2026-99999.html
hostname: suse.com
description: Secure your Linux systems from CVE-2026-99999 with SUSE.
sitename: SUSE
date: "2026-01-01"
tags: ['CVE-2026-99999, security advisory, suse linux, suse, security, cve']
fingerprint: "81fa7852d5bf74ef"
---
### Upstream information

#### Description

In the Linux kernel, the following vulnerability has been resolved:
ipv4: validate checksum\_start before completing checksum

If a packet with bad checksum metadata gets into the ipv4 stack,

skb\_checksum\_help can corrupt the network header and cause a bunch of

mischief.

This was discovered and reported by Paulos, and has been reporoduced

by others independently since.

We really shouldn't allow such packets in, but as a defence

in depth measure, let's also check before we complete the checksum.

A more complete validation at input is forthcoming, but needs more work.

### Other Security Trackers

### [SUSE information](https://www.suse.com/c/cve-pages-self-help-security-issues-suse-linux-enterprise/)

Overall state of this security issue: Pending

This issue is currently rated as having [important](https://www.suse.com/support/security/rating/) severity.

| CVSS v3 Scores |  |  |  | 
|---|---|---|---|
| CVSS detail | CNA (NVD) | Linux Kernel CNA | SUSE | 
|---|---|---|---|
| Base Score | 9.3 | 9.3 | 8.8 | 
| Vector | CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H | CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H | 
| Attack Vector | Local | Local | Local | 
| Attack Complexity | Low | Low | Low | 
| Privileges Required | None | None | Low | 
| User Interaction | None | None | None | 
| Scope | Changed | Changed | Changed | 
| Confidentiality Impact | High | High | High | 
| Integrity Impact | High | High | High | 
| Availability Impact | High | High | High | 
| CVSSv3 Version | 3.1 | 3.1 | 3.1 | 

| CVSS v4 Scores |  | 
|---|---|
| CVSS detail | SUSE | 
|---|---|
| Base Score | 9.3 | 
| Vector | CVSS:4.0/AV:L/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H | 
| Attack Vector | Local | 
| Attack Complexity | Low | 
| Attack Requirements | None | 
| Privileges Required | Low | 
| User Interaction | None | 
| Vulnerable System Confidentiality Impact | High | 
| Vulnerable System Integrity Impact | High | 
| Vulnerable System Availability Impact | High | 
| Subsequent System Confidentiality Impact | High | 
| Subsequent System Integrity Impact | High | 
| Subsequent System Availability Impact | High | 
| CVSSv4 Version | 4.0 | 

#### Note from the SUSE Security Team on the kernel-default package

SUSE will no longer fix all CVEs in the Linux Kernel anymore, but declare some bug classes as won't fix. Please refer to
[TID 21496](https://support.scc.suse.com/s/redirect/?id=000021496)for more details. SUSE Bugzilla entry:

[1285684](https://bugzilla.suse.com/show_bug.cgi?id=1285684)\[NEW\] No SUSE Security Announcements cross referenced.

### Status of this issue by product and package

Please note that this evaluation state might be work in progress, incomplete or outdated. Also information for service packs in the LTSS phase is only included for issues meeting the LTSS criteria. If in doubt, feel free to contact us for clarification. The updates are grouped by state of their lifecycle. SUSE product lifecycles are documented [on the lifecycle page](https://www.suse.com/lifecycle/).

| Product(s) | Source package | State | 
|---|---|---|
| Products under general support and receiving all security fixes. |  |  | 
| SUSE Linux Enterprise Desktop 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Desktop 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise High Availability Extension 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-rt | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-rt | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP7 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Server 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 16.2 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for NVIDIA 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.2 | kernel-source | Affected | 
| SUSE Linux Micro 6.0 | kernel-default | Affected | 
| SUSE Linux Micro 6.0 | kernel-source | Affected | 
| SUSE Linux Micro 6.0 | kernel-source-rt | Affected | 
| SUSE Linux Micro 6.1 | kernel-default | Affected | 
| SUSE Linux Micro 6.1 | kernel-source | Affected | 
| SUSE Linux Micro 6.1 | kernel-source-rt | Affected | 
| SUSE Linux Micro 6.2 | kernel-default | Affected | 
| SUSE Linux Micro 6.2 | kernel-source | Affected | 
| SUSE Linux Micro Extras 6.0 | kernel-default | Affected | 
| SUSE Linux Micro Extras 6.0 | kernel-source | Affected | 
| SUSE Linux Micro Extras 6.0 | kernel-source-rt | Affected | 
| SUSE Linux Micro Extras 6.1 | kernel-default | Affected | 
| SUSE Linux Micro Extras 6.1 | kernel-source | Affected | 
| SUSE Real Time Module 15 SP7 | kernel-source-rt | Affected | 
| openSUSE Leap 16.0 | kernel-source | Affected | 
| openSUSE Leap 16.1 | kernel-source | Affected | 
| Products under Long Term Service Pack support and receiving important and critical security fixes. |  |  | 
| SUSE Linux Enterprise High Performance Computing 12 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 11 SP4 LTSS EXTREME CORE | kernel-default | Affected | 
| SUSE Linux Enterprise Server 11 SP4 LTSS EXTREME CORE | kernel-source | Affected | 
| SUSE Linux Enterprise Server 12 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 12 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 12 SP5-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP4-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP4-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP5-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP6-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP6-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server LTSS Extended Security 12 SP5 | kernel-default | Affected | 
| SUSE Linux Enterprise Server LTSS Extended Security 12 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP4 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP5 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP6 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP6 | kernel-source | Affected | 
| Products past their end of life and not receiving proactive updates anymore. |  |  | 
| SUSE CaaS Platform 4.0 | kernel-source | Affected | 
| SUSE Enterprise Storage 6 | kernel-source | Affected | 
| SUSE Enterprise Storage 7 | kernel-source | Affected | 
| SUSE Enterprise Storage 7.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 11 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Desktop 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP1-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP1-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP2-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP2-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP3-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP3-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.2 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.2 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP4 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Real Time 15 SP5 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Server 11 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 11 SP4-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP1-BCL | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP1-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP1-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP2-BCL | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP2-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP2-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP3-BCL | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP3-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP3-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP3 | kernel-source | Affected | 
| SUSE Manager Proxy 4.0 | kernel-source | Affected | 
| SUSE Manager Proxy 4.1 | kernel-source | Affected | 
| SUSE Manager Proxy 4.2 | kernel-source | Affected | 
| SUSE Manager Proxy 4.3 | kernel-source | Affected | 
| SUSE Manager Proxy LTS 4.3 | kernel-source | Affected | 
| SUSE Manager Retail Branch Server 4.0 | kernel-source | Affected | 
| SUSE Manager Retail Branch Server 4.1 | kernel-source | Affected | 
| SUSE Manager Retail Branch Server 4.2 | kernel-source | Affected | 
| SUSE Manager Retail Branch Server 4.3 | kernel-source | Affected | 
| SUSE Manager Retail Branch Server LTS 4.3 | kernel-source | Affected | 
| SUSE Manager Server 4.0 | kernel-source | Affected | 
| SUSE Manager Server 4.1 | kernel-source | Affected | 
| SUSE Manager Server 4.2 | kernel-source | Affected | 
| SUSE Manager Server 4.3 | kernel-source | Affected | 
| SUSE Manager Server LTS 4.3 | kernel-source | Affected | 
| SUSE Real Time Module 15 SP4 | kernel-source-rt | Affected | 
| SUSE Real Time Module 15 SP5 | kernel-source-rt | Affected | 
| openSUSE Leap 15.3 | kernel-source | Affected | 
| openSUSE Leap 15.4 | kernel-source | Affected | 
| openSUSE Leap 15.4 | kernel-source-rt | Affected | 
| openSUSE Leap 15.5 | kernel-source | Affected | 
| openSUSE Leap 15.5 | kernel-source-rt | Affected | 
| openSUSE Leap 15.6 | kernel-source | Affected | 

### SUSE Timeline for this CVE

CVE page created: Thu Oct 15 22:39:15 2026
CVE page last modified: Sat Oct 17 15:55:17 2026
