---
title: vCenter 9.1.2.0 Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-11-24"
fingerprint: be97ed44d945e898
language: en
pagetype: article
filedate: "2026-11-25"
---
# vCenter 9.1.2.0 Release Notes

This document contains the following sections

## Introduction

VMware vCenter 9.1.2.0 | 24 NOV 2026 | Build 25946533

Check for additions and updates to these release notes.

## What's New

- This release resolves CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, and CVE-2026-123909. For more information on these vulnerabilities and their impact on Broadcom products, see[VMSA-2026-0011](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626).
- vCenter has upgraded open-source packages to incorporate the latest timezone changes.TZData:- : vCenter has upgraded open-source packages to confirm that eMudhra certificates are no longer in use.eMudhra

**Synchronization of VM templates across linked vCenter instances in VCF Operations:**

Content Library now supports virtual machine template synchronization across vCenter instances that are linked using vCenter groups in VCF Operations. This allows you to maintain consistent, centralized template catalogs across distributed, multi-vCenter environments without requiring traditional Enhanced Linked Mode (ELM) configurations or manual replication workflows.

**Enhanced NFC Handling for Content Library Transfers:**

Content Library transfer sessions now dynamically calculate Network File Copy (NFC) timeouts based on the payload file size and transfer throughput, replacing the previous static 20-minute limit. This change prevents premature session timeouts and failed sync operations when transferring large VM templates, OVFs, and ISO images across high-latency or bandwidth-constrained networks.

**Resilient Cluster Configuration Remediation and Pre-Check Deadlock Prevention:**

You can now reliably remediate cluster configurations without being blocked by false-positive health check failures. You see an All pre-check results tab that groups results by cluster checks, cluster solutions, and hosts, which allows you to review each issue and select Ignore health check issues to proceed with the remediation. With the new capability, you can intentionally proceed with configuration remediation when the applied changes directly address the reported prerequisite issue, such as mounting required datastores to satisfy a vSphere HA dependency. For more information, see [Remediate a Cluster Against the Desired or Draft Configuration](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_068&appid=vsphere-9-1&language=&format=rendered).

**Disabling Automatic Compliance Checks in vSphere Configuration Profiles:**

You can now pause automatic vSphere Configuration Profiles operations on a cluster such as compliance checks and remediation to save resources and administration overhead:

- Turning off scheduled background compliance scans reduces vCenter CPU, memory, and database I/O utilization. This optimizes management performance across large enterprise environments with high cluster density.Reduced vCenter infrastructure overhead:- Administrators can run compliance checks on-demand or during designated maintenance windows. This prevents false-positive drift alarms and alert fatigue when temporary host changes are made during maintenance or testing.Control over maintenance windows and alert noise:

**Coexistence of vSphere Configuration Profiles and vSphere Host Profiles:**

Starting with vCenter 9.1.2, when you enable vSphere Configuration Profiles on an existing cluster, any vSphere Host Profiles that are already attached to the cluster or to individual hosts in the cluster are not detached and you can continue using them. This behavior allows you to retain existing vSphere Host Profiles while you evaluate vSphere Configuration Profiles. For more information, see [Coexistence of vSphere Configuration Profiles and vSphere Host Profiles](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_098&appid=vsphere-9-1&language=&format=rendered).

**ESX Host Configuration Support by vSphere Configuration Profiles:**

Starting with vCenter 9.1.2, vSphere Configuration Profiles supports ESX host configuration, enabling declarative, cluster-wide management of ESX hosts by using JSON profiles. You start using vSphere Configuration Profiles by enabling the feature during cluster creation or by enabling vSphere Configuration Profiles on an existing cluster. You can switch from using vSphere Host Profiles to enabling and using vSphere Configuration Profiles at any time, but the change is irreversible. For information about how to enable vSphere Configuration Profiles during cluster creation and set a desired configuration for the cluster, see [Enable vSphere Configuration Profiles During Cluster Creation](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_125&appid=vsphere-9-1&language=&format=rendered) and [Enable vSphere Configuration Profiles on an Existing Cluster](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_126&appid=vsphere-9-1&language=&format=rendered).

## Build Details

**VMware vCenter 9.1.2**

**Download Filename:**

VMware-vCenter-Server-Appliance-9.1.2.0.25946533-patch-FP.iso

**Build:**

25946533

**Download Size:**

7545 MB

**SHA256 checksum:**

7d86b2233fb0d096587dd4014312476a55c26619c3191388ad8a59010abb876a

**CVEs**

CVE-2026-123906, CVE-2026-123907, CVE-2026-123908, CVE-2026-123909

## Applying the Patch

Log in to the [Broadcom Support Portal](https://support.broadcom.com/) to download this patch, depending on your entitlement.

For download instructions, see [Download Broadcom products and software](https://knowledge.broadcom.com/external/article?articleId=142814).

For more information on using the vCenter shells, see Broadcom knowledge base article [2100508](https://kb.vmware.com/s/article/2100508).

For information about deploying, converging, upgrading, or patching your environment to 9.1.2, see [Getting to 9.1.2](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes.html#getting-to-vcf-9.1.2).

For VCF environments, you apply this patch by using VCF Operations. See [Upgrade or Patch an Individual VCF Component](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_535&appid=vcf-9-1&language=&format=rendered).

For VMware vSphere Foundation environments, see [Upgrading the vCenter Appliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vsphclient_110&appid=vsphere-9-1&language=&format=rendered).

## Resolved Issues

## vCenter Appliance and vSphere Client Issues

**Compliance checks or remediation against a vSphere Lifecycle Manager desired image might fail due to excessive metadata**

During scans, remediations, or updates, vCenter sends excessive metadata to ESX hosts while processing depots that contain base images, add-ons, components, and manifests. As a result, such metadata might overload the memory pool of an ESX host and lead to scan and remediation failures. In the vSphere Client, you might see errors such as:

Host status is unknown An internal error occurred while staging/remediating host SHA-1 signature found in host certificate False. Support for certificates with weak signature algorithm SHA-1 has been removed in ESXi 8.0. To proceed with upgrade, replace it with a SHA-2 signature based certificate.

The ESX host encounters memory exhaustion within the host/vim/vmvisor/settingsd-task-forks resource group, as described in Broadcom knowledge base article [449182](https://knowledge.broadcom.com/external/article/449182). The default memory limit is insufficient for the vSphere Lifecycle Manager daemon to parse the metadata zip files provided by the vCenter Server during the upgrade/remediation process. The /var/run/log/lifecycle.log file on the ESX host, you see an error such as Current ESXi version does not provide a mechanism to mount a tardisk into a ramdisk.

**ESX Live Install might fail if the desired image has no Live Patch VIB in it**

If you use the option Live Install Allowed on individual VIBs and the desired image has no Live Patch VIB in it, in the vSphere Client you might see errors such as:

Live Patch cannot be performed together with solution(s) com.vmware.nsxt that will be enabled or disabled live.

Disable the 'Enforce Live Patch' remediation option and retry the operation without using Live Patch. Alternatively, disable the remediation option, modify the image to remediate these solution(s) first, then re-enable the option and retry Live Patch.

This issue occurs if the vCenter instance is of version 9.0 and later, and the ESX version is 8.x.

**Everyone can see SMTP credentials in the vSphere Client and OptionManager API**

When you use Enterprise SMTP Integration and set the relevant credentials by using Advanced Settings in the vSphere Client or the OptionManager API, the configuration component treats all values as globally accessible and any user with permissions to read the configuration can obtain those credentials by the same interfaces.

SMTP credential fields are now considered secret and display as (not shown). Updates to the field are saved internally, but subsequent reads still show the redaction text.

**Metadata of encrypted file-based backups does not include integrity protection**

In vCenter 9.1.2, file-based backup adds an HMAC to the metadata of each new encrypted backup. The HMAC key is derived from the backup password, so the HMAC cannot be recreated without the password. During restore, vCenter verifies the HMAC before any data is restored and stops the restore if the verification fails. This protection applies only to encrypted backups. The backup and restore workflow does not change.

**File-based backup and restore of vCenter instances with large databases take a long time**

In vCenter 9.1.2.0, file-based backup compresses backup files with Zstandard (zstd) instead of gzip. Zstandard compresses and decompresses data faster than gzip, which can reduce backup and restore time, especially for vCenter instances with large databases. In the names of backup files on the backup server, the .gz extension is replaced with .zst.bin. If you use scripts or tools that process backup files by name, you must update such scripts. The backup and restore workflow does not change.

**After breaking Enhanced Linked Mode (ELM), you still see stale or duplicate vCenter entries**

After you break ELM on a vCenter instance, in the vSphere Client you can still see stale or duplicate vCenter entries under the Lifecycle Manager or VMware Cloud Foundation Operations tabs. The vCenter drop-down menu might still lists vCenter instances that are no longer linked.

**In the vSphere Client, you see errors for insufficient resources of vCenter due to changed ID of DirectPath Profile (DPP) service**

When vCenter upgrades to version 9.1.x, the version ID of the DPP service might change and cause issues with the presentation of the usage and capacity of various passthrough devices and accelerators, such as GPUs. In the vSphere Client, you see an error such as Insufficient resources. The resources of the vSphere Zone are insufficient for the operation. In the vpxd logs, you see errors such as doesn't have sufficient DPPs to deploy resource profile slot.

**Zonal datastore compatibility calculation does not skip hosts in maintenance mode**

When deciding whether a datastore is eligible for zonal placement, Storage Policy Based Management (SPBM) checks every host in a cluster, including hosts that are in maintenance mode and cannot run any workloads. As a result, when a host is added to an existing cluster and is still in maintenance mode, creating a PersistentVolumeClaim (PVC) can fail or take much longer than expected, depending on the environment. Starting with VCF 9.1.2, hosts in maintenance mode are skipped during the zonal compatibility check, which speeds up the process.

**In the vSphere Client, you see outdated endpoint certificates for VASA 5 or later providers**

If a VASA 5 or later provider, which supports the VirtualHost capability, has the retainVasaProviderCertificate" flag set to True, in the Storage Providers screen in the vSphere Client you might see outdated endpoint certificates for the provider. This is a cosmetic issue and does not impact the VASA provider functionality.

**You might see unresponding virtual machines during vSphere Replication with the error: No connection to VR Server: Disk size mismatch**

A race condition between the checksum throttling mechanism and the full-sync cancellation logic within the vSphere Replication service might cause some virtual machines to become unresponsive. In the vSphere Client, the status of the replication job displays the error: No connection to VR Server: Disk size mismatch.

**After a vCenter upgrade, the SNMP agent is enabled by default** 

After a vCenter upgrade, the SNMP agent might be automatically enabled, even if it was not active before the upgrade.

**Virtual machine templates might fail to sync when vCenter instances are linked by using vCenter grouping in VCF Operations**

With VCF 9.1, you link vCenter instances in vCenter Groups under **Operate > Administration > Configurations > vCenter Linking** in VCF Operations, instead of using the vCenter Enhanced Linked Mode (ELM), which is deprecated. After you create a vCenter group, if you create a content library on one of the vCenter instances, add a VM template, and try to create a new subscription, the VM template sync might fail. In the vSphere Client, you might see either of the following errors:

A general system error occurred: Failed to publish library \<source library> to subscribed library \<target library> on vCenter Server XYZ. Reason: The operation failed due to Permission to perform this operation was denied.

Permission to perform this operation was denied: You do not hold privileges... VM template sync works if the vCenter instances are linked in ELM.

**In the vSphere Client, you see a License Inventory Monitoring alarm** 

After you assign an override license to an ESX hosts of version 8.x, the license usage calculation might incorrectly include the usage from the ESXi 8.x hosts to the license assigned to the managing vCenter instance. As a result, in the vSphere Client you see a **License Inventory Monitoring** alarm. The license calculation discrepancy affects only the API responsible for the vCenter alert. The overall core count displayed in the **Licenses** tab in the vSphere Client is correct and matches the license usage metrics in VCF Operations.

## Auto Deploy Issues

**ESX hosts provisioned with Auto Deploy might not automatically join the target vCenter instance due to invalid SSL certificate**

In some cases, such as when VMware Certificate Authority (VMCA) is configured as a subordinate CA under an external enterprise root, the certificate file of an ESX host might contain more than one certificate. As a result, when you run an Auto Deploy rule to provision such hosts, they boot successfully, but do not automatically join the target vCenter instance. You can manually add the hosts to the vCenter instance.

## Miscellaneous Issues

**Stale VAPI tasks might cause a memory leak in the licensing service**

Completed entitlement VAPI tasks that are not cleaned up might cause a memory leak that eventually leads to an out-of-memory condition in the licensing service. The memory leak is below 1 MB per day and the accumulation takes more than 90 days. As a result, in the VCF Operations UI, you see errors such as Licenses could not be synchronized with vCenters. and Licenses could not be assigned to vCenter. Another effect of the issue is that since requests of the licensing service start to fail, NSX cannot confirm a license and might switch to evaluation mode.

**You see virtual appliance components with placeholder "$name" when generating a vCenter support bundle** 

When generating a vCenter Server support bundle from the vCenter Appliance Management Interface (VAMI), the list of selectable components in the Virtual Appliance group shows two entries with the literal placeholder name $name instead of a real component name.

## vSphere High Availability Issues

**Virtual machine with attached Encrypted CNS volumes might fail to restart during vSphere High Availability failover**

In a vCenter environment using encrypted Cloud Native Storage (CNS) or First Class Disk (FCD) volumes, vSphere HA might fail to restart a Kubernetes or Supervisor-managed virtual machine after the ESX host running the VM becomes unavailable.

You might see the following symptoms:

- The ESX host fails or becomes unavailable.
- vSphere HA initiates failover for the affected VM.
- HA cannot find a compatible ESX host.
- The VM remains powered off, resulting in extended application downtime.
- The encrypted CNS/FCD volume encryption key is present only on the ESX host where the disk was originally attached.
- Other hosts in the HA/DRS cluster do not have the required encryption key.

## Backup and Restore Issues

**Encryption of file-based backup files does not include integrity protection**

In vCenter 9.1.2, file-based backup encrypts new backups with AES-256-GCM, which also protects each encrypted backup file against modification. If an encrypted backup file was modified or truncated, the restore fails. The encryption key is derived from the backup password with PBKDF2-HMAC-SHA256. Both algorithms are FIPS-approved. Unencrypted backups and the backup and restore workflow do not change, and no action is required.

**Metadata of encrypted file-based backups does not include integrity protection**

Starting with vCenter 9.1.2, file-based backup adds an Hash-based Message Authentication Code (HMAC) to the metadata of each new encrypted backup. The HMAC key is derived from the backup password, so the HMAC cannot be recreated without the password. During restore, vCenter verifies the HMAC before any data is restored and stops the restore if the verification fails. This protection applies only to encrypted backups. The backup and restore workflow does not change.

**File-based backup and restore transfers to external FTPS, HTTPS, or SFTP servers execute without authenticating the target server identity**

Starting with vCenter 9.1.2, file-based backup and restore can verify the identity of the backup server before any data is transferred.

- For FTPS and HTTPS, the identity is the server TLS certificate.
- For SFTP, it is the server SSH host key.
- You turn on verification for each backup, backup schedule, or restore with theVerify server identityoption. The option is in the vCenter Appliance Management Interface (VAMI) and in the restore wizard. In the API, use theverify\_server\_identityparameter. The option is selected by default for new backups, new backup schedules, and restores. Existing backup schedules keep their current behavior after an upgrade.

When verification is on:

- A certificate issued by a trusted certificate authority (CA) is accepted automatically.
- A self-signed or privately issued certificate, or an SFTP host key, must be accepted once.
- VAMI and the restore wizard show the certificate or host key so that you can compare it with the value from the server administrator before you accept it.

If the server later presents a different certificate or host key, the backup or restore fails until you accept the new identity. Accepted server identities are kept across restore, upgrade, and vCenter HA failover. The VAMI backup page shows whether the backup server identity for the schedule is verified. If verification is off, transfers run without verification, as in earlier releases.

## Known Issues

## vCenter Appliance and vSphere Client Issues

**In the vSphere Client, you see an error that your sign-in request has expired or has already been used**

Due to security improvements, the vCenter sign-in must be completed with an allocated sign-in request window. A sign-in request is single-use and expires after 5 minutes. Any attempt to sign-in after this window results in a HTTP 403 response and an error in the vSphere Client such as Your sign-in request has expired or has already been used. Please close this window and sign in again.

Workaround: Restart the sign-in process in the same browser tab.

**vCenter Single Sign-On log in to the vSphere Client might fail if you click Login multiple times in a rapid succession**

In environments with high-latency or slow networks, vCenter Single Sign-On log in to the vSphere Client might take a while and repeated clicks on the Login button might trigger duplicate concurrent SAML authentication requests before the initial request finishes processing. As a result, after entering valid credentials and clicking Login, the browser navigates to https://\<vcenter-fqdn>/ui/saml/websso and not to the https://\<vcenter-fqdn>/ui/.

Workaround: If you face the issue, do not use the Refresh or Reload button in the browser you use as this re-submits the corrupted SAML session data. Manually navigate directly to https://\<vcenter-fqdn>/ui/ in your browser address bar or open it in a new tab to start a fresh session.
