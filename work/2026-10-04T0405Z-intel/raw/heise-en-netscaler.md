---
title: "Netscaler admins beware: Zero-day causes crashes and code execution"
author: Heise Online; Dr Christopher Kunz
url: https://www.heise.de/en/news/Netscaler-admins-beware-Zero-day-causes-crashes-and-code-execution-11474996.html
hostname: heise.de
description: Security researchers and administrators are reporting massive spontaneous reboots of affected devices. These were on the latest patch level.
sitename: Heise Online
date: "2026-10-03"
categories: ['IT']
tags: ['Citrix, Citrix NetScaler ADC, Citrix Netscaler Gateway, Exploit, IT, Security']
---
# Netscaler admins beware: Zero-day causes crashes and code execution

Security researchers and administrators are reporting massive spontaneous reboots of affected devices. These were on the latest patch level.

Since the evening of October 2, 2026, an exploit for a new security vulnerability on Citrix NetScaler devices has apparently been circulating. The manufacturer warns in a blog post, security researchers claim to have observed malware on their test devices. Patches are not yet available at the moment.

According to British security expert Kevin Beaumont, it could be an evasion of the fix for the vulnerability disclosed last week, “Pitscaler” (CVE-2026-88771 / CVE-2026-88772). He writes: “So on one of the honeypots it’s running a downloaded (malware) binary. Both *[honeypots, ed.]* were patched, so new vuln.” It is apparently exploitable on the recently released latest version of the NetScaler operating system -- a zero-day.

Other experts second this: “the watchTowr Labs team has now successfully reproduced this vulnerability.” This means that just one week after the last fatal vulnerability, an exploit for NetScaler systems capable of injecting malware and attacking corporate networks is once again in circulation. The exploit can likely be executed by sending a massive number of SAML requests to a vulnerable device. Reddit users are discussing the vulnerability and its exploitation in an [extensive discussion thread](https://www.reddit.com/r/Citrix/comments/1wvwuno/vulnerability_scans_causing_netscaler_reboots/).

Videos by heise

### Citrix is investigating -- no patch yet

The manufacturer also commented surprisingly quickly [in its blog](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/). However, it names neither effective countermeasures nor provides a solution via patch. Affected parties should contact customer support. Until a patch for the zero-day is available, only increased vigilance on the holiday weekend will help. We will continuously update this report.

Just a few days ago, a [zero-day attack on Citrix appliances](https://heise.de/news/Sicherheitsforscher-warnen-Neue-Zero-Day-Exploits-in-Citrix-Netscaler-11467200.html?from-en=1) sweetened the weekend for admins and security researchers worldwide, and before that in [August](https://heise.de/news/Citrix-stopft-kritische-Anmeldungsumgehung-in-Netscaler-ADC-und-Gateway-11420304.html?from-en=1).

([cku](mailto:cku@heise.de))
