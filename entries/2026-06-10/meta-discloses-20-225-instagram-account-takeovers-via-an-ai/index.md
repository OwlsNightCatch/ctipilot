---
schema: 1
kind: incident
title: "Meta discloses 20,225 Instagram account takeovers via an AI support-tool logic flaw; Maine AG notification filed 8 June"
headline: "Meta discloses 20,225 Instagram account takeovers via an AI support-tool logic flaw; Maine AG notification filed 8 June"
summary: "Meta filed a breach notification with the Maine Attorney General on 8 June disclosing that a logic flaw in its AI-assisted account-recovery tool (\"High Touch Support\") allowed unauthorised actors to hijack 20,225 Instagram accounts between 17 April and 31 May 2026 (BleepingComputer, 2026-06-08)."
discovered_at: "2026-06-10T05:00:03Z"
event_date: 2026-06-08
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - data-breach
  - ai-abuse
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/meta-ai-support-data-breach-affects-20-000-instagram-accounts/"
    publisher: "BleepingComputer, 2026-06-08"
    role: primary
  - url: "https://www.securityaffairs.com/193307/ai/meta-ai-recovery-tool-flaw-exposed-20000-instagram-accounts.html"
    publisher: "Security Affairs, 2026-06-08"
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
migrated_from: briefs/2026-06-10.md
---

Meta filed a breach notification with the Maine Attorney General on 8 June disclosing that a logic flaw in its AI-assisted account-recovery tool ("High Touch Support") allowed unauthorised actors to hijack 20,225 Instagram accounts between 17 April and 31 May 2026 ([BleepingComputer, 2026-06-08](https://www.bleepingcomputer.com/news/security/meta-ai-support-data-breach-affects-20-000-instagram-accounts/)). A separate code path failed to verify that the email address supplied with a reset request matched the account's registered address, so the reset link was sent to the attacker-provided address — a confused-deputy bypass requiring no prior knowledge of the victim's email, phone or password ([Security Affairs, 2026-06-08](https://www.securityaffairs.com/193307/ai/meta-ai-recovery-tool-flaw-exposed-20000-instagram-accounts.html)). Accounts with two-factor authentication enabled were protected from full takeover even when the reset link was obtained. Meta disabled the tool on discovery (31 May), invalidated pending reset links, and will notify affected users on 19 June.

**Why it matters to us:** this is the AI-support-automation risk class in practice — a "helpful" AI workflow induced to act on attacker-supplied identity claims without cross-checking authoritative records (T1078, T1556). Organisations deploying AI help-desk or self-service account-recovery should audit whether the AI decision path can be steered by attacker-controlled email/identity input, and enforce 2FA so a password-reset bypass alone does not yield takeover.
