---
title: PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches
author: The Hacker News
url: https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
hostname: thehackernews.com
description: PHP warns CVE-2026-115560 may enable code execution in unusual session setups and advises disabling session upload progress pending a routine fix.
sitename: The Hacker News
date: "2026-10-23"
categories: ['Article']
fingerprint: b55c37f3fe8277c2
---
PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws.

The new issue, assigned **CVE-2026-115560**, affects only web applications configured in an unusual way, and PHP considers it an unlikely risk.

The project is not issuing an emergency fix for it. Instead, it recommends turning off a feature called **session upload progress** until a fix is available in the next routine release.

The warning came in a short [informational advisory](https://www.php.net/archive/2026.php#2026-10-23-1) published on October 23. It follows the October 21 [emergency release](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html) that fixed two critical PHP2Shell flaws, **CVE-2026-109618** and **CVE-2026-109619**, which let an attacker without an account run code on a server. Those were patched in PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The new issue is separate and is not fixed by those releases.

Only a narrow setup is at risk. PHP says the problem can occur when a web application does all of the following: sets the **session.serialize\_handler** option to php\_binary or php\_serialize in its configuration, then changes that option to php while running by calling ini\_set(), and makes that change before it calls session\_start().

Session upload progress must also still be turned on. An application that never changes the serialize handler while running can leave the feature on and is not exposed through this path. PHP says this setup is unlikely in practice.

The action is one line. PHP recommends setting **session.upload\_progress.enabled=0** until the next routine bugfix release. This is the same setting it already listed as a mitigation in the October 21 [advisory](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) for CVE-2026-109619.

Anyone who applied it then and left it in place needs to do nothing more for the new issue. Session upload progress is turned on by default and lets an application track the progress of a file upload.

Because the setup is uncommon, PHP is handling the fix as part of its regular release cycle rather than as an emergency, and it will publish a full advisory for CVE-2026-115560 with the next release.

PHP has not stated which versions are affected, which releases will contain the fix, or a severity score. It also has not said whether the new issue shares a root cause with CVE-2026-109619.

No exploitation of CVE-2026-115560 has been reported; the attacks reported since October 21 target the two earlier PHP2Shell flaws.

Separately, attempts to exploit the two earlier PHP2Shell flaws have surged. Amazon said its [honeypots logged an exploit attempt](https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html) against CVE-2026-109618 and CVE-2026-109619 on October 17, four days before the flaws were disclosed, and Cloudflare said attempts [rose from tens of thousands](https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html) within 45 minutes of the October 21 disclosure to millions by early October 22.

Attackers have tried to use the flaws to install a Mirai botnet variant, according to Sophos and Arctic Wolf. Those attempts have so far failed: Previdian, Wordfence and others report scanning and probing but no confirmed code execution, and researchers say a reliable exploit is proving harder to build than expected. That activity targets the two flaws patched on October 21, not CVE-2026-115560, which has not been reported under attack.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
