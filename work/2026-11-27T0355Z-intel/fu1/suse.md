---
title: CVE-2026-99362 Common Vulnerabilities and Exposures
url: https://www.suse.com/security/cve/CVE-2026-99362.html
hostname: suse.com
description: Secure your Linux systems from CVE-2026-99362 with SUSE.
sitename: SUSE
date: "2026-01-01"
tags: ['CVE-2026-99362', 'security advisory', 'suse linux', 'suse', 'security', 'cve']
fingerprint: "81fa7852f5bfd4ee"
language: en
image: https://www.suse.com/assets/img/suse-social-sharing-image.png
filedate: "2026-11-27"
---
### Upstream information

#### Description

In the Linux kernel, the following vulnerability has been resolved:
nfsd: preflight SEQUENCE replies before accepting a slot

nfsd4\_sequence() narrows the reply buffer to the session's cached

reply limit before it accepts the slot seqid. A client may negotiate

ca\_maxresponsesize\_cached down to NFSD\_MIN\_HDR\_SEQ\_SZ, and

nfsd4\_alloc\_slot() then gives every slot a zero-length sl\_data\[\]. A

COMPOUND tag can fill that narrowed buffer until it holds the

SEQUENCE opcode but not the status word that follows.

nfsd4\_encode\_operation() returns without running

nfsd4\_encode\_sequence(), so cstate.data\_offset stays zero. It leaves

op->status at nfs\_ok as well, so the COMPOUND is treated as having

succeeded.

nfsd4\_store\_cache\_entry() declines to cache a lone SEQUENCE that

returned an error. That test reads the status the operation

reported, so it passes here. The copy starts at offset zero and

takes the whole reply, RPC and COMPOUND headers included, into the

zero-length sl\_data\[\]. The COMPOUND tag is copied along with it, so

the client picks most of the bytes written past the end of the slot:

BUG: KASAN: slab-out-of-bounds in read\_bytes\_from\_xdr\_buf+0x1bc/0x390

Write of size 80 at addr ffff888003a549cd by task kunit\_try\_catch/24

\_\_asan\_memcpy+0x38/0x60

read\_bytes\_from\_xdr\_buf+0x1bc/0x390

nfsd4\_sequence\_done+0x5b0/0x810

nfs4svc\_encode\_compoundres+0x1bf/0x240

Check that the fixed-size SEQUENCE result, plus room for a following

operation's error status, fits the negotiated limit before narrowing

the buffer and consuming the slot seqid. The slot and its reply

cache are left unchanged, as RFC 8881 Section 2.10.6.1.2 requires of

an error returned from SEQUENCE.

### [SUSE information](https://www.suse.com/c/cve-pages-self-help-security-issues-suse-linux-enterprise/)

Overall state of this security issue: Pending

This issue is currently rated as having [critical](https://www.suse.com/support/security/rating/) severity.

| CVSS v3 Scores |  |  |  | 
|---|---|---|---|
| CVSS detail | CNA (NVD) | Linux Kernel CNA | SUSE | 
|---|---|---|---|
| Base Score | 9.8 | 9.8 | 9.8 | 
| Vector | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 
| Attack Vector | Network | Network | Network | 
| Attack Complexity | Low | Low | Low | 
| Privileges Required | None | None | None | 
| User Interaction | None | None | None | 
| Scope | Unchanged | Unchanged | Unchanged | 
| Confidentiality Impact | High | High | High | 
| Integrity Impact | High | High | High | 
| Availability Impact | High | High | High | 
| CVSSv3 Version | 3.1 | 3.1 | 3.1 | 

| CVSS v4 Scores |  | 
|---|---|
| CVSS detail | SUSE | 
|---|---|
| Base Score | 9 | 
| Vector | CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H | 
| Attack Vector | Network | 
| Attack Complexity | Low | 
| Attack Requirements | Present | 
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
[TID 21496](https://support.scc.suse.com/s/redirect/?id=000021496)for more details. SUSE Bugzilla entries:

[1291223](https://bugzilla.suse.com/show_bug.cgi?id=1291223)\[NEW\],

[1291224](https://bugzilla.suse.com/show_bug.cgi?id=1291224)\[NEW\] No SUSE Security Announcements cross referenced.

### Status of this issue by product and package

Please note that this evaluation state might be work in progress, incomplete or outdated. Also information for service packs in the LTSS phase is only included for issues meeting the LTSS criteria. If in doubt, feel free to contact us for clarification. The updates are grouped by state of their lifecycle. SUSE product lifecycles are documented [on the lifecycle page](https://www.suse.com/lifecycle/).

| Product(s) | Source package | State | 
|---|---|---|
| Products under general support and receiving all security fixes. |  |  | 
| SUSE Linux Enterprise Desktop 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Desktop 15 SP7 | kernel-source | In progress | 
| SUSE Linux Enterprise High Availability Extension 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 15 SP7 | kernel-source | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise High Availability Extension 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-rt | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.4 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.5 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP7 | kernel-source | In progress | 
| SUSE Linux Enterprise Module for Development Tools 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP7 | kernel-source | In progress | 
| SUSE Linux Enterprise Real Time 15 SP7 | kernel-source-rt | In progress | 
| SUSE Linux Enterprise Server 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP7 | kernel-source | In progress | 
| SUSE Linux Enterprise Server 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Server 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for NVIDIA 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for NVIDIA 16.1 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for NVIDIA 16.1 | kernel-source-nvidia | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP7 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP Applications 15 SP7 | kernel-source | In progress | 
| SUSE Linux Enterprise Server for SAP applications 16.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.0 | kernel-source | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Server for SAP applications 16.1 | kernel-source | Affected | 
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
| SUSE Real Time Module 15 SP7 | kernel-source-rt | In progress | 
| openSUSE Leap 16.0 | kernel-source | Affected | 
| openSUSE Leap 16.1 | kernel-source | Affected | 
| openSUSE Leap 16.1 | kernel-source-nvidia | Affected | 
| Products under Long Term Service Pack support and receiving important and critical security fixes. |  |  | 
| SUSE Linux Enterprise High Performance Computing 12 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP4-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 11 SP4 LTSS EXTREME CORE | kernel-default | Not affected | 
| SUSE Linux Enterprise Server 11 SP4 LTSS EXTREME CORE | kernel-source | Not affected | 
| SUSE Linux Enterprise Server 12 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 12 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 12 SP5-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP4-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP4-LTSS | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP5-LTSS | kernel-default | Affected | 
| SUSE Linux Enterprise Server 15 SP5-LTSS | kernel-source | Affected | 
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
| SUSE Linux Enterprise Desktop 11 SP4 | kernel-source | Not affected | 
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
| SUSE Linux Enterprise High Performance Computing 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise High Performance Computing 15 SP5-ESPOS | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.0 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.1 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.2 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.2 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-default | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-rt | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-source | Affected | 
| SUSE Linux Enterprise Micro 5.3 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Basesystem 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP1 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Module for Development Tools 15 SP6 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP2 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP3 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Real Time 15 SP4 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Real Time 15 SP5 | kernel-source-rt | Affected | 
| SUSE Linux Enterprise Server 11 SP4 | kernel-source | Not affected | 
| SUSE Linux Enterprise Server 11 SP4-LTSS | kernel-source | Not affected | 
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
| SUSE Linux Enterprise Server 15 SP4 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP5 | kernel-source | Affected | 
| SUSE Linux Enterprise Server 15 SP6 | kernel-source | Affected | 
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

CVE page created: Mon Nov 23 12:53:13 2026
CVE page last modified: Thu Nov 26 19:58:37 2026
