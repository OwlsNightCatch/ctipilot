---
schema: 1
kind: incident
horizon: operational
title: "TeamPCP / Mini Shai-Hulud — OpenAI named as victim; code-signing certificate rotation enforced for all macOS apps"
headline: "TeamPCP / Mini Shai-Hulud — OpenAI named as victim; code-signing certificate rotation enforced for all macOS apps"
summary: "UPDATE (originally covered 2026-05-13): OpenAI disclosed on approximately 2026-05-13 that two employee devices were compromised through the TanStack npm supply-chain attack (Mini Shai-Hulud / TeamPCP, first covered in this brief series on 2026-05-12 and 2026-05-13) and that the compromise affected OpenAI's macOS …"
discovered_at: "2026-05-15T05:00:09Z"
event_date: 2026-05-14
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://techcrunch.com/2026/05/14/openai-says-hackers-stole-some-data-after-latest-code-security-issue/"
    publisher: "TechCrunch, 2026-05-14"
    role: primary
  - url: "https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm"
    publisher: "The Record, 2026-05-14"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-13/mini-shai-hulud-teampcp-worm-hits-tanstack-uipath-mistral-ai
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-15.md
---

**UPDATE (originally covered 2026-05-13):** OpenAI disclosed on approximately 2026-05-13 that two employee devices were compromised through the TanStack npm supply-chain attack (Mini Shai-Hulud / TeamPCP, first covered in this brief series on 2026-05-12 and 2026-05-13) and that the compromise affected OpenAI's macOS code-signing certificates ([TechCrunch, 2026-05-14](https://techcrunch.com/2026/05/14/openai-says-hackers-stole-some-data-after-latest-code-security-issue/) · [The Record, 2026-05-14](https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm)).

The attackers exfiltrated "limited credential material" from internal source code repositories accessible to the two affected employees; OpenAI states no customer data, production systems, or core intellectual property were accessed. Critically, the certificate used to sign OpenAI's macOS desktop applications (ChatGPT for macOS and related apps) was among the compromised material, triggering an emergency certificate rotation. OpenAI is requiring all macOS app users to update to the latest version before **June 12, 2026**, after which older builds will lose functionality and macOS Gatekeeper notarization will block apps signed with the compromised certificate. Enterprise MDM administrators with OpenAI macOS apps in their managed fleet should push a forced update immediately. Threat attribution is unofficially assessed as TeamPCP (the same actor behind the broader TanStack worm), consistent with prior reporting on the actor's OIDC token theft and credential exfiltration goals.
