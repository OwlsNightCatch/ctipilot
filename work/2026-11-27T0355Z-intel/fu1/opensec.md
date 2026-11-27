Title: NFS2ROOT: a 12-year-old pre-auth remote root in the Linux kernel's NFS server

URL Source: https://opensec.in/blog/nfs2root-cve-2026-99362

Published Time: 2026-11-25T19:52:40.114+00:00

Markdown Content:
Port 2049 sits open on file servers, NAS appliances, build farms and Kubernetes storage nodes. Since 2014, the Linux kernel listening on it has let anyone who can reach it write into kernel memory before logging in. We pointed OpenSec's Antara at it. It came back with a root shell.

Advisory[CVE-2026-99362](https://www.cve.org/CVERecord?id=CVE-2026-99362)critical CVSS 9.8

Pre-auth heap overflow in the Linux NFS server (nfsd)

Fixed in Linux 6.12.117, 6.18.61, 7.3.2 and 7.4-rc1. Update the kernel and reboot.

What you need to know

*   **What:** a pre-auth heap overflow in the kernel's NFS server, `nfsd`.
*   **Who:** any Linux host serving NFSv4.1 or 4.2 (the default) on a reachable tcp/2049.
*   **Impact:** one TCP connection writes 61 bytes past a kernel heap object; chained, that gives a root shell.
*   **Now:** patch and reboot. Until then, firewall tcp/2049.

Key facts

*   **Severity** 9.8 Critical (AV:N/AC:L/PR:N/UI:N)
*   **Attack** Remote, unauthenticated, tcp/2049
*   **Impact** Kernel heap overflow → remote root shell
*   **Bug age** 12 years, since Linux 3.16 (2014)
*   **Affected** In-kernel nfsd with NFSv4.1 or 4.2
*   **Fixed in** 6.12.117 · 6.18.61 · 7.3.2 · 7.4-rc1

## One connection, no login

The NFS server runs inside the kernel and parses network input before it knows who you are. CVE-2026-99362 lives in that gap: a client can shrink its reply cache to zero bytes, then make the server copy a full reply into it. The copy lands on the kernel heap, and the client picks most of the bytes.

How NFS2ROOT reaches a Linux NFS server: one unauthenticated TCP connection to port 2049

## Twelve years in a few lines of C

Timeline

1.   Mar 2014
Commit `47ee52986472` narrows the reply buffer while handling `SEQUENCE`. It ships in Linux 3.16.

2.   2014 to 2026
12 years Every kernel since 3.16 carries it: LTS, distribution and appliance kernels.

3.   17 Aug 2026
Jérémy Jean of ANSSI sends a fix upstream with a KASAN report.

4.   21 Sep 2026
OpenSec's Antara flags the bug, scores it 9.8 and turns it into a root shell on its own.

5.   20 Nov 2026
CVE-2026-99362 is published with fixes.

## Watch it run

A real run, end to end. Left: the victim's console. Right: our client on another machine, talking to the victim only over tcp/2049.

NFS2ROOT recording: an unauthenticated client gets a root shell on a Linux NFS server

The overflow. The kernel warns in `nfsd4_check_resp_size`, but the out-of-bounds copy has already happened.

Root. The attacker hangs up, and the victim's kernel runs our command: `root`, then `uid=0(root)`, then power-off.

## Root cause

Each NFSv4.1 session slot caches its last reply, so a retried request is answered exactly once. The client decides how big that cache is.

Set it to the minimum and every slot's buffer is zero bytes. `nfsd4_sequence()` then shrinks the reply buffer to that limit _before_ it accepts the slot. Pad the request's tag so the buffer fills right after the `SEQUENCE` opcode, and the encoder quits without flagging an error. The server believes `SEQUENCE` succeeded and caches the whole reply, headers and tag included, into a buffer with room for nothing.

KASAN report from the upstream fix text

```
BUG: KASAN: slab-out-of-bounds in read_bytes_from_xdr_buf+0x1bc/0x390
Write of size 80 at addr ffff888003a549cd
 __asan_memcpy+0x38/0x60
 read_bytes_from_xdr_buf+0x1bc/0x390
 nfsd4_sequence_done+0x5b0/0x810
 nfs4svc_encode_compoundres+0x1bf/0x240
```

That is 80 bytes copied, 61 of them past the end of the heap object, 40 of them chosen by the client.

Inside NFS2ROOT: the reply is copied into a slot buffer with no room for it.

The fix checks that the reply fits before taking the slot, and makes the encoder report what it can't fit.

## From overflow to root

The exploit stays private. Each step is an ordinary NFS request:

1.   **Overflow**
The write corrupts the neighbouring slot's bookkeeping.

2.   **Leak**
A replay request returns 3.8 KB of kernel heap, and with it the KASLR slide.

3.   **Free**
A forged pointer makes the kernel free an object we choose.

4.   **Reclaim**
We refill that memory with a fake callback built from NFS client names.

5.   **Trigger**
We hang up. `nfsd` calls the fake callback, and the kernel runs `/bin/sh` as root.

In the recording, that command is `whoami; id; poweroff -f`: the victim prints `root`, then `uid=0(root)`, and switches itself off.

## Found and proven by a machine

Antara, OpenSec's white-box harness, flagged the `nfsd` reply-cache path, scored it 9.8, and built the leak, the arbitrary free and the root shell shown in the video by itself: end to end, with no human in the loop.

> Kernel hardening does not remove the overflow. Patch every host.

## Am I exposed?

Tick what's true for your host. All four means exposed, today.

Am I exposed?

*   **Kernel**Older than 6.12.117, 6.18.61, 7.3.2 or 7.4-rc1, with no distribution backport`uname -r` 
*   **nfsd running**The in-kernel NFS server is loaded`lsmod | grep -w nfsd` 
*   **NFSv4.1 or 4.2 on**The list shows `+4.1` or `+4.2``cat /proc/fs/nfsd/versions` 
*   **2049 reachable**Listening on an address other than loopback`ss -ltn 'sport = :2049'` 

0 of 4 conditions met
## What to do

### Patch and reboot

| Branch | Fixed in |
| --- | --- |
| 6.12 LTS | 6.12.117 |
| 6.18 | 6.18.61 |
| 7.3 | 7.3.2 |
| mainline | 7.4-rc1 |

On a distribution kernel, install the update that lists CVE-2026-99362.

### Can't patch today? Close 2049

Only the storage network may reach nfsd Bash

`nft add rule inet filter input tcp dport 2049 ip saddr != 10.20.0.0/16 drop`
### Or turn off NFSv4.1 and 4.2

/etc/nfs.conf ini

```
[nfsd]
vers4.1=n
vers4.2=n
```

Then restart `nfs-server`. This turns off pNFS and some 4.2 features.

## Hunting for it

The attack is valid NFS, so there is no network signature. Look for:

*   **Kernel warnings** from `nfsd4_check_resp_size`, on every attempt, successful or not.
*   **Oopses** with `nfsd4_*`, `svc_*` or `call_usermodehelper*` frames.
*   **Shells spawned by kernel workers** on a file server.
*   **Bursts of short NFSv4.1 sessions** from one source.

## Disclosure

We reported the bug to the NFSD maintainers and [security@kernel.org](mailto:security@kernel.org) on 22 September 2026 with the full remote-root exploit, and sent a patch the same day. CVE-2026-99362 was published with fixes on 20 November.

## Credits

*   **OpenSec Intelligence:** found the bug with Antara, which escalated it to pre-auth root on its own, and reported it with the full exploit and a patch.
*   **Jérémy Jean (ANSSI):** found it independently and wrote the upstream fix, `5d5a72e965c8` and `241848cc774e`.
*   **Chuck Lever and Jeff Layton:** the NFSD maintainers.

## References

[nfsd: preflight SEQUENCE replies before accepting a slot The upstream fix for CVE-2026-99362, by Jérémy Jean.github.com](https://github.com/torvalds/linux/commit/5d5a72e965c8)[nfsd: set op->status when an operation's header cannot be encoded The follow-up guard in the NFSv4 encoder.github.com](https://github.com/torvalds/linux/commit/241848cc774e)

*   Introduced by [47ee52986472](https://github.com/torvalds/linux/commit/47ee52986472) (Linux 3.16)
*   [Patch thread](https://patch.msgid.link/20260817-jean-v1-1-9e356596ab85@kernel.org)
*   [OpenSec's patch submission](https://lore.kernel.org/linux-nfs/20260922112608.1256363-1-mayank.jangid.moon@gmail.com/)

Links/Buttons:
- [Skip to content](https://opensec.in/blog/nfs2root-cve-2026-99362#blog-main)
- [](https://opensec.in/)
- [Platform](https://opensec.in/#platform)
- [How it works](https://opensec.in/#workflow)
- [Research](https://opensec.in/blog?category=Research)
- [Why OpenSec](https://opensec.in/#why-opensec)
- [Benchmarks](https://opensec.in/benchmarks)
- [Blog](https://opensec.in/blog)
- [Login](https://opensec.in/login)
- [What you need to know](https://opensec.in/blog/nfs2root-cve-2026-99362#summary)
- [Watch the video](https://opensec.in/blog/nfs2root-cve-2026-99362#video)
- [CVE-2026-99362](https://opensec.in/blog?search=CVE-2026-99362)
- [#](https://opensec.in/blog/nfs2root-cve-2026-99362#references)
- [security@kernel.org](mailto:security@kernel.org)
- [nfsd: preflight SEQUENCE replies before accepting a slotThe upstream fix for CVE-2026-99362, by Jérémy Jean.github.com](https://github.com/torvalds/linux/commit/5d5a72e965c8)
- [nfsd: set op->status when an operation's header cannot be encodedThe follow-up guard in the NFSv4 encoder.github.com](https://github.com/torvalds/linux/commit/241848cc774e)
- [47ee52986472](https://github.com/torvalds/linux/commit/47ee52986472)
- [Patch thread](https://patch.msgid.link/20260817-jean-v1-1-9e356596ab85@kernel.org)
- [OpenSec's patch submission](https://lore.kernel.org/linux-nfs/20260922112608.1256363-1-mayank.jangid.moon@gmail.com/)
- [linux](https://opensec.in/blog?search=linux)
- [kernel](https://opensec.in/blog?search=kernel)
- [nfsd](https://opensec.in/blog?search=nfsd)
- [exploit](https://opensec.in/blog?search=exploit)
- [Share on X](https://x.com/intent/post?url=https%3A%2F%2Fopensec.in%2Fblog%2Fnfs2root-cve-2026-99362&text=NFS2ROOT%3A%20a%2012-year-old%20pre-auth%20remote%20root%20in%20the%20Linux%20kernel%27s%20NFS%20server)
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fopensec.in%2Fblog%2Fnfs2root-cve-2026-99362)
- [Subscribe](https://opensec.in/newsletter)
- [Our intelligence](https://opensec.in/#intelligence)
- [Questions & answers](https://opensec.in/#faq)
- [Disclosures](https://opensec.in/#disclosures)
- [Changelog](https://opensec.in/changelog)
- [Request early access](https://opensec.in/contact?topic=access)
- [Contact us](https://opensec.in/contact)
- [Privacy](https://opensec.in/privacy)
- [Terms](https://opensec.in/terms)
- [Status](https://opensec.in/status)
- [Back to top](https://opensec.in/blog/nfs2root-cve-2026-99362#top)
