---
title: Critical FortiSIEM Flaw Gets Public Exploit PoC for Unauthenticated Remote Code Execution
author: The Hacker News
url: https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html
hostname: thehackernews.com
description: Researchers release a PoC for critical FortiSIEM flaw CVE-2026-106173, showing how unauthenticated attackers can achieve remote code execution.
sitename: The Hacker News
date: "2026-10-20"
categories: ['Article']
fingerprint: "902afd96aab109e1"
---
Cybersecurity researchers have [released](https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/) a proof-of-concept (PoC) exploit for a recently patched critical security flaw impacting Fortinet FortiSIEM that could result in arbitrary code execution.

The vulnerability, tracked as **[CVE-2026-106173](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)** (CVSS score: 9.4), is a critical path traversal flaw that could allow an unauthenticated attacker to execute unauthorized code or commands via specially crafted packets.

Patches for the flaw were released last week by Fortinet in the following versions -

- FortiSIEM 7.5.0 (Upgrade to 7.5.1 or above)
- FortiSIEM 7.6 (Not affected)

According to Horizon3.ai, the issue involves an unauthenticated attacker connecting to the gRPC service listening on TCP port 27918 and exploiting the flaw to overwrite an existing file outside of the intended directory and turn the arbitrary-file-write primitive into remote code execution.

"The FortiSIEM gRPC QueryResultReq handler processes untrusted metadata without proper path validation," Horizon3.ai [said](https://github.com/horizon3ai/CVE-2026-106173). "By crafting metadata containing both path traversal sequences (../) and NUL-byte injection within gRPC's HTTP/2 and HPACK encoding layers, an attacker can write arbitrary files to the file system."

The problem stems from a case of unsafe path construction within a function named SendQueryResult(), which passes a user-supplied "query-id" parameter directly without sufficient validation.

In other words, an attacker can leverage this flaw to include directory traversal sequences such as "../" and escape that directory. However, this only allows an attacker to navigate to a directory of their choice and write to it, but not to opt for a file name because the program automatically adds its own file name "result-\<source IP address>-0-0-\<id>.dat," where \<id> is a counter value controlled by the server.

That's where a second weakness enters the picture: a null byte ("\0") can be embedded in the "query-id" parameter, causing the operating system to interpret it as a string terminator and discard everything that comes after it. This, in turn, results in the appended file name suffix being ignored when the path is passed to the file-opening function.

An attacker could exploit this behavior to craft a "query-id" value with "\0" placed such that it's preceded by the actual file name to be overwritten – i.e., "../../../../../opt/charting/redishb.sh\0..." The file in question is a shell script that performs health checks on the Redis service and is run every 60 seconds by a cron job.

"The write lands on the exact path that preceded the null byte," Zach Hanley, Chief Attack Engineer at Horizon3.ai, said. "Pointed at an existing file, this overwrites it in place, keeping the original owner and permissions; a second variant uses two requests to create a brand-new file with an exact name."

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
