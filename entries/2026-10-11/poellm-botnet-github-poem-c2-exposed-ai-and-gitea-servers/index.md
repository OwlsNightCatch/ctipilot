---
schema: 1
kind: threat
title: "PoeLLM: a cryptomining botnet that reads its C2 address out of a GitHub poem compromises exposed LiteLLM, Ollama, Gotenberg and Gitea servers and turns them into scanners"
headline: "Lumen: a botnet takes its C2 address from a GitHub poem and spreads through exposed AI and developer servers"
summary: >
  Lumen's Black Lotus Labs tracks PoeLLM, a financially motivated botnet active since at least April 2026 that Lumen says has
  impacted more than 3,400 servers, mostly in the United States and Western Europe, among them exposed LiteLLM, Ollama,
  Gotenberg and Gitea servers, with Ivanti Sentry possibly targeted. The malware derives its command-and-control address from
  words in a poem in a GitHub repository, runs XMRig and Iron miners and turns victims into scanners and exploit launchers
  that Lumen says likely abuse the LiteLLM CVE-2026-42271 path.
discovered_at: "2026-10-11T03:37:00Z"
updated_at: null
event_date: "2026-10-07"
run_id: 2026-10-11T0256Z-intel
priority: notable
immediate_action: null
tags: [botnet, cryptocrime]
regions: [global]
sectors: [technology]
entities: ["malware:poellm"]
techniques: [T1190, T1496.001, T1102.001, T1105, T1595.002, T1584.008]
affected_products: ["LiteLLM", "Ollama", "Gotenberg", "Gitea", "Ivanti Sentry"]
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware"
    publisher: "Lumen Black Lotus Labs"
    date: "2026-10-07"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/"
    publisher: "BleepingComputer"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The malware derives its current C2 server from keywords in a poem hosted in a GitHub repository."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware"
  - quote: "We assess that PoeLLM is associated with an Italian-speaking threat actor and is deployed through vulnerability exploitation of publicly exposed services."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware"
verification: single-source
sourcing_note: >
  Lumen's Black Lotus Labs is the only party that observed the botnet; BleepingComputer reports Lumen's findings without
  independent telemetry. Lumen's page carries a 2026-03-16 date field although its content runs to September 2026, and
  the outlets that reported it date it 2026-10-07. Lumen's summary and its narrative give different victim counts, and
  BleepingComputer notes that Lumen raised the figure in the live report. Attribution and the victim count are Lumen's own
  telemetry-based assessments.
confidence: medium
references:
  - 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti
  - 2026-05-30/cve-2026-48710-badhost-starlette-fastapi-vllm-litellm-mcp-sd
  - 2026-08-31/ai-infrastructure-litellm-ragflow-kestra-intrusions
  - 2026-06-10/cve-2026-10520-cve-2026-10523-ivanti-sentry-pre-auth-os-comm
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

Lumen's Black Lotus Labs says PoeLLM has been active since at least April 2026, deploys XMRig and Iron cryptocurrency miners that connect to a Kryptex mining pool, and is deployed through vulnerability exploitation of publicly exposed services, mainly LiteLLM and Ollama and, in the hundreds, the Gotenberg PDF converter and Gitea, with other products such as Ivanti Sentry possibly targeted ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). It counts more than 3,400 impacted servers, a figure it raised after first circulating the report ([BleepingComputer, 2026-10-07](https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/)), predominantly in the United States and Western Europe, and assesses that PoeLLM is associated with an Italian-speaking threat actor ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)).

The command channel is the unusual part: the malware derives its current C2 server from keywords in a poem hosted in a GitHub repository, so the operator rotates servers by editing the poem, which Lumen counts 11 edits of since the first commit on 2026-04-13 ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). Several C2 servers were routers with exposed administration pages, which Lumen reads as the operator repurposing compromised routers ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). Infected servers become scanners and exploit launchers that sweep ports 3000 and 4000, the primary ports of Gotenberg and LiteLLM, and send a crafted POST that makes the target fetch a payload from the C2; the payload is a single ELF binary that bundles a remote shell, the miners, HTTP and HTTPS scanning and exploit deployment, and beacons back to the C2 ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). For LiteLLM, Lumen says the endpoint /mcp-rest/test/connection, which the CVE-2026-42271 command injection references, was likely the exploitation path ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)), and BleepingComputer adds that Horizon3 showed it can be chained with CVE-2026-48710 for unauthenticated remote code execution ([BleepingComputer, 2026-10-07](https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/)). Lumen met the infrastructure while investigating the Ivanti Sentry flaw CVE-2026-10520, when a compromised Sentry victim contacted a PoeLLM C2 and began scanning for other vulnerable devices; it states no further link between that flaw and the botnet ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)).

**Exposure:** internet-reachable LiteLLM, Gotenberg, Ollama and Gitea servers, and Ivanti Sentry on a vulnerable build; Gotenberg's own installation guidance warns against exposing the service to the internet ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). An external attack-surface scan plus the patch level of LiteLLM (CVE-2026-42271 and CVE-2026-48710) and Sentry (CVE-2026-10520) shows whether a host is in scope.

**Detection:** egress telemetry from AI, PDF-conversion and Git servers to mining pools and to unfamiliar C2 addresses, servers originating scans toward ports 3000 and 4000, and process telemetry for an unfamiliar ELF binary running on such servers ([Lumen, 2026-10-07](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)). Patching removes the entry point, not a running implant, so hosts that were exposed on a vulnerable build need the check as well.

**Defender takeaway:** bring AI gateways and utility services such as these into the same exposure and patch inventory as other internet-facing software, take them off the internet where they need no public reach, and check any host that was exposed on a vulnerable build for miners and outbound scan traffic, since Lumen reports that infected servers are reused to attack others.
