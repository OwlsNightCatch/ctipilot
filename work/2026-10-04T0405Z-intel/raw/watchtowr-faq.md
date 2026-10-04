---
title: "Citrix NetScaler Zero-Day RCE FAQ: CVE-2026-88771 and CVE-2026-88772"
url: https://watchtowr.com/intelligence/citrix-netscaler-zero-day-vulnerabilities-faq/
hostname: watchtowr.com
description: Two Citrix NetScaler RCE zero-days, exploited in the wild and now fixed. What is affected, how to fix and check for compromise, and how watchTowr Rapid Reaction flagged exposure before the CVEs existed.
sitename: Watchtowr
date: "2026-09-27"
categories: ['Vulnerability FAQ']
---
## What are the Citrix NetScaler zero-day vulnerabilities?

CVE-2026-88771 and CVE-2026-88772 are critical remote code execution (RCE) vulnerabilities in Citrix NetScaler ADC and Citrix NetScaler Gateway that attackers exploited as zero-days, before any fix existed. Citrix confirmed both and released fixed builds on September 27, 2026 in security bulletin [CTX697096](https://support.citrix.com/external/article/CTX697096). Both are rated 9.5 Critical under CVSS 4.0. The same bulletin fixes six more NetScaler CVEs, all listed below.

| CVE | Description | CVSS 4.0 | Exploited in the wild | 
|---|---|---|---|
| [CVE-2026-88771](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) | Improper input validation that lets an unauthenticated attacker run arbitrary commands. Affects the default configuration. | 9.5 Critical | Yes | 
| [CVE-2026-88772](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) | Memory overflow that can lead to remote code execution or denial of service when DTLS is enabled (the default for VPN virtual servers). | 9.5 Critical | Yes | 
| [CVE-2026-88773](https://nvd.nist.gov/vuln/detail/CVE-2026-88773) | HTTP request smuggling (inconsistent interpretation of HTTP requests). Depends on specific configurations. | 9.3 Critical | Not reported | 
| [CVE-2026-88774](https://nvd.nist.gov/vuln/detail/CVE-2026-88774) | NetScaler ADC and NetScaler Gateway vulnerability. Depends on specific configurations. | 7.0 High | Not reported | 
| [CVE-2026-88775](https://nvd.nist.gov/vuln/detail/CVE-2026-88775) | Memory overflow. Depends on specific configurations. | 8.8 High | Not reported | 
| [CVE-2026-88776](https://nvd.nist.gov/vuln/detail/CVE-2026-88776) | Memory overflow. Depends on specific configurations. | 8.8 High | Not reported | 
| [CVE-2026-88777](https://nvd.nist.gov/vuln/detail/CVE-2026-88777) | Memory overflow. Depends on specific configurations. | 8.8 High | Not reported | 
| [CVE-2026-88778](https://nvd.nist.gov/vuln/detail/CVE-2026-88778) | Predictable value from previous values. Fixed by enabling Enhanced ISN Generation, not by the upgrade alone. | 8.8 High | Not reported | 

## Are CVE-2026-88771 and CVE-2026-88772 being exploited in the wild?

Yes. Citrix states it has observed exploitation of both vulnerabilities on unmitigated NetScaler deployments, and CISA reports that threat actors are exploiting them globally. CISA added CVE-2026-88771 and CVE-2026-88772 to its [Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771) on September 27, 2026.

## How did the NetScaler zero-days come to light?

Before Citrix published anything, NetScaler administrators reported being told by suppliers and security teams to shut their appliances down, following a private pre-notification from the Dutch National Cyber Security Centre (NCSC-NL). On September 26, 2026, [watchTowr publicly warned](https://x.com/watchtowrcyber) that multiple unpatched NetScaler remote code execution vulnerabilities were being exploited in the wild, that the information was credible and came from forensic investigations, and that Citrix patches were expected early the following week. Citrix published bulletin CTX697096 the next day.

## How is watchTowr helping NetScaler customers?

[watchTowr Rapid Reaction](https://watchtowr.com/use-cases/rapid-reaction/) identified NetScaler exposure across the watchTowr client base, and clients were made aware of their exposure on September 26, 2026, before Citrix’s bulletin and CVE IDs existed. [Attacker Eye](https://watchtowr.com/platform/#attacker-eye), our global honeypot network, is monitoring for exploitation activity as it emerges.

This is what [Preemptive Exposure Management](https://watchtowr.com/resources/what-is-preemptive-exposure-management-pem/) means in practice: knowing which of your systems an attacker can reach, and acting on it, while a vulnerability is still a zero-day. [Request a demo](https://watchtowr.com/demo/) to see how [Rapid Reaction](https://watchtowr.com/use-cases/rapid-reaction/) answers “are we affected?” within hours of an emerging threat.

Our [Rapid Reaction post](https://watchtowr.com/intelligence/citrix-netscaler-adc-citrix-netscaler-gateway-remote-code-execution-cve-2026-88771/) covers CVE-2026-88771 and CVE-2026-88772 in full.

## What is Citrix NetScaler ADC and NetScaler Gateway?

Citrix NetScaler ADC and Citrix NetScaler Gateway sit at the edge of enterprise networks, where they handle VPN and remote access, load balancing, and user authentication for staff and customers connecting to internal applications. A compromised appliance gives an attacker a foothold at the perimeter and a path to internal systems, which is why NetScaler vulnerabilities are prized by ransomware groups and state-sponsored attackers alike.

## Which NetScaler versions are affected?

| Product | Affected versions | Fixed version | 
|---|---|---|
| NetScaler ADC and NetScaler Gateway 14.1 | Before 14.1-73.37 | 14.1-73.37 and later | 
| NetScaler ADC and NetScaler Gateway 13.1 | Before 13.1-64.23 | 13.1-64.23 and later releases of 13.1 | 
| NetScaler ADC 14.1-FIPS | Before 14.1-73.37 FIPS | 14.1-73.37 FIPS and later | 
| NetScaler ADC 13.1-FIPS and 13.1-NDcPP | Before 13.1-37.279 | 13.1-37.279 and later | 

Secure Private Access hybrid deployments that use NetScaler instances are also affected. The bulletin applies to customer-managed appliances; Citrix updates its own managed cloud services. Prioritize every NetScaler Gateway, VPN and AAA virtual server reachable from the internet: the vulnerabilities need only network access, not a valid account.

## How do I fix CVE-2026-88771 and CVE-2026-88772?

Update every NetScaler ADC and NetScaler Gateway appliance to the fixed build for its branch. Citrix has not published a workaround for either vulnerability, so upgrading is the only fix. CISA advises checking for compromise and preserving forensic evidence first, because an update can remove the evidence.

1. Capture logs, a snapshot, a support bundle and a core dump from each exposed appliance.
2. Check for compromise (see the next question).
3. Install the fixed build. On 13.1, run `show ns variable` first: if it returns any variables, use 13.1-64.24 to avoid a known reboot loop during the upgrade.
4. Rotate passwords, secrets and certificates stored on or used through the appliance, and forward NetScaler logs to your SIEM.
5. Keep management interfaces off the public internet.

## How do I check a NetScaler appliance for compromise?

Run the IOC scan on the NetScaler Console Security Advisory page (version 14.1-73.36 or later, with telemetry enabled), or ask Citrix Support for the indicators of compromise (IOCs), as described on the [NetScaler blog](https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778/). Citrix warns that the IOCs do not cover every technique, so a clean result is not proof that an appliance was not compromised.

## What other NetScaler vulnerabilities does CTX697096 fix?

The same bulletin fixes six further NetScaler vulnerabilities, CVE-2026-88773 to CVE-2026-88778, that depend on specific configurations, including HTTP request smuggling and denial of service issues. CVE-2026-88778 is closed by configuration: enable [Enhanced ISN Generation](https://docs.netscaler.com/en-us/citrix-adc/current-release/system/tcp-configurations.html#enhanced-isn-generation), because the upgrade alone does not fix it.

## Are they related to CVE-2026-19490?

No. CVE-2026-19490 is an earlier NetScaler vulnerability that CISA added to the KEV catalog on September 9, 2026. Appliances patched for CVE-2026-19490 remain vulnerable to CVE-2026-88771 and CVE-2026-88772 unless they run one of the fixed builds above.

## Which threat actors are exploiting them?

No attribution has been made public. Historically, NetScaler vulnerabilities have been exploited by both state-sponsored groups and ransomware operators.

## Have there been similar NetScaler vulnerabilities before?

Yes. These earlier NetScaler vulnerabilities were added to the CISA KEV catalog after exploitation in the wild:

| CVE | Description | Added to KEV | 
|---|---|---|
| CVE-2026-19490 | NetScaler ADC and NetScaler Gateway vulnerability | September 9, 2026 | 
| CVE-2026-8452 | NetScaler ADC and NetScaler Gateway buffer overflow | August 26, 2026 | 
| [CVE-2026-3055](https://watchtowr.com/intelligence/rapid-reaction-to-cve-2026-3055/) | NetScaler out-of-bounds read | March 30, 2026 | 
| CVE-2025-7775 | NetScaler memory overflow | August 26, 2025 | 
| [CVE-2025-5777](https://labs.watchtowr.com/how-much-more-must-we-bleed-citrix-netscaler-memory-disclosure-citrixbleed-2-cve-2025-5777/) | NetScaler ADC and Gateway out-of-bounds read (“CitrixBleed 2”), analyzed by watchTowr Labs | July 10, 2025 | 
| CVE-2025-6543 | NetScaler ADC and Gateway buffer overflow | June 30, 2025 | 
| CVE-2023-4966 | NetScaler ADC and Gateway buffer overflow (“CitrixBleed”) | October 18, 2023 | 
| CVE-2023-3519 | NetScaler ADC and Gateway code injection | July 19, 2023 |
