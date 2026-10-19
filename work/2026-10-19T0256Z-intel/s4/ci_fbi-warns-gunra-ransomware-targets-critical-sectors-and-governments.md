---
title: FBI warns Gunra ransomware targets critical sectors and governments
author: Amar Ćemanović
url: https://cyberinsider.com/fbi-warns-gunra-ransomware-targets-critical-sectors-and-governments/
hostname: cyberinsider.com
description: US warns organizations about Gunra, an emerging ransomware operation that has attacked critical organizations and governments worldwide.
sitename: CyberInsider
date: "2026-08-11"
categories: ['News', 'Ransomware']
fingerprint: a73e80db96a7e24d
---
US authorities are warning organizations about Gunra, an emerging ransomware operation that has attacked victims worldwide, stolen as much as tens of terabytes of data in individual incidents, and opened ransom negotiations at amounts exceeding tens of millions of dollars.

The group targets organizations across healthcare and finance, government, manufacturing, transportation, utilities, and retail.

The FBI first observed Gunra in April 2025, according to a [joint advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a) published on August 10, 2026, by the FBI, CISA, the Department of Defense Cyber Crime Center, the NSA, the US Secret Service, and South Korea’s National Police Agency (KNPA). Investigations into attacks and the Gunra infrastructure showed that the operation expanded into a ransomware-as-a-service (RaaS) program in January 2026, providing affiliates with ransomware builders and Windows and Linux payloads. The gang has also used the Golden Community alias to recruit penetration testers and ethical hackers to gain access to enterprise networks.

Gunra victims have appeared across the Americas, Europe, the Middle East, Africa, and Asia-Pacific, spanning at least ten broad sectors. The ransomware is believed to be based on or heavily influenced by the Conti ransomware source code leaked in 2022. Like many modern ransomware groups, Gunra uses double extortion, in which attackers steal sensitive information before encrypting systems, then threaten to publish or sell the stolen files if payment is not made.

Authorities found that Gunra frequently gains entry by exploiting vulnerabilities in internet-facing firewalls and VPN appliances. In particular, the FBI linked attacks to CVE-2024-55591 and CVE-2025-24472, authentication-bypass flaws affecting certain FortiOS and FortiProxy versions. In some incidents, attackers also abused default credentials, compromised administrator accounts, hijacked user sessions, and modified authentication systems so an attacker-controlled one-time password could bypass MFA.

Once inside, Gunra operators use tools including Impacket, Mimikatz, RClone, FileZilla, 7-Zip, AnyDesk, and Sliver to steal credentials, move between systems, and extract data. The FBI observed a malicious main.exe utility used to steal files from Microsoft OneDrive and SharePoint, with one victim losing data measured in the tens of terabytes. Stolen archives were also uploaded to the Mega file-sharing service.

The ransomware encrypts files using ChaCha20 and RSA-4096, typically adds the .ENCRT extension, and leaves a R3ADM3.txt ransom note. Victims are generally given 5 to 7 days to negotiate via Tor or qTox. Attackers have also deleted Windows shadow copies and, in one case, destroyed backup data at both primary and disaster-recovery sites before and after deploying ransomware.

The agencies recommend immediately patching known exploited vulnerabilities in exposed VPN and remote-access systems, eliminating default credentials, segmenting networks, and maintaining tested offline and immutable backups that are isolated from production infrastructure. Organizations should also investigate unexpected privileged accounts and unusual access to VPN, VDI, OneDrive, and SharePoint environments.

## Leave a Reply Cancel reply
