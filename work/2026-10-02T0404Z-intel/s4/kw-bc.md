---
title: Kiteworks patches max severity code injection vulnerability
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/kiteworks-patches-max-severity-email-protection-gateway-code-injection-vulnerability/
hostname: bleepingcomputer.com
description: Secure file-sharing software company Kiteworks has released security updates to address 126 vulnerabilities, including a max-severity flaw affecting its Email Protection Gateway (EPG) security solution.
sitename: BleepingComputer
date: "2026-10-01"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Code Injection, Email Protection Gateway, File Sharing, Kiteworks, Vulnerability,virus removal, malware removal, computer help, technical support']
---
Secure file-sharing software company Kiteworks has released security updates to address 126 vulnerabilities, including a max-severity flaw affecting its Email Protection Gateway (EPG) security solution.

EPG is a component of the Kiteworks Private Content Network (PCN), which integrates enterprise email, Managed File Transfer (MFT), file sharing, APIs, and web forms into a single platform.

Formerly known as Accellion, Kiteworks provides services to thousands of global corporations and government agencies, and its Private Content Network has over 100 million end-users.

As part of the [same set of security patches](https://github.com/kiteworks/security-advisories/security), Kiteworks has also fixed 11 critical authentication bypass, admin account takeover, stored cross-site scripting (XSS), improper access control, and improper authentication vulnerabilities in the Core and EPG components.

Tracked as CVE-2026-54154, the maximum-severity vulnerability was reported through Kiteworks' bug bounty program on YesWeHack.

Successful exploitation can let remote threat actors without privileges gain code execution and take over the targeted EPG appliance by exploiting a chain of path traversal, code injection, and missing authentication in low-complexity attacks that don't require user interaction.

The flaw affects all Kiteworks Email Protection Gateway releases before 9.4.1 and is now patched in versions 9.4.1 or later.

"A combination of input-handling flaws in publicly reachable endpoints of the Kiteworks Email Protection Gateway potentially allowed an unauthenticated remote attacker to achieve arbitrary code execution and, by chaining additional local weaknesses, to escalate to full administrative (root) control of the appliance," [Kiteworks explained](https://github.com/kiteworks/security-advisories/security/advisories/GHSA-5xhq-9wq3-rvj6) in a Wednesday advisory.

Last week, Kiteworks [urged customers to shut down their servers](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/) after receiving threat intelligence warning of a potentially imminent zero-day cyberattack.

The company lifted the precautionary advisory on Monday after patching a critical vulnerability and brought all hosted customer systems back online, and said that it found no evidence of compromise or suspicious activity. However, Kiteworks has yet to share additional details on the fixed vulnerability and has not yet assigned a CVE ID for easy tracking.

Threat watchdog Shadowserver currently tracks [nearly 400 Kiteworks instances](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=other_range&d1=2026-09-26&d2=2026-09-27&vendor=kiteworks&type=other-software&model=kiteworks&limit=100&group_by=geo&stacking=stacked) exposed on the Internet, but provides no information on how many have already been patched or are honeypots.

## 
            [Build your security blueprint for AI-powered attacks](https://hubs.li/Q04x67m50)
        

        Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed.

[Save your seat](https://hubs.li/Q04x67m50)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
