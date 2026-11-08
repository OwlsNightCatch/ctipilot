---
title: QNAP says hackers breaching NAS devices in Plex2Shell attacks
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/qnap-says-hackers-breaching-nas-devices-in-plex2shell-attacks/
hostname: bleepingcomputer.com
description: QNAP urges users to update Plex Media Server to the latest version available in the QNAP App Center, as hackers are exploiting the Plex2Shell vulnerability chain.
sitename: BleepingComputer
date: "2026-11-06"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, Hardware, NAS, Plex, Plex Media Server, Plex2Shell, QNAP,virus removal, malware removal, computer help, technical support']
fingerprint: b445b012d9b3df47
---
QNAP urges users to update Plex Media Server to the latest version available in the QNAP App Center, as hackers are exploiting the Plex2Shell vulnerability chain.

The vendor said it had received multiple reports of suspected compromises involving customers’ network-attached storage (NAS) devices.

"QNAP has received reports from some users that Plex Media Server on their NAS appears to have been compromised through \[Plex2Shell\] vulnerabilities, and QNAP Technical Support is assisting the affected users,” the company says in an advisory today.

Plex2Shell is a chain of four vulnerabilities in the Plex Media Server, tracked as CVE-2026-96652, CVE-2026-96654, CVE-2026-96655, and CVE-2026-96656.

Security researcher [Zach Main discovered and reported](https://zmain.info/blog/plex2shell) the flaws to Plex on July 27. Exploitation started shortly after the full technical details became public on October 16.

CISA added all four flaws to its Known Exploited Vulnerabilities catalog on October 20, 2026, [urging federal agencies to upgrade](https://www.bleepingcomputer.com/news/security/cisa-hackers-chain-plex-flaws-in-plex2shell-attacks-to-breach-servers/) to Plex 1.43.3.10861 or later within three days, giving it maximum priority.

QNAP’s NAS devices are specialized computers with built-in storage that allow users to store, access, and share files across a network. They are typically used to back up computers and store media files.

Users can also expand their devices' capabilities by installing applications from the QNAP App Center, such as Plex Media Server, which streams movies, TV shows, and music directly from NAS drives.

QNAP advises users to update Plex Media Server to the latest version available through the QNAP App Center, currently 1.43.3.10861, to protect against Plex2Shell attacks.

“The QNAP Product Security Incident Response Team (QNAP PSIRT) has confirmed that the vulnerabilities exist only in Plex Media Server; QTS, QuTS hero, and other QNAP operating systems are not themselves affected,” the vendor says.

### User action required

QNAP says that users should treat their NAS devices and all personal content as compromised if they're running a vulnerable Plex server that is exposed on the public web.

The vendor warned that updating now will not remove any payloads the attackers have already installed on the device.

The recommended action is to check for the signs of compromise shared in the [security bulletin](https://www.qnap.com/en/security-news/2026/qnap-security-notice-plex-media-server-vulnerabilities-plex2shell-update-to-1-43-3-10861-or-later-immediately), perform a clean reinstall of the OS (QTS or QuTS hero), and then reset Plex and NAS credentials.

Users who do not need to access Plex remotely should disable the related features and stop forwarding port 32400. Those who need remote access are advised to connect via VPN.

QNAP has released a detailed [step-by-step remediation guide](https://www.qnap.com/en/how-to/faq/article/plex2shell-check-and-remediation-faq-for-qnap-nas-users) on how to do the above.

The company also offers to investigate logs from suspected compromises, which users can submit via QNAP’s technical support portal.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
