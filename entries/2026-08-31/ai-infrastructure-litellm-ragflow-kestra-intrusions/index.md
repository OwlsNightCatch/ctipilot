---
schema: 1
kind: threat
title: "AI infrastructure as the new control plane: Microsoft confirms three separate intrusions against a LiteLLM gateway, a RAGFlow deployment and a Kestra orchestration environment, converging on credential theft and persistence, with compute monetisation in two of the three"
headline: "Three unrelated AI platforms, three intrusions, one pattern: gateways and orchestrators concentrate the credentials and execution privilege attackers want"
summary: >
  Microsoft Threat Intelligence confirms three separate real-world intrusions against exposed AI
  infrastructure: a LiteLLM gateway compromised via CVE-2026-42271 chained with CVE-2026-48710, a
  RAGFlow deployment reached through an unattributed code-execution path, and a Kestra workflow
  environment exploited via CVE-2026-49869. Credential harvesting and durable persistence recurred
  across all three despite different initial-access paths; compute monetisation followed in the
  LiteLLM and Kestra intrusions but not RAGFlow's, whose objective was narrower credential
  interception. Together they establish AI gateways, retrieval platforms and orchestration services
  as a distinct, high-value attack surface.
discovered_at: "2026-08-31T05:25:00Z"
updated_at: null
event_date: "2026-08-26"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [cloud, vulnerabilities, actively-exploited, cryptocrime]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190, T1059.006, T1059.004, T1552.001, T1057, T1518, T1036.005, T1564.001, T1496, T1098.004, T1053.003, T1222.002, T1505, T1071.001, T1095, T1105]
affected_products: ["BerriAI LiteLLM", "RAGFlow", "Kestra"]
cves:
  - id: CVE-2026-42271
    cvss: "8.7"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [cisa-kev, exploited, patch-available]
    affected: ">= 1.74.2, < 1.83.7"
    fixed: "1.83.7"
  - id: CVE-2026-48710
    cvss: "6.5"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "<= 1.0.0"
    fixed: "1.0.1"
  - id: CVE-2026-49869
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "prior to 1.0.45 and 1.3.21"
    fixed: "1.0.45 / 1.3.21"
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-08-26"
    role: primary
  - url: "https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g"
    publisher: "BerriAI (GitHub Security Advisory)"
    date: "2026-06-09"
    role: corroborating
  - url: "https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr"
    publisher: "Starlette / Kludex (GitHub Security Advisory)"
    date: "2026-05-30"
    role: corroborating
  - url: "https://vulnerability.circl.lu/vuln/CVE-2026-49869"
    publisher: "CVE Program (via CIRCL Vulnerability-Lookup, sourcing Kestra's GHSA-5vc5-wxxq-3fjx)"
    date: "2026-06-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Microsoft assesses with high confidence that initial access likely occurred through exploitation of the exposed LiteLLM gateway surface. Relevant public vulnerability paths include CVE-2026-42271, an authenticated command-execution issue in LiteLLM MCP stdio test endpoints, and the route described in public research that chains this flaw with CVE-2026-48710, a Starlette host-header validation bypass, to achieve unauthenticated remote code execution in vulnerable exposed deployments."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"
  - quote: "Telemetry showed the payload reading /proc/1/environ, filtering for keywords such as master, API key, token, password, and UI-related fields, then sending collected values to attacker-controlled infrastructure."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"
  - quote: "Microsoft assesses with high confidence that initial access likely occurred through exploitation of CVE-2026-49869, a critical authentication-bypass vulnerability in Kestra. Exploitation could allow an unauthenticated remote attacker with network access to bypass the login mechanism, define a malicious workflow using the Process runner, and trigger worker-side shell-script execution."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"
verification: single-source
sourcing_note: "First-party Microsoft telemetry from its own detection surface. Microsoft states high confidence in the LiteLLM and Kestra initial-access assessments, and explicitly low confidence in which vulnerability, if any, enabled the RAGFlow intrusion — that uncertainty is preserved in the body rather than resolved."
confidence: high
references: ["2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti", "2026-05-30/cve-2026-48710-badhost-starlette-fastapi-vllm-litellm-mcp-sd"]
deep_dive: true
deep_dive_category: cloud-saas
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Audit every internet-reachable LiteLLM, RAGFlow or Kestra deployment for direct exposure of admin/management interfaces; patch LiteLLM against CVE-2026-42271/CVE-2026-48710 and Kestra against CVE-2026-49869 immediately, and rotate every credential (model-provider keys, LiteLLM master key, database connection strings) that gateway process could have held, since a patch alone does not invalidate an already-exposed secret."
updates: []
migrated_from: null
---

AI gateways, retrieval platforms and workflow orchestrators have become a new layer of enterprise infrastructure sitting between users, applications, data and models — and that position concentrates credentials, data access and execution privilege in one runtime. Microsoft Threat Intelligence confirms three separate real-world intrusions exploiting exactly that concentration: a LiteLLM gateway, a RAGFlow retrieval-augmented-generation deployment, and a Kestra workflow orchestration environment. The initial-access paths differed by product, and credential theft and durable persistence recur across all three, but resource monetisation was specific to two of them: Microsoft states the LiteLLM and Kestra objectives each included compute monetisation, while the RAGFlow intrusion's objective was narrower — intercepting newly configured LLM provider credentials and model metadata, with no miner deployment observed ([Microsoft Threat Intelligence, 2026-08-26](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)). The June 2026 disclosure of the LiteLLM chain itself is already tracked in this store; what is new here is confirmation that the chain reached real production environments, alongside two further distinct AI-workload intrusions with no vulnerability overlap.

## Case 1: LiteLLM gateway — credential harvesting to database exfiltration to cryptomining

Microsoft assesses with high confidence that initial access exploited the exposed LiteLLM gateway surface via CVE-2026-42271 (CVSS 8.7, affecting LiteLLM >= 1.74.2 and < 1.83.7, fixed in 1.83.7 — [BerriAI GHSA-v4p8-mg3p-g94g](https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g)), a command-execution flaw in LiteLLM's MCP stdio test endpoints, chained with CVE-2026-48710 (CVSS 6.5, affecting Starlette <= 1.0.0, fixed in 1.0.1 — [Starlette GHSA-86qp-5c8j-p5mr](https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr)), a host-header validation bypass that can strip the authentication requirement in vulnerable configurations — the combination yields unauthenticated remote code execution in the gateway process itself. From that foothold, the observed chain ran six stages. First, the payload read `/proc/1/environ` — the environment block of the gateway's PID-1 process in its container — filtering for provider API keys, the LiteLLM master key, database connection strings and other credential-shaped values, and exfiltrated them using whichever of Python's `urllib`, `curl` or `wget` was available. Second, a masqueraded ELF binary was retrieved and launched with Linux-service-style arguments; a parallel shell-based delivery path provided redundancy. Third, the payload fingerprinted the host, checked for passwordless sudo, and swept for competing miners or remote-access tooling. Fourth, it loaded the Linux MSR kernel module with write access — RandomX/XMRig CPU-tuning behaviour — and rewrote crontab entries to remove rival miners before installing its own. Fifth, using the harvested `DATABASE_URL`, it connected directly to the LiteLLM-backed Azure Database for PostgreSQL instance and dumped the `LiteLLM_ProxyModelTable` and `LiteLLM_VerificationToken` tables — model configuration, upstream provider keys and proxy-issued virtual keys — base64-encoding and exfiltrating the output in chunks to an out-of-band endpoint. Sixth, it established durable access via an SSH key written to a service account, immutable-flag protection on its payload directories, and periodic callbacks confirming continued execution.

## Case 2: RAGFlow — a persistent hook inside the application itself

Microsoft assesses with high confidence that the RAGFlow intrusion also began with exploitation of the exposed application surface, but states explicitly it has only low confidence in which specific vulnerability enabled the resulting code execution — telemetry could not isolate the precise execution sink from inside the RAGFlow Flask service process. Several publicly documented RAGFlow vulnerabilities provide plausible technical context without being confirmed as the cause. What followed exploitation was distinctive: the payload located the RAGFlow install from inside the container, identified the tenant LLM configuration code path, and modified the application's own startup/import sequence so a hidden hook would load every time the service started — persistence implemented as a backdoored application component rather than a separate process, surviving container restarts as long as the modified filesystem state remains. The hook then wrapped the tenant LLM configuration flow itself, capturing provider type, model name, API key material and endpoint metadata every time a user configured a new LLM connection from that point forward, and exfiltrated it over outbound HTTP with errors suppressed so the application kept functioning normally. Unlike the LiteLLM case, Microsoft observed no miner deployment or interactive shell here — the objective was narrowly future-credential interception.

## Case 3: Kestra — workflow execution as the shell-access primitive

Microsoft assesses with high confidence that the Kestra intrusion exploited CVE-2026-49869 (CVSS 10.0 Critical, affecting Kestra prior to 1.0.45 and 1.3.21, fixed in those releases — [Kestra GHSA-5vc5-wxxq-3fjx via the CVE Program](https://vulnerability.circl.lu/vuln/CVE-2026-49869)), a pre-authentication bypass that lets an unauthenticated, network-reachable attacker skip the login mechanism entirely, define a malicious workflow using Kestra's Process runner, and trigger shell-script execution on a worker node. Two closely timed workflow-origin shell sessions followed: the first performed shell initialisation, the second executed the main follow-on actions. Because the worker had access to the mounted Docker socket, the attacker queried container metadata and enumerated the `Config.Env` arrays of every other container reachable through that socket — a single compromised orchestration worker exposing the environment-embedded cloud keys, database passwords and API tokens of unrelated containers on the same host. A cryptominer (XMRig, RandomX-tuned) was then deployed, and a later workflow-origin event retrieved and executed a remote script via a curl-pipe-shell pattern with no file ever written to disk, storing its output through Kestra's own key-value interface rather than a standalone file.

## The pattern that matters more than any single product

Initial access differed — command execution from a gateway process, SSRF-then-RCE against a web application, and workflow-engine authentication bypass — but credential collection and durable access converged in all three; resource monetisation converged in two of the three (LiteLLM's cryptomining, Kestra's XMRig deployment on the compromised worker), while the RAGFlow intrusion pursued only future-credential interception with no miner or interactive shell observed ([Microsoft Threat Intelligence, 2026-08-26](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)). Microsoft's own framing is the operational takeaway: these platforms should be monitored according to their control-plane role, not as isolated applications, because a gateway, retrieval or orchestration service can concentrate credentials, database access, workflow execution and container privileges in one runtime. Correlating an unexpected shell or interpreter spawned from an AI-workload process with subsequent secret access, application-file modification, Docker-socket use, outbound callbacks and resource-hijacking activity exposes this class of attack earlier than any single product-specific indicator ([Microsoft Threat Intelligence, 2026-08-26](https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/)).

**Defender takeaway:** treat internet-reachable AI gateways, retrieval platforms and orchestrators as Tier-0 secrets stores, not as ordinary applications. Require authentication on every API and UI surface, never expose management interfaces directly to the internet, issue scoped per-team virtual keys rather than sharing master keys, and store upstream provider credentials in a managed secret store rather than process environment variables. Restrict database access for the gateway's service account to the minimum required objects, and mount container temporary directories non-executable where feasible. Detection concepts: any AI-gateway, retrieval or orchestration process spawning a shell, downloader or scripting interpreter is the earliest high-value pivot — this is not expected behaviour for normal model-routing, retrieval or workflow-scheduling activity; command-line references to `/proc/1/environ`, `DATABASE_URL` or PostgreSQL client libraries appearing anywhere in that process's descendant commands are a strong secondary signal; and unfamiliar Docker-socket access from an orchestration worker, or configuration files inside an AI application's own source tree changing outside a deployment window, both warrant investigation. **Triage:** administrative maintenance of these platforms is itself process-heavy and can resemble the early stages of this pattern; the discriminator is process ancestry combined with destination — a gateway process's child shell reaching outbound to raw-IP infrastructure or an out-of-band callback domain, rather than to the model-provider or database endpoints the platform is configured to reach, separates compromise from routine operation.
