---
title: Zyxel fixes zero-day exploited to hack nearly 1,000 network switches
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/
hostname: bleepingcomputer.com
description: Zyxel has patched a zero-day vulnerability in its GS1900 series network switches that hackers exploited to compromise nearly 1,000 devices worldwide and steal configuration files and credentials.
sitename: BleepingComputer
date: "2026-11-04"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, CVE-2026-107441, CVE-2026-7273, Router, Zero-Day, Zyxel,virus removal, malware removal, computer help, technical support']
fingerprint: "25b0e1119c9ef2cd"
---
Zyxel has patched a zero-day vulnerability in its GS1900 series network switches that hackers exploited to compromise nearly 1,000 devices worldwide and steal configuration files and credentials.

The vulnerability, tracked as CVE-2026-107441, is an out-of-bounds write flaw in the switches' web management interface that allows an unauthenticated attacker with network access to execute operating system commands using specially crafted HTTP requests.

The flaw affects ten GS1900 switch models, and Zyxel released security updates on October 22 and published a [security advisory](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-out-of-bounds-write-vulnerability-in-gs1900-series-switches-11-03-2026) on November 3.

However, the vulnerability was initially mistaken for an older flaw that Zyxel had already patched months before the attacks began.

## Attacks linked to zero-day flaw

On June 16, 2026, Zyxel [released security updates](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026) addressing CVE-2026-7273, a pre-authentication buffer overflow vulnerability affecting the same GS1900 switches.

Starting around August 17, cybersecurity company GreyNoise observed a suspected Chinese-speaking threat actor tracked as Kapibala exploiting Zyxel switches, reporting that the [attackers compromised 996 devices](https://www.bleepingcomputer.com/news/security/chinese-hackers-exploit-multiple-technologies-to-steal-govt-data/) across 48 countries.

The threat actors exploited the flaw to execute commands remotely before downloading a script that collected device configurations, hashed root credentials, and network information.

GreyNoise linked Kapibala to the Red Heron hacking campaign, which [Acronis previously reported](https://www.acronis.com/en/tru/posts/red-heron-exploits-gitea-n-day-flaw-in-multinational-campaign-exposing-new-linux-rootkit/) was exploiting a critical vulnerability in the self-hosted Git service Gitea.

When GreyNoise disclosed the campaign on September 21, it attributed the exploitation to CVE-2026-7273, the vulnerability Zyxel had patched in June.

That same day, [CISA added CVE-2026-7273](https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/) to its Known Exploited Vulnerabilities catalog, requiring federal agencies to address the flaw.

However, researchers at firmware security company [Binarly discovered](http://www.binarly.io/blog/zyxel-gs1900-rce-cve-2026-107441) that the exploit used in the attacks actually targeted a separate, previously unknown vulnerability that remained unpatched.

While investigating Red Heron infrastructure linked to the JITTERLY backdoor and SIXZUT rootkit, Binarly researchers found an exposed archive containing an obfuscated Python exploit targeting Zyxel GS1900 switches.

After analyzing the exploit, the researchers found that it specifically checked for firmware versions patched for CVE-2026-7273, indicating the exploit had been developed or updated to target those versions.

Binarly confirmed on September 28 that the exploit remained effective against all ten firmware releases patched for CVE-2026-7273.

The researchers determined that the earlier security update added checks to prevent a buffer overflow, but attackers could bypass them by corrupting a parameter counter before it was validated.

This allowed the exploit to overwrite memory and execute commands without authentication, even on switches running the earlier security updates.

Binarly reported its findings to Zyxel on September 29, and the vendor confirmed the new vulnerability on October 11, assigning it CVE-2026-107441.

Zyxel classified it as a separate flaw because the exploit also abused missing validation of HTTP parameter lengths.

On October 22, Zyxel released new firmware updates that limit parameter sizes and validate the parameter count before copying data into memory, preventing the exploitation technique.

While the recovered exploit specifically targeted firmware patched for CVE-2026-7273, it remains unclear whether it was deliberately developed to bypass those updates or exploited a related vulnerability that the earlier patches failed to address.

Administrators of affected Zyxel GS1900 switches are advised to install the latest firmware updates to protect against CVE-2026-107441.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
