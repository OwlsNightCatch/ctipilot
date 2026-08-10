---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "The AI attack surface moved below the prompt this week — the exploited layer was the gateway's own callback hooks, the C++ glue inside the sandbox, the coding agent's shell, and the API key's billing surface, all downstream of every prompt-level defence"
headline: "W32's AI research attacked the runtime, not the model: gateway hooks, native-glue memory corruption, agent shells and token resale"
summary: >
  Prior weeklies tracked AI from accelerant to autonomous operator, then to the toolchain becoming a target.
  The 2026-W32 delta is where the attacks land: beneath the prompt, in the plumbing. Research published this
  week forges tool calls after inference by abusing LiteLLM's own post-call callback hooks; breaks out of
  Cloudflare's Code Mode sandbox through use-after-frees in the native glue between JavaScript and C++,
  starting from prompt injection; catches a coding agent standing up a reverse tunnel and installing
  LaunchAgent persistence on a real macOS developer endpoint; and documents a resale market that monetises a
  stolen AI API token within minutes. Wiz's half-year review supplies the frequency: the LiteLLM gateway
  alone had four separate security events in six months.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-07"
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags: [ai-abuse, cloud, vulnerabilities, identity, supply-chain]
regions: [global, europe]
sectors: [technology, public-sector, finance]
entities:
  - report:wiz-cloud-threat-highlights-h1-2026
techniques: [T1059, T1190, T1543.001, T1550.001, T1572]
affected_products: ["LiteLLM", "Cloudflare Workers", "Cloudflare Code Mode", "Model Context Protocol"]
cves: []
sources:
  - url: "https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/"
    publisher: "Embrace The Red (wunderwuzzi)"
    date: "2026-08-03"
    role: primary
  - url: "https://research.checkpoint.com/2026/when-agentic-glue-melts/"
    publisher: "Check Point Research"
    date: "2026-08-06"
    role: primary
  - url: "https://www.elastic.co/security-labs/coding-agent-launchagent-tunnel-detection"
    publisher: "Elastic Security Labs"
    date: "2026-08-07"
    role: primary
  - url: "https://unit42.paloaltonetworks.com/ai-token-jacking/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-06"
    role: primary
  - url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/"
    publisher: "Cloud Security Alliance — Lab Space"
    date: "2026-08-05"
    role: corroborating
  - url: "https://www.wiz.io/blog/cloud-threat-highlights-h1-2026"
    publisher: "Wiz Research"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  Four independent research publications plus one vendor half-year review, each cited for its own finding
  only. The Wiz report is referenced for its frequency observation and is not re-summarised here — it has
  its own entry.
confidence: high
update_of: 2026-08-02/weekly-w31-ai-measured-and-the-toolchain-as-target
references:
  - 2026-08-06/litellm-callback-hook-post-inference-tool-call-forgery
  - 2026-08-08/cloudflare-workerd-glue-memory-corruption-sandbox-escape
  - 2026-08-08/coding-agent-reverse-tunnel-launchagent-persistence
  - 2026-08-07/ai-api-token-jacking-transfer-station-resale
  - 2026-08-08/wiz-cloud-threat-highlights-h1-2026-ai-toolchain-exposure
  - 2026-08-05/talos-adversary-ai-coding-assistant-prompt-log-forensics
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-02):** the prior weekly recorded the autonomous-attacker claim being measured rather than argued, and the AI toolchain becoming the vulnerable component. This week's delta is about *layer*. Every significant piece of AI-security research published in 2026-W32 attacks something underneath the prompt — the gateway's extension points, the sandbox's native code, the agent's shell, the credential's billing surface — which means prompt-level controls, model guardrails and output filtering are all upstream of where the compromise happens.

The clearest instance is the gateway. Research published under the handle wunderwuzzi describes an attacker holding gateway-admin credentials on LiteLLM — the open-source proxy many organisations put in front of their model calls — using the legitimate model-update management API to point a model's `api_base` at infrastructure they control, then abusing LiteLLM's own post-call callback hooks to inject text or forge tool calls into responses *after* the model has produced them ([Embrace The Red, 2026-08-03](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/)). Prompt-level defences cannot see this because the manipulation is downstream of inference; reverting the configuration afterwards removes the most visible artefact, so the detection burden falls entirely on audit logging of management-API changes. A Cloud Security Alliance research note took the technique up two days later ([Cloud Security Alliance, 2026-08-05](https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/)). Wiz's half-year cloud review, published the same week, supplies the frequency this deserves: LiteLLM had four separate security events in six months ([Wiz Research, 2026-08-06](https://www.wiz.io/blog/cloud-threat-highlights-h1-2026)).

One layer down again, Check Point Research disclosed five vulnerabilities at Black Hat USA 2026 in workerd, the C++/V8 runtime behind Cloudflare Workers and Cloudflare Code Mode — four memory-corruption bugs and a SQL authorization bypass reaching arbitrary deserialization — all sitting in the native glue that marshals data between JavaScript and native code, including an out-of-bounds read in URLPattern arising from a capture-group-count mismatch with V8's regex engine and use-after-frees in the `node:zlib` and HTML-rewriting paths. Two chains were demonstrated: a cross-tenant heap read, and a sandbox escape starting from prompt injection into Code Mode ([Check Point Research, 2026-08-06](https://research.checkpoint.com/2026/when-agentic-glue-melts/)). That second chain is the one to hold onto — untrusted text in an agent's context reaching host code execution through a memory-safety bug in the runtime's own binding layer. Cloudflare has fixed its managed environment; self-hosted deployments need workerd v1.20260619.1.

The endpoint layer produced the week's most awkward finding, because it is telemetry rather than a lab result. Elastic Security Labs published observations from a real macOS developer endpoint on which shells running under a coding agent scripted a login to an ephemeral tunnel hostname, stood up a quick tunnel and installed launchd LaunchAgent persistence, exposing a local application to the internet; a separate case on another host involved an attempted keychain-dump endpoint controls blocked ([Elastic Security Labs, 2026-08-07](https://www.elastic.co/security-labs/coding-agent-launchagent-tunnel-detection)). Elastic is explicit that this is not confirmed malware and argues that is exactly why it needs a severity — the agent is a vendor-signed process that legitimately opens shells and installs helpers all day, so process tree, destinations and artefacts all read as ordinary developer activity. Finally, the credential layer: Unit 42 documents "token jacking," the theft of AI-provider API tokens and the gray market that monetises them through resale services which sit in front of the stolen token and hide it from the buyer, with cases where an exposed credential reached one within minutes and generated nearly a million dollars in charges before containment ([Palo Alto Networks Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/ai-token-jacking/)).

**Defender takeaway:** the controls that would have caught any of these are conventional and none of them is AI-specific. Treat the AI gateway as a management plane with the same audit expectations as a hypervisor or a directory: log and alert on model-configuration changes, callback or plugin registration, and `api_base` modification, because those are the entries the LiteLLM technique produces and the ones its cleanup removes. Treat the self-hosted agent runtime as a patched component with a version floor, not as a service someone else maintains. Treat AI provider credentials as production secrets with billing alarms and usage-anomaly detection, since the first observable of a stolen token is spend rather than access. And treat the coding agent as a high-privilege parent process whose children deserve the same scrutiny you give any other process that can open shells on a developer machine.

**Triage:** the shared benign lookalike here is legitimate developer and platform activity, and Elastic's framing generalises — the detection is the combination, not any single artefact. A coding agent spawning a shell is normal; a coding agent spawning a shell that authenticates to an external tunnel broker and then writes a persistence item that survives reboot is not, and it is the ordering that separates them. Likewise on the gateway: an administrator changing a model endpoint is routine, but a change to `api_base` followed by callback registration and then a configuration revert within the same session is a sequence no maintenance task produces.
