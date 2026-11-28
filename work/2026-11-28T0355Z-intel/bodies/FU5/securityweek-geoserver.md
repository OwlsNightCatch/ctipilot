---
title: Two Newly Disclosed GeoServer Vulnerabilities Under Attack
author: Eduard Kovacs
url: https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/
hostname: securityweek.com
description: Attackers are probing GeoServer instances for two high-severity flaws that can be chained with other bugs for unauthenticated RCE.
sitename: SecurityWeek
date: "2026-11-25"
categories: ['Vulnerabilities']
tags: ['exploited', 'GeoServer', 'RCE', 'vulnerability']
fingerprint: "64e32497b803d627"
language: en
image: https://www.securityweek.com/wp-content/uploads/2024/04/Vulnerability-Databases.jpg
pagetype: article
filedate: "2026-11-28"
---
**Threat actors are targeting two recently disclosed GeoServer vulnerabilities that can be chained with other flaws to achieve unauthenticated remote code execution (RCE).**

Cybersecurity firm WatchTowr has observed attempts to exploit two high-severity GeoServer vulnerabilities tracked as CVE-2026-120705 and CVE-2026-129243. The activity appears to be aimed at identifying vulnerable servers.

“Attackers sent error-based exploit probes to validate that the server is vulnerable by creating and invoking stored queries,” WatchTowr [noted](https://x.com/watchtowrcyber/status/2125547398021693623).

WatchTowr has not reported any instances of attackers successfully achieving remote code execution. At the time of writing there do not appear to be any other reports of exploitation attempts.

GeoServer is an open source application for publishing and sharing geospatial data. Government agencies widely use it, and utilities also deploy it. Cybersecurity company Eye Security has [identified](https://labs.eye.security/unauthenticated-remote-code-execution-vulnerability-in-geoserver/) more than 3,000 internet-accessible GeoServer instances.

CVE-2026-120705 is an XML injection vulnerability that can allow an unauthenticated attacker to obtain sensitive files or conduct server-side request forgery (SSRF) attacks. CVE-2026-129243 can enable attackers to bypass access controls and perform operations typically reserved for administrators.

The two security holes are part of a five-bug exploit chain discovered by Rapid7 researcher Jonah Burgess, aka CryptoCat, who reported his findings to GeoServer developers in early August.

Burgess also reported CVE-2026-129244, CVE-2026-129245, and CVE-2026-129242. He showed how an attacker can gain admin access and execute arbitrary commands with the GeoServer process’s privileges.

The researcher disclosed [technical details](https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/) this week and published [PoC exploit code](https://github.com/Crypto-Cat/geoserver-unauth-rce-poc).

Eye Security has independently found some of the vulnerabilities. It demonstrated unauthenticated RCE on Linux and Windows by combining three weaknesses: CVE-2026-120705, CVE-2026-129245, and CVE-2026-120704. The security firm said it reported its findings to the vendor in late September.

GeoServer released patches several weeks ago, and it published [advisories](https://github.com/geoserver/geoserver/security/advisories) in recent days. Organizations are advised to upgrade to GeoServer 3.0.2, 2.28.6, or 2.27.7.

GeoServer vulnerabilities have been targeted in the past. In August 2026, [hackers exploited](https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/) a vulnerability as a zero-day, and in 2025 it came to light that a US government agency had been [breached](https://www.securityweek.com/geoserver-flaw-exploited-in-us-federal-agency-hack/) through the exploitation of a GeoServer flaw.

**Related**: [Drupal Flaw Found by Anthropic Scanner Exploited in Attacks](https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks)

**Related**: [Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library](https://www.securityweek.com/hackers-exploit-unpatched-flaw-in-defunct-idunno-anticsrf-library/)

**Related**: [Palo Alto Networks Patches Fragnesia Flaw Used to Root Firewalls](https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/)
