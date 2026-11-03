# extract: served via trafilatura-direct
---
title: CVE-2026-98432
url: https://security-tracker.debian.org/tracker/CVE-2026-98432
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: e5a379df9ae8ca97
---
| **Name** | CVE-2026-98432 | 
| **Description** | In the Linux kernel, the following vulnerability has been resolved: ipv4: free inet\_opt and ireq\_opt after an RCU grace period tcp\_v4\_syn\_recv\_sock() transfers ownership of ireq->ireq\_opt to the child socket (newinet->inet\_opt) without copying it. Another cpu can concurrently process a retransmitted SYN for the same request socket, and send a SYNACK from tcp\_check\_req(). tcp\_v4\_send\_synack() and inet\_csk\_route\_req() read ireq->ireq\_opt under rcu\_read\_lock() only, and ip\_build\_and\_send\_pkt() and ip\_options\_build() then read opt->optlen twice. Note that the SYNACK timer itself is not an issue: it holds a reference on its request socket, and inet\_csk\_reqsk\_queue\_drop() calls timer\_delete\_sync() before the child can be freed. Since commit 079096f103fa ("tcp/dccp: install syn\_recv requests into ehash table"), request sockets are processed without holding the listener lock, so nothing prevents the child socket from being freed while the SYNACK is still being built. TCP child sockets do not have SOCK\_RCU\_FREE, and inet\_sock\_destruct() frees inet\_opt with a plain kfree(), leading to a use-after-free in ip\_options\_build(). A similar issue exists with request socket migration (net.ipv4.tcp\_migrate\_req=1, or a BPF\_SK\_REUSEPORT\_SELECT\_OR\_MIGRATE program). reqsk\_timer\_handler() clones the request socket with inet\_reqsk\_clone(), so that the old request socket and its clone share the same ireq\_opt, then reqsk\_migrate\_reset() clears the pointer in the old one. Another cpu holding a reference on the old request socket can still be using these options (sending a SYNACK, or creating a child in tcp\_v4\_syn\_recv\_sock()) when the clone is freed, and tcp\_v4\_reqsk\_destructor() also uses a plain kfree(). Readers already use RCU, and other paths replacing inet\_opt (do\_ip\_setsockopt(), cipso\_v4\_sock\_setattr()...) already use kfree\_rcu(). Use kfree\_rcu() in inet\_sock\_destruct() and tcp\_v4\_reqsk\_destructor() as well. IPv6 is not affected by the first issue, because tcp\_v6\_syn\_recv\_sock() duplicates the options. tcp\_v6\_reqsk\_destructor() has the same migration issue with ipv6\_opt, which is only set by CALIPSO. This will be addressed in a separate patch. | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-98432) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-98432); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-98432), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-98432), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-98432), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-98432), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-98432), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-98432), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-98432), [Ubuntu](https://ubuntu.com/security/CVE-2026-98432), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-98432), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-98432)/[CVE](https://www.suse.com/security/cve/CVE-2026-98432/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-98432)/[code](https://github.com/search?type=Code&q=%22CVE-2026-98432%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-98432%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-98432%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DLA-4841-1](https://security-tracker.debian.org/tracker/DLA-4841-1), [DLA-4850-1](https://security-tracker.debian.org/tracker/DLA-4850-1), [DSA-6568-1](https://security-tracker.debian.org/tracker/DSA-6568-1) | 

The table below lists information on source packages.

| Source Package | Release | Version | Status | 
|---|---|---|---|
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) ([PTS](https://tracker.debian.org/pkg/linux)) | bookworm | 6.1.176-1 | vulnerable | 
|  | bookworm (security) | 6.1.190-1 | fixed | 
|  | trixie | 6.12.107-1 | vulnerable | 
|  | trixie (security) | 6.12.115-2 | fixed | 
|  | forky | 7.2.12-1 | fixed | 
|  | sid | 7.2.15-1 | fixed | 
| [linux-6.12](https://security-tracker.debian.org/tracker/source-package/linux-6.12) ([PTS](https://tracker.debian.org/pkg/linux-6.12)) | bookworm (security) | 6.12.113-1\~deb12u1 | fixed | 

The information below is based on the following data on fixed versions.

| Package | Type | Release | Fixed Version | Urgency | Origin | Debian Bugs | 
|---|---|---|---|---|---|---|
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) | source | bookworm | 6.1.190-1 |  | [DLA-4841-1](https://security-tracker.debian.org/tracker/DLA-4841-1) |  | 
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) | source | trixie | 6.12.113-1 |  | [DSA-6568-1](https://security-tracker.debian.org/tracker/DSA-6568-1) |  | 
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) | source | (unstable) | 7.2.10-1 |  |  |  | 
| [linux-6.12](https://security-tracker.debian.org/tracker/source-package/linux-6.12) | source | bookworm | 6.12.113-1\~deb12u1 |  | [DLA-4850-1](https://security-tracker.debian.org/tracker/DLA-4850-1) |  | 

[https://git.kernel.org/linus/e3f33b0a1d89d738e2b913dab519226eaf76e15b](https://git.kernel.org/linus/e3f33b0a1d89d738e2b913dab519226eaf76e15b) (7.3-rc7)
