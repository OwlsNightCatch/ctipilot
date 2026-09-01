# extract: served via trafilatura-direct
---
title: ValleyRAT Backdoor Hides in Signed Adware That Users Add to Antivirus Exclusions
author: The Hacker News
url: https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html
hostname: thehackernews.com
description: ValleyRAT abuses signed QN Wallpaper software for DLL sideloading, disables Windows Defender, and runs inside a trusted process.
sitename: The Hacker News
date: "2026-08-31"
categories: ['Article']
---
The threat actor known as **Silver Fox** has been observed distributing the **ValleyRAT** backdoor disguised as a signed Chinese adware application, running the malware under a trusted process to slip past users who add such software to their antivirus exclusions.

Russian cybersecurity vendor Kaspersky said the attackers built the disguise around **QN Wallpaper**, a genuine Chinese desktop-wallpaper tool that in its unmodified form is adware, bundling partner apps and displaying ad banners.

Once installed, ValleyRAT (also tracked as Winos 4.0) hands the operator full control of the compromised machine. Kaspersky said the attack's geography and payload point to Silver Fox as the likely group behind it, and urged users to avoid software of questionable reputation and to keep it away from security-tool exclusions.

"This case is a clear example of how adware and affiliate networks can turn out to be far more dangerous than they appear. ValleyRAT is a sophisticated backdoor capable of collecting sensitive data such as keystrokes and clipboard contents, taking screenshots, and delivering additional malicious modules," Kaspersky said in [its analysis](https://securelist.com/valleyrat-backdoor-adware/121175/).

The disguise relies on DLL sideloading. The installer unpacks a modified copy of QN Wallpaper and runs its signed executable, `QnWallpaper.exe`, which loads a malicious `libcef.dll` planted in the same directory. With the library executing inside a legitimately signed process, the backdoor runs without triggering controls that trust the signature.


Before the adware component starts, the installer switches off Windows Defender through the `DisableAntiSpyware` registry key and adds the program to the system's autorun entries. When the logged-in user lacks administrator rights, the malware relaunches itself with `runas` to acquire them.

ValleyRAT can also flag its own process as critical, so that any attempt to terminate it triggers a blue screen of death.

Kaspersky shared the following indicators of compromise (IoCs) -

- **Hashes (MD5):**`c24e99f9437feacaa63766a3cde3fe3d` (the submitted installer),`07ddbbe2c71c45577a7a4fbcdba0df91` (the malicious`libcef.dll` ), and`8a626d844943da3456b044f38deae3a2`
- **Command-and-control servers:** 103.45.66.18 on ports 441, 442 and 443, and 192.253.225.173 on ports 6666 and 8888
- **Domains in the chain:** qnwallpaper[.]keansoft[.]cn, the abused adware's download site, and meeting[.]tencent[.]com, a legitimate page opened as a decoy
- **Host artifacts:** the`DisableAntiSpyware` registry value and the install directory`C:\Program Files\QNWallpaper\5.4.0.1662\`

DLL sideloading through signed, legitimate software is an established part of Silver Fox's toolkit. In a campaign against a Japanese manufacturer about five weeks earlier, [Cato Networks documented](https://www.catonetworks.com/blog/cato-ctrl-silverfox-evolves/) what it called the group's "newly observed abuse of legitimate applications for DLL sideloading," and the same `libcef.dll` filename had already featured in [a 2025 ValleyRAT loader](https://thehackernews.com/2025/01/pngplug-loader-delivers-valleyrat.html).

Kaspersky itself tracked the group in [an earlier tax-themed campaign](https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html) against organizations in India and Russia.

Kaspersky's account is based on a single installer submitted by a customer; its advertising features stay inert while the infection chain runs, and the report stops short of attaching a victim count to the adware route.

Across 2026 the vendor recorded more than 100,000 detections of ValleyRAT and associated malware affecting over 1,500 unique users, mostly in China and India, a figure spanning all of the year's ValleyRAT activity rather than this campaign alone.

Kaspersky also urged organizations to set clear policies on third-party software on work devices and to keep staff aware of the threat.

"For individual users, we recommend avoiding the installation of software with a questionable reputation, and, even more importantly, never adding such software to your security solutions' exclusion lists," the company said.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
