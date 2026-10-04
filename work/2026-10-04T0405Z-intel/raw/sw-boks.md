---
title: Fortra Patches Critical Vulnerabilities in BoKS
author: Ionut Arghire
url: https://www.securityweek.com/fortra-patches-critical-vulnerabilities-in-boks/
hostname: securityweek.com
description: The bugs could lead to authentication bypass, shell command execution, and memory corruption.
sitename: SecurityWeek
date: "2026-10-03"
categories: ['Vulnerabilities']
---
**Fortra has released patches for eight vulnerabilities in Core Privileged Access Manager (BoKS), including three critical-severity bugs.**

BoKS provides organizations with central management of Unix and Linux fleets, enabling policy enforcement and access control across accounts.

On Thursday, the company warned that BoKS Manager deployments relying on BoKS keytab for Active Directory service account management are affected by a critical flaw leading to authentication bypass.

Tracked as CVE-2026-79901 (CVSS score of 9.9), the issue exists because AD service account passwords are generated from a “predictable pseudo-random sequence seeded with the current Unix timestamp.”

“An attacker who knows the service principal and can estimate the password-change time can reproduce a limited candidate set and verify candidates offline,” Fortra warned.

The company underlined that an attacker could exploit the flaw if they knew the affected service principal, could estimate the password-change time, and had suitable Kerberos ticket material.

“A standard authenticated Active Directory account can ordinarily request a service ticket for an SPN assigned to the affected account; administrative access to BoKS, the service host, or its keytab is not normally required. A previously captured service ticket can alternatively provide offline verification material,” it said.

The second critical bug, CVE-2026-79898 (CVSS score of 9.1), is a command injection defect in *crlserver* that could allow an authenticated user to substitute shell commands that would be processed as root on the BoKS Master.

According to Fortra, the vulnerability is exploitable through BCC and the WSI REST or SOAP API. BCC and WSI can be accessed over the network without a local *sudo* or *suexec* rule.

The company also resolved CVE-2026-12627 (CVSS score of 9.8), a stack buffer overflow in BoKS’s autoregistration functionality that could allow a remote attacker to trigger memory corruption.

Additionally, Fortra patched five high- and medium-severity BoKS flaws: heap buffer overflows, out-of-bounds read, insecure temporary file, and predictable password generation.

The company makes no mention of any of these vulnerabilities being exploited in the wild. Additional information can be found on Fortra’s [product security](https://www.fortra.com/security/advisories/product-security) page.

**Related:** [Warlock Expands SharePoint Exploitation in Critical Infrastructure Attacks](https://www.securityweek.com/warlock-expands-sharepoint-exploitation-in-critical-infrastructure-attacks/)

**Related:** [Exploited Fortinet FortiMail Zero-Day Calls for Urgent Action](https://www.securityweek.com/exploited-fortinet-fortimail-zero-day-calls-for-urgent-action/)

**Related:** [WatchGuard Patches Critical Fireware OS Code Injection Vulnerability](https://www.securityweek.com/watchguard-patches-critical-fireware-os-code-injection-vulnerability/)

**Related:** [Chrome, Firefox Updates Patch Over 100 Vulnerabilities](https://www.securityweek.com/chrome-firefox-updates-patch-over-100-vulnerabilities/)
