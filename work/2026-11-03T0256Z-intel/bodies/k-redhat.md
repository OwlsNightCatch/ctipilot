# extract: served via trafilatura-direct
---
title: CVE-2026-98432
url: https://access.redhat.com/security/cve/cve-2026-98432
hostname: redhat.com
description: CVE Details App
sitename: access.redhat.com
date: "2026-10-15"
fingerprint: "25bae525ce2998cb"
---
# CVE-2026-98432

## Description

A flaw was found in the Linux kernel's IPv4 networking subsystem. A race condition occurs during concurrent processing of retransmitted Transmission Control Protocol (TCP) connection requests or socket migrations, allowing socket options to be freed while still in use. A remote attacker could exploit this vulnerability by sending specially timed network requests, triggering a use-after-free condition. This could results in system crash leading to a Denial of Service (DoS), memory corruption, or remote code execution.

### Security Bulletin

## Statement

This vulnerability is rated as Critical severity for Red Hat Enterprise Linux because it allows an unauthenticated remote attacker to cause kernel memory corruption or an immediate system crash over standard IPv4 TCP network traffic without requiring local privileges or user interaction. In default enterprise configurations across Red Hat environments, TCP services accept incoming connections without specialized tuning, making the concurrent connection handling paths inherently exposed to remote networks. Although reliably executing arbitrary code through this timing-sensitive use-after-free scenario requires precise heap control, the lack of network prerequisites and the potential for severe system instability elevate the impact above Important.

## Mitigation

See the security bulletin for a detailed mitigation procedure.

## Common Vulnerability Scoring System (CVSS) Score Details

#### Info alert:Important note

CVSS scores for open source components depend on vendor-specific factors (e.g. version or build chain). Therefore, Red Hat's score and impact rating can be different from NVD and other vendors. Red Hat remains the authoritative [CVE Naming Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) source for its products and services (see [Red Hat classifications](https://access.redhat.com/security/updates/classification#cvss)).

### CVSS v3 Score Breakdown

|  | Red Hat | NVD | cve.org | 
|---|---|---|---|
| Base Score | 9.8 | N/A | 9.8 | 
| Attack Vector | Network | N/A | Network | 
| Attack Complexity | Low | N/A | Low | 
| Privileges Required | None | N/A | None | 
| User Interaction | None | N/A | None | 
| Scope | Unchanged | N/A | Unchanged | 
| Confidentiality | High | N/A | High | 
| Integrity Impact | High | N/A | High | 
| Availability Impact | High | N/A | High | 

### Vector

Red Hat: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

cve.org: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

## Frequently Asked Questions

Not sure what something means? Check out our [Security Glossary](https://access.redhat.com/security/glossary).

Want to get errata notifications? [Sign up here](https://www.redhat.com/wapps/ugc/protected/notif.html?extIdCarryOver=true&sc_cid=701f2000001Css5AAC).
