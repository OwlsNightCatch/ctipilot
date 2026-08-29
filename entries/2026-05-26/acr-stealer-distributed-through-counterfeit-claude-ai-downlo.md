---
schema: 1
kind: threat
title: ACR Stealer distributed through counterfeit Claude AI download pages promoted by malicious search ads
headline: ACR Stealer distributed through counterfeit Claude AI download pages promoted by malicious search ads
summary: "SANS ISC handler Brad Duncan documented a delivery chain that impersonates Anthropic's Claude desktop app via counterfeit \"Download for Windows\" pages, promoted through malicious search ads hosted on sites.google.com, ultimately dropping ACR Stealer (SANS Internet Storm Center, 2026-05-26)."
discovered_at: "2026-05-26T05:00:01Z"
event_date: 2026-05-26
run_id: 2026-05-26-ae9d0d4b
priority: notable
immediate_action: null
tags:
  - infostealer
  - phishing
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33018"
    publisher: "SANS Internet Storm Center, 2026-05-26"
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
migrated_from: briefs/2026-05-26.md
---

SANS ISC handler Brad Duncan documented a delivery chain that impersonates Anthropic's Claude desktop app via counterfeit "Download for Windows" pages, promoted through malicious search ads hosted on `sites.google.com`, ultimately dropping **ACR Stealer** ([SANS Internet Storm Center, 2026-05-26](https://isc.sans.edu/diary/33018)). Clicking the download button delivers a corrupted ZIP archive containing obfuscated PowerShell; the infection chain also involves a JPEG image whose precise role the SANS ISC analyst could not characterise (no embedded data was identified in it), and ends in execution of the commodity infostealer ACR Stealer, which harvests credentials and browser data ([`T1566.002`](https://attack.mitre.org/techniques/T1566/002/), [`T1059.001`](https://attack.mitre.org/techniques/T1059/001/)). `[SINGLE-SOURCE]` — reported by SANS ISC only at time of writing.

**Why it matters to us:** this is the demand-side mirror of the TrapDoor item above — attackers monetising trust in AI tooling, here against ordinary employees searching for an AI client rather than developers. Add Anthropic/Claude and other AI-brand impersonation to brand-abuse and malvertising monitoring; hunt for `powershell.exe` spawned from browser-download or archive-extraction paths (Sysmon EID 1 / Windows 4688, especially with `-nop`/`-w hidden`/`-enc`), PowerShell reading image files as code, and outbound connections from `powershell.exe` to newly-registered domains.
