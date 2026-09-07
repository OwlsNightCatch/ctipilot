# extract: served via trafilatura-direct
---
title: New Ted Backdoor Hides Inside Victims' Own HAProxy Builds to Intercept Web Traffic
author: The Hacker News
url: https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html
hostname: thehackernews.com
description: Ted hides inside trojanized HAProxy builds to intercept traffic and serve altered pages at two South Korean organizations.
sitename: The Hacker News
date: "2026-09-04"
categories: ['Article']
---
A previously undocumented Linux toolkit has been found compiled directly into the trojanized **HAProxy** load balancers of two South Korean organizations, where it intercepted web traffic and served altered pages to selected visitors.

The attackers named the implant **ted** in debug strings left in the binary. It is not a HAProxy vulnerability, and installing it requires code execution on the host and the ability to replace the running binary.

Rapid7 Labs attributed the toolkit with medium confidence to North Korean state-sponsored actors and put the two victims in South Korea's automotive and media sectors.

Command-and-control (C2) requests never reach a backend server and are erased from HAProxy's own connection counters, so neither the backend logs nor the load balancer's statistics record them.

"Further evidence is necessary to make a more definitive assessment," Rapid7 said.

A request for one specific image path puts the filter into C2 mode, Rapid7 said in [a report published Friday](https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/). The implant decrements HAProxy's live connection counters, thereby dropping the connection from the load balancer's statistics. It writes the command body to a named pipe under /tmp. Zeroing the request channel afterwards leaves nothing to forward, and the command terminates at the load balancer.

Output returns on the raw socket under a standard HTTP/1.0 200 OK header, which is what makes the exchange look like ordinary web traffic.

Through that channel, the operator can beacon, upload and download files, run shell commands, and replace the implant's configuration. Only requests clearing four checks receive a modified page.

The request has to carry a User-Agent and match a rule whose URL and referer patterns both fit. Delivery then falls to either whitelist membership on the client address, checked exactly and again at the /24 level, or an operator key in the Accept-Language header that overrides the address filtering entirely.


The implant rewrites the content type and length on the way out, forces the response status to 200, and deletes the Accept-Ranges header so a client cannot request byte ranges and notice the size change.

Rapid7 said its evidence was not enough to establish a timeline or determine how the attackers first got in.

Its hypothesis that they came in through an exposed Groupware portal, a class of Korean enterprise collaboration software, rests on [the ENKI research it points to](https://www.enki.co.kr/en/media-center/blog/analysis-of-kimsuky-s-attack-on-a-south-korean-groupware-vendor-using-a-new-gomir-family-variant). That report documented Kimsuky compromising a groupware vendor through a mail server flaw.

The stager deploys only where HAProxy or cron is already running, and it verifies root before dropping anything. It overwrites the legitimate crond binary and gives the replacement the creation timestamp of /usr/bin/ssh. It then strips the keywords tmp, wget, cron and crond from root's bash history and from six system logs, among them auth.log and audit/audit.log.

A trojanized sshd in the same toolkit encrypts captured plaintext passwords and writes them to a fixed path.

Rapid7 found the same code in trojanized agetty, atd, and polkitd binaries. A companion remote access trojan (RAT) that Rapid7 calls curlRAT beacons every 12 hours by default and drops to a 30-second interval when the operator sets a flag. It aborts unless it finds a marker file showing the host is virtualized.

curlRAT is distinct from CurlBack RAT, [a separate family of that name](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html) attributed to the Pakistan-linked SideCopy group.

Rapid7 shared the following indicators of compromise (IoCs) -

- **Domain** - img.monderhouse[.]space
- **Domain** - img.smartnords[.]site
- **Domain** - img.darklights[.]store
- **Domain** - img.responsive.pstatic[.]autos
- **Domain** - img.socialteams[.]store
- **Domain** - img.worksongo[.]store
- **File** - ~/cache/haproxy-1000.cache
- **File** - /var/lib/sshd/c8c68e629bba773a10ac80012d10bf19
- **File** - /var/lib/snapd/g580
- **File** - /tmp/jasper-log
- **SHA-256** - 72e70936f0dbe459142a1d867617c35f8d0cce5d18c6a49e1090a2a5adc8e558
- **SHA-256** - 4bb923eb040aa13ca8fd409c31ee4729c60ddff32e350efe1c5a4a9168a065f5

The Hacker News confirmed on September 4 that none of the six domains resolves, returning NXDOMAIN, meaning no such name exists, for both A and NS records via Google Public DNS. They are useful for reviewing historical logs rather than for blocking live traffic.

Part of the attribution rests on a listing of those domains under APT37 in maltrail, an open-source detection project. [The maltrail file Rapid7 links](https://github.com/stamparm/maltrail/blob/master/trails/static/malware/apt_37.txt) stopped resolving after [a repository restructure in August](https://github.com/stamparm/maltrail/blob/master/CHANGELOG) moved the project's static trail data elsewhere.

The Hacker News confirmed on September 4 that all six are present at the new location, each labelled as APT37 infrastructure. [maltrail's APT37 source file](https://github.com/stamparm/trails/blob/master/malware/apt_37.txt) credits those entries to two posts on X from July 2025 and carries no reference to Rapid7.

Six further domains sit in the same two maltrail entries but not in Rapid7's list: primgs[.]lol, admin.primgs[.]lol, grip-cdns[.]space, show.grip-cdns[.]space, cleanos[.]online and app.cleanos[.]online. Rapid7 has not said whether they are the same infrastructure.

[The ThreatFox tag](https://threatfox.abuse.ch/browse/tag/RicochetChollima/) Rapid7 names as its second source for the same domains records five sightings, all timestamped July 2, 2025.

One of the two X posts maltrail cites was published three hours earlier that day.

The attribution passage draws on three separate North Korean clusters, APT37 for the domain list, Lazarus for the delivery model, and Kimsuky for the initial-access hypothesis.

[Mandiant's 2023 assessment](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023) of North Korean cyber structure recorded shared tooling and overlapping targeting across those clusters.

"We believe that this will make precise attribution more difficult," Mandiant said.

Rapid7 compared the delivery model to [the Operation SyncHole campaign](https://thehackernews.com/2025/04/lazarus-hits-6-south-korean-firms-via.html), in which visitors to South Korean online media sites were filtered by a server-side script and redirected. Kaspersky researchers Sojun Ryu and Vasily Berdnikov assessed "with medium confidence" that the redirected page may have run a malicious script against a flaw in Cross EX, a South Korean browser helper.

[Kaspersky's SyncHole report](https://securelist.com/operation-synchole-watering-hole-attacks-by-lazarus/116326/) identified at least six victims in the software, IT, financial, semiconductor manufacturing and telecommunications sectors.

Both victims ran HAProxy 2.8.12, released on November 8, 2024 per [HAProxy's own release history](https://www.haproxy.org/bugs/bugs-2.8.12.html). The implant reads HAProxy's internal structures at offsets fixed to that release, and Rapid7 does not say whether other 2.8 builds exist.

The current release on that branch is 2.8.28, from August 27, 2026, 16 point releases later. HAProxy's tracker lists 529 known bugs affecting 2.8.12 that are already fixed in the branch, including 1 critical and 16 major.

Upgrading does not clean a host the implant already sits on, because the attackers replace the binary rather than exploit a flaw in it.

Rapid7 recommended independent network correlation, memory behavioural analysis and binary integrity checks. The report publishes no detection rules for that last check, and a recompiled HAProxy reports the same version string as a clean build.

The development comes as AhnLab and ENKI WhiteHat documented [a similar watering-hole campaign](https://thehackernews.com/2026/07/hackers-exploit-anysign4pc-via-hacked.html) in July, in which state-sponsored operators abused compromised Korean websites to attack the AnySign4PC signing client.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
