---
schema: 1
kind: threat
title: "VAPOR PANDA: CrowdStrike reports a China-nexus actor running the ARTEX agent framework against more than 200 organisations from 17 October, among them foreign ministries in Europe and a Greek government entity, and deploying the BLOODALCHEMY backdoor"
headline: "CrowdStrike: VAPOR PANDA runs ARTEX against 200+ organisations, European foreign ministries among them"
summary: >
  CrowdStrike reports that from 2026-10-17 the China-nexus actor VAPOR PANDA used the ARTEX agent framework, driven mainly by the DeepSeek model, against more than 200 organisations
  worldwide, with the controller CrowdStrike saw directing exploitation in at least 14 countries, including foreign ministries in Europe, a European country's presidency, prime minister's office and defence, justice, finance and intelligence entities, and a Greek government entity.
  CrowdStrike confirmed post-exploitation at nine organisations, with the BLOODALCHEMY backdoor loaded by a renamed legitimate binary, and says this campaign is separate from the Storm-0940 ARTEX activity Microsoft reported.
discovered_at: "2026-10-30T03:48:00Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-10-30T0255Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, ai-abuse, china-nexus]
regions: [global, europe]
sectors: [public-sector]
entities: ["actor:vapor-panda", "malware:bloodalchemy", "tool:artex"]
techniques: [T1588.007, T1190, T1078, T1133, T1651, T1505.003, T1134.001, T1574.001, T1036.005, T1552.005, T1555, T1606.002, T1606, T1110.003, T1518.001, T1114.002, T1090.003, T1572]
affected_products: []
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
    publisher: "CrowdStrike"
    date: "2026-10-29"
    role: primary
closed_sources: []
evidence:
  - quote: "Beginning on October 17, 2026, the adversary used ARTEX against more than 200 distinct organizations worldwide, including foreign ministries in Latin America, Europe, Asia, and the Middle East"
    publisher: "CrowdStrike"
    source_url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
  - quote: "The VAPOR PANDA campaign detailed in this blog post is separate from the ARTEX activity recently reported by industry sources under the Storm-0940 designation."
    publisher: "CrowdStrike"
    source_url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
  - quote: "Against a Greek government entity, the operator supplied the agent with a 2022 directory export from the organization's mail server containing authentication keys that had likely not been rotated since the export."
    publisher: "CrowdStrike"
    source_url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
verification: single-source
sourcing_note: >
  A single vendor report built on CrowdStrike's own telemetry and on transcripts recovered from an exposed ARTEX controller; the attribution to VAPOR PANDA is CrowdStrike's assessment from infrastructure links, and no second source has reported the campaign yet.
confidence: medium
references: ["2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse", "2026-10-26/jpcert-nict-app-to-backend-api-attacks-ai-scanning-japan"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

CrowdStrike OverWatch reports that from 2026-10-17 a single ARTEX controller linked to VAPOR PANDA infrastructure directed exploitation against entities in at least 14 countries over 11 days, and that the campaign reached more than 200 organisations, including foreign ministries in Europe ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). One engagement focused on a single European country, its foreign ministry, presidency, prime minister's office and defence, justice, finance and intelligence entities, and another targeted 19 US organisations in pharmaceuticals, semiconductors, defence, nuclear and finance ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). CrowdStrike confirmed post-exploitation at nine organisations and password spraying and credential scanning against at least 12 more, among them government entities in Europe ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). CrowdStrike states that the campaign is separate from the Storm-0940 ARTEX activity Microsoft reported and is VAPOR PANDA's first observed use of AI-driven tooling ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)).

The framework ran mainly on the DeepSeek model, with a human operator steering the agents at decision points while they pursued web, cloud, container, Active Directory, mail and VPN paths in parallel ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). In transcripts at a US pharmaceutical company the agent chained an unsigned SAML assertion with an XML external entity flaw to query the cloud instance metadata service and obtain a role that could issue administration commands to thousands of instances; at a second it deployed web shells, abused an unauthenticated orchestration service for root in a container environment, read LAPS passwords and abused resource-based constrained delegation ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). Against a Greek government entity the operator supplied a 2022 directory export from the mail server whose authentication keys had likely not been rotated; the agent forged an administrator token, read mailboxes and used VPN configurations from a user's sent mail, with a VPN client key the operator described as coming from a May 2024 email leak, to reach the internal network ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). The operator also told the agents to find domain Windows hosts without the CrowdStrike Falcon sensor ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). At a Middle East interior ministry and a Latin American foreign ministry the actor loaded the BLOODALCHEMY backdoor through a legitimate GameHook binary renamed svchost.exe that loads a malicious DLL ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)). No Swiss target is named.

**Exposure:** government, mail, identity and VPN estates where a directory export or backup holding authentication keys has never been rotated, SAML service providers that accept unsigned assertions, and cloud instances that still allow instance metadata service version 1; CrowdStrike names foreign ministries and government entities in Europe among the targets.

**Detection:** telemetry classes are authentication logs (password spraying and credential scanning against many accounts, an administrator token minted outside the identity provider, VPN logins that use a configuration or key from an old mailbox or leak), cloud control-plane audit (administration commands issued to many instances through the cloud systems manager, instance metadata queries from an application), process lineage (a legitimate GameHook binary renamed svchost.exe loading a malicious DLL) and endpoint inventory queries for hosts without the security agent; CrowdStrike lists ARTEX-named command-line parameters, cloud roles and a directory under ProgramData as hunt markers ([CrowdStrike, 2026-10-29](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)).

**Defender takeaway:** rotate keys held in old directory exports and backups, require signed SAML assertions and IMDSv2, and hunt authentication and cloud audit logs for the parallel, many-target pattern an operator-steered agent produces; CrowdStrike expects China-nexus actors to keep adopting agent frameworks.
