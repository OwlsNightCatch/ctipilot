---
title: Hackers compromise Check Point Servers in 22 organizations
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/
hostname: bleepingcomputer.com
description: Threat actors have exploited multiple vulnerabilities to compromise two dozen Check Point Security management servers in an ongoing campaign targeting 22 organizations.
sitename: BleepingComputer
date: "2026-11-24"
tags: ['computers', 'windows', 'linux', 'mac', 'support', 'tech support', 'spyware', 'malware', 'virus', 'security', 'Check Point Software', 'Cyberattack', 'Management Server', 'Security Breach', 'virus removal', 'malware removal', 'computer help', 'technical support']
fingerprint: "7dd3c4e3a9355491"
language: en
image: https://www.bleepstatic.com/content/hl-images/2026/05/05/hacker.jpg
pagetype: article
filedate: "2026-11-25"
---
Threat actors have exploited multiple vulnerabilities to compromise two dozen Check Point Security management servers in an ongoing campaign targeting 22 organizations.

Threat intelligence firm GreyNoise detected the activity, noting that it resembled cyberespionage operations, although the attacker's motivation could not be conclusively determined.

The researchers track the activity as GT13 and confirmed it was ongoing between October 17 and November 2, when their visibility ended. However, given the threat actor's persistent access to Check Point devices, they believe the campaign remains active.

GreyNoise says the 22 victim organizations are spread across 17 countries, and show no clear evidence of specific targeting. They include government entities, financial services providers, and companies in the energy, transportation, mining, and manufacturing sectors.

The attacks were launched from 99 IP addresses that appear to come from compromised Check Point devices and ExpressVPN exit nodes.

A Rejetto HTTP File Server, compromised by exploiting CVE-2026-61500, was used as an operational relay for managing intrusions and collecting stolen data from the compromised environments.

While GreyNoise could not determine when or how the Check Point servers were breached, it observed the exploitation of CVE-2026-16232 during the post-compromise stages.

The vulnerability is an authentication bypass in Check Point SmartConsole that allows attackers to obtain an application login token and authenticate with administrator privileges.

Check Point warned about the flaw in July, marking it as an [actively exploited zero-day](https://www.bleepingcomputer.com/news/security/check-point-patches-smartconsole-zero-day-exploited-in-attacks/).

The researchers also observed attempts to exploit CVE-2025-5777 (Citrix NetScaler), CVE-2024-21893 (Ivanti), CVE-2026-41089 (Windows NetLogon), CVE-2026-16232 (Check Point SmartConsole auth bypass to Run Script), and CVE-2026-98432 (Linux IPv4 UAF).

[GreyNoise recorded](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) over 1,400 network sessions, 800 command-line artifacts, and 1,200 file-related activities, such as:

- Stealing firewall databases, credentials, configuration data, and internal certificate authority files.
- Generating a new certificate in one victim's environment.
- Unloading security policies, effectively disabling firewall protections.
- Conducting internal network reconnaissance and attempting lateral movement.
- Targeting additional enterprise systems, including Citrix NetScaler (CVE-2023-4966), Ivanti Connect Secure (CVE-2024-21893), VMware vCenter (CVE-2021-21972 and CVE-2023-34048), Microsoft Exchange (CVE-2021-26855/34473), and Microsoft Netlogon (CVE-2020-1472).

On October 26, the attacker performed a bulk certificate management operation across all 24 compromised Check Point servers, which failed, but still helped GreyNoise identify victims.

Τhe researchers assess that GT13 operated an AI-powered offensive tool, based on behavior, observed automation, and custom tooling, but the use of AI in this campaign remains unconfirmed.

Although GreyNoise lost visibility into the campaign operations on November 2, the researchers believe it could still be ongoing and have notified international government partners and CERTs to alert impacted organizations.

The company also shared indicators of compromise (IoCs) that could help identify additional intrusions or block future attempts.

BleepingComputer has contacted Check Point to ask if they have better visibility into those attacks and which flaw was exploited for initial access, and we are waiting for their response.

*Update 25/11* - A Check Point spokesperson responded to our inquiry with the below statement:

"We are aware of the activity outlined by the GreyNoise article. The attackers used CVE-2026-16232, a SmartConsole authentication bypass vulnerability that Check Point publicly disclosed in July 2026, with a note that exploitation had been observed in the wild. This vulnerability and available protections are therefore not new. The GreyNoise article also reports that the attackers used an adaptation of the publicly available Metasploit module for CVE-2026-16232, so the exploitation method described is also previously known." - Check Point

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
