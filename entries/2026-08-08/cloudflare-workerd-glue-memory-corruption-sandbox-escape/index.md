---
schema: 1
kind: research
title: "Check Point breaks out of Cloudflare's Code Mode sandbox through a use-after-free in workerd's native glue — prompt injection to native host code, and a cross-tenant heap read"
headline: "Five bugs in the C++ layer between JavaScript and native code turn an agent prompt injection into host execution"
summary: >
  Check Point Research disclosed five vulnerabilities in workerd, the open-source C++/V8 runtime behind
  Cloudflare Workers and Cloudflare Code Mode, at Black Hat USA 2026 — four of them memory-corruption bugs
  and one a SQL authorization bypass reaching arbitrary deserialization. They sit in the native
  glue layer marshalling data between JavaScript and native code — an out-of-bounds read in URLPattern from
  a capture-group-count mismatch with V8's regex engine, and use-after-frees in node:zlib deflateParams()
  and HTMLRewriter's AttributesIterator. Two chains were demonstrated: a cross-tenant heap read, and a
  sandbox escape starting from prompt injection into Code Mode. Cloudflare has fixed its managed environment;
  self-hosted deployments need workerd v1.20260619.1. No CVEs were assigned.
discovered_at: "2026-08-08T05:13:00Z"
event_date: "2026-08-06"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cloud, ai-abuse, rce, patch-available]
regions: [global]
sectors: [technology, public-sector, telco, finance]
entities: []
techniques: [T1611, T1190]
affected_products: ["Cloudflare Workers", "Cloudflare Code Mode", "workerd"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/when-agentic-glue-melts/"
    publisher: "Check Point Research"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "Because workerd underpins both Code Mode sandboxes and Workers tenant isolation, the findings create sandbox-escape and cross-tenant exposure risk."
    publisher: "Check Point Research"
  - quote: "Self-hosted workerd / Code Mode deployments should update to v1.20260619.1."
    publisher: "Check Point Research"
  - quote: "As of now, Cloudflare has not assigned CVEs."
    publisher: "Check Point Research"
verification: single-source
sourcing_note: "Check Point Research's own coordinated disclosure; Cloudflare's remediation is quoted inside the Check Point article rather than published in an independently retrievable Cloudflare advisory, and this run could not reach Cloudflare's own security-advisories listing to confirm it separately. No CVE identifiers exist to cross-check against."
confidence: high
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
  - "If you run self-hosted workerd or Code Mode rather than Cloudflare's managed platform, update to v1.20260619.1 — there is no CVE to catch this in a scanner feed and no advisory will arrive through vulnerability-management tooling."
migrated_from: null
---

The interesting part of Check Point Research's Black Hat disclosure is where the bugs are, not how many there are. All five sit in workerd's own native code — four of them memory-corruption defects in the "glue" layer — the C++ code that marshals data between JavaScript and native implementations — which is the seam that every isolate-based multi-tenant runtime depends on and that JavaScript-level reasoning about sandbox safety does not cover ([Check Point Research, 2026-08-06](https://research.checkpoint.com/2026/when-agentic-glue-melts/)).

Three are worth naming for what they say about the class. An out-of-bounds read in the URLPattern implementation arises from a mismatch between the capture-group count workerd's own parser computes and the count V8's regex engine actually produces. Two use-after-frees come from native-object lifetime management: one in `node:zlib`'s `deflateParams()`, one in HTMLRewriter's `AttributesIterator`. The fifth is not a memory-corruption bug at all: a SQL authorization bypass in the Durable Objects storage path that Check Point calls "a classic that leads to arbitrary deserialization" ([Check Point Research, 2026-08-06](https://research.checkpoint.com/2026/when-agentic-glue-melts/)).

Two chains were demonstrated, and the second is the reason this belongs in an operational brief rather than a conference recap. The first is a cross-tenant heap read: one Worker reaching across the shared process heap to read a co-located tenant's secrets. The second starts from a prompt injection into Code Mode — Cloudflare's LLM tool-use feature — and rides the zlib use-after-free out of the V8 isolate into native code execution on the host. Check Point's own framing is that "Because workerd underpins both Code Mode sandboxes and Workers tenant isolation, the findings create sandbox-escape and cross-tenant exposure risk" ([Check Point Research, 2026-08-06](https://research.checkpoint.com/2026/when-agentic-glue-melts/)).

That chain is a concrete instance of something the AI-security discussion usually leaves abstract. Prompt injection is generally reasoned about as a content problem — the model can be made to say or request the wrong thing — with the sandbox as the backstop that bounds the damage. Here the model-controlled code is the input that reaches a memory-corruption bug in the sandbox itself, so the backstop is what fails. Exploitation still requires getting attacker-chosen JavaScript to run inside a Worker, which in the managed platform means being a tenant, and in the Code Mode case means steering the model.

Remediation is uneven in a way that matters. Cloudflare's managed Workers environment has been fixed in production, but "Self-hosted workerd / Code Mode deployments should update to v1.20260619.1", and "As of now, Cloudflare has not assigned CVEs" ([Check Point Research, 2026-08-06](https://research.checkpoint.com/2026/when-agentic-glue-melts/)). Check Point released proof-of-concept code as part of the presentation. For most readers the managed fix means no action; for anyone running workerd themselves the absence of a CVE means no scanner, SBOM tool or advisory feed will surface this — the version check has to be made deliberately. No in-the-wild exploitation is reported.

**Triage:** no host-side detection concept follows from what is published — the exploitation is in-process inside a runtime that does not expose per-isolate telemetry to its operators, and Check Point describes no post-exploitation artifact. The honest operational content here is the version check and the design lesson, not a hunt.
