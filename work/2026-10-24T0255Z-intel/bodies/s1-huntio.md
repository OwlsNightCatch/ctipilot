---
title: Hunting Leaked PHP2Shell RCE Across Open Directories (CVE-2026-109618, CVE-2026-109619)
url: https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories
hostname: hunt.io
description: Two critical PHP RCE flaws, CVE-2026-109618 and CVE-2026-109619, leaked pre-patch. We map the exposed PHP footprint and hunt open directories for exploitation.
sitename: Hunt Intelligence
date: "2026-10-21"
fingerprint: b718a99be8213682
---
# Hunting Leaked PHP2Shell RCE Across Open Directories (CVE-2026-109618, CVE-2026-109619)

Published on

Two critical PHP remote code execution bugs, [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/cve-2026-109618) and [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/cve-2026-109619), both rated CVSS v4.0 9.2, leaked before their scheduled patch on October 21, 2026 at 14:00 UTC.

A large share of the web runs on PHP, so the exposed surface is big. And attackers wasted no time: php2shell scanning hit our honeypots about 20 minutes after the patch shipped. What we haven’t seen yet is a successful exploit.

So far, we’ve seen attempts and staged tooling, but no confirmed compromises, and no vendors have reported any. Below we map how much PHP is exposed, why a version number in a header is a weak way to judge real risk, and what turned up in attacker open directories through [AttackCapture](https://hunt.io/features/attackcapture).

## What happened

On October 20 the PHP security team put out an [advance notice](https://www.php.net/archive/2026.php): an emergency release coming, two critical bugs, no technical detail, patch set for October 21 at 14:00 UTC. They kept the option to ship sooner if the details got out or exploitation turned up.

The details leaked. Over October 20 and 21 the two CVEs and a nickname, "php2shell", started circulating, and several researchers confirmed the bugs are real:

- watchTowr was first to confirm the leak was genuine and [says](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/) it reproduced both bugs.
- Huntress (John Hammond) put out a [rapid-response writeup](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities).
- [Sansec](https://sansec.io/research/php2shell), [The Hacker News](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html), [SecurityWeek](https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/), and [Patchstack](https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/) all covered the leak.
- CERT-EU issued advisory 2026-018.

PHP [shipped](https://www.php.net/ChangeLog-8.php) the fix on October 21 at about 14:00 UTC in 8.5.12, 8.4.27, 8.3.36 and 8.2.35. End-of-life branches get no upstream release, though distro security teams and backport repos cover most older versions.

The scramble was real even without a confirmed compromise. Oh Dear's uptime monitoring [recorded](https://ma.ttias.be/php-land-last-24-hours/) 18.8% of the sites it watches going offline at the peak, against 0.9% a week earlier, as operators pulled their own sites down rather than wait to get hit.

## The flaws: what the advisory confirms

What is confirmed:

- Two CVEs, CVE-2026-109618 and CVE-2026-109619, both critical at CVSS v4.0 9.2.
- Both are remote code execution in the PHP interpreter itself, not in a plugin or framework on top of it.
- Fixed in PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35.

The root cause is confirmed. In PHP's advisory (GHSA-w8hw-w9fx-j79w, CVE-2026-109618), this is remote code execution via out-of-memory corruption in PHP core. When an allocation fails mid-request, PHP's old OOM path used longjmp() to bail out of the current context without accounting for memory that was only partially initialized, and request shutdown then reads or branches on that invalid state. [php.net](http://php.net) describes both fixes under Core as "avoid state corruption via bailout," and the patch removes the longjmp OOM path.

The entry point is multipart/form-data parsing: an attacker crafts requests that exhaust memory on purpose (no usable content length, unrestricted headers per part, empty file controls that still allocate), which is why the attempts we log carry oversized multipart bodies and leave a burst of "Allowed memory size exhausted" errors in PHP-FPM. One common trigger is session.upload\_progress, on by default since PHP 5.4, so turning it off is a useful stopgap, though the advisory frames the bug as the OOM-bailout handling rather than that one feature. Either way it is reachable without authentication on a default install, since PHP parses request data before your application code runs.

Worth keeping in mind through the rest of this: reaching memory corruption is not the same as getting code execution. That gap is the story.

Figure 01. PHP2Shell at a glance: two critical PHP core remote code execution flaws, CVE-2026-109618 and CVE-2026-109619, both rated CVSS v4.0 9.2, with the exposed PHP footprint measured from Hunt.io scan data.
## Scope of exposure

To get a sense of how much PHP is exposed, we pulled Hunt.io's current scan state for every internet-facing IP whose HTTP headers show PHP or a PHP framework signal. The query runs against ip.current in [HuntSQL](https://hunt.io/features/hunt-sql), which keeps the latest observation per IP instead of a single day's crawl:

```
SELECT ip
FROM ip.current
WHERE http.headers.raw LIKE '%PHP%'
   OR http.headers.raw LIKE '%wp-json%'
   OR http.headers.raw LIKE '%laravel_session%'
   OR http.headers.raw LIKE '%19 Nov 1981%'
```
                Copy
As of October 22, 2026 that returned 3,189,999 unique IPs exposing PHP. Of those, 1,665,351 report a version in a header (X-Powered-By or Server), and 1,524,653 are detected by another PHP signal (a PHPSESSID or laravel\_session cookie, a WordPress wp-json link, or PHP's default Expires: 19 Nov 1981 header) without showing a version. Read these as a floor, not a full count: hosts with expose\_php off and no other PHP tell never show up, so the real footprint is larger. These are unique IPs, not services, so one IP hosting many sites still counts once.

To break it down by branch, count IPs per version prefix. ip.current does not take GROUP BY, so run one filter per branch:

```
SELECT ip FROM ip.current WHERE http.headers.raw LIKE '%PHP/7.4%'
SELECT ip FROM ip.current WHERE http.headers.raw LIKE '%PHP/8.3%'
-- one per branch, etc.
```
                Copy
Top exposed branches by unique IP, current snapshot (head of a long tail, so these do not add up to the total):

| PHP branch | Unique IPs | Status | 
|---|---|---|
| 7.4 | 300,930 | End of life | 
| 8.3 | 175,276 | Supported | 
| 7.2 | 172,114 | End of life | 
| 8.2 | 159,701 | Supported | 
| 5.4 | 150,086 | End of life | 
| 5.6 | 141,147 | End of life | 
| 7.3 | 90,259 | End of life | 
| 5.3 | 74,565 | End of life | 
| 8.0 | 71,753 | End of life | 
| 8.4 | 65,250 | Supported | 

A few things stand out. End-of-life branches dominate: 7.x, 5.x and 4.x together are about 1.1 million IPs that get no upstream fix at all, and the unsupported 8.0 and 8.1 add roughly 127k more. Supported branches show up too, with 8.3 second overall and 8.2 close behind, so hosts that were up to date were still exposed during the pre-patch window, same as the old ones. Even fully patched systems were exposed before the fix shipped on the 21st.

Figure 03. Exposed PHP branches by unique IP, Hunt.io current snapshot (October 22, 2026). End-of-life branches dominate the top of the list, with supported 8.3 and 8.2 in the mix too.
### A caveat that matters

A version string in a header tells you what the software claims to be, not whether it is actually vulnerable. Linux distributions patch bugs and leave the upstream version number untouched all the time, so a host reporting an "old" PHP build may already be fixed. Any count built purely on version strings will run high. We call it out because these exposure numbers get passed around without that context, and they shouldn't be.

## Exploitation in the wild: attempted, not achieved

This is the part to get right. As of October 21, 2026 at 23:45 UTC, we see live php2shell attempts and plenty of tooling being staged, but no successful in-the-wild compromise, and no vendor has confirmed one. It comes down to four things:

- Attempts began quickly but have stayed low-volume. Scanning started about 20 minutes after the 14:00 UTC patch. Our honeypots have logged two php2shell requests, both from a single IP that has already rotated its user-agent.
- Tooling is ahead of results. About ten attacker workspaces in AttackCapture hold php2shell tooling. None holds a victim list, a shell, or stolen data from it.
- The only mass-exploitation operator we found ran ten passes against up to 123 servers and logged zero shells.
- The exploit is hard to land. Code execution on a real site needs a second weakness or a server without address-space randomization. VulnCheck found no public PoC that clears that bar on x86-64, and the researchers who tore the public code apart say the same: Justin Elze ([@HackingLZ](https://x.com/HackingLZ/status/2113054904436601007)) reviewed all 30 public GitHub repos and found nothing that works against a real target, Marcus Hutchins ([@MalwareTechBlog](https://x.com/MalwareTechBlog/status/2113047467357048903)) points out the RCE needs ASLR-protected memory addresses, and [@an0n\_r0](https://x.com/an0n_r0/status/2113198375415710160) notes the one credible PoC is stuck on an unrealistic single-worker PHP-FPM setup.

### Who is scanning

The php2shell traffic we see comes from an established Mirai-style IoT botnet that has been around since at least May 2026 and just added php2shell to its spreading kit. Its scanner, 45.198.224\[.\]169, shares a network (VPSVAULT, AS215925) and scanning fingerprint with hosts that have served the botnet's [C2 infrastructure](https://hunt.io/features/c2-infrastructure). At 20:36 UTC on the 21st it came back with a new user-agent, php2shell-109618.

### What is sitting in the open directories

AttackCapture pulls in attacker staging servers left exposed on the internet and lets us [search inside the files](https://hunt.io/blog/introducing-code-search-on-attackcapture-uncover-exploit-code-reverse-shells-c2-configs-and-more). Pulling the php2shell tooling out of everything else is a one-line query: a [Code Search for php2shell](https://portal.hunt.io/attackcapture/code-search?q=php2shell&run=true), or for either CVE ID, surfaces the staged scripts directly.

[Code Search for php2shell](https://portal.hunt.io/attackcapture/code-search?q=php2shell&run=true)across the captured open directories returns 146 matching files, here probe\_rfc1867.py and verify\_fixation.py with CVE-2026-109619 and the session.upload\_progress trigger sitting right in the code. Searching the CVE IDs directly works the same way.

About ten of those [open directories](https://hunt.io/glossary/open-directories) hold php2shell tooling right now. Grouped by what they actually are:

| Tier | Hosts | What it is | Result | 
|---|---|---|---|
| Custom tooling | 102.210.149\[.\]166 | Hand-written scripts plus WordPress plugin bugs, \~3.3K-site target list | Own scan results empty. Pivoted to an AVideo SQL injection that did yield account data. Idle since 16:05 UTC | 
| Custom tooling | 122.10.110\[.\]72, 122.10.17\[.\]49 | One operator, shared directory, php2shell project inside a broad workspace | Lab only, no php2shell victims in either http.log | 
| Custom tooling | 58.221.60\[.\]160:8000 | Chinese-commented probe scripts (probe\_rfc1867.py, verify\_fixation.py) that detect session.upload\_progress exposure and verify session fixation, plus X-Powered-By version scanners and target lists | Surface scanning only, no shells or php2shell victims (seen 2026-10-22) | 
| Mass exploitation | 206.188.197\[.\]105 (BL Networks, AS399629, NL) | Mass-exploit tool routed through a \~97-proxy farm, 10 runs 19:11 to 20:23 UTC, list grown from 23 to 123 servers | No code execution or shell logged, callback listener caught only internet scanners | 
| Public PoC reuse | 41.223.30\[.\]7, 157.230.117\[.\]70 | Same public tool, identical file hashes | Tooling only | 
| Public PoC reuse | 104.219.251\[.\]31 | Different public PoC repo plus defender WAF rules | Research / defensive | 
| Public PoC reuse | 107.150.31\[.\]151 | PoC held before the patch, WHMCS named | No results | 
| Targeted assessment | 217.160.132\[.\]82 | Pentest-style write-up against a hosting provider, dated 21 Oct, lists php2shell among risks checked | Judged not exploitable there | 
| Research / labs | 47.100.125\[.\]108, 54.169.109\[.\]7, 139.162.165\[.\]136 | Test setups and harnesses | None | 

[Public PoC reuse and staged webshells on 104.219.251\[.\]31:8123](https://portal.hunt.io/attackcapture/filemanager?host=http://104.219.251.31:8123)in AttackCapture. The workspace holds a cloned php2shell PoC plus ready-to-drop PHP backdoors (shell.php pulling from maste.mangsud\[.\]org, autologin\_fd.php, the tebaran\_\* CMS deployers). No php2shell victim was recorded on this host.

The only real compromises in any of these directories have nothing to do with php2shell: account data taken from an AVideo install by SQL injection (102.210.149\[.\]166), and one third-party server calling back to the 122.10.x operator after a Java attack. We keep those separate on purpose. Staging a php2shell tool is not the same as landing it, and we are not going to blur the two.

### What they are aiming at

Operators are pointing php2shell at commerce, billing, and general web hosting, with a clear preference for servers on old PHP that will never be patched. Neither target set we recovered shows a successful compromise.

The ranked list on 102.210.149\[.\]166 narrowed roughly 13.3K candidate hosts down to \~3.3K live sites, then ranked them by PHP version and the data each holds:

| Platform | Sites | Top-priority | Data at risk | 
|---|---|---|---|
| WooCommerce | \~3K | 0 | Customers, orders | 
| WHMCS | 251 | 25 | Customers, billing, support tickets | 
| Magento | 131 | 31 | Customers, orders, admin | 

Their own notes say no attack chain against these sites was verified. The top-priority 56 sites run PHP 5.x to 8.1, branches PHP itself no longer supports. A fix is still reachable for most of them though: distro security teams and backport repos like packages.sury.org and ppa:ondrej/php ship patched builds back to 5.6, usually without changing the version string. The real exposure is operators who never apply those updates, not an absence of a fix. Geography skews to the US (\~1.8K), then Germany (277), Singapore (250) and the UK (202). The operator even logged 151 sites that rejected the exploit request outright with HTTP 403, 405 or 406.

[The mass-exploitation server on 206.188.197\[.\]105](https://portal.hunt.io/attackcapture/filemanager?host=http://206.188.197.105:9999) hit 123 servers across cloud, shared-hosting and ISP networks. About 57 run PHP, many on unsupported 5.x to 7.x. Ten rejected the request outright, including three of the five sitting behind Cloudflare. None was exploited.

## What to do right now

1. Patch now. The fix is out: PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35. On managed hosting, confirm your provider's timeline today.
2. If you cannot patch immediately, put a WAF in front of it. Cloudflare switched on managed WAF rules for php2shell across all plans, including Free, at 03:02 UTC on October 21; in our data they block some attempts but not all, so treat the WAF as a layer that buys time, not a fix. Patching is the fix that actually closes it.
3. Inventory your PHP. Know every host and what it runs. Anything on 7.x or older is not getting a fix, so plan the upgrade.
4. Hunt for the attempt signatures in the indicators below, especially the php2shell user-agent, multipart posts carrying PHP\_SESSION\_UPLOAD\_PROGRESS with an oversized body, and bursts of "Allowed memory size exhausted" in PHP-FPM logs. Those show you were targeted, not that you were compromised.

## IOCs and network observables

Network, request, and log indicators tied to the activity above. Everything here is attempt and staging infrastructure, not evidence of a successful php2shell compromise.

| Use | Indicator | Context | 
|---|---|---|
| Block | 45.198.224\[.\]0/24 | Scanner network, AS215925 | 
| Block | 85.11.167\[.\]243 | Second scanner (peer reporting) | 
| Block | 92.118.112\[.\]100 | Payload host | 
| Block | 89.32.41\[.\]16, 89.32.41\[.\]50, 45.198.224\[.\]88 | Botnet binary hosts | 
| Block | \*.botlesscucks\[.\]st, \*.godofthunder\[.\]st, \*.gettingheadfromduckysmom\[.\]st | Botnet C2 domains | 
| Detect | User-agent containing php2shell | Seen as php2shell-scan/109618 and php2shell-109618 | 
| Detect | JA4H po11cn050000\_0a87faf13e54\_fe81d65a9ab0\_0b5a6e5841d5 | Scanner fingerprint (peer reporting) | 
| Detect | Multipart POST with a PHP\_SESSION\_UPLOAD\_PROGRESS field and an unusually large body | Exploit request pattern | 
| Detect | A burst of "Allowed memory size exhausted" errors in PHP-FPM from 21 Oct on | Server-side trace of an attempt, not of compromise | 
| Watch | 91.90.123\[.\]25, user-agent php2shell-verify/1.0 | Likely research checker (Belgium) | 

Staging-only operator and reuse hosts referenced above: 102.210.149\[.\]166, 122.10.110\[.\]72, 122.10.17\[.\]49, 58.221.60\[.\]160, 206.188.197\[.\]105, 41.223.30\[.\]7, 157.230.117\[.\]70, 104.219.251\[.\]31, 107.150.31\[.\]151, 217.160.132\[.\]82, 47.100.125\[.\]108, 54.169.109\[.\]7, 139.162.165\[.\]136.

## Summary

The leak squeezed the usual patch window down to almost nothing. php2shell details were public on October 20, the fix landed around 14:00 UTC on the 21st, and scanning started roughly 20 minutes after that. The interest is real: an established IoT botnet bolted php2shell onto its spreading kit, and at least ten workspaces are holding tooling, one of them spraying 123 servers through a proxy network.

The part that matters is what has not happened. We have not confirmed any successful exploitation. The bugs get you memory corruption, but turning that into code execution on a live server needs a second weakness or a host without address randomization, and no public tool clears that on x86-64 right now. Big exposure, clear intent, no confirmed working mass exploit yet. That is the window to patch and watch for the attempt signatures, instead of waiting for a working exploit to decide for you. We are watching, and if a real compromise shows up in our data we will say so.

**Hunt.io watches this kind of infrastructure as it goes up, the exposed tooling and the servers staging it, so you catch something like php2shell while it is still being built instead of after it has hit you. If you want to run these hunts against your own environment, [book a demo](https://hunt.io/demo).**

Two critical PHP remote code execution bugs, [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/cve-2026-109618) and [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/cve-2026-109619), both rated CVSS v4.0 9.2, leaked before their scheduled patch on October 21, 2026 at 14:00 UTC.

A large share of the web runs on PHP, so the exposed surface is big. And attackers wasted no time: php2shell scanning hit our honeypots about 20 minutes after the patch shipped. What we haven’t seen yet is a successful exploit.

So far, we’ve seen attempts and staged tooling, but no confirmed compromises, and no vendors have reported any. Below we map how much PHP is exposed, why a version number in a header is a weak way to judge real risk, and what turned up in attacker open directories through [AttackCapture](https://hunt.io/features/attackcapture).

## What happened

On October 20 the PHP security team put out an [advance notice](https://www.php.net/archive/2026.php): an emergency release coming, two critical bugs, no technical detail, patch set for October 21 at 14:00 UTC. They kept the option to ship sooner if the details got out or exploitation turned up.

The details leaked. Over October 20 and 21 the two CVEs and a nickname, "php2shell", started circulating, and several researchers confirmed the bugs are real:

- watchTowr was first to confirm the leak was genuine and [says](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/) it reproduced both bugs.
- Huntress (John Hammond) put out a [rapid-response writeup](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities).
- [Sansec](https://sansec.io/research/php2shell), [The Hacker News](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html), [SecurityWeek](https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/), and [Patchstack](https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/) all covered the leak.
- CERT-EU issued advisory 2026-018.

PHP [shipped](https://www.php.net/ChangeLog-8.php) the fix on October 21 at about 14:00 UTC in 8.5.12, 8.4.27, 8.3.36 and 8.2.35. End-of-life branches get no upstream release, though distro security teams and backport repos cover most older versions.

The scramble was real even without a confirmed compromise. Oh Dear's uptime monitoring [recorded](https://ma.ttias.be/php-land-last-24-hours/) 18.8% of the sites it watches going offline at the peak, against 0.9% a week earlier, as operators pulled their own sites down rather than wait to get hit.

## The flaws: what the advisory confirms

What is confirmed:

- Two CVEs, CVE-2026-109618 and CVE-2026-109619, both critical at CVSS v4.0 9.2.
- Both are remote code execution in the PHP interpreter itself, not in a plugin or framework on top of it.
- Fixed in PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35.

The root cause is confirmed. In PHP's advisory (GHSA-w8hw-w9fx-j79w, CVE-2026-109618), this is remote code execution via out-of-memory corruption in PHP core. When an allocation fails mid-request, PHP's old OOM path used longjmp() to bail out of the current context without accounting for memory that was only partially initialized, and request shutdown then reads or branches on that invalid state. [php.net](http://php.net) describes both fixes under Core as "avoid state corruption via bailout," and the patch removes the longjmp OOM path.

The entry point is multipart/form-data parsing: an attacker crafts requests that exhaust memory on purpose (no usable content length, unrestricted headers per part, empty file controls that still allocate), which is why the attempts we log carry oversized multipart bodies and leave a burst of "Allowed memory size exhausted" errors in PHP-FPM. One common trigger is session.upload\_progress, on by default since PHP 5.4, so turning it off is a useful stopgap, though the advisory frames the bug as the OOM-bailout handling rather than that one feature. Either way it is reachable without authentication on a default install, since PHP parses request data before your application code runs.

Worth keeping in mind through the rest of this: reaching memory corruption is not the same as getting code execution. That gap is the story.

Figure 01. PHP2Shell at a glance: two critical PHP core remote code execution flaws, CVE-2026-109618 and CVE-2026-109619, both rated CVSS v4.0 9.2, with the exposed PHP footprint measured from Hunt.io scan data.
## Scope of exposure

To get a sense of how much PHP is exposed, we pulled Hunt.io's current scan state for every internet-facing IP whose HTTP headers show PHP or a PHP framework signal. The query runs against ip.current in [HuntSQL](https://hunt.io/features/hunt-sql), which keeps the latest observation per IP instead of a single day's crawl:

```
SELECT ip
FROM ip.current
WHERE http.headers.raw LIKE '%PHP%'
   OR http.headers.raw LIKE '%wp-json%'
   OR http.headers.raw LIKE '%laravel_session%'
   OR http.headers.raw LIKE '%19 Nov 1981%'
```
                Copy
As of October 22, 2026 that returned 3,189,999 unique IPs exposing PHP. Of those, 1,665,351 report a version in a header (X-Powered-By or Server), and 1,524,653 are detected by another PHP signal (a PHPSESSID or laravel\_session cookie, a WordPress wp-json link, or PHP's default Expires: 19 Nov 1981 header) without showing a version. Read these as a floor, not a full count: hosts with expose\_php off and no other PHP tell never show up, so the real footprint is larger. These are unique IPs, not services, so one IP hosting many sites still counts once.

To break it down by branch, count IPs per version prefix. ip.current does not take GROUP BY, so run one filter per branch:

```
SELECT ip FROM ip.current WHERE http.headers.raw LIKE '%PHP/7.4%'
SELECT ip FROM ip.current WHERE http.headers.raw LIKE '%PHP/8.3%'
-- one per branch, etc.
```
                Copy
Top exposed branches by unique IP, current snapshot (head of a long tail, so these do not add up to the total):

| PHP branch | Unique IPs | Status | 
|---|---|---|
| 7.4 | 300,930 | End of life | 
| 8.3 | 175,276 | Supported | 
| 7.2 | 172,114 | End of life | 
| 8.2 | 159,701 | Supported | 
| 5.4 | 150,086 | End of life | 
| 5.6 | 141,147 | End of life | 
| 7.3 | 90,259 | End of life | 
| 5.3 | 74,565 | End of life | 
| 8.0 | 71,753 | End of life | 
| 8.4 | 65,250 | Supported | 

A few things stand out. End-of-life branches dominate: 7.x, 5.x and 4.x together are about 1.1 million IPs that get no upstream fix at all, and the unsupported 8.0 and 8.1 add roughly 127k more. Supported branches show up too, with 8.3 second overall and 8.2 close behind, so hosts that were up to date were still exposed during the pre-patch window, same as the old ones. Even fully patched systems were exposed before the fix shipped on the 21st.

Figure 03. Exposed PHP branches by unique IP, Hunt.io current snapshot (October 22, 2026). End-of-life branches dominate the top of the list, with supported 8.3 and 8.2 in the mix too.
### A caveat that matters

A version string in a header tells you what the software claims to be, not whether it is actually vulnerable. Linux distributions patch bugs and leave the upstream version number untouched all the time, so a host reporting an "old" PHP build may already be fixed. Any count built purely on version strings will run high. We call it out because these exposure numbers get passed around without that context, and they shouldn't be.

## Exploitation in the wild: attempted, not achieved

This is the part to get right. As of October 21, 2026 at 23:45 UTC, we see live php2shell attempts and plenty of tooling being staged, but no successful in-the-wild compromise, and no vendor has confirmed one. It comes down to four things:

- Attempts began quickly but have stayed low-volume. Scanning started about 20 minutes after the 14:00 UTC patch. Our honeypots have logged two php2shell requests, both from a single IP that has already rotated its user-agent.
- Tooling is ahead of results. About ten attacker workspaces in AttackCapture hold php2shell tooling. None holds a victim list, a shell, or stolen data from it.
- The only mass-exploitation operator we found ran ten passes against up to 123 servers and logged zero shells.
- The exploit is hard to land. Code execution on a real site needs a second weakness or a server without address-space randomization. VulnCheck found no public PoC that clears that bar on x86-64, and the researchers who tore the public code apart say the same: Justin Elze ([@HackingLZ](https://x.com/HackingLZ/status/2113054904436601007)) reviewed all 30 public GitHub repos and found nothing that works against a real target, Marcus Hutchins ([@MalwareTechBlog](https://x.com/MalwareTechBlog/status/2113047467357048903)) points out the RCE needs ASLR-protected memory addresses, and [@an0n\_r0](https://x.com/an0n_r0/status/2113198375415710160) notes the one credible PoC is stuck on an unrealistic single-worker PHP-FPM setup.

### Who is scanning

The php2shell traffic we see comes from an established Mirai-style IoT botnet that has been around since at least May 2026 and just added php2shell to its spreading kit. Its scanner, 45.198.224\[.\]169, shares a network (VPSVAULT, AS215925) and scanning fingerprint with hosts that have served the botnet's [C2 infrastructure](https://hunt.io/features/c2-infrastructure). At 20:36 UTC on the 21st it came back with a new user-agent, php2shell-109618.

### What is sitting in the open directories

AttackCapture pulls in attacker staging servers left exposed on the internet and lets us [search inside the files](https://hunt.io/blog/introducing-code-search-on-attackcapture-uncover-exploit-code-reverse-shells-c2-configs-and-more). Pulling the php2shell tooling out of everything else is a one-line query: a [Code Search for php2shell](https://portal.hunt.io/attackcapture/code-search?q=php2shell&run=true), or for either CVE ID, surfaces the staged scripts directly.

[Code Search for php2shell](https://portal.hunt.io/attackcapture/code-search?q=php2shell&run=true)across the captured open directories returns 146 matching files, here probe\_rfc1867.py and verify\_fixation.py with CVE-2026-109619 and the session.upload\_progress trigger sitting right in the code. Searching the CVE IDs directly works the same way.

About ten of those [open directories](https://hunt.io/glossary/open-directories) hold php2shell tooling right now. Grouped by what they actually are:

| Tier | Hosts | What it is | Result | 
|---|---|---|---|
| Custom tooling | 102.210.149\[.\]166 | Hand-written scripts plus WordPress plugin bugs, \~3.3K-site target list | Own scan results empty. Pivoted to an AVideo SQL injection that did yield account data. Idle since 16:05 UTC | 
| Custom tooling | 122.10.110\[.\]72, 122.10.17\[.\]49 | One operator, shared directory, php2shell project inside a broad workspace | Lab only, no php2shell victims in either http.log | 
| Custom tooling | 58.221.60\[.\]160:8000 | Chinese-commented probe scripts (probe\_rfc1867.py, verify\_fixation.py) that detect session.upload\_progress exposure and verify session fixation, plus X-Powered-By version scanners and target lists | Surface scanning only, no shells or php2shell victims (seen 2026-10-22) | 
| Mass exploitation | 206.188.197\[.\]105 (BL Networks, AS399629, NL) | Mass-exploit tool routed through a \~97-proxy farm, 10 runs 19:11 to 20:23 UTC, list grown from 23 to 123 servers | No code execution or shell logged, callback listener caught only internet scanners | 
| Public PoC reuse | 41.223.30\[.\]7, 157.230.117\[.\]70 | Same public tool, identical file hashes | Tooling only | 
| Public PoC reuse | 104.219.251\[.\]31 | Different public PoC repo plus defender WAF rules | Research / defensive | 
| Public PoC reuse | 107.150.31\[.\]151 | PoC held before the patch, WHMCS named | No results | 
| Targeted assessment | 217.160.132\[.\]82 | Pentest-style write-up against a hosting provider, dated 21 Oct, lists php2shell among risks checked | Judged not exploitable there | 
| Research / labs | 47.100.125\[.\]108, 54.169.109\[.\]7, 139.162.165\[.\]136 | Test setups and harnesses | None | 

[Public PoC reuse and staged webshells on 104.219.251\[.\]31:8123](https://portal.hunt.io/attackcapture/filemanager?host=http://104.219.251.31:8123)in AttackCapture. The workspace holds a cloned php2shell PoC plus ready-to-drop PHP backdoors (shell.php pulling from maste.mangsud\[.\]org, autologin\_fd.php, the tebaran\_\* CMS deployers). No php2shell victim was recorded on this host.

The only real compromises in any of these directories have nothing to do with php2shell: account data taken from an AVideo install by SQL injection (102.210.149\[.\]166), and one third-party server calling back to the 122.10.x operator after a Java attack. We keep those separate on purpose. Staging a php2shell tool is not the same as landing it, and we are not going to blur the two.

### What they are aiming at

Operators are pointing php2shell at commerce, billing, and general web hosting, with a clear preference for servers on old PHP that will never be patched. Neither target set we recovered shows a successful compromise.

The ranked list on 102.210.149\[.\]166 narrowed roughly 13.3K candidate hosts down to \~3.3K live sites, then ranked them by PHP version and the data each holds:

| Platform | Sites | Top-priority | Data at risk | 
|---|---|---|---|
| WooCommerce | \~3K | 0 | Customers, orders | 
| WHMCS | 251 | 25 | Customers, billing, support tickets | 
| Magento | 131 | 31 | Customers, orders, admin | 

Their own notes say no attack chain against these sites was verified. The top-priority 56 sites run PHP 5.x to 8.1, branches PHP itself no longer supports. A fix is still reachable for most of them though: distro security teams and backport repos like packages.sury.org and ppa:ondrej/php ship patched builds back to 5.6, usually without changing the version string. The real exposure is operators who never apply those updates, not an absence of a fix. Geography skews to the US (\~1.8K), then Germany (277), Singapore (250) and the UK (202). The operator even logged 151 sites that rejected the exploit request outright with HTTP 403, 405 or 406.

[The mass-exploitation server on 206.188.197\[.\]105](https://portal.hunt.io/attackcapture/filemanager?host=http://206.188.197.105:9999) hit 123 servers across cloud, shared-hosting and ISP networks. About 57 run PHP, many on unsupported 5.x to 7.x. Ten rejected the request outright, including three of the five sitting behind Cloudflare. None was exploited.

## What to do right now

1. Patch now. The fix is out: PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35. On managed hosting, confirm your provider's timeline today.
2. If you cannot patch immediately, put a WAF in front of it. Cloudflare switched on managed WAF rules for php2shell across all plans, including Free, at 03:02 UTC on October 21; in our data they block some attempts but not all, so treat the WAF as a layer that buys time, not a fix. Patching is the fix that actually closes it.
3. Inventory your PHP. Know every host and what it runs. Anything on 7.x or older is not getting a fix, so plan the upgrade.
4. Hunt for the attempt signatures in the indicators below, especially the php2shell user-agent, multipart posts carrying PHP\_SESSION\_UPLOAD\_PROGRESS with an oversized body, and bursts of "Allowed memory size exhausted" in PHP-FPM logs. Those show you were targeted, not that you were compromised.

## IOCs and network observables

Network, request, and log indicators tied to the activity above. Everything here is attempt and staging infrastructure, not evidence of a successful php2shell compromise.

| Use | Indicator | Context | 
|---|---|---|
| Block | 45.198.224\[.\]0/24 | Scanner network, AS215925 | 
| Block | 85.11.167\[.\]243 | Second scanner (peer reporting) | 
| Block | 92.118.112\[.\]100 | Payload host | 
| Block | 89.32.41\[.\]16, 89.32.41\[.\]50, 45.198.224\[.\]88 | Botnet binary hosts | 
| Block | \*.botlesscucks\[.\]st, \*.godofthunder\[.\]st, \*.gettingheadfromduckysmom\[.\]st | Botnet C2 domains | 
| Detect | User-agent containing php2shell | Seen as php2shell-scan/109618 and php2shell-109618 | 
| Detect | JA4H po11cn050000\_0a87faf13e54\_fe81d65a9ab0\_0b5a6e5841d5 | Scanner fingerprint (peer reporting) | 
| Detect | Multipart POST with a PHP\_SESSION\_UPLOAD\_PROGRESS field and an unusually large body | Exploit request pattern | 
| Detect | A burst of "Allowed memory size exhausted" errors in PHP-FPM from 21 Oct on | Server-side trace of an attempt, not of compromise | 
| Watch | 91.90.123\[.\]25, user-agent php2shell-verify/1.0 | Likely research checker (Belgium) | 

Staging-only operator and reuse hosts referenced above: 102.210.149\[.\]166, 122.10.110\[.\]72, 122.10.17\[.\]49, 58.221.60\[.\]160, 206.188.197\[.\]105, 41.223.30\[.\]7, 157.230.117\[.\]70, 104.219.251\[.\]31, 107.150.31\[.\]151, 217.160.132\[.\]82, 47.100.125\[.\]108, 54.169.109\[.\]7, 139.162.165\[.\]136.

## Summary

The leak squeezed the usual patch window down to almost nothing. php2shell details were public on October 20, the fix landed around 14:00 UTC on the 21st, and scanning started roughly 20 minutes after that. The interest is real: an established IoT botnet bolted php2shell onto its spreading kit, and at least ten workspaces are holding tooling, one of them spraying 123 servers through a proxy network.

The part that matters is what has not happened. We have not confirmed any successful exploitation. The bugs get you memory corruption, but turning that into code execution on a live server needs a second weakness or a host without address randomization, and no public tool clears that on x86-64 right now. Big exposure, clear intent, no confirmed working mass exploit yet. That is the window to patch and watch for the attempt signatures, instead of waiting for a working exploit to decide for you. We are watching, and if a real compromise shows up in our data we will say so.

**Hunt.io watches this kind of infrastructure as it goes up, the exposed tooling and the servers staging it, so you catch something like php2shell while it is still being built instead of after it has hit you. If you want to run these hunts against your own environment, [book a demo](https://hunt.io/demo).**

Related Posts

Related Posts

Related Posts
