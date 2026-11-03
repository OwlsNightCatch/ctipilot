# extract: served via trafilatura-direct
---
title: Synology warns of C3RB3R ransomware attacks targeting NAS devices
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/
hostname: bleepingcomputer.com
description: Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks.
sitename: BleepingComputer
date: "2026-11-02"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, C3RB3R, Cerber, Ransomware, Synology, Warning,virus removal, malware removal, computer help, technical support']
fingerprint: "351280c71ed1ac4d"
---
Taiwanese network-attached storage (NAS) appliance maker Synology warned customers to update their devices immediately due to a surge in C3RB3r ransomware attacks.

The company urged users to enable automatic updates and upgrade the DiskStation Manager (DSM) software running on their NAS devices to the latest version to protect their data.

"Synology has identified threat actors exploiting a vulnerability patched in December 2024 to target devices running outdated versions of DSM. These attacks aim to encrypt data and extort ransom," it said in a [Thursday advisory](https://www.synology.com/en-global/company/news/article/C3RB3R/Synology%20urges%20users%20to%20update%20DSM%20following%20ransomware%20attacks%20on%20outdated%20DSM%20versions).

"Synology strongly urges all users running vulnerable versions to update DSM immediately to protect their systems. Synology also recommends enabling automatic updates to keep DSM up to date at all times."

A Synology spokesperson was not immediately available when BleepingComputer reached out for more information on these C3RB3r ransomware attacks.

While Synology has yet to share which vulnerability is being exploited in these ongoing attacks, it linked to a [November 2024 security advisory](https://www.synology.com/zh-tw/security/advisory/Synology_SA_24_20) with information about patches released for vulnerabilities allowing attackers to execute arbitrary code (CVE-2024-10441), read files (CVE-2024-50629), and write files (CVE-2024-10445) on unpatched devices.

Synology users are advised to immediately block access to the management web interface from the Internet and update their DSM software to block attackers' attempts to hack and encrypt their devices.

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| DSM 7.2.2 | Critical | Upgrade to 7.2.2-72806-1 or above. | 
| DSM 7.2.1 | Critical | Upgrade to 7.2.1-69057-6 or above. | 
| DSM 7.2 | Critical | Upgrade to 7.2-64570-4 or above. | 
| DSM 7.1 | Critical | Upgrade to 7.1.1-42962-7 or above. | 
| DSM 6.2 | Moderate | Upgrade to 6.2.4-25556-8 or above. | 

Synology rarely issues security advisories warning of attacks targeting its customers' devices, with the last such alert [published in August 2019](https://www.bleepingcomputer.com/news/security/synology-warns-of-malware-infecting-nas-devices-with-ransomware/) following large-scale brute-force attacks that led to [eCh0raix ransomware infections](https://www.bleepingcomputer.com/news/security/ech0raix-ransomware-now-targets-both-qnap-and-synology-nas-devices/).

Last week's advisory follows a massive wave of reports from Synology customers whose data was encrypted and who were prompted to buy "C3rb3r Decryptor" tool from a dark web portal for thousands of dollars.

The first reports surfaced [more than two weeks ago](https://www.bleepingcomputer.com/forums/t/819759/c3rb3r-ransomware-encrypting-nas-devices-l0ck3d-extension-read-me3txt/), with [affected](https://www.reddit.com/r/synology/comments/1xhqgov/well_it_finally_happened_my_first_real_ransomware/) [users saying](https://www.reddit.com/r/synology/comments/1xifzoi/for_victims_of_c3rb3r_ransomware/) the [ransomware](https://www.reddit.com/r/synology/comments/1xhh3zs/i_got_ransomed_next_step_before_restoration/) dropped a ransom note (read-me3.txt) and added a .L0CK3D extension to encrypted files.

"All your important files have been encrypted. Any attempts to restore your files with thrid-party software will be fatal for your files! The only way to decrypt your files safely is to buy the special decryption software 'C3rb3r Decryptor'," the ransom note warns.

"At this page you will receive the complete instructions how to buy the decryption software for restoring all your files. Also at this page you will be able to restore any one file for free to be sure 'C3rb3r Decryptor' will help you."

The Cerber ransomware (also known as C3RB3R and CerberImposter), now deployed in attacks targeting Synology NAS devices, borrowed its name from a notorious Ransomware-as-a-Service (RaaS) with the same name [that emerged in 2016](https://www.bleepingcomputer.com/news/security/the-cerber-ransomware-not-only-encrypts-your-data-but-also-speaks-to-you/).

Before disappearing at the end of 2019, the old Cerber ransomware operation accounted for [more than 80% of all ransomware attacks](https://www.bleepingcomputer.com/news/security/cerber-dominates-ransomware-landscape-after-lockys-demise/) and [a quarter of all ransomware infections](https://archive.li/dS4yJ) on enterprise endpoints.

Starting in December 2021, [when it was first spotted](https://www.bleepingcomputer.com/news/security/new-cerber-ransomware-targets-confluence-and-gitlab-servers/), C3RB3R was also deployed on Atlassian Confluence and GitLab servers as part of [several](https://www.bleepingcomputer.com/news/security/new-cerber-ransomware-targets-confluence-and-gitlab-servers/) attack [waves](https://www.bleepingcomputer.com/news/security/critical-atlassian-confluence-bug-exploited-in-cerber-ransomware-attacks/) exploiting remote code execution ([CVE-2021-26084](https://www.bleepingcomputer.com/news/security/atlassian-confluence-flaw-actively-exploited-to-install-cryptominers/) and [CVE-2021-22205](https://www.bleepingcomputer.com/news/security/over-30-000-gitlab-servers-still-unpatched-against-critical-bug/)) and authentication bypass ([CVE-2023-22518](https://www.bleepingcomputer.com/news/security/atlassian-warns-of-exploit-for-confluence-data-wiping-bug-get-patching/)) flaws.

Internet threat watchdog Shadowserver [now tracks over 380,000 Internet-exposed Synology NAS devices](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=180&vendor=synology&type=nas&limit=100&group_by=geo&stacking=stacked), but doesn't provide information on how many have already been secured against these attacks or are honeypots.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Comments

## beepboopboopbleeep - 7 hours ago

Synology seem to try really hard to give their paying customers the impression they do not care about keeping their tech stack up to date. Their own Synology Drive Server, even in the just released v4.0.4) runs on node.js v20 which does not receive any patches
