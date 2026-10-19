---
title: "One Parser, Two Bugs, Many Routers: Exploiting Broadcom WiFi Across eCos and Linux"
author: Qkaiser
url: https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/
hostname: quentinkaiser.be
description: A vulnerability in Broadcom’s proprietary WPS implementation enables unauthenticated attackers within WiFi range to leak memory and achieve unauthenticated remote code execution on millions of routers. This post covers its discovery through agentic vulnerability research, exploitation across eCos and Linux platforms, its impact on the global router supply chain, and a disclosure process rather … interesting.
sitename: QTNKSR
date: "2026-10-16"
fingerprint: b669a7176f2033c1
---
Photo by [Hasan Almasi](https://unsplash.com/@hasanalmasi) on [unsplash](https://unsplash.com/photos/gray-and-white-brick-tunnel-3DlYPd91ln4)

*This post is the long-form version of the talk I gave at [Hexacon in Paris on October 16th, 2026](https://www.hexacon.fr/conference/speakers/#one_parser_two_bugs).*

A vulnerability affecting Broadcom’s proprietary implementation of 802.11 has been present in their SDK since [at least 2010](https://github.com/shantanugoel/asus-rt-n66u-merlin/blob/ede220728e1eb417b4cc88912738b4311abdc088/release/src-rt/wps/common/ap/ap_eap_sm.c#L4). An incomplete patch was silently released in 2018, followed by Broadcom’s recommendation to move to `hostapd` instead, making it a definitive forever day on eCos-based platforms (BCM3380, BCM3383, BCM33834) and a potential forever day on Linux platforms (BCM3390, BCM65xx, BCM68xx) unless affected Original Equipment Manufacturers (OEMs) are willing to migrate.

The vulnerability can be triggered remotely over WiFi without knowledge of the network key or completion of a normal WPS enrollment. Exploitation provides controlled information disclosure and arbitrary code execution.

It affects dozens of vendors, hundreds of products, and millions of Broadcom-based access points worldwide. In an effort to discover all affected vendors and devices, I’m providing [a fingerprinting script and YARA rule](https://github.com/qkaiser/broadcom-wps/) so you can help me document the blast radius.

According to Broadcom’s own response, they’ve known about the bug since 2018 and they’ve received information about it from other external entities. Yet they refused to assign a CVE to this vulnerability or to communicate publicly about it which is probably the reason why so many OEMs did not patch

I demonstrated that the vulnerability is present and exploitable on 3 out of 4 Belgian Internet Service Providers including Proximus (BBOX 3V+), VOO (Netgear CG3100, Netgear CG3700, Technicolor 7210, CGA4233) and Orange (ASKEY TCG3000). Telenet may be affected through Sagemcom F@st devices, but I could not get my hands on one.

As of October 15th, 2026, none of these affected devices have been patched. This means you can get a root shell from across the street on a significant proportion of routers in Belgium, and probably elsewhere.

### Demos

In the video below I’m exploiting an Orange Belgium CPE (the ASKEY TCG3000). The exploit gains unauthenticated remote code execution, and the arbitrary shellcode I’m executing fetches the PSK from NVRAM and sends it back to the attacker over 802.11. Finally, I’m joining the network using the leaked key to demonstrate the target is stable and the PSK is correct.

Don’t be fooled by the antenna proximity. This attack works over long distances.

In the video below I’m exploiting a Proximus CPE (the BBOX3V+ aka Sagemcom F@st). The exploit gains unauthenticated remote code execution. I’m using this capability to get a reverse shell over 802.11 frames, so no need for a C2 in the cloud!

## Slides

Slides from my talk are available [here](https://quentinkaiser.be/assets/qkaiser-broadcom-wps-hexacon-2026.pdf); they go into agentic vulnerability research, Broadcom’s eCos and Linux-based implementation of 802.11 parsing, the bug itself, exploitation primitives, chaining, supply chain security and affected devices.

## Guesstimation

I did some napkin math with my friend Sol using data published by the IBPT and public communication from the ISPs about model release over the years. I have medium confidence in these numbers; hopefully the ISPs will start communicating about the exact number of affected devices once this hits the Internet.

| ISP | Subscribers | Estimated Affected Gateways | Affected Models | 
|---|---|---|---|
| Proximus | 2.318.000 | 850.000 | BBOX 3, BBOX3V+ | 
| VOO (legacy fleet) | \~500.000 | 500.000 | Netgear CG3100, Netgear CG3700, Technicolor TC7210, CGA4233 | 
| Orange Belgium | \~547.000 | 210.000 | ASKEY TCG3000 | 
| Telenet | \~1.758.000 | ? | F@ST3896LG (To be confirmed), F@ST5685LGB (To be confirmed) | 

## Disclosure Timeline

I followed a strict 90-day disclosure policy and the clock started ticking when I sent the report on 18/07/2026. All parties were informed of the disclosure deadline on 16/10/2026.

I did not want to use shorter timelines because it would have been *unfair* to ISPs, even though the “vulnpocalypse” should really push us towards shorter disclosure timeline. Similarly, I did not want to provide an extended deadline because it has been abused in the past by vendors and Internet Service Providers, and has only led to partial mitigation being deployed after 9 months or more.

- **18/07/2026** - sent KS-20260718-02 report to Broadcom PSIRT (WPS EAP reassembly overflow on BCM3380, BCM3383, BCM33834)
- **27/07/2026** - sent KS-20260727-01 report to Broadcom PSIRT (WPS EAP reassembly overflow on BCM3390, BCM65xx, BCM68xx)
- **28/07/2026** - Broadcom answers that a patch is available, and that if I find affected devices I should reach out to the manufacturer telling them to contact Broadcom.
- **29/07/2026** - Follow-up with Broadcom. They refuse to register a CVE or to provide a copy of the notification they sent to OEMs through the Broadcom Customer Portal.
- **29/07/2026** - Sent detailed report to Proximus through their CVD form
- **29/07/2026** - Attempt to establish contact with Orange Belgium
- **29/07/2026** - Attempt to establish contact with VOO (which is now Orange, but you never know)
- **29/07/2026** - Sent report and toolkit to Cyber Security Center Belgium so they can reach out to unresponsive ISPs.
- **29/07/2026** - Proximus requests access to the full report, I send it.
- **04/08/2026** - I open a case at CERT/CC through VINCE. Case closed on the same day due to Broadcom being a CVE Numbering Authority and its unwillingness to register a CVE.
- **18/08/2026** - Orange Belgium CISO follows me on LinkedIn now. Still no answer from Orange.
- **25/08/2026** - Follow-up call with Proximus PSIRT analyst.
- **16/10/2026** - Presentation at Hexacon in Paris

So I tried my best to inform everyone. At this point I have no information about the measures taken by affected vendors and ISPs. All I know is that as of October 15th 2026, all of these devices are still missing the patch.

And this is **not** limited to Belgium. Affected manufacturers serve a larger market.

## Key Takeaways

**Security through Complexity is Dead**. Although I could have done this research by myself, it would have taken me months to get there. With AI frontier models it took me less than a week. Which is a good thing because we can start looking into deeper and deeper layers of our technical infrastructure for a fraction of the cost.

**Support Windows Discrepancies are Attacker Opportunities**. A bug introduced in 2010, with a patch released in 2018, is still present in access points sold by original equipment manufacturers and actively deployed in internet service providers’ networks in 2026. The shelf life of this bug is therefore 16 years. This bug could enjoy a nice Orval at the bar.

**Our Tech Debt will be Collected. By Whom?** These kinds of vulnerabilities are perfect for threat actors that enjoy [Nearest-Neighbour Attacks](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/) or [hotel network compromission](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/). Highly targeted, over the air, against devices which defenders have very limited visibility into, allowing for traffic manipulation and collection.
