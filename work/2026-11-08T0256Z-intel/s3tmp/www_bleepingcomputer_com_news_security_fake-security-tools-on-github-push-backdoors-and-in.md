---
title: Fake security tools on GitHub push backdoors and infostealers
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/
hostname: bleepingcomputer.com
description: Cybersecurity professionals are being targeted with infected security projects on GitHub that deploy a backdoor and information stealer malware.
sitename: BleepingComputer
date: "2026-11-06"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, AsyncRAT, Clipper, GitHub, Info Stealer, Information Stealer,virus removal, malware removal, computer help, technical support']
fingerprint: "377c3d599e36a646"
---
Cybersecurity professionals are being targeted with infected security projects on GitHub that deploy a backdoor and information stealer malware.

The campaign started about two years ago and initially targeted crypto wallet users, but recently the threat actor switched focus and published malicious repositories for automating scans, security testing, and log analysis.

Researchers at cybersecurity company Dr. Web found that more than 2,000 Windows systems have been compromised so far.

One malicious repository they found is a fake script advertised as a lightweight solution to parse, clean, and format output from the Fscan network scanner.

Previous lures included blockchain games, bots, and cheat tools, typically targeting blockchain and game enthusiasts.

Dr. Web's investigation found malicious code embedded in Visual Studio project files, Python scripts, and Go source files, hidden behind long stretches of whitespace, an old technique that still proves effective.

In some Visual Studio projects, a pre-build event routine runs the code before compilation, the [researchers say](https://news.drweb.com/show/?i=15311&lng=en&c=5).

The infection chain uses PowerShell to retrieve an encrypted download link that fetches a modular Electron-based loader named ‘Microsoft.exe.’

The loader establishes persistence on the infected host, elevates its privileges, disables Windows security and recovery features, and injects the next-stage (malware) into legitimate processes.

Dr. Web describes six evasion techniques in the loader’s Mode3 mode, which is its default operational mode:

1. Makes explorer.exe appear to be the malware’s parent process
2. Changes a Windows registry value to disable Smart App Control
3. Restores original ntdll.dll code from disk to remove hooks added by security software
4. Makes direct Windows system calls that are harder for security tools to intercept
5. Patches EtwEventWrite in memory to suppress event tracing in the affected process
6. Patches AmsiScanBuffer in memory to interfere with antivirus scanning of scripts

If that mode fails to launch, the loader uses Mode2, which adds Microsoft Defender exclusions and uses a PowerShell script to decrypt and inject the payloads into ‘RegAsm.exe.’

The final payloads delivered to the host are the AsyncRAT backdoor, clipper malware that replaces crypto wallet addresses in the clipboard, and an information stealer.

The infostealer collects browser data, VPN settings, FTP client configuration files, gaming account data, and Discord tokens, and exfiltrates the details through a Telegram bot.

According to Dr. Web, the malware also attempts to remove ESET, McAfee, and Malwarebytes antivirus tools from the infected computer, tries to disconnect them from their update servers, and also interferes with Windows backups.

Dr. Web researchers also found a seemingly unfinished component that could help keep the loader running and download it again if it was removed from the host’s disk.

This finding suggests that the threat actor is working to improve the malware with new features. The researchers [shared a complete list of indicators of compromise](http://github.com/DoctorWebLtd/malware-iocs/blob/master/Trojan.Loader.3261/README.adoc) observed in this campaign.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
