---
schema: 1
kind: threat
title: "ReliaQuest: LLM-driven agents run most of an intrusion through one unauthenticated Spring Batch job-submission feature on Apache Tomcat, from in-process JavaScript to SYSTEM in under 24 hours"
headline: "ReliaQuest: AI agents took a Tomcat server to SYSTEM in under a day through an exposed job-submission feature"
summary: >
  ReliaQuest assesses with high confidence that LLM-driven agents carried out substantial parts of an intrusion it
  investigated, using only known techniques: an internet-facing Apache Tomcat application accepted Spring Batch job
  definitions without a login, jobs ran JavaScript through the Nashorn engine inside the application process, plaintext SQL
  Server sysadmin credentials from the application's configuration led to xp_cmdshell, and two public privilege-escalation
  tools reached SYSTEM. ReliaQuest names no victim, sector or region, nor the vendor of the exposed application, and could not determine how
  many agents ran, which model drove them or how much a person approved.
discovered_at: "2026-10-09T03:45:00Z"
updated_at: null
event_date: "2026-10-07"
run_id: 2026-10-09T0255Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [global]
sectors: []
entities: []
techniques: [T1190, T1059.007, T1552.001, T1505.001, T1134.001, T1003.002, T1136.001, T1070.004, T1105, T1140]
affected_products: ["Apache Tomcat", "Spring Batch", "Microsoft SQL Server"]
cves: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/"
    publisher: "ReliaQuest Threat Research"
    date: "2026-10-07"
    role: primary
closed_sources: []
evidence:
  - quote: "The attacker entered through an internet-facing application feature on an Apache Tomcat server that accepted and ran task descriptions without requiring a login."
    publisher: "ReliaQuest Threat Research"
    source_url: "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/"
  - quote: "No single one establishes that an LLM agent was involved; a human directing scripts could produce several of them."
    publisher: "ReliaQuest Threat Research"
    source_url: "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/"
verification: single-source
sourcing_note: >
  ReliaQuest is the only source and is describing an incident it investigated; the agent-driven reading is its own
  assessment from combined indicators, not a confirmed fact, and no victim or region is named and the exposed application's vendor is not given.
confidence: medium
references:
  - "2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes"
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

ReliaQuest says the attacker needed no zero-day and no new malware: an internet-facing Apache Tomcat application used Spring Batch, in which a task definition names the code to run, and accepted and ran task descriptions without a login ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)). The decisive step was submitting tasks that invoked Nashorn, the JavaScript engine in the application's Java environment, so the code ran inside the application with its account privileges and created no child process until a shell was spawned later; results came back through deliberately triggered error messages, in fixed 1,800-byte chunks reassembled over hundreds of requests ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)). The application's configuration files held plaintext credentials with SQL Server sysadmin rights; the attacker enabled xp_cmdshell, found SeImpersonatePrivilege, uploaded PrintSpoofer and GodPotato in base64 fragments through the same channel and reached SYSTEM when the first tool failed on file permissions and the second worked ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)). With SYSTEM it saved the SAM, SYSTEM and SECURITY registry hives for offline extraction, created two local administrator accounts and deleted only one, and removed artifacts after the actions that produced them ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)).

The agent-driven reading rests on a live, unauthenticated Cairn agent-orchestration dashboard (an open-source platform for coordinating AI agents; no source says whether it is the Cairn exploitation engine of Gambit Security's reporting, and it is not Talos' CAIRN toolkit) on the address that sent the opening requests, on command timing (roughly half the gaps five seconds or less), on job names that tracked read offsets and upload parts without a gap, on machine-readable pipe-delimited output, and on payloads whose next version repaired the fault the previous one returned; ReliaQuest says no single indicator establishes it and that it could not determine how many agents ran, which model drove them or how much a person approved ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)). Submission and collection ran from different addresses, so blocking the submitting address alone would not have stopped retrieval, and the tool assembly is not a fingerprint for any group ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)).

**Exposure:** an internet-reachable Spring Batch or comparable job-submission or job-management feature that accepts task definitions without authentication, on a Java runtime that still provides the Nashorn engine; ReliaQuest names no vendor or product for the exposed application ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)).

**Detection:** application job definitions, execution and step history, exceptions and exit descriptions are the record that outlasted the attacker's deleted files, so retain them beside web, database and endpoint logs and hunt for unusual job volume or sequencing together with unexpected script-engine use and output returned through error messages; Nashorn errors were almost absent from the baseline history and tracked the malicious jobs. In database and host telemetry, look for xp_cmdshell being enabled followed by operating-system commands from the database service account, for impersonation-privilege escalation tools, and for the SAM, SYSTEM and SECURITY hives being saved ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)). ReliaQuest treats command cadence as a useful signal and not as a stand-alone detector.

**Defender takeaway:** require authentication on every exposed job-management endpoint, keep database credentials out of application configuration files and give the service account only the rights it needs, and scope an incident of this kind from the application's job records rather than from what survives on disk; a leftover local administrator account is part of the check, since one of the two created here was left in place ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)).
