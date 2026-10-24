---
title: PaperCut NG/MF Security Bulletin (24 Sep 2026)
url: https://www.papercut.com/kb/Main/security-bulletin-sep-2026/
hostname: papercut.com
description: September Security Bulletin covering multiple disclosed vulnerabilities that addressed in the recent versions of PaperCut products.
sitename: PaperCut
date: "2026-10-13"
fingerprint: afe9ddaa2e26466b
---
- 
                  Help Center home
- ## Release notes
- ## System requirements

# PaperCut NG/MF Security Bulletin (24 Sep 2026)

Last updated October 13, 2026

## Summary

At PaperCut, we are consistently working on improving the security posture of our products. This ongoing commitment involves regular internal audits, proactive “pattern hunting” in our codebase, and collaboration with external security researchers. This process is designed to identify and remediate potential issues before they can be exploited.

PaperCut prioritizes the safety of our customers through a responsible disclosure policy. As part of this approach, you may observe specific CVE identifiers appearing in our product release notes before a formal security bulletin or a CVE database entry is fully published. This “fix-first” strategy allows us to provide immediate protection while delaying the publication of technical details that could be used to develop exploits. Full documentation is published only when we are confident that disclosure no longer poses an immediate risk to our customer base.

This bulletin addresses the following security vulnerabilities affecting PaperCut NG/MF, and PaperCut Hive Embedded Application for Ricoh.

### PaperCut NG/MF:

**NOTE: If you have already upgraded to the latest release (26.0.5, 25.0.13, 24.1.11) the issues are already addressed.**

- [CVE-2026-14780](https://www.cve.org/CVERecord?id=CVE-2026-14780): Remote Code Execution via Scripting Subsystem
- [CVE-2026-82077](https://www.cve.org/CVERecord?id=CVE-2026-82077): Remote Code Execution via Scan2Fax
- [CVE-2026-87739](https://www.cve.org/CVERecord?id=CVE-2026-87739): User permissions are not evaluated on report generation

### PaperCut Hive:

- [CVE-2026-11744](https://www.cve.org/CVERecord?id=CVE-2026-11744): Embedded Ricoh App: Javascript injection

**Recommendation:**

- PaperCut NG/MF customers should [upgrade](https://www.papercut.com/help/manuals/ng-mf/common/upgrade/) to version 26.0.5 (or 25.0.13 on the 25.x branch, 24.1.11 on the 24.x branch) or later.
- PaperCut Hive Embedded Application for Ricoh customers should upgrade to version 2.3.0 or later.

## Security issues addressed

| **CVE** | **Notes** | **CVSS rating and vector** | 
| [**CVE-2026-14780**](https://www.cve.org/CVERecord?id=CVE-2026-14780) PaperCut NG/MF: Remote Code Execution via Scripting Subsystem | Where the optional Print and Device Scripting feature is enabled, an attacker who already holds **authenticated** administrator access to the PaperCut administration interface could run code on the underlying application server operating system. Not exploitable by an unauthenticated user. Print and Device Scripting has been disabled by default since 22.1.1. **Vulnerability Type:** CWE-94 Improper Control of Generation of Code ('Code Injection') **Impact:** Remote code execution on the PaperCut application server **Fixed in:** PaperCut NG/MF **26.0.2** (released 30 June 2026); **25.0.12** for the 25.x branch (released 27 August 2026); **24.1.11** for the 24.x branch (released 11 October 2026); **Reported by:** Mark Fox \<mark.fox@blacklanternsecurity.com> | 7.5 (HIGH) [CVSS:4.0/AV:N/AC:L/AT:P/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:P/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N) | 
| **CVE-2026-82077** PaperCut NG/MF: Remote Code Execution via Scan2Fax | An improper limitation of a pathname to a restricted directory (path traversal) vulnerability in the Scan-to-Fax component of PaperCut NG and PaperCut MF allows an **authenticated** administrator to execute arbitrary commands on the underlying host via crafted fax provider settings. **Vulnerability Type:** CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), CWE-78 Improper neutralization of special elements used in an OS command ('OS command injection') **Impact:** Remote code execution on the PaperCut application server **Fixed in:** PaperCut NG/MF **26.0.5**; **25.0.13** for the 25.x branch; **24.1.10** for the 24.x branch. **Reported by:** Piotr Bazydlo (@chudyPB) of watchTowr | 7.3 (HIGH) [CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N/E:P](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N/E:P) | 
| **CVE-2026-87739** PaperCut NG/MF: User permissions are not evaluated on report generation | An improper authentication vulnerability in PaperCut NG/MF allows an unauthenticated, remote attacker to trigger report generation. By submitting report generation requests without valid credentials, an attacker can generate reports and gain unauthorized access to sensitive information. **Vulnerability Type:** CWE-639 Authorization Bypass Through User-Controlled Key **Impact:** Information disclosure **Fixed in:** PaperCut NG/MF **26.0.5**; **25.0.13** for the 25.x branch; **24.1.10** for the 24.x branch. **Reported by:** internal discovery through the security uplift program | 6.9 (MEDIUM) [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:L/SI:N/SA:N/AU:Y](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:L/SI:N/SA:N/AU:Y) | 
| [**CVE-2026-11744**](https://www.cve.org/CVERecord?id=CVE-2026-11744) PaperCut Hive Embedded Ricoh App: Javascript injection | An input validation vulnerability exists in the PaperCut Hive embedded application for Ricoh devices. The application fails to properly sanitize input received during the NFC card reading process before passing it to the application's web view interface. A local attacker with **physical access** to the device and a specially crafted NFC card or emulator could exploit this flaw to execute arbitrary code within the context of the *embedded* application's user interface. This could result in unauthorized actions or information disclosure. **Vulnerability Type:** CWE-79 Improper neutralization of input during web page generation ('cross-site scripting') **Impact:** Arbitrary javascript code execution within the embedded browser sandbox on Ricoh devices. **Fixed in:** PaperCut Hive Embedded Application for Ricoh **2.3.0** (upgradable via one-click install) **Reported by**: internal discovery through the AI assisted security uplift program | 3.8 (LOW) [CVSS:4.0/AV:P/AC:L/AT:N/PR:N/UI:N/VC:H/VI:L/VA:N/SC:H/SI:L/SA:N/E:U](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:P/AC:L/AT:N/PR:N/UI:N/VC:H/VI:L/VA:N/SC:H/SI:L/SA:N/E:U) | 

## Who is impacted

#### PaperCut NG/MF

- **CVE-2026-14780 (PaperCut NG/MF):** You are potentially affected if you are running PaperCut NG/MF earlier than 26.0.2 (or 25.0.12 on the 25.x branch, 24.1.11 on the 24.x branch) **and** have the optional Print and Device Scripting feature enabled. This feature has been off by default since version 22.1.1, so most customers are not affected. Exploitation also requires the attacker to already hold authenticated administrator access to your PaperCut administration interface; it is not exploitable by an unauthenticated user.
- **CVE-2026-82077 (PaperCut NG/MF):** You are affected if you are running PaperCut NG/MF earlier than 26.0.5 (or 25.0.13 on the 25.x branch, 24.1.10 on the 24.x branch). The exploitation requires the attacker to already hold authenticated administrator access to your PaperCut administration interface: it is not exploitable by an unauthenticated user.
- **CVE-2026-87739 (PaperCut NG/MF):** You are affected if you are running PaperCut NG/MF earlier than 26.0.5 (or 25.0.13 on the 25.x branch, 24.1.10 on the 24.x branch).

#### PaperCut Hive

- **CVE-2026-11744 (PaperCut Hive Embedded Ricoh App):** You are affected if you are running Ricoh devices with PaperCut Hive Embedded Application earlier than 2.3.0 installed. The exploitation *requires* **physical access** to the card reader.

If none of the above applies to your environment, no action is required.

## Steps to resolve

PaperCut recommends that all customers upgrade to the latest version of PaperCut NG or MF inline with their upgrade cycle.

**CVE-2026-14780, CVE-2026-82077, and CVE-2026-82077 (PaperCut NG/MF)**

- [Upgrade](https://www.papercut.com/help/manuals/ng-mf/common/upgrade/) to PaperCut NG/MF 26.0.5 (or 25.0.13 on the 25.x branch, 24.1.11 on the 24.x branch) or later.

**CVE-2026-11744 (PaperCut Hive Embedded Ricoh App)**

- [Upgrade](https://www.papercut.com/kb/PaperCutPocketHive/upgrading-the-ricoh-full-embedded-app/#installation-of-app-version-2xx) PaperCut Hive Embedded Ricoh App to 2.3.0.

## FAQs

Q Has this been exploited?

We have no evidence that any of these issues have been exploited. We continually monitor for signs of exploitation and will update this bulletin if that changes.

Q How were these issues found?

Through a combination of our own internal security processes and reports from external security researchers under our responsible disclosure policy.

Q Why am I only hearing about this now if some of these fixes shipped earlier?

Some of these fixes were included in earlier scheduled releases as part of our normal development process. We deliberately hold back publication of technical detail until we're confident the majority of affected customers have had the opportunity to update, to reduce the window in which that detail could be used against customers who haven't yet applied the fix.

Q Do I need to upgrade if I'm not using the affected feature?

No. Where a complete configuration-based mitigation is available (see Steps to Resolve above), you do not need to upgrade immediately, though we still recommend upgrading at your next scheduled maintenance window.

Q I am running PaperCut Hive Embedded Ricoh App v1. Do I still need to upgrade?

The v1 versions of PaperCut Hive Embedded Ricoh App are not vulnerable, but you may want to still upgrade to the latest v2 version for other reasons.

## Security notifications

To stay informed about high impact security updates please subscribe to our [<u>Security notifications sign-up form</u>](https://www.papercut.com/contact/security/#subscribe).

## Updates

| Date | Update/action | 
| 24 September, 2026 (AEST) | Published the initial Security Bulletin. | 
| 24 September, 2026 (AEST) | Re-arranged sections to make it clear what parts relate to PaperCut NG/MF and which are for PaperCut Hive. | 
| 27 September, 2026 (AEST) | Corrected a typo in one of the references to Ricoh App version 2.3.0. | 
| 13 October, 2026 (AEST) | Updated back ported versions to outline the v24 fix versions. | 

*Category:* 
            [Security Bulletins](https://www.papercut.com/kb/Category/SecurityBulletins/)

*Subcategory:* 
        
        
                [Security and Privacy](https://www.papercut.com/kb/Category/SecurityAndPrivacy/)

## Comments

Comments are not available in this preview environment. On papercut.com, this space shows the live Disqus comment thread for this page.
