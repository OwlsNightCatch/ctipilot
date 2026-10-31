---
schema: 1
kind: threat
title: "Attackers social-engineer Meta's AI support chatbot into resetting Instagram passwords"
headline: "Attackers social-engineer Meta's AI support chatbot into resetting Instagram passwords"
summary: "Over the weekend of 31 May–1 June, instructions circulated on Telegram showing how to coax Meta's conversational \"AI support assistant\" into linking an attacker-controlled email to a target Instagram account and triggering a password reset, bypassing Instagram's normal account-recovery friction (Krebs on Security …"
discovered_at: "2026-06-02T05:00:03Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - identity
  - phishing
  - iran-nexus
regions:
  - global
sectors:
  - technology
  - media
entities: []
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/"
    publisher: Krebs on Security
    role: primary
  - url: "https://techcrunch.com/2026/06/01/hackers-hijacked-instagram-accounts-by-tricking-meta-ai-support-chatbot-into-granting-access/"
    publisher: TechCrunch
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-02.md
---

Over the weekend of 31 May–1 June, instructions circulated on Telegram showing how to coax Meta's conversational "AI support assistant" into linking an attacker-controlled email to a target Instagram account and triggering a password reset, bypassing Instagram's normal account-recovery friction ([Krebs on Security, 2026-06-01](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/) · [TechCrunch, 2026-06-01](https://techcrunch.com/2026/06/01/hackers-hijacked-instagram-accounts-by-tricking-meta-ai-support-chatbot-into-granting-access/)). Pro-Iranian actors used the method to briefly deface high-profile accounts, including the archived Obama White House handle and that of the Chief Master Sergeant of the U.S. Space Force. The exploit reportedly failed against any account with MFA enabled; Meta said the issue was resolved by 1 June.

**Defender takeaway:** This is an emerging attack class, not a one-off — an AI support agent able to modify account credentials or recovery linkages without re-challenging the *currently registered* second factor punctures the account's MFA envelope from the support-channel direction. Any organisation deploying AI for account-recovery or helpdesk workflows should scope those agents to read-only actions and require out-of-band challenge to existing registered methods before any credential or recovery change.
