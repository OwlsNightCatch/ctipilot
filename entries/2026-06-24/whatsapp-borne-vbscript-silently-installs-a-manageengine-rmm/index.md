---
schema: 1
kind: threat
title: WhatsApp-borne VBScript silently installs a ManageEngine RMM agent for living-off-the-land remote control
headline: WhatsApp-borne VBScript silently installs a ManageEngine RMM agent for living-off-the-land remote control
summary: "A globally active campaign pushes obfuscated VBScript through WhatsApp Desktop/Web that disables UAC and silently installs a ManageEngine Endpoint Central RMM agent pointed at attacker infrastructure — living-off-the-land remote control with no bespoke malware. (Kaspersky, 2026-06-22)."
discovered_at: "2026-06-24T05:11:47Z"
event_date: 2026-06-23
run_id: 2026-06-24-de656486
priority: high
immediate_action: null
tags:
  - phishing
  - organized-crime
  - identity
regions:
  - global
  - europe
  - apac
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://securelist.com/whatsapp-vbs-rmm-campaign/120290/"
    publisher: Kaspersky Securelist
    role: primary
  - url: "https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: the messages contained only the malicious attachment and did not include any accompanying text
    publisher: Kaspersky Securelist
  - quote: "Stage 2 modifies UAC registry key HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ConsentPromptBehaviorAdmin to value 0, disabling consent prompts"
    publisher: Kaspersky Securelist
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
migrated_from: briefs/2026-06-24.md
---

Kaspersky documented (2026-06-22) a globally active campaign distributing heavily obfuscated VBScript via compromised WhatsApp Desktop / Web accounts, with financial-themed document lures in multiple languages ([Kaspersky Securelist, 2026-06-22](https://securelist.com/whatsapp-vbs-rmm-campaign/120290/); [The Hacker News, 2026-06-23](https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html)). The three-stage chain: a stage-1 VBScript creates working directories and fetches payloads via `curl`/`bitsadmin`/`certutil`/PowerShell; stage 2 disables UAC consent by writing `ConsentPromptBehaviorAdmin=0` to `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` and strips `Zone.Identifier` ADS; stage 3 silently installs a preconfigured **ManageEngine Endpoint Central** RMM agent via `msiexec` pointed at attacker-controlled infrastructure. Kaspersky attributes the activity only with low confidence to a Chinese-speaking operator, on the basis of Simplified-Chinese code comments and C2 infrastructure overlapping prior ValleyRAT / Gh0st RAT activity — the claim, not a firm attribution. Victims are concentrated in Malaysia (~80%) with clusters including the UK and Spain.

**Why it matters to us:** Abuse of a legitimate, signed RMM agent (`T1219`) is the operational point — there is no bespoke implant to signature, and ManageEngine Endpoint Central is plausibly already whitelisted in many estates. Mapped to `T1566.001` (spearphishing attachment, via WhatsApp), `T1059.005` (VBScript), `T1112` / `T1548` (UAC-bypass registry write), `T1105` (ingress tool transfer). Detection: `msiexec.exe /quiet` parented by `wscript.exe`/`cscript.exe`; writes to `...\Policies\System\ConsentPromptBehaviorAdmin`; `certutil -decode` or `bitsadmin` in a script context; and ManageEngine `DCAgentService.exe` appearing on a host with no corresponding IT-provisioning change ticket. RMM-agent abuse is a well-worn precursor to hands-on-keyboard intrusion and ransomware staging.
