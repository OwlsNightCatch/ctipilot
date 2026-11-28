---
schema: 1
kind: threat
title: "Unit 42: more than ten campaigns in July to September 2026 ran autonomous AI agents from web-shell footholds on vulnerable web applications, with a command-gap median of 1.4 seconds, ===[Title]=== script headers and 40 to 100 unique Base64 payloads per session"
headline: "Unit 42: AI agents behind web shells in 10+ campaigns; hunt 1.4 s command gaps and ===[Title]=== headers"
summary: >
  Unit 42 tracked more than ten campaigns between July and September 2026 in which different attackers pointed autonomous AI agents at targets in sectors including government, logistics, manufacturing and education. Every campaign began with a web shell on a vulnerable web application, after which the agent did reconnaissance, credential harvesting, privilege escalation and lateral movement mostly with single-use scripts and no compiled implants. Unit 42 reports no new technique but measurable traces: a median gap of 1.4 seconds between commands in a subset of attacks (23.9 seconds in the human phase), section headers such as ===[Title]=== in every campaign, and 40 to 100 unique Base64 payloads per session.
discovered_at: "2026-11-25T04:40:00Z"
updated_at: null
event_date: "2026-11-24"
run_id: 2026-11-25T0356Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [global]
sectors: [public-sector, transport, manufacturing, education]
entities: [tool:cyberstrikeai]
techniques: [T1190, T1505.003, T1059.006, T1059.001, T1068, T1552.005, T1580, T1021.002, T1518.001, T1110.001]
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-11-24"
    role: primary
  - url: "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/"
    publisher: "ReliaQuest"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Once an AI operator took command, the median inter-command gap dropped to 1.4 seconds."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/"
  - quote: "In every campaign that we observed, AI operators used section headers in shell commands and scripts, such as ===[Title]===."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/"
verification: single-source
sourcing_note: "One vendor's telemetry; no victims are named, and the labelling of the activity as agentic is Unit 42's inference. Unit 42 says no behavioural marker links the activity to a specific model or framework. ReliaQuest corroborates only that the same address acted as a staging host with a CyberStrikeAI login page and says it could not tell whether that tool played a part in its own incident."
confidence: medium
references:
  - 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  - 2026-11-14/cyberstrikeai-aws-cloudtrail-intrusion-one-source-ip
  - 2026-10-09/reliaquest-llm-agents-spring-batch-tomcat-nashorn-system
  - 2026-11-25/bacs-first-confirmed-ai-agent-attacks-switzerland
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

Unit 42 tracked more than ten global campaigns between July and September 2026 in which different attackers deployed autonomous AI agents, against sectors including government, logistics, manufacturing, agriculture and education. Every campaign began with a web shell deployed through a vulnerable web application, typically supplied by the human operator, after which the agent did reconnaissance, credential harvesting, privilege escalation and lateral movement; Unit 42 names no product, CVE or flaw class for the entry vectors and says the novelty was speed and efficiency, not technique ([Unit 42, 2026-11-24](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)).

The traces: a median gap of 1.4 seconds between commands once an agent took over, against 23.9 seconds in the human phase of a subset of attacks; about 800 unique commands in 140 minutes in one case; section headers such as ===[Title]=== in shell commands and scripts in every campaign and step-by-step reasoning notes in more than half; 40 to 100 unique, target-tailored Base64 payloads per session; and no compiled implants, the arsenal being in most cases simple single-use scripts such as PHP web shells, PowerShell WMI backdoors and Python credential harvesters. The agents probed defences: the same find command ran on six endpoints excluding three security vendors, and one agent applied strace to the Microsoft Defender for Endpoint daemon ([Unit 42, 2026-11-24](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)).

The Copy Fail exploit recurred across several organisations; in a different attack sequence an agent tried the public PwnKit and CVE-2024-1086 binaries, then wrote custom C on the target and rewrote the exploit in Python, and Unit 42 saw agents try five techniques in sequence when earlier ones failed. In one AWS case it switched to IMDSv2 token acquisition after IMDSv1 was blocked and enumerated 20 services across eight regions; in another it pushed web shells to more than 40 locations on a Windows IIS server within 26 minutes, and Unit 42 describes another agent that found a vendor's GitLab credentials on a victim's web server and tried to brute-force access to that GitLab instance, exploiting no GitLab flaw ([Unit 42, 2026-11-24](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)).

Unit 42 found no behavioural marker tying the activity to a model or framework; a command-and-control address in one campaign also hosted a CyberStrikeAI instance, from which it infers the orchestration platform ([Unit 42, 2026-11-24](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)). ReliaQuest saw a credential-gated CyberStrikeAI login page on a staging host and could not determine whether the tool played a part ([ReliaQuest, 2026-10-07](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/)).

**Exposure:** internet-facing web servers that host a vulnerable web application; Unit 42 does not name the applications.

**Detection:** in process-lineage telemetry, shells and scripts spawned through a web shell's `sh -c` interface in bursts seconds apart, with ===[Title]=== headers or reasoning-style comments and many unique Base64 payloads; the same enumeration command across hosts excluding security-product directories, and tracing of the endpoint-security daemon; on cloud workloads, a switch to IMDSv2 token requests after IMDSv1 is blocked.

**Triage:** Base64 commands and reconnaissance appear in human-operated intrusions; Unit 42's discriminators are the volume and uniqueness of payloads, the command cadence and the headers, which it says rarely appear in human-operated attacks except with pre-coded scripts.

**Defender takeaway:** hunt web-server hosts for these traces, looking for volumes of single-use scripts rather than malware families, and close the web-tier entry first; enforce MFA, sign-in rate limiting and source-address restriction on services whose credentials sit on web servers, as Unit 42 advises for GitLab.
