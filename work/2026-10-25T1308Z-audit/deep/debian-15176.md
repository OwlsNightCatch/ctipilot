# extract: served via trafilatura-direct
---
title: CVE-2026-15176
url: https://security-tracker.debian.org/tracker/CVE-2026-15176
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: f8b83ddff2e7c682
---
| **Name** | CVE-2026-15176 | 
| **Description** | A vulnerability exists in NGINX Plus and NGINX Open Source when a location is configured that uses the alias directive together with rewrite and a set or return directive referencing the $request\_filename variable. Alternatively, the same result could be achieved when the $request\_filename variable is used in an access log format directive. An unauthenticated attacker along with conditions beyond their control can exploit this vulnerability by sending crafted HTTP requests. This may cause a heap buffer overflow in the NGINX worker process leading to a restart. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.  Impact: This vulnerability may allow remote attackers to cause a denial-of-service (DoS) on the NGINX system or to possibly trigger a code execution. There is no control plane exposure; this is a data plane issue only.     Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated. | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-15176) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-15176); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-15176), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-15176), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-15176), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-15176), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-15176), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-15176), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-15176), [Ubuntu](https://ubuntu.com/security/CVE-2026-15176), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-15176), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-15176)/[CVE](https://www.suse.com/security/cve/CVE-2026-15176/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-15176)/[code](https://github.com/search?type=Code&q=%22CVE-2026-15176%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-15176%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-15176%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DSA-6575-1](https://security-tracker.debian.org/tracker/DSA-6575-1) | 

The table below lists information on source packages.

The information below is based on the following data on fixed versions.
