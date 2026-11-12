---
title: Fortinet Releases Security Hardening Release for Multiple Products | CISO Collective
author: Carl Windsor
url: https://www.fortinet.com/blog/ciso-collective/fortinet-releases-security-hardening-release-for-multiple-products
hostname: fortinet.com
description: Fortinet announces frontier AI hardening releases for a range of products including FortiOS, FortiManager, FortiAnalyzer, FortiMail, and FortiAuthenticator.…
sitename: Fortinet Blog
date: "2026-10-21"
categories: ['CISO Collective']
tags: ['artificial intelligence (AI),CISO Collective,AI-Driven Security Operations,artificial intelligence', 'artificial intelligence (AI)', 'AI-Driven Security Operations', 'artificial intelligence']
fingerprint: "7b3139c6e4a555c9"
---

# Fortinet Releases Security Hardening Release for Multiple Products

Preparing for the forthcoming security hardening releases, including frontier AI fixes and how this will change the release process going forward

**UPDATED November 10, 2026:** Today, Fortinet published our monthly PSIRT advisory as part of our standard disclosure process, which includes fixes resulting from the frontier AI-assisted product security testing described below. This ongoing effort complements the conventional methods we employ to identify and address vulnerabilities. This approach gives customers time to prioritize upgrades before additional technical details become public, which matters even more as AI shortens the time between disclosure and exploitation. For more detail on the advisories, please visit the Fortinet [PSIRT Advisories page](https://www.fortiguard.com/psirt).


On October 22, 2026, Fortinet will release a coordinated set of security updates for FortiOS, FortiManager, and FortiAnalyzer following recent releases from FortiMail and FortiAuthenticator. We strongly urge every customer to plan and promptly complete these upgrades as soon as the releases are available, prioritizing internet-facing devices

These releases include fixes to address vulnerabilities identified through our [frontier AI-assisted security testing program](https://www.fortinet.com/blog/ciso-collective/update-on-fortinet-use-of-frontier-ai). Fortinet would like to thank Anthropic, OpenAI, Google, and SpaceX for their collaboration throughout this process.

Fortinet has integrated frontier AI models into our product security testing process. These models analyze code paths, protocol handling, and configuration logic at a depth and speed that traditional fuzzing and manual review cannot match.

This work has helped surface vulnerabilities more efficiently than conventional methods, allowing us to proactively fix them before they may be found and exploited by malicious actors. This is our secure-by-design commitment in practice: finding and closing weaknesses at the source.

We are also being transparent about one implication. The same class of AI capability is becoming available to attackers, particularly as open weight models improve. The window between disclosure and exploitation continues to shrink, and we expect it to keep shrinking.

We recommend customers treat this release as a priority change rather than a routine maintenance cycle. Four factors drive this urgency:

1. **Criticality of fixes:** These releases include critical and high-severity fixes.
2. **Faster weaponization:** AI tools can now help adversaries reverse-engineer patches and build working exploits in hours or days, rather than weeks.
3. **Patch diffing risk:** Once updates are public, the fixes themselves reveal where changes were made, exposing a potential system weakness. Unpatched devices then become easier targets for attackers.
4. **Chaining of vulnerabilities:** AI has the ability to link seemingly unrelated lower severity vulnerabilities together to achieve a more severe, exploitable vulnerability.

Our recommendation is to apply temporary mitigations, including limiting exposure by managing devices out of band, moving resources behind VPN or SASE where feasible, and applying virtual patches until the patching can be prioritized.

**Affected products and fixed versions**

| Product | Affected Versions | Fixed Version | Availability | 
|---|---|---|---|
| FortiOS 8.0 | 8.0.0–8.0.1 | 8.0.2 or above | October 22 | 
| FortiOS 7.6 | 7.6.0–7.6.7 | 7.6.8 or above | October 22 | 
| FortiOS 7.4 | 7.4.0–7.4.12 | 7.4.13 or above | October 22 | 
| FortiOS 7.2 | 7.2.0–7.2.13 | 7.2.14 or above | October 22 | 


| Product | Affected Versions | Fixed Version | Availability | 
|---|---|---|---|
| FortiManager 8.0 | 8.0.0–8.0.1 | 8.0.2 or above | October 22 | 
| FortiManager 7.6 | 7.6.0–7.6.7 | 7.6.8 or above | October 22 | 
| FortiManager 7.4 | 7.4.0–7.4.11 | 7.4.12 or above | October 22 | 
| FortiManager 7.2 | 7.2.0–7.2.12 | 7.2.13 or above | October 22 | 


| Product | Affected Versions | Fixed Version | Availability | 
|---|---|---|---|
| FortiAnalyzer 8.0 | 8.0.0–8.0.1 | 8.0.2 or above | October 22 | 
| FortiAnalyzer 7.6 | 7.6.0–7.6.7 | 7.6.8 or above | October 22 | 
| FortiAnalyzer 7.4 | 7.4.0–7.4.11 | 7.4.12 or above | October 22 | 
| FortiAnalyzer 7.2 | 7.2.0–7.2.12 | 7.2.13 or above | October 22 | 


| Product | Affected Versions | Fixed Version | Availability | 
|---|---|---|---|
| FortiMail 8.0 | 8.0.0–8.0.1 | 8.0.2 or above | Today | 
| FortiMail 7.6 | 7.6.0–7.6.6 | 7.6.7 or above | Today | 
| FortiMail 7.4 | 7.4.0–7.4.8 | 7.4.9 or above | Today | 
| FortiMail 7.2 | 7.2.0–7.2.9 | Upgrade to 7.4 branch or later | Today | 


| Product | Affected Versions | Fixed Version | Availability | 
|---|---|---|---|
| FortiAuthenticator 8.0 | 8.0.0–8.0.3 | 8.0.4 or above | Today | 
| FortiAuthenticator 6.6 | 6.6.0–6.6.10 | 6.6.11 or above | Today | 

Note that public advisories will be made available at the next Patch Tuesday on November 10 as part of Fortinet’s ongoing commitment to responsible transparency while balancing customer security. The advisories will be published on the [Fortinet Product Security Incident Response Team (PSIRT) page.](https://www.fortiguard.com/psirt)

- FortiSASE will be automatically updated prior to the release on October 22.
- FortiManager Cloud releases will be available for update by October 22 but may require manual update.
- Updates for public cloud instances are in the process of being pushed out via the relevant cloud partners. Please follow their standard releases process.

Prepare today so you can upgrade as soon as these releases are published on October 22.

- **Inventory:** Identify every FortiManager device and FortiOS instance, prioritizing those that are exposed to the internet
- **Schedule maintenance windows:** Prioritize change windows for October 22–23 for internet-facing systems
- **Back up configurations:** Save current configurations before upgrading
- **Monitor:** Watch logs for unusual administrative access or unapproved configuration changes before and after patching

If you cannot upgrade immediately, reduce exposure in the interim by:

- Restricting administrative interfaces (HTTPS, SSH) to trusted IP addresses or disable them on external interfaces
- Ensuring FortiManager administration is not reachable from the internet
- Following best practices, which include:
  - Using strong unique credentials
  - Enforcing MFA for all administrator accounts

These steps reduce risk but do not replace the need for a timely upgrade.

We believe customers are best protected when vendors proactively find and fix vulnerabilities and disclose them responsibly. Using frontier AI in our own testing is another way we stay ahead of attackers using the same tools. We will continue to apply these methods across the Fortinet portfolio and share our findings with customers in the spirit of security transparency.

Thank you for acting quickly. For upgrade assistance, contact Fortinet Technical Support or your account team. Subscribe to [FortiGuard PSIRT advisories](https://www.fortiguard.com/psirt) for release-day details.


*- Carl Windsor, Chief Information Security Officer, Fortinet*


| [Join](https://global.fortinet.com/lp-en-wc-2026Q4-ciso-collective?lsci=701Pr00000valFjIAI&meeting_offer__c=&UID=ftnt-3346-563028) Carl Windsor on Wednesday, December 9 at 8 a.m. PT \| 11 a.m. ET \| 4 p.m. GMT for the next Fortinet Global CISO Collective, our quarterly conversation built by and for CISOs. | 

[**Learn**](https://www.fortinet.com/content/dam/fortinet/assets/solutions/fortinet-ai-enabled-security.pdf) how to prepare for AI enabled cyber events
