---
title: Windows 11’s Paint has a no-click hacking bug, and even with auto-updates on, you may not have the fix
author: Mayank Parmar
url: https://www.windowslatest.com/2026/11/05/windows-11s-paint-has-a-no-click-hacking-bug-and-even-with-auto-updates-on-you-may-not-have-the-fix/
hostname: windowslatest.com
description: Microsoft Paint apparently has a security flaw, and while there's a patch, nobody is actually seeing it when they look for one in the Store.
sitename: Windows Latest
date: "2026-11-05"
categories: ['Windows 11']
fingerprint: "17586db3e4c3c4e1"
---
You [shouldn’t delay or ignore updates for Windows 11](https://www.windowslatest.com/2026/09/09/microsoft-warns-dont-delay-windows-11s-update-released-today-confirms-record-security-fixes-as-ai-becomes-a-threat/), and that includes its inbox apps. Microsoft Paint apparently has a security flaw, and while there’s a patch, nobody is actually seeing it when they look for one in the Microsoft Store.

Microsoft disclosed the vulnerability on October 13, and if left unpatched, it could allow an attacker to run code on your PC over a network without you clicking anything. We’re not seeing any reports of the vulnerability being exploited in the wild, but some third-party antivirus software, specifically for enterprises, may flag Paint for missing the security patch.

Microsoft is tracking the Paint vulnerability as CVE-2026-83844, and it has a severity score of 8.1 out of 10. Microsoft rates it as “Important,” below the “Critical” rating used for more severe issues. That doesn’t mean you should keep using Paint when it isn’t fully patched, but at the same time, I wouldn’t freak out.

## Microsoft says the Paint fix is available, but we’re not seeing it

On October 13, when Microsoft [disclosed](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844) the vulnerability, it also rolled out a patch through the Microsoft Store. According to its own support document, if you’ve got Paint version 11.2609.401.0 or newer, you’re fully protected.

I’ve got automatic updates turned on in the Microsoft Store, so I was hoping to have the update already applied. I did not find any available updates in the Store for Paint, so I assumed it must have already been updated, as I’ve “auto-updates” turned on in the MS Store settings after all.

However, when I checked Paint’s version from the app’s settings, it was running 11.2603.251.0:

That’s clearly an older version than the recommended 11.2609.401.0, so it’s quite confusing what’s going on. We don’t know whether a bug is blocking the patched version of Paint from showing up in the Store or whether Microsoft documented an incorrect app version as the required update in its own security bulletin.

It’s not just us who observed the odd behavior with Microsoft Paint’s security update; other users noticed it today, too. On Reddit, IT admins [confirmed](https://old.reddit.com/r/sysadmin/comments/1xnlkjf/cve202683844_what_is_everyone_doing/) that they do not see the Paint update at all, even when they used a third-party tool to download the MSIX of the app.

It’s also worth noting that installing [Windows 11’s October 2026 update](https://www.windowslatest.com/2026/10/13/windows-11-kb5127648-26h2-is-out-with-major-changes-like-emoji-17-file-explorer-preview-pane-upgrade-and-more-direct-download-links-for-offline-installer-msu/), which itself patched over 1,000 security issues, doesn’t necessarily protect you from the Paint flaw. Since Paint is maintained through the Microsoft Store, having an up-to-date Windows installation isn’t enough if the app itself hasn’t been patched.

## Microsoft says an attacker could send a network packet to trigger the Paint flaw

Microsoft describes the bug as an “out-of-bounds read,” which means the affected code reads memory outside the area it’s supposed to access. In this case, the flaw could lead to remote code execution, which would allow an attacker to run their own code on an affected PC.

“An unauthenticated attacker could exploit this vulnerability by sending a specially crafted packet to an affected service over the network,” Microsoft [explains](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844).

The good news is that Microsoft says the vulnerability is difficult to exploit, so even if the fix is not yet applied to your PC, you’ve nothing to worry. We’re not seeing any reports of it being exploited in the wild.

## How to check your Microsoft Paint version

To see which version of Paint is installed, open Windows PowerShell and run:

powershell Get-AppxPackage -Name Microsoft.Paint | Select-Object Name, Version

Paint version 11.2609.401.0 or newer is patched, according to Microsoft’s documentation. Versions below that are considered vulnerable.

In either case, I’d recommend installing the latest Paint update available to you, even if its version number is older than the patched version listed in Microsoft’s documentation. As I noted, it’s entirely possible that Microsoft has either accidentally pulled the update for Paint or documented an incorrect version (a nonexistent version) as the patched version.
