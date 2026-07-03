---
schema: 1
kind: vulnerability
horizon: operational
title: "June 2026 Patch Tuesday: four CVSS ≥ 9.1 criticals — Windows kernel TCP/IP RCE, Nuance PowerScribe, Azure Stack Edge, Exchange Online"
headline: "June 2026 Patch Tuesday: four CVSS ≥ 9.1 criticals — Windows kernel TCP/IP RCE, Nuance PowerScribe, Azure Stack Edge, Exchange Online"
summary: "June 2026 Patch Tuesday carries four CVSS ≥ 9.1 criticals, led by CVE-2026-45657 — an unauthenticated use-after-free RCE in the Windows kernel TCP/IP path reachable by crafted network traffic (Microsoft MSRC, 2026-06-09)."
discovered_at: "2026-06-12T05:00:05Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - rce
  - info-disclosure
  - patch-available
regions:
  - global
sectors:
  - public-sector
  - healthcare
entities: []
cves:
  - id: CVE-2026-45657
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-26142
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-47643
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
  - id: CVE-2026-48579
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
sources:
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45657"
    publisher: Microsoft MSRC CVE-2026-45657
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26142"
    publisher: Microsoft MSRC CVE-2026-26142
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-47643"
    publisher: Microsoft MSRC CVE-2026-47643
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-48579"
    publisher: Microsoft MSRC CVE-2026-48579
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0185"
    publisher: NCSC-NL NCSC-2026-0185
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0189"
    publisher: NCSC-NL NCSC-2026-0189
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Prioritise CVE-2026-45657 in the June Windows rollout.** Unauthenticated network-reachable kernel TCP/IP RCE to SYSTEM — patch internet-exposed and untrusted-network-facing Windows hosts first; the other June criticals (Nuance PowerScribe, Azure Stack Edge) follow by exposure."
migrated_from: briefs/2026-06-12.md
---

Microsoft's June cumulative update (9 June) carries four criticals that clear the CVSS 9+ bar. **CVE-2026-45657 (CVSS 9.8)** is the priority: a use-after-free with a heap-overflow component in the Windows kernel's TCP/IP processing path, reachable by "specially crafted network traffic" with no authentication and no user interaction, yielding SYSTEM-level code execution ([Microsoft MSRC, 2026-06-09](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45657)). Microsoft rates exploitation "Less Likely" and reports no in-the-wild activity, but the unauthenticated network-reachable kernel surface makes this the June cycle's patch-first item for any Windows host exposed to untrusted networks. **CVE-2026-26142 (CVSS 9.8)** is an unauthenticated deserialization-of-untrusted-data RCE (CWE-502) in Nuance PowerScribe, the radiology reporting platform common in hospital imaging departments — clinical networks integrating PowerScribe with PACS/RIS should patch and restrict the service to clinical subnets ([Microsoft MSRC, 2026-06-09](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26142)). **CVE-2026-47643 (CVSS 9.8)** lets an unauthenticated attacker control the file name/path in an Azure Stack Edge upload endpoint (CWE-73), writing outside the intended directory through to code execution on the hybrid-cloud appliance ([Microsoft MSRC, 2026-06-09](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-47643)). **CVE-2026-48579 (CVSS 9.1)**, an improper-authorisation information-disclosure flaw in Exchange Online, is already fixed service-side with no customer action required — tenants wanting assurance can review the Unified Audit Log for anomalous mailbox-access operations predating 4 June ([Microsoft MSRC, 2026-06-04](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-48579)). NCSC-NL groups these in its June Patch Tuesday advisories ([NCSC-NL, 2026-06-11](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0185), [NCSC-NL 0189](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0189)).
