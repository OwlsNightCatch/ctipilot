---
title: D-Link warns of multiple zero-days in DGS-3130 Series switches
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/d-link-warns-of-multiple-zero-days-in-dgs-3130-series-switches/
hostname: bleepingcomputer.com
description: D-Link shared mitigation measures for multiple unpatched security flaws affecting DGS-3130 series managed Gigabit stackable switches.
sitename: BleepingComputer
date: "2026-11-06"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, D-Link, DGS-3130, DGS-3130-30TS, Switch, Vulnerability, Warning, Zero-Day,virus removal, malware removal, computer help, technical support']
fingerprint: "3e32e543ca7cb3ce"
---
D-Link shared mitigation measures for multiple unpatched security flaws affecting DGS-3130 series managed Gigabit stackable switches.

[These switch models](https://www.dlink.com/ro/ro/products/dgs-3130-gigabit-layer-3-stackable-managed-switches) provide multi-gigabit uplinks, allowing enterprise network administrators to eliminate data bottlenecks, and are designed primarily for small-to-medium businesses (SMBs) and metro Ethernet deployments.

While D-Link didn't share details on these flaws and has yet to publicly disclose the CVE IDs for easier tracking, it said Spectrum Community Solutions network engineer Giresh Kumar Enugu found the bugs in the D-Link Discovery Protocol (DDP) authentication, access control, and information handling.

Successful exploitation could allow attackers to obtain sensitive device data, make unauthorized credential/configuration changes, leak SNMP communities, or cause service disruptions and device resets.

The zero-days affect multiple [DGS-3130-30TS](https://www.dlink.com/us/en/products/dgs-3130-30ts-30-port-lite-layer-3-stackable-managed-gigabit-switch) firmware versions, and the company is still investigating the impact on other D-Link switching platforms and firmware security mechanisms (including SSH service security configuration, safeguards underlying operating-system credentials, and handles firmware encryption/embedded cryptographic keys).

"The reported vulnerabilities involve the D-Link Discovery Protocol (DDP) and certain components of the device's firmware security architecture," [D-Link said](https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10523).

"According to the security researcher, successful exploitation of certain vulnerabilities may allow an attacker with access to the affected network to obtain sensitive device information, perform unauthorized administrative operations, modify device configuration, or disrupt network services."

Until it releases new firmware to address these flaws, D-Link asked admins to disable DDP to remove the primary known attack vector, remove unnecessary or default SNMP community strings, and restrict SSH, web UI, and SNMP accessibility solely to isolated management networks and designated admin hosts.

D-Link also advised admins to maintain offline switch configuration backups and track device logs for unexpected configuration changes, unprompted reboots, or factory resets.

In September, D-Link warned customers of a maximum-severity zero-day (tracked as [CVE-2026-86296](https://nvd.nist.gov/vuln/detail/cve-2026-86296)) with a public proof-of-concept (PoC) exploit and no patch, affecting legacy DIR-822A dual-band Wi-Fi routers.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
