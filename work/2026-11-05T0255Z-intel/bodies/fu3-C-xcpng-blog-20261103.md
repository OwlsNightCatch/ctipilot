---
title: "November 2026 Security and Maintenance Updates #1 for XCP-ng 8.3 LTS"
author: Samuel Verschelde
url: https://xcp-ng.org/blog/2026/11/03/november-2026-security-and-maintenance-updates-1-for-xcp-ng-8-3-lts/
hostname: xcp-ng.org
description: Critical security update for XCP-ng 8.3 LTS, along with other maintenance updates.
sitename: XCP-ng Blog
date: "2026-11-03"
tags: ['Update', 'Security']
fingerprint: f601d91748b1f7f0
---
# November 2026 Security and Maintenance Updates #1 for XCP-ng 8.3 LTS

New updates are available for [XCP-ng 8.3 LTS](https://docs.xcp-ng.org/management/updates/#support-cycle).

[follow this guide](https://docs.xcp-ng.org/management/updates/). You can also join

[the discussion](https://xcp-ng.org/forum/topic/9964/xcp-ng-8-3-updates-announcements-and-testing/)on our community forum.

**Host reboots are necessary after this update.**

XCP-ng's updates are cumulative, so applying updates now will also apply any previous updates that weren't applied to your hosts. Update advisories: [https://xcp-ng.org/blog/tag/update/](https://xcp-ng.org/blog/tag/update/).

## Summary

The current batch of updates contains a fix for **a critical vulnerability** that may allow a malicious guest to compromise the host and other guests.

**critical**, and

**we advise updating immediately**.

Unfortunately, another important vulnerability was disclosed recently, related to the Linux kernel's TCP stack, and despite our efforts, circumstances did not allow us to include its fix in today’s batch. At the time of writing, the fix is undergoing QA and will be released as soon as possible, within 24 hours at most, and announced in a new update blog post.

**Both updates require a reboot of the hosts.**We are aware of the burden this adds and apologize for not being able to combine the updates. However, an

**iptables-based**

**mitigation is available**for the kernel vulnerability, which may allow you to postpone the second reboot until your next maintenance window.

Refer to this planned kernel update's

[Vates Security Advisory](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-056)for details.

Other changes include storage performance improvements (faster writes), PCI passthrough fixes, a hopefully final fix for incorrect snapshot metadata after VM reverts, and other maintenance changes.

## Precautions before or after the update

As detailed below, each VM switches to the new HVM PIRQ default the next time it boots. If a VM with a passed-through device behaves differently after its reboot, you can [turn HVM PIRQ back on](https://docs.xcp-ng.org/troubleshooting/common-problems/#issues-with-the-fix) for this VM.

## Security updates

### XSA-523: arbitrary read/write via grant copy

Two flaws in the Xen hypervisor's grant copy implementation let a malicious guest read and write arbitrary memory belonging to other domains, including Dom0. Because the affected memory can include the hypervisor and Dom0, a single compromised guest can break out of its isolation and take over the whole host. This is a guest escape with no known mitigation other than the fix, so we recommend applying this update as soon as possible.

*References: VSA-2026-055, CVE-2026-102703, CVE-2026-102704, XSA-523*

### sudo

`sudo` was updated to 1.9.17p2, with fixes for three privilege escalations and for an additional vulnerability which could let a local user with time-limited sudo rights extend them.

These vulnerabilities can only be exploited from a local account other than `root`, or through sudo rules added for such accounts. A default XCP-ng installation has neither.

Its default `secure_path` no longer contains `/usr/local/sbin` and `/usr/local/bin`. If you modified `/etc/sudoers`, your file is kept, and the new one is saved as `/etc/sudoers.rpmnew`.

*References: VSA-2026-051, CVE-2025-32462, CVE-2025-32463, CVE-2026-35535, CVE-2026-96512*

## Storage performance: faster writes

Faster writes thanks to finer locking in tapdisk.

When QCOW2 support was introduced, `tapdisk` became multithreaded, which required locks to protect shared data. One of these locks covered a larger section of code than necessary. This update restricts it to what really needs protection, so writes to QCOW2 disks can be significantly faster when the VM sends many I/O requests in parallel.

Large writes and many small parallel writes benefit the most. We have seen improvements of **up to 70% on some write-heavy workloads**.

## PCI passthrough: HVM PIRQ disabled by default

HVM PIRQ is an old Xen feature, only used by Linux guests. It was initially meant as a performance improvement, but some devices passed through to a Linux VM, such as some GPUs and SSDs, don't work properly with it, and Xen's log then shows messages such as `Unsupported MSI delivery mode 7`. Xen's own toolstack stopped enabling it by default in 2024.

In our [previous update](https://xcp-ng.org/blog/2026/10/05/october-2026-updates-1-for-xcp-ng-8-3-lts/), we added a VM setting to disable HVM PIRQ, and said we were working on doing it automatically. With this update, HVM PIRQ is **disabled by default** for HVM VMs, so you don't need to change this setting yourself anymore. The new default applies the next time a VM boots or reboots.

If a VM works better with HVM PIRQ, you can turn it back on with `xe vm-param-set uuid=<VM UUID> platform:hvm-pirq=true`, then reboot the VM. If you need to, please let us know, so that we learn which devices still need it. [Our documentation](https://docs.xcp-ng.org/troubleshooting/common-problems/#pci-passthrough-error-unsupported-msi-delivery-mode-7) gives more details.

## Control plane (XAPI)

XAPI is XCP-ng's control plane. Besides the HVM PIRQ default, here's what changed in this update.

### Fixing incorrect snapshot metadata

Context: each snapshot of a virtual disk keeps a reference to the disk it was taken from, in its `snapshot_of` field. This is what makes it possible to tell snapshots apart from regular disks. In some situations, this reference could end up incorrect, and a regular disk could then look like a snapshot.

The issue was complex and it took us several rounds of fixes to address it completely. Our developers believe that they have now fixed the root cause.

Note that the update **will not automatically fix pre-existing incorrect metadata**. Refer to the [detailed documentation](https://docs.xcp-ng.org/troubleshooting/xapi/snapshot-of/) for instructions on how to check whether any disks are affected and, if so, fix their metadata.

### Backups

This update improves the handling of the NBD servers used by Xen Orchestra to read virtual disk contents for backups, preventing backups of disks on shared SRs from failing with `HOST_OFFLINE` when a host in the pool is offline.

### Other fixes and changes

- A storage operation stuck on an SR no longer prevents XAPI from starting.
- When HA is enabled, evacuating a host that runs a VM not protected by HA now fails with a clear error message, instead of a misleading one about free memory. The behaviour itself doesn't change.
- A host joining a pool whose bonded network uses jumbo frames could end up with mismatched MTUs, and stay in maintenance mode. This is fixed.
- Opening VNC console snapshots of VMs no longer fails with an HTTP 500 error.
- As a hardening measure, the XAPI plugin that Xen Orchestra uses to restart the XOSTOR services during rolling pool updates now refuses to manage other services.
- `gpumon` and `xcp-featured` were rebuilt for the new XAPI, with no functional change.

## Storage

### Tapdisk changes

- Fix a possible bug in blktap, when, in rare cases, the process handling a VM disk (tapdisk) could crash during a backup and leave the disk impossible to detach.
- Our storage team continues to modernize the `tapdisk` codebase, to make future improvements possible. No functional change is expected from this preparatory work.

### XOSTOR changes

- When a host shuts down or reboots, the VMs that still run are now always shut down before the LINSTOR services stop. Before, the LINSTOR services could stop first, while VMs still used their disks. This could make rolling pool updates of large pools fail.
- Fix enabling HA on pools that use XOSTOR, broken by [our previous update](https://xcp-ng.org/blog/2026/10/05/october-2026-updates-1-for-xcp-ng-8-3-lts/).
- Fix the XOSTOR health check shown in Xen Orchestra. The check no longer analysed the state of the disks.

## Virtualization & System

### Xen

In addition to the security fixes mentioned above:

- Xen was synced with XenServer's 4.17.7-4 release. The next two items come from this sync.
- On Intel Granite Rapids hosts (Xeon 6900/6700/6500 with P-cores) whose BIOS provides old microcode, loading some newer microcode can hang the host (Intel erratum GNR98). Xen now skips these microcode updates and logs `microcode: Granite Rapids erratum GNR98 detected` with a recommendation to update the firmware. Affected hosts need a BIOS update, which our `intel-microcode` package can't replace.
- Xen includes the fix for XSA-516. As explained in [October 2026 Security Updates #2](https://xcp-ng.org/blog/2026/10/13/october-2026-security-updates-2-for-xcp-ng-8-3-lts/), XCP-ng 8.3 LTS is not impacted, since [PV guests don't run on XCP-ng 8.3](https://docs.xcp-ng.org/releases/release-8-3/#pv-virtualization-mode). The fix was included to stay aligned with upstream and facilitate future maintenance.

## Drivers and firmware

- Intel CPUs get the [microcode-20260925](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/releases/tag/microcode-20260925) release, as redistributed by XenServer. It brings the security fixes Intel published in August (INTEL-SA-01379, 01404, 01423, 01428, 01435, 01441, 01442 and 01443) and functional fixes, for Xeon Scalable 3rd, 4th and 5th gen, Xeon 6, Xeon D and several Core generations. The microcode for Granite Rapids AP/SP (Xeon 6900/6700/6500 with P-cores, except the R1S models) doesn't change.
- AMD Zen 5 CPUs of family 1Ah get new microcode (CPUID 00b00f21 and 00b10f10), as redistributed by XenServer.

## User interface

### XO Lite 0.26.0

XO Lite, the management interface embedded in every XCP-ng host, was updated to version 0.26.0, with a new batch of previously missing features:

- Reboot, force reboot, shut down, start and forget a host.
- Delete host internal networks.

Also, tab labels are no longer in uppercase, for better readability.

**Again, given the severity of the Xen vulnerability fixed in this release, we strongly advise users to update as soon as possible.**
