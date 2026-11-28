---
title: CVE-2026-123007
url: https://security-tracker.debian.org/tracker/CVE-2026-123007
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: b2f6794fc6b3f58e
filedate: "2026-11-28"
---
| **Name** | CVE-2026-123007 | 
| **Description** | This issue affects NGINX Plus or NGINX Open Source configurations that use HTTP/2. When NGINX processes undisclosed traffic, the flow control window can exceed the allowed threshold, potentially resulting in a heap buffer overflow typically followed by an NGINX worker segmentation fault. Additionally, attackers can execute code on systems with Address Space Layout Randomization (ASLR) disabled or when the attacker can bypass ASLR.  Impact: An attacker could leverage this vulnerability to crash the NGINX worker process, corrupt its memory, or potentially execute code remotely. There is no control plane exposure; this is a data plane issue only.    Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated. | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-123007) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123007); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-123007), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-123007), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-123007), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-123007), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-123007), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-123007), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-123007), [Ubuntu](https://ubuntu.com/security/CVE-2026-123007), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-123007), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-123007)/[CVE](https://www.suse.com/security/cve/CVE-2026-123007/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-123007)/[code](https://github.com/search?type=Code&q=%22CVE-2026-123007%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-123007%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-123007%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DLA-4918-1](https://security-tracker.debian.org/tracker/DLA-4918-1), [DSA-6642-1](https://security-tracker.debian.org/tracker/DSA-6642-1) | 

The table below lists information on source packages.

The information below is based on the following data on fixed versions.
