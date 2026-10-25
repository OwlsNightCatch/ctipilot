# extract: served via trafilatura-direct
---
title: Suspected state-sponsored hackers exploited NetScaler zero-day since early September (CVE-2026-88772) - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/09/30/cve-2026-88772-netscaler-exploitation-zero-day/
hostname: helpnetsecurity.com
description: Advanced threat actor exploited CVE-2026-88772, one of the two recently disclosed NetScaler zero-day flaws, for weeks.
sitename: Help Net Security
date: "2026-09-30"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['education', 'Europe', 'financial industry', 'Google Cloud', 'government', 'Mandiant', 'NetScaler', 'telecommunications', 'USA', 'WatchTowr', 'education', 'Europe', 'financial industry', 'Google Cloud', 'government', 'Mandiant', 'NetScaler', 'telecommunications', 'USA', 'WatchTowr']
fingerprint: "1f9a1959e8201fc2"
---
# Suspected state-sponsored hackers exploited NetScaler zero-day since early September (CVE-2026-88772)

“Advanced and suspected state-sponsored threat actors” are likely to be behind the initial targeted intrusions that leveraged CVE-2026-88772, one of the two recently disclosed NetScaler vulnerabilities that have been exploited as zero-days, [says](https://www.linkedin.com/feed/update/urn:li:activity:7510702011294769152/) Mandiant CTO Charles Carmakal.

Mandiant and Google Threat Intelligence Group (GTIG) know of dozens of impacted organizations across North America and Europe, he added, “including in the government, financial services, education, telecommunications, and legal and professional services sectors.”

### Two NetScaler zero-days exploited

On September 27, 2026, a few days after organizations around the world began getting notified of active attacks involving a possible zero-day vulnerability in Citrix NetScaler ADCs and Gateways, Citrix confirmed that two flaws [had been exploited](https://www.helpnetsecurity.com/2026/09/28/citrix-netscaler-rce-zero-days-exploited-for-weeks-cve-2026-88771-cve-2026-88772/): CVE-2026-88771 and CVE-2026-88772.

Both allow remote attackers to achieve remote code execution on vulnerable appliances. While the former works on all devices that run a default configuration, the latter is exploitable only if DTLS configuration is enabled.

CVE-2026-88771 exploitation attempts and successes have already been detailed by cybersecurity firms and security researchers, but Mandiant’s incident responders and Google Threat Intelligence Group (GTIG) researchers have now released their own findings on the attacks relying on CVE-2026-88772.

They say that they first flagged in-the-wild exploitation of CVE-2026-88772 in late September 2026 and that the exploitation activity has been ongoing since at least early September.

### How the attacks unfolded

“Exploitation of CVE-2026-88772 bypasses authentication and triggers an unhandled termination of the NetScaler Packet Processing Engine (NSPPE) to establish initial root-level access,” they [found](https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances).

“While Google Threat Intelligence Group does not possess exploit code, analysis of frontline telemetry suggests that transmitting specially malformed or fragmented record headers induces heap memory boundary corruption within the packet engine, diverting control flow to execute arbitrary shellcode with root-level operating system privileges on the underlying FreeBSD platform.”

In some attacks, after gaining access, the attackers’ initial web shell payload modifies *httpd.conf*, the configuration file for the Apache web server built into the appliance, so that the web server would handle *.deb* files as though they were PHP scripts and attackers could covertly stage web shells with deceptive file type extensions in */netscaler/gui/vpn/scripts/linux*.

“In other intrusions, the threat actor implemented a stealthier configuration hook that disguised web shell execution as image requests,” the researchers noted.

The attackers used a number of web shells to execute commands and achieve persistence on targeted devices, as well as a TCP tunneling tool (dubbed SLAPSHOT by the researchers), which allowed them to proxy traffic into internal networks.

### Patching is not enough

Carmakal says that broad and opportunistic exploitation of CVE-2026-88772 and CVE-2026-88771 by various threat actors is expected.

Widespread “spray and pray” exploitation of the latter [has already started](https://www.helpnetsecurity.com/2026/09/29/netscaler-zero-day-exploitation-escalates-into-mass-attacks-cve-2026-88771/) after technical details and a PoC have been shared online.

Wider exploitation of the former is likely to have started already, as watchTowr researchers [shared](https://labs.watchtowr.com/here-we-go-again-citrix-netscaler-dtls-preauth-memory-overflow-cve-2026-88772/) an analysis of the flaw and a “Detection Artefact Generator” on Tuesday.

Google’s researchers have shared detailed threat hunting, containment and remediation guidance which all organizations running NetScaler ADCs and Gateways should follow, and Carmakal has made sure to stress that upgrading to a fixed version is not enough to boot the attackers out, and does nothing to address the risk related to stolen credentials.

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
