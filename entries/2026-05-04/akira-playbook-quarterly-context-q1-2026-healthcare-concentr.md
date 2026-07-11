---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Akira playbook quarterly context — Q1 2026 healthcare concentration; Qilin remains the dominant operator on German healthcare victims"
headline: "Akira playbook quarterly context — Q1 2026 healthcare concentration; Qilin remains the dominant operator on German healthcare victims"
summary: W1 horizon research added Q1 2026 healthcare quarterly context to the Groupe 3R item in § 1.
discovered_at: "2026-05-04T05:00:41Z"
event_date: 2026-04-29
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
regions:
  - europe
  - dach
  - switzerland
sectors:
  - healthcare
entities:
  - "actor:thegentlemen"
  - "actor:akira"
  - "actor:qilin"
cves: []
sources:
  - url: "https://www.comparitech.com/news/healthcare-ransomware-roundup-q1-2026-stats-on-attacks-ransoms-and-data-breaches/"
    publisher: Comparitech Q1 2026 Healthcare
    role: primary
  - url: "https://www.cybermaxx.com/resources/ransomware-research-report-q1-2026-audio-blog-interview/"
    publisher: CyberMaxx Q1 2026 Ransomware Research
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
migrated_from: briefs/weekly/2026-W19.md
---

W1 horizon research added Q1 2026 healthcare quarterly context to the Groupe 3R item in § 1. Across Q1 2026, Akira posted 84 victims in March alone (second-most-active month on record) and claimed 5 healthcare victims; Qilin led healthcare at 23 claims (with **RENAFAN GmbH** and **Suchthilfe direkt Essen gGmbH** as Qilin's confirmed German victims), and The Gentlemen at 10 healthcare claims ([Comparitech Q1 2026 Healthcare, 2026-04-29](https://www.comparitech.com/news/healthcare-ransomware-roundup-q1-2026-stats-on-attacks-ransoms-and-data-breaches/) · [CyberMaxx Q1 2026](https://www.cybermaxx.com/resources/ransomware-research-report-q1-2026-audio-blog-interview/)). Akira's documented attack chain for healthcare: initial access via unpatched VPN (Cisco ASA, SonicWall, Fortinet) or compromised RDP credentials; lateral movement via [T1021.001 Remote Services: Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001/) and [T1047 Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/); LSASS credential harvesting via `comsvcs.dll` / Mimikatz; AV termination via PowerTool weaponising the Zemana AntiMalware driver (BYOVD); data exfiltration; double extortion. The cross-finding for Swiss / DACH operators reading after Groupe 3R: at least two ransomware-as-a-service operators (Akira and Qilin) are hitting European healthcare in Q1–Q2 2026 via the edge-device / unpatched-VPN attack surface, and the operator that hits a given hospital is less salient defensively than the shared initial-access funnel they exploit.
