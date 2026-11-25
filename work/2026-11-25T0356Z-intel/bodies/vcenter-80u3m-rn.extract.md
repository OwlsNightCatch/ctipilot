---
title: VMware vCenter 8.0 Update 3m Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-11-23"
fingerprint: b787bc464f61edd0
language: en
pagetype: article
filedate: "2026-11-25"
---
# VMware vCenter 8.0 Update 3m Release Notes

This document contains the following sections

## Introduction

VMware vCenter 8.0 Update 3m | 19 NOV 2026 | ISO Build 25934264

Check for additions and updates to these release notes.

## What's New

- This release resolves CVE-2026-123890. For more information on this vulnerability and its impact on Broadcom products, see[VMSA-2026-0009](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495).
- vCenter has upgraded open-source packages to incorporate the latest timezone changes.TZData:- : vCenter has upgraded open-source packages to confirm that eMudhra certificates are no longer in use.eMudhra- For Photon OS updates, see[VMware vCenter Server Appliance Photon OS Security Patches](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-appliance-photonos-security-patches.html).

**Secure Boot Platform Key (PK) Remediation:**

To address Microsoft 2011 Secure Boot certificate expirations, as detailed in Broadcom knowledge base article [423893](https://knowledge.broadcom.com/external/article/423893), vCenter 8.0 Update 3m introduces a vCenter alarm to proactively warns administrators when Secure Boot-enabled, powered-on virtual machines have an out-of-date NULL PK. This per-VM alarm is triggered once vCenter and the ESX host are upgraded to 8.0 Update 3m.

**vCenter alert on API session limits:**

vCenter 8.0 Update 3m adds an alert to the vCenter Appliance Management Interface (VAMI) that notifies you when vCenter API sessions reach a preconfigured threshold and prevents vCenter management capabilities such as API endpoints and vSphere Client to become unresponsive. Previously, the health alerts in vCenter did not include the API session metric and you could see a Healthy status despite the API session limit exhaustion. Now, you see the vCenter Session Health metric and can take action accordingly. The metric is configurable, with a default value of 90%.

## Upgrade Notes

- For supported upgrade paths from vCenter 8.0 Update 3m to later releases, see the[vCenter upgrade path matrix](https://interopmatrix.broadcom.com/Upgrade?productId=2&isHidePatch=false&isHideLegacyReleases=true).

## Build Details

## VMware vCenter 8.0 Update 3m

**Download Filename**

VMware-vCenter-Server-Appliance-8.0.3.01200-25934264-patch-FP.iso

**Build**

25934264

**Download Size**

8470 MB

**sha256checksum**

0666cff51ee265616022f1bb99f8b9c495caf626dfe2602cf7ddb8a33e7c8c0c

**CVEs**

CVE-2026-123890

## Download and Installation

Log in to the [Broadcom Support Portal](https://support.broadcom.com/) to download this [patch](https://support.broadcom.com/web/ecx/solutiondetails?patchId=16137).

For more information on using the vCenter Server shells, see VMware knowledge base article [2100508](https://kb.vmware.com/s/article/2100508).

For more information on patching vCenter Server, see [Patching and Updating vCenter Server 8.0 Deployments](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-server-upgrade-8-0/patching-and-updating-vcenter-server.html).

For more information on staging patches, see [Upgrading the vCenter Server Appliance](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-server-upgrade-8-0/upgrading-and-updating-the-vcenter-server-appliance/preparing-to-upgrade-vcenter-server-appliance.html).

## Resolved Issues

## Miscellaneous Issues

A**fter renewal, you see Solution User certificates with 2-year validity instead of the expected 10 years**

When you use the vSphere Certificate Manager Utility to renew or replace a solution user certificate, if you set the option **Do you wish to generate all certificates using configuration file** to Y, the new certificates default to a 2-year validity period. If the option is set to N, the solution user certificates are generated with a validity period of 10 years, which is the expected and documented behavior.

This issue is resolved in this release.

## vSphere Client and vCenter Issues

**After a vCenter upgrade, the SNMP agent is enabled by default** 

After a vCenter upgrade, the SNMP agent might be automatically enabled, even if it was not active before the upgrade.

This issue is resolved in this release.

**Compliance checks or remediation against a vSphere Lifecycle Manager desired image might fail due to excessive metadata**

During scans, remediations, or updates, vCenter sends excessive metadata to ESX hosts while processing depots that contain base images, add-ons, components, and manifests. As a result, such metadata might overload the memory pool of an ESX host and lead to scan and remediation failures. In the vSphere Client, you might see errors such as:

Host status is unknown An internal error occurred while staging/remediating host

SHA-1 signature found in host certificate False. Support for certificates with weak signature algorithm

SHA-1 has been removed in ESXi 8.0. To proceed with upgrade, replace it with a SHA-2 signature based certificate.

The ESXi host encounters memory exhaustion within the host/vim/vmvisor/settingsd-task-forks resource group, as described in Broadcom knowledge base article [449182](https://knowledge.broadcom.com/external/article/449182). The default memory limit is insufficient for the vSphere Lifecycle Manager daemon to parse the metadata zip files provided by the vCenter Server during the upgrade/remediation process. The /var/run/log/lifecycle.log file on the ESXi host, you see an error such as Current ESXi version does not provide a mechanism to mount a tardisk into a ramdisk.

This issue is resolved in this release.

**Scheduled vCenter file-based backups might fail intermittently when several vCenter instances back up to the same backup location**

Before each backup, vCenter checks the backup server, creates a directory vCenter/backup\_\<YYYYMMDD-HHMM> in the backup location, writes a sample file to it, and deletes every vCenter/backup\_\* directory. The vCenter/backup\_\<YYYYMMDD-HHMM> directory has only a one-minute UTC timestamp and since backup checks of different vCenter instances might overlap, the creation and deletion of backup directories for the different vCenter instances might be misplaced. As a result, you might see backup failures before any data is transferred. For example:

SFTP: /var/log/vmware/applmgmt/applmgmt.log shows curl: (21) mkdir command failed for vCenter/backup\_\<timestamp>/, and the job fails with "Backup job failed to start due to server validation failure.

NFS: /var/log/vmware/applmgmt/backupValidate.log shows Failed in backup connection validation: Failed to dispatch sample file, and applmgmt.log shows data stream command status: errcode: 2.

This issue is resolved in this release. With the fix, each vCenter instance names its directory with the pattern backup\_\<hostname>\_\<YYYYMMDD-HHMM> and deletes only that directory.

**Content library synchronization occasionally fails due to a reported missing file, even though the library is fully in sync and the file exists on the publisher**

The pagination queries during a content library sync might not use a fully deterministic sort order. As a result, for libraries containing more than 100 items, some file records belonging to the same item might be returned in an inconsistent order across paginated queries. Occasionally, a file that is already present, might be identified as missing and scheduled for deletion during a subscribed library sync.

This issue is resolved in this release. The pagination queries used during library-item sync now sort deterministically by item, version, and file identifiers, ensuring files are consistently accounted for across paginated results.

**You see an in-progress alarm for vSphere High Availability (HA) failover for powered-off or deleted virtual machines**

Due to an internal race condition in the Fault Domain Manager (FDM), a VM might incorrectly remain protected in the memory of the FDM primary host. As a result, in the vSphere Client, you see an in-progress alarm for vSphere HA failover for powered-off or deleted virtual machines.

This issue is resolved in this release.

**vCenter might become unresponsive due to a sync issue with the internal database**

During configuration changes of a distributed virtual portgroup, vCenter might lose sync with the internal database. As a result, when the sync is reestablished, the vpxd service might fail instead of recovering gracefully, and vCenter becomes unresponsive.

This issue is resolved in this release.

**vCenter vpxd service might intermittently fail during backup operations due to a missing InstanceUUID in a virtual machine**

A missing InstanceUUID parameter in a virtual machine during VM backup operations with a 3-rd party tool might cause the vpxd service to fail with a core.vpxd-worker dump and Program terminated with signal SIGABRT, Aborted error.

This issue is resolved in this release.

**After an upgrade, ESXi hosts might lose access to vSphere Virtual Volumes datastore if the VASA Provider is version 4.0 or earlier**

After upgrading an ESXi host, it might lose access to the vSphere Virtual Volumes datastore and the VASA Provider shows a sync error, indicating broken communication between the vvold service and the VASA Provider. The issue occurs with VASA 4.0 or earlier, when the retainVasaProviderCertificate flag is set to True and a self-signed certificate is used, because the certificate is not stored in PEM format.

This issue is resolved in this release.

**VM web console shows a black screen when the guest OS enters power-saving mode**

When a virtual machine guest operating system enters power-saving mode after a period of inactivity, the guest OS terminates all active web console sessions. If you attempt to open a new web console in the vSphere Client, a black screen appears with a loading spinner that spins indefinitely.

This issue is resolved in this release.

**Advanced export omits Type and User columns from exported CSV files**

When you use **Advanced export** in the vSphere Client, the resulting CSV file omits the **Type** and **User** columns, regardless if you select **All columns** or **Selected columns** in the export options.

This issue is resolved in this release.

## Upgrade Issues

**vCenter file-based backups to an OpenSSH 9.9 SFTP server with PerSourcePenalties enabled might fail with: curl: (2) Failure establishing ssh session: -43, Failed getting banner**

During the creation of a SSH tunnel, vCenter  performs host-key discovery and authentication checks before transferring the backup. This connection sequence can trigger OpenSSH 9.9 per-source penalties, temporarily blocking connections from vCenter and preventing the password-authenticated SFTP fallback from completing the SSH handshake.

This issue is resolved in this release. The fix adjusts the connection sequence and reduces authentication attempts to allow backup transfers to proceed.

## vSAN Issues

**Configuring vSAN File Service with Active Directory domain fails with an error for exception caught when running pre-flight check on the file server**

In the vSphere Client, when you create a file service domain with AD and click Next, you see an error such as: Failed to check domain configuration: Exception caught when running preflight check on file server. The issue occurs because querying the Active Directory domain for LDAP SRV records returns multiple duplicate entries for the same Domain Controller hostname. As a result, the pre-flight check script causes an exception and fails the file service enablement workflow.

## vSphere Lifecycle Manager Issues

**VMware vSphere Update Manager Download Service (UMDS) configuration removes deprecated hostupdate URLs and adds entitlement token support**

Starting with vCenter 8.0 Update 3m, UMDS configuration no longer includes the deprecated hostupdate URLs such as https://hostupdate.vmware.com/software/VUM/PRODUCTION/main/vmw-depot-index.xml. The new depots are located at https://dl.broadcom.com and require an entitlement token to access the content. You can use the new CLI option vmware-umds -S --add-entitlement-token \<tokenID> to configure UMDS with the new depot URLs using your entitlement token.

This issue is resolved in this release. For more information, see Broadcom knowledge base article [390123](https://knowledge.broadcom.com/external/article/390123).

## Known  Issues from Previous Releases

## Installation, Upgrade, and Migration Issues

**If you do not open port 9087 in your firewall between ESXi hosts and vCenter, compliance checks and vSphere HA might fail after vCenter update to 8.0 Update 3**

Starting from 8.0 Update 3, the vSphere Lifecycle Manager downloads updates for ESXi hosts by a HTTPS connection to the vCenter instance on port 9087. If you do not open port 9087 in your firewall between ESXi hosts and vCenter, you might see compliance check errors. For example, in the lifecycle.log you see messages such as:

\<Timestamp> In(14) lifecycle\[2112988\]: Downloader:373 Opening https://\<VC-FQDN>:9087/vum/repository/hostupdate/\_\_micro-depot\_\_vendor-DEL\_\_DEL-ESXi-8.0-Addon-cumulative\_metadata\_\_index\_\_.xml for download

\<Timestamp> Wa(12) lifecycle\[2112988\]: Downloader:210 Download failed: \<urlopen error timed out>, 9 retry left...

In addition, vSphere HA might fail to start.

Workaround: Open port 9087 in your firewall between ESXi hosts and vCenter by using the TCP protocol.

**In a mixed vSphere 7.x and 8.x environment with vSphere DRS, an incompatible virtual machine might prevent an ESXi host to enter maintenance mode**

In a mixed vSphere 7.x and 8.x environment with DRS, a VM of 7.x version that is not compatible with ESXi 8.0 Update 1 and later might prevent an ESXi 8.0 Update 1 host to enter maintenance mode. The issue is specific for virtual machines with VMDK on a vSphere Virtual Volumes datastore. In the vSphere Client, you see an error such as Waiting for all VMs to be powered off or suspended or migrated. In a DRS cluster check the Faults page on the DRS tab for troubleshooting.

Workaround: Power-off the incompatible virtual machine.

**vSphere Lifecycle Manager baseline check compliance fails on ESXi hosts of version 7.0 GA in a vCenter 8.0 Update 3 system**

Due to a limitation of the esxupdate memory resource pool on 7.0 GA ESXi hosts, a vSphere Lifecycle Manager baseline check compliance scan might fail on 7.0 GA ESXi host in a vCenter 8.0 Update 3 system with error such as The host returns esxupdate error codes: -1.

The host esxupdate.log contains an error such as:

\<Timestamp> esxupdate: \<PID>: esxupdate: ERROR: vmware.runcommand.RunCommandError:

Error running command '\['/sbin/smbiosDump'\]': \[Errno 12\] Cannot allocate memory

The vmkernel.log contains error such as:

\<Timestamp> cpu0:\<PID>)Admission failure in path: host/vim/vmvisor/esxupdate/python.\<PID>:python.\<PID>:uw.\<PID>

This issue is specific for 7.0 GA ESXi hosts, as esxupdate memory allocation is increased in 7.0 Update 1 and later.

Workaround: Use an ISO upgrade baseline to upgrade the 7.0 GA ESXi hosts to a 8.x version or revert the vCenter system back to version 7.0 and upgrade the hosts to a version of 7.0 Update 1 and later.

**You see an error Failed to get ceip status in the Virtual Appliance Management Interface (VAMI) during update to vCenter Server 8.0 Update 1**

During an update, vCenter stops and restarts the VMDir service and within this interval, if you try to log in to the VAMI, you might see an error such as **Failed to get ceip status**. This is expected and does not indicate an actual issue with the vCenter system.

Workaround: Wait for the VMDir service to restart and refresh the Virtual Appliance Management Interface.

**If you click NEXT before the progress bar reaches 100% in a vCenter Server Lifecycle Manager plug-in upgrade, the Server Lifecycle Manager service fails**

In the Upgrade Plug-in step of the vCenter Server Lifecycle Manager plug-in upgrade wizard, if you click NEXT before the progress bar reaches 100%, the Server Lifecycle Manager service fails.

Workaround: Wait for the progress bar to reach 100% before you click NEXT.

**vCenter upgrade or update to 8.0 Update 2a or later fails during precheck with the error "VMCA root certificate validation failed"**

If your vCenter system has a legacy VMCA root certificate dating back to version 5.x which does not have the Subject Key Identifier (SKID) extension, upgrades and updates to vCenter 8.0 Update 2 and later fail because the OpenSSL version 3.0 in 8.0 Update 2 is not compatible with legacy root certificates. vCenter Server 8.0 Update 2a adds a precheck to detect this issue and shows the error message VMCA root certificate validation failed if the source vCenter has VMCA root certificate without SKID.

Workaround: Regenerate a VMCA root certificate by following the steps in VMware knowledge base article [94840](https://kb.vmware.com/s/article/94840).

**You see a "vc.health.error.dbjob3" warning after a vCenter upgrade**

In the vSphere Client or the in Virtual Appliance Management Interface, you might see the warning vc.health.error.dbjob3 after a vCenter upgrade although the vCenter overall health status is green. This issue does not affect vCenter operations, it can only affect historical statistics when some data does not roll up for more than 72 hours.

Workaround: See [Delete old tasks, events and statistics data in vCenter Server 5.x, 6.x, 7.x and 8.x](https://knowledge.broadcom.com/external/article?legacyId=2110031) how to clear stats data, if not relevant anymore.

**Update to vCenter 8.0 Update 3 might fail with an error "Destination path '/storage/analytics/stage/...' already exists"**

Starting with vCenter 8.0 Update 3, the analytics service stores telemetry log files in a new directory.

In rare cases, if previous update attempts had failed and reverted, when patching to vCenter 8.0 Update 3, the attempt to copy the telemetry log files to the new location might fail because these files already exist from a prior patching attempt. In the patchrunner.log file, you see an error such as Destination path '/storage/analytics/stage/XXXXXX\_processed\_logs' already exists.

Workaround: Delete all files under /storage/log/vmware/analytics/stage,/storage/log/vmware/analytics/prod, /storage/analytics/stage, and /storage/analytics/prod, and retry the update.

**You see a security warning for the ESX Agent Manager configuration during the pre-check phase of a vCenter upgrade**

During the pre-check phase of a vCenter update or upgrade, in the vSphere Client and logs, you might see an error such as:

Source ESX Agent Manager Configuration contains URLs that are not trusted by the System! Verify following URLs and their respective statuses and follow KB 93526.

Workaround: For more information, see VMware knowledge base article [93526](https://kb.vmware.com/s/article/93526).

**Firmware compliance details are missing from a vSphere Lifecycle Manager image compliance report for an ESXi standalone host**

Firmware compliance details might be missing from a vSphere Lifecycle Manager image compliance report for an ESXi standalone host in two cases:

1. You run a compliance report against a standalone host managed with a vSphere Lifecycle Manager image from vSphere Client and then navigate away before the compliance report gets generated.
2. You trigger a page refresh after the image compliance reports are generated.

In such cases, even when you have the firmware package available in the Desired State, the firmware compliance section remains empty when you revisit or refresh the vSphere Client browsing session. If you use GET image compliance API, then firmware compliance details are missing from the response.

Workaround: Invoke the image compliance scan for a standalone host managed with a vSphere Lifecycle Manager image by using the vSphere Client and do not navigate away or refresh the browser. For API, use the Check image compliance API for fetching the firmware details as apposed to GET image compliance.

**If you apply a host profile using a software FCoE configuration to an ESXi 8.0 host, the operation fails with a validation error**

Starting from vSphere 7.0, software FCoE is deprecated, and in vSphere 8.0 software FCoE profiles are not supported. If you try to apply a host profile from an earlier version to an ESXi 8.0 host, for example to edit the host customization, the operation fails. In the vSphere Client, you see an error such as Host Customizations validation error.

Workaround: Disable the Software FCoE Configuration subprofile in the host profile.

**URL-based patching or file-based backup of vCenter 8.0 Update 2 might fail due to OpenSSL noncompliance to Federal Information Processing Standards (FIPS)**

With vCenter 8.0 Update 2, OpenSSL works only with Diffie-Hellman parameters compliant to NIST SP 800-56A and FIPS 140-2. For URL-based patching or file-based backup of vCenter 8.0 Update 2 systems, FTPS servers in your environment must support the following ciphers:

OpenSSL Cipher Suite

Name AT-TLS Cipher Suite Name

Hexadecimal Value

DHE-RSA-AES256-SHA

TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA

39

DHE-DSS-AES256-SHA

TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA

38

AES256-SHA

TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA

35

EDH-RSA-DES-CBC3-SHA

TLS\_DHE\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

16

EDH-DSS-DES-CBC3-SHA

TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA

13

DES-CBC3-SHA

TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

0A

DHE-RSA-AES128-SHA

TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA

33

DHE-DSS-AES128-SHA

TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA

32

AES128-SHA

TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA

2F

Workaround: Make sure your file servers are FIPS compliant.

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

**ESXi hosts might become unresponsive, and you see a vpxa dump file due to a rare condition of insufficient file descriptors for the request queue on vpxa**

In rare cases, when requests to the vpxa service take long, for example waiting for access to a slow datastore, the request queue on vpxa might exceed the limit of file descriptors. As a result, ESXi hosts might briefly become unresponsive, and you see a vpxa-zdump.00\* file in the /var/core directory. The vpxa logs contain the line Too many open files.

Workaround: None. The vpxa service automatically restarts and corrects the issue.

## Networking Issues

**Overlapping hot-add and hot-remove operations for DirectPath I/O devices might fail**

With vSphere 8.0 Update 1, by using vSphere API you can add or remove a DirectPath I/O device without powering off VMs. However, if you run several operations at the same time, some of the overlapping tasks might fail.

Workaround: Plan for 20 seconds processing time between each hot-add or hot-remove operation for DirectPath I/O devices.

**Hot adding and removing of DirectPath I/O devices is not automatically enabled on virtual machines**

With vSphere 8.0 Update 1, by using vSphere API you can add or remove a DirectPath I/O device without powering off VMs. When you enable the hotplug functionality that allows you to hot add and remove DirectPath I/O devices to a VM, if you use such a VM to create an OVF and deploy a new VM, the new VM might not have the hotplug functionality automatically enabled.

Workaround: Enable the hotplug functionality as described in [Hot-add and Hot-remove support for VMDirectPath I/O Devices.](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-networking/GUID-FAD98A33-EBFC-40D2-9BD2-195C0E620341.html)

**You cannot set the Maximum Transmission Unit (MTU) on a VMware vSphere Distributed Switch to a value larger than 9174 on a Pensando DPU**

If you have the vSphere Distributed Services Engine feature with a Pensando DPU enabled on your ESXi 8.0 system, you cannot set the Maximum Transmission Unit (MTU) on a vSphere Distributed Switch to a value larger than 9174.

Workaround: None.

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

**vSphere Storage vMotion operations might fail in a vSAN environment due to an unauthenticated session of the Network File Copy (NFC) manager**

Migrations to a vSAN datastore by using vSphere Storage vMotion of virtual machines that have at least one snapshot and more than one virtual disk with different storage policy might fail. The issue occurs due to an unauthenticated session of the NFC manager because the Simple Object Access Protocol (SOAP) body exceeds the allowed size.

Workaround: First migrate the VM home namespace and just one of the virtual disks. After the operation completes, perform a disk only migration of the remaining 2 disks.

## vCenter Server and vSphere Client Issues

**PR 3667115: When editing vSphere Namespace CPU limits in the vSphere Client, values higher than 1000 GHz are incorrectly handled**

If you set a CPU limit on a vSphere Namespace higher than 1000 GHz, the vSphere Client might fall back to the default unit (MHz) instead of the respective unit in Terahertz (THz). For example, if you set a CPU limit of 1500 GHz, you should see the metric as 1.5 THz, but in the Resource Limits modal, you see a value of 1.5 with the unit selection box appearing empty or unselected. If you save the setting in this state, the system defaults to MHz, effectively slashing the 1500 GHz (1.5 THz) limit down to just 1.5 MHz.

This issue is resolved in this release.

**You cannot hide or show plug-ins with 5-part version numbers in the vSphere Client**

In the vSphere Client, you cannot hide or show plug-ins registered with a 5-part version number, such as 9.0.0.0.12345, due to an issue with the serialization of 5-part package versions.

Workaround: None. Instead of hiding or showing a plug-in with a 5-part version number in the vSphere Client, you can unregister and re-register the plug-in to achieve a similar result.

**PR 3667116: In the vSphere Client, very large SCSI vSphere Virtual Volumes datastores might display incorrect capacity and free space values**

When a SCSI vSphere Virtual Volumes datastore exceeds several exabytes, the vSphere Client fails to format the numerical value because it exceeds the maximum unit type defined in the formatting service. As a result, you see such capacity values as undefined. For example, 8 undefined free or 8 undefined capacity. The CLI and the Managed Object Browser (MOB) report the correct values.

This issue is resolved in this release. The fix updates the storage unit service of the vSphere Client to handle and scale correctly extremely large capacity values to the maximum supported units.

**You cannot upload logs packages to a VMware service request by using the vSphere Client**

You cannot upload logs packages to a VMware service request by navigating in the vSphere Client to Administration > Support > Upload File to Service Request. Instead, you see a link to a KB article that provides steps to upload log bundles in the Broadcom Support Portal. This is expected.

Workaround: Follow the steps in [Uploading files to cases on the Broadcom Support Portal](https://knowledge.broadcom.com/external/article/140731/uploading-files-to-cases-on-the-broadcom.html).

**A rare race in the vCenter automated space\_cleanup utility when file-based backup is configured with an NFS volume might cause high memory usage**

vCenter 8.0 Update 3h has an automated space cleanup utility which is scheduled to run everyday at midnight to clean up old logs. In rare situations, due to a race condition, this scheduled cleanup task might conflict with the file-based backup and restore configured with an NFS mount point. As a result, you see high memory utilization from the space\_utility process, which might consume most memory on the vCenter. Instance.

Workaround: See KB [422390](https://knowledge.broadcom.com/external/article/422390).

**When you move a standalone ESXi host back to a cluster that you manage with vSphere Lifecycle Manager images, you might see an error in the vSphere Client**

If you move out an ESXi host from a cluster that you manage with vSphere Lifecycle Manager images, it becomes a standalone host that is connected to a vCenter Server instance but is not part of any cluster. If you move such a host back to a cluster, in the Updates tab of the vSphere Client you might see an error such as The host \[IP\] is not a vLCM managed standalone host. This message does not indicate a functional issue.

Workaround: Refresh the vSphere Client session or change the tab and return to the Updates tab.

**You see the same license product name displayed multiple times in the vSphere Client**

Starting with vSphere 8.0 Update 2b, you can apply a single Solution License to the components of VMware vSphere Foundation and VMware Cloud Foundation. In different screens in the vSphere Client, you might see the license product name multiplied by the number of components for which you use the license. For example, if you use a vSphere 8 Enterprise Plus for VMware Cloud Foundation license for 3 components, such as ESXi, vCenter, and vSphere with Tanzu, you see the name listed 3 times.

Workaround: None

**An external gateway firewall might block vSphere Pod traffic to clusterIPs**

When you deploy Supervisor Services on vSphere Pods with Supervisors configured with the VDS stack, traffic from the vSphere Pod to ClusterIPs goes through the external gateway and a custom firewall can block it.

Workaround: For more information, see [vSphere Pod Traffic to ClusterIP Time-outs](https://knowledge.broadcom.com/external/article?legacyId=97170).

**A scheduled task fails and doesn't schedule further runs**

With vSphere 8.0 Update 2, if a vCenter user is unauthorized or unauthenticated, all scheduled tasks they own fail and cannot be scheduled until the user privileges are restored or a different vSphere user takes over the scheduled tasks. In the vSphere Client, you see messages for failed tasks and reasons for the failure.

Workaround: Any vSphere user with sufficient privileges to edit scheduled tasks, including the current task owner with restored privileges, can click **Edit** and submit the scheduled task, without actually changing the scheduled task. For more information, see [Scheduling vSphere Tasks](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-vcenter-esxi-management/GUID-30D0B751-41A4-459E-B1DC-E9866083892F.html#GUID-F9DC9B18-625E-4ACB-AA3A-17BEB109A206__GUID-01AAD7FD-1CEF-4776-AD9B-FD506C7F905E).

## Virtual Machine Management Issues

**The vpxd agent might fail after expanding the disk size of a virtual machine with a NVMe controller in a vCenter 8.0 Update 3 mixed environment**

If you have ESXi hosts of version 8.0 Update 1 and earlier in your vCenter 8.0 Update 3 system, expanding the disk of a VM with a NVMe controller might cause the vpxd service to fail with core.vpxd-worker coredump.

Workaround: Upgrade your ESXi hosts of version 8.0 Update 1 and earlier to 8.0 Update 3. Alternatively, use the VMware Host Client to extend the disk size from Edit settings of the VM.

## vSphere Lifecycle Manager Issues

**In the vSphere Client, you see a different count of components in a vSphere Lifecycle Manager image**

When you prepare a vSphere Lifecycle Manager image for a cluster or standalone ESXi host, and manually add or remove components, you might see a different count of the components in Updates > Hosts > Image > Components and in the list of components when you click Show details. The discrepancy occurs when the vSphere Lifecycle Manager considers not to use some of the additional components, for example if a driver is being deprecated, or if you remove a component, such as VMware Tools or Host Client.

Workaround: None. You can safely ignore the difference in the count, because it does not impact the actual list of components that vSphere Lifecycle Manager uses for the image installation.

**You cannot edit the VMware vSphere Lifecycle Manager Update Download scheduled task**

In the vSphere Client, when you navigate to a vCenter Server instance and select Scheduled Tasks under the Configure tab, if you select the VMware vSphere Lifecycle Manager Update Download task and click Edit, you cannot modify the existing settings.

Workaround: You can edit the VMware vSphere Lifecycle Manager Update Download task by following the steps in the topic [Configure the vSphere Lifecycle Manager Automatic Download Task](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-lifecycle-manager/GUID-F6066939-F926-4FCC-A458-A7F150615975.html).

**Manually applied security advanced options on a vCenter system might not persist across vSphere Lifecycle Manager operations**

Some of all manually applied security advanced options on a vCenter system might not persist across vSphere Lifecycle Manager operations, such as upgrade, update, backup, or restore.

Workaround: Re-apply the manual settings after the vSphere Lifecycle Manager task completes.

**If a parallel remediation task fails, you do not see the correct number of ESXi hosts that passed or skipped the operation**

With vSphere 8.0, you can enable vSphere Lifecycle Manager to remediate all hosts that are in maintenance mode in parallel instead of in sequence. However, if a parallel remediation task fails, in the vSphere Client you might not see the correct number of hosts that passed, failed, or skipped the operation, or even not see such counts at all. The issue does not affect the vSphere Lifecycle Manager functionality, but only the reporting in the vSphere Client.

Workaround: None.

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

## Backup and Restore Issues

**SSH File Transfer Protocol (SFTP) backups fail while creating a directory on a remote backup server**

Repeated re-connection to a remote backup server while trying to create a SSH tunnel might cause backup server to reject connections from vCenter. As a result, in the backup logs, you see an error such as Failure establishing ssh session: -43, Failed getting banner.

Workaround: See KB [399004](https://knowledge.broadcom.com/external/article/399004).
