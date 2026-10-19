---
title: F5, Juniper Networks Patch Critical Vulnerabilities
author: Ionut Arghire
url: https://www.securityweek.com/f5-juniper-networks-patch-critical-vulnerabilities/
hostname: securityweek.com
description: Successful exploitation of some of these issues could lead to remote code execution and full device takeover.
sitename: SecurityWeek
date: "2026-10-16"
categories: ['Vulnerabilities']
fingerprint: "7e7acd1ffeb1d035"
---
**F5 and Juniper Networks have rolled out patches for dozens of vulnerabilities across their products, including critical-severity remote code execution (RCE) flaws.**

Security and application delivery firm F5 [announced](https://my.f5.com/manage/s/article/K000163408) fixes for 11 security defects in NGINX. Among them, CVE-2026-15176 and CVE-2026-93479 are critical-severity bugs that could be exploited without authentication via crafted HTTP requests.

Under certain conditions beyond their control, an unauthenticated attacker could exploit the security holes to trigger a buffer overflow leading to a restart. If ASLR is disabled or can be bypassed, the attacker could achieve RCE.

Another critical issue, CVE-2026-97205, could cause memory corruption or the worker process to terminate, or could lead to RCE if ASLR is disabled.

The remaining vulnerabilities could allow attackers to bypass verification/validation, read sensitive information, spoof request attributes, inject data in proxied requests, cause unbounded memory growth, or access protected paths before authentication.

This week, Juniper Networks [published](https://supportportal.juniper.net/s/global-search/%40uri#sortCriteria=date%20descending&f-sf_primarysourcename=Knowledge&f-sf_articletype=Security%20Advisories&numberOfResults=25) 17 advisories detailing over 150 security defects in Junos OS and Junos OS Evolved, and four bugs in Juniper Cloud-Native Router (JCNR).

Approximately two dozen of these flaws are critical-severity issues that lead to code/command execution with root privileges, complete device takeover, kernel panic, crashes, Routing Engine reboot, service disruption, and buffer overflow (caused by an off-by-one error).

The company also patched multiple high-severity security holes that could lead to RCE, denial-of-service (DoS), and other types of attacks.

F5 and Juniper Networks make no mention of any of these vulnerabilities being exploited in the wild.

**Related:** [Microsoft Patches Two Dozen RCE Flaws in Office](https://www.securityweek.com/microsoft-patches-two-dozen-rce-flaws-in-office/)

**Related:** [Palo Alto Networks Patches PAN-OS Zero-Day Exploited for Remote Code Execution](https://www.securityweek.com/palo-alto-networks-patches-pan-os-zero-day-exploited-for-remote-code-execution/)

**Related:** [Cisco Warns of Exploited Secure Email Gateway Vulnerability](https://www.securityweek.com/cisco-warns-of-exploited-secure-email-gateway-vulnerability/)

**Related:** [Chrome, Firefox Updates Patch 114 Flaws as Mozilla Unveils Firefox Enterprise](https://www.securityweek.com/chrome-firefox-updates-patch-114-flaws-as-mozilla-unveils-firefox-enterprise/)
