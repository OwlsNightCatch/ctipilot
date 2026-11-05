---
title: Hackers use n-day exploits in zero-click attacks on iOS, Android devices
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/hackers-use-n-day-exploits-in-zero-click-attacks-on-ios-android-devices/
hostname: bleepingcomputer.com
description: A large-scale watering hole attack associated with Russian hackers has been targeting iOS and Android users visiting compromised sites or fake ones impersonating legitimate portals.
sitename: BleepingComputer
date: "2026-11-04"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Android, APT29, Darksword, iOS, iPhone, Russia, Watering Hole,virus removal, malware removal, computer help, technical support']
fingerprint: a387a9939a374145
---
A large-scale watering hole attack associated with Russian hackers has been targeting iOS and Android users visiting compromised sites or fake ones impersonating legitimate portals.

The campaign used multiple high-profile websites in the U.S., Ukraine, the Czech Republic, and Bulgaria that delivered the same payload for profiling visitors and their devices.

This initial stage allows the attacker to determine the browser version to deploy "platform-specific n-day exploit chains without user interaction."

Researchers at cybersecurity company Sekoia attribute the operation with moderate-to-high confidence to APT29 (aka Midnight Blizzard), a Russian threat group that was recently linked to [hotel WiFi attacks](https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/).

Based on their findings, compromised legitimate sites belong to a Ukrainian gas producer, a U.S. chemical industry trade association, and a Bulgarian military-related site.

Lookalike domains impersonated the official America250 site and Raffles London at The OWO hotel, relaying content from the real sites in an adversary-in-the-middle attack model.

The researchers also discovered that the threat actor had compromised Ukrainian web analytics service Plerdy and modified its SEO tracker, which was loaded by thousands of websites, mostly in Ukraine, between August 27 and September 3.

In all cases, the initial payload was JavaScript code that profiled website visitors to determine their devices and browser versions. The command-and-control (C2) server then pushed the correct exploit chain.

According to Sekoia, the threat actors exploited the following vulnerabilities to extract cookies, messaging app databases, and credentials:

- [CVE-2025-43529](https://www.bleepingcomputer.com/news/security/apple-fixes-two-zero-day-flaws-exploited-in-sophisticated-attacks/) and CVE-2024-27834 (in iOS 16.7). The payload targets cookies stored in Safari.
- CVE-2025-43529, CVE-2026-20700, CVE-2025-14174, CVE-2025-43510, and CVE-2025-43520 (in iOS 18.5). The payload harvests WhatsApp and Telegram databases, Keychain credentials, location data, and photos.
- [CVE-2026-3910](https://www.bleepingcomputer.com/news/google/google-fixes-two-new-chrome-zero-days-exploited-in-attacks/) and [CVE-2025-27038](https://www.bleepingcomputer.com/news/security/android-gets-patches-for-qualcomm-flaws-exploited-in-attacks/) (in Chrome for Android 139 to 145, excluding 143). Uses AndroSnitch to collect Chrome cookies, login data, browsing history, and saved WiFi credentials.

The researchers identified four other vulnerabilities in unreachable code or alternate exploit paths, but they were not used in the analyzed chains.

CVE-2025-43529 is linked to the [“DarkSword” exploit kit](https://www.bleepingcomputer.com/news/security/new-darksword-ios-exploit-used-in-infostealer-attack-on-iphones/), first documented in March, and leveraged in attacks since at least November 2025 by multiple threat groups.

[Sekoia says](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits) that none of the payloads APT29 used in these attacks established persistence, allowing a device reboot to stop the malicious activity until visiting a compromised site again.

Regarding its attribution to APT29, Sekoia notes similarities to past watering-hole operations by the same threat group, infrastructure overlaps, and a compromised site that a partner linked to a 2025 APT29 campaign.

Apple and Google have patched all flaws targeted in this campaign, with fixes even [reaching older iOS releases](https://www.bleepingcomputer.com/news/security/apple-expands-ios-18-updates-to-more-iphones-to-block-darksword-attacks/), so users are recommended to apply the latest available security updates for their devices.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
