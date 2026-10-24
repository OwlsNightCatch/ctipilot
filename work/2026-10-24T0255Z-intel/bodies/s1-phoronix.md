---
title: Several Linux Kernel Vulnerabilities Accidentally Posted To Public Kernel Mailing List
author: Michael Larabel
url: https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities
hostname: phoronix.com
description: Seemingly as an accident, overnight several new Linux kernel vulnerability reports were posted to the public Linux kernel mailing list rather than the private security mailing list
sitename: Phoronix
date: "2026-10-22"
tags: ['Phoronix, Linux Hardware Reviews, Linux hardware benchmarks, Linux server benchmarks, Linux benchmarking, Desktop Linux, Linux performance, Open Source graphics, Linux How To, Ubuntu benchmarks, Ubuntu hardware, Phoronix Test Suite']
fingerprint: b43329d6dca5942a
---
# Several Linux Kernel Vulnerabilities Accidentally Posted To Public Kernel Mailing List

Seemingly as an accident, overnight several new Linux kernel vulnerability reports were posted to the public Linux kernel mailing list rather than the private security mailing list. The vulnerabilities have yet to be patched on mainline but at least in some cases there are patches undergoing testing or queued in "-next" branches. The CVSS scores are as high as 9.0.


Trend Micro's Zero Day Initiative sent out a number of vulnerability reports to the public Linux kernel mailing list (LKML) rather than the typical private security mailing list. This seemingly was a mistake with Linux's second-in-command Greg Kroah-Hartman responding to each report asking about their submission to the public mailing list.


Among these newly-disclosed vulnerabilities include:


[ZDI-CAN-33549](https://lore.kernel.org/lkml/BYAPR01MB3830472B5702C089B0BBB77D80662@BYAPR01MB3830.prod.exchangelabs.com/)  as a CVSS 9.0 scored vulnerability for SMB Direct remote code execution vulnerability due to integer underflow. For this one there is a patch in a Git branch of code intended for Linux v7.5 but now presumably will be expedited for getting to mainline.


[ZDI-CAN-33774](https://lore.kernel.org/lkml/BYAPR01MB383076AC412E19C48CFBEAE980662@BYAPR01MB3830.prod.exchangelabs.com/) as a KSMBD race condition that can lead to remote code execution. Another CVSS 9.0 rated vulnerability.


[ZDI-CAN-33367](https://lore.kernel.org/lkml/BYAPR01MB3830CECF5D0871064C59BA0280662@BYAPR01MB3830.prod.exchangelabs.com/) is a vulneravbility for skbuff skb\_zerocopy in the network code that can lead to local privilege escalation. For this one Linux kernel developers received a security report from another source last week over the same issue and a patch is expected to be posted soon.


[ZDI-CAN-34068](https://lore.kernel.org/dri-devel/2026102254-protector-seventy-6454@gregkh/) as a VMWGFX VMware graphics driver bug with an out-of-bounds write leading to local privilege escalation.


[ZDI-CAN-34076](https://lore.kernel.org/all/2026102226-duly-imprison-a2c1@gregkh/) an uninitialized resource in the NVMET code leading to information disclosure.


[ZDI-CAN-32005](https://lore.kernel.org/all/BYAPR01MB383046745372577D8F5902D580672@BYAPR01MB3830.prod.exchangelabs.com/) was also posted to the mailing list a day prior for a search-domain TCP query stack buffer overflow leading to local privilege escalation.


The bug and security reports keep on coming in the AI fueled world.

25 Comments
