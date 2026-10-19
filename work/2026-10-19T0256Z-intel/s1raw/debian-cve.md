---
title: CVE-2026-99999
url: https://security-tracker.debian.org/tracker/CVE-2026-99999
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: d4b3509f9bed7696
---
| **Name** | CVE-2026-99999 | 
| **Description** | In the Linux kernel, the following vulnerability has been resolved:  ipv4: validate checksum\_start before completing checksum  If a packet with bad checksum metadata gets into the ipv4 stack, skb\_checksum\_help can corrupt the network header and cause a bunch of mischief.  This was discovered and reported by Paulos, and has been reporoduced by others independently since.  We really shouldn't allow such packets in, but as a defence in depth measure, let's also check before we complete the checksum.  A more complete validation at input is forthcoming, but needs more work. | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-99999) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-99999); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-99999), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-99999), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-99999), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-99999), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-99999), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-99999), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-99999), [Ubuntu](https://ubuntu.com/security/CVE-2026-99999), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-99999), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-99999)/[CVE](https://www.suse.com/security/cve/CVE-2026-99999/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-99999)/[code](https://github.com/search?type=Code&q=%22CVE-2026-99999%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-99999%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-99999%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DLA-4841-1](https://security-tracker.debian.org/tracker/DLA-4841-1), [DSA-6568-1](https://security-tracker.debian.org/tracker/DSA-6568-1) | 

The table below lists information on source packages.

The information below is based on the following data on fixed versions.
