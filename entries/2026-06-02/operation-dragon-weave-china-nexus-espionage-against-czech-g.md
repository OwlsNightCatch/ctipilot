---
schema: 1
kind: threat
horizon: operational
title: "Operation Dragon Weave: China-nexus espionage against Czech government with Azure Blob Storage dead-drop C2"
headline: "Operation Dragon Weave: China-nexus espionage against Czech government with Azure Blob Storage dead-drop C2"
summary: "China-nexus Operation Dragon Weave targets Czech and Taiwanese government, academic and financial organisations with a Rust loader and an AdaptixC2 agent that routes C2 through Microsoft Azure Blob Storage as a dead-drop — today's deep dive (Seqrite Labs, 2026-06-01)."
discovered_at: "2026-06-02T05:00:11Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
  - cloud
regions:
  - europe
  - apac
sectors:
  - public-sector
  - education
  - finance
  - technology
entities:
  - "campaign:operation-dragon-weave"
cves: []
sources:
  - url: "https://www.seqrite.com/blog/operation-dragon-weave-uncovering-a-china-linked-campaign-targeting-czech-republic-and-taiwan-using-azure-cloud-c2/"
    publisher: Seqrite Labs
    role: primary
  - url: "https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-02.md
---

Seqrite Labs disclosed **Operation Dragon Weave** on 1 June 2026: a China-linked espionage campaign delivering spearphishing ZIP attachments to government, research, academic, technology and financial-services organisations in the **Czech Republic** and **Taiwan** ([Seqrite Labs, 2026-06-01](https://www.seqrite.com/blog/operation-dragon-weave-uncovering-a-china-linked-campaign-targeting-czech-republic-and-taiwan-using-azure-cloud-c2/) · [The Hacker News, 2026-06-01](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html)). A January 2026 iteration of the same activity used Cobalt Strike and additionally hit Cambodia and South Korea; the June reporting documents an evolved toolset and is the reason a Czech-government-targeting campaign warrants a Swiss/EU public-sector deep dive — the targeting set (a Central-European EU member's ministries and universities) is directly representative of the threat surface a Swiss federal SOC defends.

**Infection chains.** Two variants were observed, both arriving as ZIP attachments (`T1566.001` [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)). The first executes a malicious LNK disguised as a PDF, which launches PowerShell (`T1059.001` [PowerShell](https://attack.mitre.org/techniques/T1059/001/)) to stage the next component; the second drops and runs a binary directly. In both cases a Rust-based dropper that Seqrite names **RUSTCLOAK** performs DLL side-loading (`T1574.002` [DLL Side-Loading](https://attack.mitre.org/techniques/T1574/002/)) against a legitimate signed executable to load a malicious library, which deploys the final payload, **AZUREVEIL**.

**AZUREVEIL and the dead-drop C2.** AZUREVEIL is an agent built on **AdaptixC2** — an open-source command-and-control framework increasingly adopted by both red teams and intrusion sets — compiled with 36 post-exploitation commands spanning file operations, shell execution, process management and beacon-object-file (BOF) injection. Its distinguishing feature is the C2 channel: operator commands are routed through **Microsoft Azure Blob Storage as a dead-drop resolver** (`T1102.001` [Dead Drop Resolver](https://attack.mitre.org/techniques/T1102/001/)), with the agent polling and posting to blob endpoints over ordinary HTTPS (`T1071.001` [Web Protocols](https://attack.mitre.org/techniques/T1071/001/)). Because traffic terminates at `*.blob.core.windows.net`, it blends with the legitimate Azure usage of almost any modern enterprise and is allowlisted by most egress proxies — the same "abuse a trusted cloud service for C2" pattern seen this run in the WordPress/Steam campaign (§3) and recurring across recent intrusion sets.

**Attribution.** Seqrite attributes the activity to a China-based cluster at moderate confidence and names no specific group. The Hacker News's broader China-nexus roundup covers SteppeDriver and UNC5221 as separate actor clusters reported in the same window — these are distinct from Dragon Weave, and neither Seqrite nor The Hacker News connects Dragon Weave to either cluster ([The Hacker News, 2026-06-01](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html)). Treat the China nexus as the researcher's assessment rather than settled fact, and do not infer a group identity the sources do not assert.

**Detection concepts (no IOCs).** Hunt for: PowerShell spawned from non-standard parent processes immediately after archive extraction; LNK files masquerading as PDFs in mail-derived paths; signed-binary executions that side-load an unexpected DLL from a writable user-profile directory (Sysmon EID 7 image-load anomalies against a known-good binary); and — the highest-value network concept — outbound HTTPS to `blob.core.windows.net` from host processes with no legitimate Azure-SDK reason to talk to Blob Storage (browsers, Office, line-of-business apps that are not Azure-native). Baseline which of your hosts legitimately reach Azure Blob Storage and alert on the long tail.

**Hardening.** Enforce attachment policies that strip or detonate LNK-in-ZIP payloads at the mail gateway; apply WDAC/AppLocker rules that block user-writable-directory DLL side-loading against your signed-application inventory; and, where your environment does not legitimately use Azure Blob Storage, consider egress controls or monitoring that treat `*.blob.core.windows.net` as a named-service destination rather than blanket-allowlisting the Azure namespace. For estates that do use Azure, scope the allowlist to your own storage-account hostnames rather than the entire `blob.core.windows.net` wildcard.
