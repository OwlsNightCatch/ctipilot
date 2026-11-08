---
title: White House Network Appears in Global Residential Proxy Traffic - Security Affairs
author: Pierluigi Paganini
url: https://securityaffairs.com/202563/security/white-house-network-appears-in-global-residential-proxy-traffic.html
hostname: securityaffairs.com
description: Layer3 found residential proxy traffic using the White House network, raising concerns about potential exposure of internal systems.
sitename: Security Affairs
date: "2026-11-06"
categories: ['Breaking News', 'Malware', 'Security']
tags: ['Kimwolf botnet']
fingerprint: f723db5df028f0c3
---
Layer3 Intel says it found residential proxy traffic leaving through the White House network. The researchers spotted it while browsing their new Residential Proxy Observatory, a tool that gives a global view of residential proxy and anonymized internet activity.

“While our team was looking through it, we noticed residential proxy exit activity on [AS2650](https://layer3intel.com/context/AS2650). AS2650 is registered to the Executive Office of the President, the federal agency that hosts the White House network.” reads the [report](https://layer3intel.com/blog/residential-proxies-white-house-network) published by Layer3.

A residential proxy service allows customers to use everyday devices to route their internet traffic. This makes their activity look as if it comes from the device’s normal home internet connection. Layer3 detected this activity on AS2650, a network registered to the Executive Office of the President, the agency responsible for the White House network. Layer3 has not accused anyone at the White House of wrongdoing and says its data cannot identify who or what caused the activity.

Between October 5 and November 3, Layer3 detected 236 connections through this network. The traffic came from six IP addresses and was recorded on 26 of those 30 days. A total of 28 residential proxy services were able to use the network. To check their findings, researchers compared the IP addresses with data from other security services, including Spur and Synthient. Both services also identify these addresses as residential proxy exit points.

Getting this data took no special skill. Anyone can sign up to a public residential proxy service, pay a few dollars and send requests through it. Layer3 says it didn’t target the network or try to steer its probes there, and it caught the activity by chance, simply by requesting global rotating access through these services.

The timing suggests something more than a guest network. About half the activity falls between 5 p.m. and midnight Eastern time, and almost none happens in the early morning. Layer3 reads that as a person, not public guest Wi-Fi: someone regularly on the White House network late into the evening whose device carries a proxy SDK, a software kit that turns a device into an exit point.

*“Past research has shown that poorly secured proxy SDKs can allow internal network access and lateral movement. This is how past botnets have spread. In [A Broken System Fueling Botnets](https://synthient.com/blog/a-broken-system-fueling-botnets), the researchers at Synthient documented how the Kimwolf botnet reached at least 2 million devices, mostly Android devices with an exposed ADB service, through residential proxy networks.” continues the report. “If an SDK on this network has the same kind of flaw, anyone buying proxy access could use it to reach internal systems.”*

That matters because poorly secured proxy SDKs have let attackers into internal networks before. Synthient’s research, [A Broken System Fueling Botnets](https://synthient.com/blog/a-broken-system-fueling-botnets), documented how the [Kimwolf botnet](https://securityaffairs.com/tag/kimwolf-botnet) reached at least 2 million devices, mostly Android devices with an exposed ADB service, through residential proxy networks. If an SDK on the White House network has the same kind of flaw, anyone buying proxy access could reach internal systems. Layer3 doesn’t claim that’s the case here, and it describes the risk as conditional.

The White House isn’t the only surprise. The observatory also finds residential proxies in some of the most isolated places on the planet. Saint Helena, Ascension and Tristan da Cunha, a South Atlantic territory that includes the most remote inhabited island in the world, shows 413 addresses and more than 32,000 observations, split between Starlink and the local provider, Sure Saint Helena.

Layer3 also detected three instances of proxy activity in Antarctica. All came from a Cloudflare WARP address linked to McMurdo Station. The researchers jokingly noted that penguins are not suspects. On Pitcairn Island, they found one Starlink address and one observation. Norfolk Island had one Norfolk Telecom address with four observations, while Svalbard had one Starlink address in Longyearbyen with three observations.

The researchers also found 388 addresses in the Falkland Islands, 43 in the Chagos Islands, 21 in Tokelau and seven in South Georgia. These findings suggest that residential proxy networks now operate in almost every corner of the world. For security teams, the main concern is that devices connected to protected networks could unknowingly become proxy exit points, potentially exposing those networks to outside traffic.

However, Layer3 says its data only shows where proxy traffic exits. It cannot identify the device being used or the person behind it. As the company explains, “Our data shows the exits, not the device or the person behind them.”

*“Residential proxies have infected every corner of the world, and it looks like there is no place they cannot reach. Layer3 Intel tracks residential proxy and anonymization infrastructure worldwide. Even when the proxies hide in networks on the farthest corners of the planet, we can still observe them, leaving threat actors no place to hide.” concludes the report.*

**Follow me on Twitter: @securityaffairs and Facebook and Mastodon**

**(SecurityAffairs – hacking, proxy traffic)**
