---
schema: 1
kind: incident
title: "Braintrust AI evaluation platform AWS account breach: customer-stored AI provider API keys likely exposed, all customers urged to rotate org-level keys"
headline: "Braintrust AWS account breach likely exposed customers' stored AI provider keys; every customer asked to rotate them"
summary: "Braintrust, an AI evaluation and observability platform, discovered on 2026-05-04 that attackers had accessed one of its AWS accounts, which likely gave them the org-level API keys customers store with it to access AI models. At least one customer was affected and three others reported suspicious spikes in AI provider usage; Braintrust asked every customer to rotate the AI provider keys they store with it."
discovered_at: "2026-05-10T05:00:01Z"
event_date: 2026-05-05
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - cloud
  - ai-abuse
regions:
  - global
sectors:
  - technology
entities:
  - "incident:braintrust-aws-breach-2026"
techniques: [T1528]
affected_products: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/"
    publisher: "TechCrunch"
    date: "2026-05-06"
    role: primary
  - url: "https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/"
    publisher: "SecurityWeek"
    date: "2026-05-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the startup confirmed “unauthorized access” in one of its Amazon Web Services (AWS) cloud accounts, which contained API keys used by customers for accessing cloud-based AI models."
    publisher: "TechCrunch"
    source_url: "https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/"
  - quote: "The company said the cause of the breach is under investigation."
    publisher: "TechCrunch"
    source_url: "https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/"
  - quote: "The incident, the company says, was discovered on May 4, after receiving a report of suspicious behavior, and was communicated to customers via email on May 5."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/"
  - quote: "According to the company, at least one customer has been affected by the incident, with three other customers reporting suspicious spikes in AI provider usage."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/"
  - quote: "Braintrust recommends that customers access their org-level settings page, delete or revoke the existing secrets, configure new secrets, and confirm that they were rotated by checking their timestamps."
    publisher: "SecurityWeek"
    source_url: "https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/"
verification: single-source-victim
sourcing_note: >
  Every fact about the breach comes from Braintrust's customer email and website notice as TechCrunch and SecurityWeek relay them;
  no independent party has reported examining it. The two outlets differ by a day on the customer email (Monday 2026-05-04 in TechCrunch,
  2026-05-05 in SecurityWeek), and the list of companies whose keys were likely stored is a Nudge Security executive's estimate.
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
actions: []
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-10-21T20:23:33Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Braintrust discovered the breach of one of its AWS accounts on 2026-05-04 and disclosed it on
      2026-05-05; no source gives the date the attackers got in. The stored keys were org-level AI
      provider keys, the rotation was a request to every customer rather than a mandate, and the companies
      named as likely key holders are a Nudge Security executive's estimate, not adjacent SaaS credentials
      at risk. At least one customer was affected and three others reported suspicious AI provider usage
      spikes.
    fields: [affected_products, body, classification, confidence, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title, verification]
---

Braintrust, an AI evaluation and observability platform, discovered on 2026-05-04, after a report of suspicious behaviour, that attackers had accessed one of its AWS accounts ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). It emailed customers on Monday 2026-05-04 and disclosed the incident on its website on Tuesday 2026-05-05 ([TechCrunch, 2026-05-06](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/)); SecurityWeek dates the customer email to 2026-05-05 ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). The internal AWS account likely gave the attackers access to the org-level API keys customers store with Braintrust to access AI models; at least one customer was affected and three others reported suspicious spikes in AI provider usage, while Braintrust said it had not identified broader customer exposure ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). Braintrust locked down the compromised account, audited and restricted access across related systems and rotated internal secrets; the cause of the breach is under investigation ([TechCrunch, 2026-05-06](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/)). Nudge Security CTO Jaime Blasco told SecurityWeek the exposed keys were likely stored for AI-forward companies such as Box, Cloudflare, Dropbox, Notion, Ramp and Stripe, and called every AI evaluation, observability and gateway tool a company adopts a credential warehouse ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)).

**Exposure:** organisations that stored org-level AI provider keys in Braintrust; Braintrust informed all org admins with stored AI provider secrets ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)).

**Detection:** AI provider usage and billing telemetry for the keys that were stored in Braintrust: the signal three customers reported was a suspicious spike in AI provider usage ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)).

**Defender takeaway:** Braintrust customers delete or revoke the existing AI provider secrets on the org-level settings page, configure new ones and confirm the rotation from their timestamps, as Braintrust recommends ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)), and review the provider-side usage of the old keys up to their revocation; organisations that stored no keys in Braintrust have no decision to make.

## Correction — 2026-10-21T20:23:33Z

Braintrust discovered the incident on 2026-05-04 after a report of suspicious behaviour ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)) and disclosed it on its website on 2026-05-05 ([TechCrunch, 2026-05-06](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/)); 2026-05-04 is not the date of the attackers' access, which no source gives, so there is no known access window to search audit logs against. The exposed secrets were the API keys customers use to access AI models, with no AI provider named, and the email asked every customer to rotate them ([TechCrunch, 2026-05-06](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/)); Braintrust's notice calls them org-level AI provider keys ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). Box, Cloudflare, Dropbox, Notion, Ramp and Stripe are companies whose AI provider keys were likely stored in Braintrust, in the estimate of Nudge Security's CTO, not SaaS services whose credentials were at risk ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)). At least one customer was affected and three others reported suspicious spikes in AI provider usage ([SecurityWeek, 2026-05-08](https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/)), so the check that matters is the provider-side usage of the keys that were stored in Braintrust.
