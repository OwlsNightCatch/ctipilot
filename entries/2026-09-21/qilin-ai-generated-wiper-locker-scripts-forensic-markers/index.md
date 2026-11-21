---
schema: 1
kind: threat
title: "Talos finds AI-generated Python wiper and mass-deployment scripts in a Qilin-affected environment, identified by step-numbered comments and consistent per-step logging"
headline: "Cisco Talos: a Qilin intrusion's own staging directory held ransomware deployment scripts the investigators assess were probably written by an AI model"
summary: >
  Cisco Talos found Python post-exploitation scripts in a Qilin ransomware-affected environment —
  a GPO-deployed time-triggered wiper, a Veeam-backup-destruction script and a mass ransomware
  deployment launcher — that Talos assesses with medium-to-high confidence were AI-generated, based on
  step-numbered code comments, consistent per-step logging and specification-style docstrings, plus a
  bash-history reference to a local "llm_chatbot" tool.
discovered_at: "2026-09-21T04:41:00Z"
updated_at: null
event_date: "2026-09-17"
run_id: 2026-09-21T0410Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - ai-abuse
regions:
  - global
sectors: []
entities:
  - "actor:qilin"
techniques:
  - T1489
  - T1490
  - T1484.001
  - T1486
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
    publisher: "Cisco Talos"
    date: "2026-09-17"
    role: primary
closed_sources: []
evidence:
  - quote: "Talos identified several characteristics in Python scripts found in an open directory used by Qilin that suggest, with medium-to-high confidence, that scripts may have been generated using AI"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
  - quote: "Figure 17 shows an excerpt from \"veeam_kill.py\", a Python script designed to stop, disable, and destroy Veeam backups. As shown in Figures 17 and 18, the main() function clearly divides the overall process into four stages, labeled \"Step 1\" through \"Step 4,\" with comments and progress logs provided at a consistent level of detail for each step."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/"
verification: single-source
sourcing_note: >
  Cisco Talos is the sole publisher; the AI-generation assessment is explicitly stated as
  medium-to-high confidence, based on stylistic markers rather than direct proof (no model watermark or
  provider admission), which this entry's wording preserves.
confidence: medium
references: ["2026-09-08/sekoia-kudelski-dprk-lazarus-umbrella-six-cluster-split"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Investigating a separate, Qilin-affected environment, Cisco Talos found three Python post-exploitation scripts in the operator's own staging directory that it assesses with medium-to-high confidence were generated with AI assistance rather than hand-written: `deadman.py`, a time-triggered wiper deployed via Group Policy Object; `veeam_kill.py`, which stops, disables and destroys Veeam backup infrastructure; and `deploy_locker.py`, a mass-deployment launcher for the ransomware payload itself ([Cisco Talos, 2026-09-17](https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)). Talos's basis for the AI-generation call is stylistic rather than a direct admission or watermark: `veeam_kill.py`'s `main()` function divides execution into four numbered stages, each carrying a comment and a progress-log line held to a uniform level of detail, and `deadman.py`'s `do_gpo` function shows the same evenly-commented, staged structure — a pattern Talos found consistent across the scripts and consistent with specification-style docstrings rather than typical hand-written incident-response or red-team tooling. The operator's own bash history additionally references a local tool named `llm_chatbot`, which Talos cites as corroborating evidence for AI involvement in the scripting workflow.

**Defender takeaway:** during incident response or threat hunting inside a ransomware-affected environment, treat evenly-structured, heavily step-commented Python (or equivalent) post-exploitation tooling as a forensic marker worth flagging on its own — it suggests a lower barrier to producing bespoke destructive tooling per engagement, which changes the assumption that only well-resourced affiliates write custom backup-killing or mass-deployment scripts. Any Veeam backup estate should independently verify that GPO deployment and backup-service-stop actions require the same monitored change-control path as any other production GPO change, since this is exactly the mechanism `deadman.py` and `veeam_kill.py` abused.
