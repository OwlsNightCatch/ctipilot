---
schema: 1
kind: vulnerability
horizon: operational
title: "VMSA-2026-0006 — VMware vCenter: unauthenticated Directory Service auth bypass and Syslog traversal RCE (both CVSS 9.8), plus a VMXNET3 guest-to-host escape"
headline: "Broadcom patches two pre-auth CVSS 9.8 flaws in vCenter and a VM escape in the VMXNET3 adapter — no workaround exists for any of the five"
summary: >
  Broadcom's VMSA-2026-0006 (2026-07-29) fixes five flaws across VMware ESX, vCenter, Workstation and
  Fusion, and NCSC-CH, NCSC-NL and BSI CERT-Bund all carried it across 2026-07-28 and 2026-07-29. CVE-2026-59309 (CVSS 9.8)
  is an authentication bypass in vCenter's Directory Service reachable with nothing but network access to
  vCenter, and CVE-2026-59310 (CVSS 9.8) is a directory traversal in vCenter's Syslog server that reaches
  arbitrary code execution. CVE-2026-47876 (CVSS 9.3) is an out-of-bounds write in the VMXNET3 virtual
  network adapter that lets a guest administrator execute code on the ESX host, affecting only VMs using
  that adapter. No workaround exists for any of the five, so patching is the only control; none is reported
  exploited, and all were reported privately to Broadcom, one of them through Pwn2Own.
discovered_at: "2026-07-30T04:54:00Z"
event_date: "2026-07-29"
run_id: 2026-07-30T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, rce, path-traversal, patch-available]
regions: [global]
sectors: [public-sector, energy, healthcare, finance, telco]
entities: []
techniques: [T1190, T1611]
affected_products: ["VMware vCenter Server", "VMware ESX", "VMware Workstation", "VMware Fusion", "VMware Cloud Foundation", "VMware vSphere Foundation", "VMware Telco Cloud Platform", "VMware Telco Cloud Infrastructure"]
cves:
  - id: CVE-2026-59309
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "vCenter component of VMware Cloud Foundation and vSphere Foundation 9.1.x.x and 9.0.x.x, standalone VMware vCenter Server 8.0, and the vCenter component of VMware Cloud Foundation 5.x."
    fixed: "vCenter 9.1.0.0300, vCenter 9.0.2.0100, and vCenter Server 8.0 U3k; Cloud Foundation 5.x takes an async patch to 8.0 U3k."
  - id: CVE-2026-59310
    cvss: "9.8"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Same vCenter product and version spread as CVE-2026-59309."
    fixed: "Same as CVE-2026-59309: vCenter 9.1.0.0300, 9.0.2.0100, 8.0 U3k, and an async patch to 8.0 U3k for Cloud Foundation 5.x."
  - id: CVE-2026-47876
    cvss: "9.3"
    epss: null
    type: memory-corruption
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "ESX component where a guest VM is configured with a VMXNET3 virtual network adapter; VMs using other adapter types are not affected."
    fixed: "ESXi-9.1.0.0200, ESXi-9.0.2.0100 and ESXi80U3k."
  - id: CVE-2026-41703
    cvss: "7.6"
    epss: null
    type: info-disclosure
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "ESX, Workstation and Fusion. Broadcom publishes two different scores for this CVE by product — 7.6 on ESX, where a denial of service of the host process is the more likely outcome, and 2.7 on Workstation and Fusion, where the advisory restricts the impact to information disclosure."
    fixed: "ESXi-9.1.0.0, ESXi-9.0.2.0100 and ESXi80U3i; VMware Cloud Foundation 5.x ESX takes 5.2.3; Workstation and Fusion both fix in 26H1."
  - id: CVE-2026-41709
    cvss: "2.7"
    epss: null
    type: logic-flaw
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "ESX only — insufficient logging that lets an administrator perform actions without those actions being recorded."
    fixed: "ESXi-9.1.0.0, ESXi-9.0.2.0100, ESXi80U3j and 5.2.4."
sources:
  - url: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017"
    publisher: "Broadcom"
    date: "2026-07-29"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12814"
    publisher: "NCSC Switzerland"
    date: "2026-07-29"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0269"
    publisher: "NCSC-NL"
    date: "2026-07-29"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2569"
    publisher: "BSI CERT-Bund"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system."
    publisher: "Broadcom"
  - quote: "A malicious actor with local administrative privileges on a virtual machine with VMXNET3 virtual network adapter may exploit this issue to execute code on the host. Non VMXNET3 virtual adapters are not affected by this issue."
    publisher: "Broadcom"
  - quote: "Multiple vulnerabilities in VMware ESX, vCenter, Workstation, and Fusion were privately reported to Broadcom. Updates are available to remediate these vulnerabilities in affected Broadcom products."
    publisher: "Broadcom"
verification: multi-source
sourcing_note: >
  Every version and score in this entry is transcribed from the response-matrix tables in Broadcom's own
  advisory rather than from its prose summary or from any national-CERT restatement. Broadcom publishes two
  distinct scores for CVE-2026-41703 depending on product, and both are recorded here rather than reduced
  to one. Full-text search of the advisory found no reference to exploitation or in-the-wild activity, and
  none of the three national CERTs reports any. Broadcom describes the reports only as private and names
  Pwn2Own for one of them; it does not describe a bug-bounty programme, and this entry does not either. The
  management-segmentation guidance is NCSC-NL's — NCSC-CH's advisory carries severity, affected products,
  vulnerability details and references without any segmentation recommendation.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Patch vCenter to 9.1.0.0300, 9.0.2.0100 or 8.0 U3k on its respective track — the two CVSS 9.8 flaws need only network reachability to vCenter and Broadcom lists no workaround for either, so there is no interim mitigation to fall back on while the change is scheduled."
  - "Inventory which guest VMs use the VMXNET3 adapter and patch the ESX hosts carrying them to ESXi-9.1.0.0200, ESXi-9.0.2.0100 or ESXi80U3k: the escape is reachable from guest administrative privilege, which makes any tenant-operated or lower-trust VM on a shared host a path to the hypervisor."
migrated_from: null
---

Broadcom published VMSA-2026-0006 on 2026-07-29, covering five vulnerabilities across VMware ESX, vCenter, Workstation and Fusion, and stating that they "were privately reported to Broadcom" with updates available to remediate them ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). Three national CERTs picked it up immediately: NCSC-CH on 2026-07-29 ([NCSC Switzerland, 2026-07-29](https://security-hub.ncsc.admin.ch/#/posts/12814)), NCSC-NL on 2026-07-29 ([NCSC-NL, 2026-07-29](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0269)), and BSI CERT-Bund, whose advisory is dated 2026-07-28 with a 2026-07-29 revision ([BSI CERT-Bund, 2026-07-29](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2569)).

Two of the five sit on vCenter and need no credentials. CVE-2026-59309 (CVSS 9.8) is an authentication bypass in the VMware Directory Service, and Broadcom's own attack-vector text is unambiguous about the prerequisite: "a malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system" ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). CVE-2026-59310, also CVSS 9.8, is a directory-traversal flaw in vCenter's Syslog server that reaches arbitrary code execution through manipulated file and directory paths ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). vCenter is the control plane for an entire virtual estate: an unauthenticated path into it is a path to every workload it manages, which is why an anonymous network-reachable bypass warrants out-of-cycle handling even with no exploitation reported.

The third flaw crosses the isolation boundary in the other direction. CVE-2026-47876 (CVSS 9.3) is an out-of-bounds write in the VMXNET3 virtual network adapter, and Broadcom scopes it precisely: "a malicious actor with local administrative privileges on a virtual machine with VMXNET3 virtual network adapter may exploit this issue to execute code on the host. Non VMXNET3 virtual adapters are not affected by this issue" ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). That precondition is the useful part of the triage: exposure is determined by adapter configuration rather than by ESX version alone, so the inventory question is which guests run VMXNET3 and how much you trust whoever administers them.

Two lower-severity issues complete the advisory. CVE-2026-41703 is an out-of-bounds read that Broadcom scores differently by product — 7.6 on ESX, where it says a denial of service of the host process is the more likely outcome than information disclosure, against 2.7 on Workstation and Fusion, where it restricts the impact to information disclosure ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). CVE-2026-41709 is insufficient logging on ESX that allows an administrator to act without the action being recorded ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)) — minor as a vulnerability, but worth noting for anyone who treats ESX audit logs as a complete record during an investigation.

Two product families beyond the obvious ones are in scope and are easy to miss on a first read of the advisory: Broadcom lists VMware Telco Cloud Platform and VMware Telco Cloud Infrastructure as impacted, with their own knowledge-base fix path rather than the vCenter and ESXi build numbers below ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). Any telco operator running those stacks needs to follow that path rather than assuming the vSphere builds cover them.

Fixed builds differ per flaw and per track. vCenter takes 9.1.0.0300, 9.0.2.0100 or 8.0 U3k, with Cloud Foundation 5.x served by an async patch to 8.0 U3k; the VMXNET3 escape is fixed in ESXi-9.1.0.0200, ESXi-9.0.2.0100 and ESXi80U3k ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)). Broadcom records no workaround for any of the five, which removes the usual option of mitigating while the maintenance window is arranged.

Nothing here is reported exploited. Broadcom states the vulnerabilities "were privately reported to Broadcom" and credits Atredis Partners, Nguyen Hoang Thach of STARLabs SG working with Pwn2Own held by the Zero Day Initiative, an independent researcher, and CrowdStrike ([Broadcom, 2026-07-29](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)), and none of the three national CERTs reports in-the-wild activity. What earns this out-of-cycle attention is the reachability profile rather than an exploitation signal: two anonymous network paths into a virtualization control plane, with no interim control available.

Detection on the vCenter side means watching the two named services rather than the appliance generally: authentication events from the Directory Service, where a successful bind that no operator session accounts for is the signal, and Syslog-server request logging, where path-traversal sequences in a requested file or directory path have no legitimate counterpart. For the guest-to-host escape the telemetry is host-side — hypervisor crash and process-fault records on ESX hosts running VMXNET3 guests, since a failed escape attempt is far more likely to surface as an anomalous fault than as a clean compromise. On hardening, NCSC-NL is the source that spells out the architectural control: access to ESX and vCenter should be made available only from a separated management environment and not reachable directly from the internet or external networks ([NCSC-NL, 2026-07-29](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0269)). Broadcom's own advisory offers no hardening section and records "Workarounds: None" against every one of the five.
