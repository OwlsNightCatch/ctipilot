---
title: Security Research Blog | PWN.AI
author: Octagon Networks
url: https://pwn.ai/blog
hostname: pwn.ai
description: Explore the latest in vulnerability research, AI-powered security, web application security, and threat intelligence.
sitename: PWN.AI
date: "2022-01-10"
tags: ['security research,vulnerability research,web security,AI security,penetration testing,cybersecurity blog']
---
### CVE-2025-54322 (ZERODAY) - Unauthenticated Root RCE affecting ~70,000+ Hosts

A critical zero-day vulnerability, CVE-2025-54322, has been discovered that enables Unauthenticated Root Remote Command Execution (RCE) in devices running Xspeeder's SXZOS firmware. These networking devices, primarily edge routers and SD-WAN appliances, are extensively used, resulting in an estimated 30,000+ hosts being publicly exposed to full system compromise. The vulnerability was autonomously discovered by the pwn.ai platform. This public disclosure follows six months of unsuccessful attempts to notify the vendor, Xspeeder. The technical findings reveal that the exploit bypasses several superficial defenses, including an Nginx user-agent check and a custom Django GateKeeper middleware that attempts to restrict access using a time-sensitive header nonce and session checks.

-rw-r--r--Dec 26, 20255min
