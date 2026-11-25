---
title: ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs
author: The Hacker News
url: https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html
hostname: thehackernews.com
description: ROMULUS ClickFix attacks deliver CNCMachineRMS RAT through DLL sideloading, enabling remote control, surveillance, and file access.
sitename: The Hacker News
date: "2026-11-20"
categories: ['Article']
tags: ['ClickFix', 'DLL Sideloading', 'Malware', 'Remote Access Trojan', 'Social Engineering', 'Threat Intelligence']
fingerprint: "8d3c99a1833fb203"
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjugg63OPJwZuh94vDIg7MkA4YoeLKr5sjiqI6CEgjvDjUvJ-pBJOfUrUBxPUTbartqVwdldczbKSYo6lpkcVic1EDQYIDyWq12zMdMONjpDtK4NKCgkppAWvnOJpXe7prfmRG8WNpH0RrQ0bhX2nZKGpRy33y0OMZraBjEPoDorp9h3kNJSa-IQrJC7Nl5/s1700-nu-rw-lo-l85-e365/cf.jpg
pagetype: article
filedate: "2026-11-25"
---
Threat actors have been observed using the **ROMULUS** ClickFix malware delivery platform to deliver a previously undocumented remote access trojan (RAT) that shares similarities with CNCMachineRMS.

"ROMULUS likely operates as a delivery service, distributing CNCMachineRMS and Legion Loader through separate chains while retaining ClickFix and signed binary sideloading techniques," Blackpoint Cyber researchers Sam Decker, Nevan Beal, and Andi Ursry [said](https://blackpointcyber.com/blog/romulus-cncmachinerms/) in a report.

ROMULUS was [first publicly documented](https://thehackernews.com/2026/10/romulus-clickfix-platform-tricks-users.html) by Forescout Research last month, describing it as a malware delivery service that employs ClickFix-style lures to distribute malware families like Legion Loader (aka Satacom downloader, CurlyGate, and RobotDropper).

Attacks involving ROMULUS have also leveraged [ChatGPT Custom GPTs](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html) as a pathway to direct unsuspecting victims to malicious sites that employ ClickFix lures to deliver a RAT payload by means of DLL sideloading.

Interestingly, CNCMachineRMS has also been [delivered](https://thehackernews.com/2026/08/threatsday-296k-iot-botnet-100-water.html#clickfix-chain-drops-new-rat) via another malware loader called BabaDeda Loader through ClickFix attacks that employ DLL sideloading involving the legitimately signed IBM SPSS IDE executable.

The latest findings from Blackpoint Cyber indicate that ROMULUS is distributing CNCMachineRMS alongside LegionLoader through separate infection chains.

One of the payloads delivered through the ClickFix activity associated with ROMULUS is a malicious MSI installer ("IconEdit2Turb.msi") that's executed using "msiexec.exe" by means of a PowerShell command. The installer masquerades as Stardock Smart DeElevation Tool, while initiating a DLL sideloading chain to run a malicious DLL ("I++u.dll").

The DLL is designed to decode and run embedded shellcode responsible for launching CNCMachineRMS. It's worth noting that the RAT malware is the same final implant also distributed via the aforementioned ChatGPT Custom GPT lures.


The trojan enables remote desktop control, screen streaming, microphone and camera capture, file management, and system reconnaissance. It's also equipped to run additional payloads on demand. Communication with attacker-controlled infrastructure takes place through DNS over HTTPS (DoH).

"As attackers continue to change the applications and loaders used to distribute their payloads, the underlying malware architecture provides a more consistent way to identify related activity and understand the threats being delivered," Blackpoint Cyber said.

The findings coincide with the discovery of a number of ClickFix-style campaigns that -

- Combine ClickFix with EtherHiding on more than [70,000 compromised websites](https://www.stormshield.com/news/cti-payload-slaiclind-campaign/) to run JavaScript that interacts with a Polygon smart contract to fetch additional JavaScript that renders a fake Cloudflare CAPTCHA prompt and ultimately deliver malware ("slaiclind").
- Use [fake Zillow apartment-review pages](https://efficientip.com/blog/clickfix-netsupport-rat/) that serve a fake verification prompt to install NetSupport RAT on visitors' Windows computers.
- Employ a JavaScript-to-WordPress attack chain called [TRUST#GRAFT](https://www.securonix.com/blog/trust-graft-wordpress-admin-php-backdoor/) that employs an unknown initial access method to inject JavaScript into WordPress sites that serves a fake Cloudflare verification prompt and then fingerprints the visitor and checks if the request is from an already authenticated WordPress administrator browser before uploading a malicious PHP plugin named Web Media Optimizer that's capable of injecting remote JavaScript into public pages and copying itself into the "mu-plugins" plugins directory for persistence.
- Use a [sponsored Google search result](https://www.huntress.com/blog/amazon-clickfix-finger) for the keywords "amazon business" to a spoofed Amazon login page ("orders-amazon\[.\]com\[.\]advancedfences\[.\]com") with an embedded ClickFix command that uses the Window's built-in [finger](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/finger) utility to initiate a multi-stage attack chain that leads to the deployment of the NetSupport Client remote monitoring and management (RMM) tool and a version of Lumma Stealer.
- Abuse Google Ads to direct users to an [Anthropic Claude shared chat](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html#fake-claude-guide-spreads-malware) that stages a [fake "Download Claude" page](https://www.gendigital.com/blog/insights/research/claude-content-sharing-malware) with ClickFix commands to trick Mac users into running a malicious command on their Terminal, resulting in the deployment of Atomic macOS Stealer (AMOS) stealer.
- Use a typosquatted domain that employs a ["House Wiring Scheme" theme](https://flare.io/learn/resources/blog/crocorat-clickfix-dns-payload-delivery) ("veriffication-redirect\[.\]com") to serve a fake Cloudflare verification prompt, which utilizes clipboard manipulation to trick users into running a malicious command on the Windows Run dialog, which then retrieves next-stage Python payloads via DNS TXT records. This includes a previously unreported trojan called CrocoRat, along with a broader theft workflow targeting web browsers, stored credentials, cryptocurrency wallets, and seed phrases on standalone systems.
- Directly [contact targets via phone](https://fieldeffect.com/blog/clickfix-cluster-observed-activity-recent-campaigns) and convince them to open compromised WordPress sites that serve ClickFix lures to deliver malicious payloads via trojanized MSI packages masquerading as 3D PDF Maker Smart, Bitwarden VPN, and ESET Sysinspector, and execute them via DLL sideloading.
- Use a ClickFix variant called [TerminalFix](https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html) that instructs users to open Windows Terminal and run a command to deploy a [Python-based tunneling implant](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling) using [Lorem Ipsum Loader](https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html). The [activity](https://www.forescout.com/blog/from-clickfix-to-c2-comparative-analysis-of-two-malware-loaders/) is being tracked as STAC4924.
- Use [Google search ads for "claude mac"](https://pushsecurity.com/blog/adception-malvertising-another-search-engines-search-results) to a Bing search result, which then directs the victim to a compromised retail website before landing on a fake Claude download page. The bogus landing page employs another ClickFix variant called [InstallFix](https://thehackernews.com/2026/03/clickfix-campaigns-spread-macsync-macos.html) to get Mac users to copy and run a malicious command on their Terminal. The crafty Google Search-to-Bing redirect and cloaking technique has been codenamed Adception.
- Use [fake Cloudflare verification prompts](https://flare.io/learn/resources/blog/clickfix-attacks-summary) on bogus sites mimicking gaming marketplace [DMarket](https://flare.io/learn/resources/blog/hunting-clickfix-attacks-deep-dive), [Microsoft Office authentication in Czech](https://flare.io/learn/resources/blog/microsoft-lookalike-domain-clickfix-campaign) ("login.microsoftofice\[.\]cz"), and U.K. retailer [Howdens](https://flare.io/learn/resources/blog/hunting-clickfix-attacks-deep-dive) ("updates.howclens\[.\]com") to deliver CrashHandler RAT and remote access malware, including one that abuses the [Stripe API](https://sansec.io/research/stripe-api-skimmer-infrastructure) as command-and-control (C2) to receive instructions and send back stolen information.

In a report published last week, Huntress revealed that ClickFix-style attacks have broadened its scope beyond simple script or loader delivery into sophisticated attack chains that establish persistence, support lateral movement, and enable reconnaissance and credential theft, in some cases using steganographic tricks to hide malware and reconstruct them on the infected host.

"Threat actors are using increasingly elaborate delivery methods, including browser-cache-seeded chains and executables reconstructed from data hidden in PNG files," Huntress researchers [said](https://www.huntress.com/blog/the-evolving-tradecraft-of-clickfix).

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
