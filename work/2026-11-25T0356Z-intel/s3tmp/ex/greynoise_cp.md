---
title: An Active Intrusion Campaign Against Check Point Security Management Servers
author: Steve Miller November
url: https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign
hostname: greynoise.io
description: GreyNoise recently discovered an intrusion campaign targeting Check Point Security Management Servers, with confirmed attack activity between October 17th and November 2nd, 2026, impacting at least 22 distinct organizations globally.
sitename: greynoise.io
date: "2026-11-23"
fingerprint: b4fbb6f3242884b1
language: en
image: https://cdn.prod.website-files.com/667dd40ebb8095e89f27565d/6b00b96c7176ac8c286ffb00_GreyNoise-Blog-Check-Point-1600x900.png
pagetype: website
filedate: "2026-11-25"
---
GreyNoise tracks threat activity using our Global Observation Grid (GOG), a sensor network designed to attract adversarial scanning and exploitation attempts on our managed infrastructure. One might think of these sensors as conventional “honeypots,” but that doesn’t quite capture the variety, versatility, and scale at which we deploy and manage the complex fabric of the GOG. Unsolicited activity against our sensors is sketchy if not outright nefarious, and our approach allows us to capture end-to-end intrusions and analyze a broad swath of attacker infrastructure, tools, and tactics in near realtime, without waiting for lengthy incident response investigations. We fuse data from our sensor network with additional novel sources and methods to develop a comprehensive picture of adversaries.


## Campaign Summary

- GreyNoise recently discovered an intrusion campaign targeting Check Point Security Management Servers, with confirmed attack activity between October 17th and November 2nd, 2026, impacting at least 22 distinct organizations globally.

- We are tracking this set of threat activity as GreyNoise Threat 13 (GT13) which represents adversary infrastructure, tools and post-exploitation action against the 22 victims.

- The campaign targeting does not appear to be focused on any specific geography or industry sector. The impacted orgs include victims with assets in the United Kingdom, Ireland, France, Netherlands, Greece, Germany, Austria, Bulgaria, Poland, India, Thailand, Vietnam, South Korea, Hong Kong, China, Australia, and the United States. The victim orgs sit in sectors including financial services, energy, government, transportation, mining, engineering, and manufacturing.

- We do not attribute GT13 to any known or publicly tracked threat group at this time. We do not currently have enough information to make assessments relating to the motivation of the actor or alignment to a nation-of-origin.

- The actor used 99 IP addresses, much of which were disposable network infrastructure to conduct scanning, exploitation, and control of its victims, including the use of a compromised server acting as an “operational relay box” (ORB) or more simply, a “hop,” for interacting with downstream victim assets. The actor used this relay box / hop to save command results and data stolen from 24 distinct Check Point Security Management Servers.

- The actor used [Nmap](https://github.com/nmap/nmap), [Chisel](https://github.com/jpillora/chisel), [Impacket](https://github.com/fortra/impacket), [Paramiko](https://github.com/paramiko/paramiko) and other Python tooling to perform intrusion activities against their victim assets, including attempts to perform internal reconnaissance, privilege escalation, and lateral movement.

- The threat actor used or attempted to exploit multiple CVEs, including, but not limited to: [CVE-2026-61500](https://viz.greynoise.io/cves/CVE-2026-61500) (Rejetto HFS), [CVE-2025-5777](https://viz.greynoise.io/cves/CVE-2025-5777) (Citrix NetScaler), [CVE-2024-21893](https://viz.greynoise.io/cves/CVE-2024-21893) (Ivanti), [CVE-2026-41089](https://www.cve.org/CVERecord?id=CVE-2026-41089) (Windows NetLogon), [CVE-2026-16232](https://viz.greynoise.io/cves/CVE-2026-16232) (Check Point SmartConsole auth bypass to Run Script), and [CVE-2026-98432](https://viz.greynoise.io/cves/CVE-2026-98432) (Linux IPv4 UAF).

- Though we observed hands-on-keyboard activity, we believe that like most modern attacks, the actor used LLMs and agentic systems to perform vulnerability scanning, exploitation, tool development, and automated interaction with compromised assets.

- Our visibility into this attack activity stopped around November 2nd, 2026, but given the actor’s persistent access to victim Check Point devices, we expect that this intrusion campaign is ongoing.

- We are working with international government partners and CERTs to share relevant intelligence and notify the victims.


## Observed Attacker Activities

We witnessed the GT13 actor use 99 IP addresses, all of which were either egresses through [ExpressVPN](https://viz.greynoise.io/ips?q=metadata.vpn_service:%22EXPRESS_VPN%22) or compromised victim Check Point devices, including activity over 1400+ network sessions, 800+ command line artifacts, and 1200+ files downloaded, uploaded, or created. We cannot cite all of the details here, but we can highlight observed GT13 adversary activities to illustrate their tradecraft and tactics, techniques, and procedures (TTPs).


### HFS Scanning and Exploitation

The GT13 threat actor used an automated scanning and exploitation pipeline to compromise an HFS server using [CVE-2026-61500](https://viz.greynoise.io/cves/CVE-2026-61500).

**2026-10-02 13:17:45 UTC** - The actor scanned and began exploitation against the HFS server. Each POST to the HFS loginSrp1 endpoint returns a new signed session cookie containing a “sid” value drawn from JavaScript’s Math.random() function. Through conducting several logins in succession, the actor collected enough output to reconstruct the internal state of the V8 PRNG algorithm, and thus recover an HFS session-cookie signing key, then forge a signed admin session cookie. This allows the attacker to login as admin without a password.

*Example POST to loginSrp1 and response*

*Decoded hfs\_http blob from 200 OK response showing the sid that is harvested*


**2026-10-02 13:19:37 UTC** - Minutes later, we observed admin requests with forged session cookies, leading us to believe this exploitation was indeed [CVE-2026-61500](https://www.cve.org/CVERecord?id=CVE-2026-61500) for session forgery, which was not patched on this server. The actor now had control of the server.

*Example HTTP POST request with forged cookie*


Note that this forged cookie contains “allow\_session\_ip\_change:true” which does exactly what it sounds like, letting the forged cookie work from any IP address. This is perfect for an adversary behind a VPN or operating from multiple exits.

**2026-10-05 12:21:30 UTC** - A few days later, the actor used this same flow to gain access to install HFS middleware hooks that would issue commands to the compromised server. This allowed the attacker to append an SSH key to /root/.ssh/authorized\_keys.

On October 8th, we observed the actor’s automation check in to the compromised server using HFS command hook for “uname -a; df -h / | tail -1; whoami”. Then there was a lull in activity until October 19th.


### Establishing the Operational Relay Box / Hop

**2026-10-19 14:53:48 UTC** - We don’t know why (possibly a problem with the multi-agent architecture), but the actor did not use the SSH access right away. Instead, the actor’s automated pipeline reused the HFS exploitation route to forge new session cookies and leverage the HFS server\_code feature to attempt to download and install additional malware on the server. At this point, we can see that the actor intended to use the compromised server as a relay or “hop” for further intrusion operations.

*Example of HFS command, which was preserved on the compromised server.*


*Example decoded base64 blob demonstrating that the actor was intending to download an apparent “ZULT” Linux implant to the compromised machine.*

The malware download failed, and the adversary attempted to troubleshoot the download by checking running processes, invoking curl to access the resource, and viewing the network configuration.

*Example of the actor following up, attempting to check on their implant*

They couldn't figure out why their implant did not download, and the actor returned the next day with a direct SSH connection to continue setting up their relay.

**2026-10-20 07:22:08 UTC -** The actor created a script (/root/exfil/srv\_post2\_\<redacted>.py) which set up an unauthenticated HTTP server on the hop, after which the actor began to upload files. The first exfiltrated .tgz file contained results from scan of network routes from a compromised Check Point Security Management Server, demonstrating that the actor already had access to targeted victim assets.

The actor continued to set up their environment, uploaded and installed open-source tools like Nmap and [Chisel](https://github.com/jpillora/chisel), and then set up a Chisel server as a reverse proxy.


### Intrusion Operations and Exfiltration

Once the actor had the compromised server set up as a relay, they began to use it to manage their interactions with their previously compromised victim Check Point devices. There’s a lot of commingled victimology here, so we’ll refer to two sets of victims. During our visibility, the actor was actively working towards deepening their intrusion against Victim A, and we later observed bulk actions on 21 other victim Check Point devices.

Between October 20th and 26th, the adversary had one of their Victim A compromised assets download the Chisel program and run it in client mode allowing them to further scan and interact with the Victim A environment. Over the Chisel tunnel, and by using a script for [CVE-2026-16232](https://viz.greynoise.io/cves/CVE-2026-16232) (Check Point SmartConsole auth bypass to Run Script), the actor launched over 100 management tasks on multiple Check Point Management Servers. This included copying the firewall database and the Internal CA, minting a new certificate (pivot.p12), and unloading security policies (which would disable the firewall). Further, the actor probed Citrix Netscaler, Ivanti Connect Secure, VMware vCenter, Microsoft Exchange, Oracle TNS assets and several domain controllers.

The bulk of the adversary commands and interaction is too voluminous to dig into here, but we can expose some of the adversary’s TTPs by taking a glimpse at their tooling. The actor used at least 30 Python scripts, many of which were helpers or launchers for other scripts, and several of them were probes for vulnerabilities or runners of exploits. Excerpts are provided below to illustrate the more specialized tooling and workflows.

**2026-10-20 13:54:30 UTC** - First use of exploit.py against a Victim A Check Point server.

*Excerpt from exploit.py-  This CVE-2026-16232 script is purportedly an adaptation of the Metasploit module for the same function. This appears to be how the actor was sending commands to the victim Check Point Security Management Servers.*

**2026-10-20 14:17:51 UTC** - spray\_portal.py used to scan another Check Point server in the Victim A environment.

*Excerpt from spray\_portal.py - note that this contained common/default/weak passwords, and those apparently tailored for the victim.*

**2026-10-21 00:34:51 UTC** - The actor could not get the second compromised Check Point device to report back to the hop, so they created and launched pull\_\<redacted\_id>.py to steal the data from the second Check Point server and save it on the first compromised server, which could help exfiltrate the data back to the hop server.

*Excerpt from pull\_\<redacted\_id>.py - The actor named this script after their targeted device. The script runs exploit\_socks.py which runs exploit.py for CVE-2026-16232, enabling the actor to harvest data from the second compromised Check Point device through the first, to the hop box. Notice that this steals credentials, internal CA files, and firewall configuration.*


**2026-10-21 02:56:38 to 06:34:40 UTC** - The actor runs broad port scanning using curl, telnet, nmap scripts, a domain controller probe and other tools for internal reconnaissance.

**2026-10-21 06:39:24 to 11:28:04 UTC** - The actor uses exploit scripts against multiple target servers in the Victim A environment.

- [CVE-2020-1472](https://viz.greynoise.io/cves/CVE-2020-1472) (Microsoft Netlogon),
- [CVE-2023-4966](https://viz.greynoise.io/cves/CVE-2023-4966) (Citrix Netscaler),
- [CVE-2024-21893](https://viz.greynoise.io/cves/CVE-2024-21893) (Ivanti Connect Secure),
- [CVE-2021-26855](https://viz.greynoise.io/cves/CVE-2021-26855)/34473 (Microsoft Exchange) and
- [CVE-2021-21972](https://viz.greynoise.io/cves/CVE-2021-21972) / CVE-2023-34048 (VMware vCenter)

**2026-10-21 11:41:21 UTC** - The actor uses comb.py, ssh\_comb.py and ssh\_spray.py to scan a variety of targets in Victim A’s network. Note that these scripts contain usernames and passwords that were themed to the target victim. The actor either knew or was guessing names and passwords that the target might use.

*Excerpt from comb.py*

*Excerpt from ssh\_comb.py*

*Excerpt from ssh\_spray.py*

**2026-10-26 02:17:30 UTC** - The actor issued a bulk certificate managing task to 24 compromised Check Point Security Manager servers including those belonging to Victim A and 21 other victim assets. The results of this task were shipped back to the hop server in a text file. We did not observe the actor sending this command task to these devices, indicating that it was issued from another part of the adversary’s infrastructure.

Note that these text files contained the victim IP addresses and were in incrementing IP order, indicating an automation looped through them to run the commands on the compromised Check Point servers, and deliver them via scp to this exfil folder. Each file was delivered from victim infrastructure, showing that each of the compromised devices hold the SSH private key that matches the public key planted on the hop.

All of these files contain error messages which indicate that the certificate task failed. Though we did not see follow-on attempts, the task information and IP addresses from these outputs were enough for us to identify and notify many of the victim organizations either directly or through government partners.

*Excerpt from sample /root/exfil/pc\_XXX-XXX-XXX-XXX.txt*

One of the error messages had a preload error for /usr/lib/.libproc.so registered in /etc/ld.so.preload, which may indicate an implant on the device.

After the certificate minting failures, the actor’s activity dropped again until November 2nd.


### Protecting Their Access

**2026-11-02 02:28:27 UTC** - By early November, other threat actors had begun to scan and attempt to abuse the compromised server. We observed the GT13 actor use a script to perform a self-check for a Linux IPv4 use-after-free bug (CVE-2026-98432). After the check, the actor attempted to patch the system using Linux’s own command-line tool nftables to drop IPv4 packets with IP options that may trigger the bug. This allowed the actor to protect their hop from others engaging in future exploitation of the bug.

*Excerpt from cve\_2026\_98432.py*

*Example commands of the actor testing a CVE-2026-98432 script on the hop box, and then attempting to patch the vulnerability with nftables, the built-in Linux firewall and packet-filtering framework. You’ll notice the patching commands happened quickly.*


### Notes on Attack Timeframe and Timeline

- The GT13 adversary had access to the victim Check Point Security Management Servers before they compromised the HFS server. We could not determine when or how the attacker gained access to those Check Point assets.

- We observed GT13 attack activity between 2026-10-02 13:17:45 and 2026-11-02 03:19:46 UTC. During our observation of the actor, we did not observe any adversary hands-on-keyboard activity between \~17:00 UTC and \~00:19 UTC, and nothing in the 05:00 UTC hour. We know the risks of time zone analysis and do not put much weight into the actor’s tendency to operate in what would be a convenient UTC+7- or UTC+8 workday.

- The attack infrastructure was long established before we first saw it, as we note the attempted malware domain newpayapp\[.\]com was first registered on 2026-03-13 12:46:28 UTC. It may be a UTC+7-friendly coincidence that the domain was originally created with the registrant state as “Hai Phong” with country code “VN” (see [Cloudflare’s RDAP service](https://rdap.cloudflare.com/rdap/v1/domain/newpayapp.com)).

- We suspect the GT13 actor has a mature AI-enabled offensive apparatus. We believe the actor has separate agentic harnesses and systems weaponizing vulnerabilities, scanning for vulnerable assets, and automatically exploiting them to gather sets of systems that can be later used for operational relays or true targets. We suspect some of the foibles in the timeline reflect agentic offensive operations.


## Indicators

[Read the full report](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)
