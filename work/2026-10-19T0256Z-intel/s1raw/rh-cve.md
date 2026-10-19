---
title: CVE-2026-99999
url: https://access.redhat.com/security/cve/CVE-2026-99999
hostname: redhat.com
description: CVE Details App
sitename: access.redhat.com
date: "2026-10-15"
fingerprint: "9592f11dd47122c3"
---
# CVE-2026-99999

## Description

A flaw was found in the Linux kernel. A local attacker or untrusted guest virtual machine can exploit this vulnerability by transmitting network packets containing malformed checksum metadata into the IPv4 networking subsystem. This failure to validate checksum metadata can corrupt memory during packet handling, potentially leading to arbitrary code execution on the host, a system crash resulting in Denial of Service (DoS), or information disclosure of sensitive memory.

## Statement

This IMPORTANT-severity flaw affects the Linux kernel as shipped in Red Hat products, including the kernel and kernel-rt packages in Red Hat Enterprise Linux and the kernels shipped in Red Hat In-Vehicle OS. The IPv4 networking subsystem does not validate packet checksum metadata before completing a checksum: when a packet with a malformed checksum\_start value enters the IPv4 stack, skb\_checksum\_help() can write out of bounds and corrupt the network header and other kernel memory (CWE-787). A local attacker or an untrusted guest virtual machine able to transmit such packets into an affected host could exploit this to crash the system (denial of service), disclose sensitive kernel memory, or potentially execute arbitrary code on the host. Red Hat tracks this flaw as a KEV active-exploit case. All currently tracked Red Hat product streams are marked affected, and fixes are being pursued by the responsible Red Hat product teams under delegated resolution. Red Hat's severity differs from the upstream assessment: Red Hat assigns a CVSS 3.1 score of 8.8 (IMPORTANT, AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H), while the CVE.org record assigns 9.3 (CRITICAL, AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H); the two assessments differ on the privileges-required metric.

## Mitigation

Mitigation for this issue is either not available or the currently available options do not meet the Red Hat Product Security criteria comprising ease of use and deployment, applicability to widespread installation base, or stability.

## Common Vulnerability Scoring System (CVSS) Score Details

#### Info alert:Important note

CVSS scores for open source components depend on vendor-specific factors (e.g. version or build chain). Therefore, Red Hat's score and impact rating can be different from NVD and other vendors. Red Hat remains the authoritative [CVE Naming Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) source for its products and services (see [Red Hat classifications](https://access.redhat.com/security/updates/classification#cvss)).

The following CVSS metrics and score provided are preliminary and subject to review.

### CVSS v3 Score Breakdown

|  | Red Hat | NVD | cve.org | 
|---|---|---|---|
| Base Score | 8.8 | N/A | 9.3 | 
| Attack Vector | Local | N/A | Local | 
| Attack Complexity | Low | N/A | Low | 
| Privileges Required | Low | N/A | None | 
| User Interaction | None | N/A | None | 
| Scope | Changed | N/A | Changed | 
| Confidentiality | High | N/A | High | 
| Integrity Impact | High | N/A | High | 
| Availability Impact | High | N/A | High | 

### Vector

Red Hat: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H

cve.org: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H

## Understanding the Weakness (CWE)

### Integrity

Technical Impact: Modify Memory; Execute Unauthorized Code or Commands

Write operations could cause memory corruption. In some cases, an adversary can modify control data such as return addresses in order to execute unexpected code.

### Availability

Technical Impact: DoS: Crash, Exit, or Restart

Attempting to access out-of-range, invalid, or unauthorized memory could cause the product to crash.

### Other

Technical Impact: Unexpected State

Subsequent write operations can produce undefined or unexpected results.

## Frequently Asked Questions

Not sure what something means? Check out our [Security Glossary](https://access.redhat.com/security/glossary).

Want to get errata notifications? [Sign up here](https://www.redhat.com/wapps/ugc/protected/notif.html?extIdCarryOver=true&sc_cid=701f2000001Css5AAC).
