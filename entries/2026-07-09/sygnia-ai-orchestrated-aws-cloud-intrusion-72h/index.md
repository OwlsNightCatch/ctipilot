---
schema: 1
kind: research
title: "Sygnia: an AI-orchestrated AWS intrusion reached broad compromise in ~72 hours — four keys from four accounts used from one source in the same second"
headline: "Sygnia IR: an AI-assisted AWS intrusion ran four parallel workstreams per stolen key and used four accounts' keys in one second"
summary: >
  Sygnia's incident response into a financially-motivated AWS intrusion found no novel
  malware or zero-day — every technique maps to a known MITRE ATT&CK ID — but the tempo
  and parallelism point to AI-assisted/agentic tooling: initial access to broad compromise
  in ~72h, and four access keys from four separate accounts used from one source IP and
  user-agent within a single observed second. The detection signal is the orchestration,
  not the individual actions. Defenders should pre-build minutes-not-hours containment and
  alert on one source authenticating with multiple distinct keys in a tight window.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-08"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, cloud, organized-crime]
regions: [global]
sectors: [public-sector, finance, telco, energy]
entities: []
cves: []
sources:
  - url: "https://www.sygnia.co/blog/inside-an-ai-assisted-cloud-attack/"
    publisher: "Sygnia"
    date: "2026-07-08"
    role: primary
closed_sources: []
evidence:
  - quote: "In one observed second, four different access keys belonging to four separate accounts were used from the same source IP address and the same user-agent"
    publisher: "Sygnia"
  - quote: "The intrusion progressed from initial access to broad cloud compromise within approximately 72 hours."
    publisher: "Sygnia"
  - quote: "multiple attacker-created artifacts were framed as part of a 'pentest' or a 'red team'. This framing appeared in branch names, commit messages, and other artifacts, including references suggesting the activity was approved by a non-existent CEO."
    publisher: "Sygnia"
verification: single-source
sourcing_note: "Single-source: Sygnia (Admiralty B) incident-response analysis of one engagement; the AI-orchestration assessment is Sygnia's, drawn from observed tempo/artefacts rather than confirmed attacker tooling — framed as assessed, not proven."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions:
  - "Alert on a single source IP/user-agent authenticating with multiple distinct IAM access keys or accounts within seconds, and on repeated re-execution of the same discovery/secrets-harvesting sequence triggered by newly-created credentials."
  - "Assume any exposed credential is used immediately and at scale: automate secrets rotation, IP-allowlist cloud management planes, enforce MFA on privileged/external access, and pre-build containment playbooks (isolation + rotation + session revocation) that execute in minutes."
migrated_from: null
---

Sygnia's incident-response investigation of a financially-motivated AWS cloud intrusion found no novel malware or zero-day — every individual technique maps to a long-tracked MITRE ATT&CK ID — but the operationalisation was materially faster than typical manual intrusions, which Sygnia attributes to AI-assisted or agentic tooling ([Sygnia, 2026-07-08](https://www.sygnia.co/blog/inside-an-ai-assisted-cloud-attack/)). After obtaining an initial access key via a weakness in an internet-facing application, the actor ran four workstreams in parallel — secrets theft (ECS/EC2 environment variables, GitHub/Bitbucket CI/CD runner env vars, S3 plaintext secrets, Secrets Manager, SSM Parameter Store); persistence (new IAM users, EC2/ECS reverse shells, modified deployment files); RDS exfiltration via several hundred distinct SQL queries across dozens of databases; and reversible impact (S3 access denial, ECS scaled to zero, SQS purges) used purely as extortion leverage — and repeated the full playbook on every newly obtained credential rather than progressing linearly. The most striking artefact: four different AWS access keys from four separate accounts were used from the same source IP and user-agent within a single observed second, which Sygnia assesses is very hard to explain as manual operation ([Sygnia, 2026-07-08](https://www.sygnia.co/blog/inside-an-ai-assisted-cloud-attack/)).

Scripts, structured reporting output, and commit messages/branch names framing the activity as an authorized "pentest"/"red team" with a fabricated CEO sign-off are consistent with LLM-generated tooling — possibly including prompt-framing meant to reduce refusal from AI assistants being abused by the operator. Sygnia maps the case onto the same tactic distribution (Execution, Discovery, Credential Access, Collection, Defense Evasion) that Anthropic's June 2026 LLM ATT&CK research found concentrated in banned AI-abuse accounts. Relevant IDs per Sygnia include `T1651 Cloud Administration Command`, `T1552/T1528` (credential/token harvesting), `T1087/T1580/T1619` (account/cloud-infra/storage discovery re-run per key), `T1578` (modify cloud compute infra) and `T1078 Valid Accounts`.

**Defender takeaway:** for a Swiss/EU public-sector estate mid-cloud-migration running AWS with GitHub/Bitbucket CI/CD, the lesson is tempo. The ATT&CK-mappable individual actions are not the alarm — the orchestration is: one source authenticating with multiple distinct keys/accounts in seconds, and the same secrets-harvesting sequence re-firing on each new credential. Because manual response cannot keep pace, containment (network isolation, credential rotation, session revocation) has to be pre-built to run in minutes, and every exposed credential must be assumed used instantly and at scale.
