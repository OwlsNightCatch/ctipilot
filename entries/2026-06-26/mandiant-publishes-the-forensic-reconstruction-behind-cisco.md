---
schema: 1
kind: vulnerability
horizon: operational
title: Mandiant publishes the forensic reconstruction behind Cisco SD-WAN Manager CVE-2026-20245
headline: Mandiant publishes the forensic reconstruction behind Cisco SD-WAN Manager CVE-2026-20245
summary: "Mandiant reconstructs a months-long zero-day compromise of Cisco Catalyst SD-WAN Manager (CVE-2026-20245) — updating our 6 June coverage, GTIG details an authenticated request tenant-upload CLI command-injection path that planted a troot UID-0 account on the controller, reached after a peering-auth-bypass foothold and exploited at a service provider from late 2025 through March 2026, well before the patch (Mandiant/GTIG, 2026-06-24). Today's deep dive (§5). Patch to the fixed trains immediately and audit vManage hosts for OS-level account creation."
discovered_at: "2026-06-26T04:54:42Z"
event_date: 2026-06-24
run_id: 2026-06-26-6bbe4619
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - priv-esc
  - rce
  - patch-available
regions:
  - global
sectors:
  - telco
  - public-sector
entities: []
cves:
  - id: CVE-2026-20245
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - exploited
      - patch-available
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager"
    publisher: Mandiant/GTIG
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx"
    publisher: Cisco PSIRT
    role: corroborating
closed_sources: []
evidence:
  - quote: "UPDATE (originally covered 2026-06-06): When we first noted CVE-2026-20245 it was a fresh Cisco advisory for a command-injection-to-root flaw in Catalyst SD-WAN Manager with confirmed exploitation but little public detail."
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
update_of: 2026-06-06/cve-2026-20245-cisco-catalyst-sd-wan-manager-actively-exploi
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-26.md
---

**UPDATE (originally covered 2026-06-06):** When we first noted CVE-2026-20245 it was a fresh Cisco advisory for a command-injection-to-root flaw in Catalyst SD-WAN Manager with confirmed exploitation but little public detail. Mandiant/GTIG has now published the forensic reconstruction, confirming the flaw was used as a **zero-day at a communications service provider from late 2025 through March 2026 — months before the patch** ([Mandiant/GTIG, 2026-06-24](https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager)).

The new substance is the kill chain: a peering-authentication-bypass foothold (CVE-2026-20127 / CVE-2026-20182) into SSH as `vmanage-admin`, then a crafted tenant CSV through the `request tenant-upload` CLI handler injecting commands that planted a backdoor `troot` UID-0 account, with anti-forensic clean-up (admin-password change-then-revert, history/syslog deletion). Mandiant names no threat actor. Full mechanics, ATT&CK mapping and host-level detection are in §5.
