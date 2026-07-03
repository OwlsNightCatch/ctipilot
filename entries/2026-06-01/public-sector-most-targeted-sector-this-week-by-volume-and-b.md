---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Public sector — most-targeted sector this week by volume and by operational severity
headline: Public sector — most-targeted sector this week by volume and by operational severity
summary: "ENISA NIS360 2026: public administration receives nearly 63% of all EU hacktivist attacks yet remains structurally under-mature relative to its criticality. Seven sectors in the persistent \"risk zone\" where criticality exceeds maturity. (ENISA)"
discovered_at: "2026-06-01T05:00:08Z"
event_date: 2026-06-06
run_id: 2026-W23-9118e7bd
priority: high
immediate_action: null
tags:
  - nation-state
  - hacktivism
  - vulnerabilities
  - actively-exploited
regions:
  - europe
  - switzerland
sectors:
  - public-sector
entities:
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
  - "actor:op-512"
cves: []
sources:
  - url: "https://www.enisa.europa.eu/enisa-nis360-2026"
    publisher: ENISA NIS360 2026
    role: primary
  - url: "https://securityaffairs.com/193002/reports/enisa-nis360-2026-progress-across-the-board-but-the-sectors-that-matter-most-are-still-falling-short.html"
    publisher: Security Affairs — NIS360
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
actions: []
migrated_from: briefs/weekly/2026-W23.md
---

The public sector carried the highest concentration of critical items this week. CVE-2026-41089 (Netlogon SYSTEM RCE) and CVE-2026-20245 (Cisco SD-WAN no-patch zero-day) both have active exploitation with direct public-sector estate exposure. NCSC-CH's G7 Évian advisory is a direct Swiss federal / cantonal SOC priority for the coming week (. VerdantBamboo's intrusion entered through an MSP's pfSense — the precise threat model for any federation of public-sector organisations sharing managed-service relationships (§7). MISP CVE-2026-10868 patches EU CERT tooling directly used by the operators of this newsletter's primary audience. OP-512's China-linked IIS/.NET 4.0 cluster ([daily 2026-06-06](/briefs/2026-06-06/)) targets the legacy web-server estate still common in cantonal and municipal government, with per-deployment cryptographic keying defeating signature-based detection entirely. ENISA NIS360 confirms public administration is the most consistently targeted EU sector by hacktivist activity, receiving nearly 63% of all EU hacktivist attacks, yet about a third of entities lack structured cybersecurity expertise at management level.
