---
schema: 1
kind: threat
horizon: operational
title: "FrostyNeighbor / Ghostwriter (UNC1151, Belarus state-aligned): ESET documents March–May 2026 campaign targeting Polish, Lithuanian, and Ukrainian government and industrial sectors"
headline: "FrostyNeighbor / Ghostwriter (UNC1151, Belarus state-aligned): ESET documents March–May 2026 campaign targeting Polish, Lithuanian, and Ukrainian government"
summary: "ESET published a new technical report on 2026-05-14 documenting fresh operational activity from FrostyNeighbor — a cluster ESET and Mandiant track as Ghostwriter / UNC1151 / UAC-0057, assessed as apparently Belarus state-aligned — against Polish, Lithuanian, and Ukrainian government and industrial organisations across …"
discovered_at: "2026-05-15T05:00:02Z"
event_date: 2026-05-14
run_id: 2026-05-15-58b94fbd
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
  - healthcare
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
    publisher: "ESET WeLiveSecurity, 2026-05-14"
    role: primary
  - url: "https://thehackernews.com/2026/05/ghostwriter-targets-ukrainian.html"
    publisher: "The Hacker News, 2026-05-14"
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
migrated_from: briefs/2026-05-15.md
---

ESET published a new technical report on 2026-05-14 documenting fresh operational activity from FrostyNeighbor — a cluster ESET and Mandiant track as Ghostwriter / UNC1151 / UAC-0057, assessed as apparently Belarus state-aligned — against Polish, Lithuanian, and Ukrainian government and industrial organisations across a March–May 2026 wave ([ESET WeLiveSecurity, 2026-05-14](https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)). The Ukraine strand distributes RAR archives via spear-phishing PDFs impersonating Ukrtelecom; the archives drop a JavaScript downloader (a PicassoLoader variant) that fingerprints the victim environment (username, process list, OS version) and beacons every 10 minutes to operator infrastructure. A server-side geofencing check delivers a benign decoy to IPs outside Ukraine, making emulation from a non-Ukrainian network appear clean. Polish and Lithuanian targeting covers industrial/manufacturing, healthcare and pharmaceuticals, logistics, and government organisations — ESET documents victimology spanning both NATO member states in the same campaign wave. Once operators manually approve a victim, a Cobalt Strike Beacon payload is staged, indicating deliberate victim-vetting prior to full post-compromise operations. MITRE ATT&CK: [T1566.001](https://attack.mitre.org/techniques/T1566/001/) (Spearphishing Attachment), [T1027](https://attack.mitre.org/techniques/T1027/) (Obfuscated Files), [T1059.007](https://attack.mitre.org/techniques/T1059/007/) (JavaScript), [T1082](https://attack.mitre.org/techniques/T1082/) (System Information Discovery — victim-vetting step), [T1105](https://attack.mitre.org/techniques/T1105/) (Ingress Tool Transfer — Cobalt Strike staging). Detection: alert on JavaScript execution from browser/document-viewer parent-process trees, followed by 10-minute periodic outbound HTTP(S) beacons to a new destination; test detections with Ukrainian-egress routing to bypass the geofencing blind spot.
