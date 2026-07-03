---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: FortiBleed
headline: FortiBleed
summary: "FortiBleed escalates from credential exposure to confirmed AD domain takeover at a NATO-aligned defence contractor — patch level is irrelevant; rotate any FortiGate credential active May–June and hunt AD persistence. (daily 06-24, CISA)"
discovered_at: "2026-06-29T00:21:19Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - actively-exploited
  - data-breach
  - identity
  - russia-nexus
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - defense
  - telco
entities:
  - "incident:fortibleed-fortigate-credential-exposure"
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-of-credential-exposure"
    publisher: CISA alert
    role: primary
  - url: "https://securityaffairs.com/194004/hacking/fortibleed-the-most-detailed-breakdown-yet-of-an-active-russian-credential-harvesting-operation.html"
    publisher: Security Affairs
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
migrated_from: briefs/weekly/2026-W26.md
---

The W25 top story continued without a scale revision — the device count holds at the 86,644 figure the dailies reported — but the in-window development is the clearest state-interest signal yet: CISA [updated its hardening alert on 06-22](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-of-credential-exposure) to link Fortinet's revised guidance, and reporting now confirms that on in mid-June the Russian-speaking operator completed offline Kerberos-hash cracking from captured FortiGate configs and immediately exfiltrated DFS backup data from a NATO-aligned defence contractor — a full AD domain takeover ([Security Affairs](https://securityaffairs.com/194004/hacking/fortibleed-the-most-detailed-breakdown-yet-of-an-active-russian-credential-harvesting-operation.html)). Outstanding for defenders: treat any FortiGate admin/VPN credential active May–June 2026 as compromised, rotate, then hunt AD for pass-the-hash, DCSync and DFS-backup exfiltration (Kerberos ticket anomalies, LSASS access, `ntdsutil`/impacket artefacts). Patch level is irrelevant — this is credential reuse, not a new CVE.
