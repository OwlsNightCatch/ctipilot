---
title: Hackers exploit SiteGuard WAF flaw to run commands as admins
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/hackers-exploit-siteguard-waf-flaw-to-run-commands-as-system-root/
hostname: bleepingcomputer.com
description: Attackers are targeting an OS command injection vulnerability in SiteGuard Server Edition that lets them execute commands as root or SYSTEM on affected servers.
sitename: BleepingComputer
date: "2026-10-18"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, RCE, Remote Code Execution, SiteGuard, Vulnerability, WAF,virus removal, malware removal, computer help, technical support']
fingerprint: "86a019de89f16d87"
---
Hackers are exploiting an OS command-injection vulnerability in the SiteGuard Server Edition web application firewall (WAF), allowing them to execute commands with root or SYSTEM privileges on affected machines.

The security issue is tracked as CVE-2026-106931 and affects the statistics feature in host-based WAF instances, which is enabled by default.

SiteGuard is a leading Japanese WAF vendor that claims to protect more than [1.5 million websites](https://www.e-guardian.co.jp/info/2024/20240122.html). Based on WordPress.org statistics, the product is active on [500,000 sites.](https://wordpress.org/plugins/siteguard/)

According to the vendor’s bulletin and a warning from Japan's CERT agency, CVE-2026-106931 has critical severity and is currently being exploited in the wild.

“An OS command injection vulnerability (CVE-2026-106931) has been found in the statistics function of SiteGuard Server Edition. Abuse has already been confirmed,” [reads SiteGuard’s alert](https://www.eg-secure.co.jp/siteguard/news/alert-202610-1).

The attacker’s identity, the victims, the scale of the attacks, and the methods used remain unclear, as neither security advisory provides these details.

According to the vendor, the following versions of the product are vulnerable to CVE-2026-106931:

- SiteGuard Server Edition for Apache httpd, Nginx, and IIS (excluding FreeBSD) versions 2.20 and later, before 8.00 Update 5.
- SiteGuard Server Edition for Apache httpd and Nginx on FreeBSD versions 2.20 and later, before 7.00 Update 6.

Successful exploitation is possible in the above versions if the statistics function is active. IIS editions 3.10 through 4.00 Update 4, inclusive, are not affected, [JPCERT/CC notes](https://jvn.jp/en/jp/JVN88474777/index.html).

For installations that cannot be upgraded, the vendor offers a patch that replaces files used in statistics processing, including for end-of-life versions.

The [vendor warns](https://www.eg-secure.co.jp/siteguard/news/alert-202610-1) that remediation may erase attack traces, and recommends that administrators preserve evidence before updating or patching.

To do this, administrators are instructed to download and retain “Diagnostic information” from the web management interface (Web management screen ‐>Diagnostic information‐> Download diagnostic information)

The vendor said customers with direct support contacts were notified of the flaw earlier, on September 29.

## [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)

Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
