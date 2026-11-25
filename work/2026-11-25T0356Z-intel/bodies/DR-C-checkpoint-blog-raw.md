---
title: Security Advisory - Action Required - July 2026 Security Update
author: Lotem Finkelstein; VP Research
url: https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-check-point-smartconsole-authentication-bypass-cve-2026-16232/
hostname: checkpoint.com
description: As part of Check Point’s Frontier AI Readiness Program, we are releasing a jumbo hotfix with security and hardening fixes for our firewall and management %
sitename: Check Point Blog
date: "2026-07-22"
fingerprint: "8c3564574530ec5d"
language: en
image: https://blog.checkpoint.com/wp-content/uploads/2026/07/sa-july-2026-800x400px.jpg
pagetype: article
filedate: "2026-11-25"
---
# Security Advisory – Action Required – July 2026 Security Update

**Lotem Finkelstein, VP Research**

As part of Check Point’s Frontier AI Readiness Program, we are releasing a jumbo hotfix with security and hardening fixes for our firewall and management products.

This update includes a number of security hardening improvements and fixes, the most significant of which are outlined below.

During a routine BLAST review, we discovered a few vulnerabilities. Following a thorough analysis, we identified one of those in the wild, affecting a handful of customers. This only affects a very specific configuration — when Management is exposed directly to the internet without IP restrictions. All affected customers have been notified. All Smart-1 Cloud customers are already protected.

This is exactly why programs like BLAST exist: to find and close gaps before they become real risks. We’ll keep pushing the technological frontier, so organizations stay protected against what’s coming next. It’s proof of our ongoing commitment to the highest level of product security, and to keeping our customers protected.

We encourage all customers to install the jumbo hotfix and follow our published security best practices.

| CVE | Description | CVSS | Affected Products | Affected Versions | In the Wild | SK | 
|---|---|---|---|---|---|---|
| CVE-2026-16232 | Authentication bypass with SmartConsole login using application token – Management | 9.3 | Security Management, Multi-Domain Management | R81.10, R81.20, R82, R82.10 (older versions impacted as well) | Yes, for a handful of customers with specific configurations. |                       [sk185169](https://support.checkpoint.com/results/sk/sk185169)  | 
| CVE-2026-62144 | Management authentication bypass and privilege escalation | 9.3 | Security Management, Multi-Domain Management | R81.10, R81.20, R82, R82.10 (older versions impacted as well) | No |                       [sk185152](https://support.checkpoint.com/results/sk/sk185152)  | 
| CVE-2026-62145 | Local privilege escalation in GaiaOS WebUI – Gateway | 7.5 | Firewall, Multi-Domain Management, Multi-Domain Log Server | R81.10, R81.20, R82, R82.10 (older versions impacted as well) | No |                       [sk185153](https://support.checkpoint.com/results/sk/sk185153)  | 

Additional information can be found in the respective Secure Knowledge updates as linked below.

### IoCs

IP addresses observed:

151.241.99\[.\]207

151.241.99\[.\]233

158.62.198\[.\]182

192.142.10\[.\]99

139.28.37\[.\]250

194.213.18\[.\]137

### Mitigation

Apply the following steps to mitigate the Management vulnerabilities:

1. Limit Trusted Clients (GUI clients) to trusted IP addresses/subnets.
2. Protect Management access with Firewall, restrict access to trusted IP addresses, and verify that implied rules for control connections are enabled.

### Solution

Install the latest Jumbo hotfix released today (July 22, 2026).

### Need support?

If you need help assessing your exposure, applying a mitigation, or installing the hotfix, please contact Check Point Support at:

[checkpoint.com/support-services/contact-support/](https://www.checkpoint.com/support-services/contact-support/)
