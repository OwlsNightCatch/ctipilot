---
title: Unauthenticated Remote Code Execution in Image Optimization API when SVG files are used
author: Eps
url: https://github.com/vercel/next.js/security/advisories/GHSA-2464-fhr4-w9xw
hostname: github.com
description: "<!-- https://linear.app/vercel/issue/NSEC-386 --> ## Impact A memory-related vulnerability has been discovered in an upstream library used for Image Optimization can lead to possible remote c..."
sitename: GitHub
date: "2026-10-14"
categories: ['repository:70107786']
fingerprint: "95342bc7ec339ae2"
---
  
    
## Impact

A memory-related vulnerability has been discovered in an upstream library used for Image Optimization can lead to possible remote code execution (RCE) when Next.js runs on glibc-based Linux.

## Workaround

Ensure the version of `sharp` used by Next.js is greater than or equal to `0.35.5`. Fresh installs automatically get a fixed version fo `sharp`.

Upgrading Next.js to the patched versions will ensure package managers automatically provide a fixed version of `sharp` to Next.js.

## Impact

A memory-related vulnerability has been discovered in an upstream library used for Image Optimization can lead to possible remote code execution (RCE) when Next.js runs on glibc-based Linux.

## Workaround

Ensure the version of

`sharp`used by Next.js is greater than or equal to`0.35.5`. Fresh installs automatically get a fixed version fo`sharp`.
Upgrading Next.js to the patched versions will ensure package managers automatically provide a fixed version of

`sharp`to Next.js.
