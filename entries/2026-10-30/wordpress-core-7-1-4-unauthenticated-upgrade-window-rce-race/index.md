---
schema: 1
kind: vulnerability
title: "WordPress core 4.7 to 7.1.3: an unauthenticated race in the core update process can lead to remote code execution, fixed in 7.1.4 and backported to every supported branch, with Wordfence reporting exploitation attempts and no CVE assigned in the sources"
headline: "WordPress 7.1.4 fixes an unauthenticated upgrade-window RCE race; Wordfence sees probing, so confirm the auto-update ran"
summary: >
  WordPress 7.1.4 of 2026-10-28 fixes a weakness in the core upgrade process that lets an unauthenticated attacker reach the staged installer and run code on the server
  during a full-package core update, in versions 4.7 to 7.1.3, with backports for every branch down to 4.7. Wordfence reports more than 18,500 probing requests in the first 21 hours,
  while Patchstack calls the race hard to win and says it needs a web-reachable staging directory; no source gives a CVE identifier.
discovered_at: "2026-10-30T03:45:00Z"
updated_at: null
event_date: "2026-10-28"
run_id: 2026-10-30T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: []
entities: ["product:wordpress-core"]
techniques: [T1190]
affected_products: ["WordPress Core"]
cves: []
sources:
  - url: "https://wordpress.org/news/2026/10/wordpress-7-1-4/"
    publisher: "WordPress.org"
    date: "2026-10-28"
    role: primary
  - url: "https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/"
    publisher: "Wordfence"
    date: "2026-10-29"
    role: corroborating
  - url: "https://patchstack.com/articles/wordpress-7-1-4-security-release/"
    publisher: "Patchstack"
    date: "2026-10-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A weakness in the WordPress upgrade process which can lead to remote code execution during the upgrade window"
    publisher: "WordPress.org"
    source_url: "https://wordpress.org/news/2026/10/wordpress-7-1-4/"
  - quote: "During the first 21 hours, we recorded more than 18,500 requests targeting staged `setup-config.php` installer paths."
    publisher: "Wordfence"
    source_url: "https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/"
  - quote: "You have to request the right path at the moment an update runs, which is why we scored it `AC:H` and would not call it practical to exploit."
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/wordpress-7-1-4-security-release/"
verification: multi-source
sourcing_note: >
  WordPress.org is the disclosing party and names the weakness without a CVE identifier; the CVSS 8.1 score is Wordfence's. Wordfence and Patchstack analysed the fix independently and agree on the mechanism, while the exploitation-attempt telemetry is Wordfence's alone and Patchstack rates the race impractical to win.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Confirm in Dashboard > Updates that every WordPress site your organisation, its web agencies or its hosting suppliers run is on 7.1.4 or the fixed release of its branch, and deny web access to wp-content/upgrade/ in the web server configuration of each, because the race can be probed during any full-package core update and a firewall that WordPress itself loads does not run for that request."
updates: []
migrated_from: null
---

WordPress 7.1.4, released on 2026-10-28, fixes a weakness in the upgrade process that can lead to remote code execution during the upgrade window, and backports follow for every branch that receives security fixes, currently through 4.7 ([WordPress.org, 2026-10-28](https://wordpress.org/news/2026/10/wordpress-7-1-4/)); WordPress's release documentation counts 22 vulnerabilities, as Wordfence reports ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). During a core update with a complete package, the new files are unpacked into a predictable directory under `wp-content/upgrade`; the temporary copy includes the installer, and an unauthenticated attacker who requests it at the right moment can interact with the staged copy and reach PHP code execution ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). Wordfence scores it CVSS 8.1 for versions 4.7 through 7.1.3 and states that the attack complexity is high, because the attacker needs web access to the staging tree and must win a race that lasted only seconds in its lab ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). Patchstack reads the same flaw as needing `wp-content/upgrade/` to be reachable over the web, notes that the sink dates back to WordPress 2.8 and that the window returns on every update, unattended ones included, and would not call it practical to exploit ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)).

Wordfence reports that its new firewall rule matched within nine minutes of deployment and that it recorded more than 18,500 requests for staged `setup-config.php` installer paths in the first 21 hours, with two large sources polling small groups of sites for about 14.5 hours, which it reads as attempts to catch the update window ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). No source reports a successful compromise, and no source assigns a CVE identifier. The fix randomises the staging directory, adds an index guard and prevents unsafe promotion of staged configuration data ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). Most sites receive the release through automatic background updates, which Wordfence says should be checked rather than assumed ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).

**Exposure:** any WordPress site on 4.7 to 7.1.3 that runs a full-package core update, automatic ones included, with `wp-content/upgrade/` reachable from the internet; Dashboard > Updates shows the running version, and the fixed releases are 7.1.4 and the backport of each branch (7.0.8, 6.9.11, 6.8.12, 6.7.11, 6.6.11 and the earlier branches listed by Wordfence down to 4.7.39) ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).

**Detection:** in web server access logs, requests under `wp-content/upgrade/` and for `setup-config.php` inside a staging directory, repeated from one source against a few sites as Wordfence saw ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)); between updates the directory holds only an `index.php` ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)). Where an update ran while the site was unpatched and the directory was reachable, confirm that `wp-config.php` and the database it names are unchanged, because the fix exists to stop unsafe promotion of staged configuration data.

**Triage:** a request to a staging path outside an update window finds only an `index.php` and is probing, not compromise; a successful response from the staged installer during an update is the event that matters.

**Defender takeaway:** confirm that the automatic update completed on every site instead of assuming it, and deny web access to `wp-content/upgrade/` at the web server, because a firewall that WordPress itself loads cannot block the request: the staged copy loads from its own files ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)); Wordfence's blocking rule helps only where its firewall is set up to run before direct PHP requests reach their file ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).
