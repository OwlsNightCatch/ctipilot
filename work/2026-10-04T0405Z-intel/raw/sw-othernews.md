---
title: "In Other News: $15K iCloud Spoofing Bugs, AI Policy Experts Phished, Adblocker Spies on AI Chats"
author: SecurityWeek News
url: https://www.securityweek.com/in-other-news-15k-icloud-spoofing-bugs-ai-policy-experts-phished-adblocker-spies-on-ai-chats/
hostname: securityweek.com
description: "Noteworthy stories that might have slipped under the radar: Kiteworks patches over 100 vulnerabilities, Microsoft publishes 2026 Digital Defense Report, AI finds 24 Android app flaws."
sitename: SecurityWeek
date: "2026-10-02"
categories: ['Malware & Threats']
---
**SecurityWeek’s weekly** **cybersecurity news roundup** **offers a concise overview of important developments that may not receive full standalone coverage yet remain relevant to the broader threat landscape.**

This curated summary highlights key stories across vulnerability disclosures, emerging attack methods, policy updates, industry reports, and other noteworthy events to help readers stay well-informed about the evolving cybersecurity environment.

**Here are this week’s highlights:** 

**Microsoft threat report sees phishing triple as exploit windows shrink**

[Microsoft’s 2026 Digital Defense Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Digital-Defense-Report.pdf) (covering July 2025 to June 2026) says AI has pushed the median time from vulnerability discovery to weaponization well below 24 hours, with a record of roughly 72,000 CVEs expected this year. Phishing rose from 7% to 23% of initial access vectors in Microsoft’s incident response cases, Teams vishing climbed 502%, and ransomware detonations against enterprises increased nearly 16%. Government agencies were the most affected sector, accounting for 27% of observed activity.

**Kiteworks publishes over 100 security advisories in a single day**

Kiteworks published over 100 [security advisories](https://github.com/kiteworks/security-advisories/security) on September 30, covering its Core platform, Email Protection Gateway, Secure Data Forms, and MFT Server. A dozen are rated critical, mostly Email Protection Gateway bugs that can lead to account takeover, code execution, or access to internal network resources. Dozens more are rated high severity. The most common issues are information disclosure and arbitrary code execution, followed by privilege escalation. 

**Smuggled headers turned iCloud into an email spoofing tool**

SEC Consult researcher Timo Longin has disclosed [two iCloud vulnerabilities](https://sec-consult.com/blog/detail/from-anyoneicloudcom-spoofing-arbitrary-apple-icloud-identities/) that let attackers send emails from arbitrary icloud.com addresses, and the messages passed SPF, DKIM and DMARC checks. Both stemmed from differences in how two parts of Apple’s outgoing mail pipeline parsed messages, which let a forged From header slip past sender verification. The first issue was reported in May 2024, but Apple’s initial fix was incomplete, and it wasn’t fully fixed until December 2025. Apple paid a $15,000 bug bounty.

**Poper Blocker’s hidden interpreter siphons AI conversations**

Bay Area Labs researchers [found](https://amibeingpwned.com/blog/poper-blocker-the-adblocker-that-spies-on-you) that Poper Blocker, a featured Chrome adblocker extension with more than 2 million users, collects full browsing history and conversations from ChatGPT, Claude, Gemini and Google’s AI Mode once users are nagged into accepting data sharing. The collection logic is downloaded from the vendor’s server and run by a custom interpreter inside the extension, so the operator can change what is collected, and where it is sent, without pushing an update.

**GitHub Security Lab turns AI taskflows on Android apps**

GitHub Security Lab says Android-focused taskflows for its open source AI security agent have uncovered [24 vulnerabilities](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) in Android applications. Examples include an OsmAnd flaw that let any installed app (even one with no permissions) silently change the navigation app’s settings to leak the user’s location and routes, and two Wikipedia app bugs that chain into account takeover through a malicious deeplink. The researchers note that the AI often misjudged severity and flagged unrealistic issues, so findings still need human review.

**Two US airmen sentenced to prison for BEC attacks**

Chijioke Timothy Odimegwu and Harafat Mogaji, two Delaware men who were serving in the US Air Force at the time, have been [sentenced](https://www.justice.gov/usao-sdia/pr/delaware-men-sentenced-cyber-intrusion-scheme-targeting-victims-southern-district-iowa) to 111 and 78 months in prison, respectively. Working with co-conspirators over nearly two years, they phished employee email credentials and used spoofed emails to redirect business payments, diverting more than $1.68 million from an Iowa victim and over $720,000 from an Ohio victim. They were also ordered to pay a combined $1.36 million in restitution.

**Vulnerability let Cloudflare Containers users peek at other customers’ data**

Cloudflare has [patched](https://blog.cloudflare.com/containers-cross-tenant-vulnerability/) a flaw in Containers (and Sandboxes, which is built on it), reported by Accomplish researcher Oren Yomtov, that let a Workers Paid customer recover leftover data from disk blocks other customers’ containers had used on the same host. Because newly allocated storage blocks weren’t zeroed, the researchers found residual material, including directory structures, database pages and complete SQLite databases, on 18 of 24 placements, although they couldn’t target a specific victim. Cloudflare found no evidence of malicious exploitation.

**Fake AI advisory committee invites used by Chinese cyberspies**

Proofpoint has detailed [TA419](https://www.proofpoint.com/us/blog/threat-insight/hallucinating-credibility-china-aligned-ta419-impersonates-its-way-us-ai-policy), a new China-aligned espionage group that impersonated former White House OSTP Principal Deputy Director Lynne Edwards Parker and economist Heidi Crebo-Rediker in July 2026 to phish AI policy experts at US think tanks, universities and law firms. Targets who replied to the initial benign outreach were sent to a fake OneDrive page that passes the Microsoft 365 sign-in through an adversary-in-the-middle (AitM) proxy, capturing session cookies even when MFA is used. The group also posed as an Anthropic employee in February 2026.

**Related**: [In Other News: Ransomware Developer Sentenced, Plugin4Shell AI Attack, Critical SAP Flaw](https://www.securityweek.com/in-other-news-ransomware-developer-sentenced-plugin4shell-ai-attack-critical-sap-flaw/)

**Related**: [In Other News: Clop Leak Site Takeover, Docker Botnet Hunts AI Keys, Water Utility Exposure](https://www.securityweek.com/in-other-news-clop-leak-site-takeover-docker-botnet-hunts-ai-keys-water-utility-exposure/)
