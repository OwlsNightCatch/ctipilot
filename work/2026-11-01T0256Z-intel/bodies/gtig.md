---
title: "ARTEX and Friends: Enter Agentic Offensive Frameworks | Google Cloud Blog"
author: Google Threat Intelligence Group; Mandiant
url: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks
hostname: google.com
description: Mandiant and GTIG provide remediation guidance against a new paradigm of machine-speed intrusions driven by threat actors using ARTEX and similar agentic pentesting frameworks.
sitename: Google Cloud Blog
date: "2026-10-31"
tags: ['Threat Intelligence']
fingerprint: b5139adb4623d3cd
---
# ARTEX and Friends: Enter Agentic Offensive Frameworks

##### Google Threat Intelligence Group

##### Mandiant

Written by: Aurora Blum, David Mainor, Rohit Nambiar, Omar ElAhdan, Matthew McWhirt, Will Silverstone, Bhavesh Dhake, Chris Busse

### Introduction 

Recent intrusions in which threat actors have been observed weaponizing agentic frameworks to execute highly-automated intrusions has put a spotlight on evolving adversarial use of LLMs. In our [September 2026 report](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai), Google Threat Intelligence Group (GTIG) noted that forward leaning adversaries were beginning to transition from basic prompting to agentic workflows and LLM-enabled automation.

Since this publication, GTIG and Mandiant have observed multiple threat actors abusing the open-source, agentic pentesting frameworks ARTEX, Hexstrike and CAIRN in incident response engagements to conduct a broad range of actions across multiple phases of the attack life cycle. This activity has been seen across the threat landscape, as noted in a recent Wiz [report](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors). The emergence of Artex and similar agentic offensive intrusion frameworks underscores a broader shift toward threat actor adoption of open source multi-agent offensive frameworks, as well as potentially custom agentic harnesses.

This represents a paradigm shift towards intrusions occurring at machine speed, with the automated chaining of complex attack paths scaling intrusions exponentially. While the mechanics of the intrusions remain the same, such as using compromised credentials and targeting unpatched systems, the speed and scale at which frameworks can exploit these known weaknesses introduces a new defensive challenge. Security teams, developers, and system administrators will need to fundamentally rethink defense strategies to counter scalable, autonomous software. We also provide defensive strategies from Mandiant Consulting. The defensive strategies suggested—control-plane isolation, short-lived credentials, least privilege, segmentation, and behavioral detection—are long-standing security best practices.

### Observations in the Wild

We are seeing tools used by adversaries evolving towards autonomous agentic attacks. One way this is occurring is through suites of tools or frameworks designed for penetration testing (“pentesting”). These tools and frameworks orchestrate various agents using open source and frontier LLMs to automate various stages of intrusions. Historically, cyber espionage and financially motivated threat actors have taken advantage of pentesting or red-teaming platforms built for security professionals to exploit systems, such as Cobalt Strike or Metasploit. Today, adversaries are pivoting toward offensive frameworks powered by LLMs. While these frameworks have existed in the wild, they are now yielding success in intrusions in the wild, representing a critical evolution that increases both the speed and scale of intrusion activity.

Since late August 2026, we have observed threat actors actively operating popular open-source multi-agent pentesting platforms like ARTEX, PentAGI, CAIRN and other potentially custom harnesses within Mandiant incident response engagements; use of these platforms has been further corroborated by our research telemetry. In these incidents, we have observed agentic activity conducting significant parts of the attack lifecycle (e.g., lateral movement, database exploitation, exfiltration preparation). Evidence of in the wild usage of these frameworks marks a critical inflection point for defenders, as agents now autonomously explore multiple attack paths, troubleshoot errors, and achieve objectives in seconds and minutes. Coupled with continual advancements in underlying LLM capabilities, the acceleration in attack velocity and scale signals a notable shift in the threat landscape that fundamentally alters traditional intrusion dynamics.

#### ARTEX Framework

ARTEX is an autonomous, multi-agent LLM-driven pentesting and offensive command-and-control (C2) platform written in Go with an embedded Next.js web console. The framework was originally developed by the user [Autumn-27](https://github.com/Autumn-27) and released on GitHub. Although the original repository was taken down by its creator in October 2026 due to widespread threat actor abuse, the framework continues to proliferate globally via community forks, including localized variations such as ScopeWeaver and a commercial version dubbed ARTEX PRO. ARTEX abstracts the attack lifecycle across six specialized sub-agents. By leveraging APIs from frontier and open source models, the framework translates high-level tactical goals into actionable machine commands. GTIG has observed capabilities including automated Active Directory reconnaissance, privilege escalation, target cloud-infrastructure profiling (such as harvesting Azure storage keys), to the synthesis and deployment of custom webshells.

Since late August 2026, ARTEX has been adopted by a diverse range of threat actors across the motivational spectrum, including both financially motivated extortion groups and suspected cyber espionage operators. For example, the Wiz Research team has been tracking a campaign associated with ARTEX, which GTIG tracks as UNC7228, that overlaps with activity tracked by [Microsoft as the PRC-nexus actor STORM-0940](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/). The research has expanded Wiz’s understanding of this campaign beyond the [October IT focused activity](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors) with activity now dating back to at least August 2026. Wiz identified the targeting, compromise, and data theft affecting multiple entities in the US and Europe across the enterprise software, industrial automation, semiconductor manufacturing and design, and telecommunications industry verticals. This actor has moved extremely quickly, typically moving from their first compromised account to deep system access in around four hours and in one case as rapidly as 15 minutes. They have also customized their tooling to take advantage of victim-specific setups and fallen back to open proxies if their initial infrastructure was blocked.

Demonstrating broader adoption of ARTEX, GTIG and Mandiant observed multiple other threat actors using ARTEX for post-compromise reconnaissance, lateral movement, and privilege escalation in incident response investigations. This includes financially motivated threat actors who used the framework to facilitate data theft extortion, and additional suspected PRC-nexus clusters. Their operations collectively impacted organizations across government, technology, chemicals and materials, and manufacturing sectors in the US, alongside [public reporting](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) of ARTEX targeting the financial sector in Asia.

In several cases, adversaries provided ARTEX with compromised credentials for the targeted organization, and instructed the framework to execute subsequent stages of the attack lifecycle. Analysis of these intrusions reveals key differences between activity conducted by the ARTEX framework and that of a human operator:

- Based on log files and timestamps, we identified bursts of activity that would be highly irregular for a human operator. While each of the intrusions exhibited extended pauses during operational phases, individual ARTEX execution sequences ran in compressed bursts of roughly 2 to 25 seconds. In at least one operation, we observed 27 events in 23 seconds of active burst time, performing rapid probing of AWS permissions across different security groups. While preparing potential exfiltration scripts, ARTEX was capable of successfully adapting to errors quoting “script too large” by trimming the script and relaunching it to successfully deploy a 17-snapshot instance in approximately 10 seconds.
- Compared to a competent human operator, ARTEX achieved code execution in a far more forensically noisy manner, relying on rapid, iterative trial-and-error. In one instance, supplied with valid credentials, ARTEX accessed an external-facing Linux Weaver OA web server to execute SQL commands via exposed API calls. Using legitimately-exposed application-specific API calls, ARTEX was able to achieve partial command-execution to conduct further reconnaissance despite hitting technical complexities. However, this process generated 240 log events and exhibited errors potentially caused by multiple sub-agents overwriting one another while pursuing the same objective.
- In an attempt to pivot from a database-execution context to a system-execution context, ARTEX used an application-specific SQL API, accessible to the supplied-user credential, to modify the MySQL instance to write log files with a `.jsp` extension to publicly accessible locations. The SQL-commands executed were likely intended to poison MySQL logs into writing web-accessible JSP webshells.
- Using the API, ARTEX ran `SET GLOBAL general_log_file = '<path to webshell>’` followed by `SET GLOBAL general_log = 1`; subsequent SQL commands were written to the filepath defined in `general_log_file`. ARTEX then ran SQL SELECT statements in the form `` `SELECT '<% [webshell content] %>'` ``. Due to how the underlying Java web servlet handles JSP files, the Java code in the '\<% %>' gets parsed and compiled into the process memory space, providing means of execution.
- Log activity shows multiple iterations of the above sequence, with ephemeral, somewhat-incremental file names (`cl1217.jsp, f1219a.jsp, z1219.jsp`) for each webshell candidate, each one executing a different command. Errors when trying to run the webshell (e.g. `variable ‘t is already defined`’) caused the webshell to fail and likely had ARTEX refactor its approach, writing several unique webshells, each with a different goal, some correcting previous errors until the `.jsp` webshells executed cleanly and returned valid command output to ARTEX.

In another case, during access-probing efforts, ARTEX generated files of various extension types with the filename `artex-probe-*`, where `*` carried five digit somewhat-incremental numbers. Based on our visibility, it’s difficult to comment on the exact significance of these numbers or how they increment. However, ARTEX was seen using similar incremental numeric markers within dropped file names, created account names, their passwords and within email subjects.

#### Observed ARTEX Activity Mapped along the phases of a targeted attack lifecycle

#### PentAGI Offensive Framework

GTIG also observed in the wild abuse of PentAGI (Penetration Testing Artificial General Intelligence), an autonomous offensive framework designed to automate the pentesting process within an isolated environment. Developed by VXControl, the framework is offered in an open source and commercial edition. It is designed so that the user only needs to describe a target and a goal, which enables entry-level users to run complex cyber security campaigns. Once the target and the goal have been selected, the framework uses a team of specialized agents, each with their own functionalities to break tasks (called “Flows”) into various sub-tasks, execute each step, and report on it. The tools and commands are all run in isolated sandboxes running Kali Linux instead of in the host environment. All the tools used by PentAGI are open-source pentesting tools available by default in Kali Linux (e.g., metasploit, nmap, SQLmap). The framework supports over a dozen cloud and local LLM backends, including frontier and open weight models.

The majority of observed PentAGI activity remained at the stage of WHOIS asset mapping or active vulnerability scanning. However, analysis of operational artifacts indicates that some operations progressed to active intrusions and persistence across multiple organizations. Operators are also adapting and integrating the framework in different ways. In one case, we identified a customized attack orchestration platform built on the open-source version of PentAGI likely used between at least late August and early October 2026 to conduct systematic reconnaissance and vulnerability scanning against a wide range of organizations in Asia, including system integrators and major telecommunications firms. In another instance, we observed PentAGI chained with proxy services to target the Aerospace sector.

### Evolution of Autonomous Offensive Frameworks

We are seeing a significant maturation in the application of LLM capabilities across the threat landscape in a short period of time; this includes the incorporation of LLM-written malicious code, development of dynamic LLM-enabled malware, poisoning of agent-harness files, and the building of multi-agent offensive frameworks. Notably, between late 2025 and October 2026, autonomous and semi-autonomous offensive frameworks crossed a decisive operational threshold to multi-agent frameworks actively weaponized by threat actors to perform in the wild intrusions.

GTIG has been tracking the evolution of this experimentation over time, from simple prompting of LLMs to help with coding, through the use of frameworks in the wild towards a potential future with fully autonomous frameworks running intrusions. In a fully autonomous attack, a human’s role would consist of telling the agent what to target, and then simply benefiting from the operational objective.

At the time of reporting, we assess that the current adversary use of autonomous offensive frameworks is still in early stages characterized by open source tools currently being used in low-sophisticated ways, resulting in broad and noisy, but still successful campaigns. As the sophistication of these frameworks, the underlying LLMs and the orchestrating human-operator increase, we expect to see not only less human interaction, but also increased stealth and sophistication.

The following stages represent our observations of how LLM-augmentation in cyber operations have evolved over the last year and how we expect this development to continue:

**Stage 1: Prompt-based use of LLMs**

- **Activity**: Adversaries interact with LLMs in a prompt based chatbot fashion, using LLMs to write and debug code for malware, draft phishing emails, create personas, and conduct light reconnaissance on targets.
- **Evolution**: Adversaries outsource low-failure, easy-to-rectify, tasks to an LLM to increase speed of simple discrete tasks.
- **Timeframe:** [End of 2025 to early 2026](https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai?e=48754805)

**Stage 2: Embedding LLM capabilities into malware** 

- **Activity**: Adversaries trust an LLM to take certain low-failure, easy to execute actions, particularly writing code, such as in malware families like HONESTCUE or PROMPTSPY using LLMs dynamically during execution to, for example, obfuscate payloads in different ways in attempts to evade defenses.
- **Evolution**: Adversaries begin use incorporating LLMs into post-intrusion attack phases.
- **Timeframe**: [Early 2026](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use?e=48754805)

**Stage 3: Incorporating LLM-enabled automation into operations** 

- **Activity**: As agentic capabilities develop, adversaries begin using them for discrete tasks (e.g., standing up or debugging malware development environments). Agents begin being used alongside human-operators to develop novel exploits and to assist with high-stake vulnerability research. Adversaries begin being more cognizant of OPSEC and visibility into their LLM-usage operations and start using LLM-proxy services to obscure activities.
- **Evolution**: LLMs being used for more high-stake tasks but with human operators in the loop.
- **Timeframe**: Early 2026 - [September 2026](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai?e=48754805) 

**Stage 4: Developing and experimenting with autonomous frameworks**  

- **Activity**: Adversaries begin developing and experimenting with autonomous frameworks. Campaigns begin offloading more stages of the lifecycle to LLM-augmented tooling, and integrating model APIs into their tools and telegram bots to take autonomous action.
- **Evolution**: Experimentation with LLMs running more stages of the attack lifecycle.
- **Timeframe**: [Mid 2026 - September 2026](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai?e=48754805) 

**Stage 5: Multiple attack lifecycle stages being conducted by LLM-driven tooling in the wild**

- **Activity**: In the wild evidence of multiple attack lifecycle stages being conducted by LLM-driven tooling, with fewer humans in the loop during operations. Observations surrounding mass-exploitation campaigns where a substantial portion of the lifecycle is being carried out by an agent, requiring only minimal human intervention, as well as activity accompanied by malware possessing more autonomous capabilities. Additionally, continued experimentation by threat actors with better obfuscation—including LLM mixers, inference services, local models. Overall TTPs of these attacks remain messy, noisy but yet successful.
- **Evolution**: Adversaries have actively integrated LLMs into their operations to conduct successful intrusions, while simultaneously exploring ways to obscure/reduce reliance on frontier-lab LLMs.
- **Timeframe**: Current stage of development

**Stage 6: Multi-agent-driven, unsophisticated attacks with little to no human interaction** 

- **Activity**: Highly-autonomous, but unsophisticated, forensically noisy operations with human operators no longer in the loop. Adversaries define the target and objective, while multi-agent frameworks execute the entire attack chain and return operational objectives.
- **Evolution**: Adversaries diversifying infrastructure and tooling, further inhibiting defenders’ visibility.
- **Timeframe**: Near-term (1 - 3 months)

**Stage 7:  Sophisticated, fully autonomous/agentic attacks** 

- **Activity**: This stage represents peak maturity on the offensive LLMs capability curve, characterized not only by fully autonomous intrusions requiring little to no human interaction, but also by increased stealth and sophistication of the activity, with operators interacting with LLMs through either obscurely designed infrastructure or self-hosted LLMs altogether.
- **Evolution**: This stage would grant autonomous and stealthier operations while limiting defender’s visibility into the activity.
- **Timeframe**: Medium-term (3 - 6 months)

We believe malicious actors will continue to experiment with these offensive agentic frameworks, moving towards future autonomous usage. GTIG has observed evidence of threat-actor experimentation with tools like the ZeroHollow inference service and the fully agentic framework [AgentZero](https://github.com/agent0ai/agent-zero).

### Outlook

Over the past 12 months, GTIG has observed a decisive evolution in adversarial tradecraft leveraging LLMs, progressing from ad hoc operational productivity support toward the deployment of coordinated, multi-agent, autonomous offensive frameworks. While earlier milestones documented in our quarterly [research](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) highlighted early agentic interest, recent observations across frontline incident response engagements and proactive intelligence collection reveals adversary adoption of these frameworks to automate discrete phases and specific operational tasks during intrusions. Threat actors are increasingly leveraging generative models to achieve unprecedented speed and scale, actively developing more complex attack infrastructure powered by agentic AI capabilities and AI-enabled automation.

Frameworks such as ARTEX compress attack timelines to machine speed; however, they currently trade stealth for velocity. Unrestricted autonomous execution generates forensic traffic, relies on recognizable identifiers, and leaves behind distinct code-level traces, increasing the likelihood of detection and mitigation. These tools are therefore best suited to scenarios in which the cost of detection is low. Additionally, detection and disruption/response are two different functions–simply detecting the attack in time does little to hinder objective completion.

Consequently, GTIG assesses with high confidence that cyber crime threat actors will continue incorporating autonomous offensive tools into their operations, given that the increased reach of their campaigns will likely compensate for any decreases in success rates. We anticipate that actors, who specialize in stealthy operations designed to maintain long-term access, are less likely to use the publicly available versions of these tools, though they may employ them for purposes of scale and speed, depending on operational priorities. Regardless of motivation, the low barrier to entry, ease of integrating new exploits, and massive scaling potential make autonomous frameworks an attractive, low-cost force multiplier for a wide range of threat actors, making it highly likely that we will continue to see increasing threat actor adoption of these types of frameworks in the near term.

### Defending Against AI-Enabled Attacks: Five Layers of Defense

LLM-enabled offensive tooling does not fundamentally change the techniques attackers use. It reduces the time required to combine them. Credential discovery, permission testing, lateral movement, and data access that previously required hours of operator effort can now occur in minutes, frequently through valid identities and supported functionality that static indicators will not detect. Organizations are best positioned to withstand this when compromise of a single identity, credential, or workload provides only limited access. Restricting control-plane exposure, replacing long-lived secrets with short-lived and tightly scoped credentials, segmenting application tiers, and placing guardrails on high-impact business functions all reduce the speed advantage automation provides. Behavioral detection addresses the activity that these controls do not prevent, but it depends on having sufficient identity, control-plane, data-plane, and network telemetry to establish what normal activity looks like. Many of these controls are already familiar to defenders. The difference is that automated tooling can now identify and exploit the gaps between them far more quickly.

As illustrated above, LLM-enabled offensive tooling is increasing the speed and scale of cyber attacks. LLM-enabled and autonomous tools can identify weaknesses, test access, interpret errors, adjust their approach, and continue through an attack path with limited human interaction. Work that might previously have required an operator to investigate an environment, write or modify code, troubleshoot failures, and execute the next step over several hours can increasingly happen in minutes.

This creates a detection challenge as well. Much of the activity may use valid credentials and supported functionality (living-off-the-land, LotL). An attacker may authenticate with a legitimate service principal, call a normal management API, access cloud storage through a supported protocol, or execute commands through an existing administrative interface. Tool names, hashes, IP addresses, and other static indicators provide useful signals when available, but they will not cover much of this activity.

Effective defenses combine two capabilities:

1. Controls that limit what an attacker can do after gaining valid access.
2. Telemetry that shows when an identity, application, or workload begins operating outside its normal pattern.

#### How Adversarial Use of LLMs Changes the Attacker Timeline

Several themes repeatedly appear during investigations involving LLM-enabled or highly automated attacker activity:

- **Speed and scale**: Automated tooling can perform broad reconnaissance, test several attack paths at once, react to failures, and immediately continue into follow-on activity. The time between initial access, privilege discovery, lateral movement, and data access can become very short.
- **Interconnected environments**: Attackers rarely remain inside one technology stack. An internet-facing application may expose credentials in a configuration file. Those credentials may provide access to cloud storage, source repositories, identity systems, or internal infrastructure. Automation makes it easier to discover and test those relationships quickly.
- **Legitimate-looking identity activity**: Many actions look normal when viewed independently. A service principal authenticates, an API is called, a storage object is downloaded. The stronger signal often comes from context: where the request originated, how much activity occurred, what happened immediately before and after it, and whether the behavior is expected for that identity.
- **Control-plane and data-plane blind spots**: Many organizations have mature endpoint monitoring but considerably less visibility into management APIs, programmatic identities, and cloud storage activity. Permission testing, retrieval of storage keys, bulk downloads, firewall changes, and management API calls may all be logged without generating useful alerts.

Mandiant recommends structuring enterprise defenses across five foundational layers designed to restrict lateral movement and limit the speed advantage of autonomous tooling:

Table 1: Foundational layers for restricting adversarial LLM speed advantage and lateral movement

### Layer 1: Protect the Control Plane

Restrict access to the systems attackers can use to administer, deploy, or reconfigure the environment.

The control plane extends well beyond Active Directory or a cloud console. It includes identity providers, cloud management APIs, network and firewall management platforms, virtualization infrastructure, code repositories, CI/CD systems, privileged access management platforms, backup infrastructure, certificate authorities, SaaS administration consoles, and application administration interfaces.

#### Why It Is Important

Internet-accessible management interfaces can quickly become part of an attack path after credentials are obtained. For example, Azure App Service includes an administrative interface through Kudu Site Control Manager, or SCM, which supports application deployment and management functionality. If an attacker obtains publishing credentials or another identity capable of accessing that interface, automation can quickly test authentication, enumerate functionality, interact with application files, execute commands, retrieve output, and remove staged artifacts.

Similar exposure exists across firewall administration, virtualization consoles, cloud management APIs, backup platforms, CI/CD interfaces, and other management services. Any reachable administrative path gives an automated attacker another capability to test.

#### Mitigations

- **Reduce Administrative Internet Exposure**: Restrict cloud administration, network device management, application publishing interfaces, hypervisors, backup platforms, and other sensitive services to trusted networks, private connectivity, or dedicated administrative paths wherever possible.
- **Require Trusted Administrative Paths**: Require privileged users to administer sensitive infrastructure from managed devices, privileged access workstations, or approved jump hosts. Pair these controls with phishing-resistant authentication such as FIDO2 or passkeys where supported.
- **Harden Application Management Interfaces**: Treat application administration and publishing endpoints as privileged infrastructure rather than extensions of the public application.
- Configure access restrictions for Kudu/SCM endpoints separately where appropriate.
- Limit SCM access to approved management networks or deployment infrastructure.
- Disable basic publishing authentication where it is not required.
- Restrict access to deployment and publishing credentials.
- Consider deployment models such as run-from-package that reduce direct modification of deployed application files.
- **Control Public Exposure by Design**: Establish governance around public IP allocation and require architecture review before workloads or management interfaces are exposed directly to the internet.
- **Apply Similar Controls to Programmatic Administration**: Where supported, restrict administrative service principals and automation identities to expected networks, workloads, or private connectivity.
- **Monitor the Control Plane as a Distinct Security Surface**: Centralize authentication, configuration change, deployment, and administrative telemetry from cloud platforms, application administration interfaces, network infrastructure, backup platforms, and other management systems. Alert on administrative access from previously unseen networks, hosting providers, or geographies.

### Layer 2: Restrict Identities and Keys

Reduce the value of stolen credentials by limiting their lifetime, permissions, and where they can be used.

Security programs have traditionally placed more emphasis on human identities. Service principals, service accounts, API keys, storage keys, cloud access keys, deployment tokens, personal access tokens, and application secrets can receive less scrutiny despite providing significant access.

Programmatic identities are especially useful to an automated attacker when they combine long-lived credentials, broad permissions, limited conditional controls, and limited monitoring.

#### Why It Is Important

Consider an exposed cloud storage credential. Once automated tooling discovers the credential in source code, an environment variable, application configuration, a database, or another compromised system, it can immediately test the credential and begin enumerating available data.

A long-lived credential that works from anywhere on the internet and provides broad storage access can turn a single credential exposure into large-scale data access very quickly.

The same pattern applies to service principals and other programmatic identities. A credential intended for an internal CI/CD runner carries considerably more risk when the identity can also authenticate from an arbitrary network and access production resources.

Credential security therefore needs to address both what an identity can access and the conditions under which that access is valid.

#### Mitigations

- **Prioritize Workload and Programmatic Identities**: Apply the same rigor used for privileged human identities to service principals, service accounts, API keys, cloud access keys, application credentials, deployment tokens, and Personal Access Tokens. These identities should have defined owners, lifecycle controls, least privilege, monitoring, and incident response procedures.
- **Move From Long-Lived to Short-Lived Credentials**: Remove persistent secrets and use temporary or workload-bound credentials wherever possible.
- Transition from static AWS IAM access keys to temporary credentials through IAM roles.
- Replace Azure Service Principal client secrets with Managed Identities.
- Disallow Azure Storage Account Shared Key Authentication in favor of Entra ID authorization with Conditional Access Policies.
- Use Google Cloud Workload Identity Federation instead of long-lived service-account keys.
- Move from GitHub classic PATs to fine-grained PATs or workload-based authentication such as GitHub Actions OIDC where supported.
- **Constrain Both the Where and the What**: Limit non-human identities to the APIs, subscriptions, projects, repositories, storage resources, and systems that they actually require. Where supported, restrict the locations and workloads from which those identities can authenticate. A service principal used by an internal CI/CD runner should not also be usable from arbitrary external infrastructure.
- Hardening multi-cloud service principals requires replacing long-lived, static credentials with short-lived tokens and strictly enforcing access controls. Essential approaches across major providers include:
- **Google Cloud**: Using Workload Identity Federation and targeted IAM constraints.
- **AWS**: Leveraging OIDC federation combined with Service Control Policies (SCPs).
- **Azure**: Applying Conditional Access policies to restrict access contextually.
- **Okta**: Implementing Private Key JWT authentication along with network-restricted Authentication Policies.
- Use private connectivity, expected source ranges, workload federation, resource policies, and IAM conditions where appropriate across cloud platforms.
- **Restrict AWS IAM Role Delegation**: Tightly control permissions that allow one identity to assign or pass another identity’s privileges. In AWS, restrict iam:PassRole to specific roles and intended services and apply conditions such as iam:PassedToService where appropriate.
- **Isolate Credential and Secret Stores**: Place enterprise password vaults and secret management systems behind tightly controlled administrative and network paths. Require strong authentication for privileged access, restrict programmatic access to expected workloads and networks where supported, and alert on unusual bulk secret queries, enumeration, or export activity. These detections overlap with legitimate automation; the signal is in the identity, origin, volume, and sequence, not the action. Baseline known-good automation first and alert on deviation, or expect false positives on routine activity.
- **Harden Password Reset and Account Lifecycle Processes**: Require strong re-authentication or additional identity verification for high-risk password resets and account recovery. Monitor unusual bursts of password resets, account creation, credential additions, permission changes, or other lifecycle activity.
- **Automate Secret Hygiene**: Implement continuous scanning of repositories, container images, build artifacts, and pipelines for exposed secrets and credentials. Remove credentials from application code, configuration files, deployment scripts, and databases and move them into dedicated secret-management platforms. Rotate exposed credentials promptly rather than relying on removal from source-control history.

### Layer 3: Harden Configurations and Reduce Attack Paths

Remove weaknesses that provide an initial foothold and limit how far a compromised workload can reach.

Automated tooling is particularly effective in environments where several smaller weaknesses can be combined into a larger attack path. An exposed application, an overly privileged workload identity, a credential in an environment variable, and unrestricted network access may each appear manageable in isolation. Together, they can provide a direct path into sensitive systems.

#### Why It Is Important

A vulnerability in an internet-facing application may initially appear isolated. In practice, that application may have access to a backend database. The database may contain credentials. Application environment variables may contain cloud tokens. The underlying host may have an attached cloud identity with access to storage, secrets, or management APIs.

Automation can test those paths in rapid succession. Failures can also become useful feedback. An application error, stack trace, database response, compiler output, or API error may give the tooling enough information to modify its next request within seconds. Detailed diagnostic information exposed externally therefore provides more than troubleshooting value; it can accelerate experimentation during an attack.

#### Mitigations

- **Continuously Reduce the External Attack Surface**: Scan internet-facing applications and infrastructure for vulnerabilities, exposed administrative services, default configurations, and unnecessary services. Vulnerability programs should include custom applications, frameworks, libraries, and dependencies in addition to operating systems.
- **Assume the Workload Can Be Compromised**: Design applications so compromise of the front end provides access only to the systems required for that application’s function. Reduce application permissions and limit access to required databases, APIs, queues, storage accounts, and backend services.
- **Enforce Application-Tier Segmentation**: Segment internet-facing applications from identity infrastructure, management systems, and unrelated internal services. Restrict DMZ workloads from initiating unnecessary Kerberos, NTLM, LDAP, SMB, RDP, SSH, database, and administrative connections into internal networks.
- **Harden Database Runtime Privileges**: Application database accounts should not have broad administrative privileges. Restrict capabilities that allow a database engine or application identity to execute operating-system commands, write arbitrary files, modify server-wide settings, or cross the database-to-OS boundary unless the application requires them.
- **Reduce Credential Exposure in Workloads**: Review application configurations, environment variables, infrastructure-as-code, deployment scripts, CI/CD pipelines, and databases for embedded secrets. Compromise of one workload should not expose credentials for unrelated systems.
- **Limit Error Feedback to External Users**: Avoid returning detailed stack traces, compiler messages, SQL errors, internal paths, framework details, or other diagnostic information to unauthenticated users. Keep detailed troubleshooting information in internal logs.
- **Harden Network and Security Appliances**: Remove unnecessary management services from routers, firewalls, VPN appliances, and other infrastructure. Review configurations for unexpected accounts, scheduled jobs, startup scripts, configuration changes, and persistence mechanisms. Validate firmware integrity and vendor signatures where supported.
- **Harden Active Directory Certificate Services**: Review AD CS for certificate templates and enrollment paths that could allow an attacker to obtain authentication certificates or escalate privileges.
- Remove ENROLLEE\_SUPPLIES\_SUBJECT where it is not required, particularly on templates supporting client authentication.
- Restrict enrollment permissions to the identities that require them.
- Require certificate manager or CA approval for higher-risk enrollment scenarios where appropriate.
- Enable Extended Protection for Authentication on applicable CA web interfaces where supported.
- Monitor unusual certificate enrollment involving privileged users or unexpected requesting systems.
- **Reduce Credential Replay and Relay Opportunities**: Enable Windows Credential Guard where appropriate, use Protected Users for suitable privileged accounts, enforce SMB signing, and enforce LDAP signing and channel binding. Reduce or disable NTLM where operationally feasible and continue hardening against credential relay, Pass-the-Hash, Pass-the-Ticket, and related techniques.
- **Restrict Unnecessary Authentication From Exposed Workloads**: Internet-facing servers should only initiate Kerberos, NTLM, LDAP, SMB, WinRM, or RDP traffic to systems where those protocols are explicitly required.

### Layer 4: Harden Application Development

Harden legitimate enterprise functionality that attackers can reuse after gaining access.

A large portion of attacker activity relies on capabilities already present in the environment. Applications, authentication protocols, administrative services, scripting environments, messaging systems, deployment platforms, and business workflows may provide everything needed to continue an intrusion without introducing new malware. Automation makes these capabilities easier to discover and use quickly.

#### Why It Is Important

Internal business applications, scripts, and APIs are often customized to each organization without public documentation, and require a level of insider knowledge to understand exploitation opportunities. Automated LLM-powered offensive tooling has enabled attackers to enumerate and rapidly understand these internal applications and use them to their advantage.

Internal communication functionality is one example. A compromised application account may legitimately have access to a notification, messaging, or email API. Sending messages is expected behavior for that application. That same capability can be abused to send hundreds or thousands of phishing messages. Without recipient limits, rate limits, or behavioral monitoring, a standard business function can become a high-speed distribution mechanism.

#### Mitigations

- **Put Guardrails Around High-Impact Business APIs**: Applications capable of accessing sensitive data, retrieving credentials, sending email, notifications, creating users, modifying access, or performing other high-impact actions should have rate limits, recipient limits, transaction thresholds, and abuse controls appropriate to their function. Alert when an application operates materially outside its normal volume.
- **Inventory Legitimate Administrative Capabilities Before an Incident:** Security teams should know which platforms provide remote command execution, deployment, scripting, certificate issuance, identity synchronization, bulk messaging, and other high-impact functions. Those capabilities should have appropriate restrictions and monitoring in place before they are used during an intrusion.
- **Conduct Automated Application Testing and Threat Modelling**: All internal applications should have SAST and DAST scans conducted and findings resolved prior to deployment. Organizations can also leverage LLM-enabled tooling to automate the discovery, triage, reproduction, and patching of software vulnerabilities and potential attack paths. Organizations can also apply agentic source-code review and continuous AI-assisted vulnerability testing—whether a bespoke LLM harness or a managed capability such as [Google AI Threat Defense](https://cloud.google.com/security/ai-threat-defense)—to find, triage, and reproduce these attack paths before an attacker does.

### Layer 5: Detect Behavioral and Volumetric Change

Detect when identities, applications, workloads, and infrastructure begin operating outside their established patterns.

Many actions performed during an automated attack are legitimate operations when viewed individually. Detection therefore depends heavily on context: identity, source network, volume, timing, sequence, target resource, and historical activity.

#### Why It Is Important

A service principal accessing cloud storage is not necessarily suspicious. A service principal that normally accesses ten objects from one internal network and suddenly downloads thousands of objects from an unfamiliar hosting provider is a different situation.

Outbound activity provides similar context. Automated tooling on a compromised server may contact external webhook services to confirm execution or transfer results. It may also communicate with LLM platforms, temporary file-sharing infrastructure, tunneling services, or attacker-controlled systems.

A single HTTPS connection may be routine. A production server that historically communicates with a small set of known destinations and suddenly begins reaching several new external services deserves closer attention.

#### Mitigations and Detection Priorities

- **Baseline Behavior at the Identity and Workload Level**: Establish expected authentication sources, APIs, resources, activity volumes, and communication patterns for sensitive service principals, applications, workloads, and administrative identities.
- **Detect Changes in Authentication Origin**: Track the networks, ASNs, cloud regions, hosting providers, and other infrastructure used by privileged users and workload identities. Investigate successful authentication from infrastructure that falls outside the identity’s normal pattern.
- **Monitor Control-Plane Velocity**: Alert on unusual bursts of management API calls, permission testing, configuration changes, resource enumeration, credential retrieval, and other administrative activity. The timing and sequence of legitimate API calls can provide important context.
- **Baseline Data-Plane Activity**: Establish normal read, write, and object-access patterns for sensitive storage and data platforms. Detect sudden enumeration, unusual write-read-delete sequences, large increases in object access, or material changes in bytes transferred.
- **Build Detections Around Sequences**: Correlate related events across identity, control-plane, data-plane, endpoint, and network telemetry. A new authentication source followed by permission probing, storage enumeration, bulk downloads, and a connection to a previously unseen external service should be analyzed as one sequence.
- **Monitor East-West Behavior From Exposed Workloads**: Detect unexpected LDAP, Kerberos, NTLM, SMB, database, remote administration, and port-scanning activity originating from DMZ or internet-facing systems.
- **Control and Monitor Server Egress**: Restrict unnecessary outbound internet connectivity from production servers and route sensitive workloads through controlled egress paths where practical. Monitor previously unseen destinations, particularly webhook services, OAST infrastructure, tunneling platforms, public file-transfer services, and external AI platforms that are not required by the workload.
- **Preserve the Telemetry Needed to See the Behavior**: Collect and centralize interactive and non-interactive identity logs, service-principal authentication, cloud control-plane activity, sensitive storage data-plane logs, application administration logs, network flow, DNS, proxy telemetry, and endpoint activity. Establishing normal behavior depends on having enough historical data to compare against current activity.

### Google Security Operations (SecOps)

Google SecOps customers have access to these broad category rules and more under the Mandiant Frontline Threats and Mandiant Hunting Rules rule pack. The activity discussed in the blog post is detected in Google SecOps under the rule names:

- Suspicious Webhook.Site Interaction
- Suspicious Curl Invocation
- Cmd Launching Curl
- AWS Cloud Accounts Getcalleridentity
