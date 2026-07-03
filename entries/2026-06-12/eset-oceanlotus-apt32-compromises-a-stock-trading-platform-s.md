---
schema: 1
kind: research
horizon: operational
title: "ESET: OceanLotus (APT32) compromises a stock-trading platform's update server — selective SPECTRALVIPER delivery, no integrity checks to defeat"
headline: "ESET: OceanLotus (APT32) compromises a stock-trading platform's update server — selective SPECTRALVIPER delivery, no integrity checks to defeat"
summary: "ESET documents two SPECTRALVIPER-delivered OceanLotus (APT32) intrusions running from mid-2024 into 2026: a long-dwell espionage compromise of a Vietnamese infrastructure/transport construction firm (likely via RCE on a public-facing Microsoft SQL Server, T1190) and — more transferable — a supply-chain attack on …"
discovered_at: "2026-06-12T05:00:08Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
regions:
  - apac
sectors:
  - finance
  - transport
entities:
  - "actor:oceanlotus"
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/oceanlotus-external-espionage-domestic-targeting/"
    publisher: ESET WeLiveSecurity
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
migrated_from: briefs/2026-06-12.md
---

ESET documents two SPECTRALVIPER-delivered OceanLotus (APT32) intrusions running from mid-2024 into 2026: a long-dwell espionage compromise of a Vietnamese infrastructure/transport construction firm (likely via RCE on a public-facing Microsoft SQL Server, [T1190](https://attack.mitre.org/techniques/T1190/)) and — more transferable — a supply-chain attack on FireAnt MetaKit, a stock-investment platform, between October 2025 and March 2026 ([ESET WeLiveSecurity, 2026-06-11](https://www.welivesecurity.com/en/eset-research/oceanlotus-external-espionage-domestic-targeting/)). The platform's update mechanism fetched its `version.xml` over plain HTTP with no integrity validation; OceanLotus replaced the update binary with a downloader that fingerprinted hosts and delivered the SPECTRALVIPER backdoor via process injection and DLL side-loading ([T1195.002](https://attack.mitre.org/techniques/T1195/002/), [T1055](https://attack.mitre.org/techniques/T1055/)) to only a small subset of victims — investigative targeting, not mass compromise. ESET's disclosure attempts to the vendor went unanswered. [SINGLE-SOURCE — ESET Research.] Defender takeaway: the pattern (unsigned updates, cleartext transport, no version-file integrity check) is endemic in regional/vertical software far beyond Vietnam — inventory third-party auto-updaters in your estate and flag any fetching over HTTP or lacking signature validation; egress-monitor the hosts that run them.
