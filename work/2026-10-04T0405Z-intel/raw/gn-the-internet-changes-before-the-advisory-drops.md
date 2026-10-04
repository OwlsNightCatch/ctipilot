---
title: The Internet Changes Before the Advisory Drops
author: GreyNoise April
url: https://www.greynoise.io/blog/the-internet-changes-before-the-advisory-drops
hostname: greynoise.io
description: GreyNoise identifies statistically significant pre-disclosure attack surges, revealing early signals for 33 CVEs across 16 vendors in their latest report Ten Days Before Zero.
sitename: greynoise.io
date: "2026-04-20"
---
Before Cisco published its advisory for CVE-2026-20127 — a CVSS 10.0 zero-day cited in a Five Eyes joint warning — GreyNoise sensors had already observed eight distinct surges of Cisco-targeting activity. The earliest arrived 39 days before disclosure. Each one came closer than the last. A new study finds this pattern is not an anomaly.


## What the Data Shows

Over 103 days, GreyNoise tracked 147.8 million sessions across 276 vendor-specific tags covering 18 network infrastructure vendors. Of 104 detected surge events, 68 preceded a vendor-matched CVE — spanning 33 vulnerabilities across 16 vendor families. Statistical testing confirmed the pattern is not coincidence.

- **Median lead time: 11 days.** 49% of surges arrived within 10 days of disclosure. 78% within 21 days.

- **Session volume is the primary signal.** Session volume carries the early warning. IP count alone is a weaker predictor, but when both spike simultaneously, the warning is highest confidence and the lead time extends to 21 days.

- **Countdown compression.** SonicWall CVE-2026-0400: six surges from 37 to 3 days, peaking at 69x median volume. Fortinet CVE-2026-24858 (CVSS 9.4, zero-day): one day of warning.

- **Concentrated targeting shortens the window.** Distributed surges averaged 21.3 days of lead. Concentrated hosting surges: 7.5 days. 11 ASNs appeared across 3+ vendor families.


## Why This Matters

Mandiant's M-Trends 2026 found that mean time-to-exploit has gone negative. VulnCheck documented that 28.96% of KEVs in 2025 were exploited on or before publication day. The traditional model — wait for the advisory, then act — leaves a measurable gap. The signals that narrow that gap are already visible in GreyNoise data.

Download GreyNoise's [Ten Days Before Zero](https://www.greynoise.io/resources/ten-days-before-zero?utm_campaign=42512031-Gated-Report-Ten-Days-Before-Zero&utm_source=blog-cta) report to discover the full findings.


## What's Inside the Report

- 33 paired CVEs across 16 vendor families with lead times and attack-type decomposition
- Countdown compression case studies: Cisco, SonicWall, Fortinet, Ivanti, MikroTik
- Infrastructure analysis: 11 cross-vendor ASNs, 4 attacker clusters, phase transitions
- Statistical methodology and validation approach
- Actionable framework for integrating pre-disclosure signals into patch prioritization



[Read the full report](https://www.greynoise.io)
