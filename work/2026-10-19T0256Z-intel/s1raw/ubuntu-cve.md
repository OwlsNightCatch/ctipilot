---
title: CVE-2026-99999 | Ubuntu
url: https://ubuntu.com/security/CVE-2026-99999
hostname: ubuntu.com
description: Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things.
sitename: Ubuntu
date: "2026-10-15"
fingerprint: d467d1c85a00fb5e
---
# CVE-2026-99999

Publication date 15 October 2026

Last updated 15 October 2026

Ubuntu priority

## Cvss 3 Severity Score

## Description

In the Linux kernel, the following vulnerability has been resolved: ipv4: validate checksum\_start before completing checksum If a packet with bad checksum metadata gets into the ipv4 stack, skb\_checksum\_help can corrupt the network header and cause a bunch of mischief. This was discovered and reported by Paulos, and has been reporoduced by others independently since. We really shouldn't allow such packets in, but as a defence in depth measure, let's also check before we complete the checksum. A more complete validation at input is forthcoming, but needs more work.

## Status

| Package | Ubuntu Release | Status | 
|---|---|---|
| linux | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
|  | 16.04 LTS xenial | Needs evaluation | 
|  | 14.04 LTS trusty | Needs evaluation | 
| linux-hwe | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored replaced by linux-hwe-5.4 | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-hwe-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-hwe-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-hwe-5.11 | 
| linux-hwe-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-hwe-5.13 | 
| linux-hwe-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-hwe-5.15 | 
| linux-hwe-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-hwe-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.2 | 
| linux-hwe-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.5 | 
| linux-hwe-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-hwe-6.8 | 
| linux-hwe-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-hwe-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-hwe-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-hwe-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-hwe-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-hwe-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-hwe-edge | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-hwe-5.4 | 
|  | 16.04 LTS xenial | Ignored superseded by linux-hwe | 
| linux-lts-xenial | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 14.04 LTS trusty | Needs evaluation | 
| linux-kvm | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-allwinner-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
| linux-aws | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
|  | 16.04 LTS xenial | Needs evaluation | 
|  | 14.04 LTS trusty | Needs evaluation | 
| linux-aws-5.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-aws-5.3 | 
| linux-aws-5.3 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-aws-5.4 | 
| linux-aws-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-aws-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-aws-5.11 | 
| linux-aws-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-aws-5.13 | 
| linux-aws-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-aws-5.15 | 
| linux-aws-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-aws-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.2 | 
| linux-aws-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.5 | 
| linux-aws-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-aws-6.8 | 
| linux-aws-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-aws-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-aws-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-aws-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-aws-hwe | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-azure | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Ignored superseded by linux-azure-5.3 | 
|  | 16.04 LTS xenial | Needs evaluation | 
|  | 14.04 LTS trusty | Needs evaluation | 
| linux-azure-4.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-azure-5.3 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-azure-5.4 | 
| linux-azure-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-azure-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-azure-5.11 | 
| linux-azure-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-azure-5.13 | 
| linux-azure-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-azure-5.15 | 
| linux-azure-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-azure-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.2 | 
| linux-azure-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.5 | 
| linux-azure-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-6.8 | 
| linux-azure-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-azure-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-azure-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-fde | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Ignored superseded by linux-azure-fde-5.15 | 
| linux-azure-fde-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-azure-fde-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-azure-fde-6.2 | 
| linux-azure-fde-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored replaced by linux-azure-6.5 | 
| linux-azure-fde-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-azure-fde-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-fde-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-fde-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-nvidia | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-azure-nvidia-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-bluefield | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-azure-edge | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-azure-5.3 | 
| linux-fips | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-aws-fips | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-azure-fips | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-gcp-fips | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-gcp | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Ignored superseded by linux-gcp-5.3 | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-gcp-4.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-gcp-5.3 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-gcp-5.4 | 
| linux-gcp-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-gcp-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-gcp-5.11 | 
| linux-gcp-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-gcp-5.13 | 
| linux-gcp-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-gcp-5.15 | 
| linux-gcp-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-gcp-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.2 | 
| linux-gcp-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.5 | 
| linux-gcp-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-gcp-6.8 | 
| linux-gcp-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-gcp-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-gcp-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-gcp-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-gcp-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-gcp-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-gke | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
| linux-gke-4.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-gke-5.0 | 
| linux-gke-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored end of kernel support | 
| linux-gke-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
| linux-gkeop | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
| linux-gkeop-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored end of kernel support | 
| linux-gkeop-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
| linux-ibm | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-ibm-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-ibm-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-ibm-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-intel-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored end of kernel support | 
| linux-intel-iotg | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-intel-iotg-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-iot | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-intel-iot-realtime | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-lowlatency | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-lowlatency-hwe-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-lowlatency-hwe-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.2 | 
| linux-lowlatency-hwe-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.5 | 
| linux-lowlatency-hwe-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-lowlatency-hwe-6.8 | 
| linux-lowlatency-hwe-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-lowlatency-hwe-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored replaced by linux-hwe-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-nvidia-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-nvidia-6.5 | 
| linux-nvidia-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-nvidia-6.8 | 
| linux-nvidia-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-nvidia-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored end of kernel support | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia-bos | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia-lowlatency | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-nvidia-tegra | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-nvidia-tegra-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-nvidia-tegra-igx | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-oracle | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
|  | 18.04 LTS bionic | Needs evaluation | 
|  | 16.04 LTS xenial | Needs evaluation | 
| linux-oracle-5.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-oracle-5.3 | 
| linux-oracle-5.3 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored superseded by linux-oracle-5.4 | 
| linux-oracle-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-oracle-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oracle-5.11 | 
| linux-oracle-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oracle-5.13 | 
| linux-oracle-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oracle-5.15 | 
| linux-oracle-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-oracle-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oracle-6.8 | 
| linux-oracle-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-oracle-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oracle-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oracle-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oem | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Ignored replaced by linux-hwe-5.4 | 
| linux-oem-5.6 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oem-5.10 | 
| linux-oem-5.10 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oem-5.13 | 
| linux-oem-5.13 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-oem-5.14 | 
| linux-oem-5.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored replaced by linux-hwe-5.15 | 
| linux-oem-5.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.1 | 
| linux-oem-6.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.1 | 
| linux-oem-6.1 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.5 | 
| linux-oem-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-oem-6.8 | 
| linux-oem-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-oem-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oem-6.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-oem-6.14 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oem-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oem-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-oem-7.0 | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
| linux-raspi | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-raspi2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored replaced by linux-raspi | 
| linux-raspi-5.4 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 18.04 LTS bionic | Needs evaluation | 
| linux-raspi-realtime | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-realtime | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-realtime-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
| linux-realtime-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
| linux-riscv | 26.04 LTS resolute | Needs evaluation | 
|  | 24.04 LTS noble | Ignored replaced by linux-riscv-6.14 | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
|  | 20.04 LTS focal | Ignored superseded by linux-riscv-5.8 | 
| linux-riscv-5.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-riscv-5.11 | 
| linux-riscv-5.11 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Ignored superseded by linux-riscv-5.13 | 
| linux-riscv-5.15 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-riscv-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
| linux-riscv-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-riscv-6.8 | 
| linux-riscv-6.8 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
| linux-riscv-6.14 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Ignored superseded by linux-riscv-6.17 | 
|  | 22.04 LTS jammy | Not in release | 
| linux-riscv-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-riscv-7.0 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-starfive-5.19 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
| linux-starfive-6.2 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored superseded by linux-starfive-6.5 | 
| linux-starfive-6.5 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Ignored end of kernel support | 
| linux-vmware | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-xilinx | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Needs evaluation | 
|  | 22.04 LTS jammy | Not in release | 
| linux-xilinx-zynqmp | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Needs evaluation | 
|  | 20.04 LTS focal | Needs evaluation | 
| linux-realtime-6.17 | 26.04 LTS resolute | Not in release | 
|  | 24.04 LTS noble | Not in release | 
|  | 22.04 LTS jammy | Not in release | 

## Severity score breakdown

CVSS version: CVSS v3.0

**Base score**
      
      9.3 · Critical

**Vector:** CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
