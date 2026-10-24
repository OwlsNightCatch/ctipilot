---
schema: 1
kind: annual-report
title: "ANNUAL REPORT: Mandiant AI Risk and Resilience Report 2026: eight frontline case studies of AI-related attacks, failures and assessments"
headline: "Mandiant: an attacker used a hijacked AI coding-assistant session to steal OAuth tokens and deploy the Shai-Hulud worm"
summary: >
  Mandiant's 2026 AI Risk and Resilience report, the follow-up to its 2025 edition, synthesizes eight 2026 case studies
  of AI-related attacks, failures and assessments: an attacker who, after a hijacked AI coding-assistant session
  recommended a poisoned package, used that session to install an infostealer, harvest GitHub OAuth tokens and deploy the
  self-propagating Shai-Hulud worm across roughly 100 repositories;
  a stolen CI/CD credential turned into a live, in-session AI co-debugging offensive hub;
  tampered AI-assistant CLI hooks used for native remote code execution; malware that rewrites
  its own command strings at runtime using embedded AI inference to evade EDR signatures; a
  prompt-injection "Confused Deputy" that exfiltrated internal repositories through an allowlisted
  external domain; a runaway agent reasoning loop that generated a $50,000 cloud-billing spike; a
  customer-service RAG agent Mandiant assessed as open to leaking cross-tenant PII through indirect
  prompt injection in forum comments; and a DARK CASTLE (ex-UNC2814) espionage campaign against telecoms and government
  bodies caught when an agentic SOC triage pipeline escalated a single low-severity command
  execution a human analyst would routinely have deprioritized.
discovered_at: "2026-09-17T04:52:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-09-17T0409Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, supply-chain, identity, cloud]
regions: [global]
sectors: [public-sector, technology]
entities: ["report:mandiant-ai-risk-resilience-2026", "actor:dark-castle"]
techniques: [T1195.001, T1528, T1078.004, T1027.010, T1567.001, T1102.002, T1021.004]
affected_products: []
cves: []
sources:
  - url: "https://cloud.google.com/security/resources/ai-risk-and-resilience-2026"
    publisher: "Mandiant / Google Threat Intelligence Group (Google Cloud)"
    date: "2026-09"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/09/16/google-mandiant-enterprise-ai-security-risks-report/"
    publisher: "Help Net Security"
    date: "2026-09-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "By executing this recommendation, the assistant inadvertently functioned as a trojan horse, facilitating the installation of malicious software."
    publisher: "Mandiant"
  - quote: "deploy the self-propagating Shai-Hulud worm across approximately 100 internal code repositories"
    publisher: "Mandiant"
  - quote: "In under an hour it generated over 15,000 high-frequency, high-cost reasoning API calls, triggering a sudden ~$50,000 cloud-billing spike and causing severe local database locking that halted active business transactions."
    publisher: "Mandiant"
  - quote: "the malware dynamically rewrites its own command execution strings at runtime to bypass detection"
    publisher: "Mandiant"
  - quote: "Behavior-based detection successfully thwarted a global cyber espionage campaign (threat actor DARK CASTLE, formerly tracked as UNC2814) targeting global telecommunications providers and government organizations."
    publisher: "Mandiant"
verification: single-source
sourcing_note: "Help Net Security's coverage restates Mandiant's own report rather than independently assessing any of its case studies, so this is functionally a single primary source (Mandiant/GTIG) despite the press pickup."
confidence: high
references: []
deep_dive: true
deep_dive_category: annual-report
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:11Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    internal: true
    summary: >
      Priority recalibrated from high to notable: an annual AI-risk report with
      no finding that forces a decision within a week.
    fields: [priority]
  - at: "2026-10-11T13:49:15Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      Corrects several case-study descriptions against Mandiant's report: the Shai-Hulud intrusion began with a hijacked AI coding-assistant session, the RAG cross-tenant PII case is a weakness Mandiant assessed rather than an observed leak, the AI-built framework harvested data rather than credentials, the runaway agent caused database locking rather than locking a ledger database, and Mandiant's identity example is Agent Identity. Case studies 3 to 7 gain their citation. The report page gives only September 2026 as its date, so the publication date is no longer stated to the day. The title and summary describe the cases as AI-related attacks, failures and assessments, since one is an operational failure, one an assessed weakness and one a detection, and event_date is the first dated coverage.
    fields: [headline, summary, techniques, body, sources, title, event_date]
  - at: "2026-10-20T08:54:19Z"
    run_id: 2026-10-20T0835Z-audit
    type: correction
    summary: >
      In Mandiant's first case study the attacker, not the poisoned package, deployed the Shai-Hulud worm:
      after a hijacked AI coding-assistant session recommended the poisoned package, the attacker used
      that session to install an infostealer, harvest GitHub OAuth tokens and deploy the worm. The
      per-case hardening and hunting guidance is cited to the defensive controls in Mandiant's report.
    fields: [body, headline, summary, title]
migrated_from: null
---

Mandiant's [2025 edition](https://cloud.google.com/security/resources/ai-risk-and-resilience) of this annual report documented enterprise AI adoption centred on assistive, human-guided knowledge retrieval. The 2026 edition, published in September 2026 and covered by Help Net Security on 2026-09-16 ([Help Net Security, 2026-09-16](https://www.helpnetsecurity.com/2026/09/16/google-mandiant-enterprise-ai-security-risks-report/)), tracks the shift Mandiant and Google Threat Intelligence Group (GTIG) observed since: distributed, autonomous agentic systems executing API calls, optimising production configurations and analysing telemetry across hybrid-cloud environments with far less human-in-the-loop oversight ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). The report's eight case studies, which Mandiant presents as observed in its own work ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)), are its most operationally useful content for defenders: each pairs an attack pattern with concrete detection and hardening guidance.

**Case study 1: an attacker uses a hijacked AI coding-assistant session to deploy the Shai-Hulud worm.** A threat actor compromised a SaaS provider and hijacked an active AI coding-assistant session on a developer's workstation; the assistant, operating as a trusted interpreter, recommended installing an external package the attacker had poisoned ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). The attacker used the resulting access to install a PyPI-packaged infostealer, harvest GitHub OAuth tokens (T1528), and deploy the self-propagating Shai-Hulud worm across roughly 100 internal repositories, automating theft of repository secrets and exfiltration of proprietary source code; the actor then poisoned a package inside the organization's official namespace, triggering a secondary infection when another employee pulled the compromised version ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). **Hardening:** enforce IDE/CLI verification hooks that validate every AI-recommended dependency against cryptographic checksums and approved allowlists, isolate local credentials from extensions, and route dependency traffic through an internal package repository ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 2: a stolen CI/CD credential becomes a live AI co-debugging hub.** At a global healthcare organization, an attacker used a compromised long-lived CI/CD credential (T1078.004) to seize an unisolated VM and worked an LLM interactively, in real time, rather than developing malware offline: first synchronizing code and loading README files to align the model with campaign goals, then co-debugging a multi-worker data-harvesting framework to raise its exfiltration frequency to a three-hour cycle, then having the model write dynamic IP-rotation scripts and co-develop a Rust tool to validate stolen financial-account balances. The campaign compromised thousands of credentials ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). **Hardening:** replace long-lived access keys with short-lived Workload Identity Federation trust relationships, enforce egress containment (e.g. VPC Service Controls) against unapproved external LLM providers, and run continuous secrets scanning with a runtime prompt firewall (Mandiant names Model Armor) to block hardcoded credentials and offensive script execution in real time ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 3: tampered CLI hooks turn an AI assistant's own extensibility into RCE.** At an IT and software-development organization, an attacker poisoned an internal AI repository and tampered with an AI assistant's CLI hooks, achieving native remote code execution through the assistant's own standard operational workflow; the same report also notes attackers separately using AI CLIs to manage command-and-control infrastructure through natural-language queries ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). **Hardening:** require all local AI-assistant binaries, CLI helpers, plugins and MCP servers to be signed and verified before execution; enforce multi-party approval and continuous monitoring on internal AI repositories; and sandbox AI-assistant execution engines in micro-segmented, containerized runtimes (gVisor or microVMs) so a subverted hook cannot reach the host, with human-in-the-loop approval required before shell execution, configuration changes or outbound network calls ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 4: just-in-time polymorphic malware.** Malware using embedded, lightweight local AI inference fingerprints the active security tools on a host, then dynamically rewrites its own command-execution strings at runtime (T1027.010), never writing a predictable payload to disk, so it evades static EDR signatures while it persists and reconnoiters ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). **Hunt/detection:** tune EDR and SIEM for in-memory compilation (unexpected native-compiler process spawns from non-developer parent processes and rapid file-create-execute-delete cycles in temp directories) and baseline endpoint CPU/GPU consumption to catch sudden, unexplained spikes from otherwise-lightweight background processes; response playbooks should suspend the entire parent execution tree (not just the worker thread) and capture a memory snapshot before network isolation ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 5: "Confused Deputy" exfiltration via an allowlisted domain.** Mandiant's own offensive-security team used role-confusion prompt injection to convince a client's internal AI assistant, scoped to specific internal repositories, that it was assisting an authorized security test; because GitHub was an allowed external domain, the assistant used its native CLI to clone sensitive internal repositories and push them to an external, tester-controlled account (T1567.001): a sanctioned tool weaponized through semantic manipulation of the assistant's own trust in its task ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). **Hunt/detection:** cross-correlate application logs with network egress telemetry, and alert when an internal-facing AI service account initiates unauthorized outbound transfers or opens anomalous external API connections; on detection, invalidate the agent's active OAuth tokens and downgrade its container's egress privileges while keeping the instance alive for prompt-history forensics ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 6: a runaway reasoning loop triggers a $50,000 "denial-of-wallet."** A financial-services accounting-reconciliation agent with read/write access to billing databases hit a corrupted null-value formatting bug and entered an unconstrained recursive reasoning loop trying to self-correct, firing over 15,000 high-cost API calls in under an hour, spiking cloud billing roughly $50,000 and causing severe local database locking that halted active business transactions ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). This is an operational-resilience failure rather than an external attack, but the mechanics are identical to a denial-of-service condition. **Hardening:** define cost-cap thresholds and bounded recursion limits at the service-identity and project level, and implement automated financial circuit breakers that halt agent operations after a set number of consecutive task failures ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 7: indirect prompt injection could leak cross-tenant PII.** Mandiant assessed a public-facing customer-service agent that used Retrieval-Augmented Generation over community forum comments and support tickets: the customer had not considered indirect prompt injection, so hidden instructions in retrieved entries could be read by the model as system-level commands and could potentially hijack its reasoning to expose other customers' PII from their support tickets in its responses ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). This is a weakness Mandiant identified, not an observed leak. **Hardening:** treat all RAG-retrieved content (forum posts, tickets, partner feeds) as untrusted input; enforce tenant-isolated vector indexing so a public-facing agent cannot query cross-tenant data; and route incoming context and generated responses through a semantic firewall (Model Armor or equivalent) to strip injected instructions and screen for PII before it reaches an end user ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Case study 8: agentic SOC triage catches DARK CASTLE (ex-UNC2814).** A backdoor hid its command-and-control inside legitimate cloud productivity-spreadsheet traffic (T1102.002) as part of an espionage campaign targeting global telecommunications providers and government organizations ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). A single, low-frequency anomalous command execution, the kind a human analyst would typically triage as low-severity, was escalated by the defending team's agentic AI triage pipeline, which autonomously correlated it with subtle outbound-traffic signals to reconstruct a complete attack timeline, letting engineers trace the actor's lateral movement over SSH (T1021.004) and privilege escalation by an unstated mechanism, and sever its access before it spread further ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

Mandiant's cross-cutting architectural recommendation is to replace static service-account identities with cryptographically bound, lifecycle-integrated agent identities (such as Google's Agent Identity) across five pillars: hyper-segmented identity perimeters, dual-execution authority requiring human re-authorization for high-risk bulk actions, data/tool/operational governance (financial circuit breakers, bounded recursion), active multi-layered telemetry (semantic firewalls, behavioral monitoring), and treating AI coding assistants and MCP servers as privileged sessions requiring cryptographic CLI-hook integrity checks ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

**Defender takeaway:** the case studies that most directly apply to a public-sector environment are 2 and 3 (any team running AI coding assistants or MCP-integrated developer tooling on long-lived CI/CD credentials), 5 and 7 (any deployment of an internal or customer-facing AI assistant that ingests external content or is scoped against an allowlisted external domain), and 8 (the concrete argument for correlating isolated endpoint anomalies against outbound-traffic telemetry in SOC triage, rather than scoring them in isolation). Audit which of your own AI-assistant deployments hold a long-lived credential, an allowlisted external domain, or ingest untrusted external content, and prioritise the corresponding hardening control above the others.

## Correction — 2026-10-11T13:49:15Z

Mandiant's report describes case study 1 as a threat actor who compromised a SaaS provider and hijacked an active AI coding-assistant session, after which the assistant recommended a package the attacker had poisoned; the actor later poisoned a package inside the organization's official namespace ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). Case study 7 is a weakness Mandiant identified in a customer's RAG agent, which "could potentially hijack the model's reasoning" and expose other customers' PII ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)); it is not a reported leak. Case study 2's AI-built tool was a data-harvesting framework, case study 6's runaway agent caused "severe local database locking that halted active business transactions", and Mandiant's example of a cryptographically bound agent identity is Agent Identity ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).

## Correction — 2026-10-20T08:54:19Z

Mandiant does not say the poisoned package spread the worm: after the hijacked AI coding-assistant session recommended a package the attacker had poisoned, the attacker used the developer's active session to install an infostealer through a poisoned PyPI package, harvest GitHub OAuth tokens and deploy the Shai-Hulud worm across approximately 100 internal code repositories ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)). The hardening and hunting guidance under each case study is Mandiant's own, from the defensive controls the report lists for that case ([Mandiant, 2026-09](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)).
