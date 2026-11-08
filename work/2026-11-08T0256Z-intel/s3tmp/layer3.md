---
title: Residential Proxies Detected on White House Network
author: Layer
url: https://layer3intel.com/blog/residential-proxies-white-house-network
hostname: layer3intel.com
description: "Our new Residential Proxy Observatory shows residential proxy traffic exiting the White House network: 236 times in 30 days, through 28 public proxy services."
sitename: Layer3 Intel
date: "2026-11-04"
categories: ['Research']
tags: ['residential proxy detection, residential proxy, proxy detection, VPN detection']
fingerprint: f723f235b0286241
---
Our [Residential Proxy Observatory](https://layer3intel.com/context), launched earlier this week, is a first-of-its-kind interface that gives researchers a global view of residential proxy and anonymized internet activity.

While our team was looking through it, we noticed residential proxy exit activity on [AS2650](https://layer3intel.com/context/AS2650). AS2650 is registered to the Executive Office of the President, the federal agency that hosts the White House network. [Residential proxy services](https://layer3intel.com/what-is-a-residential-proxy) sell access to everyday devices, letting customers send traffic through them so it appears to come from that device's network.

## What we observed

From October 5 to November 3:

- Our residential proxy enumeration pipeline exited through the White House network **236 separate times**.
- Those exits came from **6 addresses**, on **26 of the 30 days**.
- **28 separate residential proxy services** were able to exit through this network.

To make sure this was not a fluke, we checked these addresses against other residential proxy detection services, such as Spur and Synthient. Their public IP context pages independently identify these addresses as residential proxy exits.

This is public access. Anybody can obtain it by signing up to a public residential proxy service, paying a few dollars and sending requests through it. We did not selectively target this network or try to make our probes exit from it. We caught this by chance, simply by requesting global rotating access through these services.

## Why this is concerning

Most of the activity happens in the evening, Eastern time: about half of it falls between 5 p.m. and midnight, and almost none happens in the early morning. That pattern suggests a person rather than a public guest Wi-Fi network: someone regularly on the White House network late into the evening, whose device is infected with a proxy SDK. Our data shows the exits, not the device or the person behind them.

Past research has shown that poorly secured proxy SDKs can allow internal network access and lateral movement. This is how past botnets have spread. In [A Broken System Fueling Botnets](https://synthient.com/blog/a-broken-system-fueling-botnets), the researchers at Synthient documented how the Kimwolf botnet reached at least 2 million devices, mostly Android devices with an exposed ADB service, through residential proxy networks. If an SDK on this network has the same kind of flaw, anyone buying proxy access could use it to reach internal systems.

## No place is too remote

The White House is not the only surprise in the observatory. Residential proxies also reach some of the most isolated places on the planet.

[Saint Helena, Ascension and Tristan da Cunha](https://layer3intel.com/context/country/SH) is the South Atlantic territory that includes the most remote inhabited island in the world. We recorded **413 addresses** and more than **32,000 observations** there, split between Starlink and the island's local internet provider, Sure Saint Helena.

We also recorded **three observations** from [Antarctica](https://layer3intel.com/context/country/AQ). All of them come from a Cloudflare WARP address that points to McMurdo Station.

Other remote places with activity:

- [Pitcairn](https://layer3intel.com/context/country/PN): 1 Starlink address, 1 observation.
- [Norfolk Island](https://layer3intel.com/context/country/NF): 1 Norfolk Telecom address, 4 observations.
- [Svalbard](https://layer3intel.com/context/country/SJ): 1 Starlink address in Longyearbyen, 3 observations.
- Also seen: [the Falklands](https://layer3intel.com/context/country/FK) (388 addresses), [the Chagos Islands](https://layer3intel.com/context/country/IO) (43), [Tokelau](https://layer3intel.com/context/country/TK) (21) and [South Georgia](https://layer3intel.com/context/country/GS) (7).

Residential proxies have infected every corner of the world, and it looks like there is no place they cannot reach. Layer3 Intel tracks residential proxy and anonymization infrastructure worldwide. Even when the proxies hide in networks on the farthest corners of the planet, we can still observe them, leaving threat actors no place to hide.

**For relevant agencies:**We have backed up the raw logs of the recorded activity and are willing to share them. You can request them through our

[contact page](https://layer3intel.com/contact).
