---
schema: 1
kind: research
title: "Microsoft Defender Experts — AI-chatbot search-poisoning extends SEO-poisoning lure; GPU-utility lookalikes drop ScreenConnect, then process-hollowed miners under signed Microsoft binary"
headline: "Microsoft Defender Experts — AI-chatbot search-poisoning extends SEO-poisoning lure; GPU-utility lookalikes drop ScreenConnect, then process-hollowed miners"
summary: "Microsoft Defender Experts documented an active cryptojacking campaign dating from March 2026 that uses GPU-utility brand impersonation (CrystalDiskInfo, HWMonitor, Display Driver Uninstaller, FurMark, K-Lite Codec Pack, PDFgear) as initial delivery via SEO poisoning (Microsoft Security Blog, 2026-05-26; The Hacker …"
discovered_at: "2026-05-28T05:00:09Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - cryptocrime
  - ai-abuse
  - phishing
  - infostealer
regions:
  - global
sectors:
  - technology
  - finance
entities:
  - "campaign:microsoft-ai-chatbot-search-poisoning-cryptojacking-screenconnect-process-hollow"
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/"
    publisher: Microsoft Security Blog
    role: primary
  - url: "https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-28.md
---

Microsoft Defender Experts documented an active cryptojacking campaign dating from March 2026 that uses GPU-utility brand impersonation (CrystalDiskInfo, HWMonitor, Display Driver Uninstaller, FurMark, K-Lite Codec Pack, PDFgear) as initial delivery via SEO poisoning ([Microsoft Security Blog, 2026-05-26](https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/); [The Hacker News, 2026-05-27](https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html)). The operationally novel evolution is from April 2026: users querying AI chatbots for software-download recommendations were directed to attacker-controlled domains in generated responses — *search-poisoning extended into the LLM-generation layer*. Delivery chain: (1) fake utility site hosts a ZIP on a `gleeze.com` subdomain (DDNS via Dynu); (2) ZIP contains the legitimate executable alongside an `autorun.dll`; (3) DLL side-loading installs `vcredist_x64.dll` via `msiexec.exe` — a ScreenConnect packaged installer named to mimic Visual C++ Redistributable; (4) ScreenConnect establishes persistent remote access; (5) the session delivers `SimpleRunPE.exe`; (6) `SimpleRunPE` persists via Registry Run keys and scheduled tasks, configures Microsoft Defender exclusions, and uses process hollowing to inject miner code (`gminer`, `lolMiner`, `SRBMiner-MULTI`) into a Microsoft-signed binary. 150+ malicious domains identified since March 2026.

**Defender takeaway:** AI-search-result poisoning generalises the SEO-poisoning class to the prompt-response surface; orgs adopting AI coding assistants and chatbots should treat outbound URLs in generated responses as untrusted by default. Detection: Sysmon EID 7 loads of a DLL named `autorun.dll` from non-standard paths; `msiexec.exe` spawned as a child of a user-facing utility outside admin intent; ScreenConnect (`ConnectWise Control`) service installation from an unexpected parent process chain; Microsoft Defender exclusion modifications via command-line. Hardening: WDAC blocking unsigned DLLs; AppLocker scoping `msiexec.exe` to admin context; enable Defender Tamper Protection.
