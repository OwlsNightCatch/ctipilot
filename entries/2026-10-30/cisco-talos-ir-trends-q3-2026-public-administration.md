---
schema: 1
kind: annual-report
title: "ANNUAL REPORT: Cisco Talos Incident Response trends Q3 2026: public administration tied with finance as the most targeted sector, help-desk vishing into remote-management tools, and ransomware operators uninstalling and killing EDR"
headline: "Talos IR Q3: public administration tied for most targeted; vishing into RMM and EDR killing mark the ransomware cases"
summary: >
  Cisco Talos Incident Response's Q3 2026 trends report names public administration, tied with finance at 18 percent of engagements, as the most targeted sector, and puts
  phishing first and public-facing application exploitation second among initial-access techniques. Its ransomware cases (27 percent of engagements) show help-desk vishing that
  leads the victim to allow remote access through a legitimate remote-management tool, and operators who uninstall or terminate EDR, including with vulnerable drivers.
discovered_at: "2026-10-30T03:46:00Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-10-30T0255Z-intel
priority: routine
immediate_action: null
tags: [ransomware, phishing]
regions: [global]
sectors: [public-sector]
entities: ["report:cisco-talos-ir-trends-q3-2026", "malware:vypr-ransomware", "actor:interlock"]
techniques: [T1566.004, T1219, T1059.001, T1105, T1685, T1070, T1486]
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/ir-trends-q3-2026/"
    publisher: "Cisco Talos"
    date: "2026-10-29"
    role: primary
closed_sources: []
evidence:
  - quote: "Targeting of the financial industry increased from last quarter to comprise 18 percent of all engagements, tying with public administration as the most targeted sector."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ir-trends-q3-2026/"
  - quote: "numerous threat actors conducting voice phishing (vishing) in tandem with IT desk impersonation to socially engineer the victim into allowing remote access via a legitimate remote monitoring and management (RMM) tool"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ir-trends-q3-2026/"
  - quote: "making multiple attempts to impair endpoint detection EDR capabilities by trying to uninstall Cisco Secure Endpoint (CSE) on compromised systems"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ir-trends-q3-2026/"
verification: single-source
sourcing_note: >
  A single first-party report from Cisco Talos Incident Response; the percentages describe Talos IR's own engagements, not the wider population of incidents.
confidence: high
references: []
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

Cisco Talos Incident Response reports that in Q3 2026 financial organisations made up 18 percent of its engagements, tying with public administration as the most targeted sector ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)). Phishing was the leading initial-access technique at 37 percent of engagements and exploitation of public-facing applications second at 33 percent; the phishing cases include numerous actors who phone the victim as the IT help desk to get remote access allowed through a legitimate remote monitoring and management (RMM) tool ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)). Ransomware and pre-ransomware cases were 27 percent of engagements, with The Gentlemen, Qilin, Rhysida and the closed group Interlock among the families and a new variant, VYPR, that Talos calls operationally immature: it had no leak site when seen, reused leaked Conti-derived source code and exfiltrated over several days ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)).

The VYPR intrusion began with a vishing call that had the user start a Microsoft Quick Assist session; the actor then used RMM software that ran PowerShell to download and install an MSI from a remote address, with MeshAgent, Rclone, PsExec, an IP scanner and mstsc as tools, and disabled EDR with several vulnerable drivers ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)). Interlock operators repeatedly tried to uninstall Cisco Secure Endpoint, used PsExec and taskkill to end security services and integrity checkers, turned off Windows Defender real-time protection and cleared event logs ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)). Talos names insufficient logging (over 40 percent of engagements), weak credential and secret handling, and absent or incomplete MFA as the most common weaknesses, and recommends centralised logging with at least 90 days of retention ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/ir-trends-q3-2026/)).

**Exposure:** an organisation whose help desk or staff can be reached by phone and whose endpoints permit Quick Assist or an unapproved RMM agent; Talos names public administration among the most targeted sectors in its caseload.

**Detection:** in process-creation and software-install telemetry, an RMM or Quick Assist session started after an inbound call, followed by PowerShell run under the RMM agent that downloads an installer from an external address; in endpoint and service-control telemetry, attempts to uninstall the EDR agent, PsExec or taskkill ending security services, Defender real-time protection switched off, vulnerable kernel drivers loaded, and event logs cleared.

**Defender takeaway:** treat a remote-support session that nobody at the help desk started as the vishing signal and inventory which RMM tools and Quick Assist are permitted on endpoints; alert on EDR uninstall and security-service termination as a ransomware precursor; and centralise logs with the 90-day minimum retention Talos recommends, because actors delete logs on the endpoint.
