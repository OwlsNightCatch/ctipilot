---
title: Check Point Security Management Servers Hacked in AI-Assisted Campaign
author: Ionut Arghire
url: https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/
hostname: securityweek.com
description: The attacks were launched from 99 IP addresses and targeted organizations across multiple industries and countries.
sitename: SecurityWeek
date: "2026-11-24"
categories: ['Vulnerabilities']
tags: ['AI', 'Check Point']
fingerprint: "85dbf6d7a6208439"
language: en
image: https://www.securityweek.com/wp-content/uploads/2026/10/cyberattack-vulnerability-exploited.jpeg
pagetype: article
filedate: "2026-11-25"
---
**A threat actor has been using AI-enabled offensive tools in a broad campaign targeting Check Point Security Management servers, threat intelligence firm GreyNoise reports.**

As part of the campaign, which the security firm started tracking in early October and is likely still ongoing, a threat actor tracked as GreyNoise Threat 13 (GT13) has been conducting scanning, exploitation, and control activities from 99 IP addresses, many associated with disposable network infrastructure.

According to GreyNoise, GT13 targeted at least 22 organizations from the energy, engineering, financial services, government, manufacturing, mining, and transportation sectors across the US, the UK, Australia, Austria, China, France, Germany, Hong Kong, the Netherlands, South Korea, and other geographies.

GreyNoise believes the threat actor has been using agentic harnesses and systems to weaponize vulnerabilities, find vulnerable assets, and automatically exploit them. The automated operations were complemented by hands-on-keyboard activity.

“We witnessed the GT13 actor use 99 IP addresses, all of which were either egresses through ExpressVPN or compromised victim Check Point devices, including activity over 1400+ network sessions, 800+ command line artifacts, and 1200+ files downloaded, uploaded, or created,” [GreyNoise says](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign).

In one instance, GreyNoise tracked the activity to October 2, when the threat actor forged a signed admin session cookie to gain administrative access to an HFS server. The attacker obtained SSH access to the server, which was used to scan the environment and exfiltrate data.

“The GT13 adversary had access to the victim Check Point Security Management servers before they compromised the HFS server. We could not determine when or how the attacker gained access to those Check Point assets,” the company notes.

The attacker deployed tools such as Nmap, Chisel, Impacket, Paramiko, and other Python utilities and scripts, performed reconnaissance, lateral movement, and privilege escalation. They used one victim’s server as a hop to save command results and data exfiltrated from 24 previously compromised Check Point Security Management servers.

Between October 20 and 26, in addition to gaining deeper access to the victim’s environment, the threat actor conducted bulk actions against 21 other victim Check Point devices. GT13 issued a bulk certificate-management task to 24 servers across the 22 organizations. The task failed, but the threat actor collected the responses on the relay server in text files.

“These files contained the victim IP addresses and were in incrementing IP order, indicating an automation looped through them to run the commands on the compromised Check Point servers and deliver them via scp to this exfil folder. Each file was delivered from victim infrastructure, showing that each of the compromised devices holds the SSH private key that matches the public key planted on the hop,” GreyNoise says.

The activity within the first victim’s environment also involved the use or attempted exploitation of vulnerabilities such as [CVE-2026-61500](https://www.securityweek.com/exploitation-hits-rejetto-hfs-vulnerability-discovered-by-ai/) (Rejetto HFS), [CVE-2023-4966](https://www.securityweek.com/citrix-gov-agencies-issue-fresh-warnings-on-citrixbleed-vulnerability/) and [CVE-2025-5777](https://www.securityweek.com/citrixbleed-2-100-organizations-hacked-thousands-of-instances-still-vulnerable/) (Citrix NetScaler), [CVE-2024-21893](https://www.securityweek.com/governments-urge-organizations-to-hunt-for-ivanti-vpn-attacks/) (Ivanti), [CVE-2026-16232](https://www.securityweek.com/new-check-point-zero-day-vulnerability-exploited-in-the-wild/) (Check Point SmartConsole), [CVE-2026-98432](https://www.securityweek.com/cisco-watchguard-release-patches-sonicwall-wont-fix-gms-flaws/) (Linux IPv4 UAF), [CVE-2020-1472](https://www.securityweek.com/microsoft-reminds-organizations-upcoming-phase-patching-zerologon-vulnerability/) and [CVE-2026-41089](https://www.securityweek.com/critical-windows-netlogon-vulnerability-in-attackers-crosshairs/) (Windows NetLogon), [CVE-2021-26855](https://www.securityweek.com/dhs-gives-federal-agencies-5-days-identify-vulnerable-ms-exchange-servers/) and [CVE-2021-34473](https://www.securityweek.com/microsoft-issues-guidance-proxyshell-vulnerabilities/) (Microsoft Exchange), and [CVE-2021-21972](https://www.securityweek.com/vmware-vcenter-server-vulnerability-can-facilitate-attacks-many-organizations/) and [CVE-2023-34048](https://www.securityweek.com/vmware-vcenter-server-vulnerability-exploited-in-wild/) (VMware vCenter).

GreyNoise says it confirmed threat actor activity against Check Point Security Management servers between October 17 and November 2, when it stopped observing it. However, the company believes the campaign is still ongoing as GT13 had persistent access to the compromised servers.

“We believe the actor has separate agentic harnesses and systems weaponizing vulnerabilities, scanning for vulnerable assets, and automatically exploiting them to gather sets of systems that can be later used for operational relays or true targets. We suspect some of the foibles in the timeline reflect agentic offensive operations,” GreyNoise notes.

**Related:** [Elecbrakes Bluetooth Vulnerabilities Expose Trailers to Forced Braking](https://www.securityweek.com/elecbrakes-bluetooth-vulnerabilities-expose-trailers-to-forced-braking/)

**Related:** [N-able Patches Critical Flaw Discovered After Mail Assure Cyberattack](https://www.securityweek.com/n-able-patches-critical-flaw-disclosed-after-mail-assure-cyberattack/)

**Related:** [phpAfterShell Vulnerability Revives PHP2Shell’s Attack Path](https://www.securityweek.com/phpaftershell-vulnerability-revives-php2shells-attack-path/)

**Related:** [SAP NetWeaver, Cisco Expressway Flaws Exploited in Attacks](https://www.securityweek.com/sap-netweaver-cisco-expressway-flaws-exploited-in-attacks/)
