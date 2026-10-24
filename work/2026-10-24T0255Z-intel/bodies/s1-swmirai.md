---
title: Mirai Botnet Operators Join PHP2Shell Attacks as ASLR Bypass Exploits Emerge
author: Eduard Kovacs
url: https://www.securityweek.com/mirai-botnet-operators-join-php2shell-attacks-as-aslr-bypass-exploits-emerge/
hostname: securityweek.com
description: Researchers tie PHP2Shell attempts to a Mirai botnet and show an ASLR bypass, but no successful compromise has been confirmed yet.
sitename: SecurityWeek
date: "2026-10-23"
categories: ['Vulnerabilities']
fingerprint: adf8bddbcc8637c0
---
**Two days after PHP rolled out emergency fixes for the PHP2Shellvulnerabilities, threat actors have tried to use the flaws to spread a Mirai botnet. A security firm has also built an exploit that gets past a key memory protection, and an exposed attacker server has revealed custom tooling.**

Even so, no successful in-the-wild compromise has been confirmed so far.

The threat has prompted many organizations to take systems offline as a precaution. Several government, school and hospital websites in Europe went dark on October 21, and the UK government said 32 of its services were unavailable and four partly unavailable, mostly due to precautionary measures taken while patches were applied.

PHP2Shell is the name given to CVE-2026-109618 and CVE-2026-109619, two critical bugs in the PHP engine that can be exploited for unauthenticated remote code execution. Each has a CVSS v4.0 score of 9.2.

Wiz, OpenAI and Calif found the issues in August. PHP patched them on October 21 with versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35, one day earlier than planned, after the CVE identifiers [leaked online](https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/).

Amazon spotted the [first exploitation attempt](https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/) on October 17, and attack activity surged once the fixes went out. Vendors, security firms and government agencies have since [issued](https://www.securityweek.com/tech-and-security-companies-respond-to-php2shell-vulnerabilities/) advisories, detection rules and patching guidance.

## Mirai botnet linked to exploitation attempts

Sophos says threat actors have tried to leverage PHP2Shell to [install Potassium](https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619), which it believes is a variant of the Mirai botnet. The attempt it analyzed was stopped, so the malware never reached the targeted system.

Sophos describes the sample as an updated build, with more functionality, of a Mirai-derived strain first identified in early 2026. It can download additional malware and launch DDoS attacks.

Sophos’s latest analysis corrected an earlier update from the company that reported a successful exploitation.

Arctic Wolf [connected](https://arcticwolf.com/resources/blog/php2shell-critical-php-vulnerabilities-enable-unauthenticated-remote-code-execution/) two Potassium binaries to the servers hosting PHP2Shell payloads. However, it said its data does not show the PHP2Shell requests fetching or running the malware.

Hunt.io [attributed](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories) the PHP2Shell traffic it observed to an established Mirai-style botnet, active since at least May 2026, that recently added the flaws to the methods it uses to spread.

Sophos believes attackers are having a hard time with the bugs. “The lack of successful exploits in the wild suggests threat actors are also struggling,” it said. Its own adversary research team has found that building a working exploit is difficult, even with help from AI.

## Attempts, but no confirmed breaches

Other firms paint a similar picture. Hunt.io says it has seen exploitation attempts and attackers preparing tooling, but no confirmed compromise, and no vendor has reported one either. Wordfence also says attacks are continuing [without any known compromises](https://www.wordfence.com/blog/2026/10/attacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet/).

Sansec, which had predicted mass exploitation within 15 minutes of the patch release, has revised that view. In an October 22 update, it said [attackers need detailed knowledge](https://sansec.io/research/php2shell) of a server and particular conditions on it to succeed, and that the publicly available exploits fail against PHP installations with default settings.

## Exploit defeats ASLR in production setups

Researchers have cited address space layout randomization (ASLR), which randomizes where code and data are placed in memory, as a significant hurdle to achieving code execution. VulnCheck says it has found a way around it.

The company’s [exploit for CVE-2026-109618](https://www.vulncheck.com/blog/php2shell-vulnerabilities) relies on a memory leak to reach code execution on x86-64 systems with ASLR enabled and PHP error display turned off, which is the recommended setup for production. The exploit is available to VulnCheck’s Initial Access Intelligence customers.

“We are not aware of any other public or commercial exploit that achieves RCE on multiple versions of PHP in production configurations, though we expect that to change as adversaries develop incrementally more sophisticated attacks,” VulnCheck said.

The company also noted that while hundreds of PoC repositories have appeared on GitHub, very few of them contain legitimate exploits.

## Attacker server exposes PHP2Shell toolkit

SOCRadar uncovered an attacker pursuing a similar goal. It discovered [PHP2Shell tooling](https://socradar.io/blog/php2shell-exploit-tooling-attacker-server/) on an attacker-controlled server whose working files were left publicly browsable.

The files included an exploit chain for PHP 8.4.26 on Apache mod\_php, which the operator had tested in a lab and billed as a “one-click” exploit. Companion scripts checked whether real websites had the configuration the exploit requires.

That configuration is uncommon. According to SOCRadar, the chain only works on servers set up more like test systems than hardened production ones.

The operator fingerprinted about 20 websites in countries including the US, UK, Canada, France, Finland, Poland and China, and probed 11 of them in more depth. None met the exploit’s requirements.

“The operator shows strong exploit development skills, but as of October 22, 2026, we have seen no evidence of shell access on any screened site,” SOCRadar said.

Hunt.io also analyzed the server. It found that the operator ran 10 attack rounds, expanding the target list to 123 servers hosted by cloud providers, shared hosting companies and ISPs. Roughly 57 of the servers ran PHP, 10 rejected the requests, and none was successfully exploited.

## Patching lags behind

Qualys, which [analyzed](https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities) anonymized data from 12,000 of its customers, says only 199,000 PHP instances were patched within 12 hours of disclosure.

According to the company, roughly 110 million instances, or 71%, run PHP versions 5.4 through 8.1, which are past end of life, and most of them will never receive a vendor patch. Another 44 million instances run supported PHP branches for which fixes exist but had not been applied.

As of the morning of October 23, CISA had not added either vulnerability to its Known Exploited Vulnerabilities (KEV) catalog.

Censys is [tracking patching progress for PHP2Shell](https://php2shell.censys.com/) in real time through a public dashboard that shows how many internet-facing PHP services still run a vulnerable version.

**Related**: [Attackers Exploit Third VeloCloud Orchestrator Zero-Day in Four Months](https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/)

**Related**: [Oracle Patches Over 1,200 Vulnerabilities With October 2026 CPU](https://www.securityweek.com/oracle-patches-over-1200-vulnerabilities-with-october-2026-cpu/)
