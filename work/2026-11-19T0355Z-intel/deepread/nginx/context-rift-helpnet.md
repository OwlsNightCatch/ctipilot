---
title: Attackers are exploiting critical NGINX vulnerability (CVE-2026-42945) - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/05/18/ngnix-vulnerability-exploited-cve-2026-42945/
hostname: helpnetsecurity.com
description: A critical NGINX vulnerability (CVE-2026-42945) that was disclosed last week is being exploited by attackers, according to VulnCheck.
sitename: Help Net Security
date: "2026-05-18"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['exploit', 'NGINX', 'PoC', 'VulnCheck', 'vulnerability', 'exploit', 'NGINX', 'PoC', 'VulnCheck', 'vulnerability']
fingerprint: bd380449e0a6d486
---
# Attackers are exploiting critical NGINX vulnerability (CVE-2026-42945)

A critical NGINX vulnerability (CVE-2026-42945) disclosed last week is being exploited by attackers, VulnCheck security researcher Patrick Garrity revealed on Saturday.

The vulnerability, dubbed NGINX Rift, can be reliably exploited to trigger a denial-of-service condition and can potentially allow for unauthenticated remote code execution, all achievable by sending a specially crafted HTTP request to a vulnerable NGINX instance.

### What is NGINX?

NGINX is the most widely deployed web server and, as such, it’s one of the fundamental pieces of modern web infrastructure. It can also play other roles: load balancer, reverse proxy, and HTTP cache.

Its development is overseen by the networking and application delivery company F5, which maintains and releases the open-source version (NGINX Open Source), offers the commercial NGINX Plus version, and has integrated NGINX into its various application delivery and security solutions.

### About CVE-2026-42945

CVE-2026-42945 is a memory corruption vulnerability that [affects](https://my.f5.com/manage/s/article/K000161019) NGINX Open Source (versions 0.6.27 through 1.30.0) and NGINX Plus (vR32 through R36). It also affects some of F5’s products that incorporate the software, such as NGINX Ingress Controller, F5 WAF for NGINX, and others.

“A bug in the **ngx\_http\_rewrite\_module** lets a remote, unauthenticated attacker corrupt the heap of an NGINX worker process by sending crafted URI. The trigger is a common configuration pattern: a **rewrite** directive with an unnamed regex capture (**$1, $2**) and a replacement string that contains a question mark, followed by another **rewrite**, **if**, or **set** directive,” the researchers who unearthed the vulnerability [explained](https://depthfirst.com/nginx-rift).

“When that pattern is present, NGINX computes the destination buffer using one set of escaping assumptions and then writes to it using another. The write runs past the allocated buffer, producing deterministic memory corruption. The bytes written past the allocation are derived from the attacker’s URI, so the corruption is shaped by the attacker rather than random. Repeated requests can also be used to keep workers in a crash loop and degrade availability for every site served by the instance.”

### PoC and exploitation

CVE-2026-42945, along with four other security issues, was discovered by Depthfirst researchers with the help of the company’s AI-native vulnerability detection platform. Of the five, CVE-2026-42945 was the most critical.

Once F5 released fixes and the security advisory, Depthfirst researchers published technical details and a [proof-of-concept (PoC) exploit](https://github.com/depthfirstdisclosures/nginx-rift).

[According to](https://www.linkedin.com/posts/patrickmgarrity_cybersecurity-threatintelligence-riskmanagement-share-7461369931851517952-PBjV/) Garrity, VulnCheck’s canary systems began flagging exploitiation attempts on May 16, three days after the vulnerability and the PoC had been made public.

The effectiveness of these attempts depends on the targeted system.

While DoS can be achieved on default NGINX configurations, both VulnCheck and security researcher [Kevin Beaumont](https://cyberplace.social/@GossiTheDog/116572643931253811) pointed out that attackers can achieve code execution if they manage to disable address space layout randomization (ASLR) on the target server.

“A further caveat is that the target server has to be running a specific rewrite configuration to be vulnerable, so not every NGINX instance is exploitable. Our Censys query surfaces roughly 5.7M internet-exposed NGINX servers running a potentially vulnerable version, though the truly exploitable population is likely to be a much smaller subset of those,” the VulnCheck Initial Access team [noted](https://docs.vulncheck.com/initial-access/2026-05-15#cve-2026-42945-nginx-ngx_http_rewrite_module-heap-based-buffer-overflow-queries-and-signatures-only).

### Fixes

So far, F5 fixed the vulnerability in:

- NGINX Open Source – versions 1.31.0 and 1.30.1
- NGINX Plus – versions R36 P4 and R32 P6
- F5 WAF for NGINX v5.13.0
- F5 DoS for NGINX v4.9.0

It has also provided a mitigation: using named captures instead of unnamed captures in **rewrite** definitions.

[AlmaLinux](https://almalinux.org/blog/2026-05-13-nginx-rift-cve-2026-42945/), [Ubuntu](https://ubuntu.com/security/CVE-2026-42945) and [Debian](https://security-tracker.debian.org/tracker/CVE-2026-42945) developers have begun releasing patched nginx packages.

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
