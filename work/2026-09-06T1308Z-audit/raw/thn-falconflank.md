# extract: served via trafilatura-direct
---
title: Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon
author: The Hacker News
url: https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html
hostname: thehackernews.com
description: FalconFlank abuses CrowdStrike Falcon's malicious macro remediation to demonstrate local privilege escalation on updated Windows systems.
sitename: The Hacker News
date: "2026-09-03"
categories: ['Article']
---
The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed **FalconFlank**, a proof-of-concept (PoC) for a privilege escalation flaw impacting Crowdstrike Falcon.

"FalconFlank is a 0-day privilege escalation that abuses the office malicious macros remediation in CrowdStrike Falcon Sensor," the researcher [said](https://github.com/MSNightmare/FalconFlank) in a GitHub README file, adding the cybersecurity company may already have detections for the flaw by now.

"So if you want to test, you either have to add it to the exclusions or obfuscate the PoC and change the DLL load technique."

The PoC, the researcher added, works in a fully updated Windows 11 25H2 machine or Windows Server 2025 with CrowdStrike Falcon. In a statement shared with The Hacker News, a CrowdStrike spokesperson said they are currently investigating the report.

"We are actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting," the spokesperson said. "Customers remain protected through the Cloud Anti-malware for Microsoft Office Files settings. We refer customers to the FalconFlank Tech Alert in the CrowdStrike support portal."

The development comes days after Chaotic Eclipse released a PoC for another privilege escalation flaw impacting Kaspersky's endpoint security product for Windows (version 14.0.0.504). The exploit has been codenamed [HardBreacher](https://github.com/MSNightmare/HardBreacher).


"The PoC is not in the best shape at all, it is basically duct tapped, I just managed to make it work and that's all," the researcher said. "It will fail to run with error so you just have to keep rerunning it. If it succeeds, it will create a file in C:\Windows\System32\MY_SNAKE_IS_SOLID.dll with full permissions for the current user."

"The interesting part about this is that Kaspersky completely loses it when you take control over the UI process, you can cause it to stop functioning, grant/block access to files it's not supposed to, if the PoC succeeds, the entire operating system becomes a hot mess."

When reached for comment, Kaspersky told The Hacker News that it has resolved the HardBreacher issue. "The corresponding fix is delivered via an automatic update, or users can trigger database update manually," the company said.

Last month, the researcher also published a PoC for a Microsoft Defender zero-day called [ShieldBreak](https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html) (aka CVE-2026-69414) that could [grant an attacker](https://blog.qualys.com/product-tech/2026/08/24/shieldbreak-the-windows-defender-zero-day-with-no-patch-detect-it-mitigate-it-with-qualys) the ability to run arbitrary code with NT AUTHORITY\SYSTEM privileges. It's assessed to be a patch bypass for CVE-2026-50656 (aka RoguePlanet). Microsoft has yet to release a fix.

"Like its predecessors, ShieldBreak explores a different corner of the Windows operating system," LevelBlue [said](https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking). "Where RedSun abused the Cloud Files API and TieringEngineService to redirect a Defender write into System32, and LegacyHive weaponized offline registry hive manipulation and the NT Object Manager namespace, ShieldBreak combines Cloud Files, Object Manager namespace manipulation, direct Windows Defender API invocation, and a timing race in the remediation path."

"The result is a self-contained local privilege escalation chain in which Windows Defender's own clean engine is redirected to write an attacker-supplied DLL to C:\Windows\System32\phoneinfo.dll, followed by SYSTEM execution through the built-in Windows Error Reporting task."

Shortly after, the researcher claimed that Microsoft continues to ghost them and refuses to engage in "any sort of communication," [stating](https://blog.projectnightcrawler.dev/posts/2026-08-14-just-cut-the-lies-already/) the company is "trying hard to paint me as some insane criminal."

"I can't even report the bugs I find to their respective vendors because of the restrictions by Microsoft, all of this is of their own doing and you know, they don't even bother to check my case to figure out what's wrong," they [said](https://blog.projectnightcrawler.dev/posts/2026-08-13-what-other-options-do-i-have/) in a post dated August 14, 2026.

"Think I will start publishing bugs for third-parties in that window where Patch Tuesday isn't released yet. I just want to live like a normal human being for once in my life, is that too much to ask for...?"

### Update

Chaotic Eclipse has also released PoCs for an NVIDIA memory corruption bug called [GreenSection](https://github.com/MSNightmare/GreenSection) and a privilege escalation flaw in Gen Digital's Avast antivirus software called [PrettyPrague](https://github.com/MSNightmare/PrettyPrague). GreenSection causes any app that uses vulkan or OpenGL to crash after the PoC is executed.

"The PoC will dump the SAM database by abusing a vulnerability in Avast Sandbox and spawn a full SYSTEM shell, at the time of writing this the PoC works with fully patched Avast Antivirus + Patched Windows 11 25H2," the researcher said about PrettyPrague. "I'm not sure but I believe this vulnerability affects other Gen Digital products as well (such as AVG, Norton...)."

A Gen spokesperson shared the following statement when contacted for comment: "Gen was recently made aware of a security vulnerability affecting a subset of Gen products, including Avast Antivirus, that could allow an attacker to elevate their system privileges. We immediately initiated our security response procedures and are actively developing a patch. We take all security matters seriously and are committed to addressing this issue swiftly."

*(The story was updated after publication to include responses from CrowdStrike, Gen Digital, and Kaspersky.)*

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
