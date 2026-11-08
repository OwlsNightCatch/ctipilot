---
title: "CISA: Hackers chain Plex flaws in Plex2Shell attacks to breach servers"
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/cisa-hackers-chain-plex-flaws-in-plex2shell-attacks-to-breach-servers/
hostname: bleepingcomputer.com
description: The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are actively exploiting four vulnerabilities in Plex Media Server.
sitename: BleepingComputer
date: "2026-10-21"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, CISA, KEV, Known Exploited Vulnerability Catalog, Plex, Plex Media Server, Plex2Shell, Vulnerability,virus removal, malware removal, computer help, technical support']
fingerprint: b46c8512e993fb86
---
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) is warning that attackers are actively exploiting four vulnerabilities in Plex Media Server.

The security issues are collectively called Plex2Shell. When chained in an exploit, an attacker can obtain the owner's admin token and execute code with elevated privileges.

Plex Media Server is a popular media suite that helps users organize personal collections of movies, TV shows, music, and photos, and stream them to other devices at home or remotely over the internet.

CISA has directed federal agencies to prioritize patching systems affected by Plex2Shell vulnerabilities or apply mitigations by October 23.

The security issues were discovered by security researcher Zach Main, who reported them responsibly to Plex on July 27.

The individual flaws are rated medium to high in severity, but the researcher assigns the full exploit chain a critical score of 9.8.

- CVE-2026-96652 – An SSRF flaw in /player/timeline that allows unauthenticated attackers to make Plex send POST requests to arbitrary destinations, including its own internal APIs.
- CVE-2026-96654 – A URL injection flaw in searchOne that allows attackers to invoke other plugins’ functions with attacker-controlled parameters.
- CVE-2026-96655 – An authenticated SSRF flaw in the transcoder endpoint that allows users to make Plex request arbitrary internal or external addresses.
- CVE-2026-96656 – An arbitrary file write flaw in the transcoder settings that allows administrators to plant malicious shared libraries that Plex subsequently loads, leading to code execution.

Zach Main published [full technical details for the Plex2Shell](https://zmain.info/blog/plex2shell) vulnerabilities on October 16, followed by a proof-of-concept (PoC) exploit three days later.

On October 17, reports of Plex2Shell being [exploited in the wild](http://www.boredhackerblog.info/2026/10/plex-vulnerabilities-being-exploited-in.html) started to emerge, intially targeting  Plex honeypots to deploy a cryptominer.

Plex2Shell impacts Plex Media Server versions before 1.43.3.10861, which was [released on August 4](http://forums.plex.tv/t/plex-media-server/30447/711).

### Hackers also target Siemens Software Center

Alongside Plex2Shell, CISA has added to its catalog of Known Exploited Vulnerabilities ([KEV](http://www.cisa.gov/known-exploited-vulnerabilities-catalog)) an uncontrolled search path element flaw, tracked as CVE-2026-110936, in Siemens Software Center (SSC).

The German technology giant [warned on October 19](http://productcert.siemens.com/news/2026/10/19/active-exploitation-of-cve-2026-110936-in-siemens-software-center/) that hackers were leveraging the vulnerability in campaigns linked to a multi-payload ClickFix delivery platform called Romulus.

Recent research from operational technology (OT) cybersecurity company [Forescout notes](https://www.forescout.com/blog/romulus-analysis-of-a-new-multi-payload-clickfix-delivery-platform/) that Romulus "may be a privately operated panel, a commercial cybercriminal delivery service, an affiliate framework, or software that has been copied between operators."

Siemens's alert on CVE-2026-110936 shares indicators of compromise (IoCs) and advice on identifying compromised systems, urging administrators to update Siemens Software Center to version 4.0.9.8 or later.

CISA has also added CVE-2026-106931 to KEV, an OS command injection flaw that affects affecting the SiteGuard Server Edition web application firewall (WAF).

Both the vendor and [Japan's CERT flagged](https://www.bleepingcomputer.com/news/security/hackers-exploit-siteguard-waf-flaw-to-run-commands-as-system-root/) CVE-2026-106931 as actively exploited late last week.

The vendor urged users to upgrade to SiteGuard Server Edition for Apache httpd, Nginx, and IIS version 8.00 Update 5, and SiteGuard Server Edition for Apache httpd and Nginx on FreeBSD version 7.00 Update 6 and later.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
