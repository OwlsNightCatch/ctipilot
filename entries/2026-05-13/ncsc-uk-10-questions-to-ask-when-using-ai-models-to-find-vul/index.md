---
schema: 1
kind: research
title: "NCSC-UK: 10 questions to ask when using AI models to find vulnerabilities"
headline: "NCSC-UK: finding vulnerabilities with AI improves nothing without a process to fix what it finds"
summary: "NCSC-UK published on 2026-05-11 ten questions for organisations to answer before using AI models to find vulnerabilities, warning that finding vulnerabilities alone does nothing to improve security and could make it worse. The questions cover the process for fixing what AI finds, prioritising exploitable flaws, information leakage, sandboxing, production access, the permissions given to the model, data retention and legality."
discovered_at: "2026-05-13T05:00:10Z"
event_date: 2026-05-11
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - vulnerabilities
regions:
  - uk
sectors:
  - public-sector
entities: []
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities"
    publisher: "NCSC-UK"
    date: "2026-05-11"
    role: primary
closed_sources: []
evidence:
  - quote: "just *finding* vulnerabilities does nothing to improve your security. You could even make your security worse."
    publisher: NCSC-UK
    source_url: "https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities"
  - quote: "When using AI to find vulnerabilities prioritise your external attack surface. You should also look for ways to verify the results, by using both AI and humans."
    publisher: NCSC-UK
    source_url: "https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities"
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
updated_at: null
updates:
  - at: "2026-10-21T16:09:00Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      NCSC-UK's ten questions include no item on false-positive overhead; the nearest is resourcing,
      avoiding spending everything on finding vulnerabilities with nothing left to fix them. Its warning
      is that finding vulnerabilities alone does nothing to improve security and could make it worse, not
      a critique of buying AI tools, and its data and permissions questions ask about information leakage,
      production access and the permissions given to the model.
    fields: [affected_products, body, classification, evidence, headline, sources, summary, techniques, title]
---

NCSC-UK published on 2026-05-11 ten questions to answer before using an AI model to find vulnerabilities, written by its Head of Vulnerability Management Group ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)). It warns that just finding vulnerabilities "does nothing to improve your security" and "could even make your security worse", and asks whether a process exists to receive, prioritise and fix what AI finds without overwhelming teams ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)). Its risk questions cover information leakage, securing the infrastructure used, sandboxing the system so it can only talk to the LLM and the code base, whether to give it production access, the permissions given to the LLM, spending all the money, time and people on finding rather than fixing, terms and data-retention policies, and legality ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)). It ties prioritisation to exploitability: of more than 40,000 CVEs assigned in 2025, CISA's catalogue tracked about 400 new ones as exploited, around 40 of them zero-days when first exploited ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)).

**Defender takeaway:** before pointing an AI model at code or infrastructure, make sure the vulnerability-management process can absorb what it finds, sandbox the system to the model and the code base, decide deliberately on production access and the permissions it gets, and start with the external attack surface, verifying results with both AI and humans ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)).

## Correction — 2026-10-21T16:09:00Z

The ten questions contain no item on false-positive overhead for defenders; the nearest is resourcing: "How can I avoid spending all my money/time/people finding vulnerabilities, and have nothing left to fix them?" ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)). NCSC-UK's warning is that just finding vulnerabilities does nothing to improve security and could even make it worse ([NCSC-UK, 2026-05-11](https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)); it does not say AI-accelerated discovery leaves an organisation worse off or criticise buying AI tools, and its data and permissions questions ask about information leakage, production access and what permissions the LLM is given, without mentioning secrets or a compromised agent.
