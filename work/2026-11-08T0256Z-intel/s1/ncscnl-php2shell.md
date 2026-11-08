---
title: "GitHub - NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities"
url: https://github.com/NCSC-NL/php2shell
hostname: github.com
description: Operational information regarding the 2026 php2shell vulnerabilities - NCSC-NL/php2shell
sitename: GitHub
date: "2026-11-04"
categories: ['repository:1428216799']
fingerprint: b556084084d713f3
---
Operational information: 28 October 2026 16:46 CET

Software list last status update: 4 November 2026 08:15 CET

This repository contains operational information regarding the critical PHP vulnerabilities tracked by CERT-EU as CVE-2026-109618 and CVE-2026-109619.

PHP is a widely used open-source server-side scripting language, so these vulnerabilities may affect a broad range of internet-facing web applications and products that embed or depend on PHP.

This repository tracks **948 products**, including **215 vulnerable** and **185 fixed**.

On 21 October 2026, PHP published fixed releases for CVE-2026-109618 and CVE-2026-109619: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. PHP states that both vulnerabilities can allow unauthenticated remote code execution and that all PHP installations serving web requests are at risk, including PHP-FPM, Apache with mod\_php, php-cgi, FrankenPHP and LiteSpeed. PHP considers the risk highest for mod\_php, where an unauthenticated request can trigger exploitation before application code runs.

PHP describes CVE-2026-109618 as remote code execution via out-of-memory corruption during request cleanup, and CVE-2026-109619 as remote code execution via stale request-owned global state reused by a later request on the same worker. PHP 8.1 and older are no longer supported by the PHP project; distributions and LTS vendors may provide backported packages, and PHP has published minimal source backports for PHP 7.4, 8.0 and 8.1.

On 23 October 2026, PHP published an [informational advisory](https://www.php.net/archive/2026.php#2026-10-23-1) suggesting `session.upload_progress.enabled=0` until the next regular bugfix release to fully protect from an unlikely RCE vector (CVE-2026-115560). PHP will publish a full advisory with the next release; this repository does not track CVE-2026-115560 separately in the software list.

The impact is not limited to websites: PHP is also embedded in appliances, network devices, management interfaces and other vendor products where administrators may not be able to update PHP directly.

- Identify PHP-based applications and their runtime versions, with priority on internet-facing systems and web-serving SAPIs.
- Update to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or apply vendor-provided backported packages.
- After updating, keep `session.upload_progress.enabled=0` until the next regular PHP bugfix release (PHP informational advisory of 23 October 2026, CVE-2026-115560), unless your application needs the feature and never changes `session.serialize_handler` at runtime.
- Check third-party images, appliances and embedded runtimes separately; for products that bundle PHP, apply vendor updates as soon as they become available.
- If immediate patching is not possible, follow PHP's temporary mitigations, including disabling `session.upload_progress`, restarting workers, and reviewing the official `memory_limit`, `post_max_size` and PHP 8.5 `fatal_error_backtraces` guidance. PHP states that these measures are not complete fixes.
- Monitor vendor advisories, internet-facing logs, and public exploit activity.

For additional information see:

| Directory | Purpose | 
|---|---|
| [detection\_mitigation](https://github.com/NCSC-NL/php2shell/blob/main/detection_mitigation) | Contains detection and mitigation material for the vulnerabilities. | 
| [software](https://github.com/NCSC-NL/php2shell/blob/main/software) | Contains inventory lists of software products with a PHP dependency potentially affected by the vulnerabilities. | 
| [tools](https://github.com/NCSC-NL/php2shell/blob/main/tools) | Contains tools for using/generating files within this repo | 
| [Community contributions](https://github.com/NCSC-NL/php2shell/blob/main/COMMUNITY_CONTRIBUTIONS.MD) | Community tools, tips, guides, and reference resources. | 

The repository is being updated as the situation develops. Check back for updates.

Statistics as of **2026-11-04 (UTC)**, from the current SPDX inventory.

| Products tracked | Fixed | Vulnerable | Under investigation | Runtime-dependent | Not affected | Unassessed / unknown | 
|---|---|---|---|---|---|---|
| 948 | 185 | 215 | 93 | 240 | 214 | 1 | 

[Counts by update day and per-CVE statistics (JSON)](https://github.com/NCSC-NL/php2shell/blob/main/software/statistics/inventory-statistics.json) | [Software list](https://github.com/NCSC-NL/php2shell/blob/main/software/software_list.md)

| Date and time | Supplier | Product | Version (see Status) | Status CVE-2026-109618 / CVE-2026-109619 | Links | 
|---|---|---|---|---|---|
| 2026-11-04 08:15:46 +0100 | Centreon | Centreon Cloud hosted service (patched PHP rollout) | Cloud rollout confirmed 2026-10-22; service build unspecified | Fix | [source](https://thewatch.centreon.com/latest-security-bulletins-64/php-security-advisory-action-required-for-centreon-on-premise-installations-6010?postid=20972) | 
| 2026-11-04 08:15:46 +0100 | EGroupware GmbH / EGroupware project | EGroupware Cloud hosted service (patched PHP rollout) | Hosted service rollout completed 2026-10-21; vendor confirmation updated 2026-10-27 | Fix | [source](https://www.egroupware.org/en/general/php2shell-and-our-strategy) | 
| 2026-11-04 08:15:46 +0100 | EGroupware GmbH / EGroupware project | EGroupware official Docker images with patched PHP | 26.10.20261021 and 23.1.20261021; PHP 8.5.12 | Fix | [source 1](https://www.egroupware.org/en/general/php2shell-and-our-strategy) [source 2](https://github.com/EGroupware/egroupware/releases/tag/26.10.20261021) [source 3](https://github.com/EGroupware/egroupware/releases/tag/23.1.20261021) | 
| 2026-11-04 08:15:46 +0100 | Grokability / Snipe-IT project | Snipe-IT hosted service (patched PHP rollout) | Vendor-confirmed patched hosted fleet, October 2026; service build unspecified | Fix | [source](https://grokstar.dev/security/2026/10/critical-php-security-update-php2shell/) | 
| 2026-11-04 08:15:46 +0100 | Grokability / Snipe-IT project | Snipe-IT official Ubuntu and Alpine Docker images with patched PHP | snipe/snipe-it:v8.8.2 (Ubuntu); snipe/snipe-it:v8.8.3-alpine | Fix | [source 1](https://grokstar.dev/security/2026/10/critical-php-security-update-php2shell/) [source 2](https://github.com/grokability/snipe-it/releases/tag/v8.8.3) [source 3](https://hub.docker.com/v2/repositories/snipe/snipe-it/tags/v8.8.3-alpine) [source 4](https://hub.docker.com/v2/repositories/snipe/snipe-it/tags/v8.8.2) | 

See the [full software status update history](https://github.com/NCSC-NL/php2shell/blob/main/software/changelog_software_list.md).

If you have any additional information to share relevant to these PHP vulnerabilities, feel free to open a Pull request. New to this? [Read how to contribute in GitHub's documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository).

For updates to the software list: our strong preference is to receive edits in the SPDX source files in `software/spdx/`. The Markdown list pages are generated automatically from those files. In case this proves too difficult: don't worry. We'll attempt to backport edits in the .md files to the SPDX source files, but without any guarantees.

For a list of other contributions made by our community, see [Community contributions](https://github.com/NCSC-NL/php2shell/blob/main/COMMUNITY_CONTRIBUTIONS.MD).
