---
title: New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs in Days, Not Years
author: The Hacker News
url: https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
hostname: thehackernews.com
description: Researchers demonstrate physical attacks that bypass TPM PIN lockouts on AMD and some Intel PCs, exposing Windows Hello and BitLocker PINs.
sitename: The Hacker News
date: "2026-11-18"
categories: ['Article']
tags: ['AMD', 'BitLocker', 'hardware security', 'Trusted Platform Module', 'Vulnerability', 'Windows Security']
fingerprint: "3496511d45a54246"
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpsv4GxAUbzCsIV1umrxZs6VxfD1eFwAeCgRHQQG_dNbP1fLiYe48hM-Wbd_8w5IxlacAwoidLqyQgBmG7YD7qKo0_XcqW2GhggfXshuK1uXz8BOma2H0Jjs8fabCO4IxHBfRopEUFDd0xHRRv43gMeog852Usv40sfcTwnO_9coyxtIMmteJxeJI_oPA/s1700-nu-rw-lo-l85-e365/bitlocker.jpg
pagetype: article
filedate: "2026-11-25"
---
On AMD-based PCs and some Intel PCs, the TPM lockout for **Windows Hello** and **BitLocker** PINs can be reset by someone who opens the PC's case, researchers at Technische Universität Berlin say.

That leaves short PINs open to guessing. In lab tests, the researchers found a four-digit Hello PIN on an AMD laptop and a 6-digit BitLocker PIN on an Intel laptop this way.

Both PINs were set by the researchers and found within 236 tries. From the speeds they measured, they calculate a worst-case of 40 hours for a four-digit Hello PIN, compared to 69 days with the lockout working as documented. For a default six-digit BitLocker PIN, the worst-case time drops from 19 years to 20 days.

AMD confirmed yesterday that its processor firmware has a flaw that allows the attack on some PCs with its chips. It plans fixes for most of those chips between November and February 2027. For now, the researchers advise adding at least two digits to Hello and BitLocker PINs.

The TPM in these PCs is a firmware TPM, built into the processor. Unlike a separate TPM chip, it has no secure storage of its own, according to the [research paper](https://arxiv.org/abs/2611.18126v1) the researchers posted late last week. So it keeps its saved state, including the count of wrong guesses, encrypted on the mainboard's flash chip.

If someone copies that saved state and later writes the old copy back, the count goes back too, unless the PC detects it. Newer PCs try to catch this with counters inside the flash chip, called RPMC, that can only go up.

On AMD PCs that use these counters, the processor's firmware never verifies that a counter actually increased. A small board placed between the processor and the flash chip can block the update and report success, causing the PC to accept the old state.

RPMC chips from flash maker Winbond have a different weakness, the researchers found. A brief drop in the chip's power supply, called a voltage glitch, can cause the chip to reveal the secret key that signs its counter values. With that key, which took about a second to extract with their best settings, the board can forge any counter value.

On the Intel laptop they tested, one glitch was enough: the laptop's firmware feeds the chip the same value at every boot, so the leaked key kept working after each restart.


For the Hello test, the researchers attacked a locked HP OmniBook 3 with an AMD Ryzen AI 5 330 processor and a BitLocker-encrypted drive. Their setup typed PINs from 1000 upward and reached the correct one, 1235, after 236 tries in 57 minutes.

Windows still forced a restart after every 5 incorrect PIN attempts on that laptop, but no lockout delay was applied. Microsoft's [lockout defaults](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/tpm-fundamentals) lock the TPM after 32 wrong tries and forget one failure every 10 minutes.

The BitLocker test ran on a Framework Laptop 13 with an Intel Core Ultra 5 125H processor and Winbond flash. BitLocker's startup prompt adds no limit of its own, so each reset gave a fresh 32 tries. The setup found the PIN, 123457, after 236 tries in 6 minutes and 55 seconds.

In both tests, the researchers took the flash chip off the mainboard and wired in their own board. A script read the screen, typed PINs, and restarted the laptop through a KVM switch. They also changed firmware settings to slow each laptop's link to the flash chip, because their board could not keep up at full speed.

The researchers make two further claims that their tests did not cover. Either method could be used against either PIN. A recovered Hello PIN can also unlock keys tied to the device and enable Hello-based single sign-on at work, and, in some configurations, pass a multi-factor check.

The researchers have published their attack firmware, board designs, and scripts. They say reproducing the RPMC attacks is not plug-and-play and needs one of their boards. Neither the paper nor the vendor notices published so far describe attacks outside the lab.

### Which PCs the Attack Works On and What Vendors Say

Whether the attack works depends on the processor and the flash chip:

- **AMD-based PCs with RPMC flash:** open to the board that blocks counter updates. The chipmaker has confirmed the firmware flaw behind this and plans to fix it.
- **AMD-based PCs without RPMC flash:** on two AMD desktops in the researchers' tests, writing an old copy back with an ordinary flash programmer reset the count, requiring no board. They conclude that AMD processors likely have no other protection against this, though two desktops may not be representative of all AMD systems.
- **PCs that rely on Winbond RPMC flash:** the researchers say these are open to the leaked-key method whatever the processor, and that only a new chip design can fix it.
- **Intel PCs without RPMC-like flash:** three Intel systems detected the same write-back in those tests.

The researchers expect the AMD firmware flaw to affect AMD PCs that use the Microsoft Pluton security core as their TPM, but did not show this.

On an AMD PC, the owner can boot Linux, for example from a live USB stick, and run the command grep . /sys/bus/pci/drivers/ccp/\*/rpmc\_\* from the researchers' [exposure check](https://github.com/mattifinder/rpmc_attacks). The output indicates whether RPMC flash is present and enabled, which tells the owner which of the two methods applies. Missing files do not mean the PC lacks RPMC.

For Intel PCs, the researchers know of no such check. Owners would have to open the PC and look for a Winbond chip marked 25R or 74M.

AMD tracks the flaw as CVE-2026-43613 and assigns it a CVSS score of 5.1 in a [security bulletin](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7079.html) published yesterday.

The chipmaker says attacks requiring physical access fall outside its product security threat model, but that "RPMC is intended to stop this type of interposer attack." The researchers first told it about the flaw in February.

The chipmaker's fix targets run from November to February 2027 across Ryzen, Ryzen AI, Ryzen Threadripper, Athlon and EPYC chips, and one unnamed product has no date yet. These are planned dates for its own firmware, not updates already out for PCs.

The bulletin does not cover AMD PCs without RPMC flash. It also does not say whether the update will prevent an attacker from installing older, unfixed firmware on the PC, which the researchers say a fix must prevent.

Intel, whose processor was in the BitLocker test laptop, said in a [security announcement](https://www.intel.com/content/www/us/en/security-center/announcement/intel-security-announcement-2026-11-16-001.html) earlier this week that the research "did not demonstrate a vulnerability in an Intel component". That matches the tests, in which the attack on the Intel laptop needed the Winbond chip's flaw.

According to the researchers, Intel's security team called the reused value a weakness rather than a vulnerability.

The researchers told Microsoft in April. According to them, the company rated the Windows Hello report as "moderate severity" and below its bar for an immediate fix, issued no CVE or bounty, and committed to raising its recommended minimum Hello PIN length to six digits.

At the company's request, the researchers filed the BitLocker finding as a separate report for a different team. The company declined to give them any further written statement for the paper.

Separately, a Windows 11 test build released late last week makes six digits the minimum for personal-account Hello PINs, with an option to use four. The [release notes](https://learn.microsoft.com/en-us/windows-insider/release-notes/experimental-future-platforms/preview-build-29708-1003) give no reason, and features in that test channel may never reach regular releases.

According to the researchers, Winbond was first told about its chips' weakness to voltage glitches in January 2025 and received a second report in April showing that a glitch also leaks the key. The flash maker is studying the issue, possibly including a new chip design, but has not committed to a fix or a date.

### What Owners and Admins Can Do

Two extra digits make a large difference in the researchers' figures:

| Worst-case time to find a numeric PIN |  |  |  | 
|---|---|---|---|
| PIN length | With the documented lockout | Hello attack (AMD laptop) | BitLocker attack (Intel laptop) | 
|---|---|---|---|
| 4 digits | 69 days | 40 hours | 5 hours\* | 
| 6 digits | 19 years | 168 days | 20 days | 
| 8 digits | 1,903 years | 46 years | 6 years | 

\* *BitLocker accepts a four-digit PIN only if an admin lowers the six-digit minimum. The times are worst cases calculated from speeds measured on one laptop each.*

In May, Microsoft advised moving BitLocker from TPM-only to TPM+PIN to block the YellowKey bypass, as part of its [YellowKey mitigation](https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html). The same TPM lockout guards that PIN.

Steps for each setup:

- **Windows Hello for Business:** raise the *Minimum PIN length* policy, under Computer Configuration > Administrative Templates > System > PIN Complexity. If it is not set, Windows requires six digits, a worst case of 168 days in the table above, and admins can set it as low as four. The [PIN policy settings](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/policy-settings) page lists it on the PIN settings tab.
- **BitLocker:** raise the *Configure minimum PIN length for startup* policy, which allows 4 to 20 digits and requires six by default. Turning on *"Allow enhanced PINs for startup*" lets letters and symbols, which the [BitLocker PIN guidance](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq) recommends for older hardware.
- **AMD-based PCs:** install the firmware update with the chipmaker's fix when one is available for your PC. Until then, the chipmaker advises keeping PCs under physical control and watching for signs of tampering.
- **PCs that rely on Winbond RPMC flash:** the flash maker has not committed to a fix, according to the researchers. Intel advises its customers to ask their PC maker about updates.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
