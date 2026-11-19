---
title: "GitHub - sfewer-r7/CVE-2026-123007: Proof-of-concept (PoC) scripts for CVE-2026-123007, an integer underflow in NGINX HTTP/2."
url: https://github.com/sfewer-r7/CVE-2026-123007
hostname: github.com
description: Proof-of-concept (PoC) scripts for CVE-2026-123007, an integer underflow in NGINX HTTP/2. - sfewer-r7/CVE-2026-123007
sitename: GitHub
date: "2026-11-18"
categories: ['repository:1462695234']
fingerprint: "9d81947749e0f5c2"
---
This repository contains proof-of-concept (PoC) scripts for CVE-2026-123007. For a technical analysis of the vulnerability, see the [Rapid7 blog](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed/).

The file [NGINX\_HTTP2\_STANDALONE\_REPRODUCTION.md](https://github.com/sfewer-r7/CVE-2026-123007/blob/main/NGINX_HTTP2_STANDALONE_REPRODUCTION.md) details the reproduction steps.

The file [simple-trigger-poc.py](https://github.com/sfewer-r7/CVE-2026-123007/blob/main/simple-trigger-poc.py) is a minimal Python script to trigger the root cause issue.

The file [exploit/exploit.py](http://exploit/exploit.py) is a PoC exploit script to demonstrate unauthenticated RCE via CVE-2026-123007 against a vulnerable NGINX server running in a Docker container. This PoC is only suitable to demonstrate the given RCE exploitation strategy against a local freshly started Docker container. The PoC will likely fail against a vulnerable NGINX server which has multiple concurrent clients, or which has a "messy" initial heap layout (i.e. a worker process has been running and servicing requests for some time), where available network bandwidth is not sufficient to transfer the large amount of required data in a timely or consistent fashion, or where network proxying is in-place which may alter the exploits use of HTTP/2 frames. The PoC makes no attempt to account for these conditions. Alternative RCE exploitation strategies may be viable, but none are currently known.

The below video shows the PoC exploit achieving unauthenticated RCE against a vulnerable `linux/amd64` Docker image running NGINX version `1.31.8`.
