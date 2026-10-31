---
schema: 1
kind: research
title: "Pwn2Own Berlin 2026 results: 47 zero-days and $1,298,250 awarded, DEVCORE Master of Pwn, AI coding agents and inference tools exploited"
headline: "Pwn2Own Berlin 2026 paid $1,298,250 for 47 zero-days; DEVCORE won as Exchange, ESXi and AI coding agents fell"
summary: >
  Pwn2Own Berlin 2026 (14 to 16 May, OffensiveCon) ended with $1,298,250 awarded for 47 unique zero-days and
  DEVCORE as Master of Pwn with 50.5 points. Results included a three-bug SYSTEM code execution chain on
  Microsoft Exchange, a VMware ESXi memory-corruption exploit with cross-tenant code execution, SharePoint,
  Edge and Windows 11 exploits, and wins against OpenAI Codex, Cursor, LM Studio, LiteLLM, Chroma and NVIDIA
  targets in ZDI's AI and NVIDIA categories. The bugs went to the vendors under a 90-day patch window.
discovered_at: "2026-05-17T05:00:06Z"
event_date: 2026-05-16
run_id: 2026-05-17-4381863a
priority: routine
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities:
  - "incident:pwn2own-berlin-2026"
techniques: [T1190, T1068, T1611]
affected_products:
  - "Microsoft Exchange Server"
  - "Microsoft SharePoint Server"
  - "Microsoft Edge"
  - "Microsoft Windows 11"
  - "VMware ESXi"
  - "Red Hat Enterprise Linux for Workstations"
  - "NVIDIA Container Toolkit"
  - "NVIDIA Megatron Bridge"
  - "OpenAI Codex"
  - "Cursor"
  - "LM Studio"
  - "LiteLLM"
  - "Chroma"
cves: []
sources:
  - url: "https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn"
    publisher: "Zero Day Initiative, Day Three"
    date: "2026-05-16"
    role: primary
  - url: "https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results"
    publisher: "Zero Day Initiative, Day Two"
    date: "2026-05-15"
    role: corroborating
  - url: "https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results"
    publisher: "Zero Day Initiative, Day One"
    date: "2026-05-14"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/"
    publisher: "BleepingComputer"
    date: "2026-05-15"
    role: corroborating
  - url: "https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/"
    publisher: "Hackread"
    date: "2026-05-12"
    role: corroborating
  - url: "https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026"
    publisher: "Zero Day Initiative, contest announcement"
    date: "2026-03-12"
    role: corroborating
  - url: "https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html"
    publisher: "Zero Day Initiative, contest rules"
    role: corroborating
closed_sources: []
evidence:
  - quote: "bringing the final totals to $1,298,250 awarded for 47 unique 0-day vulnerabilities across three days of competition"
    publisher: "Zero Day Initiative, Day Three"
    source_url: "https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn"
  - quote: "chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange, earning $200,000 and 20 Master of Pwn points"
    publisher: "Zero Day Initiative, Day Two"
    source_url: "https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results"
  - quote: "used a single CWE-150 bug to exploit OpenAI Codex, earning $40,000 and 4 Master of Pwn points"
    publisher: "Zero Day Initiative, Day One"
    source_url: "https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results"
  - quote: "This year, we’re expanding this and splitting it into multiple different categories: AI Databases, Coding Agents, Local Inferences, and a separate category for NVIDIA products."
    publisher: "Zero Day Initiative, contest announcement"
    source_url: "https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026"
  - quote: "Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-17.md
updates:
  - at: "2026-10-21T15:48:24Z"
    run_id: 2026-10-21T1149Z-audit
    type: correction
    summary: >
      The roundup is rebuilt from ZDI's three result pages, its announcement and rules, and
      BleepingComputer: no source says the Exchange chain was unauthenticated, ZDI's 2026 AI categories
      are AI Databases, Coding Agents, Local Inferences and NVIDIA rather than an "AI Agents" track, and
      not every AI target fell. Patch forecasts, a release wave attributed to ZDI, an AI attack-pattern
      analysis, Swiss and EU framing and hardening advice that no source gives are removed, two source
      dates are corrected, and the roundup is filed as research at routine priority, down from high, since
      no result reports in-the-wild use.
    fields: [actions, affected_products, body, classification, deep_dive, deep_dive_category, evidence, headline, kind, priority, regions, sectors, sources, summary, tags, techniques, title]
---

Pwn2Own Berlin 2026, ZDI's second Berlin contest after the inaugural 2025 event, ran at OffensiveCon from 14 to 16 May ([Zero Day Initiative, 2026-03-12](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026)) ([BleepingComputer, 2026-05-15](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)). For 2026 ZDI split its AI category into AI Databases, Coding Agents, Local Inferences and NVIDIA ([Zero Day Initiative, 2026-03-12](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026)). Targets ran fully patched in their default configurations ([Zero Day Initiative, contest rules](https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html)), and vendors have 90 days to patch after the zero-days are disclosed at the contest ([BleepingComputer, 2026-05-15](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)). Before it began, Hackread wrote that it had reportedly run out of space and that some researchers turned away were releasing their findings instead ([Hackread, 2026-05-12](https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/)).

The final totals were $1,298,250 for 47 unique zero-days; DEVCORE won Master of Pwn with 50.5 points and $505,000, ahead of STARLabs SG (25 points, $242,500) and Out Of Bounds (12.75 points, $95,750) ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)).

**Enterprise and platform targets.** Orange Tsai of DEVCORE chained four logic bugs for a Microsoft Edge sandbox escape ($175,000) on Day One ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)) and three bugs for remote code execution as SYSTEM on Microsoft Exchange ($200,000) on Day Two ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)); neither ZDI nor BleepingComputer states whether the chain needs authentication. splitline of DEVCORE chained two bugs against Microsoft SharePoint ($100,000), and Nguyen Hoang Thach of STARLabs SG used a memory corruption bug against VMware ESXi with the cross-tenant code execution add-on ($200,000) ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)), an entry that runs code from a guest on the hypervisor ([Zero Day Initiative, contest rules](https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html)). Windows 11 and Red Hat Enterprise Linux for Workstations fell to privilege escalations (improper access control, heap overflow, use-after-free, integer overflow and race-condition bugs), and NV Container Toolkit to chompie ($50,000) and to 0xDACA and Noam Trobishi with a use-after-free ($25,000) ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)) ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)) ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)).

**AI targets.** OpenAI Codex fell to Compass Security with a single CWE-150 bug ($40,000), while a Doyensec entry used a bug previously known to the vendor and a Viettel attempt failed ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)); Summoning Team ($20,000) ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)) and Satoki Tsuji of Ikotas Labs, through an external control ($20,000), also exploited it ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)). Cursor fell to Viettel ($30,000) and Compass Security ($15,000) ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)). LM Studio fell to STARLabs SG (five bugs) and LiteLLM to k3vg3n (three bugs), both chains including SSRF and code injection and each worth $40,000 ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)); OtterSec took LM Studio with a code injection bug ($20,000) ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)). Out Of Bounds took Chroma with two bugs (CWE-190, CWE-362; $20,000), and NVIDIA Megatron Bridge fell three times ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)). Every Anthropic Claude Code entry, Summoning Team's Claude Desktop entry, the Ollama entry and two LiteLLM entries hit previously known bugs or collisions ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)) ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)) ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)), and an Oracle Autonomous AI Database attempt failed ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)).

**Exposure:** current releases of the products named above, whose vendors received the bugs at the contest; ZDI's result pages give no CVE ids ([Zero Day Initiative, contest rules](https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html)) ([Zero Day Initiative, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)).

**Defender takeaway:** no change on the results alone: no source reports these bugs used in the wild, and vendors have 90 days to patch them ([BleepingComputer, 2026-05-15](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)).

## Correction — 2026-10-21T15:48:24Z

ZDI and BleepingComputer report the Exchange result as three chained bugs giving remote code execution as SYSTEM, and neither says the chain works without authentication ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)) ([BleepingComputer, 2026-05-15](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)). ZDI ran no "AI Agents" category: for 2026 it split its existing AI category into AI Databases, Coding Agents, Local Inferences and NVIDIA ([Zero Day Initiative, 2026-03-12](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026)), and not every AI target fell: an Oracle Autonomous AI Database attempt failed, while Chroma was a two-bug success rather than a collision ([Zero Day Initiative, 2026-05-14](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)). The pages report results only; they carry no patch forecast, no attack-pattern analysis of the AI targets and no hardening advice. The release of findings by researchers turned away from the contest was reported by Hackread before the contest as the researchers' own action, not ZDI's ([Hackread, 2026-05-12](https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/)). Vendors have 90 days to patch after the zero-days are disclosed at the contest ([BleepingComputer, 2026-05-15](https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/)), and the NV Container Toolkit researcher is Noam Trobishi ([Zero Day Initiative, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)).
