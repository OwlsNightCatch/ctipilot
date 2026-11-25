---
title: Recent Trends and Tactics of Agentic AI Attacks
author: Tom Fakterman; Noa Dekel
url: https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/
hostname: paloaltonetworks.com
description: We tracked campaigns where attackers deployed autonomous AI agents to automate multi-platform intrusions, using standard tools while leaving distinct operational traces.
sitename: Unit 42
date: "2026-11-24"
fingerprint: "25b108c9c139b00b"
language: en
image: https://unit42.paloaltonetworks.com/wp-content/uploads/2026/11/AdobeStock_260323351-2.jpeg
pagetype: article
filedate: "2026-11-25"
---
## Executive Summary

Attackers are weaponizing autonomous AI agents in real-world campaigns, creating a risk that until recently has only been theoretical. Between July and September 2026, we identified and tracked more than 10 global campaigns in which different attackers deployed autonomous AI agents to enhance their attacks. These agentic AI attackers operated at machine speed, compressing the attack lifecycle from weeks or days into mere hours.

These campaigns targeted diverse sectors, including government, logistics, hospitality, manufacturing, agriculture and education. In every observed campaign the attackers gained their initial foothold through web shells that were deployed via vulnerable web applications.

The novelty of the observed agentic campaigns was not in their techniques, but in their speed and efficiency. Following the path of least resistance with familiar open-source tools and lightweight custom scripts, the AI-driven operators matched the tradecraft of proficient human attackers while operating at machine scale, at times executing hundreds of unique commands in just minutes.

However, using AI agents came at the expense of operational stealth. The agents left unmistakable behavioral fingerprints that revealed the involvement of non-human operators, including:

- Structured machine-readable output formats
- Adaptive exploit selection
- Iterative refinement
- Chain-of-thought reasoning comments that appeared in shell commands

This article details the real-world scenarios that we observed, organized by the tactical patterns that define how agentic AI is being weaponized today.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)  service can help identify and mitigate complex AI-enabled risks.

[Unit 42 Continuous Frontier AI Defense](https://www.paloaltonetworks.ca/unit42/prepare-for-emerging-risks/continuous-frontier-ai-defense) is an offensive security service designed to assist organizations with continuously discovering hidden and unknown exposures in dynamic environments, validate real-world exploitability across attack paths through agentic testing and expert analysis, and provide prioritized remediation and virtual patching guidance to accelerate risk mitigation.

Organizations can access tailored adversary intelligence, direct analyst consultations, and specialized exposure tracking through [Unit 42 Threat Intel Services](https://www.paloaltonetworks.com/unit42/threat-intelligence) and its [Deep and Dark Web Service](https://www.paloaltonetworks.com/resources/datasheets/unit-42-deep-and-dark-web-service).

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

| **Related Unit 42 Topics** | **[Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/), [LLM](https://unit42.paloaltonetworks.com/tag/llm/), [Web shells](https://unit42.paloaltonetworks.com/tag/web-shells/)** | 

## Background of Agentic Attacks

### What Makes an Attack Agentic?

An agentic AI attacker is an autonomous AI system — usually a large language model (LLM) with tool-calling capabilities — that independently plans, executes and adapts attack sequences without continuous human guidance.remote

Unlike chatbots that respond to individual prompts, agentic AI systems operate in a [loop](https://www.copado.com/resources/blog/an-ooda-loop-diagram-approach-to-cloud-security): they observe their environment, reason about what to do next, take action and then observe the results to inform their next step.

### How Agentic Attackers Are Changing the Threat Landscape

The weaponization of agentic AI represents an increased threat to security for several reasons:

- **Speed and scale:** An agentic AI attacker operates at machine speed. In the campaigns we observed, AI agents executed hundreds of unique commands within minutes.
- **Lowered barrier to entry:** Attackers can simply provide high-level guidance while the AI agent automates intricate technical phases. This includes complex actions such as compiling kernel exploits, navigating cross-platform lateral movement and systematically compromising cloud infrastructure.
- **Adaptive reasoning:** Unlike script-based attacks that fail when they encounter unexpected conditions, agentic AI attackers employ reasoning to try alternative approaches when failures occur. We observed agents attempting five different privilege escalation techniques in sequence when earlier ones failed, compiling custom exploit code on-target when pre-built binaries didn’t work.
- **Cross-domain fluency:** A single agentic AI attacker can operate across Linux, Windows, various cloud platforms, web applications, databases and network infrastructures. This breadth of expertise would typically require a team of specialists.
- **New challenges in threat attribution:** Because AI agents generate unique, dynamic payloads on the fly without distinct behavioral fingerprints, attributing attacks to specific threat actors is increasingly difficult.

## The Agentic AI Attack Cycle

Our analysis of more than 10 campaigns observed between July and September 2026 indicates that the most successful intrusions consistently combined human oversight with AI agents in a unified operational model:

1. **Human sets the objective:** The human operator identifies a target and provides initial access — typically a web shell on a vulnerable web application. In some cases, the human operator executes the first assessment of the target.
2. **AI agent takes over:** The AI agent autonomously performs further reconnaissance, credential harvesting, privilege escalation and lateral movement.
3. **AI agent reports back:** The AI agent structures its findings using machine-readable output formatting and periodically checks in with orchestration APIs.
4. **Human makes strategic decisions:** The human operator reviews the AI agent’s findings and directs high-level strategy. This may include instructing the agent to target the payment system or establish persistence.
5. **AI agent executes:** The AI agent carries out the human’s strategic directives with tactical autonomy.

Figure 1 shows the attack lifecycle.

## Common Characteristics of Agentic AI Attacks

A comparative analysis of AI-assisted campaigns that we observed revealed several defining operational markers. These characteristics are strong indicators of an agentic attacker rather than a human operator:

- The speed of the attack
- Use of section headers
- Overly descriptive comments

### Command Execution Rate

One of the most pronounced characteristics of an attack performed by an AI operator is its ability to rapidly execute a high volume of commands.

In one attack we investigated, the AI attacker was active for only 140 minutes across two days. In this brief period of time, the attacker progressed from initial access via web shell, to performing reconnaissance and enumerating the victim’s cloud environment, website and databases. Throughout the attack, the AI agent executed about 800 unique commands at an inhuman pace.

In another campaign conducted over a 12-day period, the attacker executed more than 8,000 unique commands.

To understand the difference in operational speed between human and AI operators, we checked the median inter-command gap between two phases of the observed attacks. In a subset of analyzed attacks, the first phase featured manual reconnaissance and connectivity checks by human operators, with a median inter-command gap of 23.9 seconds.

In the second phase of the attack, the operation was passed to an agentic AI attacker. Once an AI operator took command, the median inter-command gap dropped to 1.4 seconds. Figure 2 shows the median inter-command gap difference between the two phases.

### Headers and Delimiters

In every campaign that we observed, AI operators used section headers in shell commands and scripts, such as ===\[Title\]===. These headers help AI parse the results of the executed commands faster. In human-operated attacks such headers rarely appear, and are usually only seen when an attacker uses a pre-coded script.

Figure 3 shows an example of multiple commands executed by an AI operator, with section headers that separate the output of the commands.

### Chain of Thought Comments

A common indicator of agentic AI-generated code is using “reasoning comments” embedded within technical scripts. In more than half of the observed campaigns, we identified multiple scripts containing conversational, step-by-step reasoning notes. These notes explained the logic of the AI operator’s script execution, as Figure 4 shows.

## Operational Trends of Agentic AI Attacks in the Wild

In addition to the behavioral fingerprints distinguishing AI operators from human attackers, our investigation revealed consistent operational trends. Despite targeting diverse organizations, the agentic AI attackers followed a similar playbook:

- Moving across platforms
- Relying heavily on web shells for initial foothold and persistent C2
- Adapting strategy in real time
- Demonstrating explicit awareness of deployed security products

The following sections detail the trends that we observed across the different campaigns that we investigated.

### Multi-Platform Attacks

Many observed attacks began on Linux web servers, but quickly spread to other platforms. Each campaign aimed to expand as widely as possible across the targeted network, regardless of platform or technology. This is an example of how AI agents continue to lower the barrier of entry for less-experienced operators. While a human attacker might take years to master each operating system (OS), agentic AI can seamlessly move between them and even compromise cloud infrastructure.

#### Cloud Platform Abuse

Our investigation found agentic AI attackers misusing cloud services across three major cloud providers. We assess that the exploitation was adaptive — the agent discovered the cloud platform and pivoted to platform-specific techniques without any pre-configuration.

In one campaign targeting a US-based hospitality and gaming company, upon discovering an AWS EC2 instance role, the AI agent attempted to steal credentials via the Instance Metadata Service ([IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)). When IMDSv1 was blocked, the agent immediately adapted and switched to IMDSv2 token acquisition, succeeding after multiple iterative attempts.

Once authenticated, the AI agent enumerated 20 AWS services across eight regions, exfiltrating information about the victim’s buckets, email service and secret management. The ability to enumerate is a basic part of bucket functionality, but in this case it was misused for malicious purposes. Additionally, upon discovering S3 bucket names in the configuration files, the agent immediately targeted payment and financial data paths.

This targeted pivot suggests that the human operator instructed the agent to prioritize high-value financial assets. Cortex XDR detected the agentic AI attacker spawning multiple processes enumerating the victim’s payment resources, as Figure 5 shows.

We assess that a human operator instructed the AI agent only to collect information in preparation for a more aggressive future takeover, as no harmful actions were taken. We observed the AI agent testing its ability to write into production cloud environments, immediately deleting test files and examining the bucket’s policy and Access Control List ([ACL](https://docs.cloud.google.com/storage/docs/access-control/lists)) to see if the bucket was publicly accessible or had exploitable policies.

#### Multi-OS Compromise

The AI agents also demonstrated an ability to operate across multiple operating systems within a single attack chain. In one observed campaign, an AI agent initially compromised a Linux server via a PHP web shell, and was able to pivot to a separate Windows IIS server with stolen SMB credentials. The rate of the lateral movement was incredibly fast: Within two minutes of identifying the Windows IIS server, the agent began deploying ASPX web shells over SMB. Over the next 26 minutes it pushed webshells to more than 40 locations across the server, rotating between five different webshell variants and uploading custom web.config files to enable script execution.

### Adaptive and Strategic Attacks

One of the features that makes agentic AI attackers more powerful than older models and automations is an agent’s ability to adapt its strategy based on what it discovers.

In one campaign, we observed the AI agent demonstrate a particularly adaptive strategy: After exploiting the initial victim, the agent autonomously identified and attacked the victim’s IT vendor and sister organizations.

After gaining an initial foothold on the server, the AI agent uncovered the credentials for the vendor’s self-managed GitLab instance on the victim’s compromised web server. Pivoting immediately, the agent probed the vendor’s site, mapped infrastructure via WHOIS and tried to brute force access to the vendor’s GitLab instance, attempting a supply-chain attack across the vendor’s client base.

During a brute-force attempt, the agent used real names of marketing team members. This targeting suggests that the AI agent may have performed additional open-source intelligence (OSINT) gathering to identify specific employees. No vulnerability in GitLab was exploited; the credentials were exposed through the compromised third-party web server.

When the AI agent read the server’s NGINX virtual-host configurations, it identified over a dozen related sister-company entities on the same internal network. It then systematically probed each entity:

- Harvesting CSRF tokens from login portals
- Attempting credential reuse with passwords stolen from the primary target
- Launching four iterative SQL injection scripts against the parent company’s admin panel

The agentic attacker takeover flow is shown in Figure 6.

Beyond strategic thinking, agentic AI attackers can escalate and tailor their attacks rapidly based on new information. This adaptiveness includes:

- Quickly creating custom payloads
- Pivoting to new attack vectors
- Reacting swiftly to tool and script failures

In another case, we observed an agentic AI attacker execute a port sweep using a script named scan.sh. Just 21 seconds after the port sweep, the agent ran a second script named scan2.sh. The second script contained tailored recon commands that matched the exact technologies discovered on each port by the first script. Figure 7 shows the content of both scripts.

### Web Shell-Based Intrusions

Across all analyzed campaigns, initial network access was achieved by deploying web shells on internet-facing web servers. This trend reflects a preference among human operators for leveraging web shells when orchestrating agentic AI operations. Web shells provide a straightforward approach to establishing initial footholds at scale during opportunistic attacks.

As an alternative to a web shell, an attacker could establish a foothold on a victim’s machine using a reverse shell, a remote access Trojan (RAT) or remote monitoring and management (RMM) software. However, those methods typically require more operational effort and resources to create and maintain.

In some cases, we observed that instead of relying on compiled implants to send commands, the AI agents independently dropped and utilized web shells. This provided the agents with ongoing code execution and persistence.

#### Dynamic Command Encoding

Given the extensive use of web shells as an initial foothold, secondary payloads were routinely obfuscated using Base64 encoding — a standard technique in web shell-based intrusions. Any attacker piping multi-line code through a web shell’s sh -c interface will encode it, to avoid breaking the code on shell metacharacters, quotes and special symbols. What distinguishes agentic AI attackers from human operators is not the encoding itself, but the volume, uniqueness and variety of encoded payloads they produce.

In a typical human-operated web shell intrusion, an attacker might deliver a handful of pre-written tools via Base64, which are reusable and often appear across multiple victims with identical hashes. However, in the agentic campaigns we investigated, the pattern was different: AI agents delivered 40-100 unique Base64-encoded payloads in a single attack session, each one tailored for the specific target’s assets. No two payloads were identical across victims and no payload matched any known tool signature.

### Evasion Techniques and Security Awareness

While the high volume and fast rate of command execution make agentic AI attackers “noisy,” they demonstrated explicit awareness of deployed security products. Apart from attempting to evade sensors, agentic attackers are now actively probing their configuration, understanding the enforcement boundaries of detection tools and attempting to debug why a security tool blocked an action. This level of security-aware behavior was observed across multiple campaigns and represents a significant escalation from automated attacks that we have observed in the past.

#### EDR Path Exclusion

In one observed campaign, the AI agent deliberately excluded endpoint detection and response (EDR) directories from file discovery commands. The agent executed the same find command on six compromised endpoints, excluding three different security vendors, as seen in Figure 8.

Notably, the same agent also ran a separate security tool enumeration command, checking for the presence of 16 different security scanners (nmap, nessus, openvas, nikto, masscan, nuclei, lynis and others), mapping the defensive landscape before proceeding with its attack.

#### Direct EDR Reconnaissance

Our investigation revealed multiple cases where AI agents transitioned from simple evasion to active reconnaissance of installed security stacks. These agents methodically interrogated endpoint monitoring solutions to map their operational boundaries, as demonstrated in the following observed behaviors:

- The AI agent attempted to enumerate and exfiltrate the endpoint’s security product local directory, specifically hunting for sensitive configuration data and stored credentials.
- In a display of iterative debugging, the agent applied strace to the Microsoft Defender for Endpoint process (wdavdaemon), analyzing kernel-level system calls to reverse-engineer how the daemon monitors environment activity.

### The Absence of Custom Tools and Malware

One of the most interesting outcomes from our campaign analysis was what we didn’t find. Although in the course of our investigation we extracted hundreds of unique script payloads, we did not recover a single compiled backdoor, custom C2 framework, DLL implant or shellcode loader.

In most cases, the AI agent’s entire custom arsenal consisted of relatively simple, single-use scripts like PHP web shells, PowerShell WMI backdoors or Python credential harvesters. This is a departure from the usual tooling profile of advanced attackers, who typically invest in compiled, persistent implants designed for long-term access.

Unlike these attackers, the observed agentic AI attackers generated purpose-built scripts on the fly, tailored to whatever they discovered at the same moment. Thus, instead of a single “one-size-fits-all” implant, the attacker’s progress within the victim’s network was achieved through smaller, single-step scripts. Cortex XDR detection demonstrates how the agentic AI attacker could generate and deploy different script types under the same process chain, as Figure 9 shows.

### Reliance on Open-Source Tools and Exploits

Although we observed many cases of agentic AI attackers generating custom code on the fly, campaigns routinely incorporated existing, open-source tools *before* resorting to custom coding.

One recurring example is the [Copy Fail](https://github.com/xeloxa/copyfail-exploit) exploit (CVE-2026-31431), a Linux kernel vulnerability that appeared across several organizations targeted in the observed campaigns. In three separate cases, the AI agent attempted to directly download the exploit from external sources — either via the exploit’s official GitHub repo, or from the exploit’s website.

In a different attack sequence, the AI agent first uploaded a pre-compiled [PwnKit](https://medium.com/@ajithcrajendran/pwnkit-cve-2021-4034-f9feb312715c) binary and tried multiple invocation methods. When that binary failed, the agent fetched a pre-compiled CVE-2024-1086 [privilege escalation exploit](https://github.com/notselwyn/cve-2024-1086). Only after exhausting both public binaries did the AI agent begin writing custom C source code on the target, iterating through compilers and linkers. When the compilation attempt also failed, the agent tried to rewrite the exploit logic in Python.

In another case that combined open-source tools with custom payloads, the AI agent followed a similar, but more layered approach. After failing to execute a precompiled CopyFail for local privilege escalation, it compiled the PwnKit exploit from source directly on the target. Subsequently, for network reconnaissance, the agent wrote a custom C network probe tool (charon\_lite.c), and built custom Python spray scripts on top of it using the open-source paramiko library.

## Operator Fingerprints in AI Agent-Enhanced Attacks

With the rise of AI agent-enhanced operations, fingerprinting operations with static payload signatures and behavioral tracking is becoming more difficult. We suggest alternative methods of fingerprinting agentic AI campaigns, relying on human intention, operational mishaps and infrastructure correlation.

During our research, we did not encounter behavioral markers that link agentic activity to specific LLM models or orchestration frameworks. While attack patterns like Base64 payload delivery and systematic reconnaissance commands are consistent, their implementations are too diverse to provide a unique behavioral fingerprint. Since AI-generated code is custom built for each target, signature-based attribution is largely ineffective.

However, it was clear that a human operator was behind these agentic infrastructures. A human decides which target to attack, when to launch the operation and which assets to compromise. Beyond operational intent, the human operators and their AI agents continue to leave behind key artifacts that provide crucial attribution leads:

- **Infrastructure**
  - **Hard-coded C2 addresses in payloads:** In some cases, AI agents embed attacker-controlled IP addresses and network ranges directly into generated malware payloads and web shells. In one campaign, the C2 server 204.194.54\[.\]240 appeared in both PowerShell download cradles and cURL probes.
  - **Agent orchestration infrastructure:** Pivoting on the hard-coded 204.194.54\[.\]240 C2 server revealed that it was also hosting an instance of [CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI/blob/main/README.md), an AI-native offensive security platform. The presence of CyberStrikeAI allows us to pinpoint the use of a specific orchestration platform. This is the kind of infrastructure-level attribution that behavioral analysis alone cannot provide.
  - **Cross-campaign infrastructure overlap:** The malicious use of 204.194.54\[.\]240 is not an isolated incident. Recent threat research by [ReliaQuest](https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/) documented the same IP acting as a staging and reconnaissance node in a separate agent-driven attack. Their investigation also noted the presence of the CyberStrikeAI login page and open directories hosting privilege escalation tools on this address, corroborating the use of this specific infrastructure across multiple agentic campaigns.
- **Toolset**
  - **Accidental file paths from the attacker’s environment:** In one campaign, we observed the accidental pasting of a local file path: /home/kali/exploitmasteryai/targets/warranty/shell5.php. The exploitmasteryai path fragment is the only concrete indicator of the AI attack framework’s identity across the entire campaign, and it was exposed purely through an operational security failure.
  - **Linguistic artifacts leakage in code comments:** Attackers interact with AI agents in a variety of languages, which results in code comments generated in those languages. Defenders can treat these as artifacts like native language comments in human-operated campaigns. In one example we encountered, the attackers used two identical versions of a WMI backdoor — one that contained comments in Chinese, and a newer version that was specified to be English only. Figure 10 shows both versions of the WMI backdoor.

## Conclusion

Agentic AI attacks are no longer a theoretical concern, but an active threat targeting a broad range of industries. The campaigns we observed were aimed at government, logistics, manufacturing, hospitality, education and agriculture sectors. All of the attacks used the same method: A human operator points an AI agent at a vulnerable web application, and the agent takes it from there.

What we observed is not a new class of attack sophistication. The techniques themselves are the same ones that a skilled human attacker would employ. The agents follow well-established attack flows, rely on known CVEs and use the same open-source tools that human operators have used for years.

Where agentic AI attacks fundamentally differ is in their speed, volume and their ability to quickly and efficiently adapt to different types of platforms and operating systems. These feats allow agentic attackers to fully compromise a network in mere hours, where even an experienced attacker would take days or weeks.

However, in the attacks we witnessed, agentic attackers left behind unmistakable fingerprints that a human operator is unlikely to produce. These indications included chain-of-thought comments and specific content delimiters. Hunting for these signs could help defenders recognize and prevent this threat.

Ultimately, defending against agentic AI attacks requires AI-powered defenses, as these types of attacks are diverse, and require a solution that can identify patterns regardless of the specific tools, techniques or platforms involved.

### GitLab Hardening

Organizations running self-managed source code platforms should:

- Enforce multi-factor authentication
- Enable sign-in rate limiting
- Restrict access by IP where possible
- Keep instances up to date

GitLab publishes [specific hardening recommendations](https://docs.gitlab.com/security/hardening_application_recommendations/), and provides [application hardening guidance](https://docs.gitlab.com/security/hardening/) for self-managed deployments.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

- [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering), [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) and [Advanced IP Defense](https://www.paloaltonetworks.com/network-security/advanced-ip-defense) are designed to identify known domains, IPs and URLs associated with this activity as malicious.
- [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention) security subscription can help block CVE-2026-31431 with best practices via the following Threat Prevention signature [97176](https://threatvault.paloaltonetworks.com/?query=97176).
- [Cortex Agentic Endpoint Security](https://www.koi.ai/product/endpoint) is designed to help discover every AI artifact and AI agents’ activity across the agentic endpoint, assess its risk, enforce prevention and runtime controls, and remediate.
- [Idira Privileged Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1) is designed to unify privileged access across human, machine, and agentic identities to secure cloud access across multi-cloud environments. Building on proven PAM, it delivers centralized secrets management alongside modern controls like Just-in-Time access and Zero Standing Privileges. This enforces consistent least-privilege security across on-premises, cloud, and SaaS targets.
- [Idira Endpoint Privilege Manager (EPM)](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm) can help enable enterprises to reduce risk, satisfy compliance, and streamline operations. It helps implement least privilege via policy-driven elevation and removal of standing admin rights, and blocks risky actions, such as execution of unvetted applications and access to memory of other processes, while providing audit-ready evidence and unified identity governance.
- [Idira Secrets Manager](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/resources/_topnav/cc_home.htm) is designed to help secure and automate API keys and webhook tokens just-in-time to eliminate hardcoded credentials and prevent exfiltration.

#### Cortex XDR and XSIAM

In the era of agentic AI attackers, it is crucial that security vendors and defenders embrace a proactive approach and start fighting AI with AI. Throughout the investigation, we used several AI-enhanced solutions to track, investigate and prevent this threat.

[Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR)’s AI engine analyzes billions of daily user, system and security events to automatically generate precise, high-fidelity prevention rules. By operating at machine speed and scale, it helps eliminate manual engineering bottlenecks and neutralize threats before they gain a foothold. Figure 11 shows Cortex XDR Console flagging AI-assisted malicious activity using AI-generated detection.

[Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) are designed to help prevent the threats described in this article by employing an advanced, on-device Small Language Model (SLM) for real-time semantic code comprehension.

Cyberattacks are increasingly generated by AI, meaning that programming languages and basic syntax are no longer a boundary for threat actors, who can now easily automate novel payloads. To combat these attacks, Cortex XDR’s first market-ready, on-device SLM was trained on hundreds of millions of samples, covering popular scripting languages, live malicious packages and frontier AI-generated cyberattacks.

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)  service can help identify and mitigate complex AI-enabled risks.

[Unit 42 Continuous Frontier AI Defense](https://www.paloaltonetworks.ca/unit42/prepare-for-emerging-risks/continuous-frontier-ai-defense) is an offensive security service designed to assist organizations with continuously discovering hidden and unknown exposures in dynamic environments, validate real-world exploitability across attack paths through agentic testing and expert analysis, and provide prioritized remediation and virtual patching guidance to accelerate risk mitigation.

Organizations can access tailored adversary intelligence, direct analyst consultations, and specialized exposure tracking through [Unit 42 Threat Intel Services](https://www.paloaltonetworks.com/unit42/threat-intelligence) and its [Deep and Dark Web Service](https://www.paloaltonetworks.com/resources/datasheets/unit-42-deep-and-dark-web-service).

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

- North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
- UK: +44.20.3743.3660
- Europe and Middle East: +31.20.299.3130
- Asia: +65.6983.8730
- Japan: +81.50.1790.0200
- Australia: +61.2.4062.7950
- India: 000 800 050 45107

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Indicators of Compromise

- 150.242.254\[.\]199 — Reverse shell target
- 204.194.54\[.\]240 — C2 and payload staging
- 206.123.152\[.\]217 — Reverse shell C2
- 38.253.224\[.\]12 — GSocket and SSH tunnel relay
- webhook\[.\]site/72f421ea-5576-4a4a-8c55-a2a79c19c8b8 — C2 beacon
- pastebin\[.\]com/raw/swqSMxYs — Web shell download
