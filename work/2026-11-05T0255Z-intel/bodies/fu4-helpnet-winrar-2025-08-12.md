---
title: WinRAR zero-day was exploited by two threat actors (CVE-2025-8088) - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2025/08/12/winrar-zero-day-cve-2025-8088-attacks/
hostname: helpnetsecurity.com
description: RomCom attackers are not the only ones that have been leveraging the newly unveiled WinRAR vulnerability (CVE-2025-8088) in zero-day attacks.
sitename: Help Net Security
date: "2025-08-12"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['0-day', '7-Zip', 'APT', 'backdoor', 'BI.ZONE', 'Canada', 'cyber espionage', 'ESET', 'Europe', 'exploit', 'Russian Federation', 'spear-phishing', 'WinRAR', '0-day', '7-Zip', 'APT', 'backdoor', 'BI.ZONE', 'Canada', 'cyber espionage', 'ESET', 'Europe', 'exploit', 'Russian Federation', 'spear-phishing', 'WinRAR']
fingerprint: f1931831af26d860
---
# WinRAR zero-day was exploited by two threat actors (CVE-2025-8088)

The RomCom attackers aren’t the only ones that have been leveraging the newly unveiled WinRAR vulnerability (CVE-2025-8088) in zero-day attacks: according to Russian cybersecurity company BI.ZONE, a group tracked as Paper Werewolf has been using it to target Russian organizations.

BI.ZONE researchers may have also uncovered how RomCom and Paper Werewolf got their hands on the same exploit: it looks like it may have been offered for sale on a cybercrime forum in late June for $80,000.

WinRAR zero-day exploit for sale (Source: BI.ZONE)

### The spotted campaigns

On Monday, ESET researchers [shared](https://www.helpnetsecurity.com/2025/08/11/winrar-zero-day-cve-2025-8088/) that the attacks using **CVE-2025-8088** – a path-traversal vulnerability that affects WinRAR v7.12 and can be used for malicious code execution – were aimed at financial, manufacturing, defense, and logistics companies in Europe and Canada, and happened between July 18 and July 21.

The targets received spearphishing emails ostensibly sent by job seekers and included what seemed to be documents containing their CV.

“The vulnerability (…) uses alternate data streams (ADSes) for path traversal. The attackers specially crafted the archive to apparently contain only one benign file, while it contains many malicious ADSes (there’s no indication of them from the user’s point of view),” ESET researchers explained.

“Once a victim opens this seemingly benign file, WinRAR unpacks it along with all its ADSes. For example, for *Eli\_Rosenfeld\_CV2 – Copy (10).rar*, a malicious DLL is deployed into *%TEMP%*. Likewise, a malicious LNK file is deployed into the Windows startup directory, thereby achieving persistence via execution on user login.”

ESET’s telemetry shows that none of the targets ended up getting compromised. The researchers’ subsequent analysis has shown that the ultimate goal was to deploy a backdoor: a SnipBot variant, RustyClaw, or the Mythic agent.

“\[ESET\] researchers attribute the observed activities to RomCom with high confidence based on the targeted region, TTPs, and the malware used. RomCom (also known as Storm-0978, Tropical Scorpius, or UNC2596) is a Russia-aligned group that conducts both opportunistic campaigns against selected business verticals and targeted espionage operations. The group’s focus has shifted to include espionage operations collecting intelligence, in parallel with its more conventional cybercrime operations,” the company [noted](https://www.welivesecurity.com/en/eset-research/update-winrar-tools-now-romcom-and-others-exploiting-zero-day-vulnerability/).

“We are aware that this vulnerability has also been exploited by another threat actor, and was independently discovered by the Russian cybersecurity company BI.ZONE. Notably, this second threat actor began exploiting CVE‑2025‑8088 a few days after RomCom started doing so.”

BI.ZONE says that the spearphishing campaign delivering booby-trapped archive files containing an exploit for CVE‑2025‑8088 was aimed Russian organizations.

Prior to that, in early July, the “Paper Werewolf” threat actor also used an exploit for **CVE‐2025‐6218**, which is very similar to CVE-2025-8088. CVE‐2025‐6218 was disclosed to the WinRAR maintainers in early June 2025 and was patched in WinRAR 7.12 beta 1, released on June 10.

In both campaigns, the attackers posed as an employee at a government institution and ostensibly was making the recipient aware of a letter from one of the Russian ministries. A later campaign involved booby-trapped documents ostensibly offering information about an airline company.

### What should WinRAR users do?

With both exploited WinRAR vulnerabilities having been made public and the exploit for CVE‐2025‐6218 in who knows how many attackers’ hands, it’s highly likely that more attacks – possibly more widespread ones – will start happening soon.

The 500+ million WinRAR users are advised to download and install WinRAR 7.13, which contains fixes for both CVE‑2025‑8088 and CVE‐2025‐6218.

CVE‐2025‐6218 also affects UnRAR, the portable UnRAR source code, and UnRAR.dll, so those should be updated as well.

[ESET](https://github.com/eset/malware-ioc/tree/master/romcom) and [BI.ZONE](https://bi.zone/expertise/blog/paper-werewolf-atakuet-rossiyu-s-ispolzovaniem-uyazvimosti-nulevogo-dnya-v-winrar/) have shared indicators of compromise that can help organizations check whether they’ve been targeted in these campaigns.

### 7-Zip users should also update

A vulnerability in 7-Zip, another popular file archiver utility, has been [publicly disclosed](https://seclists.org/oss-sec/2025/q3/82) this past weekend via the OSS-SEC mailing list.

CVE-2025-55188, affecting 7-Zip versions prior to 25.01 (released in early August), may allow attackers to write arbitrary files to victim systems and execute them.

“Prior to 25.01, it was possible for a maliciously-crafted archive to create an unsafe symbolic link. 7-Zip follows symbolic links when extracting, so this leads to arbitrary file write,” the researcher who flagged the flaw explained.

They also said that exploitation can be reliably achieved if the target user uses Linux and extracts an archive file in a format for which 7-Zip supports symbolic links (such as *.zip*, *.tar*, *.7z* or *.rar*).

“This attack may also be done on Windows, but additional conditions are necessary. On Windows, the 7-Zip extraction process must have the capability to create symbolic links (e.g. extract with Administrator privileges, Windows is in Developer Mode, etc…),” they added.

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
