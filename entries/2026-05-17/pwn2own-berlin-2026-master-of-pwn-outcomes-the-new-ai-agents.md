---
schema: 1
kind: threat
horizon: operational
title: "Pwn2Own Berlin 2026: Master-of-Pwn outcomes, the new AI Agents category, and the compound-Exchange-threat picture for European defenders"
headline: "Pwn2Own Berlin 2026: Master-of-Pwn outcomes, the new AI Agents category, and the compound-Exchange-threat picture for European defenders"
summary: "Pwn2Own Berlin 2026 wraps — 47 unique zero-days, $1,298,250 awarded. DEVCORE's Orange Tsai chained three undisclosed Exchange bugs to SYSTEM-level unauthenticated RCE on Day 2 ($200K, 90-day embargo); STARLabs SG burned a memory-corruption ESXi hypervisor escape for another $200K on Day 3; the new AI Agents category produced exploits or collisions across all entered targets — OpenAI Codex (Compass Security CWE-150, $40K), Cursor (Compass Security, $15K), LM Studio (OtterSec code-injection Day 2; STARLabs SG separately ran an SSRF+code-injection 5-bug chain on Day 1), LiteLLM (k3vg3n SSRF+code-injection), with Claude Code, Chroma, Megatron Bridge and Ollama producing collisions (ZDI Day 3, 2026-05-16)."
discovered_at: "2026-05-17T05:00:06Z"
event_date: 2026-05-16
run_id: 2026-05-17-4381863a
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - zero-day
  - ai-abuse
  - supply-chain
  - cloud
regions:
  - europe
  - switzerland
  - global
sectors:
  - public-sector
  - technology
  - finance
  - healthcare
  - defense
entities:
  - "incident:pwn2own-berlin-2026"
cves: []
sources:
  - url: "https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn"
    publisher: "Zero Day Initiative — Day 3, 2026-05-16"
    role: primary
  - url: "https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results"
    publisher: "Zero Day Initiative — Day 2, 2026-05-15"
    role: corroborating
  - url: "https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results"
    publisher: "Zero Day Initiative — Day 1, 2026-05-13"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/"
    publisher: "BleepingComputer, 2026-05-15"
    role: corroborating
  - url: "https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/"
    publisher: "Hackread, 2026-05-16"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions:
  - "**Inventory AI agent / inference deployments on developer endpoints** (LM Studio, Ollama, LiteLLM, Cursor, OpenAI Codex, Claude Code, vLLM gateways) and apply network egress controls so the agent runtime cannot reach RFC-1918 internal ranges. Pwn2Own Berlin 2026 demonstrated `T1190 → T1090 → T1059` chains on every AI Agents target; SSRF-pivot to internal endpoints is the load-bearing technique. Require tool-plugin code signing where supported; ensure EDR coverage extends to the agent runtime processes (`node`, `python`, `electron` child processes spawned by agent UIs). Reference: § 5 deep dive — AI Agents section."
migrated_from: briefs/2026-05-17.md
---

**Background.** Pwn2Own Berlin (run alongside OffensiveCon, 2026-05-14 → 2026-05-16) is the second Berlin edition since Trend Micro / Zero Day Initiative moved the European event off the Vancouver-only schedule in 2025. It runs the standard Pwn2Own rules: original-research, full-chain, time-boxed in-room exploitation against current-patched production targets, with vendor-disclosure happening within minutes of a successful pop and a 90-day Pwn2Own embargo before ZDI publishes technical detail. The Berlin contest historically draws a heavier European researcher field than Vancouver — relevant this year because Swiss firm Compass Security fielded a five-researcher team and took prizes against multiple AI agent targets. Prior Pwn2Own competitions established the cadence: bugs popped in May surface as advisory-tagged CVEs in vendor August or September advisories. The May 2026 contest is meaningful for European public-sector defenders for three reasons covered below — the DEVCORE Exchange chain landing while CVE-2026-42897 is actively exploited, the new AI Agents category dragging dev-toolchain inference platforms into the public-vulnerability ecosystem, and the contest's capacity overflow which produced an unprecedented wave of *rejected-researcher* public PoC releases.

**Day-by-day outcomes — what was actually demonstrated.** Day 1 ([ZDI, 2026-05-13](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)): Orange Tsai (DEVCORE) opened the day with a four-bug Microsoft Edge sandbox escape for $175,000 — the day's biggest single award and the foundation of DEVCORE's eventual Master of Pwn victory; Compass Security exploited OpenAI Codex through a CWE-150 "improper neutralization of special elements" bug for $40,000 — the first publicly-known weaponised exploit of OpenAI's coding agent; Satoki Tsuji (Ikotas Labs) exploited NVIDIA Megatron Bridge via an overly permissive allowed-list bug for $20,000; Ikotas Labs separately collided against LiteLLM ($8,000 reduced reward); maitai (Doyensec) collided against OpenAI Codex ($10,000); Nguyen Thanh Dat (Viettel) collided against Claude Code ($20,000); k3vg3n landed an SSRF-plus-code-injection chain against LiteLLM (separate from the Ikotas Labs LiteLLM collision); Le Duc Anh Vu (Viettel) failed his attempt against Codex; STARLabs SG demonstrated a five-bug SSRF + code-injection chain against LM Studio. Day 2 ([ZDI, 2026-05-15](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)): the Exchange chain landed — Orange Tsai of DEVCORE chained three undisclosed bugs to unauthenticated SYSTEM RCE on a patched Exchange Server installation, earning $200,000 and a Master-of-Pwn step toward DEVCORE's overall victory; OtterSec popped LM Studio via a code-injection bug; 0xDACA / Noam Trobinski took the NVIDIA Container Toolkit via a use-after-free ($25,000); Compass Security took Cursor for an additional $15,000. Day 3 ([ZDI, 2026-05-16](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn); [Hackread, 2026-05-16](https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/)): STARLabs SG's Nguyen Hoang Thach burned a memory-corruption vulnerability for a full VMware ESXi hypervisor escape ($200,000, 20 Master-of-Pwn points); Windows 11 LPE chains landed; Compass Security attempted Claude Code but collided with a vulnerability ZDI already had on file. Master of Pwn final: DEVCORE 50.5 points / $505,000; STARLabs SG 25 points. Across three days: 47 unique zero-days, $1,298,250 paid out — ZDI's largest Berlin payout to date.

**Exchange — compounding the in-the-wild picture.** The DEVCORE three-bug chain attacks a different surface from CVE-2026-42897 (yesterday's deep dive) — OWA stored XSS is browser-context exploitation against authenticated users; the DEVCORE chain achieves SYSTEM-level direct RCE without authentication. Technique-class map: `T1190` Exploit Public-Facing Application → `T1059.003` Windows Command Shell → `T1068` Exploitation for Privilege Escalation, with the EWS / RPC / RemotePS attack surface as the most plausible target set given Orange Tsai's prior ProxyLogon / ProxyShell / ProxyNotShell work. Embargo window: ZDI rules require vendors to ship patches within 90 days; expect Microsoft advisories around 2026-08-14, possibly bundled into August Patch Tuesday. Operational implication for the next ~12 weeks: on-premises Exchange faces (a) the currently-exploited XSS without permanent patch, (b) an unpatched unauthenticated SYSTEM RCE class proven viable on hardened production builds, and (c) the residual ProxyShell/NotShell attack surface that the FamousSparrow Azerbaijani campaign covered in the 2026-05-14 deep dive showed is still being weaponised against unpatched installs. The defender posture published with the 2026-05-16 deep dive (verify EEMS service, monitor OWA access patterns, restrict ECP/EWS from the internet, accelerate Exchange Online migration where possible) becomes harder to argue against given the Pwn2Own evidence.

**AI Agents category — the new public-vulnerability surface for dev toolchains.** Pwn2Own Berlin 2026 was the first year ZDI ran an AI Agents track. The result across the AI-Agents and adjacent inference-stack targets — OpenAI Codex, Cursor, LM Studio, LiteLLM, Claude Code, Claude Desktop, Chroma, Megatron Bridge, Ollama — was that the entries either landed exploits or collided with bugs ZDI already had on file (the latter still confirms the vuln exists). The recurring pattern across LiteLLM, LM Studio, Cursor and the OpenAI Codex attempts is **agent-instruction-injection → server-side request forgery → arbitrary code execution**, mapped to `T1059.007` (JavaScript / scripting) and `T1090` (Proxy abuse) — the agent runtime takes adversary-supplied content (a tool invocation, a file the agent is asked to summarise, a URL), treats it as a privileged instruction, and either fetches an attacker-controlled resource SSRF-style from inside the corporate network or executes attacker-shaped code in the agent's runtime container. STARLabs SG's five-bug LM Studio chain (Day 1) and k3vg3n's LiteLLM chain (Day 1) both follow exactly that pattern — SSRF→code-injection. OtterSec's Day 2 LM Studio pop was a code-injection bug only (no SSRF prefix), demonstrating the same target falls to two distinct attack-class roots. The OpenAI Codex CWE-150 vulnerability Compass Security exploited centres on improper neutralisation of special characters in tool-invocation arguments. Defender concepts that translate without IOCs: (1) treat self-hosted inference services (Ollama, LM Studio, LiteLLM, vLLM gateways) as untrusted public-facing applications even when bound to localhost — they are reachable from any browser tab the developer opens; (2) constrain outbound egress from inference containers to only the model-update endpoints they need (RFC-1918-range alerts from agent containers are a high-signal SSRF indicator); (3) require code-signing on tool plugins loaded by Cursor / Codex / Claude Code; (4) inventory developer endpoints that have agent tooling installed and ensure EDR coverage extends to the agent's runtime processes — these are not yet routinely covered by SOC tooling baselines. For Swiss/EU public-sector environments specifically: agentic coding tools are entering federal and cantonal developer workflows ahead of any procurement-grade evaluation; the Pwn2Own results give a documented evidence base for SOC managers asking developer-tooling owners for inventory and egress controls.

**Capacity-overflow rejected-researcher PoC wave.** A distinctive feature of Berlin 2026: Pwn2Own contest slots filled before all submitted research could be staged. ZDI's response — public disclosure of full PoC chains by researchers whose submissions were rejected for slot reasons — produced an unprecedented PoC release wave covering Firefox full-chain RCE, additional Ollama / LM Studio exploitation, NVIDIA driver chains, and at least one researcher's Claude Code exploitation attempt. Operationally, defenders cannot rely on the standard Pwn2Own embargo for any of these — the technical detail is in the wild now. Browser/inference/dev-tool teams should monitor researcher Twitter/Mastodon disclosure channels and triage against their own deployment surface immediately rather than waiting for vendor advisories.

**Hardening / mitigation summary** (citing the contest blogs for each piece):
- **Exchange on-premises:** treat as severely threatened; verify EEMS M2.1.x; restrict OWA/ECP/EWS internet reachability; plan for an August Patch Tuesday emergency cycle when the DEVCORE embargo expires ([ZDI Day 2](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)).
- **VMware ESXi:** assume the hypervisor escape class is exploitable on hardened production builds until Broadcom ships a patch; restrict ESXi management network reach; monitor for atypical guest-to-host process spawn patterns ([ZDI Day 3](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)).
- **AI Agents (Codex / Cursor / LM Studio / LiteLLM / Claude Code):** treat inference containers as untrusted; egress-restrict to model-update endpoints; require tool-plugin code signing; inventory developer endpoints with agent tooling and ensure EDR coverage of agent runtime processes ([ZDI Day 1](https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results), [ZDI Day 2](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)).
- **Windows 11 LPE candidates:** track Patch Tuesday cadence ahead of August disclosure window; nothing actionable until vendors ship advisories ([ZDI Day 3](https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)).
