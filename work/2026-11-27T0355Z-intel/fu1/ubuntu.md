---
title: CVE-2026-99362
url: https://ubuntu.com/security/CVE-2026-99362
hostname: ubuntu.com
description: Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things.
sitename: Ubuntu
date: "2026-11-19"
fingerprint: fd6751c91a00f3da
language: en
image: https://assets.ubuntu.com/v1/47f12466-og_%20ubuntu.png
pagetype: website
filedate: "2026-11-27"
---
# CVE-2026-99362

Publication date 19 November 2026

Last updated 25 November 2026

Ubuntu priority

## CVSS 3 severity score

## Description

In the Linux kernel, the following vulnerability has been resolved: nfsd: preflight SEQUENCE replies before accepting a slot nfsd4\_sequence() narrows the reply buffer to the session's cached reply limit before it accepts the slot seqid. A client may negotiate ca\_maxresponsesize\_cached down to NFSD\_MIN\_HDR\_SEQ\_SZ, and nfsd4\_alloc\_slot() then gives every slot a zero-length sl\_data\[\]. A COMPOUND tag can fill that narrowed buffer until it holds the SEQUENCE opcode but not the status word that follows. nfsd4\_encode\_operation() returns without running nfsd4\_encode\_sequence(), so cstate.data\_offset stays zero. It leaves op->status at nfs\_ok as well, so the COMPOUND is treated as having succeeded. nfsd4\_store\_cache\_entry() declines to cache a lone SEQUENCE that returned an error. That test reads the status the operation reported, so it passes here. The copy starts at offset zero and takes the whole reply, RPC and COMPOUND headers included, into the zero-length sl\_data\[\]. The COMPOUND tag is copied along with it, so the client picks most of the bytes written past the end of the slot: BUG: KASAN: slab-out-of-bounds in read\_bytes\_from\_xdr\_buf+0x1bc/0x390 Write of size 80 at addr ffff888003a549cd by task kunit\_try\_catch/24 \_\_asan\_memcpy+0x38/0x60 read\_bytes\_from\_xdr\_buf+0x1bc/0x390 nfsd4\_sequence\_done+0x5b0/0x810 nfs4svc\_encode\_compoundres+0x1bf/0x240 Check that the fixed-size SEQUENCE result, plus room for a following operation's error status, fits the negotiated limit before narrowing the buffer and consuming the slot seqid. The slot and its reply cache are left unchanged, as RFC 8881 Section 2.10.6.1.2 requires of an error returned from SEQUENCE.

### Why is this CVE critical priority?

See ubuntu cvss score

## Status

| Package | Ubuntu Release | Status | 
|---|---|---|
| linux | 26.10 stonking | Vulnerable work in progress in 7.3.0-12.13 | 
|  | 26.04 LTS resolute | Vulnerable work in progress in 7.0.0-45.45 | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
| linux-aws | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
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
| linux-azure | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fde | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Vulnerable | 
|  | 14.04 LTS trusty | Not in release | 
| linux-aws-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-azure-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp-fips | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Vulnerable | 
|  | 18.04 LTS bionic | Vulnerable | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gcp | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-gke | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-intel-iotg-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-lowlatency-hwe-5.15 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
| linux-oracle | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 24.04 LTS noble | Vulnerable | 
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
|  | 24.04 LTS noble | Ignored end of life, was needs-triage | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-oem-7.0 | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-raspi | 26.10 stonking | Vulnerable | 
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
| linux-realtime | 26.10 stonking | Vulnerable | 
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Vulnerable | 
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
| linux-riscv | 26.10 stonking | Vulnerable | 
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
|  | 20.04 LTS focal | Vulnerable | 
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
|  | 22.04 LTS jammy | Vulnerable | 
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
|  | 26.04 LTS resolute | Vulnerable | 
|  | 24.04 LTS noble | Vulnerable | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Not in release | 
|  | 18.04 LTS bionic | Not in release | 
|  | 16.04 LTS xenial | Not in release | 
|  | 14.04 LTS trusty | Not in release | 
| linux-xilinx | 26.10 stonking | Not in release | 
|  | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Vulnerable | 
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

## Severity score breakdown

CVSS version:

**Base score**
        
          
        
        9.3 · Critical

**Vector:** CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N

**Base score**
        
          
        
        9.8 · Critical

**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
