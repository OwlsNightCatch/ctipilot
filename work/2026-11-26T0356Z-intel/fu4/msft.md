---
title: What defenders need to know about ARTEX, the agentic AI framework threat actors abuse
author: Microsoft Threat Intelligence
url: https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/
hostname: microsoft.com
description: The AI-powered penetration testing framework ARTEX has been abused by threat actors like Storm-0940, Storm-3358, Onyx Sleet, Pearl Sleet, Crystal Typhoon, and Salt Typhoon to accelerate their existing workflows related to network reconnaissance, credential attacks, and web application exploitation.
sitename: Microsoft Security Blog
date: "2026-11-25"
fingerprint: b5f13a83e3ced211
language: en
image: https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/11/ARTEX-featured.png
pagetype: article
filedate: "2026-11-26"
---
Since its release in July 2026, the AI-powered penetration testing framework ARTEX has been abused by many threat actors to accelerate their existing workflows related to network reconnaissance, credential attacks, and web application exploitation. As of November 2026, Microsoft Threat Intelligence has observed both state-sponsored and financially motivated threat actors such as [Storm-0940](https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/), [Storm-3358](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/), [Onyx Sleet](https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/), [Pearl Sleet](https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/), Crystal Typhoon, and Salt Typhoon integrating ARTEX into their tooling.

In the past few weeks, we’ve reported several distinct campaigns that abused ARTEX to search public repositories for exposed secrets, enable supply chain compromise, and scan internet-facing systems for exploitation. These campaigns illustrate how threat actors use ARTEX to automate various stages of the attack chain. Threat actors define scope and targets for ARTEX, which then uses AI agents to set verifiable goals, define tactical steps for each stage of the operation, use tools to attack targets, create graphs to track discovered systems and results of actions, and report back to the threat actor. Depending on the threat actor’s configuration and the target’s defenses, ARTEX can advance from reconnaissance to persistent, privileged access to a target organization in a matter of minutes.

ARTEX does not introduce new attack techniques; it uses common, pre-existing penetration testing tools and techniques. ARTEX does sometimes transmit distinctive characteristics associated with its integrated penetration testing tools. However, threat actors using ARTEX can and do vary network indicators like source IP address or user agent string, especially to bypass static or simple signature-based detection and blocking. The most reliable and durable signal of ARTEX activity is behavioral: ARTEX sends a wide variety of requests in a brief time and retries variations on the same technique or moves on to next-stage actions at machine speed.

In this blog, we’re sharing a detailed breakdown of ARTEX, including its architecture and capabilities, as well as guidance for identifying related network and system activity. Microsoft disrupts and contains threats posed by ARTEX-enabled attacks across the Microsoft Defender suite of products. Defenders can further reduce and mitigate the effectiveness of ARTEX and similar AI agentic attacks by following Microsoft’s recommendations outlined in this report to reduce internet-facing exposure, secure credentials and secrets, and limit lateral movement paths in their environment. Additionally, Microsoft recommends customers to enable automatic attack disruption in Microsoft Defender XDR to contain and isolate affected devices during an attack.

To help defenders keep pace with machine-speed attacks, [Microsoft Perception](https://www.microsoft.com/security/business/microsoft-perception-agentic-system) coordinates red, blue, and green team agents that find exploitable weaknesses, investigate threats, and remediate risks, with security teams approving critical actions. As threat actors increasingly adopt AI, we’re publishing this information to equip defenders with insights that can help protect systems, secrets, identities, and networks from AI-assisted attacks.

## ARTEX: Publicly available AI-powered offensive security framework

ARTEX (“AI 自主渗透测试系统,” or AI autonomous penetration testing system) is an AI-driven penetration testing platform. A Go-based backend coordinates multiple large language model (LLM) agents that can take an attack from reconnaissance and attack surface discovery through exploitation, verification, and reporting, with little or no human involvement. ARTEX includes an embedded Next.js web interface and uses PostgreSQL for storage.

ARTEX is primarily a web application penetration testing tool. Its built-in guidance, skills, and findings categories center on vulnerabilities in HTTP applications and APIs, including SQL injection, server-side template injection, XML external entity (XXE) injection, file upload flaws, authentication bypass, and insecure direct object references (IDOR).

ARTEX agents also perform general network reconnaissance and credential attacks. After agents gain initial access to a system or network, they can pivot through interactive shells. By default, ARTEX does not take any measures to obfuscate its malicious activity.

In July 2026, GitHub user Autumn-27 published ARTEX as open-source code with a Chinese-language interface. While the original developer removed the source code in October 2026, other developers who had forked the project continue to publish their own versions of ARTEX in many other languages. In November 2026, the China-based cybersecurity company ThreatBook (微步在线) claimed ownership of ARTEX and began offering commercial access to “ARTEX Pro”, in addition to CyberStrikeAI Enterprise Edition and other AI-powered penetration testing frameworks.

## AI agent architecture

ARTEX uses multiple AI agents for different functions. The threat actor defines the target scope, and a goals model breaks the engagement into objectives that can be verified. A planner agent continuously reviews a knowledge graph containing discovered assets and findings, then issues short attack directions called “intents.” Worker agents claim those intents and carry them out with a real shell and offensive tools. They write new assets, facts, and confirmed vulnerabilities back to the graph. Each update wakes the planner agent, which decides what to do next. The cycle continues until the goals are met or the task reaches its time or step limit. A reporter agent then documents each confirmed finding with reproduction steps and a proof of concept.

The threat actor can configure ARTEX to power its agents with virtually any large language model, including frontier models, open-weight models, or models that the threat actor has abliterated (modified to remove built-in guardrails) or otherwise manually tuned. For that reason, ARTEX activity is not necessarily constrained by any single provider’s safety controls or visible in any single provider’s telemetry.

An optional pool function allows ARTEX to switch to different models when one fails for any reason (for example, quota exhausted, invalid key, rate-limited, or erroring). The function includes a configurable priority order and cooldown, so a long campaign can continue across multiple providers or keys.

## Capabilities

ARTEX agents call tools to act on intents. While threat actors and agents can add arbitrary tools, ARTEX includes a set of pre-configured tools that define its core capabilities: network reconnaissance, web application mapping, web shell upload, and web browser-based attacks.

- nmap — A network discovery and port-scanning tool that identifies systems, exposed services, and often their versions, rather than simply testing one connection
- nc (netcat) — A general-purpose network utility for opening TCP or UDP connections, listening on ports, and moving raw data between systems
- telnet — A basic interactive TCP client useful for manually probing text-based services
- whois — A registration-data lookup tool that retrieves information about domain names or IP address allocations
- dig — A DNS diagnostic tool
- curl — A command-line HTTP and protocol client suited to crafting requests and inspecting responses, including headers, authentication, and APIs
- wget — A web download utility
- Playwright + Chromium — A browser-automation stack that drives a real Chromium browser, with all elements of the HTTP exchange exposed for manipulation
- node — A JavaScript runtime
- python3 — A general-purpose scripting runtime
- git — A tool for retrieving and inspecting code repositories and their history
- ripgrep — A fast recursive text-search tool for finding strings or patterns
- jq — A command-line JSON processor that filters and transforms structured output from APIs and other tools

Threat actors also commonly add exploitation frameworks and credential attack tools to extend the capabilities of ARTEX agents:

- sqlmap — A specialized web-application testing tool that detects and assesses SQL injection in application inputs
- hydra — A parallelized credential-testing tool supporting many network login protocols and configurable username/password combinations
- medusa — A modular, parallel network-login tester distinguished by its service-specific authentication modules
- ncrack — A network authentication testing tool from the Nmap ecosystem, focused on high-speed testing of supported remote services
- nuclei — A template-driven vulnerability scanner that checks targets for defined exposures, misconfigurations, and known issues across multiple protocols
- nikto — A web-server scanner focused on potentially dangerous files, outdated components, and common server misconfigurations
- gobuster — A wordlist-based discovery tool that enumerates web paths, DNS subdomains, or virtual hosts with a relatively focused command-line workflow
- ffuf — A flexible web fuzzer that substitutes candidate values into chosen parts of a request, such as paths, parameters, headers, or hostnames
- Msfconsole (Metasploit) — An exploitation framework and its interactive console, combining exploit modules, payloads, and post-exploitation workflows in one environment.
- john (John the Ripper) — An offline password-auditing tool notable for broad hash-format support and adaptable cracking modes
- hashcat — An offline password-recovery tool distinguished by GPU-accelerated candidate generation and hash testing

ARTEX agents can perform a wide range of actions, depending on the available tools and goals that the threat actor sets. Microsoft Threat Intelligence has observed ARTEX agents exhibiting the following capabilities as of November 2026:

- Network reconnaissance
  - Port and service scanning
  - DNS enumeration
  - HTTP probing and content scraping
  - Importing assets from separate asset-scanning platforms
- Web application reconnaissance
  - Retrieval of JavaScript bundles, source maps, runtime configuration files, and API documentation to extract routes
  - Headless-browser crawling, including with a simulated signed-in state
  - Enumeration of REST, WebSocket, and server-sent events (SSE) endpoints
- Web application exploitation
  - Exploitation of known vulnerabilities in exposed software
  - Authentication bypass (for example, unsigned tokens and manipulated OAuth callbacks)
  - SQL injection
  - Server-side template injection
  - XML external entity (XXE) injection
  - File upload flaws
  - Insecure direct object references (IDOR)
- Credential attacks
  - Weak-password testing
  - Password spraying
  - Brute force guessing
  - Abuse of account-recovery flows
- Persistence
  - Web shell upload
- Credential access
  - Reading secrets from configuration files, *.env* files, private keys, and */etc/shadow*
  - Dumping databases
  - Kerberoasting
- Lateral movement
  - Credential reuse
- Cloud identity abuse
  - Authentication with stolen or captured credentials
  - Cloud permission mapping
  - Microsoft Graph reconnaissance
  - Adding application credentials for persistence
  - Assigning privileged roles for privilege escalation
  - Reading cloud keys and tokens, including from cloud secret management stores

## Identifying ARTEX network activity

While ARTEX does not invent new attack techniques, it can combine the adaptable attack chain of a human threat actor with the speed and precision of malicious software. Therefore, the challenge of identifying network activity from AI-driven tools like ARTEX is differentiating it from both human- and software-driven activity.

Defenders can detect three types of evidence that may suggest AI-driven activity:

- The most durable signal of AI-driven activity is the pattern formed by the bursts of machine speed activity. ARTEX agents, sometimes working in parallel, continually adapt and retry a given tactic until they succeed or run out of time. ARTEX agents quickly and exhaustively iterate through different methods of access, exploitation, or abuse. A human threat actor takes time to move from one stage of the attack chain to the next. In contrast, after successfully compromising a system or credentials, the framework then dispatches additional agents to move on to the next stage of the activity at machine speed. While ARTEX is a popular tool, other AI-driven offensive security frameworks also generate similar patterns of behavior.
- Automated penetration testing tools, including the ones that ARTEX agents call, can produce a characteristically large volume of anomalous traffic from a single source in a short time. ARTEX does not obfuscate its malicious activity; a large number of these traffic bursts occurring at intervals is consistent with automated targeting.
- A small amount of traffic might have user agent strings, network protocol options, or other default values strongly associated with ARTEX or the tools it calls. However, threat actors and ARTEX agents frequently change these values, particularly when evading static rules that block such values. The following table shows two such user agent strings specific to ARTEX:

| **Type** | **Value** | **Notes** | 
|---|---|---|
| User agent string | *artex-enrich/\** | Included with a short GET request to each newly discovered web asset that does not follow redirects, closes the connection, and reads only enough of the response to extract the page title. | 
| User agent string | *norma/\** | Included with requests made directly by agents through their built-in web-fetch tool rather than through shell tools. | 

[Defensive honeypots](https://learn.microsoft.com/security/zero-trust/adopt/prevent-reduce-business-damage-breach-infrastructure#create-honeypot-resources), decoys, tarpits, and fake wins can pull autonomous AI attacks away from legitimate targets. Honeypots and decoy surfaces such as [Microsoft Sentinel Deception](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/HoneyTokens) give the agent attractive but worthless targets to pursue. Tarpits consume the agent’s time and budget. Fake wins present convincing evidence that the agent’s objective is complete, which can cause it to stop on a false success. Honeytokens can provide early warnings of AI compute hijacking. In Microsoft’s testing, these controls helped reduce the attack traffic reaching real assets and produced high-confidence, attribution-quality signal.

## Identifying ARTEX system activity

After gaining initial access to a system, ARTEX agents often use well-known risky utilities (for example, certutil, curl, wget, netcat) on the system to launch web shells, install remote access trojans (RATs), or take other action to achieve persistence. Because ARTEX does not take any measures to obfuscate its malicious activity, existing methods for detecting compromise will likely capture ARTEX activity:

- Web server processes (such as *w3wp.exe*, *php-fpm*, *httpd* or *apache2*, or Java application servers) starting *sh*, *bash*, *cmd.exe*, or PowerShell
- New or modified script files (*.php*, *.jsp*, *.jspx*, *.asp*, *.aspx*, or *.ashx*) in web-accessible or upload directories; this includes files written by a database server process after its logging settings were changed to point a log file at a web directory
- Several short-lived web shells with incrementing names, each running a different command, as ARTEX agents correct errors until a web shell runs cleanly
- Rapid reads of */etc/shadow*, *.env* and configuration files, private keys, and cloud credential files, and bursts of database extraction
- Reverse shells and outbound requests from the server to webhook or file-sharing services used to deliver scripts and return command output
- Two or three attack chains active at once, and renewed attempts through new paths after containment

## Mitigation and protection guidance

Microsoft recommends the following mitigations to reduce the impact of this threat. Check the recommendations card for the deployment status of monitored mitigations.

ARTEX doesn’t introduce new attack techniques. It runs common penetration testing tools and tries one approach after another at machine speed. The mitigations that matter most close exposure before scanning finds it, slow down bursts of requests, protect credentials and application secrets, and contain a compromise automatically.

### Reduce internet-facing exposure

- Find and fix exposed assets first by using [Microsoft Defender External Attack Surface Management discovery](https://learn.microsoft.com/azure/external-attack-surface-management/what-is-discovery) to inventory the internet-facing hosts, websites, and services you own, including ones you didn’t know about. Then prioritize fixes with [Microsoft Defender Vulnerability Management](https://learn.microsoft.com/defender-vulnerability-management/defender-vulnerability-management), which shows internet-exposed resources that lead to sensitive data or privileged identities. ARTEX agents start with port scans and web path enumeration and act on whatever they find.
- Block and slow down attacks on web applications and APIs. After tuning in detection mode, switch [Web Application Firewall on Application Gateway](https://learn.microsoft.com/azure/web-application-firewall/ag/ag-overview) to prevention mode so that SQL injection and other common web attacks are blocked, not only logged. Add [rate limiting on Application Gateway](https://learn.microsoft.com/azure/web-application-firewall/ag/rate-limiting-overview) or [rate limiting on Azure Front Door](https://learn.microsoft.com/azure/web-application-firewall/afds/waf-front-door-rate-limit) to cap how many requests one client can send in a short time, and turn on [bot protection](https://learn.microsoft.com/azure/web-application-firewall/ag/bot-protection-overview) to block or log requests from known malicious IP addresses. For APIs in Azure API Management, follow [Mitigate OWASP API security top 10 threats](https://learn.microsoft.com/azure/api-management/mitigate-owasp-api-threats) to enforce authentication, object-level authorization, and rate limits. ARTEX agents send hundreds of requests to learn which paths a server allows and harvest API documentation to find internal routes, then test them for injection, authentication bypass, and access-control flaws.

### Map and test attack paths

- Map what an exposed asset or stolen credential could reach before an agent does. Use [attack paths in Microsoft Security Exposure Management](https://learn.microsoft.com/security-exposure-management/work-attack-paths-overview) and [attack path analysis in Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/concept-attack-path) to find defensive choke points, where paths to critical assets converge, and explore the blast radius of each one. [Classify your critical assets](https://learn.microsoft.com/security-exposure-management/critical-asset-management) so the paths are complete, and [query the enterprise exposure graph](https://learn.microsoft.com/security-exposure-management/query-enterprise-exposure-graph) in advanced hunting to explore the same connections. During an incident, [blast radius analysis in the incident graph](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-graph-overview) shows the paths an attacker could take from a compromised entity to a critical asset. ARTEX agents [record the assets and vulnerabilities they discover in a graph](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/), so mapping your own graph first shows where they would go next.
- Test the paths that matter most, within Microsoft’s rules. Microsoft recommends [regular red team operations](https://learn.microsoft.com/security/benchmark/azure/mcsb-posture-vulnerability-management) to complement vulnerability scanning. Agree on the scope and constraints with resource owners and fix all critical findings. Testing of Azure resources must follow the [penetration testing rules of engagement,](https://learn.microsoft.com/azure/security/fundamentals/pen-testing) which encourage testing your security monitoring and detection, prohibit automated testing that generates excessive traffic, and prohibit using secrets that aren’t your own, [including publicly leaked ones](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement). Agentic tools like ARTEX [scan public code repositories for secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/), so decide before testing how testers will handle credentials that belong to someone else.
- Organizations can incorporate [Microsoft Perception’s](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-overview) [Recon Agent](https://learn.microsoft.com/en-us/security/agentic-security/recon-agent) to map relationships between Azure resources, Microsoft Entra ID identities, and permissions to identify potential lateral movement paths, privilege escalation opportunities, and high-value assets accessible following an initial compromise. Recon Agent’s [Identify attack paths](https://learn.microsoft.com/en-us/security/agentic-security/recon-agent#investigate-attack-paths-in-a-subscription) playbook searches for potential attack paths within an Azure subscription, while the [Assess identity risks](https://learn.microsoft.com/en-us/security/agentic-security/recon-agent#investigate-managed-identity-access-to-critical-assets) playbook investigates whether a managed identity could provide a path to critical assets. The [Protect against a threat](https://learn.microsoft.com/en-us/security/agentic-security/recon-agent#respond-to-a-new-cve-or-threat) playbook correlates identified exposures with relevant threat intelligence. Because Perception’s Recon Agent performs read-only analysis rather than active exploitation, organizations should complement its findings with authorized penetration testing to validate viable attack paths.

### Protect web servers

- Run endpoint protection on every internet-facing server and keep it blocking. Use [Defender for Endpoint on Linux](https://learn.microsoft.com/defender-endpoint/microsoft-defender-endpoint-linux) and the [Defender for Servers plan](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-servers-overview) so that the endpoint detections and hunting queries in this report cover the servers that ARTEX agents exploit, including Linux servers. Turn on [tamper protection](https://learn.microsoft.com/defender-endpoint/tamper-protection-overview), use [EDR in block mode](https://learn.microsoft.com/defender-endpoint/edr-in-block-mode) on Windows devices that run a non-Microsoft antivirus product, and turn on the [Block Webshell creation for Servers](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction-rules-reference) attack surface reduction rule on Exchange servers.
- Restrict outbound connections from web servers. Allow only the destinations each server needs, for example with [Azure Firewall threat intelligence-based filtering](https://learn.microsoft.com/azure/firewall/threat-intel), and create [indicators for IPs, URLs, and domains](https://learn.microsoft.com/defender-endpoint/indicator-ip-domain) in Defender for Endpoint to block known-bad destinations. ARTEX agents have used curl and netcat to download remote access trojans, and curl with rotating webhook.site URLs to deliver scripts and return command output.

### Secure accounts and sign-ins

- Apply Conditional Access to every user and workload identity. Create policies that require [multifactor authentication (MFA) for all users](https://learn.microsoft.com/entra/identity/conditional-access/policy-all-users-mfa-strength), enforce [phishing-resistant MFA for administrators](https://learn.microsoft.com/entra/identity/conditional-access/policy-admin-phish-resistant-mfa), and [block legacy authentication](https://learn.microsoft.com/entra/identity/conditional-access/policy-block-legacy-authentication). Consider wider adoption of [phishing-resistant passwordless authentication deployment](https://learn.microsoft.com/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication) to all users. Configure [risk policies in Microsoft Entra ID Protection](https://learn.microsoft.com/entra/id-protection/howto-identity-protection-configure-risk-policies) to require MFA or block access for medium-risk and high-risk sign-ins; sign-ins from known threat actor infrastructure, including infrastructure behind ARTEX activity, raise *Verified threat actor IP* detections at high risk.
- For service principals, use [Conditional Access for workload identities](https://learn.microsoft.com/entra/identity/conditional-access/workload-identity) to block sign-ins from unexpected locations or with elevated risk; [workload identity risk detections](https://learn.microsoft.com/entra/id-protection/concept-workload-identity-risk) flag leaked credentials and suspicious sign-ins, including credentials found in public code on GitHub.
- Ban weak passwords and slow down guessing. Turn on [Microsoft Entra Password Protection](https://learn.microsoft.com/entra/identity/authentication/concept-password-ban-bad) with a custom banned password list, extend it to [on-premises Active Directory](https://learn.microsoft.com/entra/identity/authentication/concept-password-ban-bad-on-premises), and review [smart lockout](https://learn.microsoft.com/entra/identity/authentication/howto-password-smart-lockout) settings. In one Storm-0940 campaign that used ARTEX, Microsoft recorded more than 151,000 failed sign-ins, peaking at 2,900 failures per minute.

### Protect application secrets and privileges

- Keep application secrets out of code and replace any that leak. Use [application management policies](https://learn.microsoft.com/entra/identity/enterprise-apps/tutorial-enforce-secret-standards) to limit which kinds of secrets and certificates apps can use and to enforce rotation, and move workloads to [managed identities](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) where possible. Turn on [secret scanning and push protection](https://learn.microsoft.com/azure/devops/repos/security/github-advanced-security-secret-scanning?view=azure-devops) for Azure DevOps repositories and [secrets scanning in Defender for Cloud](https://learn.microsoft.com/azure/defender-for-cloud/secrets-scanning) for virtual machines and cloud deployments and invalidate and replace any secret found in code or configuration files, including .env files. [In one case](https://www.microsoft.com/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/) that Microsoft observed, an AI agent went from searching GitHub for client secrets to taking data from Azure Key Vault in five minutes.
- Govern app registration, consent, and privileged roles by [restricting app registration](https://learn.microsoft.com/entra/identity/role-based-access-control/delegate-app-roles) to the users who need it, [configuring user consent](https://learn.microsoft.com/entra/identity/enterprise-apps/configure-user-consent) so that users can’t grant broad permissions to unverified apps, and using [app governance in Microsoft Defender for Cloud Apps](https://learn.microsoft.com/defender-cloud-apps/app-governance-manage-app-governance) to see which apps can reach your data. Use [Privileged Identity Management](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-configure) for time-bound role activation, and monitor application credential changes and role assignments as described in the [Microsoft Entra security operations guide for applications](https://learn.microsoft.com/entra/architecture/security-operations-applications). During Storm-0940 activity, ARTEX agents added credentials to applications, and an application assigned itself the Global Administrator role.

### Protect cloud resources and data

- Limit what a stolen credential or token can reach. Follow [best practices for Azure RBAC](https://learn.microsoft.com/azure/role-based-access-control/best-practices) to limit each service principal to the resources and operations its application needs, and grant [managed identities only the access they need](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/managed-identity-best-practice-recommendations) so that a token taken from the [Azure Instance Metadata Service](https://learn.microsoft.com/azure/virtual-machines/instance-metadata-service) through an XXE or SSRF flaw can’t reach other resources. ARTEX agents map the permissions of the credentials they capture and have used an XXE flaw to query a cloud metadata service for role credentials, and in one investigation AI agents used a compromised OAuth application to run scripts on Azure virtual machines.
- Harden and monitor the services that hold secrets and data. Follow [Secure your Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/secure-key-vault); for storage accounts, [prevent Shared Key authorization](https://learn.microsoft.com/azure/storage/common/shared-key-authorization-prevent) and [remediate anonymous read access to blob data](https://learn.microsoft.com/azure/storage/blobs/anonymous-read-access-prevent); [disable basic authentication](https://learn.microsoft.com/azure/app-service/configure-basic-auth-disable) for App Service publishing; and [disable local authentication](https://learn.microsoft.com/azure/ai-services/disable-local-auth) so that Foundry Tools accept only Microsoft Entra ID authentication. Then turn on [Defender for Key Vault](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-key-vault-introduction), [Defender for Storage](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-storage-introduction), [Defender for Resource Manager](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-resource-manager-introduction), [Defender for App Service](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-app-service-introduction), [Defender for open-source relational databases](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-databases-introduction), and [AI threat protection](https://learn.microsoft.com/azure/defender-for-cloud/ai-threat-protection) for the workloads you run. ARTEX agents have run commands through cloud administration interfaces such as Kudu when they had credentials for them, and AI agents have focused on credentials for AI services.

### Limit lateral movement and contain attacks automatically

- Detect credential theft on domain controllers. [Install Microsoft Defender for Identity sensors](https://learn.microsoft.com/defender-for-identity/deploy/deploy-defender-identity) on all domain controllers. Its alerts, listed in the Detections section, cover the Active Directory credential theft and reconnaissance that ARTEX agents run in compromised domains.
- Remove reusable passwords and standing access. Use [group managed service accounts](https://learn.microsoft.com/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview), whose passwords Windows manages automatically, so that service accounts don’t rely on passwords that people choose and rarely change. Use [Windows LAPS](https://learn.microsoft.com/windows-server/identity/laps/laps-overview) to rotate each device’s local administrator password so that one captured password doesn’t work across many devices and use [just-in-time machine access](https://learn.microsoft.com/azure/defender-for-cloud/just-in-time-access-overview) in Defender for Cloud to keep management ports such as RDP and SSH closed until they’re needed. ARTEX agents reuse captured credentials to move laterally over SSH and WinRM.
- Enable [automatic attack disruption](https://learn.microsoft.com/defender-xdr/automatic-attack-disruption) to contain compromised assets that an attacker is using and limit lateral movement early, as well as [automated investigation and response](https://learn.microsoft.com/defender-xdr/m365d-configure-auto-investigation-response), which investigates and remediates alerts automatically. In multiple ARTEX-driven Storm-0940 intrusions, privileged access came less than three hours after initial targeting.

## Microsoft Defender detections

[Microsoft Defender](https://www.microsoft.com/security/business/microsoft-defender) customers can refer to the list of applicable detections below. Microsoft Defender coordinates detection, prevention, investigation, and response across endpoints, identities, email, apps to provide integrated protection against attacks like the threat discussed in this blog.

### Microsoft Defender Antivirus

Microsoft Defender Antivirus detects threat components as the following:

- Behavior:Win64/ArtexAI

### Microsoft Defender for Endpoint

The following alerts might indicate threat activity associated with this threat. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

**Execution**

- Process launched in the background
- Suspicious file dropped and launched
- Suspicious file or content ingress
- Hidden file executed
- Suspicious process executed by network service
- Suspicious piped command launched
- Suspicious process launched by service
- Suspicious process launched from a world-writable directory
- Suspicious script launched
- Suspicious shell execution from PHP application
- Suspicious shell command execution

**Persistence**

- Possible Web Server compromise activity
- Suspicious cron job creation

**Defense evasion**

- Executable permission added to file or directory
- Obfuscation or deobfuscation activity
- Possible time based evasion
- Suspicious decoding of encoded content into script
- Suspicious file and directory permission modification
- Suspicious file or information obfuscation detected
- Suspicious path deletion

**Credential access**

- Suspicious access of sensitive files

**Discovery**

- Suspicious port scan activity

**Collection**

- Enumeration of files with sensitive data
- Suspicious file copy operations
- Suspicious process collected data from local system

**Lateral movement**

- Remote Desktop session

**Command and control**

- Possible reverse shell
- Suspicious connection to remote service
- Suspicious curl behavior

### Microsoft Defender for Identity

The following alerts might indicate threat activity associated with this threat. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Possible Kerberoasting attack
- Possible Kerberoasting attack following a suspicious LDAP query
- Possible Kerberoasting attack using a stealthy LDAP search
- Possible Kerberoasting LDAP reconnaissance
- Possible SPN enumeration via LDAP
- DCSync attack (replication of directory services)
- Suspected brute-force attack (Kerberos, NTLM)
- Suspected brute-force attack on Lightweight Directory Access Protocol (LDAP) authentication
- Suspected password spray attack (Kerberos, NTLM)
- Suspected password spray attack on Lightweight Directory Access Protocol (LDAP) authentication
- Suspected account enumeration (Kerberos, NTLM, AD FS)
- Suspicious LDAP query targeting sensitive attributes
- Discovery tool was observed
- Malicious sign in from a randomized user agent
- Possible service principal account secret leak
- Possibly compromised service principal account signed in
- Suspicious service principal sign-in following credential addition
- Suspicious Entra Graph API query observed

Organizations that use classic Defender for Identity alerts see Suspected Kerberos SPN exposure, Suspected DCSync attack (replication of directory services), Account Enumeration reconnaissance (LDAP), and Security principal reconnaissance (LDAP) instead. See [Defender for Identity XDR security alerts](https://learn.microsoft.com/defender-for-identity/alerts-xdr) and [Defender for Identity classic security alerts](https://learn.microsoft.com/defender-for-identity/alerts-mdi-classic).

### Microsoft Entra ID Protection

The following [risk detections](https://learn.microsoft.com/entra/id-protection/concept-identity-protection-risks) might indicate that an account was targeted or compromised by ARTEX-driven activity. These detections, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Verified threat actor IP
- Password spray
- Microsoft Entra threat intelligence
- Malicious IP address
- Anonymous IP address
- Atypical travel
- Unfamiliar sign-in properties
- Leaked credentials

The following [workload identity risk detections](https://learn.microsoft.com/entra/id-protection/concept-workload-identity-risk) can indicate that an application identity is compromised:

- Leaked Credentials
- Suspicious Sign-ins
- Anomalous service principal activity
- Microsoft Entra threat intelligence
- Suspicious application
- Malicious application

### Microsoft Defender XDR

The following alerts might indicate threat activity associated with this threat. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Multiple Service Principal Sign-ins from Single IP
- Potentially compromised OAuth application identified through attack activity analysis
- Graph API activity from a Microsoft threat intelligence IP address
- Application self-assigned Global Administrator role
- Account compromised following a password-spray attack
- Anomalous OAuth device code authentication activity
- Suspicious sign-in from verified nation-state threat actor infrastructure
- Malicious sign-in from known threat actor IP address

### Microsoft Defender for Cloud Apps

The following alerts might indicate threat activity associated with this threat. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Suspicious addition of app role assignments to service principal
- Suspicious addition of application role assignments by service principal to itself
- High-privilege application roles assigned to a service principal
- Suspicious OAuth app registration
- Suspicious mail access activity by OAuth application following role assignment
- Suspicious OAuth application created from a risky user context performing graph SharePoint enumeration
- OAuth application activity from an uncommonly visited ISP
- Activities from suspicious user agents
- Activity from a password-spray associated IP address
- Successful logon from a suspicious IP address
- Multiple failed user log on attempts to an app

The following [app governance threat detection alerts](https://learn.microsoft.com/defender-cloud-apps/app-governance-anomaly-detection-alerts) might also indicate that an application’s credentials are being abused:

- Application initiating multiple failed KeyVault read activity with no success
- OAuth App using unusual user agent
- Suspicious enumeration activities performed using Microsoft Graph PowerShell
- Dormant OAuth App predominantly using MS Graph or Exchange Web Services recently seen to be accessing ARM workloads
- App accessed from unusual location made anomalous Graph calls post certificate update
- Anomalous SharePoint activity by app that just updated or added new credentials
- Anomalous OneDrive activity by app that just updated or added new credentials
- Unused app newly accessing APIs

**Microsoft Defender for Cloud Apps behaviors**

Note that some [Microsoft Defender for Cloud Apps alerts are transitioning to behaviors](https://learn.microsoft.com/defender-cloud-apps/behaviors), and policies that generate behaviors are now disabled by default, and don’t send alerts.

[Access behaviors in the Defender portal Advanced hunting page](https://learn.microsoft.com/defender-xdr/advanced-hunting-overview) and use behaviors by querying behavior tables and creating custom detection rules that include behavior data.

The following behavior might also indicate threat activity associated with this threat. This behavior, however, can be triggered by unrelated threat activity and is not monitored in the status cards provided with this report:

- Multiple failed login attempts

In advanced hunting, this behavior has the ActionType *MultipleFailedLoginAttempts* in the *BehaviorInfo* and *BehaviorEntities* tables.

### Microsoft Defender for Cloud

Microsoft Defender for Key Vault alerts with the following titles might indicate that stolen credentials are being used to read secrets. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Suspicious secret listing and query in a key vault
- High volume of operations in a key vault
- Unusual operation pattern in a key vault
- Unusual application accessed a key vault
- Unusual user-application pair accessed a key vault
- User accessed high volume of key vaults
- Unusual access denied – User accessing high volume of key vaults denied
- Access from a suspicious IP address to a key vault
- Access from a TOR exit node to a key vault
- Unusual access to the key vault from a suspicious IP (Non-Microsoft or external)

Microsoft Defender for Storage alerts with the following titles might indicate discovery of, or data taken from, Azure Storage. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Publicly accessible storage containers successfully discovered
- Access from an unusual location to a sensitive blob container
- Unusual amount of data extracted from a storage account
- Access from a suspicious application

Microsoft Defender for Resource Manager alerts with the following titles might indicate Azure management operations from threat actor infrastructure. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Azure Resource Manager operation from suspicious IP address
- Azure Resource Manager operation from suspicious proxy IP address
- Suspicious Azure role assignment detected (Preview)

Microsoft Defender for Databases alerts with the following titles might indicate SQL injection or brute force attempts against databases. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Potential SQL injection
- A possible vulnerability to SQL Injection
- Suspected brute force attack
- Suspected successful brute force attack
- Login from a suspicious IP

AI threat protection alerts with the following titles might indicate that stolen keys or credentials are being used against AI services. These alerts, however, can be triggered by unrelated threat activity and are not monitored in the status cards provided with this report:

- Suspicious user agent detected
- Access from suspicious IP
- Access from a Tor IP
- Access anomaly in AI resource
- Suspicious invocation of a high-risk ‘Initial Access’ operation by a service principal detected (AI resources)
- Suspected wallet attack – volume anomaly

### Microsoft Sentinel

The following analytics rules from Microsoft Sentinel solutions might also indicate ARTEX-driven activity. These rules, however, can be triggered by unrelated threat activity:

- Password spray attack against Microsoft Entra ID application (Microsoft Entra ID solution)
- Malformed user agent
- Abnormal Deny Rate for Source IP (Azure Firewall solution)
- Abnormal Port to Protocol (Azure Firewall solution)

### Microsoft Security Copilot

[Microsoft Security Copilot](https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot) is [embedded in Microsoft Defender](https://learn.microsoft.com/defender-xdr/security-copilot-in-microsoft-365-defender) and provides security teams with AI-powered capabilities to summarize incidents, analyze files and scripts, summarize identities, use guided responses, and generate device summaries, hunting queries, and incident reports.

Security Copilot is also available as a [standalone experience](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot) where customers can perform specific security-related tasks, such as incident investigation, user analysis, and vulnerability impact assessment. In addition, Security Copilot offers [developer scenarios](https://learn.microsoft.com/copilot/security/developer/custom-agent-overview) that allow customers to build, test, publish, and integrate AI agents and plugins to meet unique security needs.

### Threat intelligence reports

Microsoft Defender XDR customers can use the following [threat analytics](https://learn.microsoft.com/defender-xdr/threat-analytics) reports in the Defender portal (requires license for at least one Defender XDR product) to get the most up-to-date information about the activity and techniques discussed in this blog. These reports provide intelligence, protection information, and recommended actions to prevent, mitigate, or respond to associated threats found in customer environments.

Microsoft Security Copilot customers can also use the [Microsoft Security Copilot integration](https://learn.microsoft.com/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence?bc=%2Fsecurity-copilot%2Fbreadcrumb%2Ftoc.json&toc=%2Fsecurity-copilot%2Ftoc.json#turn-on-the-security-copilot-integration-in-defender-ti) in Microsoft Defender Threat Intelligence, either in the Security Copilot standalone portal or in the [embedded experience](https://learn.microsoft.com/defender/threat-intelligence/using-copilot-threat-intelligence-defender-xdr) in the Microsoft Defender portal to get more information about this threat threat.

## Hunting

### Audit logs and investigation data

Detecting and investigating ARTEX activity depends on logs that some organizations don’t collect by default. An empty result from a hunting query isn’t proof that no access occurred if the underlying logs aren’t collected.

- Microsoft Entra logs**.** Use [Microsoft Entra diagnostic settings](https://learn.microsoft.com/entra/identity/monitoring-health/howto-configure-diagnostic-settings) to send audit logs and sign-in logs to a Log Analytics workspace. [Service principal sign-ins](https://learn.microsoft.com/entra/identity/monitoring-health/concept-sign-ins) are recorded separately from interactive user sign-ins, so include them.
- Microsoft Graph requests**.** [Microsoft Graph activity logs](https://learn.microsoft.com/graph/microsoft-graph-activity-logs-overview) record the requests that applications and users send to Microsoft Graph, including the user agent, which helps scope reconnaissance with stolen application credentials.
- Web server logs**.** [Collect IIS logs](https://learn.microsoft.com/azure/azure-monitor/vm/data-collection-iis) with Azure Monitor and turn on [App Service diagnostic logs](https://learn.microsoft.com/azure/app-service/troubleshoot-diagnostic-logs) so that request bursts and user agents are available for hunting.
- Web application firewall activity**.** [Web Application Firewall logs](https://learn.microsoft.com/azure/web-application-firewall/ag/web-application-firewall-logs) on Application Gateway include access and firewall logs for allowed and blocked requests.

### Microsoft Perception

The following prompts may be used in [Perception](https://learn.microsoft.com/security/agentic-security/agentic-security-overview), utilizing red team, blue team, and green team agents within the Microsoft Defender XDR portal.

**Focus an investigation on ARTEX-driven activity**

```
Investigate recent Defender XDR evidence of automated intrusion activity consistent 
with an agentic AI penetration testing framework such as ARTEX. Look for bursts of web 
requests, scanning, or failed sign-ins from one source; web server processes that run 
shell commands or download tools such as curl, wget, or netcat; new script files in web 
folders; reads of credential and secret files; and service principal sign-ins followed 
by credential changes, privileged role assignments, Microsoft Graph or Azure Resource 
Manager enumeration, or Key Vault and Storage access. Return prioritized findings with 
verdict, affected entities, timeline, supporting alerts and incidents, and evidence-
based next steps. Separate confirmed evidence from assumptions.
```
**Focus triage on ARTEX-driven activity**

Find and summarize recent Defender XDR alerts and incidents in which activity from the same source moves from one attack stage to the next within minutes, such as web application exploitation followed by web shell activity, credential access, or cloud identity abuse. Prioritize activity with user agents that contain artex-enrich or norma. Return affected entities, timeline, supporting alerts and incidents, verdict, and evidence-based next steps.

### Microsoft Defender XDR

Microsoft Defender XDR customers can run the following [advanced hunting](https://learn.microsoft.com/defender-xdr/advanced-hunting-overview) queries to find related activity in their networks. The first three queries require Microsoft Defender for Endpoint on the Windows and Linux servers that host internet-facing applications. The service principal query uses the EntraIdSpnSignInEvents table, which requires Microsoft Entra ID P2.

**Web server processes running bursts of shell commands**

Find web and application server processes that start shells or download tools many times within five minutes. ARTEX agents run commands through web shells and retry at machine speed and have used curl and netcat to download remote access trojans. Tune the threshold, set to 10 distinct commands by default, and exclude build or automation servers that run shells under Java or Node.js.

```
// Shells and download tools started by web or application server processes
let WebServerProcesses = dynamic(["w3wp.exe", "httpd", "apache2", "nginx", "lighttpd",
    "java", "node"]);
let ShellsAndTools = dynamic(["sh", "bash", "dash", "zsh", "cmd.exe", "powershell.exe",
    "pwsh", "pwsh.exe", "curl", "wget", "nc", "ncat", "certutil.exe", "python3", "perl"]);
DeviceProcessEvents
| where InitiatingProcessFileName in~ (WebServerProcesses)
    or InitiatingProcessFileName startswith "php"
| where FileName in~ (ShellsAndTools)
| summarize DistinctCommands = dcount(ProcessCommandLine), Tools = make_set(FileName, 20),
    SampleCommands = make_set(ProcessCommandLine, 25), FirstSeen = min(Timestamp),
    LastSeen = max(Timestamp)
    by DeviceId, DeviceName, InitiatingProcessFileName, bin(Timestamp, 5m)
| where DistinctCommands >= 10
| order by DistinctCommands desc
```
**Script files written to web folders by web or database server processes**

Find script files, such as .php, .jsp, and .aspx files, that web or database server processes create or change, including several files in a short time. ARTEX agents upload web shells with incrementing names and have written web shells through database log files. Content management system updates also write script files, so review the file names and folders.

```
// Script files created or changed by web server or database server processes
let ScriptExtensions = dynamic(["php", "phtml", "jsp", "jspx", "asp", "aspx", "ashx",
    "asmx"]);
let WebServerProcesses = dynamic(["w3wp.exe", "httpd", "apache2", "nginx", "lighttpd",
    "java", "node"]);
let DatabaseProcesses = dynamic(["mysqld", "mariadbd", "postgres", "sqlservr",
    "sqlservr.exe"]);
DeviceFileEvents
| where ActionType in ("FileCreated", "FileModified", "FileRenamed")
| extend Extension = tolower(extract(@"\.([^.]+)$", 1, FileName))
| where Extension in (ScriptExtensions)
| where InitiatingProcessFileName in~ (WebServerProcesses)
    or InitiatingProcessFileName in~ (DatabaseProcesses)
    or InitiatingProcessFileName startswith "php"
| summarize Files = dcount(FileName), FileNames = make_set(FileName, 25),
    Folders = make_set(FolderPath, 10),
    DatabaseWrites = countif(InitiatingProcessFileName in~ (DatabaseProcesses))
    by DeviceId, DeviceName, InitiatingProcessFileName, bin(Timestamp, 10m)
| where DatabaseWrites > 0 or Files >= 3
| order by DatabaseWrites desc, Files desc
```
**Commands that read several kinds of credential and secret files**

Find devices where commands reference three or more kinds of credential and secret files within 10 minutes, such as */etc/shadow*, *.env* files, private keys, and cloud credential files. ARTEX agents read these files in rapid succession after they gain a foothold.

```
// Commands that reference three or more kinds of credential and secret files
let SecretFiles = dynamic(["/etc/shadow", ".env", "id_rsa", "id_ecdsa", "id_ed25519",
    ".aws/credentials", ".azure/", ".kube/config", ".git-credentials", ".pgpass",
    ".my.cnf", "wp-config.php", "web.config", "appsettings.json"]);
DeviceProcessEvents
| where ProcessCommandLine has_any ("shadow", "env", "id_rsa", "id_ecdsa", "id_ed25519",
    "credentials", "azure", "kube", "pgpass", "cnf", "config", "appsettings")
| extend SecretFile = SecretFiles
| mv-expand SecretFile to typeof(string)
| where ProcessCommandLine contains SecretFile
| summarize SecretFileTypes = dcount(SecretFile), SecretFilesSeen = make_set(SecretFile),
    SampleCommands = make_set(ProcessCommandLine, 20), FirstSeen = min(Timestamp)
    by DeviceId, DeviceName, AccountName, bin(Timestamp, 10m)
| where SecretFileTypes >= 3
| order by SecretFileTypes desc
```
**Service principal sign-ins for several applications from one IP address**

Find IP addresses that attempt service principal sign-ins for three or more applications in an hour with both failures and successes, or that send the default ARTEX user agents. Agentic tools have used leaked application credentials across many applications and tenants. Error codes 7000215 and 7000222, an invalid or an expired client secret, show attempts with a credential for the application. When a success follows those failures from the same address, investigate right away.

```
// Service principal sign-ins for several applications from one IP address
EntraIdSpnSignInEvents
| where IsManagedIdentity == false
| summarize ServicePrincipals = dcount(ServicePrincipalId),
    SucceededFor = dcountif(ServicePrincipalId, ErrorCode == 0),
    FailedSignIns = countif(ErrorCode != 0),
    InvalidOrExpiredSecret = countif(ErrorCode in (7000215, 7000222)),
    ArtexUserAgent = countif(UserAgent has_any ("artex", "norma")),
    Applications = make_set(ServicePrincipalName, 20),
    Resources = make_set(ResourceDisplayName, 20), UserAgents = make_set(UserAgent, 10),
    FirstSeen = min(Timestamp), LastSeen = max(Timestamp)
    by IPAddress, bin(Timestamp, 1h)
| where (ServicePrincipals >= 3 and SucceededFor >= 1 and FailedSignIns >= 1)
    or ArtexUserAgent > 0
| order by ServicePrincipals desc
```
### Microsoft Sentinel

These queries require Microsoft Entra ID audit logs, and IIS logs, App Service HTTP logs, or Application Gateway access logs in the workspace.

**Machine-speed web request bursts and default ARTEX user agents**

Find client IP addresses that request 100 or more distinct paths with 50 or more client errors in one minute, or that send the default ARTEX user agents, artex-enrich and norma. The query also flags the default user agents of tools that ARTEX runs, such as curl, Wget, Python HTTP clients, headless Chromium, and Nmap. Those are common in legitimate automation, so don’t alert on them alone.

```
// Requests per client IP per minute, with default ARTEX and tool user agents flagged
union isfuzzy=true
    (W3CIISLog
    | project TimeGenerated, LogSource = "IIS", ClientIP = cIP, Path = csUriStem,
        Status = tostring(scStatus), UserAgent = csUserAgent, Target = Computer),
    (AppServiceHTTPLogs
    | project TimeGenerated, LogSource = "App Service", ClientIP = CIp, Path = CsUriStem,
        Status = tostring(ScStatus), UserAgent, Target = CsHost),
    (AGWAccessLogs
    | project TimeGenerated, LogSource = "Application Gateway", ClientIP = ClientIp,
        Path = RequestUri, Status = tostring(HttpStatus), UserAgent, Target = Host)
| extend AgentType = case(
    UserAgent has_any ("artex", "norma"), "ARTEX default",
    UserAgent matches regex @"^(curl|Wget|python-requests|Python-urllib|Go-http-client)/",
        "Tool default",
    UserAgent has_any ("HeadlessChrome", "Nmap"), "Tool default",
    "Other")
| summarize Requests = count(), DistinctPaths = dcount(Path),
    ClientErrors = countif(Status startswith "4"),
    ArtexAgentRequests = countif(AgentType == "ARTEX default"),
    ToolAgentRequests = countif(AgentType == "Tool default"),
    UserAgents = make_set(UserAgent, 10), Targets = make_set(Target, 10)
    by ClientIP, LogSource, bin(TimeGenerated, 1m)
| where ArtexAgentRequests > 0 or (DistinctPaths >= 100 and ClientErrors >= 50)
| order by ArtexAgentRequests desc, DistinctPaths desc
```
**Application credential changes and role assignments by the same identity**

Find users or applications that both add or change application credentials and assign directory roles or application permissions within an hour. During Storm-0940 activity, ARTEX agents added credentials to applications, and an application assigned itself the Global Administrator role.

```
// Credential changes and role assignments made by the same identity within an hour
AuditLogs
| where Result =~ "success"
| where OperationName in ("Add service principal credentials", "Add member to role",
    "Add app role assignment to service principal")
    or OperationName contains "Certificates and secrets management"
| extend Stage = iff(OperationName has_any ("credentials", "Certificates"), "Credential",
    "Role")
| extend ActorUpn = tostring(InitiatedBy.user.userPrincipalName),
    ActorServicePrincipalId = tostring(InitiatedBy.app.servicePrincipalId),
    ActorAppId = tostring(InitiatedBy.app.appId),
    TargetName = tostring(TargetResources[0].displayName)
| extend Actor = coalesce(ActorUpn, ActorServicePrincipalId, ActorAppId)
| summarize Stages = make_set(Stage), Operations = make_set(OperationName),
    Targets = make_set(TargetName, 20), FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated)
    by Actor, ActorAppId, bin(TimeGenerated, 1h)
| where array_length(Stages) == 2
| order by FirstSeen desc
```
## MITRE ATT&CK techniques

This tool has exhibited use of the following attack techniques. For standard industry documentation about these techniques, refer to the [MITRE ATT&CK framework](https://attack.mitre.org/).

**Resource Development**

- [T1588.007 Obtain Capabilities: Artificial Intelligence](https://attack.mitre.org/techniques/T1588/007/) | Threat actors obtain ARTEX from public repositories or forks and pair it with commercial or self-hosted LLMs.
- [T1588.002 Obtain Capabilities: Tool](https://attack.mitre.org/techniques/T1588/002/) | ARTEX agents install offensive tools at runtime or write equivalent scripts.

**Reconnaissance**

- [T1595.001 Active Scanning: Scanning IP Blocks](https://attack.mitre.org/techniques/T1595/001/) | ARTEX runs nmap for port and service scanning.
- [T1595.002 Active Scanning: Vulnerability Scanning](https://attack.mitre.org/techniques/T1595/002/) | ARTEX agents probe web applications and APIs for injection, authentication, and access-control weaknesses.
- [T1595.003 Active Scanning: Wordlist Scanning](https://attack.mitre.org/techniques/T1595/003/) | ARTEX agents enumerate directories, endpoints, and file names, sending hundreds of requests to learn which ones the server allows.
- [T1594 Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594/) | ARTEX agents harvest JavaScript bundles, source maps, runtime configuration, and API documentation from target applications to discover internal API routes, and ARTEX’s enrichment component collects page titles from discovered sites.

**Initial Access**

- [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | ARTEX agents exploit injection, file upload, authentication, and access-control flaws in internet-facing applications.
- [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/) | ARTEX reuses credentials that it captures, or that the operator supplies, against applications, hosts, and services.
- [T1078.004 Valid Accounts: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/) | ARTEX agents authenticated to Microsoft 365 tenants with stolen application credentials that Storm-0940 supplied.
- [T1199 Trusted Relationship](https://attack.mitre.org/techniques/T1199/) | ARTEX agents reached downstream tenants through an already-consented third-party application whose credentials Storm-0940 had stolen.

**Execution**

- [T1059 Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/) | ARTEX runs shell, Python, and PowerShell commands on compromised servers through command injection, web shells, and remote shells.
- [T1651 Cloud Administration Command](https://attack.mitre.org/techniques/T1651/) | ARTEX agents have run commands through cloud administration interfaces, such as Kudu, when they had credentials for them.

**Persistence**

- [T1505.003 Server Software Component: Web Shell](https://attack.mitre.org/techniques/T1505/003/) | ARTEX uploads web shells, or writes them through database logging, and then sends commands to them.
- [T1098.001 Account Manipulation: Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/) | ARTEX agents added credentials to applications to maintain access during Storm-0940 activity.

**Privilege Escalation**

- [T1098.003 Account Manipulation: Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003/) | ARTEX agents assigned privileged roles during Storm-0940 activity, including an application assigning itself the Global Administrator role.

**Credential Access**

- [T1110.001 Brute Force: Password Guessing](https://attack.mitre.org/techniques/T1110/001/) | ARTEX tests weak passwords and brute forces sign-in forms.
- [T1110.003 Brute Force: Password Spraying](https://attack.mitre.org/techniques/T1110/003/) | Storm-0940 used ARTEX to accelerate password spraying against Microsoft 365, and other actors have used it to spray identity providers.
- [T1552.001 Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | ARTEX reads *.env* files, configuration files, and keys after gaining a foothold.
- [T1003.008 OS Credential Dumping: /etc/passwd and /etc/shadow](https://attack.mitre.org/techniques/T1003/008/) | ARTEX reads */etc/shadow* on compromised Linux servers.
- [T1552.005 Unsecured Credentials: Cloud Instance Metadata API](https://attack.mitre.org/techniques/T1552/005/) | ARTEX agents have used an XXE flaw to query a cloud metadata service for role credentials.
- [T1558.003 Steal or Forge Kerberos Tickets: Kerberoasting](https://attack.mitre.org/techniques/T1558/003/) | ARTEX agents run Kerberoasting scripts in compromised domains.
- [T1003.006 OS Credential Dumping: DCSync](https://attack.mitre.org/techniques/T1003/006/) | ARTEX agents run DCSync scripts to obtain domain credentials.

**Discovery**

- [T1087.004 Account Discovery: Cloud Account](https://attack.mitre.org/techniques/T1087/004/) | ARTEX agents performed Microsoft Graph and directory reconnaissance during Storm-0940 activity.
- [T1087.002 Account Discovery: Domain Account](https://attack.mitre.org/techniques/T1087/002/) | ARTEX agents enumerate Active Directory objects, including privileged groups.
- [T1580 Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580/) | ARTEX agents map the permissions of stolen cloud credentials and enumerate cloud resources.

**Lateral Movement**

- [T1021 Remote Services](https://attack.mitre.org/techniques/T1021/) | ARTEX agents capture credentials for other reachable systems and move laterally through remote services such as Secure Shell (SSH) and WinRM.

**Collection**

- [T1213.006 Data from Information Repositories: Databases](https://attack.mitre.org/techniques/T1213/006) | ARTEX extracts database contents through SQL injection, such as with sqlmap, or with database clients.
- [T1530 Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/) | ARTEX agents perform mass reads from cloud storage with stolen credentials.

**Command and Control**

- [T1090 Proxy](https://attack.mitre.org/techniques/T1090/) | ARTEX can send target traffic through a configured outbound proxy. Threat actors have rotated through virtual private network (VPN), proxy, and Tor infrastructure when blocked.
- [T1102.002 Web Service: Bidirectional Communication](https://attack.mitre.org/techniques/T1102/002/) | ARTEX agents have used curl with rotating *webhook.site* URLs to deliver scripts to a compromised server and return command output.

### References

- [AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/). Microsoft
- [ARTEX abuse expands as cybercriminals target financial sector](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/). Microsoft
- [Threat actors use agentic AI tooling to find and abuse exposed secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/). Microsoft
- [AI, Scripts, Operator: Inside the ConnectWise Attack](https://www.huntress.com/blog/connectwise-attack-ai). Huntress
- [ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors). Wiz
- [ARTEX and Friends: Enter Agentic Offensive Frameworks](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks). Google Threat Intelligence Group
- [VAPOR PANDA Uses AI-Driven ARTEX to Scale a Global Espionage Campaign](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/). CrowdStrike
- [Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/). CrowdStrike

### Learn more

For the latest security research from the Microsoft Threat Intelligence community, check out the [Microsoft Threat Intelligence Blog](https://aka.ms/threatintelblog).

To get notified about new publications and to join discussions on social media, follow us on [LinkedIn](https://www.linkedin.com/showcase/microsoft-threat-intelligence), [X (formerly Twitter)](https://x.com/MsftSecIntel), and [Bluesky](https://bsky.app/profile/threatintel.microsoft.com).

To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the [Microsoft Threat Intelligence podcast](https://thecyberwire.com/podcasts/microsoft-threat-intelligence).
