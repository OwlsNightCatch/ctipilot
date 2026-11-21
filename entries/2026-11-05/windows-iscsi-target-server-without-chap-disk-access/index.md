---
schema: 1
kind: research
title: "SpecterOps: a Windows iSCSI Target Server set up without CHAP lets any host that knows the target and an authorised initiator name read the shared disks below file permissions, a Hyper-V domain controller's among them"
headline: "SpecterOps: iSCSI Target Server without CHAP lets a host that knows the target and initiator names read shared disks"
summary: >
  SpecterOps (2026-11-04) shows that a Windows iSCSI Target Server configured as a common cluster guide describes, with the optional CHAP step
  skipped, accepts a login from any host that knows the target host, the target name and an authorised initiator name, and the post says the host
  and the names can be found. The attacker then reads the shared disk below file-system permissions; where it holds a Hyper-V domain controller's
  virtual disk, the directory database and local credential stores are exposed. CHAP, network segmentation and volume encryption are the levers.
discovered_at: "2026-11-05T03:56:30Z"
updated_at: null
event_date: "2026-11-04"
run_id: 2026-11-05T0255Z-intel
priority: notable
immediate_action: null
tags: [identity]
regions: [global]
sectors: []
entities: ["product:microsoft-hyper-v", "product:microsoft-iscsi-target-server"]
techniques: [T1018, T1003.002, T1003.003, T1003.004]
affected_products: ["Microsoft iSCSI Target Server"]
cves: []
sources:
  - url: "https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/"
    publisher: "SpecterOps"
    date: "2026-11-04"
    role: primary
  - url: "https://www.pentestpartners.com/security-blog/an-interesting-route-to-domain-admin-iscsi/"
    publisher: "Pen Test Partners"
    date: "2016-05-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Without CHAP authentication configured, all that’s required to “login” is to know what host has the iSCSI target service installed along with its iSCSI target IQN and its client initiator IQNs."
    publisher: "SpecterOps"
    source_url: "https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/"
  - quote: "Arguably the most effective thing you can do is have proper network segmentation and host-based firewall configurations to isolate the drive"
    publisher: "SpecterOps"
    source_url: "https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/"
verification: single-source
sourcing_note: >
  SpecterOps is the only source for the research; Pen Test Partners' 2016 post describes the same weakness class and is cited only for the port
  and for the segmentation advice. The post names no Microsoft report, response or fix and names no telemetry; the detection concept below is
  derived from the mechanism the post describes, and the author says the technique has not been tested in production.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "List the computers in Active Directory that carry the service principal name the iSCSI Target Server registers and every host that listens on TCP 3260, then enable CHAP on each target and restrict TCP 3260 to the addresses of the cluster nodes, starting with targets whose volumes hold Hyper-V disks of domain controllers."
updates: []
migrated_from: null
---

SpecterOps shows that the Windows iSCSI Target Server role, set up as a community cluster guide describes it with the optional CHAP step skipped, accepts a login from any host that knows the target host, the target name and an authorised initiator name ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)). The post says the role registers a service principal name on its computer account, so a directory query lists the target hosts, that initiator names are built from the host's DNS name and are therefore predictable, and that in the author's experience the service has no rate limiting or brute-force protection ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)). Access is below the file system, so NTFS permissions do not apply, and volume encryption such as BitLocker defeats it ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)). The worst case the post shows is a volume that holds a Hyper-V domain controller's virtual disk, from which the local credential stores and the directory database can be taken ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)). The author has not tested the technique in production and warns that it can cause outages, and the post cites no Microsoft response.

**Exposure:** Windows Server hosts that run the iSCSI Target Server role without CHAP, found by the service principal name the role registers and by a listener on TCP 3260 ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/); [Pen Test Partners, 2016-05-18](https://www.pentestpartners.com/security-blog/an-interesting-route-to-domain-admin-iscsi/)). The author's own research puts the common uses with clustered resources such as Hyper-V, SQL Server and Exchange database availability groups, followed by third-party backup products ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)).

**Detection:** the post names no telemetry. What the mechanism implies, not stated by the post: iSCSI traffic to TCP 3260 on a target host from a source that is not one of its cluster nodes, and a login that presents a listed initiator name from another source address, because the access list keys on initiator names that an impersonator can present ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)).

**Defender takeaway:** enable CHAP on every iSCSI target, and isolate iSCSI traffic with segmentation and host-based firewalling, which the post calls arguably the most effective step; the post says IPsec mitigates network sniffing, and BitLocker or similar volume encryption makes the stolen disk unreadable ([SpecterOps, 2026-11-04](https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/)). Treat the disks of any domain controller that sat on an unprotected target as exposed.
