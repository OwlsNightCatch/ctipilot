---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Gamaredon — GammaPhish / GammaWorm / GammaSteel: Russian FSB campaign with USB worm and S3 exfiltration (Sekoia TDR part one)"
headline: "Gamaredon — GammaPhish / GammaWorm / GammaSteel: Russian FSB campaign with USB worm and S3 exfiltration (Sekoia TDR part one)"
summary: "Sekoia's first part of the Gamaredon series disclosed a January 2026 campaign arc (Sekoia TDR, 2026-06-01; daily 2026-06-02; update daily 2026-06-03). Initial access via CVE-2025-8088 (WinRAR path-traversal, widely unpatched) drops HTA payloads from xHTML attachments."
discovered_at: "2026-06-01T05:00:20Z"
event_date: 2026-06-03
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
  - botnet
regions:
  - europe
sectors:
  - public-sector
  - defense
entities:
  - "actor:gamaredon"
cves: []
sources:
  - url: "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"
    publisher: Sekoia TDR
    role: primary
closed_sources: []
evidence: []
verification: single-source
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

Sekoia's first part of the Gamaredon series disclosed a January 2026 campaign arc ([Sekoia TDR, 2026-06-01](https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/); [daily 2026-06-02](/briefs/2026-06-02/); update [daily 2026-06-03](/briefs/2026-06-03/)). Initial access via CVE-2025-8088 (WinRAR path-traversal, widely unpatched) drops HTA payloads from xHTML attachments. GammaWorm's NTFS-ADS concealment and USB-propagation pattern is the signature detection challenge: filesystem timestamps are useless (ADS hides the worm content), and the worm spreads to any mounted drive and mapped share, meaning air-gap-adjacent workstations remain in scope. GammaSteel exfiltrates collected data directly to S3. Part two of the Sekoia series is outstanding and expected to detail further tooling. Open question: has the campaign reached any EU public-sector estate beyond its primary Ukrainian targets? The USB-propagation vector is exactly the mechanism Luna Moth used this week for physical office intrusion — conceptually distinct actors, coincidentally parallel technique.
