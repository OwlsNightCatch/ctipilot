---
title: Apache HTTP Server 2.4.71 Fixes Critical mod_http2 Heap Corruption (CVE-2026-119618) — Patch Now
url: https://www.rescana.com/post/apache-httpd-mod-http2-cve-2026-119618-patch-now
hostname: rescana.com
description: Apache HTTP Server 2.4.71 (11 Nov 2026) fixes CVE-2026-119618 in mod_http2, rated critical by Apache, which can lead to RCE. Upgrade now. Not in CISA KEV.
sitename: Rescana
date: "2026-11-11"
categories: ['CVE Analysis Center']
fingerprint: "93114bd2ed667752"
---
The Apache HTTP Server Project released version 2.4.71 on 11 November 2026. Its [2.4 vulnerabilities page](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2026-119618) lists [CVE-2026-119618](https://www.cve.org/CVERecord?id=CVE-2026-119618) under "Fixed in Apache HTTP Server 2.4.71," "Released 2026-11-11," and Apache rates it "(critical)." Apache titles it "mod\_http2: heap corruption and RCE in assign\_headers" and describes it as: "Concurrent Execution using Shared Resource with Improper Synchronization vulnerability in Apache HTTP Server's mod\_http2 in assign\_headers() can lead to RCE."

Apache states: "This issue affects Apache HTTP Server: from 2.4.55 through 2.4.70." And: "Affected releases of mod\_h2 from GitHub: from 2.0.8 through 2.0.42." The [download page](https://httpd.apache.org/download.cgi) lists 2.4.71 as "the latest available version," and the [2.4.71 announcement](https://downloads.apache.org/httpd/Announcement2.4.txt), dated "November 11, 2026," calls it "recommended over all previous releases." Apache gives no clock time for the release.

Apache's advisory does not discuss exploitation, and this post makes no exploitation claim. CVE-2026-119618 is not in CISA KEV as of catalogVersion 2026.11.10, checked 11 November 2026 at 20:04 Asia/Jerusalem UTC+2.

## Technical Information

**CVE-2026-119618, rated critical by Apache.** The [CVE.org record](https://www.cve.org/CVERecord?id=CVE-2026-119618), published by the Apache CNA, repeats the title and description verbatim and lists CWE-362 ("Concurrent Execution using Shared Resource with Improper Synchronization"). Apache's description names the `assign_headers()` function in mod\_http2 and says the issue "can lead to RCE." Apache does not state attacker preconditions, such as whether authentication is required, and this post does not add any.

**Severity.** The vulnerabilities page heading reads "CVE-2026-119618 (critical)." Eric Covener's [oss-security advisory](https://www.openwall.com/lists/oss-security/2026/11/11/13) (11 November 2026, 14:19 Asia/Jerusalem UTC+2) opens with "Severity: critical," and the CVE.org record carries a textual severity of "critical." Apache published no CVSS vector or score, and NVD's entry is in "Received" status with no metrics. This post does not assign a CVSS score; its severity is Apache's rating.

**Credits and timeline.** Apache credits "Anthropic's OSS Scanner, as vulnerability ANT-2026-MAPKT6MZ" and "Anthony Weems and Simon Scannell of the Google Cloud Vulnerability Research." Its timeline shows reports on 2026-10-26 (Anthropic) and 2026-11-03 (Google), and "fixed in 2.4.x by 824beab9b9424d6cfb29595248fdbf6c3dddeab1" and "Update 2.4.71 released" on 2026-11-11. [CHANGES\_2.4.71](https://downloads.apache.org/httpd/CHANGES_2.4.71) carries the same title, description and ranges, with the Anthropic credit only; the oss-security timeline lists only the 26 October report. This post follows the vulnerabilities page.

**Other fixes in 2.4.71.** The same release also fixes [CVE-2026-106023](https://www.cve.org/CVERecord?id=CVE-2026-106023), which Apache rates "(important)" (mod\_md NULL pointer dereference, 2.4.30 through 2.4.70), and [CVE-2026-109163](https://www.cve.org/CVERecord?id=CVE-2026-109163), which Apache rates "(low)" (mod\_vhost\_alias, 2.4.69 and 2.4.70). Details are on Apache's page.

**Related, different issue.** CVE-2026-119618 is not CVE-2026-23918, the earlier mod\_http2 double-free fixed in 2.4.66 and covered in a [separate Rescana post](https://www.rescana.com/post/critical-apache-http-server-2-4-66-vulnerability-cve-2026-23918-http-2-mod-http2-double-free-enables-dos-and-remote-code). They are distinct bugs with different fixed releases.

## Affected and Fixed Releases

From Apache's 2.4 vulnerabilities page:

| Component | Affected, as Apache states it | Fix | 
|---|---|---|
| Apache HTTP Server | from 2.4.55 through 2.4.70 | 2.4.71, released 2026-11-11 | 
| mod\_h2 from GitHub | from 2.0.8 through 2.0.42 | No fixed mod\_h2 release is named yet | 

At the 20:04 Asia/Jerusalem UTC+2 check, the newest [icing/mod\_h2](https://github.com/icing/mod_h2/releases) release and tag was still v2.0.42 (29 May 2026), and the project's ChangeLog did not mention CVE-2026-119618. Operators of the standalone module should watch that project; this post does not name a fixed mod\_h2 version.

Distribution packages follow their own schedules. At the same check, the [Debian security tracker](https://security-tracker.debian.org/tracker/CVE-2026-119618) listed apache2 2.4.71-1 as fixed in unstable, with bookworm, trixie and forky still marked vulnerable. We found no Ubuntu or Red Hat CVE page yet.

## Exploitation Status

Apache's vulnerabilities page, the oss-security advisory, the 2.4.71 announcement, CHANGES\_2.4.71, the CVE.org record and the NVD entry do not discuss exploitation, known attacks or proof-of-concept code. CVE-2026-119618 was not in CISA KEV at the 20:04 check (catalogVersion 2026.11.10, dateReleased 21:03 Asia/Jerusalem UTC+2 on 10 November). This post makes no exploitation claim.

## Workaround and Mitigation

Apache has published no workaround for CVE-2026-119618. Its remediation is to upgrade to Apache HTTP Server 2.4.71 from the [official download page](https://httpd.apache.org/download.cgi).

As Rescana's general hardening advice, not an Apache fix or workaround: keep enabled protocols and modules to those a service needs. This does not replace the upgrade.

## Indicators of Compromise

Apache has published no indicators of compromise or detection guidance for CVE-2026-119618, and this post does not supply any.

## What to Ask Your Vendors Today

Apache HTTP Server fronts many vendor-run websites and applications, including services that handle your data. Ask suppliers that operate httpd for you, in writing. These are questions about the vendor's own posture, not Apache guidance:

- Whether their internet-facing Apache HTTP Server instances are on 2.4.71, and which version each was on before.
- For any instance not yet upgraded, the patch ETA, and whether they have taken any interim steps of their own, such as HTTP/2 disabled until the upgrade. Apache does not list this as a mitigation.
- Whether any service uses the standalone mod\_h2 module from GitHub (2.0.8 through 2.0.42), and their plan for it.
- How they will tell you if they find signs of compromise.

If you operate Apache HTTP Server yourself, upgrade to 2.4.71 first, then check the same points against your own inventory.

If your team needs help reviewing which suppliers front you with Apache HTTP Server and whether those fleets are on 2.4.71, [Talk to an expert](https://www.rescana.com/under-attack?utm_source=rescana&utm_medium=advisory&utm_campaign=under-attack&utm_content=apache-httpd-mod-http2-cve-2026-119618-patch-now).

## Sources

- [Apache HTTP Server 2.4 vulnerabilities](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2026-119618), Apache HTTP Server Project. Primary source for the rating, description, affected ranges, credits, timeline and fixed release. Rechecked 11 November 2026 at 20:04 Asia/Jerusalem UTC+2.
- [Download Apache HTTP Server](https://httpd.apache.org/download.cgi), [Announcement2.4.txt](https://downloads.apache.org/httpd/Announcement2.4.txt) and [CHANGES\_2.4.71](https://downloads.apache.org/httpd/CHANGES_2.4.71), Apache HTTP Server Project, 11 November 2026. Source tarballs [httpd-2.4.71.tar.gz](https://dlcdn.apache.org/httpd/httpd-2.4.71.tar.gz) and [httpd-2.4.71.tar.bz2](https://dlcdn.apache.org/httpd/httpd-2.4.71.tar.bz2) were available at the same check.
- [CVE-2026-119618: Apache HTTP Server: mod\_http2: heap corruption and RCE in assign\_headers](https://www.openwall.com/lists/oss-security/2026/11/11/13), Eric Covener, oss-security, 11 November 2026.
- [CVE-2026-119618](https://www.cve.org/CVERecord?id=CVE-2026-119618) on CVE.org (Apache CNA; textual severity "critical"; CWE-362; no CVSS) and [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119618) (Received, no metrics), checked at 20:04 Asia/Jerusalem UTC+2.
- [icing/mod\_h2 releases](https://github.com/icing/mod_h2/releases) — newest release v2.0.42 at the 20:04 check.
- [Debian security tracker: CVE-2026-119618](https://security-tracker.debian.org/tracker/CVE-2026-119618), checked at 20:04 Asia/Jerusalem UTC+2.
- [CISA catalog JSON feed](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) — catalogVersion 2026.11.10, dateReleased 2026-11-10T19:03:29Z; CVE-2026-119618 is not in CISA KEV as of 11 November 2026 at 20:04 Asia/Jerusalem UTC+2.
- [Earlier Rescana post on CVE-2026-23918](https://www.rescana.com/post/critical-apache-http-server-2-4-66-vulnerability-cve-2026-23918-http-2-mod-http2-double-free-enables-dos-and-remote-code) — a different mod\_http2 issue, linked as related context.
