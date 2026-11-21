---
schema: 1
kind: vulnerability
title: "isolated-vm sandbox escape (GHSA-864f-rcv7-6rh4): a TOCTOU type-confusion in ExternalCopy's transferList marshaling breaks the V8 Isolate guest/host boundary — the sandbox underneath a wide range of AI-agent and low-code automation platforms"
headline: "The V8 Isolate held; the code that carries data across it did not, and a guest can turn that into full host control-flow hijacking"
summary: >
  Endor Labs found a type-confusion vulnerability in isolated-vm, the Node.js sandboxing library
  (1M+ weekly downloads) that gives untrusted JavaScript its own V8 Isolate. A time-of-check-to-
  time-of-use flaw in ExternalCopy's transferList marshaling lets a guest use a getter to swap a
  validated ArrayBuffer for an attacker-chosen value on a second, unchecked read, yielding a
  controlled-address read/write primitive and full guest-to-host escape. No CVE assigned yet;
  fixed in isolated-vm 7.0.1 and 6.2.0.
discovered_at: "2026-08-28T05:42:00Z"
updated_at: null
event_date: "2026-08-08"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, priv-esc, patch-available, ai-abuse]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1611]
affected_products: ["isolated-vm (npm package)", "n8n", "Activepieces", "Mastra AI", "Budibase", "Sim.ai", "Directus", "Rocket.Chat"]
cves: []
sources:
  - url: "https://github.com/laverdet/isolated-vm/security/advisories/GHSA-864f-rcv7-6rh4"
    publisher: "GitHub Security Advisory (isolated-vm maintainer)"
    date: "2026-08-08"
    role: primary
  - url: "https://www.endorlabs.com/learn/ghsa-864f-rcv7-6rh4-critical-type-confusion-vulnerability-in-isolated-vm"
    publisher: "Endor Labs"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "As <ArrayBuffer>() is not a checked conversion. It is a bare reinterpret-cast that tells V8, \"trust me, this is an ArrayBuffer.\" The code assumes it is safe because walk 1 already checked, but that assumption only holds if the two walks see the same values."
    publisher: "Endor Labs"
  - quote: "We did not break the V8 Isolate. We broke the code that carries data into it."
    publisher: "Endor Labs"
  - quote: "The maintainer responded quickly and shipped a fix in versions 7.0.1 and 6.2.0. The patch wraps ExternalCopy::Copy in a v8::Isolate::DisallowJavascriptExecutionScope, which prevents any user JavaScript (getters, proxies, interceptors) from running during the copy."
    publisher: "Endor Labs"
verification: multi-source
sourcing_note: >
  Confirmed directly against both the GitHub Security Advisory (the maintainer's own record) and
  Endor Labs' independent technical analysis, satisfying two-source verification without a CVE
  identifier — GHSA-864f-rcv7-6rh4 is the only identifier assigned as of this run, and the OSV API
  404s on it per the discovering team's own report.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade isolated-vm to 7.0.1 (mainline) or 6.2.0 (6.x backport) on any self-hosted platform that uses it as a code-execution sandbox — n8n, Activepieces, Mastra AI, Budibase, Sim.ai, Directus and Rocket.Chat are all named production consumers — and treat any AI-agent or workflow-automation deployment that executes model- or user-generated code through this library as exposed until confirmed patched."
updates: []
migrated_from: null
---

isolated-vm gives each untrusted-JavaScript sandbox its own V8 Isolate — a separate heap with no shared object graph with the host, the same primitive Chrome uses to separate tabs. Endor Labs (credited discoverer, no CVE assigned as of this run) found that the isolation primitive itself held; what broke is the C++ marshaling code that copies values across the boundary: "we did not break the V8 Isolate. We broke the code that carries data into it" ([Endor Labs, 2026-08-20](https://www.endorlabs.com/learn/ghsa-864f-rcv7-6rh4-critical-type-confusion-vulnerability-in-isolated-vm)).

`ExternalCopy`'s `transferList` option — a `postMessage`-style zero-copy ArrayBuffer transfer — walks the transfer-list array twice in `src/external_copy/serializer.cc`: the first walk validates each element with `IsArrayBuffer()` and registers it; the second performs an unchecked `handle.As<ArrayBuffer>()` reinterpret-cast with no re-validation. Because `transfer_list` is a real JavaScript array and both walks read it via a genuine property access that invokes JS accessors, a guest can define `transferList[0]` as a getter that returns a real ArrayBuffer on the first read — satisfying walk 1's check — and an attacker-chosen value on the second read; the unchecked cast then treats that value as an ArrayBuffer, yielding a controlled-address read/write primitive: "As <ArrayBuffer>() is not a checked conversion. It is a bare reinterpret-cast that tells V8, 'trust me, this is an ArrayBuffer.' The code assumes it is safe because walk 1 already checked, but that assumption only holds if the two walks see the same values" ([Endor Labs, 2026-08-20](https://www.endorlabs.com/learn/ghsa-864f-rcv7-6rh4-critical-type-confusion-vulnerability-in-isolated-vm)). Endor Labs escalated this from a single `ivm.Reference` — the minimum capability any embedder must hand a sandbox for it to do anything at all — to full host control-flow hijacking, demonstrating a complete guest-to-host escape.

Fixed in 7.0.1 (mainline) and 6.2.0 (6.x backport), both released 2026-08-08, by wrapping `ExternalCopy::Copy` in a `v8::Isolate::DisallowJavascriptExecutionScope` that prevents any guest JS — getters, proxies, interceptors — from running during the copy, closing the time-of-check-to-time-of-use window outright: "the maintainer responded quickly and shipped a fix in versions 7.0.1 and 6.2.0. The patch wraps ExternalCopy::Copy in a v8::Isolate::DisallowJavascriptExecutionScope, which prevents any user JavaScript (getters, proxies, interceptors) from running during the copy" ([Endor Labs, 2026-08-20](https://www.endorlabs.com/learn/ghsa-864f-rcv7-6rh4-critical-type-confusion-vulnerability-in-isolated-vm)).

isolated-vm (1M+ weekly downloads) is the sandbox of record for a wide range of AI-agent and automation platforms that execute model- or user-generated code: Endor Labs names n8n (which recommends isolated-vm for its Code-node task runners), Activepieces, Mastra AI (its "code mode" tool-orchestration execution), Budibase (which migrated off the deprecated vm2), Sim.ai, Directus and Rocket.Chat as production consumers whose guest/host boundary is this exact library. The absence of a CVE identifier does not soften the exposure: an anonymous, single-call escape from the isolation primitive that a widely-deployed class of self-hosted automation platforms advertises as its safety boundary is the class of flaw that demands action ahead of a routine patch cycle regardless of a formal severity score.

**Triage:** any self-hosted platform advertising sandboxed code execution via isolated-vm should confirm its patched version directly — a version check against the platform's own release notes rather than against isolated-vm's version alone, since embedders bundle it at different cadences. There is no telemetry-side discriminator for this flaw once patched; the mitigation is entirely upgrade-based, since the vulnerable code path executes inside the sandbox implementation itself rather than producing an externally observable behavioral signature before the escape completes.
