---
title: Debian nginx Important Buffer Overflow Denial of Service CVE-2026-42533
author: LinuxSecurity com Team
url: https://linuxsecurity.com/advisories/debian/debian-dsa-6496-1-nginx
hostname: linuxsecurity.com
description: Several vulnerabilities in nginx could lead to denial of service, memory leaks, or arbitrary code execution needing updates
sitename: Linux Security
date: "2026-09-12"
tags: ['nginx security', 'Debian DSA', 'buffer overflow', 'memory leak', 'denial of service']
fingerprint: "3bbeab6fef34c492"
language: en
image: https://linuxsecurity.com/images/distros-large/debian-large.png
pagetype: article
filedate: "2026-11-28"
---
Attackers are using AI tools to speed up intrusions. [**Check your defenses**](https://linuxsecurity.com/news/security-trends/ai-penetration-testing-artex-risks)×

CVE-2026-42533

A heap buffer overflow was discovered in the nginx script engine. It

can be triggered when a map directive performs regular expression

matching and a string expression references captures modified by the

map, or when non-cacheable variables change between the script length

pass and the script copy pass.

CVE-2026-56434


Duplicate finalization of an HTTP subrequest can result in a

use-after-free. The issue is observable in configurations using

server-side includes together with proxy\_pass and proxy\_buffering

disabled, when an upstream response causes the same subrequest to be

posted twice.

CVE-2026-60005

ngx\_http\_regex\_exec() could replace the captures array without

clearing r->ncaptures when the new regular expression did not match.

A subsequent unnamed capture could then access uninitialised memory,

resulting in memory disclosure.

For the stable distribution (trixie), these problems have been fixed in

version 1.26.3-3+deb13u8.

W...

Severity

important

Lowest

Low

Medium

High

Critical

Get the latest Linux and open source security news straight to your inbox.
