---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "2026-W29 vulnerability status roll-up — nine CVEs crossed into confirmed exploitation/KEV, two more carry public exploit code, and a dense critical-but-unexploited tail hit edge, ERP and OT"
headline: "W29 CVE trajectory — nine exploited/KEV (SonicWall, ShareFile, Oracle EBS, SharePoint/AD FS, KNX), two public-exploit (WP2Shell, Firefox), a dense critical tail"
summary: >
  Consolidated status of the CVEs this pipeline covered operationally in ISO week 2026-W29, with each item's trajectory this week versus first coverage. Confirmed exploited / newly KEV-listed: CVE-2026-2699 (ShareFile SZC), CVE-2026-56155 (AD FS) and CVE-2026-56164 + CVE-2026-58644 (on-prem SharePoint), CVE-2026-15409 + CVE-2026-15410 (SonicWall SMA1000), CVE-2026-46817 (Oracle EBS Payments), plus two older KEV additions actively exploited now — CVE-2018-0171 (Cisco Smart Install) and CVE-2023-4346 (KNX). Public exploit code but no confirmed in-the-wild abuse: CVE-2026-63030 + CVE-2026-60137 (WordPress "WP2Shell") and CVE-2026-15718 + CVE-2026-15719 (Firefox). Critical-but-unexploited tail requiring scheduled action: SAP (CVE-2026-44747/27690/44761), VMware Avi Load Balancer (CVE-2026-47865), Siemens RUGGEDCOM ROX II (CVE-2025-40947/40948/40949), Rockwell 1715-AENTR (CVE-2026-10577, CVSS 10.0) and ABB T-MAC, plus Abacus ERP (no CVE, CVSS 9.8) and Moodle local_o365 (CVE-2026-54733). Full per-CVE detail lives in the referenced operational entries; this roll-up carries only the week's trajectory.
discovered_at: "2026-07-19T23:44:00Z"
event_date: 2026-07-17
run_id: 2026-07-19T2310Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - pre-auth
  - rce
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - energy
  - water
cves: []
techniques:
  - T1190
  - T1068
  - T1505.003
affected_products: []
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations"
    publisher: "CISA"
    date: "2026-07-16"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-07-15"
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "cves: [] by design — every CVE in this roll-up is fully sourced in its referenced operational entry; duplicating them in frontmatter would trip cross-run CVE dedup. The roll-up cites only the week's status-trajectory sources in prose."
confidence: high
update_of: null
references:
  - 2026-07-18/sonicwall-sma1000-uta0533-exploitation-kill-chain
  - 2026-07-14/progress-sharefile-szc-active-exploitation-confirmed
  - 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed
  - 2026-07-17/cve-2026-58644-sharepoint-confirmed-exploited-kev
  - 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
  - 2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup
  - 2026-07-13/fsb-centre-16-static-tundra-router-hijacking-advisory
  - 2026-07-16/cve-2023-4346-knx-building-automation-lockout-dos-kev
  - 2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030
  - 2026-07-17/firefox-152-0-6-wasm-site-isolation-public-exploit
  - 2026-07-14/sap-july-2026-patch-day-netweaver-approuter-commerce-cloud
  - 2026-07-18/vmware-avi-load-balancer-cve-2026-47865-auth-bypass
  - 2026-07-18/siemens-ruggedcom-rox-ii-unit42-three-cve-chain
  - 2026-07-15/cisa-ics-batch-rockwell-abb-energy-water-ot
  - 2026-07-17/abacus-erp-unauth-rce-path-traversal-ncsc-ch
  - 2026-07-18/moodle-local-o365-jwt-forgery-admin-takeover-cve-2026-54733
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

This roll-up tracks the week's CVEs by exploitation trajectory, not severity score. Per-CVE mechanics, affected/fixed versions and evidence are in the referenced operational entries.

**Confirmed exploited / newly KEV-listed this week.** Four Microsoft on-prem items moved: AD FS CVE-2026-56155 and SharePoint CVE-2026-56164 shipped 2026-07-14 as exploited zero-days KEV-listed the same day, and CVE-2026-58644 — a July SharePoint RCE first rated only "Exploitation More Likely" — was confirmed exploited and KEV-added on 2026-07-16, with CISA naming it in a cluster it is "aware of active exploitation" of ([CISA, 2026-07-16](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations)). SonicWall SMA1000 CVE-2026-15409/-15410 (KEV 2026-07-14) and Oracle EBS Payments CVE-2026-46817 (KEV 2026-07-15, [CISA](https://www.cisa.gov/news-events/alerts/2026/07/15/cisa-adds-two-known-exploited-vulnerabilities-catalog)) both carried confirmed in-the-wild exploitation, as did ShareFile SZC CVE-2026-2699. Two older CVEs joined KEV as actively exploited: Cisco Smart Install CVE-2018-0171 (the FSB Centre 16 router vector) and — notably for OT — KNX Connection Authorization CVE-2023-4346, a three-year-old account-lockout flaw whose fix is procedural, not a patch.

**Public exploit code, no confirmed in-the-wild abuse (short fuse).** WordPress core's "WP2Shell" chain (CVE-2026-63030 route-confusion in the unauthenticated REST batch endpoint + CVE-2026-60137 WP_Query SQL injection) reaches pre-auth RCE on a stock install; public PoC is already on GitHub and NCSC-NL assesses short-term exploitation is expected. Firefox 152.0.6 fixed a WebAssembly memory bug (CVE-2026-15718) and a site-isolation bypass (CVE-2026-15719) with public exploit code, though Mozilla states no in-the-wild abuse — contrary to some aggregator "zero-day" framing.

**Critical-but-unexploited tail (scheduled, exposure-driven action).** No confirmed exploitation yet, but each is a pre-auth or high-impact flaw on exposed or CI-relevant software: SAP's July set (CVE-2026-44747 NetWeaver kernel, CVE-2026-27690 Approuter request-smuggling, CVE-2026-44761 Commerce Cloud hardcoded credential — the last a config exposure a patch alone does not close); VMware Avi Load Balancer control-plane auth bypass CVE-2026-47865 (reported by NATO NCSC, no workaround); Siemens RUGGEDCOM ROX II's three-CVE chain to persistent root (CVE-2025-40947/40948/40949); Rockwell 1715-AENTR CVE-2026-10577 (CVSS 10.0 unauthenticated debug-port takeover) and the ABB T-MAC chain; Abacus ERP's unauthenticated RCE (CVSS 9.8, no CVE, NCSC-CH-flagged, ubiquitous in Switzerland); and Moodle's local_o365 JWT-signature-non-verification takeover CVE-2026-54733 across the European public-sector LMS estate.

**Defender takeaway:** the week's exploited set is dominated by internet-facing enterprise software and OT, and the confirmed-exploited items are exactly where an out-of-band response belongs; the critical-unexploited tail is real work but fits a prioritised patch schedule keyed on exposure. The KNX and Rockwell items are the reminder that the OT estate carries CVSS-10-class exposure with interim controls (network isolation, procedural lockout hygiene) that matter as much as the firmware.
