---
schema: 1
kind: annual-report
title: "ESET Threat Report H1 2026: first Android malware using generative AI at runtime, ClickFix detections more than double, record QR-phishing, 100+ EDR-killers"
headline: "ESET Threat Report H1 2026: PromptSpy runs Gemini in its own execution flow, ClickFix 2x, QR-phishing at record levels, 100+ EDR-killers catalogued"
summary: >
  ESET's semi-annual threat report (Dec 2025–May 2026 telemetry) flags four items for a
  Tier 2/3 team: PromptSpy, described as the first Android malware to use generative AI
  (Google Gemini) at runtime to interpret UI and adapt behaviour; ClickFix detections more
  than doubling H2 2025→H1 2026 and expanding beyond fake CAPTCHA into AI-help-page and
  cloud-auth lures; QR-code phishing at record levels (~11% of detected phishing emails);
  and 100+ distinct EDR-killer tools now catalogued in the wild.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-08"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, phishing, mobile, ransomware, infostealer]
regions: [global, europe]
sectors: [public-sector, finance, healthcare, telco]
entities: ["report:eset-threat-report-h1-2026"]
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/eset-threat-report-h1-2026/"
    publisher: "ESET / WeLiveSecurity"
    date: "2026-07-08"
    role: primary
  - url: "https://www.globenewswire.com/news-release/2026/07/08/3323874/0/en/ESET-Threat-Report-AI-boosts-cyber-attackers-efficiency.html"
    publisher: "GlobeNewswire (ESET press release)"
    date: "2026-07-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "ESET researchers identified PromptSpy, the first known Android malware to use generative AI in its execution flow"
    publisher: "ESET / WeLiveSecurity"
  - quote: "ESET detections of this vector more than doubled between H2 2025 and H1 2026"
    publisher: "ESET / WeLiveSecurity"
  - quote: "ESET Research has documented over 100 EDR killers used in the wild, with new variants appearing regularly"
    publisher: "ESET / WeLiveSecurity"
verification: single-source
sourcing_note: "Single-source: both cited references are ESET's own first-hand statement — the WeLiveSecurity report and the GlobeNewswire item, which is ESET's press release — so they are not independent corroboration. For a named vendor's own periodic threat report this is the expected shape; the report itself (Admiralty B research lab) is the primary."
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
  - "Prioritise EDR-killer detection (driver/process-tampering telemetry, protected-process-light violations) over signature-based ransomware-binary detection, given 100+ catalogued killer tools."
  - "Treat QR codes in email bodies as first-class phishing indicators requiring the same scrutiny as embedded URLs, and add 'AI help page' / browser-extension-install ClickFix lures to user-awareness material alongside the fake-CAPTCHA variant."
migrated_from: null
---

ESET's semi-annual threat-landscape report (telemetry December 2025–May 2026) flags four developments a Tier 2/3 team should track ([ESET / WeLiveSecurity, 2026-07-08](https://www.welivesecurity.com/en/eset-research/eset-threat-report-h1-2026/); [ESET press release, 2026-07-08](https://www.globenewswire.com/news-release/2026/07/08/3323874/0/en/ESET-Threat-Report-AI-boosts-cyber-attackers-efficiency.html)).

First, ESET analysed roughly 900,000 "AI skills" — small functional components used by AI agents — and found tens of thousands suspicious and thousands outright malicious, an expanding attack surface in the emerging agentic-AI ecosystem. Second, it identified **PromptSpy**, described as the first known Android malware to use generative AI (specifically Google's Gemini) inside its own execution flow to interpret UI elements and adapt behaviour across devices at runtime rather than relying on hardcoded logic — following the first AI-powered ransomware disclosed in 2025 ([ESET, 2026-07-08](https://www.welivesecurity.com/en/eset-research/eset-threat-report-h1-2026/)). Third, **ClickFix** (the fake-error social-engineering technique) has expanded beyond fake CAPTCHA prompts into AI-themed help pages, browser extensions and cloud-authentication scenarios, with ESET detections more than doubling between H2 2025 and H1 2026. Fourth, **QR-code phishing** ("quishing") reached record levels, with roughly 11% of all ESET-detected phishing emails in H1 2026 using QR codes to move victim interaction onto mobile devices and evade cursory inspection. Ransomware activity continued unabated with over **100 distinct EDR-killer tools** now catalogued by ESET, though a declining share of victims are reportedly paying.

**Defender takeaway:** this is a single reference entry for ESET's semi-annual H1/H2 report cadence (predecessor: ESET Threat Report H2 2025). The operational reads for the constituency: the volume of EDR-killer tooling argues for prioritising driver/process-tampering and protected-process telemetry over ransomware-binary signatures; QR codes in email bodies deserve the same handling as embedded URLs; and ClickFix awareness material must now cover AI-help-page and browser-extension-install variants, not just the fake-CAPTCHA lure. PromptSpy and the malicious-"AI-skills" finding are early indicators that runtime GenAI is moving into the malware execution path itself, worth tracking as a developing class rather than an immediate control change.
