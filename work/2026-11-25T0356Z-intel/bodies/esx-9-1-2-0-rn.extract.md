---
title: ESX 9.1.2.0 Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/esx-9-1-2-0-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-11-24"
fingerprint: f65f5e351e78186a
language: en
pagetype: article
filedate: "2026-11-25"
---
# ESX 9.1.2.0 Release Notes

This document contains the following sections

## Introduction

VMware ESX 9.1.2.0 | 24 NOV 2026 | Build 25946735

Check for additions and updates to these release notes.

For information about release types and dependencies, see the [Lifecycle Management](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_527&appid=vcf-9-1&language=en&format=rendered) documentation.

## What's New

This release resolves CVE-2026-123910, CVE-2026-123911, CVE-2026-123913, and CVE-2026-123915. For more information on these vulnerabilities and their impact on Broadcom products, see [VMSA-2026-0011](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626).

**Provision ESX Hosts by Script with a vSphere Configuration Profiles File:**

Starting with ESX 9.1.2, when you provision ESX hosts by using a script, you can supply a desired configuration json file of a cluster that uses vSphere Configuration Profiles instead of a long list of kickstart commands. For more information, see [Provision ESX Hosts with a Desired Configuration By Using a Script](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_128&appid=vsphere-9-1&language=&format=rendered).

**AMD 6th Generation EPYC™ 9006 SP7 (codename Venice) CPU Support:**

ESX 9.1.2 adds support to AMD EPYC™ 9006 SP7 CPU Series, which scales up to 256 cores per socket, SMT capable (2 threads per core). The 512 threads per socket can enable highly dense host server consolidation of VMs.

**Broadcom BCM57504 Network Adapters Support Hardware-Timestamped PTP over SR-IOV:**

In ESX 9.1.2, Broadcom BCM57504 network adapters support Precision Time Protocol (PTP) over SR-IOV with hardware timestamping, providing validated compatibility with VMware's TRX timekeeping solution.

## Build Details

**VMware ESX 9.1.2.0**

**VMware vSphere Hypervisor (ESX) Offline Bundle**

**Download Filename**:

VMware-ESXi-9.1.2.0.25946735-depot.zip

**Build**:

25946735

**Download Size**:

707 MB

**SHA256 checksum:**

a44e0e0bcffd6f296b5bb1983e5e0a650d2817cc29c9a0b22d113b77250e7a5a

**Live Patchable**

No

**Host Reboot Required**:

Yes

**Virtual Machine Migration or Shutdown Required**:

Yes

**VMware vSphere Hypervisor (ESX) ISO image**

**Download Filename**:

VMware-VMvisor-Installer-9.1.2.0.25946735.x86\_64.iso

**Build**:

25946735

**Download Size**:

726 MB

**SHA256 checksum:**

d36eb24f435364701f5d4d96779141d547e4596c2501e780b782ae43fd33c37c

**ESX Images**

Name and Version

Release Date

Category

Live Patchable

ESXi-9.1.2.0-25946735

24 November 2026

Bugfix and Security

No

**Image Profiles**

VMware patch and update releases contain general and critical image profiles. Application of the general release image profile applies to new bug fixes.

**Image Profile Name**

ESXi-9.1.2.0-25946735-standard

ESXi-9.1.2.0-25946735-no-tools

## Applying the Patch

Log in to the [Broadcom Support Portal](https://support.broadcom.com/) to download this patch, depending on your entitlement, [VMware vSphere Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20vSphere%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529542&viewGroup=true) or [VMware Cloud Foundation](https://support.broadcom.com/group/ecx/productfiles?displayGroup=VMware%20Cloud%20Foundation%209&release=9.0.0.0&os=&servicePk=&language=EN&groupId=529537&viewGroup=true).

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).See these KBs for details on the authenticated online and offline download: [390121](https://knowledge.broadcom.com/external/article/390121), [390098](https://knowledge.broadcom.com/external/article/390098), and [389276.](https://knowledge.broadcom.com/external/article/389276)

For information about deploying, converging, upgrading, or patching your environment to 9.1.2, see [Getting to 9.1.2](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes.html#getting-to-vcf-9.1.2).

For VCF environments, you apply this patch by using VCF Operations. See [Upgrade or Patch an Individual VCF Component](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_535&appid=vcf-9-1&language=&format=rendered).

For VMware vSphere Foundation environments, for details on updates and upgrades by using vSphere Lifecycle Manager, see [What is vSphere Lifecycle Manager](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_107&appid=vsphere-9-1&language=&format=rendered) and [vSphere Lifecycle Manager Images and Baselines](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_108&appid=vsphere-9-1&language=&format=rendered). You can also update ESX hosts without the use of vSphere Lifecycle Manager by using an image profile. To do this, you must manually download the patch offline bundle ZIP file or see the Broadcom knowledge base article [How to download ESXi ISO image for all releases including patch updates.](https://williamlam.com/2023/03/quick-tip-how-to-download-esxi-iso-image-for-all-releases-including-patch-updates.html)

For more information, see [Using ESXCLI for Host Management](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_109&appid=vsphere-9-1&language=&format=rendered) and the [VMware ESX Upgrade](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_008&appid=vsphere-9-1&language=en&format=rendered) guide.

## Resolved Issues

## ESXi-9.1.2.0-25946735

**Name**

ESX

**Version**

ESXi-9.1.2.0-25946735

**Release Date**

November 24, 2026

**Category**

Bugfix

**Live Patchable**

No

**Affected Components**

- Broadcom-ELX-lpfc
- Broadcom-bcm-mpi3
- Broadcom-bnxt-Net-RoCE
- Broadcom-elxnet
- Broadcom-lpnic
- Broadcom-lsi-mr3
- Broadcom-lsi-msgpt35
- Broadcom-ntg3
- Cisco-nenic
- Cisco-nenic-ens
- ESXi HPE-hpv2-hpsa-plugin
- Intel-i40en
- Intel-icen
- Intel-irdman
- Intel-ixgben
- Intel-ne1000
- Mellanox-nmlx5
- Microchip-smartpqi
- Microchip-smartpqiv2-plugin
- Pensando-ionic-cloud
- Pensando-ionic-en
- Solarflare-NIC
- VMware-Cpu-Microcode
- VMware-HBR-UW
- VMware-Host-Client
- VMware-NVMeoF-TCP
- VMware-VM-Tools
- VMware-vmkusb
- esx-update
- esxio-update
- vsphere-fdm

**Related CVE numbers**

CVE-2026-123910, CVE-2026-123911, CVE-2026-123913, CVE-2026-123915

**This patch resolves the following issues:**

**Nested virtual machines fail on ESX hosts with Windows guest OS on AMD CPUs**

When the guest hypervisor in nested VMs transitions between virtual environments, the CPU might retain stale address translation entries in its Translation Lookaside Buffer (TLB). On AMD processors, if such entries are not properly removed during the context switch, they might cause faults that lead to failure of the guest OS. As a result, nested virtual environments, such as WSL2 in a Windows VM, might fail or become unresponsive.

**NVIDIA MIG-backed vGPU devices that do not provide both Multi-Instance GPU (MIG) and time-slicing sharing methods might cause the hostd service to fail**

The hostd process assumes that an NVIDIA device provides vGPU MIG information in parallel with time-sliced information and if one is not present, the service might fail.

**During removal of NVMe namespaces on the target array, an ESX host might fail with a purple diagnostic screen**

Rarely, during the removal of NVMe namespaces on the target array, a race condition can occur in ESX when processing notifications from the array. As a result, the ESX host might fail with a purple diagnostic screen.

**An ESX host unexpectedly reboots or fails when powering on a virtual machine configured with a Marvell QLogic Fibre Channel (FC) HBA attached by PCI passthrough**

Marvell QLogic FC adapters do not support Function Level Reset (FLR). By default, ESX falls back to resetting such devices by using a secondary bus (bridge) reset when the device is claimed for passthrough. On some platforms, this bridge reset is not handled cleanly by the device or platform, leaving the PCIe device unresponsive and, in some cases, causing a host reboot during passthrough device initialization. In some cases, the ESX host might fail with a purple diagnostic screen.

**NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller restart**

On ESX hosts using an Emulex Fibre Channel adapter, some NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller reset or reboot. The adapter might show Link Up even though the affected paths remain unavailable after the storage controller is back online. A storage rescan might not restore the affected paths.

**You see BackMap\_Lookup failed logs flooding the vmkernel log**

In the vmkernel.log file, you see multiple warnings for Container Runtime Executive (CRX) virtual machines, such as:

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 4000019c60): Not found

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 400001a137): Not found

This issue affects only CRX VMs and the logs do not indicate an actionable problem.

**ESX host fails after mounting a vSphere Virtual Volumes datastore backed by NFSv3**

Mounting a vSphere Virtual Volumes datastore creates unique TCP connections per server IP address till the number of connections reaches the limit of the MaxConnPerIP parameter. The default value of MaxConnPerIP is 32, but if the parameter is set to a much higher value, such as more than 100, then the total number of connections might exhaust the ports which NFSv3 client can handle. As a result, new mounts might fail and cause the ESX host to fail with a purple diagnostic screen.

**An ESX host might fail with purple diagnostic screen in very rare cases of corruption of slab allocator data structures**

A memory underallocation issue in VMFS in very rare cases might cause corruption of slab allocator data structures. As a result, the ESX host might fail with a purple diagnostic screen.

**ESX 9.1.2.0 includes the following AMD microcode:**

Code Name

FMS

MCU Rev

MCU Date

Brand Names

Bulldozer

0x00600f12 (15/01/2)

0x0600063e

2/7/2018

Opteron 6200/4200/3200 Series

Piledriver

0x00600f20 (15/02/0)

0x06000852

2/6/2018

Opteron 6300/4300/3300 Series

Zen-Naples

0x00800f12 (17/01/2)

0x08001278

11/11/2024

EPYC 7001 Series

Zen2-Rome

0x00830f10 (17/31/0)

0x0830107c

12/18/2023

EPYC 7002/7Fx2/7Hx2 Series

Zen3-Milan

0x00a00f11 (19/01/1)

0x0a0011de

4/18/2025

EPYC 7003 Series

Zen3-Milan (old BIOS)

0x00a00f11 (19/01/1)

0x0a0011d5

2/23/2024

EPYC 7003 Series

Zen3-Milan-X

0x00a00f12 (19/01/2)

0x0a001247

3/27/2025

EPYC 7003X Series

Zen3-Milan-X (old BIOS)

0x00a00f12 (19/01/2)

0x0a001238

2/26/2024

EPYC 7003X Series

Zen4-Genoa

0x00a10f11 (19/11/1)

0x0a101158

6/9/2025

EPYC 9004 Series

Zen4-Genoa (old BIOS)

0x00a10f11 (19/11/1)

0x0a101148

2/23/2024

EPYC 9004 Series

Zen4-Genoa-X

0x00a10f12 (19/11/2)

0x0a101253

6/12/2025

EPYC 9004X Series

Zen4-Genoa-X (old BIOS)

0x00a10f12 (19/11/2)

0x0a101248

2/26/2024

EPYC 9004X Series

Zen4-Bergamo/Siena

0x00aa0f02 (19/a0/2)

0x0aa0021c

6/12/2025

EPYC 8004/9004 Series

Zen4-Bergamo/Siena (old BIOS)

0x00aa0f02 (19/a0/2)

0x0aa00215

2/28/2024

EPYC 8004/9004 Series

Zen5-Turin

0x00b00f21 (1a/02/1)

0x0b002175

5/28/2026

EPYC 9005 Series

Zen5-Turin-Dense

0x00b10f10 (1a/11/0)

0x0b101066

5/28/2026

EPYC 9005 Series

**You see unrealistic stats or network usage from Broadcom bnxtnet NICs**

The esxcli network nic stats get -n vmnicX command might show inflated or unrealistic stats from Broadcom bnxtnet NICs or in the vSphere Client you see inflated network usage.

The issue is fixed in the inbox driver for 9.1.2.0. For async drivers, upgrade the bnxtnet driver and firmware to 238.x or later.

**Mounting a tardisk with truncated header might cause an ESX host to fail with a purple diagnostic screen**

If the /tmp ramdisk of an ESX host does not have sufficient space when the vSphere Lifecycle Manager mounts a tardisk, a truncation in the end of a tar header might cause the host to fail with a purple diagnostic screen. The presence of function VisorFSTarPopulate() in the backtrace visible in the purple diagnostic screen is indicative of the issue. In the vmkernel.log, you see a line similar to:

WARNING: VisorFSRam: 220: Cannot extend visorfs file /tmp/imgdb-a6he6mo2/imgdb.tgz.bk because its ramdisk (tmp) is full.

**ESX host operations that reload the syslog configuration might fail with an internal error message**

When audit records are enabled on an ESX host, any operation that triggers a syslog configuration reload, such as automated vCenter **Update option value** tasks initiated by the log integration service account, `svc-li-vc-*`, VIB installations or upgrades, or syslog/audit setting changes, might cause the `vmsyslogd` service to connect to every configured `ssl://` remote syslog collector without a connection timeout. If a collector accepts the TCP connection without completing the TLS handshake or silently drops packets without sending a reset, the `vmsyslogd` command thread can block indefinitely, causing the reloads to time out/fail.

In the vSphere Client, you see a message such as:

`A general system error occurred: Internal error.`

In `/var/log/hostd.log` or `esxcli` command output, you see errors such as:

- Timed out while waiting for a response from UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

- Failed to connect to UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

In `/var/log/vmsyslogd.log`, you see records such as:

`Failed to retrieve connection identifiers: Failed to connect the supplied BIO`

The fix enforces bounded deadlines on TLS connect and handshake probes and replaces indefinite socket polling with bounded waits for clean connection recovery.

**ESX hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESX host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

Representative lines from logs:

vmkwarning.log (lwsmd cannot create threads): 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: LinuxThread: 411: lwsmd: Error cloning thread: -12 (bad0014) 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: World: 3234: Could not allocate new world handle for world ID: 6655205: Out of memory 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)uw.2099459 (7773) requires 1024 KB, asked 1024 KB from likewise (7517) which has 93056 KB occupied and 128 KB available. 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)Admission failure in path: host/vim/vmvisor/likewise:lwsmd.2099459:uw.2099459

The lwisOomCheck service now automatically starts together with the Likewise service on ESX hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**Active Directory user or group permissions might be unexpectedly removed from an ESX host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESX host might incorrectly remove permissions to an AD user or group.

The fix makes sure that ESX hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted and preserves permissions in the case of a temporary connectivity failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on** 

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

**Intel Xeon 6 processors utilizing QAT accelerators might see increased boot times on ESX 9.1**

On Intel Xeon 6 processors systems using QAT devices, in some cases, the boot time for ESX hosts might increase.

**ESX hosts might stop updating power consumption data after a Baseboard Management Controller (BMC) reset**

After a reset of the BMC, ESX hosts might stop updating power consumption data from vCenter because the sensord powersvc plugin might be disabled. The sensord service logs errors such as Failed to read from power provider and Too many failures, powersvc offline.

The fix updates the plugin to automatically resume operation after a BMC reset. On affected builds, restart sensord from the ESX shell with the /etc/init.d/sensord restart command to resume power readings.

**The snmpd service might send SNMP traps for past system events logs after a restart**

Whenever the snmpd service is restarted, stale System Event Log (SEL) records might be incorrectly sent as SNMP traps.

**On ESX hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESX hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

The fix increases the default xmapGB value from 32GB to 64GB.

**A race condition in the USB Network adapter in management controllers might cause ESX hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESX hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

**ESX host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESX host fails with a purple diagnostic screen.

**A virtual machine with a vGPU device might fail to allocate memory when system memory usage is high**

In some cases, VMs with vGPUs might consume more than 95% of the physical memory and leave insufficient overhead memory at runtime, which might lead to memory allocation failures.

**An ESX host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESX host might fail with a purple diagnostic screen.

**VMware Tools Bundling Changes in ESX 9.1.2.0**

The following VMware Tools ISO images are bundled with ESX 9.1.2.0:

- : VMware Tools 13.1.10.0 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.windows.iso

The following VMware Tools ISO images are available for download:

- VMware Tools 12.5.5:
  - VMware Tools 12.5.5 supports 64-bit Windows versions.windows.iso:  - VMware Tools 12.4.10 supports 32-bit Windows versions.windows-x86.iso:  - : VMware Tools 10.3.26 ISO image for Linux OS with glibc 2.11 or later.linux.iso

- VMware Tools 11.0.6:
  - : for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).windows.iso

- VMware Tools 10.0.12:
  - : for Windows 2000, Windows XP, and Windows 2003.winPreVista.iso  - : supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with linuxPreGLibc25.iso version earlier than 2.5.glibc
- : VMware Tools image 10.3.10 for Solaris.solaris.iso- : Supports Mac OS X versions 10.11 and later.darwin.iso

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESX:

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

**Provisioning ESX hosts by UEFI HTTPS with the bootloader vbmx64.efi and with a custom image based on OEM strings might fail**

If the software specification you use to provision ESX hosts contains customization based on OEM strings, ESX hosts that boot with UEFI HTTPS might fail to match the correct ESX image.

**An ESX host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESX host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESX host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

**ESX 9.1.2 includes the following Intel microcode:**

Code Name

FMS

Plat ID

Servicing

MCU Rev

MCU Date

Brand Names

Sandy Bridge DT

0x206a7 (06/2a/7)

0x12

baseline

0x2f

2/17/2019

Intel Xeon E3-1100 Series;

Intel Xeon E3-1200 Series;

Intel i7-2655-LE Series;

Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series;

Intel i7-3500-LE/UE;

Intel i7-3600-QE;

Intel Xeon E3-1200-v2 Series;

Intel Xeon E3-1100-C-v2 Series;

Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series;

Intel i7-4700-EQ Series;

Intel i5-4500-TE Series;

Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series;

Intel Xeon E5-2600-v2 Series;

Intel Xeon E5-2400-v2 Series;

Intel Xeon E5-1600-v2 Series;

Intel Xeon E5-1400-v2 Series

Ivy Bridge EX

0x306e7 (06/3e/7)

0xed

baseline

0x715

3/14/2019

Intel Xeon E7-8800/4800/2800-v2 Series

Haswell EP

0x306f2 (06/3f/2)

0x6f

baseline

0x49

8/11/2021

Intel Xeon E5-4600-v3 Series;

Intel Xeon E5-2600-v3 Series;

Intel Xeon E5-2400-v3 Series;

Intel Xeon E5-1600-v3 Series;

Intel Xeon E5-1400-v3 Series

Haswell EX

0x306f4 (06/3f/4)

0x80

baseline

0x1a

5/24/2021

Intel Xeon E7-8800/4800-v3 Series

Broadwell H

0x40671 (06/47/1)

0x22

baseline

0x22

11/12/2019

Intel Core i7-5700EQ;

Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series;

Intel Atom C2500 Series;

Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series;

Intel Xeon E5-4600-v4 Series;

Intel Xeon E5-2600-v4 Series;

Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series;

Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series;

Intel Xeon D-2100 Series;

Intel Xeon D-1600 Series;

Intel Xeon W-3100 Series;

Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300

Broadwell DE

0x50662 (06/56/2)

0x10

baseline

0x1c

6/17/2019

Intel Xeon D-1500 Series

Broadwell DE

0x50663 (06/56/3)

0x10

baseline

0x700001c

6/12/2021

Intel Xeon D-1500 Series

Broadwell DE

0x50664 (06/56/4)

0x10

baseline

0xf00001a

6/12/2021

Intel Xeon D-1500 Series

Broadwell NS

0x50665 (06/56/5)

0x10

baseline

0xe000015

8/3/2023

Intel Xeon D-1600 Series

Skylake H/S

0x506e3 (06/5e/3)

0x36

baseline

0xf0

11/12/2021

Intel Xeon E3-1500-v5 Series;

Intel Xeon E3-1200-v5 Series

Denverton

0x506f1 (06/5f/1)

0x01

baseline

0x3e

10/5/2023

Intel Atom C3000 Series

Ice Lake SP

0x606a6 (06/6a/6)

0x87

baseline

0xd000433

3/9/2026

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300 Series;

Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series;

Intel Xeon D-1700 Series

Snow Ridge

0x80665 (06/86/5)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Snow Ridge

0x80667 (06/86/7)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Tiger Lake U

0x806c1 (06/8c/1)

0x80

baseline

0xbe

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake U Refresh

0x806c2 (06/8c/2)

0xc2

baseline

0x3e

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake H

0x806d1 (06/8d/1)

0xc2

baseline

0x58

7/24/2025

Intel Xeon W-11000E Series

Sapphire Rapids SP HBM

0x806f8 (06/8f/8)

0x10

baseline

0x2c000435

3/2/2026

Intel Xeon Max 9400 Series

Sapphire Rapids SP

0x806f8 (06/8f/8)

0x87

baseline

0x2b000690

5/28/2026

Intel Xeon Platinum 8400 Series;

Intel Xeon Gold 6400/5400 Series;

Intel Xeon Silver 4400 Series;

Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series;

Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series;

Intel Xeon E-2200 Series (4 or 6 core)

Coffee Lake

0x906eb (06/9e/b)

0x02

baseline

0xf6

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake

0x906ec (06/9e/c)

0x22

baseline

0xf8

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake Refresh

0x906ed (06/9e/d)

0x22

baseline

0x104

11/14/2024

Intel Xeon E-2200 Series (8 core)

Rocket Lake S

0xa0671 (06/a7/1)

0x02

baseline

0x66

2/12/2026

Intel Xeon E-2300 Series

Granite Rapids SP R1S

0xa06d1 (06/ad/1)

0x20

baseline

0xa000164

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000444

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003c4

7/2/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Emerald Rapids SP

0xc06f2 (06/cf/2)

0x87

baseline

0x21000300

6/9/2026

Intel Xeon 8500 Series;

Intel Xeon Gold 6500/5500 Series;

Intel Xeon Silver 4500 Series;

Intel Xeon Bronze 3500 Series

**QuickBoot might fail with memory allocation error on platforms with several TB of DRAM**

A memory allocation error might cause QuickBoot to fail on platforms with large amount of memory, such as several TB of DRAM. In /var/run/log/loadESX.log, you can see the following errors:

2026-09-07T15:42:25.768Z +ERROR loadESX 2103140 \[esx@4413\] loadesxLive.utils.LoadESXMgmtError: LoadESXMgmtError - LoadESX management command 19 failed (status: 0xbad0014)

At approximately the same timestamp, the following error appears in the vmkernel logs:

2026-09-07T15:42:25.590Z -INFO vmkernel - \[esx@4413\] cpu665:2103140)LoadESX: LoadESXMgmtInstallVMKBoot:1135: Failed to allocate memory for vmkboot

## ESXi-9.1.2.0-25946735-standard

**Profile Name**

ESXi-9.1.2.0-25946735-standard

**Build**

For build information, see Patches Contained in This Release.

**Vendor**

Broadcom, Inc.

**Release Date**

November 24, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

VMW\_bootbank\_bcm-mpi3\_8.15.1.0.0.0-3vmw.912.0.25946735.vib, VMware\_bootbank\_bmcal\_9.1.2-0.25946735.vib, VMware\_bootbank\_bmcal-esxio\_9.1.2-0.25946735.vib, VMW\_bootbank\_bnxtnet\_232.0.36.0-75vmw.912.0.25946735.vib, VMW\_bootbank\_bnxtroce\_232.0.36.0-75vmw.912.0.25946735.vib, VMware\_bootbank\_clusterstore\_9.1.2-0.25946735.vib, VMware\_bootbank\_cpu-microcode\_9.1.2-0.25946735.vib, VMware\_bootbank\_crx\_9.1.2-0.25946735.vib, VMware\_bootbank\_drivervm-gpu-base\_9.1.2-0.25946735.vib, VMW\_bootbank\_elxnet\_12.0.1252.0-10vmw.912.0.25946735.vib, VMware\_bootbank\_esx-base\_9.1.2-0.25946735.vib, VMware\_bootbank\_esx-dvfilter-generic-fastpath\_9.1.2-0.25946735.vib, VMware\_bootbank\_esx-ui\_9.1.2-0.25946735.vib, VMware\_bootbank\_esx-update\_9.1.2-0.25946735.vib, VMware\_bootbank\_esx-xserver\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio-base\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio-combiner\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio-combiner-esxio\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_9.1.2-0.25946735.vib, VMware\_bootbank\_esxio-update\_9.1.2-0.25946735.vib, VMware\_bootbank\_gc\_9.1.2-0.25946735.vib, VMware\_bootbank\_gc-esxio\_9.1.2-0.25946735.vib, VMW\_bootbank\_i40en\_2.6.0.47-1vmw.912.0.25946735.vib, VMW\_bootbank\_icen\_1.15.0.6-1vmw.912.0.25946735.vib, VMware\_bootbank\_infravisor\_9.0.0-25821077.vib, VMW\_bootbank\_ionic-cloud\_24.9.1-16vmw.912.0.25946735.vib, VMW\_bootbank\_ionic-en\_24.9.1-16vmw.912.0.25946735.vib, VMW\_bootbank\_ionic-en-esxio\_24.9.1-16vmw.912.0.25946735.vib, VMW\_bootbank\_irdman\_1.5.0.6-1vmw.912.0.25946735.vib, VMW\_bootbank\_ixgben\_1.7.1.53-1vmw.912.0.25946735.vib, VMware\_bootbank\_loadesx\_9.1.2-0.25946735.vib, VMware\_bootbank\_loadesxio\_9.1.2-0.25946735.vib, VMW\_bootbank\_lpfc\_910.14.4.895.27-1vmw.912.0.25946735.vib, VMW\_bootbank\_lpnic\_11.4.63.0-2vmw.912.0.25946735.vib, VMW\_bootbank\_lsi-mr3\_7.736.02.00-5vmw.912.0.25946735.vib, VMW\_bootbank\_lsi-msgpt35\_37.00.00.00-3vmw.912.0.25946735.vib, VMware\_bootbank\_lsuv2-hpv2-hpsa-plugin\_1.0.0-6vmw.912.0.25946735.vib, VMware\_bootbank\_lsuv2-smartpqiv2-plugin\_1.0.0-14vmw.912.0.25946735.vib, VMware\_bootbank\_native-misc-drivers\_912.0.25946735-dummyvmw.912.0.25946735.vib, VMware\_bootbank\_native-misc-drivers-esxio\_912.0.25946735-dummyvmw.912.0.25946735.vib, VMW\_bootbank\_ne1000\_0.9.4-1vmw.912.0.25946735.vib, VMW\_bootbank\_nenic\_2.0.10.0-16vmw.912.0.25946735.vib, VMW\_bootbank\_nenic-ens\_1.0.9.2-5vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-cc\_4.25.2.1-1vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-cc-esxio\_4.25.2.1-1vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-core\_4.25.2.1-1vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-core-esxio\_4.25.2.1-1vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-rdma\_4.25.2.1-1vmw.912.0.25946735.vib, VMW\_bootbank\_nmlx5-rdma-esxio\_4.25.2.1-1vmw.912.0.25946735.vib, VMware\_bootbank\_nsx-adf\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-adf-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-cfgagent\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-cfgagent-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-context-mux\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-context-mux-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-cpp-libs\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-cpp-libs-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-esx-datapath\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-esx-datapath-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-exporter\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-exporter-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-headless-controller\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-headless-controller-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-host\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-host-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-monitoring\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-monitoring-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-mpa\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-mpa-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-nestdb\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-nestdb-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-netopa\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-netopa-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-opsagent\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-opsagent-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-platform-client\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-platform-client-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-proto2-libs\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-proto2-libs-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-proxy\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-proxy-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-python-logging\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-python-logging-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-python-utils\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-python-utils-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-scx\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-sfhc\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-shared-libs\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-shared-libs-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-snproxy\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-snproxy-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsx-vdpi-esxio\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsxcli\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_nsxcli-esxio\_9.1.2.0-9.1.25929668.vib, VMW\_bootbank\_ntg3\_4.1.16.0-6vmw.912.0.25946735.vib, VMW\_bootbank\_nvmetcp\_2.1.2.20-1vmw.912.0.25946735.vib, VMW\_bootbank\_nvmetcp-esxio\_2.1.2.20-1vmw.912.0.25946735.vib, VMware\_bootbank\_podvm-router\_9.1.2-0.25946735.vib, VMW\_bootbank\_sfvmk\_2.4.0.2010-26vmw.912.0.25946735.vib, VMW\_bootbank\_smartpqi\_90.4900.0.5000-4vmw.912.0.25946735.vib, VMware\_locker\_tools-light\_13.1.10-0.25946735.vib, VMware\_bootbank\_trx\_9.1.2-0.25946735.vib, VMware\_bootbank\_vcls-pod-crx\_9.1.2-0.25946735.vib, VMware\_bootbank\_vdfs\_9.1.2-0.25946735.vib, VMware\_bootbank\_vds-vsip\_9.1.2-0.25946735.vib, VMW\_bootbank\_vmkusb\_0.1-45vmw.912.0.25946735.vib, VMW\_bootbank\_vmkusb-esxio\_0.1-45vmw.912.0.25946735.vib, VMware\_bootbank\_vmware-fdm\_9.1.2-0.25946735.vib, VMware\_bootbank\_vmware-hbrsrv\_9.1.2-0.25946735.vib, VMware\_bootbank\_vsan\_9.1.2-0.25946735.vib, VMware\_bootbank\_vsanhealth\_9.1.2-0.25946735.vib, VMware\_bootbank\_vsipfwlib\_9.1.2.0-9.1.25929668.vib, VMware\_bootbank\_vsipfwlib-esxio\_9.1.2.0-9.1.25929668.vib

**Related CVE numbers**

CVE-2026-123910, CVE-2026-123911, CVE-2026-123913, CVE-2026-123915

**This patch resolves the following issues:**

**Nested virtual machines fail on ESX hosts with Windows guest OS on AMD CPUs**

When the guest hypervisor in nested VMs transitions between virtual environments, the CPU might retain stale address translation entries in its Translation Lookaside Buffer (TLB). On AMD processors, if such entries are not properly removed during the context switch, they might cause faults that lead to failure of the guest OS. As a result, nested virtual environments, such as WSL2 in a Windows VM, might fail or become unresponsive.

**NVIDIA MIG-backed vGPU devices that do not provide both Multi-Instance GPU (MIG) and time-slicing sharing methods might cause the hostd service to fail**

The hostd process assumes that an NVIDIA device provides vGPU MIG information in parallel with time-sliced information and if one is not present, the service might fail.

**During removal of NVMe namespaces on the target array, an ESX host might fail with a purple diagnostic screen**

Rarely, during the removal of NVMe namespaces on the target array, a race condition can occur in ESX when processing notifications from the array. As a result, the ESX host might fail with a purple diagnostic screen.

**An ESX host unexpectedly reboots or fails when powering on a virtual machine configured with a Marvell QLogic Fibre Channel (FC) HBA attached by PCI passthrough**

Marvell QLogic FC adapters do not support Function Level Reset (FLR). By default, ESX falls back to resetting such devices by using a secondary bus (bridge) reset when the device is claimed for passthrough. On some platforms, this bridge reset is not handled cleanly by the device or platform, leaving the PCIe device unresponsive and, in some cases, causing a host reboot during passthrough device initialization. In some cases, the ESX host might fail with a purple diagnostic screen.

**NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller restart**

On ESX hosts using an Emulex Fibre Channel adapter, some NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller reset or reboot. The adapter might show Link Up even though the affected paths remain unavailable after the storage controller is back online. A storage rescan might not restore the affected paths.

**You see BackMap\_Lookup failed logs flooding the vmkernel log**

In the vmkernel.log file, you see multiple warnings for Container Runtime Executive (CRX) virtual machines, such as:

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 4000019c60): Not found

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 400001a137): Not found

This issue affects only CRX VMs and the logs do not indicate an actionable problem.

**ESX host fails after mounting a vSphere Virtual Volumes datastore backed by NFSv3**

Mounting a vSphere Virtual Volumes datastore creates unique TCP connections per server IP address till the number of connections reaches the limit of the MaxConnPerIP parameter. The default value of MaxConnPerIP is 32, but if the parameter is set to a much higher value, such as more than 100, then the total number of connections might exhaust the ports which NFSv3 client can handle. As a result, new mounts might fail and cause the ESX host to fail with a purple diagnostic screen.

**An ESX host might fail with purple diagnostic screen in very rare cases of corruption of slab allocator data structures**

A memory underallocation issue in VMFS in very rare cases might cause corruption of slab allocator data structures. As a result, the ESX host might fail with a purple diagnostic screen.

**You see unrealistic stats or network usage from Broadcom bnxtnet NICs**

The esxcli network nic stats get -n vmnicX command might show inflated or unrealistic stats from Broadcom bnxtnet NICs or in the vSphere Client you see inflated network usage.

The issue is fixed in the inbox driver for 9.1.2.0. For async drivers, upgrade the bnxtnet driver and firmware to 238.x or later.

**Mounting a tardisk with truncated header might cause an ESX host to fail with a purple diagnostic screen**

If the /tmp ramdisk of an ESX host does not have sufficient space when the vSphere Lifecycle Manager mounts a tardisk, a truncation in the end of a tar header might cause the host to fail with a purple diagnostic screen. The presence of function VisorFSTarPopulate() in the backtrace visible in the purple diagnostic screen is indicative of the issue. In the vmkernel.log, you see a line similar to:

WARNING: VisorFSRam: 220: Cannot extend visorfs file /tmp/imgdb-a6he6mo2/imgdb.tgz.bk because its ramdisk (tmp) is full.

**ESX host operations that reload the syslog configuration might fail with an internal error message**

When audit records are enabled on an ESX host, any operation that triggers a syslog configuration reload, such as automated vCenter **Update option value** tasks initiated by the log integration service account, `svc-li-vc-*`, VIB installations or upgrades, or syslog/audit setting changes, might cause the `vmsyslogd` service to connect to every configured `ssl://` remote syslog collector without a connection timeout. If a collector accepts the TCP connection without completing the TLS handshake or silently drops packets without sending a reset, the `vmsyslogd` command thread can block indefinitely, causing the reloads to time out/fail.

In the vSphere Client, you see a message such as:

`A general system error occurred: Internal error.`

In `/var/log/hostd.log` or `esxcli` command output, you see errors such as:

- Timed out while waiting for a response from UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

- Failed to connect to UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

In `/var/log/vmsyslogd.log`, you see records such as:

`Failed to retrieve connection identifiers: Failed to connect the supplied BIO`

The fix enforces bounded deadlines on TLS connect and handshake probes and replaces indefinite socket polling with bounded waits for clean connection recovery.

**ESX hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESX host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

Representative lines from logs:

vmkwarning.log (lwsmd cannot create threads): 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: LinuxThread: 411: lwsmd: Error cloning thread: -12 (bad0014) 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: World: 3234: Could not allocate new world handle for world ID: 6655205: Out of memory 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)uw.2099459 (7773) requires 1024 KB, asked 1024 KB from likewise (7517) which has 93056 KB occupied and 128 KB available. 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)Admission failure in path: host/vim/vmvisor/likewise:lwsmd.2099459:uw.2099459

The lwisOomCheck service now automatically starts together with the Likewise service on ESX hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**Active Directory user or group permissions might be unexpectedly removed from an ESX host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESX host might incorrectly remove permissions to an AD user or group.

The fix makes sure that ESX hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted and preserves permissions in the case of a temporary connectivity failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on** 

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

**Intel Xeon 6 processors utilizing QAT accelerators might see increased boot times on ESX 9.1**

On Intel Xeon 6 processors systems using QAT devices, in some cases, the boot time for ESX hosts might increase.

**ESX hosts might stop updating power consumption data after a Baseboard Management Controller (BMC) reset**

After a reset of the BMC, ESX hosts might stop updating power consumption data from vCenter because the sensord powersvc plugin might be disabled. The sensord service logs errors such as Failed to read from power provider and Too many failures, powersvc offline.

The fix updates the plugin to automatically resume operation after a BMC reset. On affected builds, restart sensord from the ESX shell with the /etc/init.d/sensord restart command to resume power readings.

**The snmpd service might send SNMP traps for past system events logs after a restart**

Whenever the snmpd service is restarted, stale System Event Log (SEL) records might be incorrectly sent as SNMP traps.

**On ESX hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESX hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

The fix increases the default xmapGB value from 32GB to 64GB.

**A race condition in the USB Network adapter in management controllers might cause ESX hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESX hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

**ESX host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESX host fails with a purple diagnostic screen.

**A virtual machine with a vGPU device might fail to allocate memory when system memory usage is high**

In some cases, VMs with vGPUs might consume more than 95% of the physical memory and leave insufficient overhead memory at runtime, which might lead to memory allocation failures.

**An ESX host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESX host might fail with a purple diagnostic screen.

**VMware Tools Bundling Changes in ESX 9.1.2.0**

The following VMware Tools ISO images are bundled with ESX 9.1.2.0:

- : VMware Tools 13.1.10.0 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.windows.iso

The following VMware Tools ISO images are available for download:

- VMware Tools 12.5.5:
  - VMware Tools 12.5.5 supports 64-bit Windows versions.windows.iso:  - VMware Tools 12.4.10 supports 32-bit Windows versions.windows-x86.iso:  - : VMware Tools 10.3.26 ISO image for Linux OS with glibc 2.11 or later.linux.iso

- VMware Tools 11.0.6:
  - : for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).windows.iso

- VMware Tools 10.0.12:
  - : for Windows 2000, Windows XP, and Windows 2003.winPreVista.iso  - : supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with linuxPreGLibc25.iso version earlier than 2.5.glibc
- : VMware Tools image 10.3.10 for Solaris.solaris.iso- : Supports Mac OS X versions 10.11 and later.darwin.iso

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESX:

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

**Provisioning ESX hosts by UEFI HTTPS with the bootloader vbmx64.efi and with a custom image based on OEM strings might fail**

If the software specification you use to provision ESX hosts contains customization based on OEM strings, ESX hosts that boot with UEFI HTTPS might fail to match the correct ESX image.

**An ESX host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESXi host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESX host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

**ESX 9.1.2 includes the following Intel microcode:**

Code Name

FMS

Plat ID

Servicing

MCU Rev

MCU Date

Brand Names

Sandy Bridge DT

0x206a7 (06/2a/7)

0x12

baseline

0x2f

2/17/2019

Intel Xeon E3-1100 Series;

Intel Xeon E3-1200 Series;

Intel i7-2655-LE Series;

Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series;

Intel i7-3500-LE/UE;

Intel i7-3600-QE;

Intel Xeon E3-1200-v2 Series;

Intel Xeon E3-1100-C-v2 Series;

Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series;

Intel i7-4700-EQ Series;

Intel i5-4500-TE Series;

Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series;

Intel Xeon E5-2600-v2 Series;

Intel Xeon E5-2400-v2 Series;

Intel Xeon E5-1600-v2 Series;

Intel Xeon E5-1400-v2 Series

Ivy Bridge EX

0x306e7 (06/3e/7)

0xed

baseline

0x715

3/14/2019

Intel Xeon E7-8800/4800/2800-v2 Series

Haswell EP

0x306f2 (06/3f/2)

0x6f

baseline

0x49

8/11/2021

Intel Xeon E5-4600-v3 Series;

Intel Xeon E5-2600-v3 Series;

Intel Xeon E5-2400-v3 Series;

Intel Xeon E5-1600-v3 Series;

Intel Xeon E5-1400-v3 Series

Haswell EX

0x306f4 (06/3f/4)

0x80

baseline

0x1a

5/24/2021

Intel Xeon E7-8800/4800-v3 Series

Broadwell H

0x40671 (06/47/1)

0x22

baseline

0x22

11/12/2019

Intel Core i7-5700EQ;

Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series;

Intel Atom C2500 Series;

Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series;

Intel Xeon E5-4600-v4 Series;

Intel Xeon E5-2600-v4 Series;

Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series;

Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series;

Intel Xeon D-2100 Series;

Intel Xeon D-1600 Series;

Intel Xeon W-3100 Series;

Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300

Broadwell DE

0x50662 (06/56/2)

0x10

baseline

0x1c

6/17/2019

Intel Xeon D-1500 Series

Broadwell DE

0x50663 (06/56/3)

0x10

baseline

0x700001c

6/12/2021

Intel Xeon D-1500 Series

Broadwell DE

0x50664 (06/56/4)

0x10

baseline

0xf00001a

6/12/2021

Intel Xeon D-1500 Series

Broadwell NS

0x50665 (06/56/5)

0x10

baseline

0xe000015

8/3/2023

Intel Xeon D-1600 Series

Skylake H/S

0x506e3 (06/5e/3)

0x36

baseline

0xf0

11/12/2021

Intel Xeon E3-1500-v5 Series;

Intel Xeon E3-1200-v5 Series

Denverton

0x506f1 (06/5f/1)

0x01

baseline

0x3e

10/5/2023

Intel Atom C3000 Series

Ice Lake SP

0x606a6 (06/6a/6)

0x87

baseline

0xd000433

3/9/2026

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300 Series;

Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series;

Intel Xeon D-1700 Series

Snow Ridge

0x80665 (06/86/5)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Snow Ridge

0x80667 (06/86/7)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Tiger Lake U

0x806c1 (06/8c/1)

0x80

baseline

0xbe

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake U Refresh

0x806c2 (06/8c/2)

0xc2

baseline

0x3e

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake H

0x806d1 (06/8d/1)

0xc2

baseline

0x58

7/24/2025

Intel Xeon W-11000E Series

Sapphire Rapids SP HBM

0x806f8 (06/8f/8)

0x10

baseline

0x2c000435

3/2/2026

Intel Xeon Max 9400 Series

Sapphire Rapids SP

0x806f8 (06/8f/8)

0x87

baseline

0x2b000690

5/28/2026

Intel Xeon Platinum 8400 Series;

Intel Xeon Gold 6400/5400 Series;

Intel Xeon Silver 4400 Series;

Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series;

Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series;

Intel Xeon E-2200 Series (4 or 6 core)

Coffee Lake

0x906eb (06/9e/b)

0x02

baseline

0xf6

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake

0x906ec (06/9e/c)

0x22

baseline

0xf8

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake Refresh

0x906ed (06/9e/d)

0x22

baseline

0x104

11/14/2024

Intel Xeon E-2200 Series (8 core)

Rocket Lake S

0xa0671 (06/a7/1)

0x02

baseline

0x66

2/12/2026

Intel Xeon E-2300 Series

Granite Rapids SP R1S

0xa06d1 (06/ad/1)

0x20

baseline

0xa000164

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000444

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003c4

7/2/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Emerald Rapids SP

0xc06f2 (06/cf/2)

0x87

baseline

0x21000300

6/9/2026

Intel Xeon 8500 Series;

Intel Xeon Gold 6500/5500 Series;

Intel Xeon Silver 4500 Series;

Intel Xeon Bronze 3500 Series

**QuickBoot might fail with memory allocation error on platforms with several TB of DRAM**

A memory allocation error might cause QuickBoot to fail on platforms with large amount of memory, such as several TB of DRAM. In /var/run/log/loadESX.log, you can see the following errors:

2026-09-07T15:42:25.768Z +ERROR loadESX 2103140 \[esx@4413\] loadesxLive.utils.LoadESXMgmtError: LoadESXMgmtError - LoadESX management command 19 failed (status: 0xbad0014)

At approximately the same timestamp, the following error appears in the vmkernel logs:

2026-09-07T15:42:25.590Z -INFO vmkernel - \[esx@4413\] cpu665:2103140)LoadESX: LoadESXMgmtInstallVMKBoot:1135: Failed to allocate memory for vmkboot

**ESX 9.1.2.0 includes the following AMD microcode:**

Code Name

FMS

MCU Rev

MCU Date

Brand Names

Bulldozer

0x00600f12 (15/01/2)

0x0600063e

2/7/2018

Opteron 6200/4200/3200 Series

Piledriver

0x00600f20 (15/02/0)

0x06000852

2/6/2018

Opteron 6300/4300/3300 Series

Zen-Naples

0x00800f12 (17/01/2)

0x08001278

11/11/2024

EPYC 7001 Series

Zen2-Rome

0x00830f10 (17/31/0)

0x0830107c

12/18/2023

EPYC 7002/7Fx2/7Hx2 Series

Zen3-Milan

0x00a00f11 (19/01/1)

0x0a0011de

4/18/2025

EPYC 7003 Series

Zen3-Milan (old BIOS)

0x00a00f11 (19/01/1)

0x0a0011d5

2/23/2024

EPYC 7003 Series

Zen3-Milan-X

0x00a00f12 (19/01/2)

0x0a001247

3/27/2025

EPYC 7003X Series

Zen3-Milan-X (old BIOS)

0x00a00f12 (19/01/2)

0x0a001238

2/26/2024

EPYC 7003X Series

Zen4-Genoa

0x00a10f11 (19/11/1)

0x0a101158

6/9/2025

EPYC 9004 Series

Zen4-Genoa (old BIOS)

0x00a10f11 (19/11/1)

0x0a101148

2/23/2024

EPYC 9004 Series

Zen4-Genoa-X

0x00a10f12 (19/11/2)

0x0a101253

6/12/2025

EPYC 9004X Series

Zen4-Genoa-X (old BIOS)

0x00a10f12 (19/11/2)

0x0a101248

2/26/2024

EPYC 9004X Series

Zen4-Bergamo/Siena

0x00aa0f02 (19/a0/2)

0x0aa0021c

6/12/2025

EPYC 8004/9004 Series

Zen4-Bergamo/Siena (old BIOS)

0x00aa0f02 (19/a0/2)

0x0aa00215

2/28/2024

EPYC 8004/9004 Series

Zen5-Turin

0x00b00f21 (1a/02/1)

0x0b002175

5/28/2026

EPYC 9005 Series

Zen5-Turin-Dense

0x00b10f10 (1a/11/0)

0x0b101066

5/28/2026

EPYC 9005 Series

## ESXi-9.1.2.0-25946735-no-tools

**Profile Name**

ESXi-9.1.2.0-25946735-no-tools

**Build**

For build information, see Patches Contained in This Release.

**Vendor**

Broadcom, Inc.

**Release Date**

November 24, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

Same list as in the ESXi-9.1.2.0-25946735-standard image profile except the VMware\_locker\_tools-light\_13.1.10-0.25946735.vib

**Related CVE numbers**

CVE-2026-123910, CVE-2026-123911, CVE-2026-123913, CVE-2026-123915

**This patch resolves the following issues:**

**Nested virtual machines fail on ESX hosts with Windows guest OS on AMD CPUs**

When the guest hypervisor in nested VMs transitions between virtual environments, the CPU might retain stale address translation entries in its Translation Lookaside Buffer (TLB). On AMD processors, if such entries are not properly removed during the context switch, they might cause faults that lead to failure of the guest OS. As a result, nested virtual environments, such as WSL2 in a Windows VM, might fail or become unresponsive.

**NVIDIA MIG-backed vGPU devices that do not provide both Multi-Instance GPU (MIG) and time-slicing sharing methods might cause the hostd service to fail**

The hostd process assumes that an NVIDIA device provides vGPU MIG information in parallel with time-sliced information and if one is not present, the service might fail.

**During removal of NVMe namespaces on the target array, an ESX host might fail with a purple diagnostic screen**

Rarely, during the removal of NVMe namespaces on the target array, a race condition can occur in ESX when processing notifications from the array. As a result, the ESX host might fail with a purple diagnostic screen.

**An ESX host unexpectedly reboots or fails when powering on a virtual machine configured with a Marvell QLogic Fibre Channel (FC) HBA attached by PCI passthrough**

Marvell QLogic FC adapters do not support Function Level Reset (FLR). By default, ESX falls back to resetting such devices by using a secondary bus (bridge) reset when the device is claimed for passthrough. On some platforms, this bridge reset is not handled cleanly by the device or platform, leaving the PCIe device unresponsive and, in some cases, causing a host reboot during passthrough device initialization. In some cases, the ESX host might fail with a purple diagnostic screen.

**NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller restart**

On ESX hosts using an Emulex Fibre Channel adapter, some NVMe/FC or SCSI over Fibre Channel paths might not restore after a storage controller reset or reboot. The adapter might show Link Up even though the affected paths remain unavailable after the storage controller is back online. A storage rescan might not restore the affected paths.

**You see BackMap\_Lookup failed logs flooding the vmkernel log**

In the vmkernel.log file, you see multiple warnings for Container Runtime Executive (CRX) virtual machines, such as:

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 4000019c60): Not found

2026-03-16T17:52:43.727Z cpu11:3177077)WARNING: VmMemSample: 1024: BackMap\_Lookup failed (bpn 400001a137): Not found

This issue affects only CRX VMs and the logs do not indicate an actionable problem.

**ESX host fails after mounting a vSphere Virtual Volumes datastore backed by NFSv3**

Mounting a vSphere Virtual Volumes datastore creates unique TCP connections per server IP address till the number of connections reaches the limit of the MaxConnPerIP parameter. The default value of MaxConnPerIP is 32, but if the parameter is set to a much higher value, such as more than 100, then the total number of connections might exhaust the ports which NFSv3 client can handle. As a result, new mounts might fail and cause the ESX host to fail with a purple diagnostic screen.

**An ESX host might fail with purple diagnostic screen in very rare cases of corruption of slab allocator data structures**

A memory underallocation issue in VMFS in very rare cases might cause corruption of slab allocator data structures. As a result, the ESX host might fail with a purple diagnostic screen.

**You see unrealistic stats or network usage from Broadcom bnxtnet NICs**

The esxcli network nic stats get -n vmnicX command might show inflated or unrealistic stats from Broadcom bnxtnet NICs or in the vSphere Client you see inflated network usage.

The issue is fixed in the inbox driver for 9.1.2.0. For async drivers, upgrade the bnxtnet driver and firmware to 238.x or later.

**Mounting a tardisk with truncated header might cause an ESX host to fail with a purple diagnostic screen**

If the /tmp ramdisk of an ESX host does not have sufficient space when the vSphere Lifecycle Manager mounts a tardisk, a truncation in the end of a tar header might cause the host to fail with a purple diagnostic screen. The presence of function VisorFSTarPopulate() in the backtrace visible in the purple diagnostic screen is indicative of the issue. In the vmkernel.log, you see a line similar to:

WARNING: VisorFSRam: 220: Cannot extend visorfs file /tmp/imgdb-a6he6mo2/imgdb.tgz.bk because its ramdisk (tmp) is full.

**ESX host operations that reload the syslog configuration might fail with an internal error message**

When audit records are enabled on an ESX host, any operation that triggers a syslog configuration reload, such as automated vCenter **Update option value** tasks initiated by the log integration service account, `svc-li-vc-*`, VIB installations or upgrades, or syslog/audit setting changes, might cause the `vmsyslogd` service to connect to every configured `ssl://` remote syslog collector without a connection timeout. If a collector accepts the TCP connection without completing the TLS handshake or silently drops packets without sending a reset, the `vmsyslogd` command thread can block indefinitely, causing the reloads to time out/fail.

In the vSphere Client, you see a message such as:

`A general system error occurred: Internal error.`

In `/var/log/hostd.log` or `esxcli` command output, you see errors such as:

- Timed out while waiting for a response from UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

- Failed to connect to UDS socket /var/run/vmwSyslogCmd: Resource temporarily unavailable

In `/var/log/vmsyslogd.log`, you see records such as:

`Failed to retrieve connection identifiers: Failed to connect the supplied BIO`

The fix enforces bounded deadlines on TLS connect and handshake probes and replaces indefinite socket polling with bounded waits for clean connection recovery.

**ESX hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESX host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

Representative lines from logs:

vmkwarning.log (lwsmd cannot create threads): 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: LinuxThread: 411: lwsmd: Error cloning thread: -12 (bad0014) 2026-04-26T08:55:17.584Z Wa(180) vmkwarning: cpu36:2099471)WARNING: World: 3234: Could not allocate new world handle for world ID: 6655205: Out of memory 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)uw.2099459 (7773) requires 1024 KB, asked 1024 KB from likewise (7517) which has 93056 KB occupied and 128 KB available. 2026-04-29T03:07:39.230Z In(182) vmkernel: cpu32:2099475)Admission failure in path: host/vim/vmvisor/likewise:lwsmd.2099459:uw.2099459

The lwisOomCheck service now automatically starts together with the Likewise service on ESX hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**Active Directory user or group permissions might be unexpectedly removed from an ESX host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESX host might incorrectly remove permissions to an AD user or group.

The fix makes sure that ESX hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted and preserves permissions in the case of a temporary connectivity failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on** 

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

**Intel Xeon 6 processors utilizing QAT accelerators might see increased boot times on ESX 9.1**

On Intel Xeon 6 processors systems using QAT devices, in some cases, the boot time for ESX hosts might increase.

**ESX hosts might stop updating power consumption data after a Baseboard Management Controller (BMC) reset**

After a reset of the BMC, ESX hosts might stop updating power consumption data from vCenter because the sensord powersvc plugin might be disabled. The sensord service logs errors such as Failed to read from power provider and Too many failures, powersvc offline.

The fix updates the plugin to automatically resume operation after a BMC reset. On affected builds, restart sensord from the ESX shell with the /etc/init.d/sensord restart command to resume power readings.

**The snmpd service might send SNMP traps for past system events logs after a restart**

Whenever the snmpd service is restarted, stale System Event Log (SEL) records might be incorrectly sent as SNMP traps.

**On ESX hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESX hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

The fix increases the default xmapGB value from 32GB to 64GB.

**A race condition in the USB Network adapter in management controllers might cause ESX hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESX hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

**ESX host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESX host fails with a purple diagnostic screen.

**A virtual machine with a vGPU device might fail to allocate memory when system memory usage is high**

In some cases, VMs with vGPUs might consume more than 95% of the physical memory and leave insufficient overhead memory at runtime, which might lead to memory allocation failures.

**An ESX host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESX host might fail with a purple diagnostic screen.

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

**Provisioning ESX hosts by UEFI HTTPS with the bootloader vbmx64.efi and with a custom image based on OEM strings might fail**

If the software specification you use to provision ESX hosts contains customization based on OEM strings, ESX hosts that boot with UEFI HTTPS might fail to match the correct ESX image.

**An ESX host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESX host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESX host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

**ESX 9.1.2 includes the following Intel microcode:**

Code Name

FMS

Plat ID

Servicing

MCU Rev

MCU Date

Brand Names

Sandy Bridge DT

0x206a7 (06/2a/7)

0x12

baseline

0x2f

2/17/2019

Intel Xeon E3-1100 Series;

Intel Xeon E3-1200 Series;

Intel i7-2655-LE Series;

Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series;

Intel Xeon E5-1400 Series;

Intel Xeon E5-1600 Series;

Intel Xeon E5-2400 Series;

Intel Xeon E5-2600 Series;

Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series;

Intel i7-3500-LE/UE;

Intel i7-3600-QE;

Intel Xeon E3-1200-v2 Series;

Intel Xeon E3-1100-C-v2 Series;

Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series;

Intel i7-4700-EQ Series;

Intel i5-4500-TE Series;

Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series;

Intel Xeon E5-2600-v2 Series;

Intel Xeon E5-2400-v2 Series;

Intel Xeon E5-1600-v2 Series;

Intel Xeon E5-1400-v2 Series

Ivy Bridge EX

0x306e7 (06/3e/7)

0xed

baseline

0x715

3/14/2019

Intel Xeon E7-8800/4800/2800-v2 Series

Haswell EP

0x306f2 (06/3f/2)

0x6f

baseline

0x49

8/11/2021

Intel Xeon E5-4600-v3 Series;

Intel Xeon E5-2600-v3 Series;

Intel Xeon E5-2400-v3 Series;

Intel Xeon E5-1600-v3 Series;

Intel Xeon E5-1400-v3 Series

Haswell EX

0x306f4 (06/3f/4)

0x80

baseline

0x1a

5/24/2021

Intel Xeon E7-8800/4800-v3 Series

Broadwell H

0x40671 (06/47/1)

0x22

baseline

0x22

11/12/2019

Intel Core i7-5700EQ;

Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series;

Intel Atom C2500 Series;

Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series;

Intel Xeon E5-4600-v4 Series;

Intel Xeon E5-2600-v4 Series;

Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series;

Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series;

Intel Xeon D-2100 Series;

Intel Xeon D-1600 Series;

Intel Xeon W-3100 Series;

Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series;

Intel Xeon Gold 6200/5200;

Intel Xeon Silver 4200/Bronze 3200;

Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300

Broadwell DE

0x50662 (06/56/2)

0x10

baseline

0x1c

6/17/2019

Intel Xeon D-1500 Series

Broadwell DE

0x50663 (06/56/3)

0x10

baseline

0x700001c

6/12/2021

Intel Xeon D-1500 Series

Broadwell DE

0x50664 (06/56/4)

0x10

baseline

0xf00001a

6/12/2021

Intel Xeon D-1500 Series

Broadwell NS

0x50665 (06/56/5)

0x10

baseline

0xe000015

8/3/2023

Intel Xeon D-1600 Series

Skylake H/S

0x506e3 (06/5e/3)

0x36

baseline

0xf0

11/12/2021

Intel Xeon E3-1500-v5 Series;

Intel Xeon E3-1200-v5 Series

Denverton

0x506f1 (06/5f/1)

0x01

baseline

0x3e

10/5/2023

Intel Atom C3000 Series

Ice Lake SP

0x606a6 (06/6a/6)

0x87

baseline

0xd000433

3/9/2026

Intel Xeon Platinum 8300 Series;

Intel Xeon Gold 6300/5300 Series;

Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series;

Intel Xeon D-1700 Series

Snow Ridge

0x80665 (06/86/5)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Snow Ridge

0x80667 (06/86/7)

0x01

baseline

0x4c000026

2/28/2024

Intel Atom P5000 Series

Tiger Lake U

0x806c1 (06/8c/1)

0x80

baseline

0xbe

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake U Refresh

0x806c2 (06/8c/2)

0xc2

baseline

0x3e

7/24/2025

Intel Core i3/i5/i7-1100 Series

Tiger Lake H

0x806d1 (06/8d/1)

0xc2

baseline

0x58

7/24/2025

Intel Xeon W-11000E Series

Sapphire Rapids SP HBM

0x806f8 (06/8f/8)

0x10

baseline

0x2c000435

3/2/2026

Intel Xeon Max 9400 Series

Sapphire Rapids SP

0x806f8 (06/8f/8)

0x87

baseline

0x2b000690

5/28/2026

Intel Xeon Platinum 8400 Series;

Intel Xeon Gold 6400/5400 Series;

Intel Xeon Silver 4400 Series;

Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series;

Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series;

Intel Xeon E-2200 Series (4 or 6 core)

Coffee Lake

0x906eb (06/9e/b)

0x02

baseline

0xf6

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake

0x906ec (06/9e/c)

0x22

baseline

0xf8

2/1/2024

Intel Xeon E-2100 Series

Coffee Lake Refresh

0x906ed (06/9e/d)

0x22

baseline

0x104

11/14/2024

Intel Xeon E-2200 Series (8 core)

Rocket Lake S

0xa0671 (06/a7/1)

0x02

baseline

0x66

2/12/2026

Intel Xeon E-2300 Series

Granite Rapids SP R1S

0xa06d1 (06/ad/1)

0x20

baseline

0xa000164

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000444

7/1/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003c4

7/2/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Emerald Rapids SP

0xc06f2 (06/cf/2)

0x87

baseline

0x21000300

6/9/2026

Intel Xeon 8500 Series;

Intel Xeon Gold 6500/5500 Series;

Intel Xeon Silver 4500 Series;

Intel Xeon Bronze 3500 Series

**QuickBoot might fail with memory allocation error on platforms with several TB of DRAM**

A memory allocation error might cause QuickBoot to fail on platforms with large amount of memory, such as several TB of DRAM. In /var/run/log/loadESX.log, you can see the following errors:

2026-09-07T15:42:25.768Z +ERROR loadESX 2103140 \[esx@4413\] loadesxLive.utils.LoadESXMgmtError: LoadESXMgmtError - LoadESX management command 19 failed (status: 0xbad0014)

At approximately the same timestamp, the following error appears in the vmkernel logs:

2026-09-07T15:42:25.590Z -INFO vmkernel - \[esx@4413\] cpu665:2103140)LoadESX: LoadESXMgmtInstallVMKBoot:1135: Failed to allocate memory for vmkboot

**ESX 9.1.2.0 includes the following AMD microcode:**

Code Name

FMS

MCU Rev

MCU Date

Brand Names

Bulldozer

0x00600f12 (15/01/2)

0x0600063e

2/7/2018

Opteron 6200/4200/3200 Series

Piledriver

0x00600f20 (15/02/0)

0x06000852

2/6/2018

Opteron 6300/4300/3300 Series

Zen-Naples

0x00800f12 (17/01/2)

0x08001278

11/11/2024

EPYC 7001 Series

Zen2-Rome

0x00830f10 (17/31/0)

0x0830107c

12/18/2023

EPYC 7002/7Fx2/7Hx2 Series

Zen3-Milan

0x00a00f11 (19/01/1)

0x0a0011de

4/18/2025

EPYC 7003 Series

Zen3-Milan (old BIOS)

0x00a00f11 (19/01/1)

0x0a0011d5

2/23/2024

EPYC 7003 Series

Zen3-Milan-X

0x00a00f12 (19/01/2)

0x0a001247

3/27/2025

EPYC 7003X Series

Zen3-Milan-X (old BIOS)

0x00a00f12 (19/01/2)

0x0a001238

2/26/2024

EPYC 7003X Series

Zen4-Genoa

0x00a10f11 (19/11/1)

0x0a101158

6/9/2025

EPYC 9004 Series

Zen4-Genoa (old BIOS)

0x00a10f11 (19/11/1)

0x0a101148

2/23/2024

EPYC 9004 Series

Zen4-Genoa-X

0x00a10f12 (19/11/2)

0x0a101253

6/12/2025

EPYC 9004X Series

Zen4-Genoa-X (old BIOS)

0x00a10f12 (19/11/2)

0x0a101248

2/26/2024

EPYC 9004X Series

Zen4-Bergamo/Siena

0x00aa0f02 (19/a0/2)

0x0aa0021c

6/12/2025

EPYC 8004/9004 Series

Zen4-Bergamo/Siena (old BIOS)

0x00aa0f02 (19/a0/2)

0x0aa00215

2/28/2024

EPYC 8004/9004 Series

Zen5-Turin

0x00b00f21 (1a/02/1)

0x0b002175

5/28/2026

EPYC 9005 Series

Zen5-Turin-Dense

0x00b10f10 (1a/11/0)

0x0b101066

5/28/2026

EPYC 9005 Series
