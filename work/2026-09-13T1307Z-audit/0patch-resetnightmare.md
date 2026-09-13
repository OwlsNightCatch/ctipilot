---
title: Micropatches released for "ResetNightmare" Windows Kerberos Elevation of Privilege (CVE-2026-27912)
author: Mitja Kolsek
url: https://0patch.com/blog/micropatches-released-for-resetnightmare-windows-kerberos-elevation-of-privilege
hostname: "0patch.com"
description: Tiny reboot-less security patches for critical vulnerabilities in Windows, Microsoft Office, and other Windows products
sitename: "0Patch - Better Security Patches"
date: "2026-09-09"
---
# Micropatches released for "ResetNightmare" Windows Kerberos Elevation of Privilege (CVE-2026-27912)

*[Update 9/9/2026: Our original patches issued on 9/7/2026 blocked administrators from changing passwords for other users. Impact was limited to password change performed via Kerberos, which did not affect typical administrative use cases like password resets on domain controller or "net use" password resets. Today we revoked those patches and issued corrected ones.]*

April 2026 Windows Updates brought a patch for [CVE-2026-27912](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-27912), an elevation of privilege vulnerability allowing an attacker to change any domain user's password, and thereby take over the domain.

Security researcher [Shai Laron](https://www.linkedin.com/in/shailaron/) with [Semperis](https://x.com/SemperisTech) found this vulnerability and reported it to Microsoft. Shai subsequently published a [detailed article](https://www.semperis.com/blog/identity-crisis-novel-vulnerabilities-leading-to-kerberos-downgrade-dos-and-full-domain-takeover/) and shared a [proof-of-concept](https://github.com/Semperis-Community/ResetNightmare) tool that allowed us to reproduce the issue and create patches for legacy Windows users.

### The Vulnerability

The vulnerability lies in the Kerberos Change Password service on aWindows domain controller. A domain user who can modify the `userPrincipalName` attribute  on an account they control can change the password of any other account in the domain, including domain administrator's. The root cause is in the change-password code blindly trusting the user ID (SID) to change the password for (provided by the attacker) and not validating the requestor's identity. 

### Microsoft's Patch

Microsoft fixed the issue by adding a security check to make sure the SID of the user for which the password change was requested matches the SID of the user making such request.

### Our Patch

Our patch is logically identical to Microsoft's.

### Micropatch Availability


Micropatches were written for the following [security-adopted](https://support.0patch.com/hc/en-us/articles/4403751356050-Which-Windows-products-has-0patch-security-adopted) Windows versions:

1. Windows Server 2008 R2 - fully updated with no ESU, with ESU 1, ~~ESU 2*~~ , ESU 3 or ESU 4
2. Windows Server 2012 - fully updated with no ESU, with ESU 1 or ESU 2
3. Windows Server 2012 R2 - fully updated with no ESU, with ESU 1 or ESU 2


(* For some reason, Windows Server 2008 R2 with ESU2 applied is not vulnerable to this issue.)

Micropatches have already been distributed to, and applied on, all affected online computers with 0patch Agent in PRO or Enterprise accounts (unless Enterprise group settings prevented that).

New vulnerabilities like these are discovered regularly, and attackers can eventually learn about and exploit them. If you're using Windows that aren't receiving official security updates anymore, 0patch will help prevent these vulnerabilities from being exploited on your computers - and you won't even have to know or care about these things.

We'd like to thank [Shai Laron](https://www.linkedin.com/in/shailaron/) with [Semperis](https://x.com/SemperisTech) for sharing their analysis and POC, which allowed us to create patches for Windows versions that are no longer receiving official updates from Microsoft.

If you're new to 0patch, create a free account in [0patch Central](https://central.0patch.com), start a free trial, then install and register 0patch Agent. Everything else will happen automatically. No computer reboot will be needed.

**Did you know 0patch security-adopted Windows 10 and Office 2016 and 2019 when they went out of support in October 2025, allowing you to keep using them for at least 3 more years (5 years for Windows 10)?** [Read more about it here](https://blog.0patch.com/2024/06/long-live-windows-10-with-0patch.html) **and** [here](https://blog.0patch.com/2025/08/end-of-security-for-microsoft-office.html)**.** 

**Note that we will soon security-adopt the following products:**

- **Windows 10 22H2 with Extended Security Updates year 1: October 2026**
- **Windows Server 2012 with Extended Security Updates year 3: October 2026**
- **Windows Server 2012 R2 with Extended Security Updates year 3: October 2026**
- **Microsoft Office 2021: October 2026 -**  [Read more about it here](https://0patch.com/blog/end-of-security-for-microsoft-office-2021-not-with-0patch)
- **Windows 11 23H2 (E): November 2026**
- **Windows Server 2016: January 2027**

To learn more about 0patch, please visit our [Help Center](https://0patch.zendesk.com/hc/en-us).

[PreviousKeeping Microsoft Office 2021 Secure For 3 More Years](https://0patch.com/blog/end-of-security-for-microsoft-office-2021-not-with-0patch)
