---
title: "Update Apache httpd to 2.4.71 · Issue #3739 · nextcloud-snap/nextcloud-snap"
author: Stondino
url: https://github.com/nextcloud-snap/nextcloud-snap/issues/3739
hostname: github.com
description: "-*- coding: utf-8 -*- Changes with Apache 2.4.71 *) SECURITY: CVE-2026-119618: mod_http2: heap corruption and RCE in assign_headers (cve.mitre.org) Concurrent Execution using Shared Resource with I..."
sitename: GitHub
date: "2026-11-11"
categories: ['issue:6337713312']
fingerprint: ffc3d6b6ef227e50
---
## Repository navigation

## Description

```
                                                     -*- coding: utf-8 -*-
```
Changes with Apache 2.4.71

\*) SECURITY: [CVE-2026-119618](https://github.com/advisories/GHSA-hjhf-gpg9-qqfj): mod\_http2: heap corruption and RCE in

assign\_headers (cve.mitre.org)

Concurrent Execution using Shared Resource with Improper

Synchronization vulnerability in Apache HTTP Server's mod\_http2

in assign\_headers() can lead to RCE.

This issue affects Apache HTTP Server: from 2.4.55 through

2.4.70.

Affected releases of mod\_h2 from GitHub: from 2.0.8 through

2.0.42.

Credits: Anthropic's OSS Scanner, as vulnerability

ANT-2026-MAPKT6MZ

\*) SECURITY: [CVE-2026-109163](https://github.com/advisories/GHSA-xxrj-387x-fr5v): mod\_vhost\_alias 1 byte stack buffer

overwrite (after [CVE-2026-63292](https://github.com/advisories/GHSA-f6c9-29xf-9j37)) (cve.mitre.org)

Stack-based buffer overflow vulnerability in Apache HTTP

Server's mod\_vhost\_alias (afterÂ [CVE-2026-63292](https://github.com/advisories/GHSA-f6c9-29xf-9j37))

This issue affects Apache HTTP Server: 2.4.69 and 2.4.70.

Credits: Gustavo Aiello

\*) SECURITY: [CVE-2026-106023](https://github.com/advisories/GHSA-h2px-wj5m-vvh4): mod\_md NULL pointer dereference leads

to child process crash (cve.mitre.org)

NULL pointer dereference vulnerability in Apache HTTP Server's

mod\_md during HTTP request processing.

This issue affects Apache HTTP Server: from 2.4.30 through

2.4.70.

Credits: hexb1n, Yang Song, and JiaSheng He of 360 Vulnerability

Research Institute, working with 360 TuLongFeng.

\*) mod\_md: MDHttpProxy and MDCACertificateFile can now be set per MDomain.

New directive MDHttpProxyCACertificateFile sets the CA certificates

used to verify an HTTPS proxy.

\[Michael Kaufmann \]

\*) mod\_deflate: Read the gzip extra-field (FEXTRA) length as unsigned so a

length byte with the high bit set is no longer sign-extended, fixing

inflation of gzip streams that carry an extra field.

\[arshiya tabasum \]

\*) mod\_remoteip: Apply RemoteIP{Trusted,Internal}ProxyList to the virtual host

they are configured in, and merge the proxy entries of the main server

and of the virtual host, logging a warning when both have some.

PR 70207.  \[Arturo Bernal\]

\*) mod\_dav: Fix handling of invalid or overflowing "Timeout:"

request headers, which could silently grant a lock with an

already-expired timeout instead of the RFC 4918 maximum.

PR 65788 \[Arturo Bernal\]

\*) mod\_http2: Correctly handle the asterisk-form of OPTIONS requests

instead of rejecting them as malformed.  PR 70195.

\[Arturo Bernal \]

\*) mod\_http2: Fix duplicate logging of header limit violations.

\[Michael Kaufmann \]

\*) mod\_http2: Fix a crash creating an HTTP/2 session with

"H2PushDiarySize 0" and debug logging enabled.  \[Joe Orton\]

\*) mod\_dav\_lock: Fix dav\_generic\_load\_lock\_record() reading the

indirect-lock key length with the wrong width, which could read

back a wrong length on big-endian platforms. PR 70299

\[Arturo Bernal\]

\*) mod\_remoteip: Log a connection closed before a complete PROXY protocol

header was received at info level rather than as an error.  PR 63893.

\[Joe Orton\]

## Activity

to join this conversation on GitHub.Already have an account? Sign in to comment
