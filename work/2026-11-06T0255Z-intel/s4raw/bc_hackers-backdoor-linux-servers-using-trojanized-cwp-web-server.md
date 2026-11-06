---
title: Hackers backdoor Linux servers using trojanized CWP web server
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/hackers-backdoor-linux-servers-using-trojanized-cwp-web-server/
hostname: bleepingcomputer.com
description: A new Linux malware called CWPdoor is being distributed through a trojanized version of cwpsrv, the web server behind the Control Web Panel (CWP) management interface.
sitename: BleepingComputer
date: "2026-11-05"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Backdoor, Control Web Panel, CWP, CWPdoor, Linux, Malware,virus removal, malware removal, computer help, technical support']
fingerprint: "258d8889ecb26e83"
---
A new Linux malware called CWPdoor is being distributed through a trojanized version of cwpsrv, the web server behind the Control Web Panel (CWP) management interface.

CWPdoor acts as a passive backdoor that sits dormant on the compromised system until the attacker sends a specially crafted request.

Researchers at XLab, the cybersecurity research arm of QiAnXin Technology Group, describe CWPdoor as "exceptionally stealthy" due to its passive triggering and log suppression feature.

CWP, formerly known as CentOS Web Panel, is an open-source web hosting administration solution similar to cPanel and Plesk that allows users to manage web servers and services such as email, DNS, and databases.

According to XLab, more than 340,000 CWP instances have been exposed on the public web over the past month.

The researchers discovered the CWPdoor malware on June 29 after capturing a script posing as an updater that replaced the legitimate 'cwpsrv' binary with a malicious version.

The script replaces cwpsrv versions 1.15.10 and 1.24.0, and takes several steps to hide the switch, like restoring file and directory timestamps, deleting temporary files, and wiping the command-history log.

The malware operators activate the backdoor by sending it commands to be executed, in the form of an encrypted HTTP header (X-Ngx-Integrity-Data). The request also contains headers for the timestamp (X-Ngx-Integrity-Time) and the RSA signature (X-Ngx-Integrity-Sig).

Commands and their output are encrypted using the AES-256-CBC cipher to keep them protected.

The backdoor checks whether the timestamp falls within a five-minute window and verifies the RSA signature before decrypting the command and passing it to a helper process for execution.

“Changing either the timestamp or the ciphertext independently invalidates the signature,” [XLab explains](https://blog.xlab.qianxin.com/cwpdoor-the-invisible-backdoor-living-inside-control-web-panel/).

“By binding the three fields together and enforcing a ±300-second time window, the mechanism provides replay protection and authorization control.”

The backdoor also interferes with the server’s logging module to prevent the triggering request from appearing in the access logs.

After finding the initial infection script, the researchers saw CWPdoor uploaded to VirusTotal on September 30 in an archive that included the Ebury backdoor.

What caught their attention was that the malicious cwpsrv file (*cwpsrv.suspeito*) in the archive had zero detections.

"This indicates that the campaign was not merely experimental: real victims already exist in the wild," the researchers say, adding that the connection between Ebury and CWPdoor remains unclear.

Ebury is a Linux backdoor and credential stealer botnet operation active since at least 2009. A report from cybersecurity company ESET in May 2024 said that the malware had [infected nearly 400,000 servers](https://www.bleepingcomputer.com/news/security/ebury-botnet-malware-infected-400-000-linux-servers-since-2009/) since it emerged.

The researchers recommend that administrators check for the *ngx\_http\_integrity\_helper* Unix socket, suspicious *cwpsrv* helper processes, and X-Ngx-Integrity strings in the server binary.

If a compromise is confirmed, replace the backdoored binary with a legitimate copy, upgrade to the latest version, rotate all control panel credentials, and investigate the host for additional malware.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
