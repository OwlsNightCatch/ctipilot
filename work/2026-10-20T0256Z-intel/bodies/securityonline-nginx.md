---
title: F5 Patches Three NGINX Vulnerabilities Allowing Memory Corruption and Remote Code Execution
author: Do Son
url: https://securityonline.info/f5-patches-three-critical-nginx-vulnerabilities/
hostname: securityonline.info
description: TL;DR F5 published three security advisories on October 14, 2026, addressing high-risk NGINX vulnerabilities in NGINX Plus and NGINX Open Source. Tracked as CVE-2026-97205, CVE-2026-93479, and CVE…
sitename: Daily CyberSecurity
date: "2026-10-14"
categories: ['Vulnerability Report']
tags: ['CVE-2026-15176', 'CVE-2026-93479', 'CVE-2026-97205', 'F5', 'nginx', 'NGINX vulnerabilities']
fingerprint: b53c8f49e6a4d786
---
## TL;DR

F5 published three security advisories on October 14, 2026, addressing high-risk NGINX vulnerabilities in NGINX Plus and NGINX Open Source. Tracked as [CVE-2026-97205](https://securityonline.info/cve-watchtower/cve-2026-97205/), [CVE-2026-93479](https://securityonline.info/cve-watchtower/cve-2026-93479/), and [CVE-2026-15176](https://securityonline.info/cve-watchtower/cve-2026-15176/), each flaw carries a CVSS v3.1 score of 8.1 (High). Moreover, each flaw has a CVSS v4.0 score of 9.2 (Critical). Unauthenticated attackers can exploit these memory corruption bugs to crash worker processes or execute arbitrary code.

- **Product:** F5 NGINX Plus
- **Vulnerabilities:** 3 flaws ([CVE-2026-97205](https://securityonline.info/cve-watchtower/cve-2026-97205), [CVE-2026-93479](https://securityonline.info/cve-watchtower/cve-2026-93479), [CVE-2026-15176](https://securityonline.info/cve-watchtower/cve-2026-15176))
- **Highest severity:** 9.2 (Critical · CVSSv4)
- **Worst impact:** NGINX ngx\_http\_core\_module
- **Status:** No confirmed exploitation yet; patches available
- **Action:** Update to 37.1.0.1, 37.0.5.1, 1.31.7, 1.30.6 now

| CVE | CVSS (CVSSv4) | Type | Fixed in | Status | 
|---|---|---|---|---|
| [CVE-2026-97205](https://securityonline.info/cve-watchtower/cve-2026-97205) | 9.2 | NGINX ngx\_http\_core\_module | 37.1.0.1, 37.0.5.1, 1.31.7 (+1) | Not exploited | 
| [CVE-2026-93479](https://securityonline.info/cve-watchtower/cve-2026-93479) | 9.2 | NGINX map directive and regex matching | 37.1.0.1, 37.0.5.1, 1.31.7 (+1) | Not exploited | 
| [CVE-2026-15176](https://securityonline.info/cve-watchtower/cve-2026-15176) | 9.2 | NGINX ngx\_http\_core\_module | 37.1.0.1, 37.0.5.1, 1.31.7 (+1) | Not exploited | 

**F5**CVE's exploit risk spike before it becomes a headline.

[Get EPSS spike alerts](https://securityonline.info/cve-alerts/)

## Why These F5 NGINX Vulnerabilities Matter

NGINX Open Source and NGINX Plus power millions of reverse proxies, API gateways, and Kubernetes ingress controllers worldwide. However, all three newly disclosed NGINX vulnerabilities expose the data plane to remote denial-of-service (DoS) and potential code execution. In every advisory, F5 warns that “attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.” Currently, F5 has confirmed no public proof-of-concept exploit code for any of the three flaws. Additionally, there is no active exploitation in the wild for any of the three flaws.

## How the Attacks Work

### Use-After-Free in Asynchronous File I/O and SSI (CVE-2026-97205)

Reported by researcher Cyberlanc3r and tracked internally as NPS-187, [F5 security advisory K000162608](https://my.f5.com/manage/s/article/K000162608) for CVE-2026-97205 details a Use-After-Free (CWE-416) flaw in the `ngx_http_core_module` module. According to the advisory, “when asynchronous file I/O (AIO) is enabled in certain configurations, processing a Server Side Includes (SSI) page containing include virtual commands may trigger a Use-After-Free (UAF) in the NGINX worker process.” Consequently, this condition corrupts memory or terminates the worker process.

### Heap Buffer Overflow in Regex Map Directives (CVE-2026-93479)

Reported by Matt Suiche of Tolmo, Inc. and Mateusz Gierblinski, [F5 security advisory K000162607](https://my.f5.com/manage/s/article/K000162607) for CVE-2026-93479 (NPS-180) addresses a heap-based buffer overflow (CWE-122). The flaw occurs when a `map` directive uses regular expression matching. It also happens if the `root` directive or access log references regex capture variables before referencing the map output variable. In addition, using a non-cacheable variable in a string expression can also trigger the same heap overflow. This occurs when processing crafted HTTP requests.

### Heap Buffer Overflow in Alias and Rewrite Directives (CVE-2026-15176)

Discovered internally by F5 and tracked as NPS-139, [F5 security advisory K000162416](https://my.f5.com/manage/s/article/K000162416) for CVE-2026-15176 describes another heap-based buffer overflow (CWE-122) in `ngx_http_core_module`. Specifically, the bug triggers when a location block combines the `alias` directive with `rewrite`. This happens along with a `set` or `return` directive referencing `$request_filename`. Moreover, referencing `$request_filename` inside an access `log_format` directive also exposes the worker process to a heap overflow.

## Affected Products and Versions

While BIG-IP, BIG-IQ, F5OS, and F5 Distributed Cloud Services are unaffected, the following software branches are vulnerable across the three advisories:

- **NGINX Open Source:** 1.31.0 through 1.31.6 and 1.30.0 through 1.30.5 (plus legacy 1.0.0-1.30.5 and 0.1.29-0.9.9 for CVE-2026-15176).
- **NGINX Plus:** 37.0.0 through 37.0.4 and R33 through R36.
- **Ecosystem Components:** NGINX Instance Manager (2.18.0-2.23.0), F5 WAF for NGINX (5.9.0-5.15.0), NGINX App Protect WAF (4.12.0-4.16.0 and 5.4.0-5.8.0 for CVE-2026-97205 and CVE-2026-15176), F5 DoS for NGINX (4.8.0-4.10.0), NGINX App Protect DoS (4.5.0-4.7.0 for CVE-2026-97205 and CVE-2026-15176), NGINX Gateway Fabric (2.1.0-2.7.2, plus 1.5.0-1.6.2 for CVE-2026-93479), and NGINX Ingress Controller (5.6.0-5.6.3, plus 5.0.0-5.6.3, 4.0.0-4.0.1, 3.7.1-3.7.2, and 2026-lts-r3 to r8 for CVE-2026-93479).

## Patch Details and Mitigation Steps

Administrators should eliminate these F5 NGINX vulnerabilities by upgrading to NGINX Open Source 1.31.7 or 1.30.6. They should also upgrade to NGINX Plus 37.1.0.1 or 37.0.5.1. Fixes are also available in NGINX Instance Manager 2.24.0, F5 WAF for NGINX 5.16.0 and 5.14.2, F5 DoS for NGINX 4.11.0, NGINX Gateway Fabric 2.8.0, and NGINX Ingress Controller 5.7.0.

If teams cannot patch immediately, F5 provides targeted configuration workarounds for each flaw. To mitigate CVE-2026-97205, set `aio off;` or `ssi off;` in configuration files. For CVE-2026-93479, replace unnamed regex captures with named captures restricted to the regex match block. Finally, for CVE-2026-15176, avoid using the `alias` directive in location blocks or remove references to the `$request_filename` variable.

#### Support Our Threat Intelligence

Find our vulnerability reports and weekly recaps helpful? Support our work today and unlock a **100% ad-free** reading experience!
