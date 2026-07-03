---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Velvet Ant \"Operation Highland\" — Sygnia documents decade-long Linux PAM/sshd subversion"
headline: "Velvet Ant \"Operation Highland\" — Sygnia documents decade-long Linux PAM/sshd subversion"
summary: "key: campaign:velvet-ant-operation-highland-2026."
discovered_at: "2026-06-14T23:57:36Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
  - identity
regions:
  - global
sectors: []
entities:
  - "campaign:velvet-ant-operation-highland-2026"
cves: []
sources:
  - url: "https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.sygnia.co/blog/operation-highland-velvet-ant/"
    publisher: Sygnia — Operation Highland
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
migrated_from: briefs/weekly/2026-W24.md
---

`key: campaign:velvet-ant-operation-highland-2026`. Sygnia's "Operation Highland" report, relayed in detail by The Hacker News on 12 June and deep-dived in the [06-13 daily](/briefs/2026-06-13/), documents a China-nexus intrusion set that held covert access to an air-gapped network for nearly a decade (earliest traces ~2016) by subverting the Linux authentication stack: nine distinct backdoored `pam_unix.so` variants and credential-logging `sshd`/`ssh` binaries that suppress their own logging during operator sessions ([The Hacker News](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html); [Sygnia — Operation Highland](https://www.sygnia.co/blog/operation-highland-velvet-ant/)). The horizon framing the dailies could not give: this is the same tradecraft class as VerdantBamboo's edge-appliance persistence — long-dwell, identity/auth-layer implants on systems outside EDR coverage. The two together describe a sustained China-nexus investment in living below the endpoint-detection line. Defender watch-item: integrity-monitor PAM modules and `sshd`/`ssh` binaries against package checksums (`rpm -V` / `dpkg --verify`, AIDE/Tripwire), and treat air-gap as a latency control, not an isolation guarantee.
