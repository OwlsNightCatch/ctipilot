---
schema: 1
kind: vulnerability
title: "Abacus ERP: unauthenticated RCE (CVSS 9.8, no CVE) and authenticated path traversal in a widely-deployed Swiss ERP platform — flagged by NCSC-CH"
headline: "NCSC-CH flags an unauthenticated RCE (CVSS 9.8) in Abacus ERP — reachable endpoint is the only prerequisite"
summary: >
  Abacus Research AG shipped a hotfix on 2026-07-15 for an unauthenticated critical RCE (vendor-rated CVSS 9.8,
  no CVE assigned) in the server-side component of its proprietary client-server protocol, plus an authenticated
  path-traversal file-read flaw (CVSS 7.7) in the AbaClik / AbaClik.ai mobile-app APIs; NCSC-CH flagged both on
  2026-07-16. Abacus is one of the most widely-deployed ERP/accounting/HR platforms across Swiss SMEs,
  associations and public-sector-adjacent organizations. Every on-prem installation — including End-of-Life
  V2023 builds — is affected; WebPortal/cloud-hosted deployments are not. No in-the-wild exploitation is known
  (found via the vendor's bug-bounty program).
discovered_at: "2026-07-17T04:35:00Z"
event_date: "2026-07-15"
run_id: 2026-07-17T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, path-traversal, patch-available]
regions: [switzerland]
sectors: [public-sector, finance]
entities: []
techniques: [T1190]
affected_products: ["Abacus ERP", "Abacus AbaClik", "Abacus AbaClik.ai"]
cves: []
sources:
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12766"
    publisher: "NCSC Switzerland (Cyber Security Hub / GovCERT.ch)"
    date: "2026-07-16"
    role: primary
  - url: "https://security.abacus.ch/en/2026-84b5ca67-a46f-639c-5784-ce3c72065a34"
    publisher: "Abacus Research AG (vendor PSIRT)"
    date: "2026-07-15"
    role: primary
  - url: "https://security.abacus.ch/en/2026-8b29ce3e-c211-1f4d-9e50-a94d4d6659d1"
    publisher: "Abacus Research AG (vendor PSIRT)"
    date: "2026-07-15"
    role: primary
closed_sources: []
evidence:
  - quote: "If successfully exploited, the vulnerability allows remote code execution on the abacus server without user authentication."
    publisher: "Abacus Research AG"
  - quote: "Reachable Abacus Endpoints are the only prerequisite for an attack."
    publisher: "Abacus Research AG"
  - quote: "No, the vulnerability was found in our bugbounty program. We have no indications of a successful attack in the wild."
    publisher: "Abacus Research AG"
verification: multi-source
sourcing_note: "No CVE has been assigned by Abacus or MITRE — track by vendor advisory ID (Security Update 15.07.2026), not a CVE. Both CVSS figures (9.8 RCE / 7.7 path traversal) are vendor-rated and carried by NCSC-CH's relay; the vendor withholds deeper technical root-cause detail 'for security reasons.' Two independent Admiralty-A sources attest (vendor PSIRT for its own product; NCSC-CH as national relay)."
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
  - "Patch on-prem Abacus ERP to the fixed build (V2026 2026.201.17211 / V2025 2025.203.17044 / V2024 2024.204.16772) or apply the ServiceManager SilentHotfix — the SilentHotfix relies on a code-signing certificate known only to AbaClient ≥ 4.2, so on older clients the Abacus will fail to start until the client is updated or the hotfix reverted; EOL V2023-and-earlier has no fix and must be isolated or upgraded."
  - "Confirm the AbaClik / AbaClik.ai APIs are not reachable from untrusted networks — NCSC-CH notes they are exposed externally by default even for customers not using the mobile apps, which is the exposure the authenticated path-traversal file read abuses."
migrated_from: null
---

Abacus Research AG (Wittenbach, SG) patched two unrelated flaws on 2026-07-15 that NCSC-CH surfaced the following day ([NCSC-CH, 2026-07-16](https://security-hub.ncsc.admin.ch/#/posts/12766)). The critical one is an unauthenticated remote code execution in the server-side handler of the proprietary Abacus client-server communication protocol: "the vulnerability allows remote code execution on the abacus server without user authentication," and "reachable Abacus Endpoints are the only prerequisite for an attack" — no credentials, no user interaction ([Abacus Research AG, 2026-07-15](https://security.abacus.ch/en/2026-84b5ca67-a46f-639c-5784-ce3c72065a34)). The vendor states the flaw is not limited by license or option: every on-prem Abacus ERP installation is affected, and End-of-Life V2023-and-earlier builds remain vulnerable with no fix planned. The second flaw (CVSS 7.7) is a path traversal in two APIs tied to the AbaClik / AbaClik.ai mobile companion apps that lets an authenticated caller read a subset of server files outside the application's security realm; NCSC-CH's load-bearing point is that these APIs are network-exposed by default even for customers who do not use the mobile apps ([Abacus Research AG, 2026-07-15](https://security.abacus.ch/en/2026-8b29ce3e-c211-1f4d-9e50-a94d4d6659d1)).

Both were found through Abacus's own bug-bounty program and the vendor reports no indication of exploitation in the wild. Internet-facing on-prem deployments are the acute case; an internal-only Abacus still carries the flaw but with the attack surface reduced to the internal network. **Defender takeaway:** with no CVE, no public PoC and no vendor-published indicators of compromise ("At this moment we have no clear Indicator of Compromise for this vulnerability"), there is nothing to hunt on yet — the correct posture is to patch/hotfix immediately and shrink exposure, not to wait for detection content. Because the fix ships either as a full update or a ServiceManager SilentHotfix that itself depends on AbaClient ≥ 4.2, treat the client-version prerequisite as a change-management gate: a SilentHotfix pushed to a fleet on an older AbaClient will leave the Abacus unable to start until the client is upgraded or the hotfix reverted.
