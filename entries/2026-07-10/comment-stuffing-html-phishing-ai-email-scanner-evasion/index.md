---
schema: 1
kind: research
title: "'Comment stuffing' — HTML phishing attachments padded to ~2.5 MB to dilute or exhaust AI/NLP email scanners"
headline: "SANS ISC: a phishing page pads itself with ~430k repeated characters to dilute the payload below an AI classifier's threshold or exhaust an LLM's token budget"
summary: >
  A SANS Internet Storm Center diary analysed a phishing email whose HTML attachment was ~2.5 MB but
  whose functional credential-harvesting payload was only ~11 KB — the remainder a single HTML comment
  of ~430,000 repeated "X" characters placed after the payload. The analyst assesses the padding is
  aimed at AI/NLP-based email security: either diluting the malicious content's statistical weight
  until a probability classifier drops below its flag threshold, or inflating the token count until an
  LLM-based scanner exceeds its per-message time/size budget and cuts analysis short. The concept
  matters as AI content-scoring spreads across public-sector mail gateways; the defence is a non-AI
  fallback rule keyed on the anomalous oversized-single-character-run signature.
discovered_at: "2026-07-10T12:53:00Z"
event_date: "2026-07-10"
run_id: 2026-07-10T1228Z-intel
priority: notable
immediate_action: null
tags:
  - phishing
  - ai-abuse
regions:
  - global
sectors:
  - public-sector
  - finance
  - healthcare
  - energy
  - telco
entities: []
techniques: [T1566.001, T1027]
affected_products: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33144"
    publisher: "SANS Internet Storm Center"
    date: "2026-07-10"
    role: primary
closed_sources: []
evidence:
  - quote: "If a message contains enough innocuous material, the weight of the malicious portion can be diluted to the point where the model no longer flags it with sufficient confidence."
    publisher: "SANS Internet Storm Center"
  - quote: "The same bulk can also make a message large enough so that scanning it using AI-based mechanisms takes too long, leading some solutions to release it rather than delay delivery indefinitely."
    publisher: "SANS Internet Storm Center"
  - quote: "The padding is also about as low-entropy as any data can get, which means it wouldn’t help the file blend in with benign content on a statistical level either"
    publisher: "SANS Internet Storm Center"
verification: single-source
sourcing_note: >
  Single-source (SANS Internet Storm Center diary, reliability B — reputable research/handler community)
  and a single observed sample. The "designed to evade AI scanners" framing is the handler's explicitly
  hedged assessment ("informed speculation"), building on KnowBe4's earlier "NLP obfuscation" write-up,
  not a confirmed campaign attribution. Classification B3 (credibility 3 — plausible, hypothesis-level,
  uncorroborated). Included as developing tradecraft with a concrete, mechanism-independent detection concept.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions:
  - "Add a non-AI fallback rule to the mail gateway that flags HTML/XLS-disguised attachments containing an oversized single-repeated-character run or an HTML comment above a size threshold (e.g. >50 KB of one repeated character) — a signature independent of whatever AI/NLP scoring the gateway also runs, so the control does not fail when the classifier is drowned."
  - "Pre-process attachments to strip or truncate oversized comments/padding before AI-based scoring, and alert on large decompressed-vs-declared-size ratio outliers, so a padded payload is scored on its functional content rather than released on a timeout."
migrated_from: null
---

A SANS Internet Storm Center diary (2026-07-10, Jan Kopriva) dissects a phishing email that presented as a Microsoft Teams/SharePoint document notification and carried a `.xls.html` double-extension attachment weighing ~2.5 MB — anomalously large for a self-contained HTML page ([SANS ISC, 2026-07-10](https://isc.sans.edu/diary/33144)). Decoded from a `\uXXXX`-escaped `document.write()` wrapper, the file was ~431 KB, of which only the first ~11 KB was a working SharePoint-themed credential-harvesting page; the rest was a single HTML comment holding roughly 430,000 repeated "X" characters, placed *after* the functional payload, accounting for ~97% of the file.

The placement rules out the classic goal. Padding after the payload does nothing to conceal the malicious code, and at 2.5 MB the file falls well short of the tens-of-megabytes scan-size limits modern mail security uses, so this is not the MITRE "Binary Padding" scan-size-evasion play. The handler's assessment — explicitly flagged as informed speculation — is that the target is AI/NLP-based content scanning, which a growing number of gateways now run. Citing KnowBe4's earlier "NLP obfuscation" work, the diary notes that "if a message contains enough innocuous material, the weight of the malicious portion can be diluted to the point where the model no longer flags it with sufficient confidence", and that "the same bulk can also make a message large enough so that scanning it using AI-based mechanisms takes too long, leading some solutions to release it rather than delay delivery indefinitely" ([SANS ISC, 2026-07-10](https://isc.sans.edu/diary/33144)). The author judges the token-budget-exhaustion goal the more likely of the two here, since a featureless block of one character works as well as crafted filler for that purpose. He is candid that against a well-tuned model the tactic is blunt — "the padding is also about as low-entropy as any data can get, which means it wouldn't help the file blend in with benign content on a statistical level either" — which is precisely why a simple non-AI signature catches it.

**Defender takeaway:** as AI/NLP scoring becomes a load-bearing control in mail security, adversaries gain an incentive to attack the classifier's decision budget rather than hide from signatures — dilution below a confidence threshold, or token-count inflation past a per-message time budget that makes the gateway fail open. **Triage:** benign HTML mail and marketing content can be large, but a single repeated-character run or one HTML comment in the hundreds of kilobytes is not something legitimate senders produce — that oversized low-entropy block, and a large decompressed-vs-declared-size ratio, are the discriminators, and both are detectable without relying on the AI layer the padding is trying to defeat.
