---
schema: 1
kind: threat
horizon: operational
title: "MuddyWater (Iran/MOIS) deploys Chaos ransomware as false flag; harvests credentials via Teams"
headline: "MuddyWater (Iran/MOIS) deploys Chaos ransomware as false flag; harvests credentials via Teams"
summary: "Security researchers documented a refreshed campaign by MuddyWater (attributed to Iran's Ministry of Intelligence and Security, MOIS), targeting government contractors and defence-adjacent organisations in Europe and the Middle East."
discovered_at: "2026-05-08T05:00:03Z"
event_date: null
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - ransomware
  - phishing
  - identity
  - iran-nexus
regions:
  - europe
  - middle-east
sectors: []
entities: []
cves: []
sources:
  - url: "https://www.deepinstinct.com/blog/muddywater-2026"
    publisher: Deep Instinct Threat Intelligence — MuddyWater 2026 Campaign
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
migrated_from: briefs/2026-05-08.md
---

Security researchers documented a refreshed campaign by **MuddyWater** (attributed to Iran's Ministry of Intelligence and Security, MOIS), targeting government contractors and defence-adjacent organisations in Europe and the Middle East. The campaign deploys **Chaos** ransomware payloads with branding designed to mimic criminal ransomware groups — a deliberate false-flag technique intended to complicate attribution and delay incident response triage. A parallel social-engineering vector uses Microsoft Teams external-access invitations to gain remote-assistance sessions under a helpdesk pretext, after which credentials are harvested and used for further access via legitimate cloud services. Observed ATT&CK techniques: T1566.004 (Spearphishing via Teams), T1649 (Steal or Forge Authentication Certificates), T1486 (Data Encrypted for Impact). This is a single-source threat-intelligence vendor disclosure.
