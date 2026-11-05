---
title: "November 2026 Security Updates #2 for XCP-ng 8.3 LTS"
author: Samuel Verschelde
url: https://xcp-ng.org/blog/2026/11/04/november-2026-security-updates-2-for-xcp-ng-8-3-lts/
hostname: xcp-ng.org
description: The fix for the critical Linux kernel vulnerability CVE-2026-98432, announced in our previous post, is now available. It can be triggered remotely on XCP-ng 8.3 hosts. Update and reboot as soon as possible, or apply the mitigation until you can.
sitename: XCP-ng Blog
date: "2026-11-04"
tags: ['Security', 'Update']
fingerprint: d5a35113d8b1f6f3
---
# November 2026 Security Updates #2 for XCP-ng 8.3 LTS

New updates are available for [XCP-ng 8.3 LTS](https://docs.xcp-ng.org/management/updates/#support-cycle).

[follow this guide](https://docs.xcp-ng.org/management/updates/). You can also join

[the discussion](https://xcp-ng.org/forum/topic/9964/xcp-ng-8-3-updates-announcements-and-testing/)on our community forum.

**Host reboots are necessary after this update.**

XCP-ng's updates are cumulative, so applying updates now will also apply any previous updates that weren't applied to your hosts. Update advisories: [https://xcp-ng.org/blog/tag/update/](https://xcp-ng.org/blog/tag/update/).

## Summary

As announced in our [previous update post](https://xcp-ng.org/blog/2026/11/03/november-2026-security-and-maintenance-updates-1-for-xcp-ng-8-3-lts/) published yesterday (please read too it if you missed it), this update fixes a critical vulnerability in the Linux kernel of the control domain (Dom0). It can be triggered remotely, without authentication, by anyone able to send network traffic to the host, and could lead to a compromise of the host.

We advise updating as soon as possible. If you can't reboot your hosts right away, don't apply the update yet, and apply the iptables-based mitigation described in the VSA instead. It takes effect immediately, without a reboot, and protects your hosts until they run the fixed kernel, so you may plan the reboot for your next maintenance window.

Some details below. The comprehensive version is [the Vates Security Advisory (VSA)](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-056) itself.

## Security updates

### Linux kernel: use-after-free in IPv4 TCP connection handling

A flaw in the way the Linux kernel handles incoming IPv4 TCP connections lets an attacker make the kernel use memory that was already freed, by sending TCP packets that carry IP options. This can lead to code execution with kernel privileges in Dom0, the control domain. Dom0 controls the whole host, so its compromise means a compromise of the host and of all its VMs.

Anyone who can send TCP traffic to the host can attempt this, for example from its management network, including VMs connected to that network.

A public exploit exists. It relies on MPTCP, which the XCP-ng 8.3 kernel doesn't have, so this exploit doesn't work against XCP-ng. The underlying bug is present nonetheless, and other ways to exploit it can't be ruled out.

References: [VSA-2026-056](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-056), [CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432)
