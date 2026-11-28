---
title: "Cacti Zero-Day (4HTTP2ROOT): What We Know So Far"
author: Ryan Dewhurst
url: https://blog.previdian.com/cacti-zero-day-what-we-know-so-far/
hostname: previdian.com
description: "Published: 26 November 2026 | Last Updated: 26 November 2026 (UTC) Security researcher ek0ms savi0r has disclosed \"4HTTP2ROOT\", a zero-day unauthenticated stored SQL injection vulnerability in Cacti that can lead to remote code execution (RCE) when guest access is enabled. Previdian observed exploitation attempts targeting the vulnerability on 27 November"
sitename: Previdian Research
date: "2026-11-26"
fingerprint: "19103359cd7856c1"
language: en
image: https://storage.ghost.io/c/1c/21/1c213298-6101-4c8a-9e02-660a9e08724c/content/images/size/w1200/2026/11/cacti-0day-feature.png
pagetype: article
filedate: "2026-11-28"
---
# Cacti Zero-Day (4HTTP2ROOT): What We Know So Far

**Published:** 26 November 2026 | **Last Updated:** 26 November 2026 (UTC)

Security researcher ek0ms savi0r has disclosed **"4HTTP2ROOT"**, a zero-day unauthenticated stored SQL injection vulnerability in Cacti that can lead to remote code execution (RCE) when guest access is enabled.

**Previdian observed exploitation attempts targeting the vulnerability on 27 November 2026, less than 24 hours after public disclosure.**

A public exploit demonstrates command execution against Cacti 1.2.31 (latest) in just four HTTP requests, without requiring valid credentials, when guest access is enabled.

Previdian has verified the PoC in a lab environment.

Previdian is tracking this as [VULN-2026-0010](https://previdian.com/VULN-2026-0010?ref=blog.previdian.com)

## At a Glance

| **CVE** | Not publicly assigned | 
| **Affected Product** | Cacti | 
| **Confirmed Affected Version** | 1.2.31 | 
| **Vulnerability Type** | Unauthenticated stored SQL injection | 
| **Impact** | Remote code execution (RCE) | 
| **Severity** | Official CVSS score unavailable | 
| **Authentication Required** | No | 
| **Exploitation Prerequisite** | Guest access enabled | 
| **Exploitation Status** | Demonstrated in a laboratory | 
| **Public Exploit** | Available | 
| **Patch Available** | No confirmed fix | 

## What Is 4HTTP2ROOT?

[Research published by ek0ms savi0r](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell?ref=blog.previdian.com) demonstrates how insufficient validation of guest-controlled settings introduces a stored, second-order SQL injection vulnerability.

The SQL injection can be leveraged to manipulate Cacti's polling configuration, ultimately resulting in arbitrary operating system command execution.

The researcher demonstrated root-level command execution in a laboratory environment where Cacti was running with root privileges. On typical deployments, commands would execute with the privileges of the affected application process.

Compromising a Cacti server could expose sensitive network infrastructure credentials, potentially enabling lateral movement into internal networks.

## Who Is Affected?

The exploit has been demonstrated against Cacti 1.2.31 with guest access enabled.

According to [Cacti's official documentation](https://github.com/Cacti/documentation/blob/develop/User-Management.md?ref=blog.previdian.com), anonymous guest access is disabled by default but can be enabled to provide unauthenticated access to monitoring graphs.

The full affected version range has not yet been established.

## Is 4HTTP2ROOT Being Exploited in the Wild?

Yes. On 27 November 2026, Previdian observed 22 SQL injection attempts originating from a single source IP against our real Cacti application honeypots.

The requests contained time-based SQL injection payloads designed to test whether the newly disclosed vulnerability was exploitable. Successful remote command execution has not been confirmed.

Previdian added the vulnerability to its autonomous Watch on 26 November, approximately 14 hours before the first observed exploitation attempts.

The vulnerability is now included in Previdian KEV as [VULN-2026-0010](https://previdian.com/VULN-2026-0010?ref=blog.previdian.com).

## Is a Patch or Mitigation Available?

As of 26 November 2026, no official patch addressing 4HTTP2ROOT has been identified.

Cacti 1.2.31, the latest stable version identified in the [official release repository](https://github.com/Cacti/cacti/releases?ref=blog.previdian.com), is affected.

Disabling guest access removes a prerequisite of the publicly demonstrated unauthenticated exploit chain. This should be considered an interim mitigation, not a fix for the underlying SQL injection vulnerability.

## What Should Defenders Do?

- **Disable guest access:** Remove the designated Guest User in Cacti's Authentication Settings and disable the guest account under Console > Configuration > Users.
- **Verify access restrictions:** Confirm that a fresh, unauthenticated browser session can no longer access protected application functionality.
- **Restrict network exposure:** Limit Cacti access to trusted management networks or authenticated VPN users.
- **Hunt for compromise:** Investigate unexpected changes to user settings, polling configurations and unusual process execution.
- **Enforce least privilege:** Ensure Cacti's application and polling processes do not unnecessarily run as root.
- **Monitor for patches:** Follow the [official Cacti security advisories](https://github.com/Cacti/cacti/security/advisories?ref=blog.previdian.com).

If compromise is suspected, assess the exposure of network device credentials stored within Cacti and rotate potentially compromised credentials.

## What Remains Unknown?

- The assigned CVE identifier and official CVSS score.
- The complete affected version range.
- Whether exploitation has occurred in production environments.
- When an official security patch will become available.

## Updates

- **27 November 2026:** Previdian observed exploitation attempts against our real Cacti application honeypots, approximately 14 hours after adding the vulnerability to Watch. Added to Previdian KEV.
- **26 November 2026:** Initial public disclosure and proof of concept.

## References

## Stay Ahead of Emerging Vulnerabilities

Previdian combines real-time exploitation intelligence from our proprietary honeypot network with early warnings, continuous exposure checks and virtual patching.
