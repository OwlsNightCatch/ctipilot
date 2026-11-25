---
title: VMware ESXi 8.0 Update 3m Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3m-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-11-23"
fingerprint: f44f5e3d5e3850da
language: en
pagetype: article
filedate: "2026-11-25"
---
# VMware ESXi 8.0 Update 3m Release Notes

This document contains the following sections

## Introduction

VMware ESXi 8.0 Update 3m | 19 NOV 2026 | Build 25926933

Check for additions and updates to these release notes.

## What's New

This release delivers fixes as described in the Resolved Issues section.

**Capsule PK Update:**

ESXi 8.0 Update 3m enables a secure mechanism to safely update the out-of-date NULL PK on Secure Boot-enabled, vTPM-enabled Windows virtual machines during a guest reboot without interrupting TPM-based applications. The Capsule PK update driver triggering the PK update is available starting in VMware Tools 13.1.5 or 12.5.5 for supported Windows versions, except Windows Server 2016, Windows 10 64-bit 22H2, and 1809, which will be supported in a future VMware Tools release. For the Capsule PK update, the July 2026 Windows Cumulative Update or later is required. You must install this cumulative update before installing or upgrading VMware Tools to version 13.1.5 or 12.5.5, or newer, to allow the installation of the PK update driver, except for Windows Server 2025, Windows 11 25H2, and 24H2.

For more information, see Broadcom knowledge base article [423893](https://knowledge.broadcom.com/external/article/423893).

## Build Details

## VMware ESXi 8.0 Update 3m

**VMware vSphere Hypervisor (ESXi ISO) image**

**Download Filename**:

VMware-VMvisor-Installer-8.0U3m-25926933.x86\_64.iso

**Build**:

25926933

**Download Size**:

634 MB

**SHA256 checksum**:

a0ab7dac0db384616bffe0696d41bd57e3e015197e0151073c8b60a9ce26b301

**Host Reboot Required**:

Yes

**Virtual Machine Migration or Shutdown Required**:

Yes

**VMware vSphere Hypervisor (ESXi) Offline Bundle**

**Download Filename**:

VMware-ESXi-8.0U3m-25926933-depot.zip

**Build**:

25926933

**Download Size**:

983 MB

**SHA256 checksum:**

8c321604f77ad07bb552b91a6483feb5d6e449d6cb76496ba63930435c9d5bd3

**Host Reboot Required**:

Yes

**Virtual Machine Migration or Shutdown Required**:

Yes

**Components**

**Component**

**Bulletin**

**Category**

**Severity**

ESXi Component - core ESXi VIBs

ESXi\_8.0.3-0.106.25926933

Bugfix

Critical

ESXi Install/Upgrade Component

esx-update\_8.0.3-0.106.25926933

Bugfix

Critical

ESXi Install/Upgrade Component

esxio-update\_8.0.3-0.106.25926933

Bugfix

Critical

Broadcom Emulex Connectivity Division lpfc driver for FC adapters

Broadcom-ELX-lpfc\_14.4.0.50-35vmw.803.0.106.25926933

Bugfix

Critical

USB Native Driver for VMware

VMware-vmkusb\_0.1-26vmw.803.0.106.25926933

Bugfix

Critical

ESXi Component - core ESXi VIBs

ESXi\_8.0.3-0.104.25926924

Security

Critical

ESXi Install/Upgrade Component

esx-update\_8.0.3-0.104.25926924

Security

Critical

ESXi Install/Upgrade Component

esxio-update\_8.0.3-0.104.25926924

Security

Critical

Broadcom Emulex Connectivity Division lpfc driver for FC adapters

Broadcom-ELX-lpfc\_14.4.0.48-35vmw.803.0.104.25926924

Security

Critical

Mellanox 5th generation NICs (ConnectX and BlueField DPU series) core Ethernet and RoCE Drivers for VMware ESXi

Mellanox-nmlx5\_4.23.9.1-1vmw.803.0.104.25926924

Security

Critical

Host Based Replication Server for ESX

VMware-HBR-UW\_8.0.3-0.104.25926924

Security

Critical

VMware NVMe over TCP Driver

VMware-NVMeoF-TCP\_1.0.1.38-1vmw.803.0.104.25926924

Security

Critical

ESXi Tools Component

VMware-VM-Tools\_12.5.5.25704436-25926924

Security

Critical

Network ENS driver for VMware vmxnet3 Virtual Ethernet Controller

VMware-nvmxnet3-ens\_2.0.0.23-7vmw.803.0.104.25926924

Security

Critical

Network driver for VMware vmxnet3 Virtual Ethernet Controller

VMware-nvmxnet3\_2.0.0.31-13vmw.803.0.104.25926924

Security

Critical

**Rollup Bulletins**

These rollup bulletins contain the latest VIBs with all the fixes after the initial release of ESXi 8.0.

**Bulletin ID**

**Category**

**Severity**

**Detail**

ESXi80U3m-25926933

Bugfix

Critical

Bugfix and Security image

ESXi80U3sm-25926924

Security

Critical

Security only image

**Image Profiles**

VMware patch and update releases contain general and critical image profiles. Application of the general release image profile applies to new bug fixes.

**Image Profile Name**

ESXi-8.0U3m-25926933-standard

ESXi-8.0U3m-25926933-no-tools

ESXi-8.0U3sm-25926924-standard

ESXi-8.0U3sm-25926924-no-tools

**ESXi Images**

Name and Version

Release Date

Live Patchable

Category

Detail

ESXi 8.0 U3m - 25926933

19 November 2026

No

General

Bugfix and Security image

ESXi 8.0 U3sm - 25926924

19 November 2026

No

Security

Security only

## Patch Download and Installation

Log in to the [Broadcom Support Portal](https://support.broadcom.com) to download this [patch](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16136).

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).

For details on updates and upgrades by using vSphere Lifecycle Manager, see [About vSphere Lifecycle Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/about-vsphere-lifecycle-manager-new.html) and [vSphere Lifecycle Manager Baselines and Images](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle-8-0/about-vsphere-lifecycle-manager-new/vlcm-baselines-and-images.html). You can also update ESXi hosts without the use of vSphere Lifecycle Manager by using an image profile. To do this, you must manually download the patch offline bundle ZIP file or see the KB [Download latest ISOs and patches for vSphere ESXi](https://knowledge.broadcom.com/external/article/372545/download-esxi-patch-and-the-isos-for-lat.html)[.](https://knowledge.broadcom.com/external/article/372545/download-esxi-patch-and-the-isos-for-lat.html)

For more information, see the [Upgrading Hosts by Using ESXCLI Commands](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-upgrade-8-0/upgrading-esxi-hosts-upgrade/how-to-upgrade-hosts-by-using-esxcli-commands-upgrade/upgrading-hosts-using-by-esxcli-commands-upgrade.html#GUID-A4301ADA-8E02-459D-BF9D-0AD308DA5325-en) and the [VMware ESXi Upgrade](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-esxi-upgrade/GUID-65B5B313-3DBB-4490-82D2-A225446F4C99.html) guide.

## Resolved Issues

## ESXi\_8.0.3-0.106.25926933

**Patch Category**

Bugfix

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

- VMware\_bootbank\_esxio-combiner\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsan\_8.0.3-0.106.25926933
- VMware\_bootbank\_infravisor\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsanhealth\_8.0.3-0.106.25926933
- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc\_8.0.3-0.106.25926933
- VMware\_bootbank\_vdfs\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-xserver\_8.0.3-0.106.25926933
- VMware\_bootbank\_vds-vsip\_8.0.3-0.106.25926933
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_clusterstore\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_trx\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.106.25926933

**PRs Fixed**

N/A

**CVE numbers**

N/A

The ESXi and esx-update bulletins are dependent on each other. Always include both in a single ESXi host patch baseline or include the rollup bulletin in the baseline to avoid failure during host patching.

This patch updates the esxio-combiner, vsan, infravisor, esxio-dvfilter-generic-fastpath, crx, bmcal, vsanhealth, drivervm-gpu-base, gc, vdfs, native-misc-drivers-esxio, esx-base, esx-dvfilter-generic-fastpath, esx-xserver, vds-vsip, cpu-microcode, esxio, clusterstore, esxio-base, trx, gc-esxio, esxio-combiner-esxio, bmcal-esxio, vcls-pod-crx, native-misc-drivers , and esx-ui VIBs.

This patch resolves the following issues:

**Virtual machines on an AMD processor might fail after NUMA migration of the hypervisor internal data due to a race condition**

If a vCPU moves to another processor during a hypervisor NUMA migration, a race condition might cause an update of the old copy of some hypervisor data instead of the new one. The VM continues to work with out-of-date information and ultimately fails.

This issue is resolved in this release.

**vSphere Replication-protected virtual machines become unresponsive or display as invalid due to a race condition during placing an ESXi host into maintenance mode or a cluster update**

During ESXi host maintenance or remediation, virtual machines protected by vSphere Replication are automatically paused or reconfigured. A rare race condition in the vSphere Replication filter driver might lead to an internal deadlock that prevents virtual machine disk operations from completing. As a result, reconfiguration tasks and vSphere vMotion migration tasks might time out, which leaves affected virtual machines in an invalid state. vSphere Replication-protected virtual machines become unresponsive and cannot go out of maintenance mode.

This issue is resolved in this release. After upgrading to ESXi 8.0 Update 3m, reboot affected ESXi hosts to restore normal operations.

**After remediation with reboot, vCenter services might not be available on ESXi hosts that use internal service accounts**

Remediating the vSphere Configuration Profiles configuration might delete the svc-vcf- service accounts, which are internally managed user accounts, on ESXi hosts that reboot after the remediation. As a result, some vCenter services might not be available on such ESXi hosts. For example, the creation of a vSAN stretched cluster fails at an internal step: Disable SSH on hosts.

This issue is resolved in this release.

**Image compliance on a DPU host shows as Unknown due to a timeout**

Due to the processing of content from online depots, the DPU scan API call might spend more than the limit of 2 min before a timeout. As a result, you see the check compliance status of DPUs on the ESXi host as Unknown.

In the ESXi logs, /var/run/log/lifecycle.log, you see an error such as:

2025-09-19T15:14:41Z Er(11) lifecycle\[2124459\]: TaskBase:210 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) timedout

2025-09-19T15:14:41Z In(14) lifecycle\[2124459\]: TaskBase:261 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) finished with state TIMEDOUT ...

The issue has no specific trigger and you might see it during a routine compliance scan, but the occurrence is random, not with every compliance check, and is not related to any specific DPU type.

This issue is resolved in this release.

**Virtual machines cannot power on due to a "Module 'DevicePowerOn' power on failed" error**

Due to a string conversion issue, VMs using passthrough devices might fail to power-on even when suitable passthrough devices are available.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen while connecting a USB 3.1 HDD using PCI passthrough to a virtual machine**

An ESXi host might fail with a purple diagnostic screen while connecting a device that utilizes Reserved Memory Region Reporting (RMRR) using PCI passthrough to a VM with vIOMMU option selected (vvtd.enable = TRUE in the .vmx file), since this configuration is not supported.

This issue is resolved in this release. The fix ensures that the VM fails to power on with an error message instead of purple diagnostic screen failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on**

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

This issue is resolved in this release.

**Add Host task in the vSphere Client might fail due to an internal timeout**

Due to a timeout in the internal HTTP client during an Add Host operation in the vSphere Client, you might see such tasks take long and eventually fail.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**Migration of a VM with an NVIDIA vGPU passthrough device fails when migrating from ESXi 7.x to ESXi 8.x**

vSphere vMotion migration of a virtual machine with an NVIDIA vGPU passthrough device from an ESXi 7.x host to 8.x host might fail with an IOMMU adjustment panic error in the vmware.log file. In the vSphere Client, you see the error: The remote host closed the connection unexpectedly and migration has stopped. The closed connection probably results from a migration failure detected on the remote host.

This issue is resolved in this release. Upgrade the destination ESXi hosts to version 8.0 Update 3m or later.

**Scheduling delays when high-priority processes are placed on a busy physical CPU might cause packets drop**

When high-priority processes, for example in an Enhanced Network Stack (ENS) context, are placed on a busy physical CPU, they rely on the virtual CPU migration algorithm to move them to an idle or less busy CPU as appropriate. An issue with the migration algorithm might cause such processes to stay on the busy CPU for extended periods, causing significant scheduling delays, or high CPU Ready Time. As a result, you might see packets drop.

This issue is resolved in this release.

**Active Directory user or group permissions might be unexpectedly removed from an ESXi host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESXi host might incorrectly remove permissions to an AD user or group.

This issue is resolved in this release. The fix makes sure that ESXi hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted, and preserves permissions in the case of a temporary connectivity failure.

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

This issue is resolved in this release.

**On ESXi hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESXi hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

This issue is resolved in this release. The fix increases the default xmapGB value from 32GB to 64GB.

**ESXi hosts run out of file descriptors during high-volume VM operations, ultimately causing VM power-on failures**

On an ESXi host handling a high volume of concurrent VM power-on and vSphere vMotion operations, the Object Store File System Daemon (osfsd) might exhaust its file handle pool, reporting No free handles and VMK\_TOO\_MANY\_FILES errors. As a result, further VM power-on attempts on such hosts fail with a vim.fault.GenericVmConfigFault error in vCenter logs.

This issue is resolved in this release.

**An ESXi host fails with a purple diagnostic screen during SEsparse disk consolidation**

In extremely rare cases, during a write operation on a thin VMDK, due to an issue with the memory allocation for internal data structures, a buffer-overrun can cause failure of the slab memory allocation system. As a result, the ESXi host might fail with a purple diagnostic screen. The backtrace contains errors such as FastSlabCreateObj, FastSlabReplenishCPU, FastSlabAllocSlow, and the vmkernel.log messages show WARNING: Heartbeat: PCPU ## didn't have a heartbeat followed by ALERT: NMI: NMI IPI. The issue is specific to high I/O operations during SEsparse disk consolidation.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen during I/O to a storage device**

A race condition in the I/O scheduler might free a per-device I/O queue while a new I/O request is in the process of marking that same queue active again. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESXi host might fail with a purple diagnostic screen.

This issue is resolved in this release.

**Restoring VMs on ESXi 8.x and later using disks backed up from ESXi 7.0 Update 3 or earlier fails during disk hot-add**

When restoring a virtual machine on an ESXi 8.x and later host, if you use disks backed up from ESXi 7.0 Update 3 or earlier, the operation might fail during the hot-add of the restored disk. The issue is specific to Non-Persistent Independent disks. The failure occurs due to a descriptor version mismatch between the original disk descriptor from the older host and the newer version expected by ESXi 8.x.

This issue is resolved in this release. ESXi 8.0 Update 3m introduces a mechanism to correctly adjust the version of object-backed disk descriptors to match host capabilities when they are duplicated or moved, preventing the hot-add failure.

**The Enhanced Network Stack (ENS) configuration on ENS-enabled hosts might not turn on after an upgrade to ESXi 8.0 Update 3j**

When you upgrade an ENS-enabled ESXi host to ESXi 8.0 Update 3j, the ENS configuration might not be active on the host uplinks. The uplinks come up in the standard network stack instead of ENS, while the switch remains configured for ENS. As a result, you might experience very high latency and packet loss on the affected host.

This issue is resolved in ESXi 8.0 Update 3m and NSX 4.2.5 . ESXi now synchronizes the ENS activation state with NSX after a host reboot, so that ENS-enabled uplinks come up correctly in ENS mode after an upgrade.

**VM TCP applications might fail and cause unnecessary retransmissions on ENS-enabled NSX overlay networks due to non-zero padding**

When a network device such as an F5 load balancer appends non-zero padding bytes to small packets, TCP applications might experience connection failures that in turn cause unnecessary retransmissions. Non-zero padding might lead to incorrect outer checksum for the encapsulated traffic and some guest operating systems reject the packets, causing the application connectivity interruptions.

This issue is resolved in this release. ESXi now correctly computes the outer checksum for encapsulated traffic by accounting for non-zero Ethernet padding bytes, so that receiving hosts validate the checksum and guest operating systems no longer reject the packets.

**An ESXi host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESXi host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESXi host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen during periods of heavy vSphere vMotion traffic**

A burst of heavy concurrent vSphere vMotion traffic in an ESXi host can cause a large number of TCP connections to compete for the same per-netstack TCP connection information lock. Since this lock is implemented as a spinlock that does not guarantee fair ordering, some processes might time out due to indefinite wait and cause the ESXi host to fail with a purple diagnostic screen.

This issue is resolved in this release. The fix reduces lock contention in the TCP/IP stack under high concurrent connection load.

**ESXi hosts might experience CPU utilization at around 100% after a port is quiesced in an Enhanced Network Stack (ENS) environment**

When a network port is quiesced, the host network scheduler might fail to correctly update its internal byte counters after clearing pending packets. This mismatch causes the system to continually check for network traffic even when the queue is empty, resulting in the transmit (TX) process getting stuck in a loop and consuming up to 100% of CPU resources.

This issue is resolved in this release. The fix ensures that internal byte counters are accurately updated when packets are dropped.

**ESXi host fails with purple diagnostic screen during TCP/IP flow table cleanup**

During periodic TCP/IP stack flow table cleanup, the ESXi host might fail with a purple diagnostic screen. The issue occurs when a race condition between cleanup operations causes the host to attempt to free a route entry that another operation already released, making the host unresponsive.

This issue is resolved in this release. ESXi now includes a preventive check during TCP/IP stack flow table cleanup, so that the host does not fail with a purple diagnostic screen.

**Failure in the underlying storage hardware might cause virtual machines become unresponsive after a backup**

A failure in the underlying storage hardware might cause an issue with the Lightweight Delta (LWD) filter in backup solutions such as Dell PowerProtect Data Manager and lead to virtual machines becoming unresponsive after a backup.

This issue is resolved in this release.

**ESXi hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESXi host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

This issue is resolved in this release. Starting with vCenter 8.0 Update 3m, the lwisOomCheck service automatically starts together with the Likewise service on ESXi hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**You see multiple "Failed to fetch FC target attributes" messages in the vmkernel log file**

During device discovery, if ESXi attempts to fetch FC attributes for an invalid target, you might see multiple Failed to fetch FC target attributes messages in the vmkernel log file.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen after PCI passthrough to a Linux or Windows VM**

When you use PCI passthrough on a PCI or PCIe device to a Linux or Windows VM, including NVIDIA GPUs, the VM might not program the MSI or MSIx interrupts correctly during the device probe. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**vCenter VM connected to a static distributed virtual port group cannot restore network connectivity after registering on a new ESXi host**

When the ESXi host on which resides a vCenter VM connected to a static distributed virtual port group (DVPG) fails, you cannot register the vCenter VM on a new ESXi host, because the VM is not active and network connectivity cannot restore. Previously, recovering connectivity required creating a temporary vSphere Standard Switch (VSS) and reassigning a physical network adapter. With vCenter 8.0 Update 3m, you can load the distributed virtual port configuration directly from the local port file by using the net-dvs command while the vCenter is offline.

This issue is resolved in this release. To restore network connectivity on the target ESXi host, run the following command in the ESXi shell to load the port from its file path: net-dvs --loadDvportFile \<path\_to\_port\_file>.

**IOFilterVP memory leak causes the IOFilter provider to appear offline in the Storage Providers tab**

A memory leak in IOFilterVP causes the service to exhaust memory and become unresponsive to API calls when the IOFilterVP APIs are called frequently, such as from a vulnerability scanning tool. Because the Storage Monitoring Service in vCenter cannot communicate with IOFilterVP, vCenter shows the IOFilter provider for the affected host as offline in the **Storage Providers** tab. The memory exhaustion also produces admission failure logs in the vmkernel.log file with the message Admission failure in path: host/iofilters/iofiltervpd:ioFilterVPServer.

This issue is resolved in this release.

**Uplink gets reenabled before the time defined by the TeamPolicyUpDelay policy passes**

The ESXi advanced setting Net.TeamPolicyUpDelay sets a time before an uplink is reenabled after the link status changes from DOWN to UP. During such a wait period, new ports might be enabled for various reasons, such as migration, VM power cycle, or flapping of the network interface inside the guest OS. A newly powered on vNIC can cause an uplink in TeamPolicyUpDelay state to reactivate prematurely for all VMs connected to the switch.

This issue is resolved in this release.

## esx-update\_8.0.3-0.106.25926933

**Patch Category**

Bugfix

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_loadesx\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-update\_8.0.3-0.106.25926933

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the loadesx and esx-update VIBs.

## esxio-update\_8.0.3-0.106.25926933

**Patch Category**

Bugfix

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_loadesxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-update\_8.0.3-0.106.25926933

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the loadesxio and esxio-update VIBs.

## Broadcom-ELX-lpfc\_14.4.0.50-35vmw.803.0.106.25926933

**Patch Category**

Bugfix

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_lpfc\_14.4.0.50-35vmw.803.0.106.25926933

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the lpfc VIB to resolve the following issues:

**ESXi hosts using the lpfc driver do not provide log visibility for certain faulty small form-factor pluggable (SFP) optics**

When an SFP module is present but non-functional, the Emulex Fibre Channel adapter firmware detects the fault and reports an error code. The lpfc driver does not capture or log that specific hardware error code into the vmkernel.log file, which makes it difficult to identify and troubleshoot faulty optics.

This issue is resolved in this release. The fix enhances the driver to properly log SFP hardware errors as they occur.

**Emulex SAN Manager (ESM) does not display encryption details for certain Host Bus Adapters (HBAs)**

An issue within the lpfc driver prevents ESM from properly retrieving data from all encryption-capable Emulex Fibre Channel adapters. This occurs due to a communication mismatch during fabric port initialization and link setup sequences between the ESXi host and the switch.

This issue is resolved in this release.

## VMware-vmkusb\_0.1-26vmw.803.0.106.25926933

**Patch Category**

Bugfix

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_vmkusb\_0.1-26vmw.803.0.106.25926933
- VMW\_bootbank\_vmkusb-esxio\_0.1-26vmw.803.0.106.25926933

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the vmkusb VIB to resolve the following issue:

**A race condition in the USB Network adapter in management controllers might cause ESXi hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESXi hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

This issue is resolved in this release.

## ESXi\_8.0.3-0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsan\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_trx\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.104.25926924
- VMware\_bootbank\_clusterstore\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc\_8.0.3-0.104.25926924
- VMware\_bootbank\_vds-vsip\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_infravisor\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsanhealth\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-xserver\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal\_8.0.3-0.104.25926924
- VMware\_bootbank\_vdfs\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-base\_8.0.3-0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

The ESXi and esx-update bulletins are dependent on each other. Always include both in a single ESXi host patch baseline or include the rollup bulletin in the baseline to avoid failure during host patching. This patch updates the drivervm-gpu-base, esxio-dvfilter-generic-fastpath, vsan, esxio-combiner, bmcal-esxio, trx, esx-dvfilter-generic-fastpath, crx, cpu-microcode, clusterstore, esxio, native-misc-drivers-esxio, vcls-pod-crx, gc, vds-vsip, gc-esxio, infravisor, vsanhealth, esx-xserver, native-misc-drivers, esxio-combiner-esxio, bmcal, vdfs, esxio-base, esx-ui, and esx-base VIBs.

**ESXi 8.0 Update 3m includes the following Intel microcode:**

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

Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series

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

Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series

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

Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300

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

Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series

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

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series; Intel Xeon D-1700 Series

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

0x2b000685

3/2/2026

Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core)

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

0xa000151

3/24/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000434

4/27/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003b2

3/16/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x32

baseline

0x133

10/8/2025

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x32

baseline

0x133

10/8/2025

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

0x210002f4

3/2/2026

Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series

## esx-update\_8.0.3-0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_loadesx\_8.0.3-104.25926924
- VMware\_bootbank\_esx-update\_8.0.3-104.25746436

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the loadesx and esx-update VIBs.

## esxio-update\_8.0.3-0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_loadesxio\_8.0.3-104.25926924
- VMware\_bootbank\_esxio-update\_8.0.3-104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the loadesxio and esxio-update VIBs.

## Broadcom-ELX-lpfc\_14.4.0.48-35vmw.803.0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_lpfc\_14.4.0.48-35vmw.803.0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the lpfc VIB.

## Mellanox-nmlx5\_4.23.9.1-1vmw.803.0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_nmlx5-core-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-core\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc-esxio\_4.23.9.1-1vmw.803.0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the nmlx5 VIB.

## VMware-HBR-UW\_8.0.3-0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

No

**Virtual Machine Migration or Shutdown Required**

No

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_bootbank\_vmware-hbrsrv\_8.0.3-0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the vmware-hbrsrv VIB.

## VMware-NVMeoF-TCP\_1.0.1.38-1vmw.803.0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_nvmetcp-esxio\_1.0.1.38-1vmw.803.0.104.25926924
- VMW\_bootbank\_nvmetcp\_1.0.1.38-1vmw.803.0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the nvmetcp-esxio and nvmetcp VIBs.

## VMware-VM-Tools\_12.5.5.25704436-25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMware\_locker\_tools-light\_12.5.5.25704436-25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the tools-light VIB.

**VMware Tools Bundling Changes in ESXi 8.0 Update 3m**

The following VMware Tools ISO images are bundled with ESXi 8.0 Update 3m:

- : VMware Tools 12.5.5 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.windows.iso- VMware Tools 12.4.9 supports 32-bit Windows versions.windows-x86.iso:- : VMware Tools 10.3.26 ISO image for Linux OS with linux.iso 2.11 or later.glibc

The following VMware Tools ISO images are available for download:

- VMware Tools 11.0.6:
  - : for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).windows.iso

- VMware Tools 10.0.12:
  - : for Windows 2000, Windows XP, and Windows 2003.winPreVista.iso  - : supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with linuxPreGLibc25.iso version earlier than 2.5.glibc
- : VMware Tools image 10.3.10 for Solaris.solaris.iso- : Supports Mac OS X versions 10.11 and later.darwin.iso

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESXi:

## VMware-nvmxnet3-ens\_2.0.0.23-7vmw.803.0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_nvmxnet3-ens\_2.0.0.23-7vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-ens-esxio\_2.0.0.23-7vmw.803.0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the loadesx and esx-update VIBs.

## VMware-nvmxnet3\_2.0.0.31-13vmw.803.0.104.25926924

**Patch Category**

Security

**Patch Severity**

Critical

**Host Reboot Required**

Yes

**Virtual Machine Migration or Shutdown Required**

Yes

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs Included**

- VMW\_bootbank\_nvmxnet3\_2.0.0.31-13vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-esxio\_2.0.0.31-13vmw.803.0.104.25926924

**PRs Fixed**

N/A

**CVE numbers**

N/A

Updates the nvmxnet and nvmxnet3-esxio VIBs.

## ESXi-8.0U3m-25926933-standard

**Profile Name**

ESXi-8.0U3m-25926933-standard

**Build**

For build information, see the Build Details section.

**Vendor**

Broadcom, Inc.

**Release Date**

November 19, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

- VMware\_bootbank\_esxio-combiner\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsan\_8.0.3-0.106.25926933
- VMware\_bootbank\_infravisor\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsanhealth\_8.0.3-0.106.25926933
- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc\_8.0.3-0.106.25926933
- VMware\_bootbank\_vdfs\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-xserver\_8.0.3-0.106.25926933
- VMware\_bootbank\_vds-vsip\_8.0.3-0.106.25926933
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_clusterstore\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_trx\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.106.25926933
- VMware\_bootbank\_loadesx\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-update\_8.0.3-0.106.25926933
- VMware\_bootbank\_loadesxio\_8.0.3-0.106.25926933

- VMware\_bootbank\_esxio-update\_8.0.3-0.106.25926933
- VMW\_bootbank\_lpfc\_14.4.0.50-35vmw.803.0.106.25926933
- VMW\_bootbank\_vmkusb\_0.1-26vmw.803.0.106.25926933
- VMW\_bootbank\_vmkusb-esxio\_0.1-26vmw.803.0.106.25926933
- VMware\_locker\_tools-light\_12.5.5.25704436-25926924

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

**This patch updates the following issues:**

**Virtual machines on an AMD processor might fail after NUMA migration of the hypervisor internal data due to a race condition**

If a vCPU moves to another processor during a hypervisor NUMA migration, a race condition might cause an update of the old copy of some hypervisor data instead of the new one. The VM continues to work with out-of-date information and ultimately fails.

This issue is resolved in this release.

**vSphere Replication-protected virtual machines become unresponsive or display as invalid due to a race condition during placing an ESXi host into maintenance mode or a cluster update**

During ESXi host maintenance or remediation, virtual machines protected by vSphere Replication are automatically paused or reconfigured. A rare race condition in the vSphere Replication filter driver might lead to an internal deadlock that prevents virtual machine disk operations from completing. As a result, reconfiguration tasks and vSphere vMotion migration tasks might time out, which leaves affected virtual machines in an invalid state. vSphere Replication-protected virtual machines become unresponsive and cannot go out of maintenance mode.

This issue is resolved in this release. After upgrading to ESXi 8.0 Update 3m, reboot affected ESXi hosts to restore normal operations.

**After remediation with reboot, vCenter services might not be available on ESXi hosts that use internal service accounts**

Remediating the vSphere Configuration Profiles configuration might delete the svc-vcf- service accounts, which are internally managed user accounts, on ESXi hosts that reboot after the remediation. As a result, some vCenter services might not be available on such ESXi hosts. For example, the creation of a vSAN stretched cluster fails at an internal step: Disable SSH on hosts.

This issue is resolved in this release.

**Image compliance on a DPU host shows as Unknown due to a timeout**

Due to the processing of content from online depots, the DPU scan API call might spend more than the limit of 2 min before a timeout. As a result, you see the check compliance status of DPUs on the ESXi host as Unknown.

In the ESXi logs, /var/run/log/lifecycle.log, you see an error such as:

2025-09-19T15:14:41Z Er(11) lifecycle\[2124459\]: TaskBase:210 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) timedout

2025-09-19T15:14:41Z In(14) lifecycle\[2124459\]: TaskBase:261 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) finished with state TIMEDOUT ...

The issue has no specific trigger and you might see it during a routine compliance scan, but the occurrence is random, not with every compliance check, and is not related to any specific DPU type.

This issue is resolved in this release.

**Virtual machines cannot power on due to a "Module 'DevicePowerOn' power on failed" error**

Due to a string conversion issue, VMs using passthrough devices might fail to power-on even when suitable passthrough devices are available.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen while connecting a USB 3.1 HDD using PCI passthrough to a virtual machine**

An ESXi host might fail with a purple diagnostic screen while connecting a device that utilizes Reserved Memory Region Reporting (RMRR) using PCI passthrough to a VM with vIOMMU option selected (vvtd.enable = TRUE in the .vmx file), since this configuration is not supported.

This issue is resolved in this release. The fix ensures that the VM fails to power on with an error message instead of purple diagnostic screen failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on**

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

This issue is resolved in this release.

**Add Host task in the vSphere Client might fail due to an internal timeout**

Due to a timeout in the internal HTTP client during an Add Host operation in the vSphere Client, you might see such tasks take long and eventually fail.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**Migration of a VM with an NVIDIA vGPU passthrough device fails when migrating from ESXi 7.x to ESXi 8.x**

vSphere vMotion migration of a virtual machine with an NVIDIA vGPU passthrough device from an ESXi 7.x host to 8.x host might fail with an IOMMU adjustment panic error in the vmware.log file. In the vSphere Client, you see the error: The remote host closed the connection unexpectedly and migration has stopped. The closed connection probably results from a migration failure detected on the remote host.

This issue is resolved in this release. Upgrade the destination ESXi hosts to version 8.0 Update 3m or later.

**Scheduling delays when high-priority processes are placed on a busy physical CPU might cause packets drop**

When high-priority processes, for example in an Enhanced Network Stack (ENS) context, are placed on a busy physical CPU, they rely on the virtual CPU migration algorithm to move them to an idle or less busy CPU as appropriate. An issue with the migration algorithm might cause such processes to stay on the busy CPU for extended periods, causing significant scheduling delays, or high CPU Ready Time. As a result, you might see packets drop.

This issue is resolved in this release.

**Active Directory user or group permissions might be unexpectedly removed from an ESXi host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESXi host might incorrectly remove permissions to an AD user or group.

This issue is resolved in this release. The fix makes sure that ESXi hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted, and preserves permissions in the case of a temporary connectivity failure.

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

This issue is resolved in this release.

**On ESXi hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESXi hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

This issue is resolved in this release. The fix increases the default xmapGB value from 32GB to 64GB.

**ESXi hosts run out of file descriptors during high-volume VM operations, ultimately causing VM power-on failures**

On an ESXi host handling a high volume of concurrent VM power-on and vSphere vMotion operations, the Object Store File System Daemon (osfsd) might exhaust its file handle pool, reporting No free handles and VMK\_TOO\_MANY\_FILES errors. As a result, further VM power-on attempts on such hosts fail with a vim.fault.GenericVmConfigFault error in vCenter logs.

This issue is resolved in this release.

**An ESXi host fails with a purple diagnostic screen during SEsparse disk consolidation**

In extremely rare cases, during a write operation on a thin VMDK, due to an issue with the memory allocation for internal data structures, a buffer-overrun can cause failure of the slab memory allocation system. As a result, the ESXi host might fail with a purple diagnostic screen. The backtrace contains errors such as FastSlabCreateObj, FastSlabReplenishCPU, FastSlabAllocSlow, and the vmkernel.log messages show WARNING: Heartbeat: PCPU ## didn't have a heartbeat followed by ALERT: NMI: NMI IPI. The issue is specific to high I/O operations during SEsparse disk consolidation.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen during I/O to a storage device**

A race condition in the I/O scheduler might free a per-device I/O queue while a new I/O request is in the process of marking that same queue active again. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESXi host might fail with a purple diagnostic screen.

This issue is resolved in this release.

**Restoring VMs on ESXi 8.x and later using disks backed up from ESXi 7.0 Update 3 or earlier fails during disk hot-add**

When restoring a virtual machine on an ESXi 8.x and later host, if you use disks backed up from ESXi 7.0 Update 3 or earlier, the operation might fail during the hot-add of the restored disk. The issue is specific to Non-Persistent Independent disks. The failure occurs due to a descriptor version mismatch between the original disk descriptor from the older host and the newer version expected by ESXi 8.x.

This issue is resolved in this release. ESXi 8.0 Update 3m introduces a mechanism to correctly adjust the version of object-backed disk descriptors to match host capabilities when they are duplicated or moved, preventing the hot-add failure.

**The Enhanced Network Stack (ENS) configuration on ENS-enabled hosts might not turn on after an upgrade to ESXi 8.0 Update 3j**

When you upgrade an ENS-enabled ESXi host to ESXi 8.0 Update 3j, the ENS configuration might not be active on the host uplinks. The uplinks come up in the standard network stack instead of ENS, while the switch remains configured for ENS. As a result, you might experience very high latency and packet loss on the affected host.

This issue is resolved in ESXi 8.0 Update 3m and NSX 4.2.5 . ESXi now synchronizes the ENS activation state with NSX after a host reboot, so that ENS-enabled uplinks come up correctly in ENS mode after an upgrade.

**VM TCP applications might fail and cause unnecessary retransmissions on ENS-enabled NSX overlay networks due to non-zero padding**

When a network device such as an F5 load balancer appends non-zero padding bytes to small packets, TCP applications might experience connection failures that in turn cause unnecessary retransmissions. Non-zero padding might lead to incorrect outer checksum for the encapsulated traffic and some guest operating systems reject the packets, causing the application connectivity interruptions.

This issue is resolved in this release. ESXi now correctly computes the outer checksum for encapsulated traffic by accounting for non-zero Ethernet padding bytes, so that receiving hosts validate the checksum and guest operating systems no longer reject the packets.

**An ESXi host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESXi host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESXi host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen during periods of heavy vSphere vMotion traffic**

A burst of heavy concurrent vSphere vMotion traffic in an ESXi host can cause a large number of TCP connections to compete for the same per-netstack TCP connection information lock. Since this lock is implemented as a spinlock that does not guarantee fair ordering, some processes might time out due to indefinite wait and cause the ESXi host to fail with a purple diagnostic screen.

This issue is resolved in this release. The fix reduces lock contention in the TCP/IP stack under high concurrent connection load.

**ESXi hosts might experience CPU utilization at around 100% after a port is quiesced in an Enhanced Network Stack (ENS) environment**

When a network port is quiesced, the host network scheduler might fail to correctly update its internal byte counters after clearing pending packets. This mismatch causes the system to continually check for network traffic even when the queue is empty, resulting in the transmit (TX) process getting stuck in a loop and consuming up to 100% of CPU resources.

This issue is resolved in this release. The fix ensures that internal byte counters are accurately updated when packets are dropped.

**ESXi host fails with purple diagnostic screen during TCP/IP flow table cleanup**

During periodic TCP/IP stack flow table cleanup, the ESXi host might fail with a purple diagnostic screen. The issue occurs when a race condition between cleanup operations causes the host to attempt to free a route entry that another operation already released, making the host unresponsive.

This issue is resolved in this release. ESXi now includes a preventive check during TCP/IP stack flow table cleanup, so that the host does not fail with a purple diagnostic screen.

**Failure in the underlying storage hardware might cause virtual machines become unresponsive after a backup**

A failure in the underlying storage hardware might cause an issue with the Lightweight Delta (LWD) filter in backup solutions such as Dell PowerProtect Data Manager and lead to virtual machines becoming unresponsive after a backup.

This issue is resolved in this release.

**A race condition in the USB Network adapter in management controllers might cause ESXi hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESXi hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

This issue is resolved in this release.

**ESXi hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESXi host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

This issue is resolved in this release. Starting with vCenter 8.0 Update 3m, the lwisOomCheck service automatically starts together with the Likewise service on ESXi hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**You see multiple "Failed to fetch FC target attributes" messages in the vmkernel log file**

During device discovery, if ESXi attempts to fetch FC attributes for an invalid target, you might see multiple Failed to fetch FC target attributes messages in the vmkernel log file.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen after PCI passthrough to a Linux or Windows VM**

When you use PCI passthrough on a PCI or PCIe device to a Linux or Windows VM, including NVIDIA GPUs, the VM might not program the MSI or MSIx interrupts correctly during the device probe. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**ESXi hosts using the lpfc driver do not provide log visibility for certain faulty small form-factor pluggable (SFP) optics**

When an SFP module is present but non-functional, the Emulex Fibre Channel adapter firmware detects the fault and reports an error code. The lpfc driver does not capture or log that specific hardware error code into the vmkernel.log file, which makes it difficult to identify and troubleshoot faulty optics.

This issue is resolved in this release. The fix enhances the driver to properly log SFP hardware errors as they occur.

**vCenter VM connected to a static distributed virtual port group cannot restore network connectivity after registering on a new ESXi host**

When the ESXi host on which resides a vCenter VM connected to a static distributed virtual port group (DVPG) fails, you cannot register the vCenter VM on a new ESXi host, because the VM is not active and network connectivity cannot restore. Previously, recovering connectivity required creating a temporary vSphere Standard Switch (VSS) and reassigning a physical network adapter. With vCenter 8.0 Update 3m, you can load the distributed virtual port configuration directly from the local port file by using the net-dvs command while the vCenter is offline.

This issue is resolved in this release. To restore network connectivity on the target ESXi host, run the following command in the ESXi shell to load the port from its file path: net-dvs --loadDvportFile \<path\_to\_port\_file>.

**IOFilterVP memory leak causes the IOFilter provider to appear offline in the Storage Providers tab**

A memory leak in IOFilterVP causes the service to exhaust memory and become unresponsive to API calls when the IOFilterVP APIs are called frequently, such as from a vulnerability scanning tool. Because the Storage Monitoring Service in vCenter cannot communicate with IOFilterVP, vCenter shows the IOFilter provider for the affected host as offline in the **Storage Providers** tab. The memory exhaustion also produces admission failure logs in the vmkernel.log file with the message Admission failure in path: host/iofilters/iofiltervpd:ioFilterVPServer.

This issue is resolved in this release.

**Uplink gets reenabled before the time defined by the TeamPolicyUpDelay policy passes**

The ESXi advanced setting Net.TeamPolicyUpDelay sets a time before an uplink is reenabled after the link status changes from DOWN to UP. During such a wait period, new ports might be enabled for various reasons, such as migration, VM power cycle, or flapping of the network interface inside the guest OS. A newly powered on vNIC can cause an uplink in TeamPolicyUpDelay state to reactivate prematurely for all VMs connected to the switch.

This issue is resolved in this release.

**Emulex SAN Manager (ESM) does not display encryption details for certain Host Bus Adapters (HBAs)**

An issue within the lpfc driver prevents ESM from properly retrieving data from all encryption-capable Emulex Fibre Channel adapters. This occurs due to a communication mismatch during fabric port initialization and link setup sequences between the ESXi host and the switch.

This issue is resolved in this release.

## ESXi-8.0U3m-25926933-no-tools

**Profile Name**

ESXi-8.0U3m-25926933-no-tools

**Build**

For build information, see the Build Details section.

**Vendor**

Broadcom, Inc.

**Release Date**

November 19, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

- VMware\_bootbank\_esxio-combiner\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsan\_8.0.3-0.106.25926933
- VMware\_bootbank\_infravisor\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal\_8.0.3-0.106.25926933
- VMware\_bootbank\_vsanhealth\_8.0.3-0.106.25926933
- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc\_8.0.3-0.106.25926933
- VMware\_bootbank\_vdfs\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-xserver\_8.0.3-0.106.25926933
- VMware\_bootbank\_vds-vsip\_8.0.3-0.106.25926933
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_clusterstore\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-base\_8.0.3-0.106.25926933
- VMware\_bootbank\_trx\_8.0.3-0.106.25926933
- VMware\_bootbank\_gc-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.106.25926933
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.106.25926933
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.106.25926933
- VMware\_bootbank\_loadesx\_8.0.3-0.106.25926933
- VMware\_bootbank\_esx-update\_8.0.3-0.106.25926933
- VMware\_bootbank\_loadesxio\_8.0.3-0.106.25926933

- VMware\_bootbank\_esxio-update\_8.0.3-0.106.25926933
- VMW\_bootbank\_lpfc\_14.4.0.50-35vmw.803.0.106.25926933
- VMW\_bootbank\_vmkusb\_0.1-26vmw.803.0.106.25926933
- VMW\_bootbank\_vmkusb-esxio\_0.1-26vmw.803.0.106.25926933

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

**This patch updates the following issues:**

**Virtual machines on an AMD processor might fail after NUMA migration of the hypervisor internal data due to a race condition**

If a vCPU moves to another processor during a hypervisor NUMA migration, a race condition might cause an update of the old copy of some hypervisor data instead of the new one. The VM continues to work with out-of-date information and ultimately fails.

This issue is resolved in this release.

**vSphere Replication-protected virtual machines become unresponsive or display as invalid due to a race condition during placing an ESXi host into maintenance mode or a cluster update**

During ESXi host maintenance or remediation, virtual machines protected by vSphere Replication are automatically paused or reconfigured. A rare race condition in the vSphere Replication filter driver might lead to an internal deadlock that prevents virtual machine disk operations from completing. As a result, reconfiguration tasks and vSphere vMotion migration tasks might time out, which leaves affected virtual machines in an invalid state. vSphere Replication-protected virtual machines become unresponsive and cannot go out of maintenance mode.

This issue is resolved in this release. After upgrading to ESXi 8.0 Update 3m, reboot affected ESXi hosts to restore normal operations.

**After remediation with reboot, vCenter services might not be available on ESXi hosts that use internal service accounts**

Remediating the vSphere Configuration Profiles configuration might delete the svc-vcf- service accounts, which are internally managed user accounts, on ESXi hosts that reboot after the remediation. As a result, some vCenter services might not be available on such ESXi hosts. For example, the creation of a vSAN stretched cluster fails at an internal step: Disable SSH on hosts.

This issue is resolved in this release.

**Image compliance on a DPU host shows as Unknown due to a timeout**

Due to the processing of content from online depots, the DPU scan API call might spend more than the limit of 2 min before a timeout. As a result, you see the check compliance status of DPUs on the ESXi host as Unknown.

In the ESXi logs, /var/run/log/lifecycle.log, you see an error such as:

2025-09-19T15:14:41Z Er(11) lifecycle\[2124459\]: TaskBase:210 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) timedout

2025-09-19T15:14:41Z In(14) lifecycle\[2124459\]: TaskBase:261 Runnable (scan\_task e9d8c101-c742-5ebe-8d83-d269734f26d8) finished with state TIMEDOUT ...

The issue has no specific trigger and you might see it during a routine compliance scan, but the occurrence is random, not with every compliance check, and is not related to any specific DPU type.

This issue is resolved in this release.

**Virtual machines cannot power on due to a "Module 'DevicePowerOn' power on failed" error**

Due to a string conversion issue, VMs using passthrough devices might fail to power-on even when suitable passthrough devices are available.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen while connecting a USB 3.1 HDD using PCI passthrough to a virtual machine**

An ESXi host might fail with a purple diagnostic screen while connecting a device that utilizes Reserved Memory Region Reporting (RMRR) using PCI passthrough to a VM with vIOMMU option selected (vvtd.enable = TRUE in the .vmx file), since this configuration is not supported.

This issue is resolved in this release. The fix ensures that the VM fails to power on with an error message instead of purple diagnostic screen failure.

**Virtual machines with multiple assigned PCI passthrough devices behind a PCI bridge might fail to power on**

When multiple PCI passthrough devices behind a conventional PCI bridge or PCIe-to-PCI/PCI-X bridge are assigned to a VM, the VM might fail to power on with a warning message in the vmkernel.log such as:

WARNING: PCIPassthru: 5304: Expected no IOMMU domain for \<sbdf>, got Success

This issue is resolved in this release.

**Add Host task in the vSphere Client might fail due to an internal timeout**

Due to a timeout in the internal HTTP client during an Add Host operation in the vSphere Client, you might see such tasks take long and eventually fail.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen in rare cases due to a race condition in disks with attached I/O filter**

In rare cases, a VM that has disks with attached I/O filters might fail at the same time as another operation, such as vSphere vMotion migration or a snapshot, closes the disk. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**Migration of a VM with an NVIDIA vGPU passthrough device fails when migrating from ESXi 7.x to ESXi 8.x**

vSphere vMotion migration of a virtual machine with an NVIDIA vGPU passthrough device from an ESXi 7.x host to 8.x host might fail with an IOMMU adjustment panic error in the vmware.log file. In the vSphere Client, you see the error: The remote host closed the connection unexpectedly and migration has stopped. The closed connection probably results from a migration failure detected on the remote host.

This issue is resolved in this release. Upgrade the destination ESXi hosts to version 8.0 Update 3m or later.

**Scheduling delays when high-priority processes are placed on a busy physical CPU might cause packets drop**

When high-priority processes, for example in an Enhanced Network Stack (ENS) context, are placed on a busy physical CPU, they rely on the virtual CPU migration algorithm to move them to an idle or less busy CPU as appropriate. An issue with the migration algorithm might cause such processes to stay on the busy CPU for extended periods, causing significant scheduling delays, or high CPU Ready Time. As a result, you might see packets drop.

This issue is resolved in this release.

**Active Directory user or group permissions might be unexpectedly removed from an ESXi host**

As result of a temporary Active Directory or network connectivity issue, the periodic permission validation task on an ESXi host might incorrectly remove permissions to an AD user or group.

This issue is resolved in this release. The fix makes sure that ESXi hosts correctly distinguishes a temporary Active Directory connectivity failure from an account that has actually been deleted, and preserves permissions in the case of a temporary connectivity failure.

**BFD OAM sessions might fail after a vSphere vMotion migration of a virtual machine**

When a virtual machine using Geneve or VXLAN networking is migrated to another host by using vSphere vMotion, the underlying network health check filters, NSX VTEP OAM, might remain in a disabled state on the source host. As a result, the host cannot correctly process OAM traffic, which causes BFD health checks to fail. The issue occurs because the system fails to automatically re-enable the host-level network filters once the VM-specific filters of the migrated VM are removed.

This issue is resolved in this release.

**On ESXi hosts with DPDK-based VMs, some vNICs might fail during enablement**

On ESXi hosts that have VMs using a specialized poll mode driver (PMD) for the VMware VMXNET3 network adapter (DPDK), such as Edge VMs, some vNICs might fail during enablement due to lack of XMap memory.

This issue is resolved in this release. The fix increases the default xmapGB value from 32GB to 64GB.

**ESXi hosts run out of file descriptors during high-volume VM operations, ultimately causing VM power-on failures**

On an ESXi host handling a high volume of concurrent VM power-on and vSphere vMotion operations, the Object Store File System Daemon (osfsd) might exhaust its file handle pool, reporting No free handles and VMK\_TOO\_MANY\_FILES errors. As a result, further VM power-on attempts on such hosts fail with a vim.fault.GenericVmConfigFault error in vCenter logs.

This issue is resolved in this release.

**An ESXi host fails with a purple diagnostic screen during SEsparse disk consolidation**

In extremely rare cases, during a write operation on a thin VMDK, due to an issue with the memory allocation for internal data structures, a buffer-overrun can cause failure of the slab memory allocation system. As a result, the ESXi host might fail with a purple diagnostic screen. The backtrace contains errors such as FastSlabCreateObj, FastSlabReplenishCPU, FastSlabAllocSlow, and the vmkernel.log messages show WARNING: Heartbeat: PCPU ## didn't have a heartbeat followed by ALERT: NMI: NMI IPI. The issue is specific to high I/O operations during SEsparse disk consolidation.

This issue is resolved in this release.

**ESXi host might fail with a purple diagnostic screen during I/O to a storage device**

A race condition in the I/O scheduler might free a per-device I/O queue while a new I/O request is in the process of marking that same queue active again. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen when N-Port ID Virtualization (NPIV) is not correctly configured**

The proper configuration of NPIV requires FC switch zoning and initiator-groups (LUN masking) on the storage target. If virtual World Wide Port Names (WWPNs) are not correctly zoned on the switch or mapped on the storage target, the storage driver on the ESXi host might fail with a purple diagnostic screen.

This issue is resolved in this release.

**Restoring VMs on ESXi 8.x and later using disks backed up from ESXi 7.0 Update 3 or earlier fails during disk hot-add**

When restoring a virtual machine on an ESXi 8.x and later host, if you use disks backed up from ESXi 7.0 Update 3 or earlier, the operation might fail during the hot-add of the restored disk. The issue is specific to Non-Persistent Independent disks. The failure occurs due to a descriptor version mismatch between the original disk descriptor from the older host and the newer version expected by ESXi 8.x.

This issue is resolved in this release. ESXi 8.0 Update 3m introduces a mechanism to correctly adjust the version of object-backed disk descriptors to match host capabilities when they are duplicated or moved, preventing the hot-add failure.

**The Enhanced Network Stack (ENS) configuration on ENS-enabled hosts might not turn on after an upgrade to ESXi 8.0 Update 3j**

When you upgrade an ENS-enabled ESXi host to ESXi 8.0 Update 3j, the ENS configuration might not be active on the host uplinks. The uplinks come up in the standard network stack instead of ENS, while the switch remains configured for ENS. As a result, you might experience very high latency and packet loss on the affected host.

This issue is resolved in ESXi 8.0 Update 3m and NSX 4.2.5 . ESXi now synchronizes the ENS activation state with NSX after a host reboot, so that ENS-enabled uplinks come up correctly in ENS mode after an upgrade.

**VM TCP applications might fail and cause unnecessary retransmissions on ENS-enabled NSX overlay networks due to non-zero padding**

When a network device such as an F5 load balancer appends non-zero padding bytes to small packets, TCP applications might experience connection failures that in turn cause unnecessary retransmissions. Non-zero padding might lead to incorrect outer checksum for the encapsulated traffic and some guest operating systems reject the packets, causing the application connectivity interruptions.

This issue is resolved in this release. ESXi now correctly computes the outer checksum for encapsulated traffic by accounting for non-zero Ethernet padding bytes, so that receiving hosts validate the checksum and guest operating systems no longer reject the packets.

**An ESXi host might fail with a purple diagnostic screen with a #PF Exception 14 during the processing of a TCP timer**

A race condition in the TCP/IP stack connection cleanup path in an ESXi host can free a TCP control block while one of its timers, such as the keepalive or 2MSL timer, is still executing on it. This use-after-free condition can cause the ESXi host to fail with a purple diagnostic screen, and in some cases might result in memory corruption in other processes.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen during periods of heavy vSphere vMotion traffic**

A burst of heavy concurrent vSphere vMotion traffic in an ESXi host can cause a large number of TCP connections to compete for the same per-netstack TCP connection information lock. Since this lock is implemented as a spinlock that does not guarantee fair ordering, some processes might time out due to indefinite wait and cause the ESXi host to fail with a purple diagnostic screen.

This issue is resolved in this release. The fix reduces lock contention in the TCP/IP stack under high concurrent connection load.

**ESXi hosts might experience CPU utilization at around 100% after a port is quiesced in an Enhanced Network Stack (ENS) environment**

When a network port is quiesced, the host network scheduler might fail to correctly update its internal byte counters after clearing pending packets. This mismatch causes the system to continually check for network traffic even when the queue is empty, resulting in the transmit (TX) process getting stuck in a loop and consuming up to 100% of CPU resources.

This issue is resolved in this release. The fix ensures that internal byte counters are accurately updated when packets are dropped.

**ESXi host fails with purple diagnostic screen during TCP/IP flow table cleanup**

During periodic TCP/IP stack flow table cleanup, the ESXi host might fail with a purple diagnostic screen. The issue occurs when a race condition between cleanup operations causes the host to attempt to free a route entry that another operation already released, making the host unresponsive.

This issue is resolved in this release. ESXi now includes a preventive check during TCP/IP stack flow table cleanup, so that the host does not fail with a purple diagnostic screen.

**Failure in the underlying storage hardware might cause virtual machines become unresponsive after a backup**

A failure in the underlying storage hardware might cause an issue with the Lightweight Delta (LWD) filter in backup solutions such as Dell PowerProtect Data Manager and lead to virtual machines becoming unresponsive after a backup.

This issue is resolved in this release.

**A race condition in the USB Network adapter in management controllers might cause ESXi hosts to fail with a purple diagnostic screen**

An issue with link flapping in the USB Network adapter interface in management controllers such as BMC, iLO, and iDRAC might cause a race condition and lead to failure of ESXi hosts with a purple diagnostic screen and an error such as #PF Exception 14 in world 2100764:vmk1-tx-0.

This issue is resolved in this release.

**ESXi hosts might intermittently disjoin from Active Directory due to a memory leak**

Exhaustion of memory allocated to the Likewise service, caused by a memory leak in Active Directory operations, might cause an ESXi host to disjoin from the Active Directory domain and display as Not Responding in the vSphere Client.

This issue is resolved in this release. Starting with vCenter 8.0 Update 3m, the lwisOomCheck service automatically starts together with the Likewise service on ESXi hosts joined to an Active Directory domain. The memory-exhaustion condition described in Broadcom knowledge base article [318664](https://knowledge.broadcom.com/external/article/318664) is detected and remediated automatically. Manually enabling lwisOomCheck, as described in that KB, is no longer required.

**You see multiple "Failed to fetch FC target attributes" messages in the vmkernel log file**

During device discovery, if ESXi attempts to fetch FC attributes for an invalid target, you might see multiple Failed to fetch FC target attributes messages in the vmkernel log file.

This issue is resolved in this release.

**An ESXi host might fail with a purple diagnostic screen after PCI passthrough to a Linux or Windows VM**

When you use PCI passthrough on a PCI or PCIe device to a Linux or Windows VM, including NVIDIA GPUs, the VM might not program the MSI or MSIx interrupts correctly during the device probe. As a result, the ESXi host fails with a purple diagnostic screen.

This issue is resolved in this release.

**ESXi hosts using the lpfc driver do not provide log visibility for certain faulty small form-factor pluggable (SFP) optics**

When an SFP module is present but non-functional, the Emulex Fibre Channel adapter firmware detects the fault and reports an error code. The lpfc driver does not capture or log that specific hardware error code into the vmkernel.log file, which makes it difficult to identify and troubleshoot faulty optics.

This issue is resolved in this release. The fix enhances the driver to properly log SFP hardware errors as they occur.

**vCenter VM connected to a static distributed virtual port group cannot restore network connectivity after registering on a new ESXi host**

When the ESXi host on which resides a vCenter VM connected to a static distributed virtual port group (DVPG) fails, you cannot register the vCenter VM on a new ESXi host, because the VM is not active and network connectivity cannot restore. Previously, recovering connectivity required creating a temporary vSphere Standard Switch (VSS) and reassigning a physical network adapter. With vCenter 8.0 Update 3m, you can load the distributed virtual port configuration directly from the local port file by using the net-dvs command while the vCenter is offline.

This issue is resolved in this release. To restore network connectivity on the target ESXi host, run the following command in the ESXi shell to load the port from its file path: net-dvs --loadDvportFile \<path\_to\_port\_file>.

**IOFilterVP memory leak causes the IOFilter provider to appear offline in the Storage Providers tab**

A memory leak in IOFilterVP causes the service to exhaust memory and become unresponsive to API calls when the IOFilterVP APIs are called frequently, such as from a vulnerability scanning tool. Because the Storage Monitoring Service in vCenter cannot communicate with IOFilterVP, vCenter shows the IOFilter provider for the affected host as offline in the **Storage Providers** tab. The memory exhaustion also produces admission failure logs in the vmkernel.log file with the message Admission failure in path: host/iofilters/iofiltervpd:ioFilterVPServer.

This issue is resolved in this release.

**Uplink gets reenabled before the time defined by the TeamPolicyUpDelay policy passes**

The ESXi advanced setting Net.TeamPolicyUpDelay sets a time before an uplink is reenabled after the link status changes from DOWN to UP. During such a wait period, new ports might be enabled for various reasons, such as migration, VM power cycle, or flapping of the network interface inside the guest OS. A newly powered on vNIC can cause an uplink in TeamPolicyUpDelay state to reactivate prematurely for all VMs connected to the switch.

This issue is resolved in this release.

**Emulex SAN Manager (ESM) does not display encryption details for certain Host Bus Adapters (HBAs)**

An issue within the lpfc driver prevents ESM from properly retrieving data from all encryption-capable Emulex Fibre Channel adapters. This occurs due to a communication mismatch during fabric port initialization and link setup sequences between the ESXi host and the switch.

This issue is resolved in this release.

## ESXi-8.0U3sm-25926924-standard

**Profile Name**

ESXi-8.0U3sm-25926924-standard

**Build**

For build information, see the Build Details section.

**Vendor**

Broadcom, Inc.

**Release Date**

November 19, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsan\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_trx\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.104.25926924
- VMware\_bootbank\_clusterstore\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc\_8.0.3-0.104.25926924
- VMware\_bootbank\_vds-vsip\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_infravisor\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsanhealth\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-xserver\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal\_8.0.3-0.104.25926924
- VMware\_bootbank\_vdfs\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-base\_8.0.3-0.104.25926924

- VMware\_bootbank\_loadesx\_8.0.3-104.25926924
- VMware\_bootbank\_esx-update\_8.0.3-104.25746436
- VMware\_bootbank\_loadesxio\_8.0.3-104.25926924
- VMware\_bootbank\_esxio-update\_8.0.3-104.25926924
- VMW\_bootbank\_lpfc\_14.4.0.48-35vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-core-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-core\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMware\_bootbank\_vmware-hbrsrv\_8.0.3-0.104.25926924
- VMW\_bootbank\_nvmetcp-esxio\_1.0.1.38-1vmw.803.0.104.25926924
- VMW\_bootbank\_nvmetcp\_1.0.1.38-1vmw.803.0.104.25926924
- VMware\_locker\_tools-light\_12.5.5.25704436-25926924
- VMW\_bootbank\_nvmxnet3-ens\_2.0.0.23-7vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-ens-esxio\_2.0.0.23-7vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3\_2.0.0.31-13vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-esxio\_2.0.0.31-13vmw.803.0.104.25926924

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

**This patch resolves the following issues:**

**ESXi 8.0 Update 3m includes the following Intel microcode:**

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

Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series

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

Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series

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

Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300

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

Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series

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

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series; Intel Xeon D-1700 Series

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

0x2b000685

3/2/2026

Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core)

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

0xa000151

3/24/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000434

4/27/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003b2

3/16/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x32

baseline

0x133

10/8/2025

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x32

baseline

0x133

10/8/2025

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

0x210002f4

3/2/2026

Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series

**VMware Tools Bundling Changes in ESXi 8.0 Update 3m**

The following VMware Tools ISO images are bundled with ESXi 8.0 Update 3m:

- : VMware Tools 12.5.5 supports 64-bit Windows versions - Windows 7 SP1 or Windows Server 2008 R2 SP1 and later.windows.iso- VMware Tools 12.4.9 supports 32-bit Windows versions.windows-x86.iso:- : VMware Tools 10.3.26 ISO image for Linux OS with linux.iso 2.11 or later.glibc

The following VMware Tools ISO images are available for download:

- VMware Tools 11.0.6:
  - : for Windows Vista (SP2) and Windows Server 2008 Service Pack 2 (SP2).windows.iso

- VMware Tools 10.0.12:
  - : for Windows 2000, Windows XP, and Windows 2003.winPreVista.iso  - : supports Linux guest operating systems earlier than Red Hat Enterprise Linux (RHEL) 5, SUSE Linux Enterprise Server (SLES) 11, Ubuntu 7.04, and other distributions with linuxPreGLibc25.iso version earlier than 2.5.glibc
- : VMware Tools image 10.3.10 for Solaris.solaris.iso- : Supports Mac OS X versions 10.11 and later.darwin.iso

Follow the procedures listed in the following documents to download VMware Tools for platforms not bundled with ESXi:

## ESXi-8.0U3sm-25926924-no-tools

**Profile Name**

ESXi-8.0U3sm-25926924-no-tools

**Build**

For build information, see the Build Details section.

**Vendor**

Broadcom, Inc.

**Release Date**

November 19, 2026

**Acceptance Level**

Partner Supported

**Affected Hardware**

N/A

**Affected Software**

N/A

**Affected VIBs**

- VMware\_bootbank\_drivervm-gpu-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsan\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_trx\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-dvfilter-generic-fastpath\_8.0.3-0.104.25926924
- VMware\_bootbank\_crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_cpu-microcode\_8.0.3-0.104.25926924
- VMware\_bootbank\_clusterstore\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_vcls-pod-crx\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc\_8.0.3-0.104.25926924
- VMware\_bootbank\_vds-vsip\_8.0.3-0.104.25926924
- VMware\_bootbank\_gc-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_infravisor\_8.0.3-0.104.25926924
- VMware\_bootbank\_vsanhealth\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-xserver\_8.0.3-0.104.25926924
- VMware\_bootbank\_native-misc-drivers\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-combiner-esxio\_8.0.3-0.104.25926924
- VMware\_bootbank\_bmcal\_8.0.3-0.104.25926924
- VMware\_bootbank\_vdfs\_8.0.3-0.104.25926924
- VMware\_bootbank\_esxio-base\_8.0.3-0.104.25926924
- VMware\_bootbank\_esx-base\_8.0.3-0.104.25926924

- VMware\_bootbank\_loadesx\_8.0.3-104.25926924
- VMware\_bootbank\_esx-update\_8.0.3-104.25746436
- VMware\_bootbank\_loadesxio\_8.0.3-104.25926924
- VMware\_bootbank\_esxio-update\_8.0.3-104.25926924
- VMW\_bootbank\_lpfc\_14.4.0.48-35vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-core-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-core\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-rdma-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc\_4.23.9.1-1vmw.803.0.104.25926924
- VMW\_bootbank\_nmlx5-cc-esxio\_4.23.9.1-1vmw.803.0.104.25926924
- VMware\_bootbank\_vmware-hbrsrv\_8.0.3-0.104.25926924
- VMW\_bootbank\_nvmetcp-esxio\_1.0.1.38-1vmw.803.0.104.25926924
- VMW\_bootbank\_nvmetcp\_1.0.1.38-1vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-ens\_2.0.0.23-7vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-ens-esxio\_2.0.0.23-7vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3\_2.0.0.31-13vmw.803.0.104.25926924
- VMW\_bootbank\_nvmxnet3-esxio\_2.0.0.31-13vmw.803.0.104.25926924

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

**This patch resolves the following issues:**

**ESXi 8.0 Update 3m includes the following Intel microcode:**

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

Intel Xeon E3-1100 Series; Intel Xeon E3-1200 Series; Intel i7-2655-LE Series; Intel i3-2100 Series

Sandy Bridge EP

0x206d6 (06/2d/6)

0x6d

baseline

0x621

3/4/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Sandy Bridge EP

0x206d7 (06/2d/7)

0x6d

baseline

0x71a

3/24/2020

Intel Pentium 1400 Series; Intel Xeon E5-1400 Series; Intel Xeon E5-1600 Series; Intel Xeon E5-2400 Series; Intel Xeon E5-2600 Series; Intel Xeon E5-4600 Series

Ivy Bridge DT

0x306a9 (06/3a/9)

0x12

baseline

0x21

2/13/2019

Intel i3-3200 Series; Intel i7-3500-LE/UE; Intel i7-3600-QE; Intel Xeon E3-1200-v2 Series; Intel Xeon E3-1100-C-v2 Series; Intel Pentium B925C

Haswell DT

0x306c3 (06/3c/3)

0x32

baseline

0x28

11/12/2019

Intel Xeon E3-1200-v3 Series; Intel i7-4700-EQ Series; Intel i5-4500-TE Series; Intel i3-4300 Series

Ivy Bridge EP

0x306e4 (06/3e/4)

0xed

baseline

0x42e

3/14/2019

Intel Xeon E5-4600-v2 Series; Intel Xeon E5-2600-v2 Series; Intel Xeon E5-2400-v2 Series; Intel Xeon E5-1600-v2 Series; Intel Xeon E5-1400-v2 Series

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

Intel Xeon E5-4600-v3 Series; Intel Xeon E5-2600-v3 Series; Intel Xeon E5-2400-v3 Series; Intel Xeon E5-1600-v3 Series; Intel Xeon E5-1400-v3 Series

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

Intel Core i7-5700EQ; Intel Xeon E3-1200-v4 Series

Avoton

0x406d8 (06/4d/8)

0x01

baseline

0x12d

9/16/2019

Intel Atom C2300 Series; Intel Atom C2500 Series; Intel Atom C2700 Series

Broadwell EP/EX

0x406f1 (06/4f/1)

0xef

baseline

0xb000040

5/19/2021

Intel Xeon E7-8800/4800-v4 Series; Intel Xeon E5-4600-v4 Series; Intel Xeon E5-2600-v4 Series; Intel Xeon E5-1600-v4 Series

Skylake SP

0x50654 (06/55/4)

0xb7

baseline

0x2007006

3/6/2023

Intel Xeon Platinum 8100 Series; Intel Xeon Gold 6100/5100, Silver 4100, Bronze 3100 Series; Intel Xeon D-2100 Series; Intel Xeon D-1600 Series; Intel Xeon W-3100 Series; Intel Xeon W-2100 Series

Cascade Lake B-0

0x50656 (06/55/6)

0xbf

baseline

0x4003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cascade Lake

0x50657 (06/55/7)

0xbf

baseline

0x5003901

12/12/2024

Intel Xeon Platinum 9200/8200 Series; Intel Xeon Gold 6200/5200; Intel Xeon Silver 4200/Bronze 3200; Intel Xeon W-3200

Cooper Lake

0x5065b (06/55/b)

0xbf

baseline

0x7002b01

12/12/2024

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300

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

Intel Xeon E3-1500-v5 Series; Intel Xeon E3-1200-v5 Series

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

Intel Xeon Platinum 8300 Series; Intel Xeon Gold 6300/5300 Series; Intel Xeon Silver 4300 Series

Ice Lake D

0x606c1 (06/6c/1)

0x10

baseline

0x1000301

3/9/2026

Intel Xeon D-2700 Series; Intel Xeon D-1700 Series

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

0x2b000685

3/2/2026

Intel Xeon Platinum 8400 Series; Intel Xeon Gold 6400/5400 Series; Intel Xeon Silver 4400 Series; Intel Xeon Bronze 3400 Series

Kaby Lake H/S/X

0x906e9 (06/9e/9)

0x2a

baseline

0xf8

9/28/2023

Intel Xeon E3-1200-v6 Series; Intel Xeon E3-1500-v6 Series

Coffee Lake

0x906ea (06/9e/a)

0x22

baseline

0xfa

7/28/2024

Intel Xeon E-2100 Series; Intel Xeon E-2200 Series (4 or 6 core)

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

0xa000151

3/24/2026

Intel Xeon 6500P/6700P/6900P Series

Granite Rapids AP/SP

0xa06d1 (06/ad/1)

0x95

baseline

0x1000434

4/27/2026

Intel Xeon 6500P/6700P/6900P Series

Sierra Forest

0xa06f3 (06/af/3)

0x01

baseline

0x30003b2

3/16/2026

Intel Xeon 6700E/6900E Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x32

baseline

0x133

10/8/2025

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0671 (06/b7/1)

0x36

baseline

0x137

2/18/2026

Intel Xeon E-2400 Series

Raptor Lake E/HX/S

0xb0674 (06/b7/4)

0x32

baseline

0x133

10/8/2025

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

0x210002f4

3/2/2026

Intel Xeon 8500 Series; Intel Xeon Gold 6500/5500 Series; Intel Xeon Silver 4500 Series; Intel Xeon Bronze 3500 Series

## ESXi 8.0 U3m - 25926933

**Name**

ESXi

**Version**

ESXi 8.0 U3m - 25926933

**Release Date**

November 19, 2026

**Category**

Bugfix

**Affected Components**

- ESXi Component - core ESXi VIBs
- ESXi Install/Upgrade Component
- ESXi Install/Upgrade Component
- Broadcom Emulex Connectivity Division lpfc driver for FC adapters
- USB Native Driver for VMware

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

This patch resolves the issues listed in the ESXi\_8.0.3-0.106.25926933 bulletin.

## ESXi 8.0 U3sm - 25926924

**Name**

ESXi

**Version**

ESXi 8.0 U3sm - 25926924

**Release Date**

November 19, 2026

**Category**

Security

**Live Patchable**

No

**Affected Components**

- ESXi Component - core ESXi VIBs
- ESXi Install/Upgrade Component
- ESXi Install/Upgrade Component
- Broadcom Emulex Connectivity Division lpfc driver for FC adapters
- USB Native Driver for VMware
- Mellanox 5th generation NICs (ConnectX and BlueField DPU series) core Ethernet and RoCE Drivers for VMware ESXi
- Host Based Replication Server for ESX
- VMware NVMe over TCP Driver
- ESXi Tools Component
- Network ENS driver for VMware vmxnet3
- Virtual Ethernet Controller
- Network driver for VMware vmxnet3
- Virtual Ethernet Controller

**PRs Fixed**

N/A

**Related CVE numbers**

N/A

This patch resolves the issues listed in the ESXi\_8.0.3-0.104.25926924 bulletin.

## Known  Issues from Previous Releases

## Installation, Upgrade, and Migration Issues

**If you update your vCenter to 8.0 Update 1, but ESXi hosts remain on an earlier version, vSphere Virtual Volumes datastores on such hosts might become inaccessible**

Self-signed VASA provider certificates are no longer supported in vSphere 8.0 and the configuration option **Config.HostAgent.ssl.keyStore.allowSelfSigned** is set to **false** by default. If you update a vCenter instance to 8.0 Update 1 that introduces vSphere APIs for Storage Awareness (VASA) version 5.0, and ESXi hosts remain on an earlier vSphere and VASA version, hosts that use self-signed certificates might not be able to access vSphere Virtual Volumes datastores or cannot refresh the CA certificate.

Workaround: Update hosts to ESXi 8.0 Update 1. If you do not update to ESXi 8.0 Update 1, see VMware knowledge base article [91387](https://kb.vmware.com/s/article/91387).

**Migration of vGPU virtual machines fails with the error "Timed out waiting for migration data"**

vSphere vMotion tasks on a vGPU VM might fail due to an NVIDIA driver issue on the source ESXi host. The source host might fail to transmit the complete checkpoint of the GPU, which results in a timeout on the destination host. In certain situations, the NVIDIA driver does not return control to the ESXi hypervisor, which further complicates resuming the workload.

Workaround: None. Upgrade to the latest ESXi version and NVIDIA GRID driver to reduce the probability of failure.

**The Cancel option in an interactive ESXi installation might not work as expected**

Due to an update of the Python library, the Cancel option by pressing the ESC button in an interactive ESXi installation might not work as expected. The issue occurs only in interactive installations, not in scripted or upgrade scenarios.

Workaround: Press the ESC key twice and then press any other key to activate the Cancel option.

**If you apply a host profile using a software FCoE configuration to an ESXi 8.0 host, the operation fails with a validation error**

Starting from vSphere 7.0, software FCoE is deprecated, and in vSphere 8.0 software FCoE profiles are not supported. If you try to apply a host profile from an earlier version to an ESXi 8.0 host, for example to edit the host customization, the operation fails. In the vSphere Client, you see an error such as Host Customizations validation error.

Workaround: Disable the Software FCoE Configuration subprofile in the host profile.

**VMNICs might be down after an upgrade to ESXi 8.0**

If the peer physical switch of a VMNIC does not support Media Auto Detect, or Media Auto Detect is disabled, and the VMNIC link is set down and then up, the link remains down after upgrade to or installation of ESXi 8.0.

Workaround: Use either of these 2 options:

1. Enable the optionmedia-auto-detectin the BIOS settings by navigating to System Setup Main Menu, usually by pressing or opening a virtual console, and then F2 > Device Settings > \<specific broadcom NIC> > Device Configuration Menu. Reboot the host.Media Auto Detect2. Alternatively, use an ESXCLI command similar to:esxcli network nic set -S \<your speed> -D full -n \<your nic>. With this option, you also set a fixed speed to the link, and it does not require a reboot.

**After upgrade to ESXi 8.0, you might lose some nmlx5\_core driver module settings due to obsolete parameters**

Some module parameters for the nmlx5\_core driver, such as device\_rss, drss and rss, are deprecated in ESXi 8.0 and any custom values, different from the default values, are not kept after an upgrade to ESXi 8.0.

Workaround: Replace the values of the device\_rss, drss and rss parameters as follows:

- device\_rss: Use theDRSSparameter.
- drss: Use theDRSSparameter.
- rss: Use theRSSparameter.

## Miscellaneous Issues

**ESXi hosts might become unresponsive, and you see a vpxa dump file due to a rare condition of insufficient file descriptors for the request queue on vpxa**

In rare cases, when requests to the vpxa service take long, for example waiting for access to a slow datastore, the request queue on vpxa might exceed the limit of file descriptors. As a result, ESXi hosts might briefly become unresponsive, and you see a vpxa-zdump.00\* file in the /var/core directory. The vpxa logs contain the line Too many open files.

Workaround: None. The vpxa service automatically restarts and corrects the issue.

**RDMA over Converged Ethernet (RoCE) traffic might fail in Enhanced Networking Stack (ENS) and VLAN environment, and a Broadcom RDMA network interface controller (RNIC)**

The VMware solution for high bandwidth, ENS, does not support MAC VLAN filters. However, a RDMA application that runs on a Broadcom RNIC in an ENS + VLAN environment, requires a MAC VLAN filter. As a result, you might see some RoCE traffic disconnected. The issue is likely to occur in a NVMe over RDMA + ENS + VLAN environment, or in an ENS+VLAN+RDMA app environment, when an ESXi host reboots or an uplink goes up and down.

Workaround: None

**The irdman driver might fail when you use Unreliable Datagram (UD) transport mode ULP for RDMA over Converged Ethernet (RoCE) traffic**

If for some reason you choose to use the UD transport mode upper layer protocol (ULP) for RoCE traffic, the irdman driver might fail. This issue is unlikely to occur, as the irdman driver only supports iSCSI Extensions for RDMA (iSER), which uses ULPs in Reliable Connection (RC) mode.

Workaround: Use ULPs with RC transport mode.

**You might see compliance errors during upgrade to ESXi 8.0 Update 2b on servers with active Trusted Platform Module (TPM) encryption and vSphere Quick Boot**

If you use the vSphere Lifecycle Manager to upgrade your clusters to ESXi 8.0 Update 2b, in the vSphere Client you might see compliance errors for hosts with active TPM encryption and vSphere Quick Boot.

Workaround: Ignore the compliance errors and proceed with the upgrade.

**Reset or restore of the ESXi system configuration in a vSphere system with DPUs might cause invalid state of the DPUs**

If you reset or restore the ESXi system configuration in a vSphere system with DPUs, for example, by selecting **Reset System Configuration** in the direct console, the operation might cause invalid state of the DPUs. In the DCUI, you might see errors such as Failed to reset system configuration. Note that this operation cannot be performed when a managed DPU is present. A backend call to the -f force reboot option is not supported for ESXi installations with a DPU. Although ESXi 8.0 supports the -f force reboot option, if you use reboot -f on an ESXi configuration with a DPU, the forceful reboot might cause an invalid state.

Workaround: Reset System Configuration in the direct console interface is temporarily disabled. Avoid resetting the ESXi system configuration in a vSphere system with DPUs.

**In a vCenter Server system with DPUs, if IPv6 is disabled, you cannot manage DPUs**

Although the vSphere Client allows the operation, if you disable IPv6 on an ESXi host with DPUs, you cannot use the DPUs, because the internal communication between the host and the devices depends on IPv6. The issue affects only ESXi hosts with DPUs.

Workaround: Make sure IPv6 is enabled on ESXi hosts with DPUs.

**You might see 10 min delay in rebooting an ESXi host on HPE server with pre-installed Pensando DPU**

In rare cases, HPE servers with pre-installed Pensando DPU might take more than 10 minutes to reboot in case of a failure of the DPU. As a result, ESXi hosts might fail with a purple diagnostic screen and the default wait time is 10 minutes.

Workaround: None.

**If you have an USB interface enabled in a remote management application that you use to install ESXi 8.0, you see an additional standard switch vSwitchBMC with uplink vusb0**

Starting with vSphere 8.0, in both Integrated Dell Remote Access Controller (iDRAC) and HP Integrated Lights Out (ILO), when you have an USB interface enabled, vUSB or vNIC respectively, an additional standard switch vSwitchBMC with uplink vusb0 gets created on the ESXi host. This is expected, in view of the introduction of data processing units (DPUs) on some servers but might cause the VMware Cloud Foundation Bring-Up process to fail.

Workaround: Before vSphere 8.0 installation, disable the USB interface in the remote management application that you use by following vendor documentation.

After vSphere 8.0 installation, use the ESXCLI command esxcfg-advcfg -s 0 /Net/BMCNetworkEnable to prevent the creation of a virtual switch vSwitchBMC and associated portgroups on the next reboot of host.

See this script as an example:

\~# esxcfg-advcfg -s 0 /Net/BMCNetworkEnable

The value of BMCNetworkEnable is 0 and the service is disabled.

\~# reboot

On host reboot, no virtual switch, PortGroup and VMKNIC are created in the host related to remote management application network.

**If an NVIDIA BlueField DPU is in hardware offload mode disabled, virtual machines with configured SR-IOV virtual function cannot power on**

NVIDIA BlueField DPUs must be in hardware offload mode enabled to allow virtual machines with configured SR-IOV virtual function to power on and operate.

Workaround: Always use the default hardware offload mode enabled for NVIDIA BlueField DPUs when you have VMs with configured SR-IOV virtual function connected to a virtual switch.

## Networking Issues

**You cannot set the Maximum Transmission Unit (MTU) on a VMware vSphere Distributed Switch to a value larger than 9174 on a Pensando DPU**

If you have the vSphere Distributed Services Engine feature with a Pensando DPU enabled on your ESXi 8.0 system, you cannot set the Maximum Transmission Unit (MTU) on a vSphere Distributed Switch to a value larger than 9174.

Workaround: None.

**Connection-intensive RDMA workload might lead to loss of traffic on Intel Ethernet E810 Series devices with inbox driver irdman-1.4.0.1**

The inbox irdman driver version 1.4.0.1 does not officially support vSAN over RDMA. Tests running 10,000 RDMA connections, usual for vSAN environments, might occasionally lose all traffic on Intel Ethernet E810 Series devices with NVM version 4.2 and irdman driver version 1.4.0.1.

Workaround: None.

**Transfer speed in IPv6 environments with active TCP segmentation offload is slow**

In environments with active IPv6 TCP segmentation offload (TSO), transfer speed for Windows virtual machines with an e1000e virtual NIC might be slow. The issue does not affect IPv4 environments.

Workaround: Deactivate TSO or use a vmxnet3 adapter instead of e1000e.

**You see link flapping on NICs that use the ntg3 driver of version 4.1.3 and later**

When two NICs that use the ntg3 driver of versions 4.1.3 and later are connected directly, not to a physical switch port, link flapping might occur. The issue does not occur on ntg3 drivers of versions earlier than 4.1.3 or the tg3 driver. This issue is not related to the occasional Energy Efficient Ethernet (EEE) link flapping on such NICs. The fix for the EEE issue is to use a ntg3 driver of version 4.1.7 or later, or disable EEE on physical switch ports.

Workaround: Upgrade the ntg3 driver to version 4.1.8 and set the new module parameter noPhyStateSet to 1. The noPhyStateSet parameter defaults to 0 and is not required in most environments, except they face the issue.

**You cannot use Mellanox ConnectX-5, ConnectX-6 cards Model 1 Level 2 and Model 2 for Enhanced Network Stack (ENS) mode in vSphere 8.0**

Due to hardware limitations, Model 1 Level 2, and Model 2 for Enhanced Network Stack (ENS) mode in vSphere 8.0 is not supported in ConnectX-5 and ConnectX-6 adapter cards.

Workaround: Use Mellanox ConnectX-6 Lx and ConnectX-6 Dx or later cards that support ENS Model 1 Level 2, and Model 2A.

**Pensando DPUs do not support Link Layer Discovery Protocol (LLDP) on physical switch ports of ESXi hosts**

When you enable LLDP on an ESXi host with a DPU, the host cannot receive LLDP packets.

Workaround: None.

## Storage Issues

**vSphere vMotion operations of virtual machines residing on Pure-backed vSphere Virtual Volumes storage might time out**

vSphere vMotion operations for VMs residing on vSphere Virtual Volumes datastores depend on the vSphere API for Storage Awareness (VASA) provider and the timing of VASA operations to complete. In rare cases, and under specific conditions when the VASA provider is under heavy load, response time from a Pure VASA provider might cause ESXi to exceed the timeout limit of 120 sec for each phase of vSphere vMotion tasks. In environments with multiple stretched storage containers you might see further delays in the Pure VASA provider response. As a result, running vSphere vMotion tasks time out and cannot complete.

Workaround: Reduce parallel workflows, especially on Pure storage on vSphere Virtual Volumes datastores exposed from the same VASA provider, and retry the vSphere vMotion task.

**You cannot create snapshots of virtual machines due to an error in the Content Based Read Cache (CBRC) that a digest operation has failed**

A rare race condition when assigning a content ID during the update of the CBRC digest file might cause a discrepancy between the content ID in the data disk and the digest disk. As a result, you cannot create virtual machine snapshots. You see an error such as An error occurred while saving the snapshot: A digest operation has failed in the backtrace. The snapshot creation task completes upon retry.

Workaround: Retry the snapshot creation task.

**vSphere Storage vMotion operations might fail in a vSAN environment due to an unauthenticated session of the Network File Copy (NFC) manager**

Migrations to a vSAN datastore by using vSphere Storage vMotion of virtual machines that have at least one snapshot and more than one virtual disk with different storage policy might fail. The issue occurs due to an unauthenticated session of the NFC manager because the Simple Object Access Protocol (SOAP) body exceeds the allowed size.

Workaround: First migrate the VM home namespace and just one of the virtual disks. After the operation completes, perform a disk only migration of the remaining 2 disks.

**In a vSphere Virtual Volumes stretched storage cluster environment, some VMs might fail to power on after recovering from a cluster-wide APD**

In high scale Virtual Volumes stretched storage cluster environments, after recovering from a cluster-wide APD, due to the high load during the recovery some VMs might fail to power on even though the datastores and protocol endpoints are online and accessible.

Workaround: Migrate the affected VMs to a different ESXi host and power on the VMs.

**You see "Object or item referred not found" error for tasks on a First Class Disk (FCD)**

Due to a rare storage issue, during the creation of a snapshot of an attached FCD, the disk might be deleted from the Managed Virtual Disk Catalog. If you do not reconcile the Managed Virtual Disk Catalog, all consecutive operations on such a FCD fail with the Object or item referred not found error.

Workaround: See [Reconciling Discrepancies in the Managed Virtual Disk Catalog.](https://knowledge.broadcom.com/external/article?legacyId=2147750)

## vSphere Lifecycle Manager Issues

**A remediation task by using vSphere Lifecycle Manager might intermittently fail on ESXi hosts with DPUs**

When you start a vSphere Lifecycle Manager remediation on an ESXi hosts with DPUs, the host upgrades and reboots as expected, but after the reboot, before completing the remediation task, you might see an error such as:

A general system error occurred: After host … remediation completed, compliance check reported host as 'non-compliant'. The image on the host does not match the image set for the cluster. Retry the cluster remediation operation.

This is a rare issue, caused by an intermittent timeout of the post-remediation scan on the DPU.

Workaround: Reboot the ESXi host and re-run the vSphere Lifecycle Manager compliance check operation, which includes the post-remediation scan.

## VMware Host Client Issues

**VMware Host Client might display incorrect descriptions for severity event states**

When you look in the VMware Host Client to see the descriptions of the severity event states of an ESXi host, they might differ from the descriptions you see by using Intelligent Platform Management Interface (IPMI) or Lenovo XClarity Controller (XCC). For example, in the VMware Host Client, the description of the severity event state for the PSU Sensors might be Transition to Non-critical from OK, while in the XCC and IPMI, the description is Transition to OK.

Workaround: Verify the descriptions for severity event states by using the ESXCLI command esxcli hardware ipmi sdr list and Lenovo XCC.

## Security Features Issues

**If you use an RSA key size smaller than 2048 bits, RSA signature generation fails**

Starting from vSphere 8.0, ESXi uses the OpenSSL 3.0 FIPS provider. As part of the FIPS 186-4 requirement, the RSA key size must be at least 2048 bits for any signature generation, and signature generation with SHA1 is not supported.

Workaround: Use RSA key size larger than 2048.
