---
schema: 1
kind: incident
horizon: operational
title: "AFP-FBI-WAPF disrupt TeamPCP: two Western Australia men charged over the npm/GitHub supply-chain worm operation AFP estimates compromised 1,000+ organisations, 500,000+ credentials and 300+ GB of data"
headline: "The first law-enforcement disruption of the Shai-Hulud npm-worm operator, with AFP's own scale estimate now on the public record"
summary: >
  The AFP, FBI and Western Australia Police jointly announced on 2026-08-27 that two men, 21 and
  23, were charged with 14 Commonwealth cybercrime offences following investigations that began
  in April 2026 into TeamPCP, the operator behind the self-propagating Shai-Hulud npm-supply-chain
  worm. AFP's own estimate: 1,000+ organisations globally, 500,000+ stolen credentials, 300+ GB
  exfiltrated. Google's Threat Intelligence Group characterises the group as a decentralised peer
  community rather than a hierarchical crew.
discovered_at: "2026-08-28T06:08:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, law-enforcement, organized-crime, infostealer]
regions: [global]
sectors: [public-sector, technology, education]
entities: [actor:teampcp]
techniques: [T1195.001, T1552, T1078.004]
affected_products: []
cves: []
sources:
  - url: "https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global"
    publisher: "Australian Federal Police (joint AFP/FBI/WAPF release)"
    date: "2026-08-27"
    role: primary
  - url: "https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/"
    publisher: "KrebsOnSecurity"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It is estimated the malicious code potentially compromised more than 1000 organisations globally, enabling the theft of more than 500,000 credentials, and the exfiltration of at least 300 gigabytes of data."
    publisher: "Australian Federal Police"
  - quote: "These men are allegedly members of the cybercriminal group TeamPCP, whose malicious code potentially compromised more than a thousand organizations worldwide."
    publisher: "Australian Federal Police"
  - quote: "It is not a structured criminal crew with a single operator. It is a peer community of individually-skilled actors, with one clear center of gravity."
    publisher: "KrebsOnSecurity"
verification: multi-source
sourcing_note: >
  The AFP's own joint media release with the FBI and WAPF is the primary; KrebsOnSecurity
  corroborates independently and adds operational-model detail from its own prior June
  investigation, which had already identified one defendant as the group's self-described
  spokesperson. Extensive OSINT deanonymisation detail in Krebs's reporting (family members,
  addresses, forum-alias chains) is deliberately omitted here as non-defender-actionable.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
migrated_from: null
---

The Australian Federal Police, FBI and Western Australia Police Force jointly announced on 2026-08-27 that two Western Australian men, aged 21 and 23, were charged with a combined 14 Commonwealth cybercrime offences — unauthorised data modification with intent to commit a serious offence, supplying data with intent to commit a computer offence, dealing with proceeds of crime over AUD 100,000, and, for one defendant, failing to comply with a section 3LA data-access order — following parallel AFP/FBI investigations that began in April 2026 after multiple threat-intelligence vendors reported a supply-chain-poisoning syndicate.

AFP states the syndicate "allegedly inserted malicious code into software available on an open-source repository, which was then unwittingly used by other developers," with infected software subsequently distributed into "computer systems at other organisations across government, academia and the private sector," enabling theft of user credentials and authentication material. AFP's own estimate: "it is estimated the malicious code potentially compromised more than 1000 organisations globally, enabling the theft of more than 500,000 credentials, and the exfiltration of at least 300 gigabytes of data" ([Australian Federal Police, 2026-08-27](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global)), with remediation costs in the hundreds of millions of dollars. FBI Cyber Division names the group directly: "these men are allegedly members of the cybercriminal group TeamPCP, whose malicious code potentially compromised more than a thousand organizations worldwide" ([FBI Cyber Division Assistant Director Brett E. Leatherman, 2026-08-27](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global)).

KrebsOnSecurity, which had independently identified one of the defendants — the group's self-described spokesperson — in June and interviewed him extensively via Signal, corroborates and adds operational-model detail: TeamPCP's core tactic is cyclical, compromising a developer's credentials to insert malicious code into a widely-depended-upon open-source package, harvesting the credentials of downstream developers who install it, and repeating against the next package — powered principally by the self-propagating "Shai-Hulud" worm (three iterations to date, whose source TeamPCP itself open-sourced). Prior TeamPCP campaigns already tracked by named security vendors include the March 2026 compromise of the LiteLLM open-source AI gateway (CloudSEK: 2,500+ organisations' cloud-service keys and CI/CD secrets harvested) and a May 2026 claim of roughly 3,800 compromised GitHub repositories.

Google's Threat Intelligence Group characterises TeamPCP's structure directly: "it is not a structured criminal crew with a single operator. It is a peer community of individually-skilled actors, with one clear center of gravity" ([Austin Larsen, Google Threat Intelligence Group, via KrebsOnSecurity, 2026-08-27](https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/)), tracing its likely primary operator's residential/mobile internet connections to South Africa during at least some of its attacks. Investigators note further arrests are not ruled out; both defendants were held in custody pending an 18 September court date.

This is TeamPCP's first law-enforcement disruption. It does not change the remediation guidance already published for the LiteLLM/Trivy and coding-agent CI-harness campaigns attributed to the same actor — a decentralised peer community losing two participants does not retire the worm's self-propagating infrastructure or the copycat variants it has already spawned; the standing guidance on pinning dependencies and auditing for Shai-Hulud-family indicators still applies.
