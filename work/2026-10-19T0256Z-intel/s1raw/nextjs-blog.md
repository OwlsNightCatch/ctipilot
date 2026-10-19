---
title: Next.js Security Update for Upstream Vulnerabilities
author: Sebastian Silbermann; Josh Story; Karim Rahal
url: https://nextjs.org/blog/nextjs-security-update-october-14-2026
hostname: nextjs.org
description: The October 14, 2026 out-of-band security update for Next.js is now available
sitename: Next.js Security Update for Upstream Vulnerabilities
date: "2026-10-14"
fingerprint: "9e25ad116c398ba1"
---
Last week we announced an upcoming out-of-band security update for Next.js, including two fixes postponed from the September security release due to upstream dependency delays.

Updates are now available in v16.4.1 (Active LTS) and v15.5.28 (Maintenance LTS) to address these issues. Please patch your Next.js dependencies to maintain the security of your applications.

Terminal

npm install next@15.5.28 # for 15.5npm install next@16.4.1 # for 16.4

A vulnerability in applications using App Router with Cache Components can lead to unauthenticated remote code execution when a use cache function returns multiple typed arrays. There is no known workaround for affected applications. You should upgrade immediately even if your application does not have similar functions.

Copy link to headingUnauthenticated Remote Code Execution in the Image Optimization API when using SVG (Critical Severity)

A memory-related vulnerability in an upstream library used for Image Optimization can lead to remote code execution when Next.js runs on glibc-based Linux. As a workaround, ensure the version of sharp used by Next.js is 0.35.5 or later. Upgrading Next.js to the patched versions ensures package managers automatically provide a fixed version of sharp to Next.js.

Copy link to headingDenial of Service in App Router using Server Actions (High Severity)

Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service. Applications using Pages Router or not using Server Actions are not vulnerable.

We work with a talented set of researchers to secure Next.js and other open source frameworks through Vercel's Open Source Bug Bounty. Anyone interested in contributing to the security of eligible frameworks is encouraged to participate there.

Any questions or concerns regarding our security programs or vulnerability management can be sent to security@vercel.com.

Last week we announced an upcoming out-of-band security update for Next.js, including two fixes postponed from the September security release due to upstream dependency delays.

Updates are now available in v16.4.1 (Active LTS) and v15.5.28 (Maintenance LTS) to address these issues. Please patch your Next.js dependencies to maintain the security of your applications.

## Copy link to headingImpact

## Copy link to headingUnauthenticated Remote Code Execution in

`use cache`functions returning typed arrays (Critical Severity)GHSA-673q-mjm6-r5xr(Next.js)
Related upstream advisory:

GHSA-xqc2-xf4c-x3h3(React)
A vulnerability in applications using App Router with Cache Components can lead to unauthenticated remote code execution when a

`use cache`function returns multiple typed arrays. There is no known workaround for affected applications. You should upgrade immediately even if your application does not have similar functions.
## Copy link to headingUnauthenticated Remote Code Execution in the Image Optimization API when using SVG (Critical Severity)

CVE-2026-96889/GHSA-2464-fhr4-w9xw
A memory-related vulnerability in an upstream library used for Image Optimization can lead to remote code execution when Next.js runs on glibc-based Linux. As a workaround, ensure the version of

`sharp`used by Next.js is 0.35.5 or later. Upgrading Next.js to the patched versions ensures package managers automatically provide a fixed version of`sharp`to Next.js.
## Copy link to headingDenial of Service in App Router using Server Actions (High Severity)

GHSA-p3m5-59mp-jv5r(Next.js)
Related upstream advisory:

GHSA-h3gv-c5rc-p453(React)
Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service. Applications using Pages Router or not using Server Actions are not vulnerable.

## Copy link to headingOur security program

We work with a talented set of researchers to secure Next.js and other open source frameworks through Vercel's Open Source Bug Bounty. Anyone interested in contributing to the security of eligible frameworks is encouraged to participate there.

Any questions or concerns regarding our security programs or vulnerability management can be sent to security@vercel.com.
