---
schema: 1
kind: threat
title: "LLMjacking: stolen cloud identities and keys enable managed model services in victim accounts and resell the quota through proxy gateways (GTIG and Mandiant), with control-plane hunting guidance for AWS, Azure and Google Cloud"
headline: "GTIG: stolen cloud keys enable Bedrock and Gemini model services, then resell the quota; hunt the control-plane logs"
summary: >
  GTIG and Mandiant report 2026 incident-response cases in which actors used exposed or stolen cloud identity tokens (IAM credentials, service-account keys, GitHub tokens) for initial access and then enabled managed model services such as Amazon Bedrock and the Gemini API in victim accounts, ran up charges above USD 100,000 in a single day and resold the quota through proxy gateways. Wiz describes a Google Cloud billing-account variant and Datadog the validation of stolen AWS keys for Bedrock; GTIG lists the audit-log events to watch in AWS, Azure and Google Cloud.
discovered_at: "2026-11-09T03:26:00Z"
updated_at: null
event_date: "2026-11-02"
run_id: 2026-11-09T0255Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, cloud, identity, organized-crime]
regions: [global]
sectors: [finance, retail, technology, transport]
entities: ["actor:unc6993", "product:litellm"]
techniques: [T1078.004, T1528, T1550.001, T1552.001, T1190, T1566, T1583.008, T1580, T1555.006, T1213.003, T1548.005, T1530, T1098.001, T1098.003, T1136.003, T1098.004, T1496.004]
affected_products: ["Amazon Bedrock", "Google Gemini Enterprise Agent Platform", "Microsoft Azure", "LiteLLM", "Ollama"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models"
    publisher: "Google Threat Intelligence Group and Mandiant"
    date: "2026-11-02"
    role: primary
  - url: "https://threats.wiz.io/all-incidents/threat-actors-targeting-gcp-billing-accounts-for-llm-usage"
    publisher: "Wiz (Cloud Threat Landscape)"
    date: "2026-10-20"
    role: corroborating
  - url: "https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/"
    publisher: "Datadog Security Labs"
    date: "2026-10-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the dominant initial access vector has been exposed or stolen cloud identity tokens"
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models"
  - quote: "In multiple incidents that Mandiant investigated, LLM services were not enabled at the time of compromise."
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models"
  - quote: "Gemini Enterprise Agent Platform inference operations are contained within Data Access logs, which are disabled by default due to volume and ingestion costs."
    publisher: "Google Threat Intelligence Group and Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models"
  - quote: "Wiz identified threat actors hijacking Google Cloud Platform (GCP) billing accounts via search-ad phishing to fund unauthorized Gemini API usage."
    publisher: "Wiz"
    source_url: "https://threats.wiz.io/all-incidents/threat-actors-targeting-gcp-billing-accounts-for-llm-usage"
  - quote: "Valid credentials then undergo a separate check for Bedrock access"
    publisher: "Datadog Security Labs"
    source_url: "https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/"
verification: multi-source
sourcing_note: >
  The case details and the UNC6993 cluster rest on GTIG and Mandiant's own incident-response work. Wiz and Datadog describe different variants (Google Cloud billing accounts, AWS key validation) from their own telemetry, so they corroborate the pattern, not GTIG's individual cases. Datadog's AWS evidence is one platform's frontend code, two validation scripts and similar probing it saw at 12 of its customer organizations, which it does not link to those tools.
confidence: high
references: ["2026-08-07/ai-api-token-jacking-transfer-station-resale"]
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

Mandiant responded to multiple 2026 incidents in which actors hijacked enterprise access to large language models ("LLMJacking") with charges above USD 100,000 in a single day ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). The dominant initial access was exposed or stolen cloud identity tokens (IAM credentials, service-account keys, GitHub tokens, session tokens). One actor harvested LLM API keys from public GitHub repositories and validated them with single-token requests that stayed under EDR and SIEM volume alerts; another scripted calls against exposed Ollama endpoints to register its own models; cluster UNC6993 had users paste a raw JSON payload holding an active access token into a fake application-portal page, which bypasses password and MFA ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)).

After the foothold the actors enumerated cloud services and repositories for credentials, took secrets from cloud secret managers, created unauthorized IAM and service accounts, attached administrative policies to service roles and injected SSH keys into compute instances or instance metadata; one rotated short-lived service accounts to get around rate limits ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). In multiple incidents the model services were not enabled at compromise, and the stolen keys were used to enable them and to create further API keys ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). A follow-on cluster holding pre-validated virtual keys exploited the victim's LiteLLM gateway at its /key/regenerate endpoint to lift standard virtual keys to proxy-admin credentials ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). "LLM Mixers" proxy, aggregate and resell the stolen access; UNC6993 used the open-source new-api and gcli2api gateways ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)).

**Exposure:** any cloud account where a stolen identity, key or token can enable or call a managed model service (Amazon Bedrock, Azure's Microsoft.CognitiveServices, the Gemini Enterprise Agent Platform), and any model endpoint reachable from the internet; accounts with model services not enabled are in scope too, because the actors enabled them ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). Azure model invocations need Diagnostic Logs, and Gemini Agent Platform inference calls appear only in Data Access logs, which are off by default ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)).

**Detection:** cloud control-plane audit logs first; GTIG says to treat any unauthorized enablement of LLM services as a critical security event. In AWS CloudTrail, events from bedrock.amazonaws.com (Converse, InvokeModel, ListFoundationModels, PutUseCaseForModelAccess); in Azure, Microsoft.CognitiveServices/accounts/deployments/write and diagnostic-setting changes; in Google Cloud, ServiceUsage.EnableService for the Agent Platform and, with Data Access logs on, Predict and GenerateContent calls ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). Validation sweeps show in gateway logs as unusually small requests such as max_tokens=1; GTIG suggests reading user agents for automation SDKs (aws-sdk-go-v2, aws-sdk-rust, claude-cli) ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). Datadog saw similar probing at 12 organizations in 30 days, mostly as failed ListFoundationModels calls across several regions ([Datadog, 2026-10-06](https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/)). Wiz's Google Cloud variant starts with search-ad phishing and ends with external billing administrators and foreign projects linked to the billing account ([Wiz, 2026-10-20](https://threats.wiz.io/all-incidents/threat-actors-targeting-gcp-billing-accounts-for-llm-usage)); watch for both. GTIG describes new IAM and service accounts, policy attachments and SSH keys as the actors' persistence, so review those after revoking a stolen key ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)).

**Triage:** GTIG treats any call that disables model invocation logging, made by a principal outside infrastructure-as-code, as high severity ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)).

**Defender takeaway:** deny model-service permissions to identities that do not need them, set per-model quotas and spending caps, patch model gateways such as LiteLLM, and alert on any enablement of a model service or call that disables its logging ([GTIG, 2026-11-02](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)). Switch on model-call logging where it is not on by default, or inference calls go unseen.
