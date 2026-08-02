---
schema: 1
kind: research
horizon: operational
title: "Correction — GPT5.6 did not rediscover the patched WP2Shell chain: it found the WordPress pre-auth RCE first, and the patch followed the disclosure"
headline: "The AI capability marker is stronger than this pipeline reported: an original pre-auth RCE discovery in WordPress core, not a rebuild of a known one"
summary: >
  This pipeline's 2026-07-21 entry has Searchlight Cyber's Adam Kues tasking GPT5.6 "to autonomously
  rediscover and weaponise the already-patched" WordPress WP2Shell chain, and the W30 weekly carried
  the same framing. The cited Searchlight Cyber post says the opposite: the model was pointed
  at the WordPress source and explicitly forbidden from diffing against a patched version or using
  changelogs and git history, and Searchlight then "held off on publishing this issue to give
  defenders a chance to upgrade their WordPress instances over the weekend". This pipeline's own
  2026-07-18 entry already named Searchlight Cyber as the discoverer of CVE-2026-63030 and
  CVE-2026-60137. The correction matters because it changes the capability claim: not an LLM
  reconstructing a known, patched bug, but an LLM finding a pre-authentication RCE in WordPress core
  that no one had published, whose disclosure produced the out-of-band 7.0.2 / 6.9.5 / 6.8.6 release.
discovered_at: "2026-08-02T14:00:00Z"
event_date: "2026-07-20"
run_id: 2026-08-02T1309Z-audit
priority: notable
immediate_action: null
tags: [ai-abuse, vulnerabilities, rce, pre-auth, zero-day]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1190]
affected_products: ["WordPress"]
cves: []
sources:
  - url: "https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/"
    publisher: "Searchlight Cyber"
    date: "2026-07-20"
    role: primary
closed_sources: []
evidence:
  - quote: "We held off on publishing this issue to give defenders a chance to upgrade their WordPress instances over the weekend"
    publisher: "Searchlight Cyber"
  - quote: "Do not attempt to use changelogs, git history, or the internet to 'diff' the code against a patched version."
    publisher: "Searchlight Cyber"
verification: single-source
sourcing_note: "Single-source by nature: the correction is a re-reading of the same Searchlight Cyber post the original entry cited, re-fetched in full by this audit, so the discloser's own account is the authority for what the experiment was. The supporting cross-check is internal — this pipeline's 2026-07-18 WP2Shell entry independently records Searchlight Cyber as the discoverer of both CVEs. Credibility 2: one assessing party, uncorroborated by an independent second."
confidence: high
update_of: 2026-07-21/gpt56-autonomous-wordpress-wp2shell-exploit-chain
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-21):** the original entry's framing was wrong in the direction that understates the finding, and the weekly strategic entry for W30 inherited it. The correction was found by this pipeline's own weekly quality audit re-reading the cited primary.

What Searchlight Cyber's Adam Kues actually ran was a discovery test, not a reconstruction test. The prompt handed to GPT5.6 Sol Ultra opens "This is a test of your ability to discover zero-days" and then closes off the shortcut explicitly: "Do not attempt to use changelogs, git history, or the internet to 'diff' the code against a patched version." Kues explains the reasoning in his own voice — for novel vulnerability discovery, letting a model look at change history is a waste of tokens — and adds a second guard against a failure mode he names directly: models sometimes cheat to achieve what you ask, "either by choosing extremely unlikely configuration options or by fabricating preconditions that aren’t achievable by an attacker" ([Searchlight Cyber, 2026-07-20](https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/)). The model was told a pre-auth-to-RCE chain existed in the repository and asked to find it from first principles, which is a directed hunt with a known-positive — but it is a hunt for something not yet public, not a rebuild of something already published.

The disclosure timeline settles it. Searchlight "held off on publishing this issue to give defenders a chance to upgrade their WordPress instances over the weekend", and during that hold two other parties independently reproduced the full chain before proof-of-concept code surfaced on GitHub. A researcher does not delay publication of a rediscovery of an already-patched bug to protect defenders; the delay only makes sense because the disclosure came first and the patch was the response to it. This pipeline's 2026-07-18 entry on the WP2Shell chain reached the same conclusion from the other direction, recording Searchlight Cyber as the **discoverer** of CVE-2026-63030 and CVE-2026-60137 and noting the out-of-band WordPress release of 2026-07-17 — so the store already carried the correct attribution one entry earlier and then contradicted itself three days later.

**Defender takeaway:** the corrected reading raises rather than lowers where this sits on the capability curve, and it is the curve that drives planning assumptions. "An LLM can rebuild a known patched exploit in ten hours for $25" says exploitation of disclosed bugs is getting cheaper, which mainly compresses patch windows. "An LLM found a previously unpublished pre-authentication RCE chain in the source of the most widely deployed CMS on the internet, at that cost, under a prohibition on looking at the fix" says something different: that novel vulnerability discovery against large, mature, heavily audited codebases is now within reach of a small budget. For a defender the practical consequence is not a control to deploy but an assumption to revise — the arrival rate of pre-auth flaws in widely deployed software is more likely to rise than to stay flat, which argues for shortening the gap between an out-of-band release and its deployment rather than for anything new in the stack.

**Triage:** nothing here is an alertable behaviour — this is a correction to a capability assessment. The WP2Shell chain itself remains covered by this pipeline's 2026-07-18 disclosure entry and its 2026-07-26 confirmed-exploitation and KEV update, which carry the exploitation detail, the affected version boundaries and the compromise-assessment guidance; that guidance is unchanged by this correction.
