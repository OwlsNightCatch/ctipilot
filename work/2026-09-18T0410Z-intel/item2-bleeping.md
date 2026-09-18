---
title: Acronis warns of actively exploited flaw in its cPanel backup plugin
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/acronis-warns-of-actively-exploited-flaw-in-its-cpanel-backup-plugin/
hostname: bleepingcomputer.com
description: Acronis disclosed a high-severity Linux local privilege escalation vulnerability in its backup plugin for cPanel, WebHost Manager (WHM), and Plesk that may be exploited in the wild.
sitename: BleepingComputer
date: "2026-09-15"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Acronis, Actively Exploited, Addons, Backup, cPanel, Local Privilege Escalation, Privilege Escalation, Vulnerability,virus removal, malware removal, computer help, technical support']
---
Acronis disclosed a high-severity Linux local privilege escalation vulnerability in its backup plugin for cPanel, WebHost Manager (WHM), and Plesk that may be exploited in the wild.

cPanel & WHM and Plesk are used by web hosting companies and server administrators to manage websites and servers through graphical interfaces.

Acronis’ backup add-ons connect the hosting control panel to the company's infrastructure, allowing administrators to back up and restore websites, files, databases, mailboxes, and hosting accounts from within the cPanel and Plesk interfaces.

The flaw was published in a [brief advisory](https://security-advisory.acronis.com/updates/UPD-2609-3d72-20a7) last weekend, but the technology company issued an update today, identifying it as CVE-2026-87886 and assigning it a severity score of 7.8.

A low-privileged attacker can exploit CVE-2026-87886 to increase their permission level on a vulnerable Linux server, potentially enabling them to access or modify sensitive data and disrupt the system without user interaction.

Further technical details on CVE-2026-87886 have not been published, as the company wants to give system administrators time to apply the available patches before sharing more information.

Acronis says it has detected exploitation of the vulnerability in the wild, "in limited, targeted attacks."

“Exploitation of this vulnerability has been detected in the wild in limited, targeted attacks against Acronis Backup plugin for cPanel & WHM deployments,” the [advisory warns](https://security-advisory.acronis.com/advisories/SEC-10986).

In a statement for BleepingComputer, Acronis notes that the assessment is based on a single report from a "potentially affected" customer.

The CVE-2026-87886 vulnerability affects the following product versions:

- Acronis Backup plugin for cPanel & WHM builds earlier than 1.9.3.1021, fixed in version 1.9.3 HF3
- Acronis Backup extension for Plesk builds earlier than 1.8.11.638, fixed in version 1.8.11

The company has identified no specific indicators of compromise and did not disclose when the activity occurred or what attackers achieved beyond the privilege-escalation impact described by the advisory.

All affected users of Acronis backup integrations for cPanel & WHM and Plesk are recommended to apply the available updates immediately.

## 
            [Build your security blueprint for AI-powered attacks](https://hubs.li/Q04x67m50)
        

        Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed.

[Save your seat](https://hubs.li/Q04x67m50)

## Comments

## NoneRain - 1 day ago

"ops"
