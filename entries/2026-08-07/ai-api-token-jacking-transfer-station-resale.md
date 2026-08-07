---
schema: 1
kind: research
horizon: operational
title: "Stolen AI API tokens reach a reselling proxy within minutes — Unit 42 documents the 'transfer station' market and the account-takeover variant that mints its own keys"
headline: "An exposed AI API key is a billing incident on a clock: Unit 42 saw one reach a reseller in minutes and run up nearly a million dollars"
summary: >
  Unit 42 describes "token jacking" — theft of AI-provider API tokens via infostealers, phishing, poisoned
  packages or credentials left in improperly secured file shares and code repositories — and the gray market that monetises them.
  "Transfer station" services built on open-source LLM-proxy software sit in front of the stolen token, hide it
  from the buyer, and resell discounted model access; Unit 42 responded to cases where an exposed credential
  reached one within minutes and generated nearly a million dollars in charges before containment. A second variant needs no leaked key at all: an attacker
  using a corporate developer account harvested by an infostealer, taken by phishing or bought from an access
  broker mints new keys, removes billing limits and disables usage alerts and logging. Recovering the billed funds is largely not possible.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-06"
run_id: 2026-08-07T0411Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, cloud, identity, cryptocrime, infostealer]
regions: [global]
sectors: [technology, public-sector, finance]
entities: []
techniques: [T1552.001, T1552.004, T1528, T1078.004, T1098.001, T1496.004, T1685.002, T1090.003]
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/ai-token-jacking/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "We’ve responded to cases where attackers stole inadvertently exposed credentials and integrated them into a transfer station within minutes."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "This led to nearly a million dollars in charges before discovery and containment."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "Organizations impacted by token jacking have very little recourse to recover funds billed by the AI services for using their API tokens."
    publisher: "Palo Alto Networks Unit 42"
verification: single-source
sourcing_note: >
  Single-source: Unit 42's own incident-response observations and infrastructure analysis. No second party has
  independently assessed the transfer-station ecosystem, so credibility is 2 rather than 1. The near-million-dollar
  figure is Unit 42's account of cases it responded to, not an industry estimate, and is carried as an incident
  cost rather than as a vanity metric.
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
  - "Set hard spend ceilings on AI-provider accounts that the consuming credential cannot itself raise, and scope each API token to the minimum model and quota it needs — the account-takeover variant in this report works by removing billing limits and disabling usage alerts with the same account that spends the budget."
  - "Treat an AI API token found in a code repository or an unsecured file share as a same-shift rotation, not a backlog ticket: Unit 42 observed resale inside minutes of exposure."
migrated_from: null
---

Unit 42 has put a name and a market structure to something most organisations still treat as a billing anomaly. "Token jacking" is the theft of AI-provider API tokens — through infostealer malware, phishing, credentials leaked in poisoned packages, or keys sitting in what Unit 42 calls improperly secured file shares or code repositories — and the monetisation path is a gray-market reseller layer Unit 42 calls a transfer station ([Palo Alto Networks Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/ai-token-jacking/)). These services are typically built on openly available LLM-proxy software, which is doing something specific for the operator: it sits in front of the stolen legitimate token, obfuscates the real credential from the paying customer, handles authentication rotation and billing, and resells discounted access to the underlying model. The buyer never sees whose key they are spending, and the victim sees only usage.

The speed is what changes the response. "We’ve responded to cases where attackers stole inadvertently exposed credentials and integrated them into a transfer station within minutes" ([Palo Alto Networks Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/ai-token-jacking/)), and in one such case "this led to nearly a million dollars in charges before discovery and containment" ([Palo Alto Networks Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/ai-token-jacking/)). Unit 42 also documents a variant that does not depend on a single leaked key, and it is account takeover rather than a rogue employee: the privileged corporate developer accounts in question are harvested by infostealers or phishing, or bought from access brokers on dark-web marketplaces. An attacker holding one uses that account's own privileges to mint new API keys, provision additional models, remove billing limits, and disable usage alerts and logging — extending the abuse window by dismantling the controls that would have ended it. The financial exposure is largely one-way: "Organizations impacted by token jacking have very little recourse to recover funds billed by the AI services for using their API tokens" ([Palo Alto Networks Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/ai-token-jacking/)).

**Defender takeaway:** an AI API token now belongs in the same class as a cloud access key, with the same rotation urgency and the same blast-radius assumptions — and the "minutes" figure means secret-scanning that runs nightly is scanning after the fact. The account-takeover variant carries a design lesson worth acting on independently of any intrusion: if the credential that consumes the budget can also raise the ceiling and silence the alerts, then the budget is not a control. Detection concepts, telemetry class first: in API-gateway and provider usage telemetry, the signal Unit 42 points to is a client user-agent shift toward a generic HTTP-library string associated with proxy or relay software, appearing alongside a step-change in call volume inconsistent with the token's normal calling application; in cloud and provider audit records, key-creation, model-provisioning, billing-limit and alert-configuration changes are the account-takeover sequence and should be alerted on as administrative events rather than reviewed in a monthly billing cycle. **Triage:** a legitimate usage spike looks identical on volume alone — a team shipping a new feature will double its calls — so volume is not the discriminator. What separates the two is whether the *caller* changed at the same time: a new or unrecognised client fingerprint arriving with the new volume, from a token whose calling application has not been redeployed, is the combination that distinguishes resale from growth.
