# extract: served via trafilatura-direct
---
title: Critical Citrix NetScaler auth bypass now leveraged in attacks
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/
hostname: bleepingcomputer.com
description: Attackers have begun targeting a critical-severity Citrix NetScaler auth bypass flaw (CVE-2026-19490) in the wild, according to vulnerability intelligence company Previdian.
sitename: BleepingComputer
date: "2026-09-04"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, Authentication Bypass, Bypass, Citrix, Netscaler,virus removal, malware removal, computer help, technical support']
---
Attackers have begun targeting a critical-severity Citrix NetScaler flaw in the wild, according to vulnerability intelligence company Previdian.

Tracked as [CVE-2026-19490](https://nvd.nist.gov/vuln/detail/CVE-2026-19490), this security flaw can allow unprivileged threat actors to bypass authentication remotely when the NetScaler appliance is configured as an AAA virtual server or as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy), depending on the NetScaler firmware version and whether SAML Action is configured.

"We strongly recommend that customers review the official NetScaler ADC and NetScaler Gateway [security bulletin](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696939), assess whether their deployments are affected, and upgrade impacted appliances to the recommended builds as soon as possible," Citrix warned in mid-August when it addressed the flaw and [urged admins to patch it as soon as possible](https://www.bleepingcomputer.com/news/security/citrix-urges-admins-to-patch-new-netscaler-flaws-as-soon-as-possible/).

While the company has yet to flag the vulnerability as actively exploited in its [August 19 security advisory](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696939), Previdian founder and security researcher Ryan Dewhurst told BleepingComputer on Thursday that attackers [have begun targeting CVE-2026-19490 in the wild](https://previdian.com/CVE-2026-19490) after a "credible" proof-of-concept exploit was published online.

"On 3 September, one of our NetScaler sensors received requests matching the PoC from three distinct source IPs, geolocated to Australia, the United States and Germany," Dewhurst told BleepingComputer.

"Our current assessment is that this provides evidence of exploitation attempts, but it does not confirm successful compromise of real-world systems."

The Centre for Cybersecurity Belgium, the country's National Cybersecurity Coordination Centre for Belgium (NCC-BE), also [warned on Friday](https://ccb.belgium.be/advisories/warning-critical-authentication-bypass-citrix-netscaler-adc-netscaler-gateway-patch) of exploitation attempts targeting the CVE-2026-19490 vulnerability and urged admins to prioritize patching all vulnerable Citrix NetScaler appliances on their organizations' networks.

Although Internet threat watchdog Shadowserver tracks [over 22,000 NetScaler ADC](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=7&vendor=citrix&type=application-delivery-controller&model=netscaler&dataset=count&limit=100&group_by=geo&stacking=stacked) appliances and [nearly 1,700 Gateway](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=7&vendor=citrix&type=vpn&model=gateway&dataset=count&limit=100&group_by=geo&stacking=stacked) instances exposed online, there is no information on how many are honeypots, have vulnerable configurations, or have already been patched against CVE-2026-19490 attacks.

Citrix [urged admins](https://www.bleepingcomputer.com/news/security/citrix-urges-admins-to-patch-netscaler-flaws-as-soon-as-possible/) to patch two other NetScaler flaws ([CVE-2026-3055](https://nvd.nist.gov/vuln/detail/CVE-2026-3055) and [CVE-2026-4368](https://nvd.nist.gov/vuln/detail/CVE-2026-4368)) in March, just days before threat actors [began exploiting them in attacks](https://www.bleepingcomputer.com/news/security/critical-citrix-netscaler-memory-flaw-actively-exploited-in-attacks/).

The Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-3055) the CVE-2026-3055 flaw to its catalog of actively exploited vulnerabilities one week later and ordered federal agencies to patch vulnerable Citrix appliances within three days.

Since November 2021, the U.S. cybersecurity agency [has tagged 23 Citrix vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=citrix) as exploited in the wild, six of which have also been abused by ransomware gangs.

## 
            [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)
        

        Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
