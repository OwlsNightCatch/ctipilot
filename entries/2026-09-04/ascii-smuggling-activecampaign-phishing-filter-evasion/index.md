---
schema: 1
kind: research
title: "ASCII smuggling crosses over from AI prompt-injection research into mainstream phishing-filter evasion"
headline: "Microsoft's own AI-prompt-injection hunting logic surfaced a 1.3-million-message phishing campaign hiding invisible characters inside lure keywords"
summary: >
  Microsoft Defender for Office 365's hunting signature for invisible Unicode Tags-block characters
  — built to catch AI prompt-injection attempts — instead surfaced a finance-themed phishing
  campaign that spliced the same invisible characters into lure keywords to defeat both literal
  keyword matching and the tokenization step of ML-based spam classifiers, relayed through the
  legitimate ActiveCampaign platform to launder sender reputation. Over 99% of messages were still
  caught by other layered defenses.
discovered_at: "2026-09-04T05:40:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-04T0410Z-intel
priority: notable
immediate_action: null
tags: [phishing, vulnerabilities]
regions: [global]
sectors: [public-sector]
entities:
  - "campaign:ascii-smuggling-activecampaign-finance-phishing-2026"
techniques: [T1566, T1027]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/"
    publisher: "Microsoft Security Blog / Microsoft Threat Intelligence"
    date: "2026-09-03"
    role: primary
closed_sources: []
evidence:
  - quote: "the day before onset (February 8) the signature fired on roughly 21,000 messages; the next day it fired on more than 1.3 million"
    publisher: "Microsoft Threat Intelligence"
  - quote: "the invisible tag characters were inserted inside common financial keywords, splitting them apart so that a literal signature or keyword match would fail"
    publisher: "Microsoft Threat Intelligence"
  - quote: "over 99% of messages were flagged by layers that did not depend on catching the tag characters directly"
    publisher: "Microsoft Threat Intelligence"
verification: single-source
sourcing_note: >
  Single-source: Microsoft Threat Intelligence is the sole assessor reporting this specific
  campaign, based on its own internal Defender for Office 365 telemetry. No independent lab has
  corroborated the finding; the underlying broader ActiveCampaign-relayed phishing infrastructure
  was separately documented earlier by Fortra, but that report predates the Unicode-tag technique
  this entry covers.
confidence: high
references: []
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

Microsoft Defender for Office 365's hunting signature for the Unicode Tags block (U+E0000-U+E007F) — deployed to catch invisible characters used to smuggle instructions to AI models while hiding them from human readers — instead surfaced a large-scale phishing-filter-evasion campaign using the same code-point range for an unrelated purpose. Hits on the signature jumped from roughly 21,000 messages on 2026-02-08 to over 1.3 million the next day, sustained on a strict weekday-only cadence for roughly three months before dropping sharply after 2026-05-15 ([Microsoft Threat Intelligence, 2026-09-03](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)). Roughly 96% of flagged volume traced to around 150 disposable finance-themed sender domains built by recombining a small vocabulary of tokens. Rather than hiding a full instruction payload, the campaign spliced a single invisible TAG SPACE character into the middle of high-signal lure keywords such as "funding" — defeating literal keyword and regex matching, and, more consequentially, disrupting the tokenization step of ML- and NLP-based spam classifiers: an unexpected code point mid-word can split a familiar token into unfamiliar sub-tokens the classifier has never seen. Mail was relayed through the legitimate email-marketing platform ActiveCampaign, whose link-rewriting laundered sender reputation so the URLs a recipient clicked pointed at ActiveCampaign's own tracking domains rather than the brand-impersonation domain shown in the message.

Microsoft states over 99% of flagged messages were still caught by layers that did not depend on the Unicode signal at all — sender, IP, URL and domain reputation, ML spam/phishing classification, brand-impersonation detection and authentication checks — but flags that Tag-block abuse is rarer than the more commonly-defended zero-width-space and non-breaking-space obfuscation classes, making it a plausible blind spot for any mail-filtering pipeline that does not normalize invisible Unicode before running content signatures. Microsoft's own filter stack separately runs OCR-based visual-text extraction as an available capability, which it notes could also catch this technique, but that layer is not part of the enumerated set behind the 99% figure.

**Defender takeaway:** any organisation running its own custom mail-filtering logic (rather than relying entirely on a vendor's built-in defenses) should strip or normalize Unicode Tags-block and other zero-width/invisible code points from subject and body text before applying spam or phishing content signatures — this campaign specifically targeted the gap between what a literal-match filter sees and what a human reader sees. **Triage:** the England, Scotland and Wales subdivision-flag emojis are legitimately encoded using the same Unicode Tags-block range (a base flag code point followed by an invisible tag-character sequence), and Microsoft's own first-pass signature false-positived on these before exclusion — any hunt built on Tag-block presence should carve out those three emoji sequences before treating the range as anomalous.
