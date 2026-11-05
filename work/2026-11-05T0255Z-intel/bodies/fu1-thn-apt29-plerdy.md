---
title: APT29-Linked Hackers Hijack Web Analytics Script to Deliver iOS and Android Exploits
author: The Hacker News
url: https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html
hostname: thehackernews.com
description: APT29-linked attackers use compromised sites and Plerdy analytics to deliver iOS and Android exploits that steal browser and device data.
sitename: The Hacker News
date: "2026-11-04"
categories: ['Article']
fingerprint: b1a688b1ca35574a
---
The Russia-linked threat actor known as **[APT29](https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html)** is said to be behind a large-scale watering hole campaign targeting iOS and Android users through compromised websites, fake domains, and a supply chain attack involving a Ukrainian web analytics service called Plerdy SEO Tracker.

"The injected JavaScript code collects browser and device attributes," Sekoia researchers Amaury-Jacques Garçon and Félix Aime [said](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits) in a technical report shared with The Hacker News. "Then, the delivery infrastructure delivers a platform-specific N-day exploit chain targeting either iOS or Android."

The end goal of the attacks is to serve payloads capable of stealing browser cookies, and in some cases, Wi-Fi passwords or full mobile device data. The activity, codenamed **Poisoned Source**, was discovered by the French cybersecurity company in mid-October 2026.

A defining aspect of the campaign is the use of three infection vectors -

- Compromise of legitimate websites to inject malicious JavaScript
- Lookalike sites masquerading as high-profile websites in the U.S. ("america250\[.\]holiday"), Ukraine, Czech Republic, and Bulgaria
- Supply chain compromise of Plerdy SEO Tracker between August 27 and September 3, 2026, by injecting malicious code into "a.plerdy\[.\]com/public/js/click/main.js"

Some of the compromised websites include a major industry trade association representing U.S. companies operating in the chemical industry, a far-right European political party, and a Bulgarian military-related website. It's suspected that the watering hole campaign may have been designed to target specific individuals rather than a broad effort.

"It remains unclear whether the attackers intended to target visitors to specific websites or sought to compromise as many unpatched mobile devices as possible, indiscriminately exfiltrating data before selectively identifying and exploiting information of interest," Sekoia said.


"However, several of these sites are likely to attract high-value or strategically important visitors in the context of the Russia-Ukraine war. This supply chain attack spread through high-value targets, such as army, special forces, and military equipment (ballistic, UAV) websites."

Regardless of the method employed, all roads lead to the same payload: a JavaScript loader that profiles the visitor's device and web browser, and then serves appropriate next-stage malware. For iOS users, it leads to an exploit kit called [DarkSword](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html) to harvest cookies and full device data.

On Android, the malware is equipped to exfiltrate Chrome data and Wi-Fi passwords without establishing persistence. No less than three different exploits have been identified -

- **Class A**, which targets iOS devices running iOS 16.7 and exploits CVE-2025-43529 (the same vulnerability exploited by DarkSword) and CVE-2024-27834 to deliver JavaScript malware for cookie theft.
- **Class B**, which targets iOS devices running iOS 18.5 and exploits the [DarkSword exploit chain](https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html) comprising CVE-2025-43529, CVE-2026-20700, CVE-2025-14174, CVE-2025-43510, and CVE-2025-43520 to deliver JavaScript malware for full device data exfiltration. This includes SMS messages and iMessages; Apple Mail Envelope Index and Protected Index SQLite databases; voicemail; WhatsApp and Telegram databases; iCloud Keychain, Wi-Fi passwords; contacts; call history; Safari browser history and cookies; photos; and data from Apple Health, Calendar, Notes, and iCloud Drive.
- **Class C**, which targets Android devices running Chrome versions from 139 through 145 (but explicitly excluding version 143 for reasons that remain presently unknown) and exploits [CVE-2026-3910](https://thehackernews.com/2026/03/google-fixes-two-chrome-zero-days.html) and [CVE-2025-27038](https://thehackernews.com/2025/06/qualcomm-fixes-3-zero-days-used-in.html) to achieve remote code execution, sandbox escape, privilege escalation, and ultimately deliver AndroSnitch to collect Chrome data and Wi-Fi passwords.

In all three cases, the exfiltrated data is sent to the "ad.starx-net\[.\]com:8881/telemetry/v12" endpoint. The Android attack chain incorporates a check to determine whether the targeted device is a Samsung Galaxy S25 Ultra by examining its model identifier (i.e., SM-S938B). If the device matches, the exploitation activity is terminated.

AndroSnitch derives its name from its similarities to [ANDROSNATCH](https://thehackernews.com/2024/08/russian-hackers-exploit-safari-and.html), a Chrome cookie-stealing payload that Google documented in August 2024 in connection with a suspected APT29 watering hole campaign, which targeted Android users visiting a Mongolian government website by leveraging a Chrome exploit chain involving CVE-2024-5274 and CVE-2024-4671.

"This operation also confirms the continued reuse of CSV \[Commercial Surveillance Vendors\] mobile exploit frameworks, such as DarkSword, by state-sponsored intrusion sets," Sekoia said. "The adoption of packaged N-day exploit chains lowers the cost and technical threshold required to conduct advanced mobile exploitation."

### Coruna and DarkSword Kits Evolve

The development comes weeks after [iVerify](https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits) and [Report URI](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/) detailed the [P7 variant of DarkSword](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html) being delivered via half-click attacks that leverage ad-based infrastructure. In one case, the exploit is said to have been propagated through a malicious Instagram ad themed around the World Cup and served from "ad-track\[.\]live."

The other pathway is part of a criminal campaign dubbed DeadTag, in which attackers acquire expired domains behind old analytics and advertising tags that are still loaded by thousands of websites. The idea is to serve malicious JavaScript to iPhone visitors and silently do the attacker's bidding.

"It checks who's visiting," Report URI said. "Search engines, security scanners, automated browsers and anything else that looks like a bot gets nothing."

The script then interacts with the attacker's server, which then decides the destination to which each visitor has to be redirected. The iPhone exploit paths that take advantage of DeadTag lead to the [Coruna](https://thehackernews.com/2026/03/coruna-ios-kit-reuses-2023.html) exploit kit for older iPhones running iOS version 13 to 17.2.1 and DarkSword P7 for iOS devices running 18.4 to 18.7.

"These are not phishing pages or fake app downloads, both kits attack the browser itself," Report URI's Scott Helme said. "Simply opening the page is enough for your device to be compromised. There's nothing to tap, you don't need to click any link, nothing to install and no warning. If the iPhone is running a vulnerable version of iOS, the kit breaks out of the browser and installs spyware on the device."

Other schemes lead to decoy Google redirects, betting and casino scam sign-up pages, search advertisements for car deals and dentists, and fake surveys and "you've won" prize pages. More than 660 expired and re-registered domains are part of the DeadTag network.

According to an analysis published by Zimperium zLabs, campaigns distributing Coruna and DarkSword exploit kits have continued to evolve, with 608 domains delivering Coruna-family code as of October 2026.

Although Coruna was initially developed by a nation-state actor for highly targeted operations, its subsequent leak following initial disclosure has made the toolkit widely accessible to multiple threat actors for their own campaigns.

In many cases, the lure sites have been found to explicitly instruct visitors to exit their in-app browser or alternative iOS browser and open the link in Safari so as to trigger the exploit chain depending upon the device operating system.

"Targets running iOS 17.2.1 or earlier receive the legacy Coruna framework (exhibiting byte-identical JavaScript payloads across multiple recovered configurations)," security researcher Santiago Rodriguez [said](https://zimperium.com/blog/inside-coruna-and-darksword-chains-from-web-lures-to-ios-exploitation). "Conversely, devices running later iOS builds receive a DarkSword-derived execution chain."

"The analyzed distribution footprint spans dating portals, AI-companion platforms, cryptocurrency promotions, media streaming services, and – in several instances – compromised legitimate sites serving the kit via hidden iframes."

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
