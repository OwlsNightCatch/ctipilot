---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "FrostyNeighbor / Ghostwriter (UNC1151) — ESET analysis corroborated, Poland / Lithuania / Ukraine in EU scope"
headline: "FrostyNeighbor / Ghostwriter (UNC1151) — ESET analysis corroborated, Poland / Lithuania / Ukraine in EU scope"
summary: "ESET's 2026-05-14 analysis of activity observed since March 2026 documents an evolved spearphishing chain: (1) malicious PDFs impersonating Ukrtelecom with embedded redirect links, (2) RAR archives delivering JavaScript PicassoLoader variants, (3) server-side victim geo-validation (serves benign PDF to …"
discovered_at: "2026-05-11T05:00:36Z"
event_date: 2026-05-15
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
    publisher: ESET WeLiveSecurity
    role: primary
  - url: "https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html"
    publisher: The Hacker News
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
migrated_from: briefs/weekly/2026-W20.md
---

ESET's 2026-05-14 analysis of activity observed since March 2026 documents an evolved spearphishing chain: (1) malicious PDFs impersonating Ukrtelecom with embedded redirect links, (2) RAR archives delivering JavaScript PicassoLoader variants, (3) server-side victim **geo-validation** (serves benign PDF to non-Ukrainian IPs) with system fingerprinting every 10 minutes to determine Cobalt Strike eligibility, (4) persistence via scheduled tasks and registry modifications. The previous Polish-targeting wave exploited CVE-2024-42009 (Roundcube XSS) for credential harvesting; WinRAR CVE-2023-38831 also referenced in the toolchain. The Belarus-aligned actor cluster (UNC1151, UAC-0057, TA445, Storm-0257, Umbral Bison, White Lynx) targets governmental, industrial, healthcare, and logistics sectors. EU scope: **Poland, Lithuania, and Ukraine** confirmed; broader Eastern European public-sector exposure inferred ([ESET WeLiveSecurity](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/); [The Hacker News](https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html); [daily 2026-05-15](/briefs/2026-05-15/)).

No named EU victim disclosures this run. Status update from the W19 long-running record (`item:apt28-apt29-unc1151`): ESET's documentation of the geofencing and 10-minute fingerprinting cadence is new operational detail not present in the W19 ABW tri-attribution coverage. Detection: outbound connections to Canarytokens-style endpoints used for fingerprinting; scheduled-task creation with random GUIDs spawned from Office process trees (T1053.005); child processes of WinRAR or archive handlers executing JavaScript (T1059.007); PicassoLoader staging behaviours.
