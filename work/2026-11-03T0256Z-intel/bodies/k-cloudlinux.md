# extract: served via trafilatura-direct
---
title: "CVE-2026-98432 Linux kernel IPv4 TCP flaw: status for CloudLinux - CloudLinux"
author: Akos Vajda
url: https://blog.cloudlinux.com/cve-2026-98432-linux-kernel-ipv4-tcp-flaw-status-for-cloudlinux/
hostname: cloudlinux.com
description: CVE-2026-98432 is a use-after-free flaw in the Linux kernel's IPv4 TCP code that a remote attacker can reach without an account on the server. Exploiting it means winning a timing race inside the kernel, which is hard to do. Our kernel team couldn't reproduce the claimed remote-root exploit. On CloudLinux, the flaw affects every version except CloudLinux 7.
sitename: CloudLinux
date: "2026-10-30"
categories: ['СloudLinux Blog']
fingerprint: "17d0998f98262b59"
---
**📋 TL;DR — last updated November 2, 2026, 21:10 UTC**

CVE-2026-98432 (CVSS 9.8, Critical per Red Hat) is a use-after-free flaw in the Linux kernel’s IPv4 TCP code that **a remote attacker can reach without an account on the server**. Exploiting it means winning a timing race inside the kernel, which is hard to do. Anthropic, which reported the flaw, says its AI model built an exploit that gives remote root on servers with a Multipath TCP listener. **Our kernel team couldn’t reproduce that claim.** The exploit isn’t public, and no exploitation in the wild has been reported.

- **Affected:** CloudLinux 7h, 8, 8 LTS, 9, 9 LTS and 10, and CloudLinux for Ubuntu 22.04. CloudLinux 7 isn’t affected. → [Affected CloudLinux versions](https://blog.cloudlinux.com#affected-cloudlinux-versions)
  - **Multipath TCP:** the claimed exploit needs it, and it’s off by default on CloudLinux 8, 9 and 10. The bug itself is in ordinary TCP, so those servers still need the fix. → [What the claimed exploit needs](https://blog.cloudlinux.com#what-the-claimed-exploit-needs)
- **Mitigation:** none. → [Is there a mitigation?](https://blog.cloudlinux.com#is-there-a-mitigation)
- **Fix status:** → [Update instructions](https://blog.cloudlinux.com#update-instructions)
  - **CloudLinux 7h and 8 kernel:** fixed kernel in staged rollout.
  - **AlmaLinux kernel (CloudLinux 9, 10):** fixed kernels released by AlmaLinux, not yet in the CloudLinux repositories.
  - **LTS kernels (CloudLinux 8 LTS, 9 LTS):** fixed kernel in staged rollout.
  - **KernelCare livepatch:** on the main feed for CloudLinux 7h, 8 and 9; on the testing feed for CloudLinux 10.
  - **CloudLinux for Ubuntu 22.04:** Canonical hasn’t released its fix yet.
- **Why it matters:** the attack arrives over the network, so it needs no hosting account. → [Why this matters on a shared host](https://blog.cloudlinux.com#why-this-matters-on-a-shared-host)
- **How the bug works:** a repeated connection request can make the kernel read memory it has already freed. → [Technical details of the bug](https://blog.cloudlinux.com#technical-details-of-the-bug)

This advisory is also tracked on the [CloudLinux status page](https://cloudlinux.statuspage.io/incidents/8tpg6g4nrpl4); subscribe there for status updates.

CVE-2026-98432 is a use-after-free flaw in the Linux kernel’s IPv4 TCP code, the part that sets up new network connections. **Anyone who can reach an open IPv4 TCP port on a server can reach the vulnerable code**, with no account or password. Exploiting it means winning a timing race inside the kernel, which is hard to do.

On October 27, Anthropic, which reported the flaw, [said its AI model had built an exploit](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude) that gives remote root on servers with a Multipath TCP listener. Our kernel team couldn’t reproduce the claim. Anthropic hasn’t published the exploit, and no exploitation in the wild has been reported.

On CloudLinux, the flaw affects every version except CloudLinux 7. **Multipath TCP is off by default** on CloudLinux 8, 9 and 10, but the bug itself is in ordinary TCP code, so every affected server needs the fix.

Every shared hosting server keeps IPv4 TCP ports open for its websites, mail and SSH. On an affected server, those ports lead to the vulnerable code.

**💡 Fixes without a reboot**

[KernelCare](https://cloudlinux.com/kernelcare-hosting/) is the alternative we recommend if emergency-patching and rebooting servers is not sustainable for you. It patches the running kernel in place. No reboot, no customer downtime. The livepatch for this issue is on the main feed for CloudLinux 7h, 8 and 9, and on the testing feed for CloudLinux 10; [Stream 4](https://blog.cloudlinux.com#stream-4-kernelcare-livepatch) has the details.


## Affected CloudLinux versions

The vulnerable code arrived in Linux 4.4, so every CloudLinux kernel from that version on carries it.

| Version | Affected | Status | 
|---|---|---|
| CloudLinux 7 (CL7) Kernel 3.10 | ✅ No: the vulnerable code arrived in Linux 4.4 | ℹ️ No update needed | 
| CloudLinux 7h (CL7h) Kernel 4.18 | ❌ Yes | [✅ Kernel patch: 4.18.0-553.180.1.lve.1, in staged rollout](https://blog.cloudlinux.com#stream-1-cloudlinux-7h-and-8-kernel) [✅ Livepatch: available](https://blog.cloudlinux.com#stream-4-kernelcare-livepatch) | 
| CloudLinux 8 (CL8) Kernel 4.18 | ❌ Yes | [✅ Kernel patch: 4.18.0-553.180.1.lve.1, in staged rollout](https://blog.cloudlinux.com#stream-1-cloudlinux-7h-and-8-kernel) [✅ Livepatch: available](https://blog.cloudlinux.com#stream-4-kernelcare-livepatch) | 
| CloudLinux 8 LTS Kernel 5.14 (TuxCare ELS) | ❌ Yes | [✅ Kernel patch: kernel-lts els19, in staged rollout](https://blog.cloudlinux.com#stream-3-tuxcare-els-lts-kernel-cloudlinux-8-lts-and-9-lts) ℹ️ Livepatch: not available; install the fixed kernel | 
| CloudLinux 9 (CL9) Kernel 5.14 | ❌ Yes | [⏳ Kernel patch: 5.14.0-687.64.1.el9\_8, not yet in the CloudLinux repositories](https://blog.cloudlinux.com#stream-2-almalinux-kernel-cloudlinux-9-and-10) [✅ Livepatch: available](https://blog.cloudlinux.com#stream-4-kernelcare-livepatch) | 
| CloudLinux 9 LTS Kernel 5.14 (TuxCare ELS) | ❌ Yes | [✅ Kernel patch: kernel-lts els19, in staged rollout](https://blog.cloudlinux.com#stream-3-tuxcare-els-lts-kernel-cloudlinux-8-lts-and-9-lts) ℹ️ Livepatch: not available; install the fixed kernel | 
| CloudLinux 10 (CL10) Kernel 6.12 | ❌ Yes | [⏳ Kernel patch: 6.12.0-211.72.1.el10\_2, not yet in the CloudLinux repositories](https://blog.cloudlinux.com#stream-2-almalinux-kernel-cloudlinux-9-and-10) [⏳ Livepatch: on the testing feed](https://blog.cloudlinux.com#stream-4-kernelcare-livepatch) | 
| CloudLinux for Ubuntu 22.04 Kernel 5.15 | ❌ Yes | ⏳ Kernel patch: via Canonical, not released yet † ℹ️ Livepatch: not available | 

<sup>†</sup> CloudLinux for Ubuntu 22.04 takes its kernel from Ubuntu (Canonical) via apt, not from a CloudLinux stream. As of October 30, 2026, Canonical lists the fix for its 22.04 kernel as work in progress, and we’ll note here when Canonical releases it.


## What the claimed exploit needs

The exploit Anthropic describes needs a server with a Multipath TCP (MPTCP) listener. MPTCP is an extension of TCP that lets one connection use several network paths at once. A program uses it only if it opens its connections as MPTCP, and on CloudLinux 8, 9 and 10 the kernel doesn’t allow that by default.

To see the setting on your server, run:

`sysctl net.mptcp.enabled`
net.mptcp.enabled = 0 means it’s off.

The setting doesn’t remove the flaw. The bug sits in the ordinary TCP code that every IPv4 connection passes through, so a server with MPTCP off still runs vulnerable code and still needs the fix.


## Is there a mitigation?

No. Red Hat states that no available mitigation meets its criteria for ease of deployment, broad applicability and stability. The fix is the kernel update or livepatch for your version.


## Update instructions

The fix reaches CloudLinux servers through the four streams below, and CloudLinux for Ubuntu 22.04 gets it from Canonical. We’ll update each stream here when its state changes.

### Stream 1: CloudLinux 7h and 8 kernel

**Update: October 30, 2026, 22:55 UTC.**

CloudLinux has released a fixed kernel for CloudLinux 7h and 8: 4.18.0-553.180.1.lve.1. It is in a staged rollout to production servers, so a regular kernel update installs it only once the rollout reaches the server. To install it now, run:

```
yum update cloudlinux-release
yum update kernel --enablerepo=cloudlinux-rollout-3-bypass
reboot
```
The first command updates the package that defines the CloudLinux repositories, so the second one can reach the rollout repository. After the reboot, uname -r should report a version starting with 4.18.0-553.180.1.lve.1. We’ll note here when the rollout is complete.

**Status: October 30, 2026.**

No fixed kernel yet. CloudLinux builds the CloudLinux 7h and 8 kernels and is preparing a version with the fix. We’ll add the kernel version here when it’s released.

### Stream 2: AlmaLinux kernel (CloudLinux 9 and 10)

**Update: November 2, 2026, 21:10 UTC.**

Red Hat released its fix on November 1, and AlmaLinux has published the matching kernels to its production repositories: kernel-5.14.0-687.64.1.el9\_8 for CloudLinux 9 and kernel-6.12.0-211.72.1.el10\_2 for CloudLinux 10. These, not the testing-repository kernels from October 30, are the ones coming to the CloudLinux repositories. AlmaLinux won’t promote the testing kernels to production, though they still carry the fix.

Once the new kernels are in the CloudLinux repositories, a regular kernel update and a reboot install them, including on servers running a testing kernel. We’ll note it here when they arrive.

**Update: October 30, 2026, 22:55 UTC.**

AlmaLinux has published fixed kernels to its testing repository: kernel-5.14.0-687.61.2.el9\_8 for CloudLinux 9 and kernel-6.12.0-211.69.2.el10\_2 for CloudLinux 10. Red Hat hasn’t released its own fix yet. To install one now, enable the AlmaLinux testing repository by installing its release package from AlmaLinux directly, update the kernel, then disable the testing repository and reboot.

For CloudLinux 9:

```
rpm -Uvh --nodeps https://repo.almalinux.org/almalinux/9/extras/x86_64/os/Packages/almalinux-release-testing-9-2.el9.noarch.rpm
dnf update 'kernel*'
dnf config-manager --disable almalinux-testing
reboot
```
For CloudLinux 10:

```
dnf install -y https://repo.almalinux.org/almalinux/10/extras/x86_64/os/Packages/almalinux-release-testing-10-2.el10.x86_64.rpm
dnf update 'kernel*'
dnf config-manager --disable almalinux-testing
reboot
```
After the reboot, uname -r should report a version starting with 5.14.0-687.61.2 on CloudLinux 9 or 6.12.0-211.69.2 on CloudLinux 10. Once the kernels reach the CloudLinux repositories, a regular kernel update installs them, and we’ll note that here.

**Status: October 30, 2026.**

No fixed kernel yet. CloudLinux 9 and 10 run the AlmaLinux kernel, which follows Red Hat. Red Hat lists its RHEL 9 and 10 kernels as affected and hasn’t released a fix. We’ll add the AlmaLinux kernel version here when it’s released.

### Stream 3: TuxCare ELS LTS kernel (CloudLinux 8 LTS and 9 LTS)

**Status: October 30, 2026.**

The fixed kernels are out: kernel-lts-5.14.0-284.1101.el8.tuxcare.11.els19 for CloudLinux 8 LTS and kernel-lts-5.14.0-284.1101.el9.tuxcare.11.els19 for CloudLinux 9 LTS. They reached the beta channel on October 30 and are now in a staged rollout to production servers: a regular kernel update installs them once the rollout reaches the server. A server needs a reboot to start running the fixed kernel. We’ll note here when the rollout is complete.

### Stream 4: KernelCare livepatch

**Update: November 2, 2026, 21:10 UTC.**

The KernelCare livepatch is on the main feed for CloudLinux 7h, 8 and 9. Subscribed servers take it on their next update cycle, or you can apply it now with no reboot:

`kcarectl --update`
The livepatch for CloudLinux 10 is on the testing feed. Servers on the default feed don’t have it yet. To take it from the testing feed:

`kcarectl --update --prefix test`
Once it reaches the main feed, subscribed servers take it on their next update cycle, and we’ll note it here.

**Status: October 30, 2026.**

A livepatch is in preparation for the CloudLinux 7h and 8 kernels, and for the AlmaLinux kernels that CloudLinux 9 and 10 run. Once released, it applies the fix to running servers with no reboot. We’ll add each release here.


## How to verify you are patched

After the reboot, run uname -r and compare it with the kernel version your stream lists.

For KernelCare:

`kcarectl --patch-info | grep CVE-2026-98432`
On a server that took the livepatch from the testing feed, add --prefix test to that command.

A patched server prints lines naming the CVE. The kernel version in the kpatch-name line only shows where the patch is filed, so it can differ from the version kcarectl --uname reports. Use --patch-info for this: kcarectl --info shows only the patch level and doesn’t list CVEs, so it makes a patched server look unpatched.


## Why this matters on a shared host

The attack needs no hosting account and no compromised site on the server. The attacker sends connection requests carrying IPv4 options and repeats them to win a race inside the kernel. A lost race costs them one failed connection while the server keeps running, so they can keep trying.

How far that gets an attacker is unproven. Anthropic’s post names neither the kernel version nor the configuration its exploit ran against. The memory error our kernel team triggered with artificial delays is far from running code remotely, and we haven’t reproduced it on a CloudLinux kernel.


## Technical details of the bug

When a client opens a TCP connection, its first packet (the SYN) can carry IPv4 options such as Record Route or Timestamp. The server stores those options with the pending connection. When the handshake completes, the kernel hands them to the new connection without making a copy.

If a retransmitted copy of the same SYN arrives at that moment and another CPU handles it, that CPU builds its reply from the same options. When the new connection is freed first, the kernel releases the options while the reply is still reading them. That read of freed memory is the use-after-free.

The upstream fix changes two lines so that the kernel waits until every reader has finished before it frees the options. IPv6 copies the options instead of sharing them, so the IPv6 handshake doesn’t have this flaw.


## Comments
