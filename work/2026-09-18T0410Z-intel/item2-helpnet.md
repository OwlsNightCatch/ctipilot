---
title: Acronis backup plugin flaw exploited in targeted attacks (CVE-2026-87886) - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/09/16/acronis-backup-plugin-vulnerability-exploited-cve-2026-87886/
hostname: helpnetsecurity.com
description: A Linux privilege escalation vulnerability (CVE-2026-87886) in Acronis' backup extensions for cPanel & WHM is being exploited.
sitename: Help Net Security
date: "2026-09-16"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['Acronis', 'backup', 'Linux', 'MSP', 'plugin', 'security update', 'vulnerability', 'web hosting', 'Acronis', 'backup', 'Linux', 'MSP', 'plugin', 'security update', 'vulnerability', 'web hosting']
---
# Acronis backup plugin flaw exploited in targeted attacks (CVE-2026-87886)

A Linux privilege escalation vulnerability (CVE-2026-87886) affecting Acronis’ backup extensions for cPanel, WebHost Manager (WHM), and Plesk, is being leveraged by attackers, the backup and recovery company warns.

“Exploitation of this vulnerability has been detected in the wild in limited, targeted attacks against Acronis Backup plugin for cPanel & WHM deployments,” Acronis said in the [security advisory](https://security-advisory.acronis.com/advisories/SEC-10986) published on Tuesday.

There’s currently no signs of its active exploitation on Plesk deployments.

### What the backup plugins do

Acronis is a cybersecurity and data protection technology company that’s popular among web hosting providers and managed service providers, since its platform lets them offer backup and security to their clients under their own branding.

Acronis’ backup add-ons link cPanel & WHM and Plesk – control panel platforms that make managing web servers and websites easier through a graphical interface – to Acronis’ cloud infrastructure, allowing administrators to back up and recover sites, databases, mailboxes, etc.

### What to do

CVE-2026-87886 stems from insecure file permissions and allows authenticated attackers to achieve local privilege escalation without any user interaction.

The vulnerability’s CVSS string indicates that it can be exploited in low complexity attacks, i.e., the attack doesn’t require special conditions or circumstances beyond the attacker’s control to succeed.

Though Acronis pushed out [security](https://security-advisory.acronis.com/updates/UPD-2609-3d72-20a7) [updates](https://security-advisory.acronis.com/updates/UPD-2609-efb0-50b2) for the vulnerable backup plugins last week, it has yet to disclose details about the in-the-wild attacks. Thus, we don’t know what the attackers are doing once they escalate their privileges on vulnerable Linux servers.

Acronis has advised administrators to immediately install:

- Acronis Backup plugin for cPanel & WHM version 1.9.3 HF3
- Acronis Backup extension for Plesk version 1.8.11

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
