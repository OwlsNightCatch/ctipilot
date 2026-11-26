---
title: "Microsoft: China’s Salt Typhoon hackers are using Artex"
author: Jonathan Greig
url: https://therecord.media/microsoft-china-salt-typhoon-using-artex-ai-tool
hostname: therecord.media
description: An AI tool implicated in several high-profile breaches is rapidly being integrated into the hacking suites of groups from China and North Korea, Microsoft said.
sitename: The Record
date: "2026-11-25"
fingerprint: "265124092b8c92c0"
language: en
image: https://cms.therecord.media/uploads/microsoft_sign_pexels_altabena_efbc5ae4db.jpg
pagetype: website
filedate: "2026-11-26"
---
# Microsoft: China’s Salt Typhoon hackers are using Artex

State-backed hacking groups in China and North Korea are using a powerful AI hacking tool in attacks, according to a new report from Microsoft.

Microsoft [explained](https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/) that state-sponsored and financially motivated hackers are using Artex, an AI-powered platform that can automate multiple phases of cyber intrusions at machine speed.

The study emerged hours after [The New York Times](https://www.nytimes.com/2026/11/24/us/politics/spy-agencies-computer-network-breaches.html) and [NextGov](https://www.nextgov.com/cybersecurity/2026/11/cia-odni-unclassified-intelligence-system-hacked/417438/) reported that Artex was allegedly used in attacks on the CIA, the National Geospatial-Intelligence Agency and the Office of the Director of National Intelligence.

Microsoft said on Wednesday that Chinese state-backed groups Crystal Typhoon and Salt Typhoon have integrated Artex into their suite of tools, using it for “network reconnaissance, credential attacks, and web application exploitation.”

“In the past few weeks, we’ve reported several distinct campaigns that abused Artex to search public repositories for exposed secrets, enable supply chain compromise, and scan internet-facing systems for exploitation,” Microsoft explained.

Salt Typhoon is a prolific Chinese hacking group that U.S. agencies believe was behind the breach of [at least nine telecommunications giants](https://therecord.media/nine-us-companies-hacked-salt-typhoon-china-espionage) in 2024. The hack [alarmed](https://therecord.media/eight-telcos-breached-salt-typhoon-nsc) White House officials in 2024 because it allegedly gave China’s hackers access to communications from the phones of President Donald Trump and Vice President JD Vance as well as several Democratic leaders.

Salt Typhoon was also accused of [attacking](https://therecord.media/allied-spy-agencies-blame-chinese-companies-salt-typhoon) several [European governments](https://therecord.media/norawy-intelligence-discloses-salt-typhoon-attacks) and critical infrastructure organizations [globally](https://therecord.media/chinese-hackers-telecoms-house).

Artex was released in July, and according to Microsoft, it has been steadily added to the arsenal of multiple North Korean and Chinese groups.

Artex allows threat actors to define specific goals and use AI agents to attack targets. Microsoft said Artex “can advance from reconnaissance to persistent, privileged access to a target organization in a matter of minutes.”

“ARTEX does not introduce new attack techniques; it uses common, pre-existing penetration testing tools and techniques. ARTEX does sometimes transmit distinctive characteristics associated with its integrated penetration testing tools,” Microsoft explained.

“However, threat actors using ARTEX can and do vary network indicators like source IP address or user agent string, especially to bypass static or simple signature-based detection and blocking. The most reliable and durable signal of ARTEX activity is behavioral: ARTEX sends a wide variety of requests in a brief time and retries variations on the same technique or moves on to next-stage actions at machine speed.”

By default, Artex does not take measures to hide its activity, the researchers added.

While the Chinese researcher behind the tool initially removed the source code from GitHub last month, other developers [made copies](https://www.404media.co/the-code-is-already-copied-everywhere-the-ai-hacking-tool-causing-havoc-around-the-world-artex-github/), and at least one Chinese company now offers commercial access to a version of it.

Microsoft noted that defenders can tell when Artex is being used based on bursts of machine speed activity and by the “characteristically large volume of anomalous traffic from a single source in a short time.”

The FBI [released](https://therecord.media/artex-ai-tool-fbi-flash-alert) its own advisory on Artex two weeks ago, warning that it is being used prolifically by cybercriminals and nation-states to breach government agencies and dozens of critical sectors worldwide.

The tool was recently [implicated](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) in [multiple attacks](https://www.wsj.com/world/asia/hackers-use-chinese-ai-tool-to-hit-south-korean-banks-exposing-new-risk-5d4d3885) on South Korean and [Japanese](https://www.esecurityplanet.com/cybersecurity-threats/news-apac-artex-ai-cyberattacks-japan-companies/) financial institutions, causing national scandals in both countries. Microsoft previously said Artex was used by Chinese state-backed actors in a recent [supply chain attack on IT management software company ConnectWise](https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack).

[Jonathan Greig](https://therecord.media/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.
