---
schema: 1
kind: research
title: "Unit 42: \"Phantom Squatting\" — registering AI-hallucinated domains to poison LLM-driven URL delivery"
headline: "Unit 42: \"Phantom Squatting\" — registering AI-hallucinated domains to poison LLM-driven URL delivery"
summary: "Palo Alto Networks Unit 42 described phantom squatting, a supply-chain attack class in which adversaries systematically probe production LLMs to learn which non-existent brand/vendor domains a model hallucinates when asked for URLs, then pre-register those specific domains before defenders or brand owners react …"
discovered_at: "2026-07-01T04:41:19Z"
event_date: 2026-07-01
run_id: 2026-07-01-af9e697d
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
  - phishing
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:unit42-phantom-squatting-hallucinated-domains"
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/"
    publisher: Palo Alto Networks Unit 42
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-07-01.md
---

Palo Alto Networks Unit 42 described **phantom squatting**, a supply-chain attack class in which adversaries systematically probe production LLMs to learn which non-existent brand/vendor domains a model hallucinates when asked for URLs, then pre-register those specific domains before defenders or brand owners react ([Unit 42, 2026-07-01](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/)). When later users — or autonomous AI agents performing tool-use/browsing — ask the same or a similarly-trained model for a link, they are handed an authoritative-sounding recommendation pointing at attacker-controlled infrastructure, bypassing traditional phishing-link delivery entirely. The core evasion is a **zero-reputation bypass**: a domain registered specifically to match a predicted hallucination has no threat-intel history, blocklist entry or reputation score at first weaponized use, defeating reputation-age-based URL/DNS filtering. Unit 42 cites a concrete case — a "Montana Empire" postal-service phishing kit that went live 23 days after Unit 42 first observed an LLM hallucinating that domain. Distinct from package-name "slopsquatting": this is domain-level and targets both humans and agent browsing. Defender takeaway: log and diff every URL an LLM surfaces against a verified canonical-domain allowlist before it reaches a user or an agent's browsing tool, and treat "brand-adjacent, recently-registered, high-similarity domain" as a standalone signal independent of reputation score. **[SINGLE-SOURCE]** — vendor research, no independent corroboration in-window.
