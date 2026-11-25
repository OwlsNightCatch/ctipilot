---
title: AI-Assisted Cyber Attacks Trigger Unauthorized Payments at Indian Banks and Fintech Firms
author: The Hacker News
url: https://thehackernews.com/2026/11/ai-assisted-cyberattacks-trigger.html
hostname: thehackernews.com
description: CERT-In warns AI-assisted attacks are abusing trusted business workflows to trigger unauthorized payments at Indian financial and technology firms.
sitename: The Hacker News
date: "2026-11-23"
categories: ['Article']
tags: ['AI Agents', 'artificial intelligence', 'banking security', 'cyber attacks', 'Cybercrime', 'Financial Security']
fingerprint: a5f098d10817dba1
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijDifo0ih-I06DQJbgdnt34Xg1qWdMibKByoJO-4vqa50M4yN0Lwu4fDe88GBtoiKHMJnRDYM0WXvYDEMyCWFHEbedl0wzwKI7juH9Q9xs3osQjZK0xPygeuGm0bm6jgpWPa7bca1EuZfTQiLxn-X3aNaAhbchhvemZrCqslieabzsGmz4ezqhrKuYhDyk/s1700-nu-rw-lo-l85-e365/ai-india.jpg
pagetype: article
filedate: "2026-11-25"
---
The Indian Computer Emergency Response Team (CERT-In) has warned that threat actors are carrying out artificial intelligence (AI)-assisted cyber attacks targeting information and communication technology (ICT) assets in the country.

This unsanctioned activity has resulted in unauthorized financial transactions at banking and financial services entities, as well as technology service providers supporting government-linked payments and platforms handling vendor or partner payouts.

"In the observed incidents, attackers targeted business records and approval processes to carry out unauthorized transactions through otherwise legitimate systems," CERT-In [said](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0062) in an advisory last week.

The incidents have been found to include the following methods -

- Abuse of business applications and service provider-operated workflows, as opposed to direct exploitation of payment-related APIs.
- Modification of business records or approval relationships, followed by the use of legitimate payment processes.
- Use of trusted systems and established approval procedures to process unauthorized transactions without raising any alert.
- Exploitation of security blind spots in independent verification, reconciliation, and review of changes to business records.

CERT-In did not reveal how much money had been improperly paid out, or by whom. The activity has not been attributed to any specific threat actor.

The agency also said that separate threat-hunting has uncovered the use of AI-driven agentic offensive frameworks (AOFS) across enterprise, technology, government, academic, and research sectors to conduct the following actions -

- Automated reconnaissance to identify exposed systems, services, and potential attack paths.
- Rapid generation and modification of exploits for known vulnerabilities, including by analyzing software patches and related technical information.
- Using a cluster of AI agents to undertake intrusion tasks, such as reconnaissance and privilege discovery, in parallel.
- Modifying scripts, requests, and attack methods in response to errors, blocked attempts, or information returned by targeted systems.
- Using valid credentials, legitimate administrative functions, trust relationships, and external infrastructure to burrow deeper into target networks.

"Organizations should review the security of business applications, critical records, user identities and third-party interfaces," CERT-In said. "Existing monitoring and incident-response arrangements should also account for the risks arising from misuse of trusted business processes and automated intrusion activity."

The development comes as Indian entities have [witnessed](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0046) a spate of AI-assisted cyber attacks on financial entities, even as the national nodal agency disclosed that AI agents under research and evaluation "exceeded their task authorization and made unauthorized access" to ICT assets.

"In the financially motivated campaign against Indian entities, agentic tooling compressed the time between initial access and final impact from days to a few hours," CERT-In [said](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0049). "In addition, the campaign highlighted that multi-agent operations run in parallel for hours to days to achieve the attacker goals, consistent with the documented multi-agent capability of these tools."


Earlier this month, the agency also warned that a threat group named [Crafty Falcon](https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html) is behind a wave of AI-driven attacks on financial firms and has used offensive penetration testing tools like ARTEX, PentAGI, CAIRN, and CyberStrikeAI to automate the intrusions at machine speed.

According to the Indian Cybercrime Coordination Centre (I4C), the attacks have targeted banks, non-banking financial companies, and fintech companies, leading to multi-crore (equivalent to 10 million) unauthorized transactions through fund disbursement systems and APIs.

"Perpetrators exploit unpatched software or misconfigured internet-exposed servers / IT systems to compromise the infrastructure," I4C [said](https://i4c.mha.gov.in/theme/resources/advisories/AI-Assisted-Cyber-Attack-on-Banks-NBFCs.pdf). "Hackers then target automated fund disbursement systems or special interfaces (APIs) used for payments and fund transfers.  The money is sent to 'mule' accounts (accounts used by criminals) across different banks and then quickly moved or withdrawn through IMPS/NEFT."

India's central bank, the Reserve Bank of India, has also alerted of rising cyber attacks on financial infrastructure, urging banks to provide details of their ability to stay ahead of AI-related threats, Reuters [reported](https://www.reuters.com/legal/litigation/indias-rbi-tightens-cyber-checks-lenders-after-spate-hacks-2026-10-30/) late last month.

### The Surge in AI Attacks

The advisories also come at a time when [organizations around the world](https://thehackernews.com/2026/10/cyberstrikeai-uses-44-ai-agents-to.html) are being [targeted](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html) using AI tools, giving [attackers](https://hunt.io/blog/artex-south-korea-bank-infrastructure) a way to "execute multi-stage intrusions at greater operational velocity." Last week, the European Commission [confirmed](https://audiovisual.ec.europa.eu/en/media/video/I-298222) that [attackers](https://www.politico.eu/newsletter/brussels-playbook/cyberattack-hits-the-commission/) armed with [ARTEX](https://www.wired.com/story/artex-ai-hacking-tools/) broke into its HR, medical reimbursement, and translation systems. The first signs of the attack were detected on October 22, 2026.

ARTEX has also been implicated in a recent supply chain attack on IT management software company [ConnectWise](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html) and [Barracuda](https://trust.barracuda.com/security/barracuda-xdr-integration-credentials), with the latter revealing that a financially motivated criminal weaponized an exposed valid cloud access key provided to a third-party vendor to map its reach, repurpose discovered secrets to access more systems and look for seed phrases, and exfiltrate more credentials and secrets.

"In all, the attacker touched about 10 cloud accounts in roughly 44 hours \[between November 1 and 2\]. The work was methodical and tireless," Barracuda [said](https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion). "The probe names, the other indicators we collected, the order in which the attacker worked through our systems, and its built-in routines for hunting credentials and wallets all match ARTEX."

Frameworks like ARTEX manage a collection of sub-agents to plan, execute, and adapt tactics across multiple kill chain stages, including reconnaissance and scanning, initial access, persistence and privilege escalation, internal reconnaissance, lateral movement, and data exfiltration.

They can translate tactical goals described in natural language into machine commands that are executed by specialized AI agents. It integrates with various external LLMs, including Anthropic Claude, OpenAI GPT, DeepSeek, SpaceXAI Grok, Zhipu GLM, and Kimi.

"ARTEX significantly reduces the time required to chain attack techniques, with some intrusions progressing from initial targeting to privileged access in under three hours," the U.S. Federal Bureau of Investigation (FBI) [said](https://www.ic3.gov/CSA/2026/261113.pdf) in an alert this month.

"The framework enables threat actors with minimal technical expertise to conduct complex, multi-target operations simultaneously, fundamentally accelerating attack velocity and expanding operational scale."

Check Point, in a report published this month, said it uncovered more than 1,800 publicly exposed instances for ARTEX, with attackers leveraging the tool to conduct opportunistic, financially-motivated cybercrime.

"Analysis of agent conversations revealed that these systems work almost fully autonomously, once the initial goal is set: most actors barely interacted with their agent fleets and mostly asked for progress or directed the agents to a new target," the company [said](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/).

Data security firm Cohesity said threat actors using ARTEX are gaining access to systems that receive less security attention, such as partner and supplier portals, mobile backends, employee and sales support applications, legacy services, third-party integrations, and applications built by individual business units.

"In a research network we operate, a threat actor linked to Rhysida used an AI framework to rewrite tools in response to obstacles, often within minutes, and more than 150 versions of a single script reached a domain controller within a day," it [said](https://www.cohesity.com/blogs/artex-is-evidence-ai-is-compressing-the-cyberattack-timeline/).

In a report published last week, Google's Mandiant and Threat Intelligence Group (GTIG) identified what it described as the first observed instance of attackers using an autonomous AI framework with no human in the loop to turn security patches into exploits.

The AI framework, called "exploit\_agent," integrates with multiple frontier and local large language models (LLMs). It's designed to discover software vulnerabilities and execute exploits without human intervention. The attacker, suspected to be Russian-speaking, is said to have leveraged the framework to target French websites associated with the media and entertainment industries, as well as the education sector.

"The framework is set up to conduct continuous differential analysis of popular web application software," Mandiant and GTIG [said](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold). "It compares code before and after patch announcements, analyzes findings to identify potential vulnerabilities, drafts exploits, and automatically executes them without human intervention."

Some of the other notable incidents where AI agents and models do the legwork are listed below -

- Use of CAIRN in intrusion activity against targets, including in the aerospace sector in the U.S.
- Embedding LLMs into influence operation workflows to produce synthetic media, create convincing virtual personas, and generate and publish content.
- Use of Google's Gemini API, along with tools from multiple AI providers, to build an end-to-end influence-as-a-service (SaaS) platform designed to target public sentiment on regional political topics, specifically across Europe and the Middle East.
- Use of LLMs by a China-linked contractor called Leaky Castle to analyze, translate, and understand exfiltrated data
- Abuse of a frontier model's file-hosting infrastructure by a China-nexus threat actor to stage lure archives and exfiltrate stolen data, and a backend API to exfiltrate stolen intranet documents.
- Use of LLMs by North Korean threat actors to generate resumes and prepare for job interviews at Western organizations.
- Creation of fraudulent recruiter profiles on professional networking platforms by a suspected North Korean hacking group called [Midnight Neptune](https://thehackernews.com/2026/11/trigram-campaign-impersonates-about-50.html) (previously UNC1069) in attacks aimed at cryptocurrency entities in North America and Europe using job- and ClickFix-themed lures. These personas have been found to direct targets to fraudulent meeting platforms, which are used to run diagnostic fix scripts via ClickFix. "Following initial compromise, the actor pivoted into internal code repositories to execute a supply chain vector internal to the organization: modifying .claude/settings.json configuration files so that when users started up Claude Code, it would automatically trigger the download of the SOMBERMEME backdoor," Google said.
- Use of CyberStrikeAI ("43.240.29\[.\]11") between September 30 and October 16, 2026, to validate stolen AWS credentials, harvest secrets from Secrets Manager, pull EC2 user data, decrypt an SSM parameter, and send a remote command. "The audit log does not show what the command was or whether it succeeded," Elastic Security Labs [said](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion).
- Use of Hermes, in combination with DeepSeek, by a threat actor called [Silent Lynx](https://thehackernews.com/2026/10/silent-lynx-exploits-winrar-flaw-to.html) in [cyber espionage operations](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server) targeting Central Asian governments and critical infrastructure from April to October 2026 to assist with reconnaissance, data collection, and erasing traces of activity from compromised systems.
- Use of ARTEX to [exploit a vulnerable custom PHP upload function](https://labs.eye.security/how-we-defended-against-an-ai-driven-attack/) and stage a web shell, and use it to access secrets and API keys, and ultimately compromise a company's development pipeline to alter a Git repository and deploy an attacker-controlled Kubernetes pod.
- Use of an AI coding assistant to [revive a stalled attack](https://www.security.com/threat-intelligence/ai-assisted-attack-us-retailer) at a U.S. retail organization and come up with ways to bypass defenses and steal credentials after their commands were blocked by security software in late September 2026. The attack is assessed to be financially motivated, based on the threat actor's scans for passwords in point-of-sale scripts and an IP address overlap with a [prior campaign](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) targeting online retailers.
- Use of CAIRN by a Chinese-speaking attacker between August and September 2026 and pairing it with GLM and DeepSeek models to autonomously conduct 25 operations against at least 19 organizations. The attacks, attributed to CL-STA-1238, have targeted advanced semiconductor manufacturing, U.S. defense policy, and civil society sectors, achieving unauthorized access or data retrieval at 10 of the entities, including valid credentials, personal data, military and government identities, and the creation of persistent administrator accounts in a production system. "CAIRN coordinates its activities through a shared 'blackboard," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/). "Agents read the blackboard and write their findings back as a fact-intent graph, while human operators can inject 'hints' at any time to help guide the operations if needed. Confirmed findings accumulate as immutable facts, and the agent queues its next actions as intents."
- Use of ARTEX to [gain access to a compromised account-level API token](https://blog.cloudflare.com/adapting-to-ai-penetration-testing-orchestrators/) previously used for CI/CD with no IP restrictions or rate limiting. "Attackers repeatedly compromised static, non-expiring tokens running inside CI/CD pipelines, which granted broad, cross-environment access across the organization's hyperscaler infrastructure," Cloudflare said. "LLM frameworks greatly expand the likelihood of a client’s API key being laterally leveraged to take over other tenant environments."
- Use of ARTEX to generate [deepfake videos to trick identity verification checks](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/) at two cryptocurrency exchanges and steal AI credentials at "industrial scale" to gain free access to models. Amazon has characterized the second campaign as a "self-sustaining operation in which stolen keys paid for the LLM inference powering further credential hunting." Targets include LLM gateways and proxy platforms such as One API, New API, Veloera, Sub2API, and LiteLLM, and AI application builders such as Dify, FastGPT, Langflow (CVE-2025-3248), RAGFlow (CVE-2026-28797), Open WebUI, LobeChat, and Ollama.
- Use of CAIRN by a suspected Chinese-nexus threat actor to [discover a zero-day vulnerability](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/) ([GHSA-qc22-rmgc-vg94](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94)) in MONAI Label, a medical imaging application, and use it to gain complete control of a server within 11 minutes. The activity was detected in September 2026.

"An agent that discovers and exploits a zero-day in minutes completes its activity faster than many security operations centers can manually triage an alert," CJ Moses, CISO of Amazon Integrated Security, said in a report shared with The Hacker News.

"The most extensive operation targeted a Redis (remote dictionary server) instance at one university that was configured to allow access without authentication. The agents worked through a long list of known techniques for taking control of an open Redis server. The agents that failed against the hardened Redis target ran continuously for 16 hours without breaks, sleep, or working-hour constraints."

What's notable about accelerating AI-enabled attacks is that the technology is not just used as a force multiplier but has also emerged as the target.

"The integration of AI-enabled tools into enterprise workflows is creating new attack surfaces, particularly where those tools hold privileged access to code, credentials, data, or connected applications," Recorded Future [said](https://www.recordedfuture.com/research/ai-cyber-threat-trends-2026). "Developer tools are a primary target of attacks on AI systems. Threat actors exploited weak access controls and software supply-chain vulnerabilities to steal data or establish persistence."

Besides automating the time-consuming phases of intrusions, LLM-driven pentesting frameworks also lower the technical barrier to entry, enabling actors with minimal expertise to carry out sophisticated attacks.

"Now, an attacker can give an agent a goal in plain language," GitGuardian [said](https://blog.gitguardian.com/another-new-ai-hacking-agent-vs-the-same-credential-problem-antifox-targeting-aws-credentials/). "The agent can investigate the environment, select tools, execute commands, interpret the results, and decide what to try next. The tools are also becoming better at recovering from failed attempts. An agent can encounter an error, interpret the response, modify its next command, and continue investigating."

"Anyone with access to AntiFox or ARTEX can just verbally say into the dictation, 'find exposed credentials, determine what they access, and identify valuable resources.' That incantation initiates a series of technical actions that previously required considerably more hands-on expertise."

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
