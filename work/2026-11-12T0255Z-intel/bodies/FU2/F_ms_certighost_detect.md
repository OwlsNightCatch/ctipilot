---
title: Detecting CVE-2026-54121 (Certighost) with Microsoft Defender | Microsoft Community Hub
author: EdanZwick
url: https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/detecting-cve-2026-54121-certighost-with-microsoft-defender/4542861
hostname: microsoft.com
description: What is CVE-2026-54121? CVE-2026-54121 is an authentication-bypass vulnerability in Active Directory Certificate Services that allows an attacker to obtain...
sitename: TECHCOMMUNITY.MICROSOFT.COM
date: "2026-07-31"
fingerprint: d7514b894682ced4
---
## On July 14, 2026, Microsoft released an update that fixes CVE-2026-54121, an elevation of privilege vulnerability in Active Directory Certificate Services (AD CS) nicknamed Certighost. We strongly recommend deploying the latest security updates, including this patch, to every AD CS host that runs an Enterprise Certification Authority. This post covers the vulnerability itself and how Microsoft Defender helps you scope it, patch it, and detect it if someone attempts it in your environment.

# What is CVE-2026-54121?

CVE-2026-54121 is an authentication-bypass vulnerability in Active Directory Certificate Services that allows an attacker to obtain certificates for arbitrary domain computer accounts, including Domain Controllers. A valid Domain Controller certificate enables escalation to full domain compromise: it can be used to obtain Kerberos tickets that authenticate the attacker as a Domain Controller. Those tickets can then be used to perform attacks such as DCSync, or to recover the Domain Controller's password hash for later use.

The flaw lies in an AD CS enrollment fallback known as a chase, which occurs when the CA cannot resolve the requester. In such cases, the vulnerable CA contacts a client-supplied Domain Controller, specified in the cdc attribute, to retrieve fresher identity data and incorporates the response into the issued certificate, without verifying that it is communicating with a legitimate Domain Controller. The chase fallback occurs only for templates that require a DNS name, and only on CAs with the EDITF\_ENABLECHASECLIENTDC flag enabled.

A public proof of concept was released on July 24, 2026. Microsoft has not observed confirmed threat-actor exploitation, and the activity seen so far appears consistent with security testing. Organizations with affected AD CS configurations should apply the July 14 security update. Organizations should identify exposed Certificate Services hosts, confirm whether the required environmental conditions exist, enable the recommended AD CS auditing, and monitor for the suspicious authentication and certificate-enrollment activity described below.

[More details about VCE-2026-54121 can be found here](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54121).

# What to do

The response follows a simple order: know your exposure, patch it, instrument it, and watch for the activity.

### 1. Identify affected systems

Certighost affects Windows Server 2012 through Windows Server 2025, including Server Core installations, but several conditions must all be present for a given environment to be exploitable:

- An Enterprise Certification Authority integrated with Active Directory
- Enrollment through the machine certificate template
- A default ms-DS-MachineAccountQuota value, or a machine account already controlled by the attacker
- Network reachability between the Certification Authority and the attacker's host over SMB and LDAP
- A valid domain account, with no administrative privileges required

### 2. Patch

The primary and durable remediation is the July 14, 2026 security update, applied to every AD CS host that runs an Enterprise Certification Authority. The update validates the lookup target before the Certification Authority contacts it, rejecting invalid or attacker-controlled targets before enrollment continues. Nothing else in this post replaces patching. The monitoring below gives you defense in depth and visibility, not an alternative to the fix.

### 3. Turn on AD CS auditing

The certificate request and issuance activity at the center of this attack is only useful to defenders if it is being recorded, and AD CS certificate services auditing is not enabled by default. With it on, the same events power detection and investigation across Microsoft Defender, and Kerberos authentication telemetry requires no additional configuration.

Organizations that have Microsoft Defender for Identity sensors installed on their AD CS servers and have completed the required sensor configuration can typically skip this step, as the necessary Certificate Services auditing settings are already enabled as part of the deployment prerequisites.


Enabling AD CS auditing takes two settings:

**Turn on the Certification Services audit subcategory.** Under Advanced Audit Policy, Object Access, enable success and failure for Certification Services. Set it through Group Policy, or with auditpol:

`auditpol /set /subcategory:"Certification Services" /success:enable /failure:enable`
**Set the Certification Authority audit filter.** In the Certification Authority console this is the Auditing tab; it can also be set with certutil, followed by a service restart:

```
certutil -setreg CA\AuditFilter 127
Restart-Service CertSvc -Force
```
With both in place, the Certification Authority records Security log events for certificate lifecycle operations, including event 4886 when a certificate request is received and event 4887 when a request is approved and a certificate is issued. Each event captures the requester, the template used, and the request disposition. For Certighost, this is the record that makes the abuse visible: a certificate issued for a Domain Controller identity, requested through a machine template by a low-privileged principal, is an issuance pattern that should never occur normally, and these events let defenders detect it, investigate it, and correlate it with the PKINIT authentication and DCSync activity that follow.

For complete guidance, see [Configure Windows event auditing — Microsoft Defender for Identity](https://learn.microsoft.com/defender-for-identity/deploy/configure-windows-event-collection).

### 4. Watch for alerts

Attempts to exploit this vulnerability are detected by Microsoft Defender for Identity with the alert :

**"Potential Certighost (CVE-2026-54121) AD CS abuse."**


The alert fires on the malicious certificate requests crafted to exploit this flaw, the anomalous issuance pattern at the heart of the technique, so you do not need to author a custom rule to catch the core activity. Ensure Defender for Identity is deployed on your domain controllers and AD CS servers and treat this alert as high priority.

Because the exploitation chain touches several stages of an identity attack, you may also see supporting alerts that commonly appear alongside this activity, though on their own they do not confirm a Certighost attempt:

- Security principal reconnaissance (LDAP)
- Suspicious Active Directory Certificate Services abuse tool activity
- Suspected suspicious Kerberos ticket request
- DCSync attack (replication of directory services)

# Learn more

- [CVE-2026-54121 — Security Update Guide, Microsoft (Active Directory Certificate Services Elevation of Privilege Vulnerability)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54121)
- [Configure Windows event auditing — Microsoft Defender for Identity](https://learn.microsoft.com/defender-for-identity/deploy/configure-windows-event-collection)

To stay on top of the latest Defender for Identity capabilities, follow our [What's New](https://learn.microsoft.com/defender-for-identity/whats-new) documentation page.

[EdanZwick](https://techcommunity.microsoft.com/users/edanzwick/449759)

[Microsoft Defender Blog](https://techcommunity.microsoft.com/category/microsoft-security/blog/microsoftthreatprotectionblog)
