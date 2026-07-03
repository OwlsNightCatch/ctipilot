---
schema: 1
kind: research
horizon: operational
title: "Imperva and Varonis: indirect prompt injection and \"agent phishing\" against the OpenClaw AI agent — fixed in v2026.4.23, but the attack class generalises"
headline: "Imperva and Varonis: indirect prompt injection and \"agent phishing\" against the OpenClaw AI agent — fixed in v2026.4.23, but the attack class generalises"
summary: "Two independent teams published complementary findings against OpenClaw, the self-hosted AI-agent platform that plugs into messaging systems, mailboxes, file systems and APIs."
discovered_at: "2026-06-12T05:00:07Z"
event_date: 2026-06-10
run_id: 2026-06-12-5ab9a319
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - phishing
  - cloud
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:openclaw-prompt-injection-agent-phishing-2026"
cves: []
sources:
  - url: "https://www.imperva.com/blog/compromise-openclaw-with-prompt-injections-in-message-objects/"
    publisher: Imperva
    role: primary
  - url: "https://www.varonis.com/blog/openclaw-phishing"
    publisher: Varonis
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
migrated_from: briefs/2026-06-12.md
---

Two independent teams published complementary findings against OpenClaw, the self-hosted AI-agent platform that plugs into messaging systems, mailboxes, file systems and APIs. Imperva showed that shared contact names, vCard fields and location-pin labels flow into the LLM prompt with no untrusted-content boundary: a crafted contact — its injected command hidden behind 65 whitespace characters so the UI truncates it — executed `python3` on the victim's host the moment the victim shared the contact with their agent ([Imperva, 2026-06-10](https://www.imperva.com/blog/compromise-openclaw-with-prompt-injections-in-message-objects/)). Varonis demonstrated "agent phishing": a plain email from a plausible sender persuaded a mailbox-connected agent to forward mock AWS IAM keys and a customer export to an external address, with no exploit involved — the agent simply lacks sender-identity verification before acting ([Varonis, 2026-06-09](https://www.varonis.com/blog/openclaw-phishing)). Both teams note OpenClaw's default memory persistence lets one successful injection survive across sessions. The vendor fix (v2026.4.23) moves messaging-object metadata into a separate untrusted channel — but the structural lesson stands: wherever an agent ingests third-party-controlled strings (contacts, calendar invites, ticket bodies), that channel is an injection surface ([T1059](https://attack.mitre.org/techniques/T1059/)). Defender takeaway: pin OpenClaw ≥ v2026.4.23; inventory which AI agents hold mailbox send-permissions or shell access; gate agent-initiated outbound actions behind approval workflows the same way you gate privileged operations.
