---
title: Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It
author: The Hacker News
url: https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
hostname: thehackernews.com
description: Microsoft Store now offers Paint 11.2609.401.0 to fix CVE-2026-83844, an RCE flaw; Windows Update does not deliver the fix.
sitename: The Hacker News
date: "2026-11-06"
categories: ['Article']
fingerprint: "15ceff938345e751"
---
A fix for **CVE-2026-83844**, a remote code execution flaw in Windows Paint, is now in the Microsoft Store. Paint gets this fix only through a Store update, not through Windows updates.

The fixed build, 11.2609.401.0, was the newest Paint build in all ten countries The Hacker News checked today.

The flaw is an out-of-bounds read that could let an attacker run code over a network. Microsoft rates it as Important, with a CVSS score of 8.1, and says that a successful attack requires a deep understanding of the target system. The flaw was not known to be exploited or publicly disclosed when the company published it on October 13.

Brian Vitko of RFF, a device-management software maker, checked which Paint builds the Store offered in six countries earlier this week. He found that the newest in each was 11.2605.81.0, a build without the fix.

His test virtual machine has since moved to the fixed build on its own, through Store auto-update. That is one machine, and how quickly other PCs will get the build is not yet clear.

### Which Build Counts as Fixed

Microsoft's [security advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844) names 11.2609.401.0 as the fixed build. The CVE record for the flaw, which the company also publishes, still lists Paint as affected only below 11.2605.91.0. Its [NVD entry](https://nvd.nist.gov/vuln/detail/CVE-2026-83844) shows the same range.

So a scanner that reads the CVE record would treat any build from 11.2605.91.0 up as fixed. A copy at 11.2609.401.0 or later passes under both numbers.

As recently as last week, the advisory gave 11.2605.91.0 as the fixed build, according to a [forum question](https://learn.microsoft.com/en-us/answers/questions/6055591/microsoft-paint-11-2605-91-0) on Microsoft Q&A. The advisory's revision history still shows only its October 13 entry, with no note about the change.


### How to Check Every Copy of Paint

Paint, like other Store apps, is installed separately for each user account on a PC. Windows can also keep a provisioned copy that it installs for each new user. A check of only the signed-in account can miss older copies.

Vitko's [test write-up](https://getrff.com/blog/windows-paint-cve-2026-83844-store-fix-missing/) gives two commands to run in a PowerShell window opened as administrator. The first lists every user's copy of Paint, and the second lists the provisioned copy.

`Get-AppxPackage -AllUsers -Name Microsoft.Paint | Select-Object Version, @{ n = 'Users'; e = { $_.PackageUserInformation.UserSecurityId.Username -join ', ' } }`

`Get-AppxProvisionedPackage -Online | Where-Object DisplayName -eq 'Microsoft.Paint' | Select-Object Version`

For any copy below 11.2609.401.0:

1. Update Paint through the Store, or let the Store auto-update install the fixed build. In Intune and other device-management tools, the Store app update scan does this across many PCs.
2. Run both commands again and check that every copy shows 11.2609.401.0 or later.

The advisory lists no workaround or mitigation. Before the fix reached the Store, Vitko suggested removing Paint where nobody needs it, for every user and from the provisioned copy. He did not test that step.

### Attack Conditions and Exploitation Status

An attacker could exploit the flaw by sending "a specially crafted packet to an affected service over the network," the advisory says, but it does not name the service. The attack would require no sign-in and no user assistance.

The flaw was not in the Known Exploited Vulnerabilities catalog run by the U.S. Cybersecurity and Infrastructure Security Agency when The Hacker News checked today. The catalog was last updated earlier this week.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
