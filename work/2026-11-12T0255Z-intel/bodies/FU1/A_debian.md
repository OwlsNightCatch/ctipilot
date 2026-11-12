---
title: CVE-2026-119618
url: https://security-tracker.debian.org/tracker/CVE-2026-119618
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: "4eb77be690eda792"
---
| **Name** | CVE-2026-119618 | 
| **Description** | Concurrent Execution using Shared Resource with Improper Synchronizati ... | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-119618) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119618); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-119618), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-119618), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-119618), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-119618), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-119618), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-119618), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-119618), [Ubuntu](https://ubuntu.com/security/CVE-2026-119618), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-119618), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-119618)/[CVE](https://www.suse.com/security/cve/CVE-2026-119618/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-119618)/[code](https://github.com/search?type=Code&q=%22CVE-2026-119618%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-119618%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-119618%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **Debian Bugs** | [1153732](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1153732) | 

## Vulnerable and fixed packages

The table below lists information on source packages.

| Source Package | Release | Version | Status | 
|---|---|---|---|
| [apache2](https://security-tracker.debian.org/tracker/source-package/apache2) ([PTS](https://tracker.debian.org/pkg/apache2)) | bookworm | 2.4.68-1\~deb12u1 | vulnerable | 
|  | bookworm (security) | 2.4.67-1\~deb12u3 | vulnerable | 
|  | trixie | 2.4.68-1\~deb13u1 | vulnerable | 
|  | trixie (security) | 2.4.69-1\~deb13u1 | vulnerable | 
|  | forky | 2.4.69-1 | vulnerable | 
|  | sid | 2.4.71-1 | fixed | 

The information below is based on the following data on fixed versions.

| Package | Type | Release | Fixed Version | Urgency | Origin | Debian Bugs | 
|---|---|---|---|---|---|---|
| [apache2](https://security-tracker.debian.org/tracker/source-package/apache2) | source | (unstable) | 2.4.71-1 |  |  | [1153732](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1153732) | 

## Notes

[https://httpd.apache.org/security/vulnerabilities\_24.html#CVE-2026-119618](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2026-119618)

Fixed by: [https://github.com/apache/httpd/commit/824beab9b9424d6cfb29595248fdbf6c3dddeab1](https://github.com/apache/httpd/commit/824beab9b9424d6cfb29595248fdbf6c3dddeab1) (2.4.71)
