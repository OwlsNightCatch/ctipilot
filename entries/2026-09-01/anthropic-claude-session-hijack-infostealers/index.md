---
schema: 1
kind: threat
title: "Infostealers now specifically monetize hijacked Claude sessions: Anthropic revokes sessions compromised via Vidar, LummaC2, StealC, RedLine, Acreed and AMOS"
headline: "Anthropic force-revokes Claude sessions hijacked by infostealer-harvested cookies, bypassing password and 2FA entirely"
summary: >
  Anthropic began emailing affected users in the days before 2026-08-31 after finding that a threat actor
  was picking stolen Claude (claude.ai) login sessions out of commodity infostealer logs and
  replaying them to access accounts and consume paid usage. The malware families named are Vidar,
  LummaC2, StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of
  Macs; because a stolen session cookie authenticates as an already-logged-in user, the technique
  bypasses password and 2FA entirely. Anthropic revoked affected sessions, stripped saved payment
  methods, and refunded unauthorized charges.
discovered_at: "2026-09-01T04:11:32Z"
updated_at: null
event_date: "2026-08-30"
run_id: 2026-09-01T0411Z-intel
priority: notable
immediate_action: null
tags: [infostealer, identity, cloud, ai-abuse]
regions: [global]
sectors: [technology]
entities: ["campaign:claude-session-hijack-infostealers-2026"]
techniques: [T1539, T1550.004]
affected_products: ["Anthropic Claude"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/"
    publisher: "BleepingComputer"
    date: "2026-08-30"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/"
    publisher: "Help Net Security"
    date: "2026-08-31"
    role: corroborating
  - url: "https://www.darkreading.com/cyberattacks-data-breaches/anthropic-users-infostealer-attacks-session-thefts"
    publisher: "Dark Reading"
    date: "2026-08-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have recently become aware of a bad actor that is using common infostealer malware to steal Claude login sessions from people's computers, then using those login sessions to access Claude accounts and consume their usage"
    publisher: "Anthropic (email to affected users, via BleepingComputer)"
  - quote: "Signing you out of Claude stops the stolen sessions, but it doesn't remove the malware,"
    publisher: "Anthropic (email to affected users, via BleepingComputer)"
  - quote: "If it's still on your computer, your next login session could be stolen the same way."
    publisher: "Anthropic (email to affected users, via BleepingComputer)"
  - quote: "The malware identified in this campaign so far include Vidar, Lumma (LummaC2), StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of Macs"
    publisher: "Anthropic (email to affected users, via Help Net Security)"
  - quote: "If your usage limits looked like they refilled and then drained while you weren't using Claude, this was likely the cause,"
    publisher: "Anthropic (email to affected users, via BleepingComputer)"
verification: single-source-victim
sourcing_note: >
  The primary is Anthropic's direct email notification to affected users about its own incident,
  first surfaced publicly via a Reddit post from a recipient and reproduced with consistent wording
  by three separate outlets — one underlying source, several publishers, treated under the
  victim's-own-disclosure carve-out. No independent Anthropic blog post or trust-center advisory was
  located, and no outlet reports independent confirmation beyond relaying the same email.
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

Anthropic sent emails to affected users last week, according to Help Net Security's 2026-08-31 report, to say a threat actor had stolen active Claude (claude.ai) login sessions using general-purpose infostealer malware already resident on those users' machines, then replayed the stolen session cookies to access the accounts and consume paid usage ([Help Net Security, 2026-08-31](https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/); [Anthropic, via BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)). Anthropic names the malware families involved as Vidar, Lumma (LummaC2), StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of Macs ([Anthropic, via Help Net Security, 2026-08-31](https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/)) — all commodity infostealers whose logs are traded on criminal markets. Anthropic states the infection vector is unrelated to Claude itself, typically an unofficial download or a malicious app; the case that surfaced publicly traced to a pirated-game download ([BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)).

Because a stolen browser session cookie authenticates as an already-logged-in user, the attacker bypasses password and two-factor authentication entirely; Dark Reading frames the incident as part of a broader shift, as stronger password policies and wider MFA adoption make traditional credential theft harder, toward attackers targeting session cookies and tokens to hijack already-authenticated sessions instead ([Dark Reading, 2026-08-31](https://www.darkreading.com/cyberattacks-data-breaches/anthropic-users-infostealer-attacks-session-thefts)). Anthropic's remediation was to invalidate the stolen sessions, strip saved payment methods from affected accounts, and refund unauthorized charges; it explicitly warns that signing a user out does not remove the infostealer itself, so an unremediated host will have its next session stolen the same way ([Anthropic, via BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)).

**Defender takeaway:** any SaaS or GenAI account reachable with only a browser session cookie is exposed to infostealer logs regardless of an organization's own MFA policy, because the theft happens client-side, before authentication even completes on a subsequent visit. Session-lifetime limits, IP or device binding on session tokens, and routine monitoring of commercial infostealer-log feeds for organizational domains are the controls that address this class of takeover — a stronger password or MFA policy alone does not. Staff using Claude or comparable AI assistants for coding or analysis on personal or under-managed devices are the population most exposed, since those devices sit outside an organization's own endpoint controls.

**Triage:** the discriminating signal Anthropic itself points users to is a usage allotment that "refilled and then drained" while the subscriber was not using Claude ([Anthropic, via BleepingComputer, 2026-08-30](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)). A legitimate usage spike correlates with the account owner's own activity; a drained allotment with no corresponding use by the account owner is the anomaly infostealer-driven session replay produces.
