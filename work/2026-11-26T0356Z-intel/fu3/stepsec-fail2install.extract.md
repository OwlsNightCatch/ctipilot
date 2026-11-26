---
title: "Fail2Install (CVE-2026-132165): Drupal Installer Flaw Lets Attackers Take Over Sites and Run Code"
author: Owais Shaikh View LinkedIn November
url: https://www.stepsecurity.io/blog/fail2install-cve-2026-132165
hostname: stepsecurity.io
description: Drupal CVE-2026-132165 (Fail2Install) is an unauthenticated installer flaw that can reinstall a live site and run code. We reproduced the re-entry, confirmed the fix, and show how to detect and block it.
sitename: stepsecurity.io
date: "2026-11-26"
fingerprint: c518f88b9520f39a
language: en
image: https://cdn.prod.website-files.com/673b71f0790aabf30bd30bf8/6b07530789620bf228fe3061_6b0752df79f77b9df149f6f3_cve-2026-132165-cover-house-v3.png
pagetype: website
filedate: "2026-11-26"
---
On November 18, 2026, Drupal released versions 10.6.22, 11.3.22, and 11.4.13 to fix **CVE-2026-132165**, a flaw in the Drupal core installer, `core/install.php`. An attacker who can make the site's database connection fail briefly can open the installer on a site that is already running, take the site over, and run code on the server. No account is needed. Drupal rates it Highly critical.

The flaw is being exploited. Drupal updated its advisory to say the Drupal Security Team received a report of exploitation on live sites as early as November 19 at 19:00 UTC, about a day after the fix and five days before the public exploitation write-up. CISA added it to its Known Exploited Vulnerabilities (KEV) catalog on November 24. The same day, a research team that found the bug independently published a detailed write-up of how to exploit it on default Drupal setups, and named it **Fail2Install**. Drupal's advisory credits an automated open-source code scanner with the original discovery.

### At a glance

- **CVE:** CVE-2026-132165, Drupal advisory SA-CORE-2026-017, also called Fail2Install
- **Severity:** Highly critical, 20 out of 25 on Drupal's risk scale. The CVE record had not been published as of November 26, so there is no CVSS score yet.
- **Component:** Drupal core installer (`core/install.php`)
- **Impact:** an anonymous attacker can reinstall a live site, set up their own administrator account, and run code on the server
- **Affected:** Drupal 10 before 10.6.22, 11.0.0 through 11.3.21, and 11.4.0 through 11.4.12. The public write-up reports that the end-of-life Drupal 8.9 and 9 are affected too.
- **Fixed:** Drupal 10.6.22, 11.3.22, and 11.4.13, released November 18, 2026
- **What the attacker needs:** a reachable `core/install.php`, and a way to make the site's database refuse some connections and accept others during a single request. The public write-up does this with request floods against Drupal's official Docker images on default settings.
- **Exploited in the wild:** yes. First reported on November 19, 2026. Added to CISA's KEV catalog on November 24, with a November 27 deadline for US federal civilian agencies. CISA's entry requires forensic triage as well as patching.

## How the Bug Works

Drupal ships an installer at `/core/install.php`. On a site that is already installed, the installer should stop with a "Drupal already installed" page. To decide whether a site exists, it connects to the database configured in `settings.php` and looks for Drupal's tables.

The installer checks the database several times during that decision. In affected versions, the early checks treat a database error as a sign that Drupal is not installed yet. One of them carries this comment in the code: "Do not trigger an error if the database query fails, since the database might not be set up yet." The check that does stop the installer on a database error, its requirements check, runs later.

So if the database refuses the early connections and accepts the later one, all within one request, the installer concludes the site is new and shows its setup forms on a live site.

The installer's database form saves the settings it receives to `settings.php`. Once an attacker submits that form with their own database settings, the live site points at the attacker's database. The attacker then creates the site's administrator account.

### How attackers make the database fail

A database refuses new connections when it runs out of connection slots, and PHP cannot open a connection when the server runs out of local network ports. The public write-up uses both, depending on how the site is deployed:

- **Apache with PostgreSQL.** PostgreSQL allows 100 connections by default. Drupal's official Apache image runs up to 150 PHP workers, and every Drupal page request opens a database connection. The write-up sends enough slow requests to hold every connection slot, then frees one at the right moment so the database turns away the early checks and accepts the later one.
- **Apache with MySQL.** MySQL allows 151 connections, more than Apache has workers. The write-up sends requests whose `Referer` header contains a byte that is not valid UTF-8. MySQL rejects it when Drupal's database logger (enabled by the Standard installation profile) tries to save the log entry, and the logger retries on a second connection, so each request holds two.
- **PHP-FPM with either database.** PHP-FPM runs 5 workers by default, too few to fill a database's connection slots. Instead, the write-up uses up the PHP server's outgoing network ports. Linux keeps each closed connection's port reserved for 60 seconds (the `TIME_WAIT` state) and has 28,232 ports for outgoing connections by default. Opening about 471 new database connections per second exhausts them, and PHP reports "Cannot assign requested address". The write-up's tests reached this limit on servers with 4 virtual CPUs. On servers with 2, it reports that success depends more on the deployment.

### From reinstallation to code execution

An attacker who controls the installation can log in as the new administrator. The write-up describes a shorter path to running code on the server:

1. In the installer's database form, choose SQLite and give a database file path that ends in `.php` inside the web root, such as `web/modules/x.php`. The installer creates the SQLite database file there. Drupal's official Docker image lets the web server user write to `web/modules`.
2. In the site configuration form, enter PHP code as the site name. Drupal stores the site name in the database, so the code is written into the `.php` file.
3. Request the file. Drupal's stock `.htaccess` blocks direct requests for PHP files outside `/core`, but its exception for core scripts only checks how the URL ends. A request for `/modules/x.php/core/x.php` ends in `/core/x.php`, so the rule lets it through, and Apache runs `/modules/x.php`.

The fixed releases do not change that `.htaccess` rule. Drupal 11.4.13 and 10.6.22 ship the same lines as 11.4.12. So on Apache, a PHP file written into a code directory such as `web/modules` can still be run this way. Step 4 of [What to Do Now](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#what-to-do-now) covers who can write there.

### What the attacker needs

- **A reachable installer.** Drupal's stock `.htaccess` explicitly allows requests to PHP files in `/core`, including `install.php`. Some managed hosting platforms block the installer.
- **A Drupal site backed by MySQL or PostgreSQL.** The public write-up demonstrates the full chain on Apache and on PHP-FPM, each with MySQL and with PostgreSQL, using Drupal's official Docker images with default settings.
- **The ability to send a heavy burst of requests.** The connection and port limits above are defaults. Different limits change how many requests the attack needs. They do not remove the bug.
- **For code execution, write access for the web server.** The shortest path writes a PHP file into the web root. Drupal's advisory adds that some, but not all, exploit paths are blocked if the web server cannot write to `settings.php` or change its permissions.

## What the Fix Changes

The fix is a single commit to `core/includes/install.core.inc` ([a15a19b](https://github.com/drupal/drupal/commit/a15a19b74bb9f16f75a44ed39219049283de2381)). It makes four changes:

1. **A database error now stops the installer.** If the database configured in `settings.php` cannot be checked, the installer shows a "Requirements problem" page with the message "The configured database could not be verified." It no longer treats the error as an empty database, so a later successful connection no longer matters.
2. **A finished installation cannot be resumed.** The installer already refused to run when its stored progress said it had finished. It now also refuses when any step is recorded together with an install time, which Drupal sets only when an installation completes. This blocks sites whose stored installer progress stopped short of the final step.
3. **Only the browser that started an installation can continue it.** The installer stores a random token in the first visitor's session. Any other session gets "The installation can only be continued in the browser session that started it." This stops another visitor from taking over an installation in progress.
4. **The installer no longer changes permissions on `settings.php`.** Before the fix, when `settings.php` was not readable or writable, the installer tried to fix that with `chmod`, which succeeds whenever the web server user owns the file. The fixed installer only reports the problem.

## What We Reproduced

We installed Drupal 11.4.12 and the fixed 11.4.13 on one server we own, each on Apache with mod\_php and PostgreSQL, with Apache's worker count (150) and the web-directory ownership set to match Drupal's official Apache image. Both sites ran the Standard installation profile and were fully installed. Nothing was exposed to the internet.

### The flood reopens the installer on a live site

We flooded the finished 11.4.12 site with fast, unauthenticated requests to a single uncached page, enough to push PostgreSQL to its connection limit. During that flood we sent `GET /core/install.php?langcode=en&profile=standard` and read the page title back.

The installer's own forms tell you what happened. "Database configuration" is the form that sets a site's database, so it is the point from which a site is reinstalled. "Requirements problem" means the installer caught the database error and stopped. "Drupal already installed" means its first check reached the database and refused.

On 11.4.12, the installer reopened on a live, finished site, with no change to anything stored on it. In one 20-second run, 12% of the `install.php` requests came back as "Database configuration"; the rate swings from run to run, so read it as "this happens", not as a fixed number. The page was a real installer form, with the database-driver selector, the database name and user fields, and a "Save and continue" button. The other requests split between "Requirements problem" and "Drupal already installed", the two ways the race can miss.

We did not change the site's state to get this. The earlier state the installer needs is produced by the flood itself, within single requests.

### The patch holds under the same flood

We ran the identical flood against 11.4.13. It never reached the "Database configuration" form. Every request that reopened the installer on 11.4.12 came back as "Requirements problem." The fix stops the installer at the database error instead of continuing past it.

### We reached the reinstall form, but did not reinstall here

The "Database configuration" form is the point a site is reinstalled from. From it, an attacker points the site at a database they control, or, for the code-execution shortcut in [How the Bug Works](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#from-reinstallation-to-code-execution), at a SQLite file written to a `.php` path under the web root, and then sets the site name to PHP code. We stopped at reaching that form and did not complete the reinstall.

The SQLite shortcut also did not apply on our host. Drupal 11.4 requires SQLite 3.45 or newer, and our server runs SQLite 3.40, so the installer refuses the SQLite driver at this form. Drupal's official Docker images ship a new enough SQLite, which is what the public write-up used. A host with an older library can still be taken over by reinstalling against another database; it just cannot use this one file-writing trick to run code.

### The code-execution step is real, and the fix does not touch it

We tested the final step on its own, the part that runs a planted file. We placed a small PHP file that prints the result of a sum into `web/modules`, owned by the web server as the official image leaves it. A direct request for it returned `403`, blocked by the stock `.htaccess`. The request `GET /modules/<file>.php/core/x.php` returned `200` and ran the PHP: the computed sum came back in the response, so the file was executed, not served.

The `.htaccess` rule that allows this is **unchanged in the fixed releases**. The same request runs a planted PHP file in `web/modules` on 11.4.13 exactly as on 11.4.12. The patch closes the installer re-entry; it does not stop code execution for an attacker who can write a `.php` into a code directory by any route. Making those directories read-only for the web server (step 4 below) is a separate control.

### The attack cannot be quiet

Winning the race means driving the database into refusing connections. The 20-second flood logged thousands of PostgreSQL errors:

`FATAL:  sorry, too many clients already`
and returned 15,490 HTTP 500 responses to the flood itself, from Apache workers whose database connection was refused mid-page. The attack cannot avoid this: the connection-pool exhaustion it depends on is a loud, logged event, which the [detection section](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#how-to-spot-exploitation) builds on.

### Smaller database pools are easier to hit

PostgreSQL allows 100 connections by default. We also tested a 25-connection pool, the scale of a small managed database or a connection pooler. At 25 connections the installer reopened readily. At the default 100, a flood from a separate attacker host drove the pool to 96 of its 97 usable connections, with more than a thousand connection refusals in a single 60-second run, and the installer requests did reach a saturated pool. But across repeated tuning we did not reproduce the re-entry at 100: saturating the pool and keeping an installer request serviceable work against each other on an Apache and mod\_php server, so it rarely succeeded.

A default-pool site is not safe, though. The published research reached a reinstall at the default 100 with a purpose-built request that holds one database connection per request, and our own flood drove that pool deep into connection refusals. A smaller pool only makes the attack faster and more reliable. Treat any site with a reachable installer as exploitable regardless of its database size.

### The mitigations hold

Adding the `<Location "/core/install.php">` deny block from [What to Do Now](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#what-to-do-now) turned the installer's responses to `403`, including the request for `/core/install.php/foo`, while the homepage kept returning `200`.

The official image lets the web server user own `web/modules`, and as that user we could write a `.php` file there, which is the file the code-execution path drops. After we changed the directory's ownership so the web server could not write to it, the same write was refused and the site still served its homepage.

A per-source connection limit stopped the flood outright. We put a cap of 20 concurrent connections per source address in front of the site (an `nftables` rule; nginx `limit_conn` or a WAF connection-rate rule does the same) and ran the same flood again from the separate host. The database never passed 20 of its 100 connections, logged no refusals, and a normal client kept getting `200` while the flood ran. The attacker needs on the order of a hundred concurrent connections from one place to exhaust the pool, so capping connections per source takes that away. A flood spread across many addresses would get past it, so this raises the bar rather than closing the bug, and the patch and the installer block still come first.

All of this ran on servers we own, and we removed the planted files afterward.

## Who Is Exposed

We counted internet-facing Drupal sites with Shodan on November 26. Shodan sees about 55,800 Drupal services. The sites that still report a version in their generator meta tag break down by major release like this:

| Drupal major version | Services | This flaw | 
|---|---|---|
| 7 | 1,514 | Not affected (the flaw starts at 8.9) | 
| 8 | 4,478 | Affected, end of life, no fix | 
| 9 | 10,605 | Affected, end of life, no fix | 
| 10 | 9,613 | Affected, fixed in 10.6.22 | 
| 11 | 6,763 | Affected, fixed in 11.3.22 and 11.4.13 | 

That is about 31,500 services on affected branches, and roughly 15,000 of them on the end-of-life 8 and 9 branches, which will never get a fix and have to migrate. These are lower bounds: a site that hides its generator tag is not counted. The United States leads by country (15,921), followed by Italy, China, Germany, Vietnam, France, India, and Canada.

One difference from a flaw like a vulnerable nginx version matters for triage. Modern Drupal publishes only its major version, not its patch level. On our test site the `X-Generator` header read `Drupal 11`, not `11.4.12`. So a banner scan cannot tell a patched 10.6.22 from a vulnerable 10.6.21, and you cannot scan the internet, or your own fleet, for this CVE by version string. The two things you can check are whether `/core/install.php` is reachable and what `drupal/core` version the site was built from. The first is in [What to Do Now](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#what-to-do-now); the second is where developer-machine and build inventory help, below.

## Affected and Fixed Versions

| Drupal branch | Affected | Fixed | 
|---|---|---|
| 11.4.x | 11.4.0 to 11.4.12 | 11.4.13 | 
| 11.3.x | 11.3.0 to 11.3.21 | 11.3.22 | 
| 11.0.x to 11.2.x | All | No fix. End of life: upgrade to 11.3.22 or 11.4.13. | 
| 10.6.x | 10.6.0 to 10.6.21 | 10.6.22 | 
| 10.5.x and earlier | All | No fix. End of life: upgrade to 10.6.22 or Drupal 11. | 
| 8.9 and 9 | Affected, according to the public write-up | No fix. End of life. | 
| 7, and 8 before 8.9 | Not affected, according to the public write-up | Not applicable | 
| Official Docker images ( `drupal`) | Images for affected versions | `drupal:11.4.13`, `drupal:11.3.22`, `drupal:10.6.22`, or later | 

## What to Do Now

### 1. Find your Drupal sites and their versions

In each site's project directory (the one with `composer.json`), check the installed core version:

`composer show drupal/core | grep -E '^versions'`
Then check whether the installer is reachable from outside. These are the checks from Drupal's guide, with `example.com` replaced by your site's address:

```
curl -I https://example.com/core/install.php
curl -IL https://example.com/install.php
curl -I https://example.com/core/install.php/foo
```
A `200` response means the installer is reachable. A `403` or `404` means it is blocked.

### 2. Upgrade Drupal core

Upgrade to 10.6.22, 11.3.22, or 11.4.13, or later. With Composer, Drupal's documented update steps are:

```
composer update "drupal/core-*" --with-all-dependencies
drush updatedb
drush cache:rebuild
```
Run `composer show drupal/core` again to confirm the version, then deploy. For containers, rebuild from a fixed image and redeploy. A running container keeps the code it started with.

Sites on Drupal 11.2 or earlier, 10.5 or earlier, 9, or 8 get no fix and need to move to a supported branch. The same releases also fix SA-CORE-2026-018, a moderately critical flaw.

### 3. Block the installer, even after upgrading

Drupal now recommends blocking `/core/install.php` on every installed site. On Apache, add this to the virtual host configuration (not to `.htaccess`), then reload Apache:

```
<Location "/core/install.php">
  Require all denied
</Location>
```
On nginx, add this inside the `server` block, then reload nginx:

```
location ^~ /core/install.php {
  return 404;
}
```
Do not use an exact match (`location = /core/install.php`) on nginx. Drupal's guide warns that on servers that pass any URL containing `.php/` to PHP, an exact match does not block `/core/install.php/foo`, and the installer still runs.

Run the three `curl` checks from step 1 again. All three should return `403` or `404`. If you need the installer later, for example to add a site to a multisite setup, use `drush site:install`, which does not go through `install.php`.

### 4. Make `settings.php` and code directories read-only for the web server

Drupal's advisory says some exploit paths are blocked when the web server cannot write to `settings.php` or change its permissions. Drupal's file permissions guide goes further: files that the web server runs should be read-only for the web server and owned by a different user.

For `settings.php` and its directory, with `deploy` standing in for a user other than the web server user, and `www-data` for the web server's group (its name on Debian, Ubuntu, and the official Docker image):

```
sudo chown deploy:www-data web/sites/default web/sites/default/settings.php
sudo chmod 550 web/sites/default
sudo chmod 440 web/sites/default/settings.php
```
The `files` directory inside `web/sites/default` keeps its own ownership, so Drupal can still write uploads there.

Give `web/modules` and `web/themes` the same treatment, as Drupal's file permissions guide describes, so the web server cannot add PHP files to them. Drupal's official Docker image gives the web server user ownership of `web/sites`, `web/modules`, and `web/themes`. If you build on it, change that ownership in your own Dockerfile.

### 5. Check for signs of compromise

If a site ran an affected version with the installer reachable, especially after November 18, use the checks below.

## How to Spot Exploitation

Paths below assume a Composer-based site with its web root in `web/`. Drupal's official Docker images send the web server's logs to the container output, so read them with `docker logs <container> 2>&1` in place of the log file.

The strongest signal comes from the attack's own cost. To win the race, an attacker has to drive the database into refusing connections. That is a loud, logged event, and it has to happen for the exploit to work, so it is a high-fidelity tripwire rather than just a sign of load. In our lab a single 20-second run logged thousands of database-refusal errors and returned 15,490 HTTP 500 responses. Ordinary traffic does not produce these errors: 600 normal requests at high concurrency logged none. A large legitimate traffic spike can also exhaust a pool, so the signal to alert on is a database-refusal burst together with requests to `install.php`, which has no legitimate reason on a finished site.

- **A burst of database-refusal errors.** When its connection slots run out, PostgreSQL logs `FATAL: sorry, too many clients already`. The MySQL equivalents, in the PHP or web server error log, are `SQLSTATE[HY000] [1040] Too many connections` (slots exhausted) and `SQLSTATE[HY000] [2002] Cannot assign requested address` (the PHP server out of network ports). On a healthy site these are rare. A cluster of them, especially around requests to `install.php`, is the clearest sign of this attack. Alert on them.
- **A burst of HTTP 500s.** While the database is refusing connections, ordinary page requests fail too. A spike of `500` responses from one source in a short window, alongside the database errors above, is the same event seen from the web server.

`grep -cE '" 50[0-9] ' /var/log/apache2/access.log`
- **Requests to the installer on an installed site.** Rerunning the installer means loading and submitting its forms. An installed site has no reason to receive these. A response titled "Database configuration" to an anonymous client is the re-entry itself.

`grep -E '"(GET|POST) /core/install\.php' /var/log/apache2/access.log`
- **A PHP file that is really an SQLite database.** The code-execution path stores its payload inside an SQLite database file with a `.php` name. SQLite files start with the text `SQLite format 3`. Ordinary PHP files do not:

`grep -rla --include='*.php' '^SQLite format 3' web/`
The `-a` flag is needed because the file is binary. In our test, this found the SQLite database an attack would plant; an ordinary module file did not match.

- **URLs with `.php/core/` in the path.** This is how the code-execution path gets past `.htaccess`. Drupal does not generate such URLs.

`grep -E '\.php/core/[^ ]*\.php' /var/log/apache2/access.log`
- **Changes to `settings.php`, the install time, and user 1.** A reinstall saves new database settings to `settings.php` and records a new install time. User 1 is the administrator account the installer creates.

```
ls -l --time-style=full-iso web/sites/default/settings.php
grep -n "'driver'" web/sites/default/settings.php
drush state:get install_time
drush sql:query "SELECT uid, name, mail, changed FROM users_field_data WHERE uid = 1"
```
`install_time` and `changed` are Unix timestamps. Convert them with `date -d @<value>`. An install time later than your site's original installation means the installer ran to the end again. A `'driver'` of `sqlite` on a site that uses MySQL or PostgreSQL means the database settings were replaced.

If you find any of these, treat the server as compromised. An attacker who ran code could read `settings.php`, which holds the database password and the site's hash salt. Restore from a backup made before the attack, rotate the database credentials and any keys stored in the site's configuration, and review all administrator accounts.

## How StepSecurity Helps

Drupal sites are Composer projects. Each project's `composer.lock` pins the `drupal/core` version that gets deployed, and developers keep checkouts of those projects on their machines. [StepSecurity Dev Machine Guard](https://www.stepsecurity.io/dev-machine-guard) reads Composer declarations and lock files on each developer machine it runs on, so you can list the Drupal projects your developers work on and see which `drupal/core` version each one pins.

### Find Drupal projects on developer machines

The [OSS Packages](https://docs.stepsecurity.io/developer-machines/packages/oss-packages) page lists the open-source packages Dev Machine Guard detects on enrolled machines, by ecosystem. PHP inventory requires agent version 1.18.0 or later.

1. Open **OSS Packages** and select the **PHP** ecosystem.
2. Search for `drupal/core`.
3. Open the package. **Version distribution** lists each version with the number of devices it appears on, and **Devices** lists every machine that has it. For each match, Dev Machine Guard shows the project path where the package was found.

Compare each version with the fixed releases: 10.6.22, 11.3.22, or 11.4.13, or later. A project on an earlier version needs the Composer update from [What to Do Now](https://www.stepsecurity.io/blog/fail2install-cve-2026-132165#what-to-do-now) and a new deployment. To check several packages at once, use **Advanced search** with the PHP ecosystem and the package names and versions you want to find.

### Confirm the update reached every project

Dev Machine Guard scans each machine every 4 hours by default. During the rollout, add a **temporary boost** in Dev Machine Guard **Settings** to scan more often, for example every 60 minutes until an end time you set. The change reaches your fleet on the next agent check-in, with no redeploy, and the regular schedule returns automatically. Schedules and boosts apply to machines running agent 1.15.0 or later. To check one machine right away, run the Dev Machine Guard script on it for an on-demand scan.

Then open `drupal/core` again. When its version list shows only fixed versions, every project checkout on your enrolled machines pins a fixed release. Each site still needs the new build deployed before it is protected.

## References

**Find every Drupal project and its core version across your developer machines. [Talk to the StepSecurity team](https://www.stepsecurity.io/contact) about [Dev Machine Guard](https://www.stepsecurity.io/dev-machine-guard).**
