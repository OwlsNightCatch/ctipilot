---
schema: 1
kind: vulnerability
horizon: operational
title: "Adobe August 2026 Patch Day: ColdFusion ships a CVSS 10.0 unauthenticated OS command injection, and Campaign Classic ships two more unauthenticated CVSS 10.0 flaws in the same release"
headline: "Adobe's August bulletins carry three separate unauthenticated, maximum-severity code-execution flaws across ColdFusion and Campaign Classic"
summary: >
  Adobe's 2026-08-11 Security Patch Day fixes 16 CVEs in ColdFusion 2025/2023 (APSB26-90), headed
  by CVE-2026-48362, an unauthenticated CVSS 10.0 OS command injection, and 3 CVEs in Campaign
  Classic on-premise (APSB26-123), two of them unauthenticated CVSS 10.0 authorization flaws
  (CVE-2026-71398, CVE-2026-27302). Adobe reports no known exploitation for either bulletin.
discovered_at: "2026-08-28T05:15:00Z"
updated_at: null
event_date: "2026-08-11"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available, auth-bypass]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1190]
affected_products: ["Adobe ColdFusion 2025", "Adobe ColdFusion 2023", "Adobe Campaign Classic"]
cves:
  - id: CVE-2026-48362
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 ≤2025.0.11; ColdFusion 2023 ≤2023.0.22"
    fixed: "ColdFusion 2025.0.12; ColdFusion 2023.0.23"
  - id: CVE-2026-48273
    cvss: "9.9"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "ColdFusion 2025 ≤2025.0.11; ColdFusion 2023 ≤2023.0.22"
    fixed: "ColdFusion 2025.0.12; ColdFusion 2023.0.23"
  - id: CVE-2026-71384
    cvss: "9.6"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "ColdFusion 2025 ≤2025.0.11; ColdFusion 2023 ≤2023.0.22"
    fixed: "ColdFusion 2025.0.12; ColdFusion 2023.0.23"
  - id: CVE-2026-71398
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic ACC v7 ≤7.4.3 build 9399 (on-premise and the on-premise leg of hybrid deployments only)"
    fixed: "ACC v7 7.4.4 build 9400"
  - id: CVE-2026-27302
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic ACC v7 ≤7.4.3 build 9399 (on-premise and the on-premise leg of hybrid deployments only)"
    fixed: "ACC v7 7.4.4 build 9400"
  - id: CVE-2026-48381
    cvss: "9.0"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Adobe Campaign Classic ACC v7 ≤7.4.3 build 9399 (on-premise and the on-premise leg of hybrid deployments only)"
    fixed: "ACC v7 7.4.4 build 9400"
sources:
  - url: "https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html"
    publisher: "Adobe (APSB26-90)"
    date: "2026-08-11"
    role: primary
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-123.html"
    publisher: "Adobe (APSB26-123)"
    date: "2026-08-11"
    role: primary
closed_sources: []
evidence:
  - quote: "Adobe has released a security update for ColdFusion versions 2025 and 2023. This update resolves critical and important vulnerabilities that could result in arbitrary code execution, privilege escalation, security feature bypass, application denial-of-service, and memory exposure."
    publisher: "Adobe (APSB26-90)"
  - quote: "Adobe is not aware of any exploits in the wild for any of the issues addressed in this update."
    publisher: "Adobe (APSB26-90)"
  - quote: "This security bulletin applies only to fully on-premise deployments of Adobe Campaign Classic and to the on-premise components of hybrid deployments. Adobe-hosted instances have already been remediated and require no customer action."
    publisher: "Adobe (APSB26-123)"
verification: single-source
sourcing_note: >
  Both bulletins are Adobe's own advisories for its own products (vendor-PSIRT primary), single-
  sourced with no independent researcher write-up yet published for either — reliability follows
  the vendor's own track record for its security bulletins, credibility stays at 2 pending
  independent corroboration. The CVE-to-CVSS-to-CWE table above is transcribed cell-by-cell from
  each bulletin's own raw table structure rather than a summarizer, after an earlier CVE-mapping
  defect in prior coverage was traced to positional pairing.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Patch internet-facing ColdFusion 2025/2023 instances to 2025.0.12 / 2023.0.23 now — CVE-2026-48362 is an unauthenticated OS command injection at CVSS 10.0, the class of flaw that gets weaponised within days of a patch diff being published, and Adobe reports no exploitation yet, which is the window to close before one exists."
  - "For any on-premise or hybrid Adobe Campaign Classic ACC v7 deployment, upgrade to 7.4.4 build 9400 now — two of the three fixed flaws (CVE-2026-71398, CVE-2026-27302) are unauthenticated CVSS 10.0 code-execution paths; Adobe-hosted instances are already remediated and need no action."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [sourcing_note]
migrated_from: null
---

Adobe's 2026-08-11 Security Patch Day carries two bulletins whose headline flaws are unauthenticated, no-interaction paths to arbitrary code execution at CVSS 10.0. APSB26-90 fixes 16 CVEs in ColdFusion 2025 (≤2025.0.11) and 2023 (≤2023.0.22), led by CVE-2026-48362 (CWE-78, OS command injection, CVSS 10.0, `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`) — unauthenticated arbitrary code execution — and CVE-2026-48273 (CWE-95, eval injection, 9.9, `AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`), which needs low-privileged access rather than none ([Adobe, APSB26-90, 2026-08-11](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)). The remaining fourteen span incorrect-authorization application denial-of-service (CVE-2026-71384, 9.6), cross-site scripting escalating to code execution (CVE-2026-71386, 8.8), privilege escalation via input validation (CVE-2026-21273, 8.7), further authorization and hard-coded-key defects down to CVSS 4.9, and a heap-based buffer overflow (CVE-2026-48440, 8.1). Adobe states it is "not aware of any exploits in the wild for any of the issues addressed in this update," and separately recommends keeping the underlying JDK/JRE current and reviewing its `serialFilter` guidance for insecure deserialization ([Adobe, APSB26-90, 2026-08-11](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)).

APSB26-123 covers Adobe Campaign Classic — explicitly scoped to on-premise deployments and the on-premise leg of hybrid deployments, since "Adobe-hosted instances have already been remediated and require no customer action" ([Adobe, APSB26-123, 2026-08-11](https://helpx.adobe.com/security/products/campaign/apsb26-123.html)). Two of its three fixed CVEs are unauthenticated CVSS 10.0 incorrect-authorization flaws reaching arbitrary code execution — CVE-2026-71398 and CVE-2026-27302, the same vector under two identifiers — and the third, CVE-2026-48381 (CWE-89, SQL injection, 9.0, `AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H`), is unauthenticated with high attack complexity. All three are fixed in ACC v7 7.4.4 build 9400 for both Windows and Linux; the earlier 7.4.3 build 9399 and prior are affected. No exploitation is reported for either bulletin, and neither Adobe advisory names a researcher, which is consistent with an internally-found batch.

Detection, in vendor-neutral terms: ColdFusion's command-injection path and Campaign Classic's authorization flaws both reach the underlying host or database with no prior authentication, so the durable telemetry is process-lineage and query-shape anomalies rather than an authentication event — a ColdFusion application-server process spawning an OS shell or interpreter with no corresponding administrative session, and Campaign Classic database queries or file operations issued outside the product's own scheduled and interactive-session patterns. Because no public proof-of-concept or exploitation report exists yet for either bulletin, the defensible position is to treat the patch window itself as the exposure window and close it before a diff-derived exploit appears, rather than waiting for confirmed activity.
