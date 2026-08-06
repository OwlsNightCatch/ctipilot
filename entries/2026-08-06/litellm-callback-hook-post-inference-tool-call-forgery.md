---
schema: 1
kind: research
horizon: operational
title: "LiteLLM callback hooks let an attacker who already holds gateway admin forge tool calls after inference — downstream of every prompt-level defence"
headline: "The AI gateway's own extension points become the tamper surface, and reverting the config removes the evidence"
summary: >
  Research published under the handle wunderwuzzi on 2026-08-03 and taken up in a Cloud Security Alliance research note on
  2026-08-05 describes a post-compromise technique against LiteLLM, the open-source gateway many organisations put
  in front of OpenAI, Anthropic, Gemini and Bedrock model calls. An attacker holding gateway-admin credentials uses
  the legitimate model-update management API to point a model's api_base at infrastructure they control, then abuses
  LiteLLM's own post-call callback hooks to inject text or forge tool calls into responses after the model has
  already produced them — which defeats prompt-level defences entirely because the manipulation happens downstream
  of inference. Reverting the configuration afterwards removes the most visible artifact, so the detection burden
  falls on audit logging of management-API changes rather than on inspecting model output.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-08-03"
run_id: 2026-08-06T0411Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, identity, cloud]
regions: [global]
sectors: [technology, public-sector, finance]
entities: []
techniques: [T1557, T1565.002]
affected_products: ["LiteLLM"]
cves: []
sources:
  - url: "https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/"
    publisher: "Embrace The Red (wunderwuzzi)"
    date: "2026-08-03"
    role: primary
  - url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/"
    publisher: "Cloud Security Alliance — Lab Space"
    date: "2026-08-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "forge a tool call that was never produced by the underlying model"
    publisher: "Cloud Security Alliance — Lab Space"
  - quote: "bypasses prompt-level defenses entirely"
    publisher: "Cloud Security Alliance — Lab Space"
verification: multi-source
sourcing_note: >
  The original technique disclosure is the wunderwuzzi post of 2026-08-03, which falls two days outside this run's
  recency window; the in-window item is the Cloud Security Alliance research note of 2026-08-05, which restates and
  extends the same research with detection and hardening framing rather than independent new testing. event_date
  records the original disclosure so the reader is not misled about freshness. It is carried now because the
  technique has not been covered here before and is not tied to a patch cycle — there is no CVE and no fixed
  version, only a configuration and logging posture.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Turn on audit logging for LiteLLM's management API if it is not already recording, and alert on any change to a model's api_base or proxy setting — that configuration write is the one step of this chain that must happen before anything else and the one the attacker later reverts."
migrated_from: null
---

An attacker who already holds administrative access to a LiteLLM proxy — through leaked master-key or proxy-admin credentials, a prior vulnerability chain, or a supply-chain compromise — can use the gateway's legitimate model-update management API to change a model's configured backend address, silently routing that model's traffic through infrastructure they control and exposing the provider API keys that resolve at request time ([Cloud Security Alliance, 2026-08-05](https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/)). With traffic rerouted, the interesting part is what the relay does next: it abuses LiteLLM's own post-call callback hooks, the extension points the platform provides for logging and response processing, so that an attacker in control of these hooks can inject arbitrary text into a response or, more consequentially, forge a tool call that was never produced by the underlying model ([Cloud Security Alliance, 2026-08-05](https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/)). The technique originates in research published two days earlier under the handle wunderwuzzi ([Embrace The Red, 2026-08-03](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/)).

The consequence worth internalising is architectural rather than novel-exploit. Because the manipulation happens after the model has already generated its output, it bypasses prompt-level defenses entirely ([Cloud Security Alliance, 2026-08-05](https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/)). Every control an organisation has invested in at the prompt layer — system-prompt hardening, input filtering, injection detection, guardrail models — sits upstream of the tamper point and cannot see it. If the agent downstream of the gateway acts on tool calls, a forged tool call is an instruction to act, and it arrives carrying the gateway's own authenticity.

This is post-compromise, and that framing should govern how urgently it is treated: it is not a way in, it is what a foothold on the gateway is worth. But it inverts a common assumption about AI-agent architecture, in which the gateway is treated as plumbing and its admin credential as ordinary application configuration. On this evidence the gateway is a control-plane component whose compromise is not contained by anything downstream of it. The reporting also notes that a capable attacker reverts the rerouted configuration once finished, which removes the most visible artifact of the compromise ([Cloud Security Alliance, 2026-08-05](https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/)) — so a point-in-time configuration review is exactly the check that will come back clean.

**Defender takeaway:** treat LiteLLM gateway-admin credentials and the master key as Tier 0 secrets on the same footing as directory-administrator credentials — vault-backed, rotated, and restricted to a management path rather than held in application configuration. Detection rests on the management API rather than on model behaviour: log every configuration-changing call, alert on changes to a model's backend address, and hold those logs somewhere the gateway administrator cannot edit, because the revert is part of the technique. Egress from the gateway host to model-provider endpoints is a second, independent check — the gateway should talk to a known set of provider addresses, and a rerouted model shows up as a new destination even when the configuration has been put back.

**Triage:** legitimate operations change model configuration too — adding models, moving between regions, failing over to a secondary provider. The discriminators are that the change is made outside a deployment pipeline or change window, that the new backend address is not one of the organisation's known provider or proxy endpoints, and above all that the configuration is changed and then changed back within a short interval, which is not a shape ordinary operational work produces.
