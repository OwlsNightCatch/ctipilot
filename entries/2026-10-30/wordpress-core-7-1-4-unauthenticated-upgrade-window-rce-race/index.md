---
schema: 1
kind: vulnerability
title: "WordPress core 4.7 to 7.1.3: an unauthenticated race in the core update process can lead to remote code execution, fixed in 7.1.4 and backported to every supported branch, listed by CISA as exploited; Wordfence assigned CVE-2026-119977"
headline: "CISA lists WordPress core's upgrade-window RCE race as exploited; block wp-content/upgrade before installing 7.1.4"
summary: >
  WordPress 7.1.4 of 2026-10-28 fixes a weakness in the core upgrade process that lets an unauthenticated attacker reach the staged installer and run code on the server
  during a full-package core update, in versions 4.7 to 7.1.3, with backports for every branch down to 4.7. CISA added CVE-2026-119977 to its Known Exploited Vulnerabilities catalog on 2026-11-03;
  Wordfence reports more than 18,500 probing requests in the first 21 hours, while Patchstack calls the race hard to win and says it needs a web-reachable staging directory. The discoverer says the update that installs the fix still unpacks with the old code, so the staging directory must be blocked before updating.
discovered_at: "2026-10-30T03:45:00Z"
updated_at: "2026-11-07T03:51:45Z"
event_date: "2026-10-28"
run_id: 2026-10-30T0255Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:wordpress-core"]
techniques: [T1190]
affected_products: ["WordPress Core"]
cves:
  - id: CVE-2026-119977
    cvss: "8.1 (CVSS 3.1, Wordfence)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "WordPress Core 4.7.0 to 7.1.3 (every branch from 4.7 below its fixed release)"
    fixed: "7.1.4, 7.0.8 and the backport of each branch down to 4.7.39"
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
  - url: "https://www.wordfence.com/threat-intel/vulnerabilities/id/4b4da0cf-d9f4-47c4-a0e8-6c4dc5a6f250"
    publisher: "Wordfence Intelligence (CVE-2026-119977)"
    date: "2026-10-31"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog"
    publisher: "CISA"
    date: "2026-11-03"
    role: corroborating
  - url: "https://cyber.gc.ca/en/alerts-advisories/wordpress-security-advisory-av26-1117"
    publisher: "Canadian Centre for Cyber Security"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability"
    publisher: "Picus Security"
    date: "2026-11-05"
    role: corroborating
  - url: "https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html"
    publisher: "The Hacker News"
    date: "2026-11-06"
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
  - quote: "based on evidence of active exploitation"
    publisher: "CISA"
    source_url: "https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog"
  - quote: "The update that installs the fix still unpacks its files using the site's old, unpatched code"
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html"
  - quote: "isn’t partial versus complete. It’s whether the updater already installed on the site has been fixed."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html"
verification: multi-source
sourcing_note: >
  WordPress.org is the disclosing party and names the weakness without a CVE identifier; Wordfence, as numbering authority, has since assigned CVE-2026-119977, which its vulnerability record carries, and the CVSS 8.1 score is Wordfence's. Wordfence and Patchstack analysed the fix independently and agree on the mechanism, while the exploitation-attempt telemetry is Wordfence's alone and Patchstack rates the race impractical to win. The exploited status rests on CISA's catalog listing of 2026-11-03, which the Canadian Cyber Centre relays and which names no victim or method. The finding that the update installing the fix is itself exposed is the discoverer's, in his own post and in his statement to The Hacker News.
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
  - "On every WordPress site your organisation, its web agencies or its hosting suppliers run, deny web access to wp-content/upgrade/ in the web server configuration (not with an .htaccess file inside that folder) and confirm it answers 403 before installing 7.1.4 or the fixed release of its branch, because the update itself still unpacks with the old code and a firewall that WordPress itself loads does not run for that request; then confirm in Dashboard > Updates that each site is on 7.1.4 or the fixed release of its branch."
updates:
  - at: "2026-11-01T13:52:53Z"
    run_id: 2026-11-01T1312Z-audit
    type: correction
    summary: >
      Wordfence assigned CVE-2026-119977 (CVSS 3.1 8.1) to the WordPress upgrade-window race after the
      entry was written; the statements that no CVE identifier exists are replaced and the CVE record is
      added.
    fields: [body, cves, sources, sourcing_note, summary, title]
  - at: "2026-11-04T03:25:52Z"
    run_id: 2026-11-04T0256Z-intel
    type: update
    summary: >
      CISA added CVE-2026-119977 to its Known Exploited Vulnerabilities catalog on 2026-11-03 on evidence
      of active exploitation, so the flaw is now listed as exploited; the catalog entry names no victim or
      method, and Wordfence's probing telemetry remains the only described activity.
    fields: [cves, priority, tags, headline, summary, title, sources, evidence, sourcing_note, body]
  - at: "2026-11-07T03:51:45Z"
    run_id: 2026-11-07T0256Z-intel
    type: update
    summary: >
      The discoverer, Umut Bayram of Picus Security, shows that the update installing WordPress 7.1.4
      still unpacks with the site's old code, so the staging folder under wp-content/upgrade can be
      reachable at a predictable path during that update, while a partial package exposes the installer
      only if it contains the installer files; he advises denying web access to the folder and confirming
      it answers 403 before updating.
    fields: [headline, summary, actions, sources, evidence, sourcing_note, body]
migrated_from: null
---

WordPress 7.1.4, released on 2026-10-28, fixes a weakness in the upgrade process that can lead to remote code execution during the upgrade window, and backports follow for every branch that receives security fixes, currently through 4.7 ([WordPress.org, 2026-10-28](https://wordpress.org/news/2026/10/wordpress-7-1-4/)). During a core update with a complete package, the new files are unpacked into a predictable directory under `wp-content/upgrade`; the temporary copy includes the installer, and an unauthenticated attacker who requests it at the right moment can interact with the staged copy and reach PHP code execution ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). Wordfence scores it CVSS 8.1 for versions 4.7 through 7.1.3 and states that the attack complexity is high, because the attacker needs web access to the staging tree and must win a race that lasted only seconds in its lab ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). Patchstack reads the same flaw as needing `wp-content/upgrade/` to be reachable over the web and would not call it practical to exploit ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)).

Wordfence reports that its new firewall rule matched within nine minutes of deployment and that it recorded more than 18,500 requests for staged `setup-config.php` installer paths in the first 21 hours ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)). CISA lists the flaw as exploited, and no source names a victim or describes a successful compromise ([CISA, 2026-11-03](https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog)). The fix randomises the staging directory, adds an index guard and prevents unsafe promotion of staged configuration data ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).

**Exposure:** any WordPress site on 4.7 to 7.1.3 with `wp-content/upgrade/` reachable from the internet while a core update runs; the discoverer says the deciding factor is whether the updater already installed on the site has been fixed, so the update to 7.1.4 is exposed too, automatic updates included, although a partial package exposes the installer only if it contains the installer files ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)); on 5.9 or later the staging folder name can be predicted, on 4.4 to 5.8 a random suffix hides it unless the site leaks it, and 4.6 and earlier, which Picus counts as affected back to 2.7, get no fix ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability)). The fixed releases are 7.1.4 and the backport of each branch (7.0.8, 6.9.11 and so on down to 4.7.39) ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).

**Detection:** in web server access logs, requests under `wp-content/upgrade/` and for `setup-config.php` inside a staging directory, repeated from one source against a few sites as Wordfence saw ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)); between updates the directory holds only an `index.php` ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)). Where an update ran while the site was unpatched and the directory was reachable, confirm that `wp-config.php` and the database it names are unchanged ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability)) and look for administrator accounts, plugins and PHP files under `wp-content/upgrade/` that nobody created ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)).

**Triage:** a request to a staging path outside an update window finds only an `index.php` and is probing, not compromise; a successful response from the staged installer during an update is the event that matters.

**Defender takeaway:** deny web access to `wp-content/upgrade/` at the web server and confirm it answers 403 before the update runs, then confirm that the update completed on every site instead of assuming it, because a firewall that WordPress itself loads cannot block the request: the staged copy loads from its own files ([Patchstack, 2026-10-28](https://patchstack.com/articles/wordpress-7-1-4-security-release/)); Wordfence's blocking rule helps only where its firewall is set up to run before direct PHP requests reach their file ([Wordfence, 2026-10-29](https://www.wordfence.com/blog/2026/10/wordpress-7-1-4-security-release-rce/)).

## Correction — 2026-11-01T13:52:53Z

The flaw now has an identifier: Wordfence tracks it as CVE-2026-119977, a time-of-check time-of-use race condition scored CVSS 3.1 8.1 (AV:N/AC:H/PR:N), affecting WordPress 4.7.0 to 7.1.3 with the same fixed releases as above ([Wordfence Intelligence, 2026-10-31](https://www.wordfence.com/threat-intel/vulnerabilities/id/4b4da0cf-d9f4-47c4-a0e8-6c4dc5a6f250)). The statement that no source assigns a CVE identifier is withdrawn; scanners and asset inventories can now match the flaw by that ID.

## Update — 2026-11-04T03:25:52Z

CISA added CVE-2026-119977 to its Known Exploited Vulnerabilities catalog on 2026-11-03 on evidence of active exploitation ([CISA, 2026-11-03](https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog)), and the Canadian Cyber Centre's advisory of the same day relays the listing for WordPress Core before 7.1.4 ([Canadian Centre for Cyber Security, 2026-11-03](https://cyber.gc.ca/en/alerts-advisories/wordpress-security-advisory-av26-1117)). The listing names no victim, attacker behaviour or exploitation method, so Wordfence's probing telemetry above remains the only described activity and Patchstack's high-complexity rating still stands. A site that ran a full-package core update on 4.7 to 7.1.3 while `wp-content/upgrade/` was reachable needs the compromise check in the Detection line, not only the update.

## Update — 2026-11-07T03:51:45Z

Umut Bayram of Picus Security, who found the flaw, shows that the update which installs the fix still unpacks its files with the site's old, unpatched code ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability); [The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)). Picus says the new code's skip of wp-config.php already works in that first update but the randomised folder name does not, so the temporary installer sits at a predictable path on sites running 5.9 or later and, on 4.4 to 5.8, behind a random suffix that hides it unless the site leaks the path; an attacker who reaches it can no longer replace the live configuration but can still set up the temporary copy, log in to it, run PHP and from there read or write files in the live directory ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability)). Bayram told The Hacker News the deciding factor "isn’t partial versus complete. It’s whether the updater already installed on the site has been fixed", and that a partial package exposes the installer only if it contains the installer files; The Hacker News found WordPress.org offering an in-branch move such as 7.1.3 to 7.1.4 as a partial package, automatic updates included, so whether such an update is exposed depends on what that package contains, and only once 7.1.4 or the branch fix is installed do later updates use a random folder ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)). WordPress 4.6 and earlier get no fix ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)).

The order matters: Picus advises denying web access to wp-content/upgrade/ in the web server configuration first, confirming that the path answers 403, and only then updating; this does not break updates, because WordPress reaches the folder through the filesystem ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability)). An .htaccess file placed inside the folder does not work, because the old updater deletes the folder's contents before unpacking, and WP-CLI's wp core update is no substitute because it uses the same updater and folder ([Picus Security, 2026-11-05](https://www.picussecurity.com/resource/blog/cve-2026-119977-when-updating-wordpress-becomes-the-vulnerability)). For sites that stayed on an affected version, Wordfence suggests looking for unexpected requests to PHP files under wp-content/upgrade, administrator accounts no one recognises, plugins no one installed and PHP files in wp-content/upgrade that no one put there ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)).

Code that its authors describe as an exploit has appeared in public GitHub repositories since earlier this week, and whether it works has not been established; WordPress's own advisory rates the flaw low, against Wordfence's CVSS 8.1 and CISA's listing as exploited ([The Hacker News, 2026-11-06](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)). None of these sources reports a compromise through the update that installs the fix; CISA's listing and Wordfence's probing telemetry above are unchanged.
