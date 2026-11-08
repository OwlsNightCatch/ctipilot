---
title: Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs
author: The Hacker News
url: https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
hostname: thehackernews.com
description: CWPdoor replaces Control Web Panel's web server after root access, enabling command execution through requests hidden from access logs.
sitename: The Hacker News
date: "2026-11-06"
categories: ['Article']
fingerprint: d5ab1148e490ae43
---
A backdoor has been found hiding in the web server that runs **Control Web Panel** (CWP), a free panel for managing Linux hosting servers, researchers at QiAnXin's XLab said this week.

The backdoored web server executes commands that attackers send via web requests, and those requests never appear in its access logs. Installing it takes root access, so the attackers must already control the server.

The researchers, who named the backdoor **cwpdoor**, captured its installer, a shell script posing as a version update, on June 29. The installer handles only two versions of that web server, cwpsrv 1.15.10 and 1.24.0. The researchers do not yet know how attackers get the root access the installer needs.

On September 30, an archive holding a copy of the backdoor was uploaded to VirusTotal from Brazil. The researchers say this indicates that "real victims already exist in the wild." They give no count of infected servers.

The backdoor is **cwpsrv** itself, rebuilt with extra code, the researchers found in their [technical analysis](https://blog.xlab.qianxin.com/cwpdoor-the-invisible-backdoor-living-inside-control-web-panel/). It behaves like the normal program until a request arrives with a valid timestamp and signature in custom headers whose names begin with X-Ngx-Integrity. It then runs the command carried in the request.

When the installer replaces the cwpsrv file, it puts the file's dates back to their original values, so checks with ls and stat show it as unchanged. When the researchers checked, the backdoor file had zero detections out of 63 on VirusTotal.


### Checking a Server for the Backdoor

XLab gives three checks:

- **Socket:** run `ss -axp | grep integrity`. A result naming `ngx_http_integrity_helper`, the Unix socket the backdoor uses, is a sign of infection.
- **Process:** run `ps aux | grep cwpsrv` and look for unexpected helper processes started by cwpsrv.
- **File:** run `strings /usr/local/cwpsrv/bin/cwpsrv | grep X-Ngx-Integrity` and look for the backdoor's header names.

In the researchers' example, the socket check found the backdoor on a server where the list of open ports looked normal.

The researchers published these indicators:

- **MD5:** `e505d4ffa21cf494a5dc2d7c8f4f1236` (installer script, cwpsrv\_update.sh)
- **MD5:** `965aea67fb40de1bab5169ada993349f` (backdoored cwpsrv 1.15.10)
- **MD5:** `d3f4e95113d49ab3991b45e457bda75b` (backdoored cwpsrv 1.24.0)
- **IP:** `136.0.141[.]71` (download server)
- **URL:** `https://136.0.141[.]71/static/cwpsrv_update.sh`
- **URL:** `https://136.0.141[.]71/static/cwpsrv_1.15.10`
- **URL:** `https://136.0.141[.]71/static/cwpsrv_1.24.0`

### Cleaning Up an Infected Server

If a server is infected, the researchers recommend three steps:

1. Restore the original cwpsrv from the backup the installer creates in `/usr/local/cwpsrv/bin`, with a name starting `cwpsrv.prev-` and ending in a date and time. The researchers' description of the installer says it deletes "the temporary files and backup" after a successful swap, so this copy may be missing.
2. Upgrade to the latest version, then confirm that `ss -axp | grep integrity` returns nothing.
3. Change all control panel credentials, because the backdoor can run any command. Treat the whole server as compromised and check it for other threats.

The archive uploaded from Brazil also held the [Ebury malware](https://thehackernews.com/2024/05/ebury-botnet-malware-compromises-400000.html), an OpenSSH backdoor and credential stealer active since at least 2009. The researchers do not know whether the two are related, and say different attackers may have planted them on the same server.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
