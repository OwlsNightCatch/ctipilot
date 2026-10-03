---
schema: 1
kind: threat
title: "CLOSEDQUORUM: Cisco Talos documents the first publicly reported Windows implant that lets a panel of four commercial LLMs vote on its next action instead of a human operator"
headline: "A malware implant treats commercial AI chatbot endpoints as its command-and-control infrastructure, no attacker server required"
summary: >
  Cisco Talos disclosed CLOSEDQUORUM on 2026-09-22, a Go-compiled Windows
  implant that queries up to four commercial LLM providers (DeepSeek, Qwen,
  Mistral, Google Gemini) each cycle and executes whichever action wins a
  plurality vote among their responses — credential theft, process injection,
  or persistence — with results relayed and stolen data exfiltrated through a
  Discord webhook. Talos found it via CAIRN, a new open-source toolkit it
  released the same day for tracking AI-integrated malware, and states plainly
  it has no confirmation of in-the-wild deployment; the public distribution
  build ships placeholder API keys.
discovered_at: "2026-09-24T04:45:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-24T0405Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, infostealer, vulnerabilities]
regions: [global]
sectors: []
entities: ["malware:closedquorum", "tool:cairn-talos", "product:microsoft-windows", "product:google-chrome", "product:microsoft-edge", "product:mozilla-firefox"]
techniques: [T1055.004, T1055.012, T1003.001, T1555.003, T1547.001, T1053.005, T1546.003, T1567.004, T1685]
affected_products: ["Microsoft Windows", "Google Chrome", "Microsoft Edge", "Mozilla Firefox"]
cves: []
sources:
  - url: "https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/"
    publisher: "Cisco Talos"
    date: "2026-09-22"
    role: primary
  - url: "https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html"
    publisher: "The Hacker News"
    date: "2026-09-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "exhibits fully autonomous command and control (C2). While we do not have confirmation of in-the-wild deployment, artifacts from the binary were used to connect the developer to postings on criminal forums related to carding, dating back to 2025."
    publisher: "Cisco Talos"
  - quote: "CLOSEDQUORUM represents a shift in effort displacement for attackers, in which expanding portions of the attack chain can be executed without operator involvement."
    publisher: "Cisco Talos"
  - quote: "CLOSEDQUORUM is, to our knowledge, the first publicly documented Windows implant to apply this model to tactical command and control (C2). After deployment, it delegates the selection of its next action to a panel of commercial large language models (LLMs) and executes the resulting decision, with the intent of harvesting user credentials and crypto wallets. It does not require continued commands from a human operator or tasking from a dedicated, attacker-operated C2 server; the complete dynamic operation is delegated to the AI."
    publisher: "Cisco Talos"
  - quote: "DeepSeek holds the deciding vote in any tie"
    publisher: "Cisco Talos"
verification: multi-source
sourcing_note: "Cisco Talos is the sole technical analyst of the CLOSEDQUORUM binary; The Hacker News' reporting restates Talos's findings and adds its own editorial framing (the LAMEHUG comparison) rather than independently re-analysing the malware, so this is one assessor with a second publisher for corroboration purposes."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Cisco Talos disclosed CLOSEDQUORUM on 2026-09-22, a 16.4MB, 64-bit Go-compiled Windows implant it says is "the first publicly documented Windows implant to apply this model to tactical command and control" ([Cisco Talos, 2026-09-22](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/)). Instead of a dedicated attacker-operated server, its `ModelOrchestrator` component queries up to four commercial LLM providers — DeepSeek, Qwen, Mistral and Google Gemini — each cycle, with a system prompt instructing each model to "provide ONLY executable decisions" alongside host context (hostname, OS version, admin status) and the current target process. Each provider must respond with a fixed JSON schema naming one of four actions; `interModelDiscussion()` tallies the providers' decisions by plurality vote and executes the winner, discarding any malformed or off-schema response. On a tie, a hardcoded preference order settles it: "DeepSeek holds the deciding vote in any tie" ([Cisco Talos, 2026-09-22](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/)), followed by Qwen and then Mistral; if every provider fails to return a usable decision, the implant sleeps and retries rather than falling back to a default action.

The four possible actions are `steal` (simultaneous LSASS memory dumping via `SeDebugPrivilege` and `MiniDumpWriteDump`, Chrome/Edge/Firefox saved-credential harvesting, and MetaMask/Exodus/Ethereum wallet data collection), `inject` (Early Bird APC injection into a suspended process by default, or PEB-walk process hollowing when a model selects that exploit type), `persist` (establishes three mechanisms — a Windows-Update-themed Registry Run-key value, a scheduled task, and a permanent WMI event subscription that fires a script every 60 seconds), and `move`, which has no handler in the public build. Independent of the LLM-selected action, the implant suppresses ETW telemetry by overwriting `EtwEventWrite` with a single RET instruction, blinding any host-side ETW consumer to its subsequent activity ([Cisco Talos, 2026-09-22](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/)). Every model decision, its stated reasoning, and staged or stolen data are relayed to the operator through a Discord webhook, with exfiltrated files AES-256-GCM encrypted, base64-encoded and posted in roughly 1,900-byte chunks at one-second intervals. Talos found the binary via CAIRN, an open-source research toolkit for tracking AI-integrated malware that it released the same day, and dates the analysed build to 2026-06-17 under a prior alias, BALZAK, before it was renamed on 2026-07-03. Talos's CAIRN toolkit is unrelated to a similarly-named autonomous exploitation engine used in separate, unrelated 2026 campaigns — the shared name is coincidental. Talos states plainly "we do not have confirmation of in-the-wild deployment," though artifacts in the binary connect its developer to carding-forum postings dating back to 2025 ([Cisco Talos, 2026-09-22](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/)). The publicly distributed build ships with placeholder API keys and a dummy Discord webhook, so Talos has not observed a complete end-to-end execution; Talos assesses the actual distribution model puts a developer generating a customised binary with an individual operator's credentials injected at compile time, meaning any live deployment would run on infrastructure Talos has not seen.

Talos frames the finding as evidence of "effort displacement" — an entire phase of an intrusion handed to a model rather than merely AI-assisted tooling. The Hacker News, reporting on the disclosure, draws its own comparison to LAMEHUG, malware Ukraine's CERT-UA reported in July 2025 that asked an AI model to write commands for a task already set in its code, contrasting it with CLOSEDQUORUM asking the models to choose the task itself ([The Hacker News, 2026-09-23](https://thehackernews.com/2026/09/windows-malware-is-built-to-let-up-to.html)). The implant's failure modes are deterministic and, Talos notes, exploitable by defenders: provider refusals and rate limits, a fixed tie-break order, and a sleep-retry response to total provider failure rather than a default action.

**Detection:** the actionable signal is not a domain or IP to block, since the "C2 infrastructure" is the same commercial AI-provider endpoints thousands of legitimate applications call daily. The discriminator is co-occurrence: AI-service API traffic from a Windows binary with no legitimate reason to call multiple LLM providers within a short window, correlated with LSASS access, code injection into a suspended process, new WMI persistence, or Discord webhook traffic from the same host or process, recurring at a randomised 5-to-15-minute polling cadence chosen to outlast short sandbox runs. Prompt content itself is visible only with TLS inspection or at the provider side; a network-only vantage point sees the fact of repeated multi-provider calls, not their content. **Triage:** legitimate software may independently call one AI-provider API; a single Windows process contacting several distinct commercial LLM providers in the same short window, especially alongside credential-access or injection telemetry, is not a pattern ordinary applications produce.

**Defender takeaway:** CLOSEDQUORUM is a capability demonstration with no confirmed live deployment, not an active campaign — but its architecture (commercial AI endpoints as C2, LLM-driven action selection) is a detection blind spot worth building hunt logic for now, before a deployed variant with real credentials appears. Prioritise correlating outbound AI-provider API traffic from endpoint processes against LSASS-access, injection and WMI-persistence telemetry rather than attempting to blocklist AI-service domains that legitimate tools also use.
