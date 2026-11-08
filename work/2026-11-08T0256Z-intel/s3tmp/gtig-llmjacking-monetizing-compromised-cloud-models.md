---
title: "The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources | Google Cloud Blog"
author: Google Threat Intelligence Group; Mandiant
url: https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models
hostname: google.com
description: Mandiant reveals how LLMJacking attacks cost victims hundreds of thousands in fraudulent cloud bills, with underground markets targeting LLM credentials.
sitename: Google Cloud Blog
date: "2026-11-02"
tags: ['Threat Intelligence']
fingerprint: "253b9ddbcf9ec580"
---
# The Rise of LLMJacking: How Threat Actors Monetize Compromised Cloud and Model Resources

##### Google Threat Intelligence Group

##### Mandiant

Written by: Christopher Romano, Codi Starks, Garrett Mahoney, John Wolfram, Josh Murchie, K Singh, Mathew Potaczek, Mike Lombardi, Rik Dolfing

### Introduction 

Mandiant responded to multiple incidents in 2026 in which threat actors hijacked enterprise access to Large Language Models (LLMs), a tactic known as "LLMJacking." Spanning a variety of cloud and LLM providers, these intrusions impacted organizations in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors.

Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours. Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked.

Figure 1: Usage chart showing LLMJacking generating a spike in API requests

Analyzing the criminal ecosystem behind these frontline compromises, and building upon [previous reporting](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) on the growing underground market for LLM credentials, Google Threat Intelligence Group (GTIG) has identified a diverse set of financially motivated threat clusters operating out of multiple regions globally.

As the LLMJacking ecosystem matures, we are also tracking a division of labor between threat actors establishing initial access to compromised environments and operators managing downstream monetization infrastructure, known as “LLM Mixers”. LLM Mixers function as illicit routing gateways that proxy, aggregate, and resell unauthorized LLM access to underground subscribers. In one investigation, GTIG observed two distinct operational clusters coordinating to compromise and monetize enterprise LLM infrastructure, demonstrating the sophisticated specialization emerging in this space.

In this blog post, we describe the attack lifecycle observed across recent LLMJacking investigations and provide actionable detection, hardening, and remediation guidance to help organizations secure their infrastructure.

### Initial Access

While low-level resource theft has involved the [manipulation of customer support chatbots](https://www.cio.com/article/4155404/ai-token-freeloaders-are-coming-for-your-customer-support-chatbot.html) to conduct unauthorized tasks like code generation, threat actors conducting LLMJacking bypass these front-end interfaces to target backend model resources directly. Specifically, they focus on either identifying publicly exposed LLM endpoints or obtaining valid LLM application programming interface (API) keys. An example of the latter can be seen in Figure 1, where a threat actor uses an automated script to verify exposure by calling the `/api/create` endpoint to independently run their own models on endpoints that unsuspecting users have left publicly accessible. Leaving these services unprotected not only expands an organization's traditional attack surface, but could also introduce a significant increase in hosting costs.

Figure 2: Threat Actor tests publicly exposed Ollama endpoints and attempts to register their own models

Across multiple LLMJacking investigations, however, the dominant initial access vector has been exposed or stolen cloud identity tokens—including IAM credentials, Service Account keys, GitHub Personal Access Tokens (PATs), and active session tokens—which threat actors leverage to establish an initial foothold into target organizations' infrastructure.

For instance, in mid-2026 UNC6993 compromised a cloud instance through a misconfigured Service Account key and used this access to grant further access to an LLM API. UNC6993 also hosted a session hijacking page masquerading as an application portal to join a group of LLM users. This page tricks users into navigating to the legitimate LLM service website, and pasting their raw JSON payload containing an active access token, which was then posted to the backend API to bypass password and multifactor authentication (MFA) controls.

In another instance, one threat actor gained initial entry by combining a stolen Personal Access Token (PAT) to access private code repositories with the exploitation of a suspected web application vulnerability in a package running within a containerized cloud environment. Similarly, a different threat actor leveraged compromised IAM credentials of corporate users, using cloud federation tokens to programmatically generate fresh access keys to circumvent MFA requirements. In a separate incident, a threat actor was first observed accessing the environment with a compromised cloud Service Account key with broad project permissions.

Beyond general cloud identity credentials, threat actors also target LLM API keys. For example, a threat actor opportunistically harvested exposed corporate LLM API keys from public GitHub repositories. Demonstrating advanced evasion tradecraft, the group conducted automated credential validation sweeps using minimal single-token requests (`max_tokens=1`). This allowed the threat actor to stealthily confirm the viability of the stolen keys while remaining undetected by the victim’s endpoint detection and response (EDR) and SIEM volume anomaly alerts.

### Lateral Movement and Persistence

After gaining an initial foothold, threat actors systematically work to escalate privileges, solidify access, and conduct internal reconnaissance to identify targets and further cloud credentials.

To expand their access, threat actors enumerated cloud services, code repositories, and data stores for sensitive credentials. In one intrusion, a threat actor conducted internal reconnaissance across multiple cloud regions to map available services and identity policies. In a separate intrusion, a threat actor compromised a containerized cloud environment. Once inside, they performed extensive repository reconnaissance, cloning sensitive codebases to search for hardcoded secrets, configuration variables, and developer credentials. They also scanned access logs to identify credentials for secondary cloud environments. Threat actors also executed targeted database queries to harvest additional credentials; in one case, the threat actor queried cloud data warehouse metadata tables to search for database credentials, administrator passwords, and sensitive columns, alongside performing cloud object storage operations associated with targeted data theft.

Across intrusions, we observed threat actors abusing cloud identity permissions and virtual machine configurations to escalate privileges and maintain persistent access. Utilizing service accounts associated with compromised workloads, one threat actor exploited token-creation privileges to generate temporary credentials for high-privilege service accounts, resulting in the exfiltration of infrastructure credentials, internal database passwords, and third-party API keys from cloud secret managers. Other threat actors established persistence by creating unauthorized IAM and service accounts and injecting SSH keys into compute instances. Specifically, one actor escalated privileges by attaching administrative policies to service roles, created unauthorized IAM accounts with full administrative rights, and established interactive management sessions into running virtual machines to inject unauthorized SSH public keys into host configuration files. Similarly, another threat actor created deceptive backdoor service accounts disguised as internal billing optimization utilities and injected environment-wide SSH keys into compute instance metadata.

Beyond exploiting traditional cloud infrastructure permissions, we have observed instances of threat actors targeting vulnerabilities specifically within LLM routing software to escalate privileges. In one case, after acquiring pre-validated Virtual Keys from the threat actor that established initial access, a follow-on cluster executed targeted application logic exploitation against the victim's LiteLLM gateway. The actor exploited a user ID rebind vulnerability in the /key/regenerate endpoint (CVE-2026-40217) to elevate standard Virtual Keys into full PROXY\_ADMIN master administrative credentials, establishing deep, persistent control over the compromised environment.

### LLM Abuse

The ultimate objective of LLMJacking is the monetization and resource-hijacking of foundation models, which actors achieve through token proxying, automated model streaming, and GPU hardware provisioning.

Threat actors frequently enabled a variety of managed generative platforms, and created additional API keys to scale their operations. Upon acquiring LLM API access keys, UNC6993 attempted to generate additional API keys and enable associated services within victim cloud projects, quickly accumulating over $100,000 USD in billing charges. Another threat actor subscribed victim accounts to Pay-As-You-Go agreements, selecting premium foundation models and launching high-volume inference streams. To bypass rate limits, the threat actor deployed a "burn and rotate" strategy, continuously creating and deleting short-lived service accounts while auditing the cloud provider’s billing interface to monitor financial impact.

Threat actors also leveraged their access to host their own proxy endpoints and agentic workloads. For example, one threat actor enabled agents, deployed publicly accessible reverse proxies, and used custom Node.js proxy bundles to expose endpoints compatible with multiple frontier LLMs rebranded under a persona known as `D1337-KAIROS`. The actor deployed a containerized backdoor using the [Manus](https://manus.im) agent framework to the compromised cloud environment, which queried an upstream LLM to reason through instructions and execute resulting commands locally, supported by [SearXNG](https://github.com/searxng/searxng) metasearch and [agent-infra/sandbox](https://github.com/agent-infra/sandbox) execution environments. To scale compute, the threat actor provisioned compute instances with powerful GPUs, attempted to spin up high-end hardware across multiple regions, and requested quota increases via the cloud provider’s API. The actor also hosted [LiteLLM](https://github.com/BerriAI/litellm) gateways on external servers to manage and route API traffic.

Rather than consuming hijacked compute solely for their own operations, GTIG observed evidence of threat actors monetizing compromised API quotas by selling access to these resources through LLM Mixers. The threat actors used open-source API gateways and custom relay infrastructure to pool stolen credentials, meter usage, and obscure the origin of the requests. For example, UNC6993 used open-source tools such as [new-api](https://github.com/QuantumNous/new-api) (a centralized model hub and gateway) and [gcli2api](https://github.com/su-kaka/gcli2api) (an API proxy tool converting command line interface (CLI) tools into standard frontier model endpoints), likely to aggregate stolen keys and balance request loads across accounts. We believe the threat actor sells access to these tools via underground storefronts.

Another threat actor that executed more than 500,000 LLM API calls in less than eight hours leveraged stolen third-party API keys to power the token routing service `jet-night.com`. Jet Night passed nearly one million dollars in token costs to the victim organization. Given Jet Night’s per-token costs to users are so far below typical market rates GTIG believes the service relies on stolen keys to operate profitably. For example, Jet Night offers an unlimited token plan for approximately $60 USD per month with alleged access to frontier models, a consumer service level that would typically run between $100 and $250 per month. Moreover, the service has advertised multiple outages on its public Telegram channel which is likely due to stolen keys being revoked as victims discover their respective compromises.

Figure 3: Screenshot of Jet Night Plans and Pricing Structure

A threat actor deployed custom proxy relay infrastructure (`ai-relay`) hosted on deceptive lookalike domains. For example, they registered a domain to masquerade as the victim's legitimate internal host. This custom relay infrastructure was used to seamlessly siphon high-value commercial LLM access into the illicit `newapi[.]pro` resale ecosystem, directly draining the victim's corporate account quotas to serve their underground customers.

### Outlook

GTIG expects that threat actors will increasingly prioritize LLMJacking over traditional resource theft like cryptojacking, driven by the immediate, high-margin monetization enabled by emerging underground LLM Mixers. As enterprises integrate higher-tier models and agentic workflows into production environments, cybercriminals will likely refine automated reconnaissance to target exposed API tokens and exploit vulnerabilities in model routing middleware. This operational specialization will sustain a growing illicit resale marketplace, allowing threat actors to rapidly siphon enterprise quotas while passing the billing costs to victims before compromises are detected.

### Detection and Hunting

In the event that security measures have failed, it is critical that defenders have early visibility into abuse of cloud LLM platforms. Defenders should prioritize detection of modifications to LLM accounts and services and treat any unauthorized enablement as a critical security event. In multiple incidents that Mandiant investigated, LLM services were not enabled at the time of compromise. Abuse of access keys allowed the threat actor to modify and enable LLM API services (e.g. Bedrock, Gemini API, etc.). Once enabled, the threat actor can use the APIs to generate massive bills to the organization in just minutes or hours.

### Google Security Operations

Google Security Operations customers have access to these broad category rules and more under the Cloud Threats, Mandiant Frontline Threats, Mandiant Hunting Rules rule packs. The activity discussed in the blog post is detected in Google SecOps under the rule names:

- AWS Account Key Creation
- AWS Create New Access Key
- AWS Create User Account
- AWS Delete User Account
- Base64 Encoded Shell Command Execution
- Create and Delete Firewall in Default Network
- GCE Project SSH Keys
- GCP Service Account Key Creation
- GCP Create New Service Account
- GCP Firewall Rule Created
- Linux Archive Exfiltration via Curl or Wget
- Persistence: Compute Set Instance or Project Metadata Startup Scripts or URLs

### Mitigation and Remediation

To prevent attackers from abusing Cloud LLM services, defenders should prioritize Identity and Access Management (IAM) and supply chain security, two of the most common pathways for gaining access to and abusing Cloud services.

- **Credential Hygiene**: Utilize a centralized secrets management platform to control the management and rotation of sensitive keys and secrets. Automation of secrets and keys can limit the lifespan of leaked credentials.
- **Least Privilege**: Ensure users and service accounts only possess the permissions necessary for their specific role and required tasks. Deny all permissions that are not explicitly required, including access to Cloud LLM services.
- **Code Monitoring**: Automate secret scanning within codebases (GitHub, Gitlab, etc.) to ensure API keys and secrets added to source code are identified and removed promptly.
- **Routine Configuration Audits**: Perform periodic comprehensive configuration audits of Cloud services to identify potential attack paths and unintended exposure of endpoints.
- **Rate Limiting**: Implement a WAF like Google’s Cloud Armor to enforce rate limiting for individual client connections.
- **Network Allow Listing**: Restrict outbound connections from Cloud services via VPC firewall rules to known IP addresses where feasible.
- **Budget Alerts**: Implement granular API quotas on LLM services to limit request volume per model. Utilize spending caps to set budgets and avoid over-spending.
- **Multi-Factor Authentication (MFA):** Enforce phishing-resistant multi-factor authentication across all cloud identity providers, management consoles, and developer platforms to ensure that stolen credentials or session tokens cannot be easily exploited.
- **Shadow LLM Discovery:** Utilize Security Posture Management tools to automatically scan your hybrid cloud environments and identify unauthorized or unmonitored tools, models, and infrastructure, ensuring complete visibility of your model footprint.
- **Granular API Key Scopes:** Restrict and segment API keys by specific model endpoints, environments (dev/prod), and usage limits to ensure a compromised token for a basic utility model cannot be used to invoke expensive, high-tier frontier models.
- **Validation Sweep Monitoring:** Monitor model gateway and API access logs for anomalous, low-volume requests (such as `max_tokens=1` or zero-temperature pings). Attackers frequently use these micro-transactions for stealthy credential validation sweeps prior to launching large-scale infrastructure abuse.
- **Vulnerability & ML Supply Chain Patching:** Integrate automated vulnerability scanning (SAST/DAST/SCA) across your custom application code, containerized workloads, and machine learning dependencies (like PyTorch and Hugging Face libraries) to prevent initial access via unpatched server vulnerabilities.
- **Gateway Patch Management:** Extend vulnerability management programs to include centralized model proxy and routing  gateways (e.g., LiteLLM), ensuring rapid patching against privilege escalation and authentication bypass flaws (such as CVE-2026-40217).
- **Sandboxed Execution for Dynamic Workloads:** Isolate the runtime environment in highly virtualized, process-isolated, serverless sandboxes if your LLM application is required to execute generated code or database queries dynamically.
- **Vetted Model Repositories:** Restrict and enforce model pulls and pipeline dependencies solely from trusted internal registries or approved enterprise catalogs to prevent developers from pulling compromised models containing pre-configured backdoors.
- **Graph-Based Exposure Modeling:** Implement continuous, graph-based risk prioritization that maps cloud assets, application code, and data flows to automatically identify and remediate complex, multi-hop attack paths.
- **Adversarial Exposure Validation:** Deploy automated offensive agents to continuously test external attack surfaces, uncover exposed endpoints, and simulate credential validation sweeps.

#### Monitoring Native Cloud Audit Logs

- **AWS**: Monitor CloudTrail logs for API events from `bedrock.amazonaws.com`. Based on historical LLM Jacking incidents, monitor for the following API operations across the attack lifecycle:
- **Resource Exploitation**: Monitor for direct execution of the LLM via the `Converse`, `InvokeModel,` and `InvokeModelWithResponseStream` API operations.
- **API Throttling & Error Spikes:** Monitor for high-volume spikes in `ThrottlingException`, `ValidationException`, or `ResourceNotFoundException` errors, which could indicate an automated “spraying” methodology targeting cloud infrastructure.
- **Target Scoping**: Monitor potential reconnaissance activity used to discover available models via the `ListFoundationModels,ListInferenceProfiles`, and `GetFoundationModelAvailability` operations. Additionally, monitor for attempts to unlock new models in the environment via the `PutUseCaseForModelAccess` and `CreateFoundationModelAgreement` API operations.
- **Security/Evasion**: Review attempts to view, alter, or disable logging configurations to conceal prompt contents and avoid detection. Monitor the `GetModelInvocationLoggingConfiguration` operation, as well as `PutModelInvocationLoggingConfiguration` and `DeleteModelInvocationLoggingConfiguration`. Any calls to disable logging by non-IaC (Infrastructure as Code) principals should be treated as high severity.

**Automated Tooling: Analyze User-Agent strings to identify automated tools and SDKs (e.g., claude-cli, aws-sdk-rust, and aws-sdk-go-v2) interacting directly with the target cloud infrastructure.**

- **Azure**: Monitor Azure Activity Logs (Control Plane) and Diagnostic Logs (Data Plane) for events associated with the `Microsoft.CognitiveServices` namespace. To hunt for or detect LLM Jacking incidents, monitor the following operations:
- **Resource Exploitation**: Monitor for direct execution of the LLM. In Azure, model invocations occur on the data plane and require Diagnostic Logs to be enabled. Look for high volumes of POST requests to inference endpoints such as Completions or Chat Completions APIs. On the management plane (Activity Logs), monitor for unauthorized creation of new instances via the `Microsoft.CognitiveServices/accounts/deployments/write` operation.
- **Target Scoping**: Monitor potential reconnaissance activity to discover available Azure LLM resources, models, and deployments via the `Microsoft.CognitiveServices/accounts/read` and `Microsoft.CognitiveServices/accounts/deployments/read` operations.
- **Security/Evasion**: Review attempts to view or modify logging configurations (to see if data plane model invocations are being recorded) via the `Microsoft.Insights/diagnosticSettings/read`, `Microsoft.Insights/diagnosticSettings/write`, or `Microsoft.Insights/diagnosticSettings/delete` operations.
- **GCP**: Monitor Cloud Audit [Logging](https://cloud.google.com/logging/docs/audit) for calls to Gemini Enterprise Agent Platform endpoints (aiplatform.googleapis.com). Gemini Enterprise Agent Platform inference operations are contained within Data Access logs, which are disabled by default due to volume and ingestion costs. You must manually configure your IAM audit policies to track these.
- **Enablement of Agent Platform Services**: [Alert](https://docs.cloud.google.com/service-usage/docs/audit-logging) on enablement of Gemini Enterprise Agent Platform services via the `google.api.serviceusage.v1.ServiceUsage.EnableService` method.
- **Resource Exploitation**: Monitor for direct execution of the LLM via Gemini Enterprise Agent Platform, which requires Data Access audit logging to be enabled. Look for `google.cloud.aiplatform.v1.PredictionService.Predict`, `google.cloud.aiplatform.v1.PredictionService.GenerateContent`, and `google.cloud.aiplatform.v1.PredictionService.StreamGenerateContent` operations.
- **Target Scoping**: Monitor potential reconnaissance activity to discover available models and endpoints via the `google.cloud.aiplatform.v1.ModelService.ListModels`, `google.cloud.aiplatform.v1.EndpointService.ListEndpoints`, and `google.cloud.aiplatform.v1.PublisherModelService.ListPublisherModels` API operations.
- **Security/Evasion**: Review attempts to view or alter logging and audit configurations. Monitor for operations like `google.iam.v1.IAMPolicy.GetIamPolicy` (to check if Data Access logs are enabled on the project/resource) or attempts to review log exports via `google.logging.v2.ConfigServiceV2.ListSinks` and `google.logging.v2.ConfigServiceV2.GetSink`.

### Indicators of Compromise (IOCs)

To assist the wider community in hunting and identifying activity outlined in this blog post, we have included indicators of compromise (IOCs) in a [GTI Collection](https://www.virustotal.com/gui/collection/4377d2403ea17a04744ca871113c1313b0162f190f0b785f5a10b744e8528245/iocs) for registered users.

#### Network Indicators

Table 1: Network Indicators
