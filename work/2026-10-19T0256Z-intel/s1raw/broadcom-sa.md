---
title: "16-Year-Old Broadcom Wi-Fi Bug Lets Attackers Take Over Routers Without a Password"
author: Pierluigi Paganini
url: https://securityaffairs.com/201268/iot/16-year-old-broadcom-wi-fi-bug-lets-attackers-take-over-routers-without-a-password.html
hostname: securityaffairs.com
description: A Broadcom Wi-Fi flaw dating back to 2010 allows attackers within Wi-Fi range to execute code on vulnerable routers without authentication.
sitename: Security Affairs
date: "2026-10-19"
categories: ['Breaking News', 'Hacking', 'Internet of Things', 'Security']
tags: ['802.11', 'Broadcom', 'Hacking', 'hacking news', 'information security news', 'IT Information Security', 'Pierluigi Paganini', 'Security Affairs', 'Security News', 'Wi-Fi']
fingerprint: a471e512e98022c1
---
Researcher Quentin Kaiser presented a talk at Hexacon in Paris documenting a vulnerability in Broadcom’s proprietary 802.11 implementation that has been present in their SDK since at least 2010. The bug allows an attacker to get unauthenticated remote code execution on affected routers without knowing the WiFi password or going through the normal WPS setup process.

As of October 15, 2026, none of the affected devices in Belgium had received a patch.

*“A vulnerability affecting Broadcom’s proprietary implementation of 802.11 has been present in their SDK since [at least 2010](https://github.com/shantanugoel/asus-rt-n66u-merlin/blob/ede220728e1eb417b4cc88912738b4311abdc088/release/src-rt/wps/common/ap/ap_eap_sm.c#L4). An incomplete patch was silently released in 2018, followed by Broadcom’s recommendation to move to `hostapd` instead, making it a definitive forever day on eCos-based platforms (BCM3380, BCM3383, BCM33834) and a potential forever day on Linux platforms (BCM3390, BCM65xx, BCM68xx) unless affected Original Equipment Manufacturers (OEMs) are willing to migrate.” [states Kaiser](https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/). “The vulnerability can be triggered remotely over WiFi without knowledge of the network key or completion of a normal WPS enrollment. Exploitation provides controlled information disclosure and arbitrary code execution.”*

The vulnerability affects the WPS EAP reassembly code, which handles part of the wireless setup process used by many consumer routers. An attacker within Wi-Fi range can exploit the flaw without knowing the Wi-Fi password, completing the setup process, or requiring any action from the user. The attack can expose information and allow the attacker to run code on the router. In his demonstration, Kaiser extracted the Wi-Fi password from the router’s memory and sent it over the wireless connection. He then used the password to connect to the network.

These attacks are not just theoretical. Kaiser demonstrated working exploits against two devices: the Orange Belgium ASKEY TCG3000 and the Proximus Sagemcom F@st/BBOX3V+. Both allowed an attacker to run code without authentication. In one demonstration, the attacker opened a reverse shell using only Wi-Fi frames, without needing a command server accessible over the internet. The attack can work from a distance. The close antenna placement shown in the video was only for the laboratory setup and is not a requirement for the attack.

In the video below, Kaiser exploited an Orange Belgium router (ASKEY TCG3000). The attack allowed him to run code on the device without authentication. The code retrieves the Wi-Fi password (PSK) from the router’s NVRAM and sends it back to the attacker over Wi-Fi. He then used the stolen password to connect to the network, confirming that the exploit works and that the password is correct.

Do not be misled by how close the antenna is in the video. The attack can work over much longer distances.

In the next video, the researcher exploited a Proximus router (BBOX3V+, also known as Sagemcom F@st). This attack also allows code execution without authentication. He used it to open a reverse shell over Wi-Fi frames, without needing a command-and-control (C2) server hosted in the cloud.

Broadcom quietly released an incomplete fix in 2018, then told customers to migrate to a different software stack entirely rather than shipping a complete patch for their own code. On eCos-based platforms, covering chipsets like BCM3380, BCM3383, and BCM33834, that makes this a permanent unfixable bug by design. On Linux-based platforms (BCM3390, BCM65xx, BCM68xx) the situation depends entirely on whether individual manufacturers decide to act.

Kaiser reported the bugs to Broadcom in July 2026. Broadcom said a patch was available and told him to ask the affected device manufacturers to contact Broadcom directly. The company refused to assign a CVE or share the notification it had sent through its customer portal. CERT/CC opened a case but closed it the same day after confirming that Broadcom could assign CVEs itself and had no intention of doing so. This was not a proper disclosure process. It was a dead end, with a paper trail.

Kaiser’s rough calculation, done with Belgian telecom market data, puts the affected device count at around 850,000 for Proximus, 500,000 for VOO’s legacy fleet, and 210,000 for Orange Belgium, totalling somewhere north of 1.5 million potentially exposed gateways in one small country. Telenet may also be affected through Sagemcom devices but Kaiser couldn’t confirm because he couldn’t get hold of one.

The affected manufacturers sell into markets well beyond Belgium. The chipsets in question appear in devices across dozens of vendors and hundreds of products worldwide. Kaiser is publishing a fingerprinting script and a YARA rule specifically to help map the full scope of affected deployments, because right now nobody has a complete picture.

A vulnerability introduced in 2010 and only partly fixed in 2018 still affects routers in use today. Kaiser says AI-assisted analysis helped him find the bugs in less than a week, instead of months. This can help defenders find vulnerabilities faster, but attackers can do the same.

The risk is greatest in targeted attacks where an attacker is within Wi-Fi range, such as hotel network attacks or surveillance of nearby targets. Compromised routers are difficult to monitor, and attackers can quietly intercept or collect network traffic. Most users and security teams rarely check the firmware on ISP-provided routers.

*“Although I could have done this research by myself, it would have taken me months to get there. With AI frontier models it took me less than a week.” Kaiser concludes. “Which is a good thing because we can start looking into deeper and deeper layers of our technical infrastructure for a fraction of the cost.”*

**Follow me on Twitter: @securityaffairs and Facebook and Mastodon**

**(SecurityAffairs – hacking, Broadcom Wi-Fi)**
