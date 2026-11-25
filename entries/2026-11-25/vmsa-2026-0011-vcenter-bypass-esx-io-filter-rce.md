---
schema: 1
kind: vulnerability
title: "VMSA-2026-0011, VMware vCenter and ESX: a second Directory Service authentication bypass in vCenter (CVE-2026-123903) and two I/O filter service flaws in ESX that give code execution from network access (CVE-2026-123910, CVE-2026-123911), all CVSS 3.1 9.8; no workaround for vCenter, fixed in vCenter 9.1.2, 9.0.2.0300 and 8.0 U3m, no exploitation reported"
headline: "Broadcom VMSA-2026-0011: second vCenter auth bypass and ESX I/O filter RCE, all 9.8; the earlier fix does not cover 9.x"
summary: >
  Broadcom's VMSA-2026-0011 of 2026-11-24 fixes 23 flaws, among them CVE-2026-123903, a second authentication bypass in vCenter's Directory Service that needs only network access (CVSS 3.1 9.8, no workaround), and CVE-2026-123910 and CVE-2026-123911, I/O filter service flaws in ESX that give code execution from network access (9.8 each). vCenter 9.1.2, 9.0.2.0300 and 8.0 U3m fix the vCenter flaw, so a 9.x vCenter already on the build that fixed the exploited CVE-2026-123890 (9.1.1.0200 or 9.0.2.0200) is still affected; no source reports exploitation of these 23 flaws.
discovered_at: "2026-11-25T04:41:00Z"
updated_at: null
event_date: "2026-11-24"
run_id: 2026-11-25T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, rce, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: [product:vmware-vcenter-server, product:vmware-esxi, product:vmware-workstation, product:vmware-fusion, product:vmware-cloud-foundation]
techniques: [T1190, T1611]
affected_products: ["VMware vCenter Server", "VMware ESX", "VMware Workstation", "VMware Fusion", "VMware Cloud Foundation"]
cves:
  - id: CVE-2026-123903
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "vCenter 9.1.x before 9.1.2, 9.0.x before 9.0.2.0300, 8.0 before 8.0 U3m, 7.0, VCF 5.x before 5.2.5"
    fixed: "9.1.2, 9.0.2.0300, 8.0 U3m, VCF 5.2.5 (KB88287); 7.0 has no public fix"
  - id: CVE-2026-123910
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ESX 9.1.x before ESXi-9.1.2.0-25946735, 9.0.x before ESXi-9.0.2.0200-25953133, 8.0 before ESXi80U3m-25926933, 7.0, VCF 5.x before 5.2.5"
    fixed: "ESXi-9.1.2.0-25946735, ESXi-9.0.2.0200-25953133, ESXi80U3m-25926933, VCF 5.2.5; 7.0 has no public fix"
  - id: CVE-2026-123911
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ESX 9.1.x before ESXi-9.1.2.0-25946735, 9.0.x before ESXi-9.0.2.0200-25953133, 8.0 before ESXi80U3m-25926933, 7.0, VCF 5.x before 5.2.5"
    fixed: "ESXi-9.1.2.0-25946735, ESXi-9.0.2.0200-25953133, ESXi80U3m-25926933, VCF 5.2.5; 7.0 has no public fix"
  - id: CVE-2026-123912
    cvss: "9.3"
    epss: null
    type: memory-corruption
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "Workstation 25H2, Fusion 25H2 and the ESX builds above"
    fixed: "Workstation and Fusion 26H1u1; ESX as above"
sources:
  - url: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626"
    publisher: "Broadcom"
    date: "2026-11-24"
    role: primary
  - url: "https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md"
    publisher: "Broadcom (VMSA-2026-0011 questions and answers)"
    date: "2026-11-24"
    role: corroborating
  - url: "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html"
    publisher: "Broadcom (vCenter 9.1.2.0 release notes)"
    date: "2026-11-24"
    role: corroborating
  - url: "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html"
    publisher: "Broadcom (vCenter 8.0 U3m release notes)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/vcenter/vcenter-9-0-2-0300-release-notes.html"
    publisher: "Broadcom (vCenter 9.0.2.0300 release notes)"
    date: "2026-11-24"
    role: corroborating
  - url: "https://knowledge.broadcom.com/external/article/463535/manual-interim-workaround-for-cve2026123.html"
    publisher: "Broadcom"
    date: "2026-11-24"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "Broadcom is the vendor and the only source; CVE records for these ids were not yet published on 2026-11-25, so scores, versions and prerequisites come from the advisory's response matrices. The advisory's release notes disagree with its matrices on which CVEs some builds resolve; the matrices and the questions and answers are the vendor's stated source of truth."
confidence: high
references:
  - 2026-11-20/vmware-vcenter-cve-2026-123890-auth-bypass-exploited-gtig
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update every ESX host to ESXi-9.1.2.0-25946735, ESXi-9.0.2.0200-25953133 or ESXi80U3m-25926933 and, on ESX 8.x hosts that must wait, restrict TCP 9080 on the host firewall to the vCenter Server address as KB463535 describes, because CVE-2026-123910 and CVE-2026-123911 give code execution from network access and the restriction resolves only a small portion of the advisory's issues."
updates: []
migrated_from: null
---

Broadcom's VMSA-2026-0011 of 2026-11-24 fixes 23 flaws across vCenter, ESX, Workstation, Fusion, VMware Tools and Avi Load Balancer, rated Critical, and Broadcom's questions and answers treat the critical issues as an emergency change ([Broadcom, 2026-11-24](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md)). CVE-2026-123903 is an authentication bypass in vCenter's VMware Directory Service, CVSS 3.1 9.8, reachable with network access to vCenter and no credentials, with no workaround; Broadcom calls it a new and distinct issue from the exploited CVE-2026-123890 in the same component ([Broadcom, 2026-11-24](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md); [Broadcom, 2026-11-24](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626)). CVE-2026-123910 (heap out-of-bounds write) and CVE-2026-123911 (use-after-free) are flaws in the ESX I/O filter service, each 9.8 with network access to the host, and CVE-2026-123912 is an out-of-bounds write in the XHCI USB controller that gives code execution as the VMX process to an administrator inside a virtual machine, CVSS 9.3 in Workstation and Fusion and 8.4 in ESX ([Broadcom, 2026-11-24](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626)).

Fixed builds: vCenter 9.1.2, 9.0.2.0300 and 8.0 U3m, VMware Cloud Foundation 5.x through 5.2.5 (KB88287), with no public fix for vCenter 7.0 or ESX 7.0; ESX ESXi-9.1.2.0-25946735, ESXi-9.0.2.0200-25953133 and ESXi80U3m-25926933; Workstation and Fusion 26H1u1 ([Broadcom, 2026-11-24](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626)). Broadcom says a vCenter on 8.0 U3m from the earlier advisory needs no further update but vCenter 9.1.x does, and for 9.0.x the fixed version in the new advisory (9.0.2.0300) governs, so 9.1.1.0200 and 9.0.2.0200 do not carry the fix ([Broadcom, 2026-11-24](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md)). For ESX 8.x only, KB463535 restricts TCP 9080, where the I/O filter service listens, to the vCenter address; Broadcom says limiting access to the service resolves only a small portion of the issues in the advisory and may affect cluster operation, and tells customers to apply the updates ([Broadcom, 2026-11-24](https://knowledge.broadcom.com/external/article/463535/manual-interim-workaround-for-cve2026123.html); [Broadcom, 2026-11-24](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md)). Broadcom's release notes disagree with its response matrices in places: the vCenter 9.1.2 notes list only four vCenter CVEs, not the authentication bypass that the matrix says 9.1.2 fixes ([Broadcom, 2026-11-24](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-2-0-release-notes/vcenter-9-1-2-0-release-notes.html)), the 8.0 U3m notes list only the earlier exploited flaw ([Broadcom, 2026-11-19](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3m-release-notes.html)) and the 9.0.2.0300 notes list ESX flaws ([Broadcom, 2026-11-24](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/patch-releases-9-0-0-x/vsphere/vcenter/vcenter-9-0-2-0300-release-notes.html)), and the questions and answers score CVE-2026-123912 at 8.5 for ESX where the response matrix prints 8.4, and Broadcom names the advisory as the source of truth for affected versions and patches ([Broadcom, 2026-11-24](https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0011/README.md)). Neither the advisory nor the questions and answers say any flaw is exploited, and no source reports it as of 2026-11-25.

**Exposure:** any vCenter Server reachable over the network, with the build shown in the appliance's version summary, and any ESX host whose I/O filter service port is reachable; on ESX 8.x that service listens on TCP 9080 and KB463535 says only vCenter should reach it.

**Detection:** Broadcom publishes no indicators. Flows to TCP 9080 on ESX hosts from any address other than the vCenter Server are outside the pattern KB463535 describes, and administrator sessions or account changes on a vCenter that was reachable before patching deserve the review described for the earlier Directory Service bypass.

**Defender takeaway:** treat it as the emergency change Broadcom describes: move vCenter and ESX to the builds above, re-patch any 9.x vCenter that stopped at the earlier advisory's build, and keep management interfaces and the ESX I/O filter port off untrusted networks until then; vCenter 7.0 and ESX 7.0 have no public fix and Broadcom directs extended-support customers to its support, so isolation is the interim lever there.
