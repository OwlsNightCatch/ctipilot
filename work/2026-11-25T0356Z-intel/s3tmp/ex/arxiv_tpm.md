---
title: "Hello Again: Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs"
author: Christian Werling; Matti Finder; Hans Niklas Jacob; Julian Prein; Niclas Kühnapfel; Jean-Pierre Seifert
url: https://arxiv.org/abs/2611.18126v1
hostname: arxiv.org
description: "Windows Hello is the primary authentication mechanism on over one billion Windows 11 devices, supporting PINs as short as four digits. Such low-entropy PINs are viable only because the TPM's anti-hammering protection mitigates brute-force attacks. Most modern x86 platforms rely on firmware TPMs (fTPMs) that persist their non-volatile (NV) state, including the lockout state, to SPI flash. On newer platforms, rollback prevention of this state is delegated to the flash chip via Replay Protected Monotonic Counters (RPMCs), a JEDEC-standardized mechanism operating over a physically accessible bus. We present the first practical security analysis of RPMC in shipping x86 systems. Using low-cost interposer hardware, we identify multiple implementation flaws, two of which fundamentally undermine RPMC's security model: First, Winbond SPI flash - the leading NOR flash vendor with over 25% market share - leaks its HMAC key under voltage glitching, enabling arbitrary counter forgery. Second, AMD's NV controller does not verify RPMC increments, so an interposer can suppress them unnoticed. Moreover, AMD platforms without RPMC flash appear to lack NV rollback protection altogether: on two AMD desktops, reflashing an old image resets the fTPM's lockout counters. Both flaws enable rollbacks of the fTPM's NV state (AMD, Intel, or Pluton), including its lockout counters. We demonstrate this end-to-end on locked, encrypted hardware: our setup finds a 4-digit Windows Hello PIN in 40 hours instead of 69 days. A compromised PIN also grants access to device-bound keys and Hello-based enterprise SSO. The same primitive defeats BitLocker's TPM+PIN pre-boot protector, reducing the worst-case time for a default-length 6-digit PIN from 19 years to 20 days."
sitename: arXiv.org
date: "2026-11-13"
fingerprint: "349c811b14e3568f"
license: CC BY 4.0
language: en
image: https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-fb.png
pagetype: website
filedate: "2026-11-25"
---
# Computer Science > Cryptography and Security

\[Submitted on 13 Nov 2026\]

# Title:Hello Again: Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs

[View PDF](https://arxiv.org/pdf/2611.18126)

[HTML (experimental)](https://arxiv.org/html/2611.18126v1)

> Abstract:Windows Hello is the primary authentication mechanism on over one billion Windows 11 devices, supporting PINs as short as four digits. Such low-entropy PINs are viable only because the TPM's anti-hammering protection mitigates brute-force attacks. Most modern x86 platforms rely on firmware TPMs (fTPMs) that persist their non-volatile (NV) state, including the lockout state, to SPI flash. On newer platforms, rollback prevention of this state is delegated to the flash chip via Replay Protected Monotonic Counters (RPMCs), a JEDEC-standardized mechanism operating over a physically accessible bus.
>
> We present the first practical security analysis of RPMC in shipping x86 systems. Using low-cost interposer hardware, we identify multiple implementation flaws, two of which fundamentally undermine RPMC's security model: First, Winbond SPI flash - the leading NOR flash vendor with over 25% market share - leaks its HMAC key under voltage glitching, enabling arbitrary counter forgery. Second, AMD's NV controller does not verify RPMC increments, so an interposer can suppress them unnoticed. Moreover, AMD platforms without RPMC flash appear to lack NV rollback protection altogether: on two AMD desktops, reflashing an old image resets the fTPM's lockout counters.
>
> Both flaws enable rollbacks of the fTPM's NV state (AMD, Intel, or Pluton), including its lockout counters. We demonstrate this end-to-end on locked, encrypted hardware: our setup finds a 4-digit Windows Hello PIN in 40 hours instead of 69 days. A compromised PIN also grants access to device-bound keys and Hello-based enterprise SSO. The same primitive defeats BitLocker's TPM+PIN pre-boot protector, reducing the worst-case time for a default-length 6-digit PIN from 19 years to 20 days.

## Submission history

From: Christian Werling \[
[view email](https://arxiv.org/show-email/f6d89120/2611.18126)\]

**\[v1\]**Fri, 13 Nov 2026 12:53:55 UTC (1,565 KB)

### Additional Features

### References & Citations

Loading...

# Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

# Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

# Demos

# Recommenders and Search Tools

Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))*

CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))*

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
