# extract: served via trafilatura-direct
---
title: CVE-2026-98432 | Ubuntu
url: https://ubuntu.com/security/CVE-2026-98432
hostname: ubuntu.com
description: Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things.
sitename: Ubuntu
date: "2026-10-15"
fingerprint: fd6751c91a00f3da
---
# CVE-2026-98432

Publication date 15 October 2026

Last updated 30 October 2026

Ubuntu priority

## Cvss 3 Severity Score

## Description

In the Linux kernel, the following vulnerability has been resolved: ipv4: free inet\_opt and ireq\_opt after an RCU grace period tcp\_v4\_syn\_recv\_sock() transfers ownership of ireq->ireq\_opt to the child socket (newinet->inet\_opt) without copying it. Another cpu can concurrently process a retransmitted SYN for the same request socket, and send a SYNACK from tcp\_check\_req(). tcp\_v4\_send\_synack() and inet\_csk\_route\_req() read ireq->ireq\_opt under rcu\_read\_lock() only, and ip\_build\_and\_send\_pkt() and ip\_options\_build() then read opt->optlen twice. Note that the SYNACK timer itself is not an issue: it holds a reference on its request socket, and inet\_csk\_reqsk\_queue\_drop() calls timer\_delete\_sync() before the child can be freed. Since commit 079096f103fa ("tcp/dccp: install syn\_recv requests into ehash table"), request sockets are processed without holding the listener lock, so nothing prevents the child socket from being freed while the SYNACK is still being built. TCP child sockets do not have SOCK\_RCU\_FREE, and inet\_sock\_destruct() frees inet\_opt with a plain kfree(), leading to a use-after-free in ip\_options\_build(). A similar issue exists with request socket migration (net.ipv4.tcp\_migrate\_req=1, or a BPF\_SK\_REUSEPORT\_SELECT\_OR\_MIGRATE program). reqsk\_timer\_handler() clones the request socket with inet\_reqsk\_clone(), so that the old request socket and its clone share the same ireq\_opt, then reqsk\_migrate\_reset() clears the pointer in the old one. Another cpu holding a reference on the old request socket can still be using these options (sending a SYNACK, or creating a child in tcp\_v4\_syn\_recv\_sock()) when the clone is freed, and tcp\_v4\_reqsk\_destructor() also uses a plain kfree(). Readers already use RCU, and other paths replacing inet\_opt (do\_ip\_setsockopt(), cipso\_v4\_sock\_setattr()...) already use kfree\_rcu(). Use kfree\_rcu() in inet\_sock\_destruct() and tcp\_v4\_reqsk\_destructor() as well. IPv6 is not affected by the first issue, because tcp\_v6\_syn\_recv\_sock() duplicates the options. tcp\_v6\_reqsk\_destructor() has the same migration issue with ipv6\_opt, which is only set by CALIPSO. This will be addressed in a separate patch.

### Why is this CVE high priority?

See ubuntu cvss score

## Status

| Package | Ubuntu Release | Status | 
|---|---|---|
| linux | 26.10 stonking | Vulnerable work in progress in 7.3.0-10.10 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-43.43 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-149.149 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-203.213 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not affected | 
| linux-hwe | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-149.149\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-hwe-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-hwe-edge | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Ignored end of standard support | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lts-xenial | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Vulnerable | 
| linux-kvm | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1112.117 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-allwinner-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.4 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1017.18 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1069.74 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1120.127 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Vulnerable | 
| linux-aws-5.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.3 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1120.127\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-1069.74\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 7.0.0-1017.18\~24.04.1 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-hwe | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.4 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1020.21 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1073.82 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1126.135 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Vulnerable | 
| linux-azure-4.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.3 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1126.135\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-1073.82\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-azure-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 7.0.0-1020.21\~24.04.1 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.5 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1019.19 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1071.78 | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-fde-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored replaced by linux-azure-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-nvidia | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-nvidia-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-bluefield | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-edge | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-149.149+fips2 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-203.213+fips1 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1069.74+fips1 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1120.127+fips1 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1073.82+fips1 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1126.135+fips1 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1121.131+fips1 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.4 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1017.19 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1073.81 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1121.131 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-4.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.3 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1121.131\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-1073.81\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-gcp-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 7.0.0-1017.19\~24.04.1 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gke | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1010.11 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1068.77 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1116.122 | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Ignored end of standard support | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gke-4.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gke-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gke-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gkeop | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1053.57 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1103.111 | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gkeop-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gkeop-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-ibm | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1018.18 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1069.70 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1114.118 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-ibm-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-ibm-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1114.118\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-ibm-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-intel-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-intel-iotg | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1115.121 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-intel-iotg-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1115.121\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-iot | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-intel-iot-realtime | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-149.149.1 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-198.208 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-198.208\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.2 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-149.149.1\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored replaced by linux-hwe-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1115.116 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-nvidia-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-nvidia-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of kernel support | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-bos | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-lowlatency | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-tegra | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-tegra-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-nvidia-tegra-igx | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.4 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1016.18 | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1067.71 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1117.123 | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.3 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress in 5.15.0-1117.123\~20.04.1 | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oracle-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oracle-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 7.0.0-1016.18\~24.04.1 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Ignored end of standard support | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-5.6 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-5.10 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-5.13 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-5.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-5.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.1 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-oem-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-oem-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-1018.18 | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-raspi | 26.10 stonking | Vulnerable work in progress in 7.3.0-1004.4 | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-raspi2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Ignored end of standard support | 
|  | 16.04 LTS xenial | Ignored end of standard support | 
|  | 14.04 LTS trusty | Not in release | 
| linux-raspi-5.4 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-raspi-realtime | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-realtime | 26.10 stonking | Vulnerable work in progress in 7.3.0-10.10.1 | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.1-1064.65 | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 5.15.0-1119.128 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-realtime-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-realtime-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv | 26.10 stonking | Vulnerable work in progress in 7.3.0-10.10.1 | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Ignored replaced by linux-riscv-6.14 | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-5.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-5.11 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of standard support | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable work in progress | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-riscv-6.8 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-6.8 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable work in progress in 6.8.0-149.149\~22.04.1 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-6.14 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-riscv-6.17 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-riscv-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-starfive-5.19 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-starfive-6.2 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-starfive-6.5 | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-starfive-6.5 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-vmware | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not affected | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-xilinx | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable work in progress in 6.8.0-1042.43 | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-xilinx-zynqmp | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-realtime-6.17 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 

### Patch details

| Package | Patch details | 
|---|---|
| linux |  | 

## Severity score breakdown

CVSS version:

**Base score**
      
      8.3 · High

**Vector:** CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N

**Base score**
      
      9.8 · Critical

**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
