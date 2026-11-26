---
title: Juniper Warns of Active Exploitation in CVSS 9.8 Session Smart Router Vulnerabilities
author: Do Son
url: https://securityonline.info/juniper-session-smart-router-vulnerabilities/
hostname: securityonline.info
description: Juniper warns of active exploitation targeting CVE-2026-103406 (CVSS 9.8), one of 18 patched Session Smart Router vulnerabilities. Update now.
sitename: Daily CyberSecurity
date: "2026-10-28"
categories: ['Vulnerability News']
tags: ['CVE-2026-103406', 'CVE-2026-103409', 'Juniper Networks', 'network-security', 'SD-WAN', 'Session Smart Conductor', 'Session Smart Router']
fingerprint: "3e2b4f1df560f600"
language: en
image: https://securityonline.info/wp-content/uploads/2026/10/juniper-session-smart-router-conductor-cve-2026-103406-exploited.webp
pagetype: article
filedate: "2026-11-26"
---
## TL;DR

Juniper Networks has patched 18 Session Smart Router vulnerabilities in its October 28 security bulletin, JSA112183. Two critical flaws score 9.8 on CVSS v3.1 and need no login. The bugs also affect Session Smart Conductor, the management platform for these routers.

Unauthenticated attackers could run commands on the Conductor or gain admin rights on the router. Juniper’s own testing found all 18 issues. Upgrade to 7.0.5, 7.1.7 or 7.2.3 now.

- **CVE:** [CVE-2026-103406](https://securityonline.info/cve-watchtower/cve-2026-103406/)
- **CVSS:** 9.8 (Critical · CVSSv3)
- **Product:** Juniper Networks Session Smart Conductor
- **Affected:** \< 7.0.5, 7.1.0, 7.2.0
- **Impact:** Session Smart Conductor: An unauthenticated attacker causes arbitrary command execution during key management.
- **Status:** Exploited in the wild
- **Patched in:** 7.0.5, 7.1.7, 7.2.3
- **EPSS:** 0.9% (30-day)
- **Action:** Update to 7.0.5, 7.1.7, 7.2.3 now

**Juniper**CVE the moment it's exploited.

[Get free email alerts](https://securityonline.info/cve-alerts/)

## Why It Matters

Session Smart Router powers Juniper’s SD-WAN deployments, while Conductor manages the whole router fleet. As a result, a compromised Conductor could put many sites at risk. Juniper rates the bulletin “Critical” and says the issues “affect all versions” of both products.

## How the Attack Works

### Critical flaws

[CVE-2026-103406](https://securityonline.info/cve-watchtower/cve-2026-103406/) hits Session Smart Conductor. According to [Juniper](https://supportportal.juniper.net/s/article/2026-10-On-Demand-Security-Bulletin-Session-Smart-Router-and-Session-Smart-Conductor-Multiple-internally-discovered-vulnerabilities-resolved?), “an unauthenticated attacker causes arbitrary command execution during key management.” Meanwhile, [CVE-2026-103409](https://securityonline.info/cve-watchtower/cve-2026-103409/) affects the router. There, “an attacker obtains administrative privileges when an unauthenticated internal endpoint is accessed.”

### High severity flaws

Six more bugs score 8.8. Most need a low-privileged account, yet they can lead to root file overwrites, code execution or privilege escalation. For example, one flaw stems from a “lack of integrity verification in cache files.” Another, [CVE-2026-103408](https://securityonline.info/cve-watchtower/cve-2026-103408/), enables remote code execution through crafted DHCP options from an adjacent network.

The remaining Session Smart Router vulnerabilities range from 3.7 to 7.5. They cover crashes, memory errors and HTTP response splitting.

## Affected Versions

According to the Juniper security bulletin, all Session Smart Router and Session Smart Conductor versions before 7.0.5, 7.1.7 and 7.2.3 are affected.

## Patch and Mitigation

Install 7.0.5, 7.1.7, 7.2.3 or any later release. Juniper notes, “There are no known workarounds for all of these issues.” Until you patch these Session Smart Router vulnerabilities, limit access to Conductor and router management interfaces.

Juniper SIRT “is not aware of any malicious exploitation of these vulnerabilities.”

## November 24 Update: Active Exploitation of CVE-2026-103406

However, Juniper Networks updated security bulletin JSA112183 on November 24 to confirm active attacks in the wild. Specifically, threat actors are now targeting CVE-2026-103406, the critical command execution vulnerability in Session Smart Conductor. In the revised advisory, Juniper warned, “At least one instance of malicious exploitation of CVE-2026-103406 has been reported to the Juniper SIRT.” “Customers are encouraged to upgrade to a fixed release as soon as possible and in the meantime take steps to mitigate this vulnerability.” Therefore, administrators must immediately upgrade affected deployments to version 7.0.5, 7.1.7, or 7.2.3. Meanwhile, security teams should strictly restrict network access to all Conductor management interfaces until patching is complete.

#### Support Our Threat Intelligence

Find our vulnerability reports and weekly recaps helpful? Support our work today and unlock a **100% ad-free** reading experience!
