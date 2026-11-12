---
title: oss-security
url: https://www.openwall.com/lists/oss-security/2026/11/11/13
hostname: openwall.com
sitename: openwall.com
date: "2026-11-11"
fingerprint: "8be17fd2e3d6bd82"
---
|   |  | 

|  | 

|  [Follow @Openwall on Twitter for new release announcements and other news](https://twitter.com/openwall) | 

Message-ID: \<2df72d8d-1eb3-9b55-74bd-f4cb1af17a87@apache.org>
Date: Wed, 11 Nov 2026 12:19:30 +0000
From: Eric Covener \<covener@...che.org>
To: oss-security@...ts.openwall.com
Subject: CVE-2026-119618: Apache HTTP Server: mod\_http2: heap corruption
 and RCE in assign\_headers 
Severity: critical 
Affected versions:
- Apache HTTP Server 2.4.55 through 2.4.70
Description:
Concurrent Execution using Shared Resource with Improper Synchronization vulnerability in Apache HTTP Server's mod\_http2 in assign\_headers() can lead to RCE.
This issue affects Apache HTTP Server: from 2.4.55 through 2.4.70.
Affected releases of mod\_h2 from GitHub: from 2.0.8 through 2.0.42.
Credit:
Anthropic's OSS Scanner, as vulnerability ANT-2026-MAPKT6MZ (finder)
Anthony Weems and Simon Scannell of the Google Cloud Vulnerability Research (finder)
References:
[https://httpd.apache.org/security/vulnerabilities\_24.html](https://httpd.apache.org/security/vulnerabilities_24.html)
[https://httpd.apache.org/](https://httpd.apache.org/)
[https://www.cve.org/CVERecord?id=CVE-2026-119618](https://www.cve.org/CVERecord?id=CVE-2026-119618)
Timeline:
2026-10-26: reported

[Powered by blists](https://www.openwall.com/blists/) - [more mailing lists](https://lists.openwall.net)

Please check out the
[Open Source Software Security Wiki](https://oss-security.openwall.org/wiki/), which is counterpart to this
[mailing list](https://oss-security.openwall.org/wiki/mailing-lists/oss-security).

Confused about [mailing lists](https://www.openwall.com/lists/) and their use?
[Read about mailing lists on Wikipedia](https://en.wikipedia.org/wiki/Electronic_mailing_list)
and check out these
[guidelines on proper formatting of your messages](https://www.complang.tuwien.ac.at/anton/mail-news-errors.html).
