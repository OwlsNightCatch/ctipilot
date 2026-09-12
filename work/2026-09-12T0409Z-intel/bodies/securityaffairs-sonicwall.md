---
title: UK Council Attack Linked to Mass Exploitation of SonicWall Flaw
author: Pierluigi Paganini
url: https://securityaffairs.com/198864/hacking/uk-council-attack-linked-to-mass-exploitation-of-sonicwall-flaw.html
hostname: securityaffairs.com
description: A critical SonicWall flaw was rapidly weaponized, with a UK Council attack linked to a campaign that exposed credentials and enabled AD theft
sitename: Security Affairs
date: "2026-09-11"
categories: ['Breaking News', 'Hacking', 'Security']
tags: ['CVE-2026-15409', 'Active Directory', 'Hacking', 'hacking news', 'information security news', 'IT Information Security', 'Pierluigi Paganini', 'Security Affairs', 'Security News', 'SonicWall', 'UK Council']
---
On July 17, 2026, the Borough Council of King’s Lynn and West Norfolk announced it had detected a cyberattack affecting council services. Hunt.io has since published a detailed technical analysis linking that incident, with moderate confidence, to a wider mass-exploitation campaign against SonicWall SMA1000 appliances using [CVE-2026-15409](https://securityaffairs.com/tag/cve-2026-15409), a maximum-severity SSRF flaw that received a CVSS score of 10.0.

CVE-2026-15409 affects the WorkPlace portal’s WebSocket proxy. An attacker does not need to log in. By sending a specially crafted request to `/wsproxy`, they can make the appliance connect to port 1050 on its own local system, where a CouchDB-related Erlang service is running.

The attacker can then use a hardcoded cookie found in the appliance firmware to complete the Erlang connection and access the [\[email protected\]](https://securityaffairs.com/cdn-cgi/l/email-protection)`couchdb` account.

The attack may sound complicated, but once automated, an attacker can complete all the steps in just a few seconds.

*“Across the wider campaign, compromised appliances were used as footholds into internal networks. The operator deployed a standalone Linux build of Impacket’s secretsdump directly onto selected SonicWall appliances, enabling remote credential theft from internal Windows systems.” reads the report published by Hunt.io. “This approach could help the actor evade detection, as organisations typically have substantially less visibility into the underlying operating systems of firewall and VPN appliances than into managed Windows and Linux hosts monitored by EDR.”*

Rapid7 researchers published a proof-of-concept on July 15. The operator had adapted it into a 50-thread mass scanner by July 16. Rapid7’s own Managed Detection and Response team had already observed active exploitation of the vulnerability before SonicWall’s July 14 advisory, meaning the gap between zero-day exploitation and mass-scale automated campaigns was effectively less than three days.

Hunt.io’s AttackCapture system crawled the attacker’s open directory at 95.181.173[.]36 on July 17, the same day the council announced its incident. That directory contained the operator’s complete toolchain: scan scripts, exploit code, credential-parsing utilities, a standalone Impacket binary, and the output files from the ongoing campaign.

The campaign data covered 250 target appliances. Of those, 168 exposed LDAP configuration files containing credentials for 534 Active Directory accounts across 160 domain names and 255 internal LDAP server addresses. Nine of those environments lost SAM and LSA secrets to the operator. Five lost their entire Active Directory database through full DCSync replication, targeting seven domain controllers in total.

After gaining access, the attackers follow a clear process. Their `ldap_extract.py` script reads `/usr/local/extranet/etc/policy_file.xml` from each compromised appliance and decrypts the LDAP passwords stored in the file.

The decryption uses a fixed 32-byte AES key embedded in the `ASAPPasswordUtil.class` code. This means the same key can work on every SonicWall SMA1000 device running vulnerable firmware.

Once they obtain valid LDAP credentials, the attackers download a standalone Linux version of Impacket’s `secretsdump` to `/tmp/secretsdump` from their server using `curl`. They then use the SonicWall appliance’s network access to run the tool against internal Windows systems and extract credentials and other sensitive information.

A SonicWall VPN appliance running `secretsdump` against internal domain controllers doesn’t trigger EDR alerts on Windows endpoints, doesn’t appear in Windows event logs as a rogue process, and doesn’t show up in most SIEM rules tuned for managed hosts. The appliance is doing exactly what it’s supposed to do: connecting to internal systems. The malicious traffic blends into legitimate network behaviour.

When the LDAP credentials did not have enough privileges to perform DCSync, the attackers used LSA secrets recovered with `secretsdump`. These secrets can contain the NTLM hash of a domain controller’s machine account. Because domain controllers normally have directory replication rights, the attackers could use these hashes to perform DCSync.

Their scripts searched the `secretsdump` output for account names ending in `$`, extracted the related hashes, and used them to launch pass-the-hash DCSync requests through the compromised SonicWall appliance.

The technique worked in five environments. The attackers used the SonicWall appliance to create NTDS database files in `/tmp` and then retrieved them by exploiting CVE-2026-15409 to execute commands on the device.

*“The appliances associated with confirmed SAM and LSA theft were distributed across infrastructure in France, India, Italy and the United States.” Hunt.io states. “The wider target inventory was considerably broader, containing named gateways associated with organisations in the United Kingdom, Canada, Germany, Sweden, Poland, Hungary, South Korea and Hong Kong, among other locations.”*

The sectors covered included local government and law enforcement, healthcare, financial services, universities, manufacturing, and managed IT providers. The targeting was opportunistic: the operator selected organizations because they ran a vulnerable SonicWall appliance, not because of what sector they were in. That’s consistent with the Shodan-derived target lists recovered from the directory, which contained nearly 200,000 addresses labelled as SonicWall systems.

The scripts contained extensive Chinese-language comments, but Hunt.io assessed this as insufficient for attribution. CISA added CVE-2026-15409 to its Known Exploited Vulnerabilities catalog and noted it had been used in ransomware campaigns. A separate threat actor tracked as [UTA0533](https://securityaffairs.com/198303/security/sonicwall-patches-two-new-actively-exploited-zero-days-in-sma-1000-vpns.html) used the same vulnerability to deploy [KNUCKLEBALL](https://securityaffairs.com/195626/hacking/volexity-uncovers-zero-day-campaign-targeting-sonicwall-vpn-appliances.html) malware, and the ransomware group INC has also exploited the vulnerability chain. Multiple actors using the same CVSS-10 flaw in parallel is now the normal pattern for critical VPN and access device vulnerabilities, not an anomaly.

For SonicWall SMA1000 operators who haven’t patched: the fixed firmware versions are 12.4.3-03453 and later. Patching alone isn’t sufficient if exploitation has already occurred. SonicWall recommends re-imaging affected appliances, rotating all user and administrator credentials, and resetting TOTP tokens. The Hunt.io report includes specific log locations and indicators of compromise for assessments. The SHA-256 of the Impacket binary the operator used is `690f5031deede7d3357d0ca24c89866ae8c60e6c63b3a2c8bba813a6ac10ae5b`, and the delivery IP was 95.181.173[.]36.

The operator ran their entire post-exploitation framework from an open HTTP server on port 80 without authentication. The exploitation was technically capable. The operational security was not. Hunt.io captured the whole operation while it was still running.

*“The retained evidence shows how quickly public vulnerability research can be operationalised. By 16 July 2026, two days after SonicWall disclosed CVE-2026-15409, a threat actor was using modified, multithreaded tooling to identify vulnerable SMA 1000 appliances, extract and decrypt LDAP credentials, and automate follow-on credential theft against internal Active Directory environments.” concludes the report. “Deploying a standalone Linux build of Impacket directly to compromised edge appliances made the operation both scalable and evasive. Most organisations have substantially less process, file and network visibility into the underlying operating systems of security appliances than they have through EDR on managed Windows and Linux hosts. This visibility gap allowed the SonicWall appliances to function as internal attack platforms from which the operator collected SAM and LSA secrets and, in five AD domains, performed full DCSync replication.”*

**Follow me on Twitter:** **@securityaffairs** **and** **Facebook** **and** **Mastodon**

**(****SecurityAffairs** **– hacking, SonicWall)**
