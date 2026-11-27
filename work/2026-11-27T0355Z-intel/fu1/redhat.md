---
title: CVE-2026-99362
url: https://access.redhat.com/security/cve/cve-2026-99362
hostname: redhat.com
description: CVE Details App
sitename: access.redhat.com
date: "2026-11-19"
fingerprint: b53af505cc128ae7
language: en
filedate: "2026-11-27"
---
# CVE-2026-99362

## Description

A flaw was found in the Linux kernel's Network File System daemon (nfsd). A remote client can trigger an out-of-bounds memory write by negotiating a minimal cached reply size and sending crafted compound requests containing SEQUENCE operations. This issue occurs because the server fails to verify that the response fits within negotiated buffer limits before caching it, causing response data to be written past the end of the allocated buffer. An attacker could exploit this vulnerability to cause memory corruption and a system crash, resulting in a denial of service (DoS), or potentially execute arbitrary code.

## Statement

Critical severity is assigned because an unauthenticated network-adjacent or remote attacker can trigger kernel heap corruption, potentially achieving remote code execution or causing a kernel panic that leads to complete denial of service. Default Red Hat Enterprise Linux configurations do not run or enable the in-kernel NFS server daemon (nfsd), limiting the attack surface to systems specifically configured to export NFSv4.1 or NFSv4.2 shares. Deployments that do not operate as an NFS server are not exposed to this flaw.

## Mitigation

Disable the NFS server service if NFS sharing is not required on the system, or restrict network access to port 2049 to trusted networks.

If the NFS server is not required, stop and disable the service:

bash

systemctl stop nfs-server

systemctl disable nfs-server

If the NFS server must remain operational, restrict access to trusted hosts using firewalld:

bash

firewall-cmd --permanent --remove-service=nfs

firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="\<trusted\_ip\_or\_subnet>" service name="nfs" accept'

firewall-cmd --reload

Caveats:

Disabling \`nfs-server\` prevents the host from sharing files over the network. Restricting access via firewalld blocks any client outside the designated IP address or subnet from mounting or interacting with NFS exports.

Warning:

Stopping \`nfs-server\` terminates active NFS sessions and interrupts active client operations. Executing \`firewall-cmd --reload\` activates firewall changes immediately, which will sever connections from clients not explicitly permitted.

## Common Vulnerability Scoring System (CVSS) Score Details

#### Info alert:Important note

CVSS scores for open source components depend on vendor-specific factors (e.g. version or build chain). Therefore, Red Hat's score and impact rating can be different from NVD and other vendors. Red Hat remains the authoritative [CVE Naming Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs) source for its products and services (see [Red Hat classifications](https://access.redhat.com/security/updates/classification#cvss)).

### CVSS v3 Score Breakdown

|  | Red Hat | NVD | cve.org | 
|---|---|---|---|
| Base Score | 9.4 | N/A | 9.8 | 
| Attack Vector | Network | N/A | Network | 
| Attack Complexity | Low | N/A | Low | 
| Privileges Required | None | N/A | None | 
| User Interaction | None | N/A | None | 
| Scope | Unchanged | N/A | Unchanged | 
| Confidentiality | High | N/A | High | 
| Integrity Impact | Low | N/A | High | 
| Availability Impact | High | N/A | High | 

### Vector

Red Hat: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H

cve.org: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

## Understanding the Weakness (CWE)

### Integrity

Technical Impact: Modify Memory; Execute Unauthorized Code or Commands

Write operations could cause memory corruption. In some cases, an adversary can modify control data such as return addresses in order to execute unexpected code.

### Availability

Technical Impact: DoS: Crash, Exit, or Restart

Attempting to access out-of-range, invalid, or unauthorized memory could cause the product to crash.

### Other

Technical Impact: Unexpected State

Subsequent write operations can produce undefined or unexpected results.

## Frequently Asked Questions

Not sure what something means? Check out our [Security Glossary](https://access.redhat.com/security/glossary).

Want to get errata notifications? [Sign up here](https://www.redhat.com/wapps/ugc/protected/notif.html?extIdCarryOver=true&sc_cid=701f2000001Css5AAC).
