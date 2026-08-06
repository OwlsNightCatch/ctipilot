---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-63455 / CVE-2026-63456 — HPE Aruba Networking SD-WAN Orchestrator: spoofed HTTP headers bypass REST API authentication (CVSS 9.8), with the vendor and CERT-FR scoping the affected branches differently"
headline: "Another SD-WAN orchestration management plane takes an unauthenticated authentication bypass"
summary: >
  HPE Aruba Networking advisory HPESBNW05100 (2026-08-04, carried by CERT-FR on 2026-08-05) fixes two
  vulnerabilities in the REST API interface of SD-WAN Orchestrator, both CVSS v3.1 9.8, in which spoofed HTTP
  headers let an unauthenticated remote attacker bypass web authentication and view or modify sensitive system
  information. HPE scopes the exposure to the 9.6.x branch only — 9.6.2.x builds up to 9.6.2.40208 and 9.6.3.x
  builds up to 9.6.3.40137 — while CERT-FR's advisory on the same CVEs additionally lists 9.7.0.x builds below
  9.7.0.43264 as affected; the fixes are 9.6.2.40210, 9.6.3.40140 or 9.7.0.43264 either way. HPE Aruba says it is
  not aware of public discussion or exploit code, and its interim guidance is to keep the management interfaces off
  any general-purpose network.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-08-04"
run_id: 2026-08-06T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: [telco, public-sector]
entities: []
techniques: [T1190]
affected_products: ["HPE Aruba Networking SD-WAN Orchestrator"]
cves:
  - id: CVE-2026-63455
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Per HPE: SD-WAN Orchestrator 9.6.2.x builds 9.6.2.40208 and below and 9.6.3.x builds 9.6.3.40137 and below, with no branches outside 9.6.x.x affected. CERT-FR additionally lists 9.7.0.x builds below 9.7.0.43264 as affected — see sourcing_note."
    fixed: "9.6.2.40210 and above, 9.6.3.40140 and above, or 9.7.0.43264 and above"
  - id: CVE-2026-63456
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Per HPE: SD-WAN Orchestrator 9.6.2.x builds 9.6.2.40208 and below and 9.6.3.x builds 9.6.3.40137 and below, with no branches outside 9.6.x.x affected. CERT-FR additionally lists 9.7.0.x builds below 9.7.0.43264 as affected — see sourcing_note."
    fixed: "9.6.2.40210 and above, 9.6.3.40140 and above, or 9.7.0.43264 and above"
sources:
  - url: "https://csaf.arubanetworking.hpe.com/2026/hpe_aruba_networking_-_hpesbnw05100.txt"
    publisher: "HPE Aruba Networking PSIRT"
    date: "2026-08-04"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0969/"
    publisher: "CERT-FR"
    date: "2026-08-05"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  HPE Aruba Networking is the CNA and sole assessor; CERT-FR restates the advisory for its constituency rather than
  assessing the flaws independently, which is why credibility is rated 2 rather than 1. The two do not agree on
  scope: HPE states that no branches outside 9.6.x.x are affected, while CERT-FR's systems-affected list adds
  9.7.0.x builds below 9.7.0.43264. Both are recorded here rather than silently resolved. The vendor is
  authoritative for its own product, but an operator on a 9.7.0.4xxxx build below 9.7.0.43264 should note that its
  national CERT scopes them in, and the upgrade target is the same either way. Both CVEs share a single
  advisory entry with one description and one CVSS vector, so the vendor does not distinguish the two flaws
  individually and this entry does not invent a distinction.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Move any SD-WAN Orchestrator below 9.6.2.40210, 9.6.3.40140 or 9.7.0.43264 to one of those builds — and include 9.7.0.x instances below 9.7.0.43264 in that sweep even though HPE's advisory scopes them out, because CERT-FR's advisory on the same CVEs scopes them in and the upgrade target is identical; if the change window is further out, apply HPE Aruba's own interim control and confine the Orchestrator CLI and web management interfaces to a dedicated VLAN or firewall policy."
migrated_from: null
---

HPE Aruba Networking published HPESBNW05100 on 2026-08-04 for two vulnerabilities in the REST API interface of its SD-WAN Orchestrator, describing them as authentication bypass via spoofed HTTP headers that could allow an unauthenticated remote attacker to bypass web authentication mechanisms and access system functions, with successful exploitation permitting an attacker to view and modify potentially sensitive information on the target system ([HPE Aruba Networking, 2026-08-04](https://csaf.arubanetworking.hpe.com/2026/hpe_aruba_networking_-_hpesbnw05100.txt)). Both carry CVSS v3.1 9.8 on the vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, and the vendor scopes the exposure tightly: only the 9.6.x software branch is affected, specifically 9.6.2.x builds at 9.6.2.40208 and below and 9.6.3.x builds at 9.6.3.40137 and below, with no branches outside 9.6.x.x affected at all ([HPE Aruba Networking, 2026-08-04](https://csaf.arubanetworking.hpe.com/2026/hpe_aruba_networking_-_hpesbnw05100.txt)). Both were reported through HPE Aruba's bug-bounty programme, and the vendor states it is not aware of any public discussion or exploit code targeting them as of the advisory's release ([HPE Aruba Networking, 2026-08-04](https://csaf.arubanetworking.hpe.com/2026/hpe_aruba_networking_-_hpesbnw05100.txt)). CERT-FR carried the advisory to its constituency the next day, but scopes it wider: its systems-affected list adds EdgeConnect SD-WAN Orchestrator 9.7.0.x builds below 9.7.0.43264 alongside the two 9.6.x branches ([CERT-FR, 2026-08-05](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0969/)). The vendor is authoritative for its own product and the recommended upgrade target is unchanged either way, but an operator sitting on a 9.7.0 build below 9.7.0.43264 should know that one of the two advisories covering these CVEs places them inside the affected set.

The reason this is worth acting on ahead of the routine cycle is not the score but the class and the company it keeps. An SD-WAN Orchestrator is the control plane for an organisation's wide-area network — the system that pushes policy and configuration to every branch appliance — so authentication bypass on its API is reach into the network fabric rather than into one host. This lands in the same short window in which a directly comparable product, Arista's on-premises VeloCloud Orchestrator, was confirmed exploited through an unauthenticated command injection on an interface exposed by default (covered here on 2026-07-28). Nothing in the HPE Aruba advisory connects the two, and this entry does not: the point is that attacker attention is demonstrably on this product class right now, which is an argument for treating the exposure question as urgent even while exploitation of these particular CVEs remains unreported.

**Defender takeaway:** HPE Aruba's own recommended workaround is the tell about where the risk actually sits — it advises restricting the CLI and web-based management interfaces to a dedicated Layer 2 segment or VLAN and controlling them with Layer 3 firewall policy ([HPE Aruba Networking, 2026-08-04](https://csaf.arubanetworking.hpe.com/2026/hpe_aruba_networking_-_hpesbnw05100.txt)). If that is not already true of your Orchestrator, the network position is the finding, independent of these two CVEs. Because the bypass works by spoofing HTTP headers on the REST API rather than by crashing or corrupting anything, exploitation looks like ordinary successful API traffic: the detection opportunity is in the Orchestrator's own access and audit logs — API calls that perform privileged reads or configuration changes without a corresponding authenticated session, and administrative actions arriving from source addresses outside the management segment.
