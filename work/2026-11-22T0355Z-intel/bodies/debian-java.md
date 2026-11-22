---
title: CVE-2026-114938
url: https://security-tracker.debian.org/tracker/CVE-2026-114938
hostname: debian.org
sitename: security-tracker.debian.org
date: "2020-03-21"
fingerprint: "47d1769b93dea53b"
---
| **Name** | CVE-2026-114938 | 
| **Description** | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java SE (component: Compiler). Supported versions that are affected are Oracle Java SE: 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3. Difficult to exploit vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. Successful attacks of this vulnerability can result in takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition. Note: This vulnerability can only be exploited by supplying data to APIs in the specified Component without using Untrusted Java Web Start applications or Untrusted Java applets, such as through a web service. CVSS 3.1 Base Score 8.1 (Confidentiality, Integrity and Availability impacts). CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H). | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-114938) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114938); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-114938), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-114938), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-114938), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-114938), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-114938), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-114938), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-114938), [Ubuntu](https://ubuntu.com/security/CVE-2026-114938), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-114938), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-114938)/[CVE](https://www.suse.com/security/cve/CVE-2026-114938/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-114938)/[code](https://github.com/search?type=Code&q=%22CVE-2026-114938%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-114938%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-114938%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DLA-4917-1](https://security-tracker.debian.org/tracker/DLA-4917-1), [DSA-6639-1](https://security-tracker.debian.org/tracker/DSA-6639-1), [DSA-6640-1](https://security-tracker.debian.org/tracker/DSA-6640-1) | 

The table below lists information on source packages.

| Source Package | Release | Version | Status | 
|---|---|---|---|
| [openjdk-17](https://security-tracker.debian.org/tracker/source-package/openjdk-17) ([PTS](https://tracker.debian.org/pkg/openjdk-17)) | bookworm | 17.0.19+10-1\~deb12u2 | vulnerable | 
|  | bookworm (security) | 17.0.21.1+2-1\~deb12u1 | fixed | 
|  | sid | 17.0.21.1+2-1 | fixed | 
| [openjdk-21](https://security-tracker.debian.org/tracker/source-package/openjdk-21) ([PTS](https://tracker.debian.org/pkg/openjdk-21)) | trixie | 21.0.13+9-1\~deb13u2 | vulnerable | 
|  | trixie (security) | 21.0.13.1+2-1\~deb13u1 | fixed | 
|  | forky | 21.0.13.0.3+1-1 | vulnerable | 
|  | sid | 21.0.13.1+2-1 | fixed | 
| [openjdk-25](https://security-tracker.debian.org/tracker/source-package/openjdk-25) ([PTS](https://tracker.debian.org/pkg/openjdk-25)) | trixie | 25.0.5+8-1\~deb13u1 | vulnerable | 
|  | trixie (security) | 25.0.5.1+2-1\~deb13u1 | fixed | 
|  | forky | 25.0.5+8-1 | vulnerable | 
|  | sid | 25.0.5.1+2-1 | fixed | 
| [openjdk-27](https://security-tracker.debian.org/tracker/source-package/openjdk-27) ([PTS](https://tracker.debian.org/pkg/openjdk-27)) | sid | 27.0.1.1+4-1 | fixed | 

The information below is based on the following data on fixed versions.

| Package | Type | Release | Fixed Version | Urgency | Origin | Debian Bugs | 
|---|---|---|---|---|---|---|
| [openjdk-17](https://security-tracker.debian.org/tracker/source-package/openjdk-17) | source | bookworm | 17.0.21.1+2-1\~deb12u1 |  | [DLA-4917-1](https://security-tracker.debian.org/tracker/DLA-4917-1) |  | 
| [openjdk-17](https://security-tracker.debian.org/tracker/source-package/openjdk-17) | source | (unstable) | 17.0.21.1+2-1 |  |  |  | 
| [openjdk-21](https://security-tracker.debian.org/tracker/source-package/openjdk-21) | source | trixie | 21.0.13.1+2-1\~deb13u1 |  | [DSA-6639-1](https://security-tracker.debian.org/tracker/DSA-6639-1) |  | 
| [openjdk-21](https://security-tracker.debian.org/tracker/source-package/openjdk-21) | source | (unstable) | 21.0.13.1+2-1 |  |  |  | 
| [openjdk-25](https://security-tracker.debian.org/tracker/source-package/openjdk-25) | source | trixie | 25.0.5.1+2-1\~deb13u1 |  | [DSA-6640-1](https://security-tracker.debian.org/tracker/DSA-6640-1) |  | 
| [openjdk-25](https://security-tracker.debian.org/tracker/source-package/openjdk-25) | source | (unstable) | 25.0.5.1+2-1 |  |  |  | 
| [openjdk-27](https://security-tracker.debian.org/tracker/source-package/openjdk-27) | source | (unstable) | 27.0.1.1+4-1 |  |  |  | 

[https://openjdk.org/groups/vulnerability/advisories/2026-11-17](https://openjdk.org/groups/vulnerability/advisories/2026-11-17)

[https://calif.io/java4shell](https://calif.io/java4shell)
