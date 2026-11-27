---
title: CVE-2026-99362
url: https://security-tracker.debian.org/tracker/CVE-2026-99362
hostname: debian.org
sitename: security-tracker.debian.org
date: "2026-01-01"
fingerprint: "60b27b1f86e1cf9e"
filedate: "2026-11-27"
---
| **Name** | CVE-2026-99362 | 
| **Description** | In the Linux kernel, the following vulnerability has been resolved: nfsd: preflight SEQUENCE replies before accepting a slot nfsd4\_sequence() narrows the reply buffer to the session's cached reply limit before it accepts the slot seqid. A client may negotiate ca\_maxresponsesize\_cached down to NFSD\_MIN\_HDR\_SEQ\_SZ, and nfsd4\_alloc\_slot() then gives every slot a zero-length sl\_data\[\]. A COMPOUND tag can fill that narrowed buffer until it holds the SEQUENCE opcode but not the status word that follows. nfsd4\_encode\_operation() returns without running nfsd4\_encode\_sequence(), so cstate.data\_offset stays zero. It leaves op->status at nfs\_ok as well, so the COMPOUND is treated as having succeeded. nfsd4\_store\_cache\_entry() declines to cache a lone SEQUENCE that returned an error. That test reads the status the operation reported, so it passes here. The copy starts at offset zero and takes the whole reply, RPC and COMPOUND headers included, into the zero-length sl\_data\[\]. The COMPOUND tag is copied along with it, so the client picks most of the bytes written past the end of the slot: BUG: KASAN: slab-out-of-bounds in read\_bytes\_from\_xdr\_buf+0x1bc/0x390 Write of size 80 at addr ffff888003a549cd by task kunit\_try\_catch/24 \_\_asan\_memcpy+0x38/0x60 read\_bytes\_from\_xdr\_buf+0x1bc/0x390 nfsd4\_sequence\_done+0x5b0/0x810 nfs4svc\_encode\_compoundres+0x1bf/0x240 Check that the fixed-size SEQUENCE result, plus room for a following operation's error status, fits the negotiated limit before narrowing the buffer and consuming the slot seqid. The slot and its reply cache are left unchanged, as RFC 8881 Section 2.10.6.1.2 requires of an error returned from SEQUENCE. | 
| **Source** | [CVE](https://www.cve.org/CVERecord?id=CVE-2026-99362) (at [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-99362); [CERT](https://www.kb.cert.org/vuls/byid?searchview=&query=CVE-2026-99362), [ENISA](https://euvd.enisa.europa.eu/vulnerability/CVE-2026-99362), [LWN](https://lwn.net/Search/DoSearch?words=CVE-2026-99362), [oss-sec](https://marc.info/?l=oss-security&s=CVE-2026-99362), [fulldisc](https://marc.info/?l=full-disclosure&s=CVE-2026-99362), [Debian ELTS](https://deb.freexian.com/extended-lts/tracker/CVE-2026-99362), [Red Hat](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2026-99362), [Ubuntu](https://ubuntu.com/security/CVE-2026-99362), [Gentoo](https://bugs.gentoo.org/show_bug.cgi?id=CVE-2026-99362), SUSE [bugzilla](https://bugzilla.suse.com/show_bug.cgi?id=CVE-2026-99362)/[CVE](https://www.suse.com/security/cve/CVE-2026-99362/), GitHub [advisories](https://github.com/advisories?query=CVE-2026-99362)/[code](https://github.com/search?type=Code&q=%22CVE-2026-99362%22)/[issues](https://github.com/search?type=Issues&q=%22CVE-2026-99362%22), [web search](https://duckduckgo.com/html?q=%22CVE-2026-99362%22), [more](https://oss-security.openwall.org/wiki/vendors)) | 
| **References** | [DLA-4927-1](https://security-tracker.debian.org/tracker/DLA-4927-1) | 

The table below lists information on source packages.

| Source Package | Release | Version | Status | 
|---|---|---|---|
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) ([PTS](https://tracker.debian.org/pkg/linux)) | bookworm | 6.1.176-1 | vulnerable | 
|  | bookworm (security) | 6.1.192-3 | vulnerable | 
|  | trixie | 6.12.117-1 | fixed | 
|  | trixie (security) | 6.12.118-1 | fixed | 
|  | forky | 7.3.5-1 | fixed | 
|  | sid | 7.3.6-1 | fixed | 
| [linux-6.12](https://security-tracker.debian.org/tracker/source-package/linux-6.12) ([PTS](https://tracker.debian.org/pkg/linux-6.12)) | bookworm (security) | 6.12.117-1\~deb12u1 | fixed | 

The information below is based on the following data on fixed versions.

| Package | Type | Release | Fixed Version | Urgency | Origin | Debian Bugs | 
|---|---|---|---|---|---|---|
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) | source | trixie | 6.12.117-1 |  |  |  | 
| [linux](https://security-tracker.debian.org/tracker/source-package/linux) | source | (unstable) | 7.3.3-1 |  |  |  | 
| [linux-6.12](https://security-tracker.debian.org/tracker/source-package/linux-6.12) | source | bookworm | 6.12.117-1\~deb12u1 |  | [DLA-4927-1](https://security-tracker.debian.org/tracker/DLA-4927-1) |  | 

[https://git.kernel.org/linus/35ff1a7a7e3835c3e974bc5c45d335897564ceae](https://git.kernel.org/linus/35ff1a7a7e3835c3e974bc5c45d335897564ceae) (7.4-rc1)

[https://opensec.in/blog/nfs2root-cve-2026-99362](https://opensec.in/blog/nfs2root-cve-2026-99362)
