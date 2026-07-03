---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: node-ipc npm package — backdoored via expired-domain account takeover
headline: node-ipc npm package — backdoored via expired-domain account takeover
summary: "node-ipc npm package backdoored via expired-domain account takeover; 90+ credential categories exfiltrated; three malicious versions; ~3-minute window to detection (daily 2026-05-16)."
discovered_at: "2026-05-11T05:00:27Z"
event_date: null
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - supply-chain
  - data-breach
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://socket.dev/blog/node-ipc-package-compromised"
    publisher: Sonatype security advisory — node-ipc backdoor
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
migrated_from: briefs/weekly/2026-W20.md
---

`node-ipc` npm package backdoored via expired-domain account takeover; 90+ credential categories exfiltrated; three malicious versions; ~3-minute window to detection (daily 2026-05-16). The defender's learning is the **expired-domain account-takeover** vector — package-maintainer email domains that lapse become a one-time supply-chain compromise vector. Operational pattern-match: audit npm / PyPI / Cargo dependency trees for packages whose maintainer addresses are at domains your organisation could verify still belong to the original maintainer.
