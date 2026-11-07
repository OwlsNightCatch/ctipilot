---
schema: 1
kind: research
title: "Cisco Talos: malware now embeds natural-language instructions aimed at LLM triage pipelines, from a copied comment to template-sprayed prompts across four families, and a Russia-aligned group uses it too"
headline: "Talos: malware tells the analysing LLM to skip it; the text is plain and therefore detectable"
summary: >
  Cisco Talos documents 84 samples from four malware families, collected from January 2025 to July 2026, that embed plain
  natural-language text meant to steer the LLM stage of automated triage: a verbatim "no need to analyze this file" comment
  reused by at least four actors, templated variants, instructions repeated across seven chat-template formats, and
  intimidation or fabricated-authority text. ESET separately found UAC-0099 using a decoy request in a script comment to trip
  an LLM scanner's refusal; Talos' own test of five local models put the best techniques at steering the outcome in the
  attacker's favour in about 35% of runs, and its advice is to treat text inside a sample as evidence, never as instruction.
discovered_at: "2026-10-09T03:44:00Z"
updated_at: null
event_date: "2026-10-08"
run_id: 2026-10-09T0255Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [global]
sectors: []
entities: ["tool:cairn-talos", "actor:uac-0099"]
techniques: [T1027, T1059.001]
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/"
    publisher: "Cisco Talos"
    date: "2026-10-08"
    role: primary
  - url: "https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/"
    publisher: "ESET"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "malware that embeds natural-language instructions to influence automated analysis"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/"
  - quote: "Legitimate software has no reason to embed instructions telling an analyzer to refuse analysis, invoke copyright law, or claim government contracts."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/"
  - quote: "no single LLM engine should have the sole authority to decide that a piece of code is safe"
    publisher: "ESET"
    source_url: "https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/"
verification: multi-source
sourcing_note: >
  Talos' counts and effect rates come from its own test of five local language models; ESET documents the UAC-0099 case
  independently.
confidence: high
references:
  - "2026-06-26/macos-gaslight-a-dprk-aligned-rust-backdoor-that-targets-the"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Talos, which tracks AI-integrated malware in its CAIRN toolkit, calls the class "AI-analysis evasion": malware that embeds natural-language instructions to influence automated analysis, aimed at the layer above packers and anti-debug checks, the pipeline that extracts text from a sample and submits it to a language model for triage, classification or reverse-engineering help ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)). It traces four families and 84 samples collected from January 2025 to July 2026: a PowerShell reverse shell (FRUITSHELL) carrying a two-line comment that says there is no need to analyze the file, a comment later reused verbatim in nine further scripts from at least four actors, among them a script set that adds an AMSI bypass and runtime compilation ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)). PLOTSAFE generates the sentence from a template and keeps it alive in Go builds with a dummy function that references the strings; HOLLOWCLAD repeats one refusal instruction across seven LLM chat-template formats so one copy may match the scanner's own template, and adds fake honeypot and licence warnings; MANTLEMAZE claims invented government contracts and certifications ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)).

ESET found the technique in the hands of a named group: the Russia-aligned UAC-0099 put a decoy request for guidance on building a nuclear weapon into the comment of a VBScript, aiming to trip the safety guardrails of an LLM-powered code scanner so it stops before the malicious code that downloads the MATCHBOIL loader ([ESET, 2026-09-10](https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/)). Talos tested the strings against five local models, 135 matched pairs per string: its headline figure is that the best techniques steered the outcome in the attacker's favour in about 35% of runs, a net rate (pairs shifted toward benign minus pairs shifted toward malicious, over all pairs), while the cheapest technique, a direct instruction to ignore the sample, worked almost universally and the more complex ones had little effect or backfired by making models more suspicious; Talos calls the overall impact a mixed bag ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)). It says core conventional detection is unaffected ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)).

**Exposure:** a SOC or sandbox pipeline that passes strings, comments or decompiled code from a sample to a language model and acts on the verdict or on a refusal ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)).

**Detection:** the evasion text has to be plaintext, so imperative language addressed to an analysis system inside a binary or script is itself a stable signal; extracted strings and script comments are the telemetry class to search ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)).

**Triage:** Talos' discriminator is that legitimate software has no reason to embed instructions telling an analyzer to refuse analysis, invoke copyright law or claim government contracts ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)).

**Defender takeaway:** build triage prompts so text inside a sample is evidence and never instruction, with the boundary explicit ([Cisco Talos, 2026-10-08](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/)); no single model should decide that code is safe, and a model that returns nothing should trigger further checks ([ESET, 2026-09-10](https://www.welivesecurity.com/en/business-security/guardbreaker-derailing-ai-assisted-malware-analysis-code-comment/)).
