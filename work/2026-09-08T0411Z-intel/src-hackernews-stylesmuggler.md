# extract: served via trafilatura-direct
---
title: Unpatched Magento and Adobe Commerce Zero-Day Exploited to Backdoor Online Stores
author: The Hacker News
url: https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html
hostname: thehackernews.com
description: Sansec says attackers exploit an unpatched Magento and Adobe Commerce flaw to run server code without authentication and install persistent backdoors.
sitename: The Hacker News
date: "2026-09-06"
categories: ['Article']
---
Attackers are exploiting a new unpatched vulnerability in **Magento** Open Source and **Adobe Commerce** that lets them run malicious code on an online store's server without logging in, Dutch e-commerce security company Sansec said in an [advisory published on September 5](https://sansec.io/research/stylesmuggler).

Sansec, which discovered the flaw and named it **StyleSmuggler**, said attacks started on September 4. "Sansec is publishing early because stores are being compromised right now," the company said.

As of September 6, Adobe has not published an advisory, a CVE identifier, a patch, or a workaround, and its [Adobe Commerce security bulletin index](https://helpx.adobe.com/security/products/magento.html) lists nothing after the August 11 update.

A successful attack gives the attacker code execution on the store's server and installs a persistent backdoor. Sansec said all current versions are affected, including 2.4.9, and that it reproduced the full unauthenticated chain on clean Magento Open Source installations of 2.4.7, 2.4.8, and 2.4.9.

Its first victim ran 2.4.6-p15 with Adobe's July and [August 2026 security updates](https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html) applied, which is the latest patch level Adobe offers for that release line and one that Adobe's [August bulletin](https://helpx.adobe.com/security/products/magento/apsb26-92.html) labels 2.4.6-2026-aug.

Sansec has not published a reproduction on Adobe Commerce or on Adobe Commerce on Cloud, and Adobe has not confirmed which versions are affected. Sansec has not said how many stores have been compromised.

The researchers' interim advice for stores not running its Shield product is to temporarily disable GraphQL until Adobe releases a fix.

**Disrex Group**, a Magento hosting and development company that hosts and responded to two of the compromised stores, notes that headless and progressive web app storefronts require GraphQL, whereas most classic and Hyvä storefronts do not.


Adobe's next scheduled security release is on September 8, Sansec said, and it is not yet known whether that release will cover this bug.

Disrex's findings are independent evidence of exploitation from outside Sansec. In an [incident-response repository](https://github.com/disrex-group/stylesmuggler-mitigation) published on September 5, the company said it handled two compromised stores and a third that was attacked but not breached, and that its web-server rules are based on attack traffic captured on one of the compromised stores.

In answers to questions from The Hacker News, Disrex said both stores ran Magento Open Source rather than Adobe Commerce, and that it hosts them itself through its hosting brand RexHosting.

The store Disrex labels **Store A** ran Magento Open Source 2.4.8 and was a Sansec Shield customer, with the module installed, enabled, and licensed. It was hit at 23:10 UTC on September 4, hours before Sansec's first blocking rules for this flaw went live, and Disrex said Shield was active and blocking other malicious traffic against the store at the time.

**Store B**, which was not a Shield customer, ran Magento 2.4.7-p2, a security patch level that Adobe's [version history](https://experienceleague.adobe.com/en/docs/commerce-operations/release/versions) dates to August 2024, eight levels behind the current 2.4.7-p10. It was first hit at 00:55 UTC on September 5, Disrex said, and it is the store from which the company's web-server rules and its reading of the vulnerable code were taken.

Both stores were breached inside the roughly eight-hour window between the first exploitation Sansec observed and the moment any defence for it existed, Disrex said. "Patch status was irrelevant here, which is the part merchants most need to hear," the company told The Hacker News.

The repository carries its own warning. "This repository was written with AI assistance, during a live incident, in a few hours," its README says, adding that it has not been reviewed, that its Apache rules were never run against a live Apache server, and that most of its cleanup commands were written rather than executed.

Sansec's indicators describe the implant as a background process disguised under `[kworker/u:8:0]`, a name that belongs to a Linux kernel thread, with a binary installed at `~/.local/share/.gvfsd/gvfsd-user` under the site user's home directory rather than the web root, and a cron entry that restarts it every five minutes.

Disrex described the binary as a stripped, statically linked Rust program of roughly 1.9 MB built for x86-64 and arm64, and said the cron entry is written straight to the spool file under `/var/spool/cron/crontabs/`, so the system log shows no crontab replacement.

One store carried the same line 1,728 times, and the implant re-added it within a second of removal.

On one of the two stores, the implant made no outbound connection at all. It held 28 connections to the store's own Redis instance on port 6379 and read Magento's session storage from it, Disrex said, and neither of its two packet captures, each over 200 MB and taken while the implant was live, contained a single packet to the download host or the command-and-control address that Sansec listed.

Disrex told The Hacker News that each store ran in its own isolated account with a single site owner, no sudo rights, and no path to any other customer, that the implant ran as the unprivileged site user and could reach nothing beyond that store, and that it confirmed no lateral movement and no other affected site on its platform.

Both stores were contained the same day, roughly eleven and fourteen hours after first contact, the company said, and it found no evidence of data exfiltration, no rogue admin accounts, no injected payment skimmer, and no database backdoor. All sessions were invalidated, and credential rotation is underway as a precaution.

Because it runs a number of Magento stores on its own platform and found the first compromise quickly, Disrex said, it swept its whole estate within the hour and found the second store the same afternoon. The company has also published an [incident write-up](https://www.disrex.nl/blogs/stylesmuggler-magento-zero-day).

Sansec said that for Shield customers attacked before its rules went live, it has no indication that the backdoor was actually used, and recommended rotating Magento credentials wherever the process has been identified.

The attack works in two stages, according to Sansec's outline. It first plants PHP code in a file that Magento itself writes, for example, when generating a failure report. Then it makes Magento execute that file by triggering the platform's standard "Payment Transaction Failed Reminder" email. The code runs while Magento renders the message, so no one has to open it, and the attack can succeed even if email delivery fails.

Sansec has not yet published the full exploit chain and said a breakdown of the chain, the dropper, and the implant will follow in an update.

Disrex's reading of the chain, published in a [mechanism write-up](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/HOW-IT-WORKS.md) alongside its rules, is that a directive within the injected text drives a sequence of Magento's own classes into code that exists solely to serve the command-line dependency-injection compiler.

That code ends by including a file path the attacker chose: the log poisoned a moment earlier. The executed PHP dropper attempts six PHP functions in turn to start a process, then downloads and launches the implant.

Disrex names three files under `setup/src/Magento/Setup/Module/Di/Code/` as the point where the chain ends, and told The Hacker News it identified that sink on its own by reading Magento source on the compromised store. Sansec has not confirmed that reading, and Disrex does not publish the assembled request.

Two locations matter for the first stage. Sansec's published check searches `var/report/` for the marker `X_TRACE_`. Disrex said both of its infections were poisoned through `var/log/system.log` instead and would have been missed by that check, so both directories need searching.

The marker has already drifted: Disrex saw a trigger header of the form `X-TRACE-` followed by ten hex characters on the morning of September 5 and the same header without the word TRACE by the afternoon, so a search should match the shape rather than the exact string.

A TypeError from `array_merge()` with an integer argument in `system.log`, immediately after the include, is evidence that the exploit succeeded, Disrex said. However, a stealthier variant returns an empty array and leaves nothing in the log.

For the process, Disrex said that a genuine kernel thread is owned by root and has no resident memory, so a bracketed name on the site user with real memory usage is the implant. The implant sets its command line to the literal bracketed string, so a check written against the process's `comm` field matches nothing.

Disrex also found that the binary running in memory on one store was a different build from the file on disk, and advises hashing the running process from `/proc/<pid>/exe` as well as the file. Unexpected bursts of "Payment Transaction Failed Reminder" emails are a reason to investigate, Sansec said, although legitimate declined payments generate the same notification.

One of Disrex's two compromises was surfaced by exactly that email. Rick Bouma, Disrex's co-founder, told The Hacker News that the store emailed its own owner a failed-transaction notice in which the template variables were never resolved: a body full of raw `{{var ...}}` tags, a customer address on a `.invalid` domain, and a total of zero.

| Source: Disrex | 

It reads like a broken order, Bouma said, but it is exhaust from the exploitation attempt passing through Magento's template filter, and the merchant's forward of that email started the investigation that found the implant within the hour.

Disrex has published an anonymised copy in an [early-warning write-up](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/EARLY-WARNING-EMAIL.md), which adds Magento's own "an error occurred generating this content" fallback text appearing inside the address block as a third tell, and calls the email the single most useful early-warning sign for merchants because noticing it needs no tooling.

The following indicators have been published by Sansec and in Disrex's [indicator list](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/IOC.md) -

- **Process:**`[kworker/u:8:0]` owned by a non-root user
- **File:**`~/.local/share/.gvfsd/gvfsd-user`
- **File:**`~/.local/share/.gvfsd/.gvfsd_<8hex>.lock`
- **File:**`/tmp/.gvfsd_<8hex>.lock`
- **File:**`/tmp/.kw_<random><random>`
- **Cron:**`*/5 * * * * exec <home>/.local/share/.gvfsd/gvfsd-user` , with a variant pointing at`/tmp/.kw_`
- **SHA-256:**`e315687a1dfe61ef4a5a5642214db6d3b2b05d81391285eebc2af664641a26a7` (Sansec's sample)
- **SHA-256:**`8334b434fa3fe9f59cebe9609b11e0b1fd19d10212c45c705adec1902a1d06ef` (on disk on both Disrex stores)
- **SHA-256:**`251fabd50d7b18a8b5e1b3ef5d64e7198c17244778f6461fb1ab07f6169bf220` (running in memory on one Disrex store)
- **Domain:**`247.cdnflare[.]xyz` (malware download host)
- **IP:**`99.84.67[.]186:443` (command-and-control over WebSocket and TLS, per Sansec)
- **IP:**`88.216.72[.]181` (attacker source, per Sansec)
- **IP:**`5.181.86[.]133` (attacker source sending in bulk, per Disrex)

Sansec recommends its eComscan scanner to detect the implant, and said version 1.9.7 will terminate the process for Shield customers.

Disrex reported a clean result on Store A. eComscan ran there at 10:00 UTC on September 5, roughly eleven hours after the implant first ran and while 1,728 cron lines were present, and reported the store clean. The cause was scope rather than a scanner fault, Disrex told The Hacker News: the scheduled scan was pointed at the store's document root, and the implant had installed one directory above it, under the account's home directory. Disrex has since widened the scan path and said it would confirm the eComscan build number separately.

There is no vendor fix to install. Until Adobe ships one, the options are Sansec's temporary GraphQL shutdown; unofficial mitigations published by Disrex, ProxiBlue, and Graycore; and two server settings that do not depend on the flaw.

Disrex published nginx and Apache rules that block requests carrying the exploit's parameters in the URL query string. Its own test on a live store showed the limit: the same parameters sent in a POST body reached PHP, as did a JSON body, because nginx and Apache inspect only the query string, Disrex said. Disrex describes the rules as stopping the campaign as it currently runs rather than the vulnerability.

Disrex's main mitigation adds a check to three methods in Magento's dependency-injection code scanners, preventing them from running outside the command line. The hand edit is reverted by every composer install, so Disrex also ships it as a [composer-patches source patch](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/patches/README.md) that reapplies on deploy and, it says, applies unchanged from 2.4.6 through 2.4.9.

One of the three files, ClassesScanner.php, is called over HTTP by at least one third-party module, mageplaza/module-admin-permissions, and guarding it breaks that module's admin screen, so Disrex tells administrators to search their vendor directory before touching it.

The guard was tested on a harness rather than inside a running store, and Disrex says it is not a complete fix on its own. A GitHub user, ProxiBlue, separately published the same guard on September 5 as [three unofficial patches](https://gist.github.com/ProxiBlue/07373c92c8c70dc746bbfdcd1f07b789). Bouma told The Hacker News that **ProxiBlue**, whom he identifies as Magento developer Lucas van Staden, arrived at the identical guard without coordination, on the same three scanner methods, with the same `PHP_SAPI !== 'cli'` check and the same exception message, and that Disrex's own version was written during its response.

Disrex has since reproduced ProxiBlue's three patches [in its repository with credit](https://github.com/disrex-group/stylesmuggler-mitigation/tree/main/patches/upstream/proxiblue) so the convergence can be checked in one place, and warns that the two are the same fix and must not be applied on top of each other. Disrex regards two parties reaching the same fix separately as strong corroboration that it is the right one. Neither Sansec nor Adobe has confirmed that these scanners are where the chain ends.

Graycore, LLC published a [Magento module](https://github.com/graycoreio/magento2-style-smuggler-patch) on GitHub and Packagist on September 5 whose current code, Graycore says, hardens three points on the chain: the email template block directive refuses backend blocks, the grid row URL generator checks a class before building it, and PHP opening tags in Web API fatal error reports are broken.

The version on Packagist at the time of writing was an earlier release whose only mitigation targeted a PayPal GraphQL resolver that has since been removed. The README says "That is hardening, not a fix" and warns that other paths through the vulnerability remain open and that a store may already be compromised.

Two server settings do not depend on knowing the chain at all, Disrex said. At one of its two stores, the first four of the six PHP functions the dropper tried were disabled; `proc_open` was not, and the dropper used it to start the implant, with `open_basedir` doing nothing to contain the child process.

Adding `proc_open` to PHP's `disable_functions`, and mounting `/tmp`, `/var/tmp` and `/dev/shm` with `noexec` so a downloaded binary cannot run, are the layers Disrex puts ahead of every rule in its repository.

For a store that is already infected, Disrex's [cleanup guide](https://github.com/disrex-group/stylesmuggler-mitigation/blob/main/CLEANUP.md) sets the order: preserve evidence first, remove the cron entry before killing the process because the process restores it, do not reboot because the copy under `/proc` may be the only remaining binary, and do not run composer install to clean up because it overwrites the timestamps that show what was touched.

It then recommends flushing session storage since the implant read it, and rotating the `crypt/key` in `app/etc/env.php`, as well as every admin password, every payment provider API key, and every other integration credential in that file.

Hosting providers Nexcess and Liquid Web posted identical incident notices on September 5, stating they were reviewing their server environments and implementing [precautionary measures](https://status.nexcess.net/).

Neither claims a confirmed customer compromise or its own reproduction of the flaw. Disrex recorded 26 distinct source addresses across its two stores, taken from the stores' own nginx access logs and deduplicated, two of them hosting infrastructure sending in bulk and the rest a residential proxy pool sending two to six requests each, and said that blocking the single attacker address in Sansec's advisory would have stopped less than a quarter of the traffic it saw. An earlier count of 28 included two of Disrex's own servers making verification requests during the response, which it removed. No source has named the attackers.

The Hacker News has reached out to Adobe, Sansec, and Graycore for comment, and will update the story if we hear back.

*(The story was updated after publication with responses from Disrex Group's Rick Bouma, who corrected the versions, Shield status, and first-contact times of the two compromised stores, explained the eComscan miss, described the early-warning email that surfaced one of the compromises, and confirmed that ProxiBlue's patches, now included in the Disrex repository, were arrived at independently.)*

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
