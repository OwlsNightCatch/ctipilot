---
title: "NFS2ROOT (CVE-2026-99362) FAQ: Linux NFS Exposure and Fix"
url: https://watchtowr.com/intelligence/nfs2root-linux-nfs-cve-2026-99362-faq/
hostname: watchtowr.com
description: NFS2ROOT (CVE-2026-99362) is an Out-of-bounds Write in Linux NFS. See affected versions, the fix, and how to check systems; updated as details emerge.
sitename: watchTowr
date: "2026-11-26"
categories: ['Vulnerability FAQ']
tags: ['CVE-2026-99362', 'Linux NFS', 'NFS2ROOT', 'Out-of-bounds Write']
fingerprint: bdba391fc991b7a9
language: en
image: https://watchtowr.com/wp-content/uploads/nfs2root-linux-nfs-cve-2026-99362-faq.png
pagetype: article
filedate: "2026-11-27"
---
## What is NFS2ROOT?

CVE-2026-99362, part of the issue known as NFS2ROOT, is an Out-of-bounds Write in the Linux kernel's built-in NFS server, called nfsd. It occurs while the server processes SEQUENCE replies that manage NFS version 4.1 session slots. A connecting client can negotiate the server's cached reply size down to the smallest possible value, leaving no room in the slot's reply buffer. The server then copies an entire reply, including protocol headers, into that undersized buffer, writing past its end.

Because the bytes written past the buffer come largely from the client's own request, a remote client can corrupt memory inside the Linux kernel over an ordinary network connection. The server also sends much of that overwritten data back to the client in its reply. With the returned memory chunks attackers can map out the kernel layout address space and craft a payload that can execute instructions on the vulnerable host.

| CVE | Description | CVSS | Exploited in the wild | 
|---|---|---|---|
| [CVE-2026-99362](https://nvd.nist.gov/vuln/detail/CVE-2026-99362) | Out-of-bounds Write in Linux NFS | 9.8 Critical (CVSS 3.1) | Not reported | 

## Is NFS2ROOT being exploited in the wild?

As of November 26, 2026, no exploitation in the wild has been reported.

## How did NFS2ROOT come to light?

CVE-2026-99362 was introduced in the Linux kernel as a bug in March 2014 starting from version 3.16. The bug was surfaced upstream by the community on August 17, 2026 and reported as a security issue by OpenSec on September 21, 2026. On November 19, 2026 the vulnerability was published along with patches.

## How is watchTowr helping Linux NFS customers?

- [Adversary Sight engine](https://watchtowr.com/platform/#adversary-sight) identified Linux NFS instances across client environments and assessed exposure.
- [Rapid Reaction](https://watchtowr.com/use-cases/rapid-reaction/) identified exposure to this vulnerability across the watchTowr client base, giving teams the time they need to act.

## What is Linux NFS?

Linux NFS is the Network File System service built into the Linux kernel, which lets Linux hosts share files and directories with other systems over a network. The nfsd component handles these requests at the kernel level, and enterprise networks commonly rely on it for shared storage between servers and clients.

## Which Linux NFS versions are affected?

| Product | Affected Versions | Fixed Version | 
|---|---|---|
| Linux kernel 5.10 series | 3.16 up to but not including 5.10.275 | 5.10.275 | 
| Linux kernel 5.15 series | 3.16 up to but not including 5.15.226 | 5.15.226 | 
| Linux kernel 6.1 series | 3.16 up to but not including 6.1.193 | 6.1.193 | 
| Linux kernel 6.6 series | 3.16 up to but not including 6.6.163 | 6.6.163 | 
| Linux kernel 6.12 series | 3.16 up to but not including 6.12.117 | 6.12.117 | 
| Linux kernel 6.18 series | 3.16 up to but not including 6.18.61 | 6.18.61 | 
| Linux kernel 7.3 series | 3.16 up to but not including 7.3.2 | 7.3.2 | 
| Linux kernel mainline | 3.16 up to but not including 7.4-rc1 | 7.4-rc1 | 

- The affected system must run the Linux kernel's built-in NFS server with NFS version 4.1 or later sessions, since the issue lies in handling SEQUENCE replies used in that protocol version.
- A connecting client must negotiate its cached reply size down to the server's minimum header size before the server accepts the session slot, as the CVE record describes.
- The CVE record marks the Linux kernel as affected by default from version 3.16 onward, with no additional configuration needed to be exposed.

Security teams should prioritize Linux systems that run the in-kernel NFS server with NFS version 4.1 sessions enabled and that accept connections from outside networks, since the issue affects session handling that any connecting client can influence.

## How do I fix NFS2ROOT?

Update the Linux kernel to the fixed version for the running branch, such as 6.12.117, 6.18.61, 7.3.2, or 7.4-rc1, then reboot. If patching is not immediately possible, restrict access to port 2049 for internet exposed systems or turn off NFSv4.1 and 4.2 in the NFS service configuration file.

1. Identify all Linux hosts running the in-kernel NFS server, nfsd.
2. Determine which kernel branch and exact version each host runs.
3. Update affected hosts to the fixed kernel version listed for their branch.
4. Reboot each updated host so the new kernel code takes effect.
5. Confirm the running kernel version matches or exceeds the fixed version after reboot.

## What types of threat actors typically exploit this vulnerability?

No attribution has been made public.
