# extract: served via trafilatura-direct
---
title: Privilege Escalation Vulnerability in Falcon Crowdstrike - Truesec
author: Hjalmar Desmond
url: https://www.truesec.com/hub/blog/privilege-escalation-vulnerability-in-falcon-crowdstrike
hostname: truesec.com
description: FalconFlank abuses the office malicious macros remediation in Crowdstrike Falcon Sensor to achieve privilege escalation in the affected system. Affected
sitename: Truesec AB
date: "2026-09-04"
---
[Cybersecurity],

[Threat Intelligence]

Threat Insight

A new zero-day privilege escalation flaw impacting Falcon Crowdstrike, dubbed FalconFlank, has been dropped by the security researcher MSNightmare. They have also released a PoC abusing the vulnerability [1].

FalconFlank abuses the office malicious macros remediation in Crowdstrike Falcon Sensor to achieve privilege escalation in the affected system.

As of now the PoC works in a fully updated windows 11 25H2 / Windows Server 2025 with Crowdstrike Falcon – Phase 3 Optimal Protection with “Microsoft Office file malicious macro removal” setting.

It is advised to disable the “Microsoft Office File Suspicious Macro Removal Windows prevention” policy setting as soon as possible.

This setting can be found in the Next-gen antivirus settings under Clean infected Microsoft Office files.

After turning off the above feature, malicious macros will no longer be replaced. Customers with prevention policy settings configured, as per best practices, will remain protected. Prevention will continue to operate as normal via the Cloud Anti-malware for Microsoft Office Files settings.

Stay ahead with cyber insights

Stay ahead in cybersecurity! Sign up for Truesec’s newsletter to receive the latest insights, expert tips, and industry news directly to your inbox. Join our community of professionals and stay informed about emerging threats, best practices, and exclusive updates from Truesec.

Your current browser privacy settings may be preventing this form from loading properly. To continue, please allow cookies/tracking for this site or temporarily disable strict privacy protection, then refresh the page.

If you’re still experiencing issues, please contact us at [hello@truesec.com](mailto:hello@truesec.com)
