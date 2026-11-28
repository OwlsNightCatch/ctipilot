---
title: "Advisory: NGINX Vulnerabilities - nginx2root (CVE-2026-123007 and others)"
url: https://www.sophos.com/en-us/security-advisories/sophos-sa-20261118-nginx2root
hostname: sophos.com
sitename: Sophos
date: "2025-11-25"
fingerprint: b0b8e4d14c341546
language: en
image: https://images.contentstack.io/v3/assets/blt38f1f401b66100ad/bltb4b6c0750dc5846c/6aad5e6160452d9f5056a4ef/logo.png
pagetype: website
filedate: "2026-11-28"
---
Informational

# Advisory: NGINX Vulnerabilities - nginx2root (CVE-2026-123007 and others)

CVE(S)

CVE-2026-123007

CVE-2026-123633

CVE-2026-123634

CVE-2026-121810

CVE-2026-113425

PRODUCT(S)

N/A

Updated

2026 Nov 23

Article Version

5

First Published

2026 Nov 18

Publication ID

sophos-sa-20261118-nginx2root

Workaround

No

## Overview

On November 18, 2026, F5 publicly disclosed several memory corruption vulnerabilities in NGINX Open Source and NGINX Plus, also referred to as “nginx2root”. F5 rates each of them CVSS 3.1 8.1 (High) and CVSS 4.0 9.2 (Critical):

- **CVE-2026-123007** and **CVE-2026-123633**: affect configurations with HTTP/2 enabled.
- **CVE-2026-121810**: affects configurations with HTTP/3 (QUIC) enabled.
- **CVE-2026-123634**: affects proxy configurations where the proxied server name contains variables and a mirror or Server Side Includes (SSI) subrequest resolves the same name.
- **CVE-2026-113425**: affects NGINX configured as a mail proxy.

An unauthenticated remote attacker could exploit these vulnerabilities to crash NGINX worker processes, corrupt their memory, and potentially execute code. Proof-of-concept exploit code for CVE-2026-123007 is publicly available. As of November 23, 2026, Sophos is not aware of any confirmed exploitation in the wild, and none of these vulnerabilities is listed in CISA’s Known Exploited Vulnerabilities catalog.

## Are Sophos products affected?

The following products have been reviewed against these vulnerabilities:

| Product or Service | Status | Description | 
|---|---|---|
| Sophos Central | Fixed | Sophos-hosted service. No customer action required. | 
| Sophos DNS Protection | Fixed | Sophos-hosted service. No customer action required. | 
| Taegis XDR | Fixed | Sophos-hosted service. No customer action required. | 
| Taegis VDR | Fixed | Sophos-hosted service. No customer action required. | 
| SG UTM (all versions) | Not affected | Component not present | 
| Sophos Mobile | Not affected | Component not present | 
| Sophos Mobile EAS Proxy | Not affected | Component not present | 
| Sophos Mobile Control app (iOS + Android) | Not affected | Component not present | 
| Sophos Chrome Security | Not affected | Component not present | 
| Sophos Endpoint Protection (macOS) | Not affected | Component not present | 
| Sophos Home (macOS) | Not affected | Component not present | 
| Taegis Endpoint Agent (macOS) | Not affected | Component not present | 
| Taegis Agent Backend | Not affected | Component not present | 
| Taegis NDR-C | Not affected | Component not present | 
| Taegis iSensor | Not affected | Component not present | 

Sophos is reviewing its other products and services for these vulnerabilities. We will update this advisory if any Sophos product or service requires customer action.

## General guidance for non-Sophos systems

The following guidance is for NGINX deployments that you manage yourself, such as web servers, reverse proxies and Kubernetes ingress controllers. It does not apply to Sophos products.

### Patching

NGINX Open Source 1.30.7 and 1.31.9 fix these vulnerabilities, and F5 has released fixed NGINX Plus builds. Update NGINX and restart it to load the patched binary. Linux distributions may backport fixes without changing the reported NGINX version, so check your distribution’s security advisories. Products that embed NGINX, such as OpenResty and Kubernetes ingress controllers, need their own updates; confirm patch status with those vendors.

### Identifying affected systems

- Identify NGINX instances, including those embedded in other products and container images, prioritising internet-facing systems.
- Prioritise instances where NGINX itself accepts client HTTP/2 or HTTP/3 connections.

### Temporary mitigation

[Xint](https://xint.io/blog/nginx2root-remote-code-execution) and [Wiz](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) report that disabling HTTP/2 blocks CVE-2026-123007 and CVE-2026-123633, and Xint reports that disabling HTTP/3 blocks CVE-2026-121810. These measures do not address the other vulnerabilities. Sophos has not validated them. Test them before deploying them, and treat them as temporary measures only. Updating NGINX is the only fix for these vulnerabilities.

## Related information

### Sophos Responsible Disclosure Policy

To learn about Sophos security vulnerability disclosure policies and publications, see the [Responsible Disclosure Policy](https://www.sophos.com/legal/sophos-responsible-disclosure-policy).
