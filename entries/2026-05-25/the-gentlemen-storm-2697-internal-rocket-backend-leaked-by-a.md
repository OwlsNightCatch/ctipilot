---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "The Gentlemen / Storm-2697 — internal \"Rocket\" backend leaked by a rival; KELA and Check Point dissect the operator inner circle"
headline: "The Gentlemen / Storm-2697 — internal \"Rocket\" backend leaked by a rival; KELA and Check Point dissect the operator inner circle"
summary: "Most active RaaS exposed — The Gentlemen's internal database leaked. A rival dumped the operation's \"Rocket\" backend; KELA and Check Point analysis exposes the operator inner circle and an initial-access playbook (Fortinet/Cisco edges, NTLM relay, GPO deployment) that maps straight to hunts. (daily, Check Point)"
discovered_at: "2026-05-25T05:00:20Z"
event_date: null
run_id: 2026-W22-da77963d
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - identity
regions:
  - europe
  - switzerland
  - global
sectors:
  - manufacturing
  - healthcare
  - public-sector
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: Check Point Research — Thus Spoke The Gentlemen
    role: primary
  - url: "https://www.kelacyber.com/blog/the-gentlemen-ransomware-internal-chat-leak-analysis-2026/"
    publisher: KELA — internal chat-leak analysis
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
migrated_from: briefs/weekly/2026-W22.md
---

The most consequential campaign development of the window is one no daily captured: on 2026-05-04 a rival actor leaked The Gentlemen's internal **Rocket** database backend on underground forums, and KELA (2026-05-20) and Check Point ("Thus Spoke The Gentlemen", 2026-05-13) published deep analyses of the resulting six-month (Nov 2025 – Apr 2026) chat archive (`key: item:the-gentlemen-raas-czech-university-and-swiss-engineering-fi`). The leak exposes the inner circle (admin/infrastructure alias **zeta88**, also operating as **hastalamuerte**, alongside Wick, mAst3r, Kunder and others) and — far more useful to defenders — the operation's **initial-access playbook**: Fortinet and Cisco edge appliances, NTLM relay, harvested OWA / M365 credential logs, and **GPO-based deployment** of the encryptor. A linked affiliate runs a SystemBC SOCKS5 botnet of 1,570+ victims. This is an intelligence gift: every named access path maps to an existing hunt — prioritise edge-appliance patch state, NTLM-relay hardening (SMB/LDAP signing, channel binding) and anomalous-GPO-creation monitoring. Per Check Point's Q1 data the group sits at #3 globally (§ 6) — though its victims concentrate in Thailand, Brazil and India (US ~13%), so the European and Swiss listings carried over from W21 run *against* its centre of gravity, which is precisely what makes a CH/EU hit worth surfacing rather than treating as background.
