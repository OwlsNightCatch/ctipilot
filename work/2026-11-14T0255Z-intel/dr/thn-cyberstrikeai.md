---
title: Open-Source CyberStrikeAI Deployed in AI-Driven FortiGate Attacks Across 55 Countries
author: The Hacker News
url: https://thehackernews.com/2026/03/open-source-cyberstrikeai-deployed-in.html
hostname: thehackernews.com
description: AI-powered CyberStrikeAI linked to 600 FortiGate breaches in 55 countries, with 21 IPs tied to China-based infrastructure.
sitename: The Hacker News
date: "2026-03-03"
categories: ['Article']
fingerprint: b5d188d4843fd328
---
The threat actor behind the recently disclosed artificial intelligence (AI)-assisted campaign targeting Fortinet FortiGate appliances leveraged an open-source, AI-native security testing platform called **CyberStrikeAI** to execute the attacks.

The new findings come from Team Cymru, which detected its use following an analysis of the IP address ("212.11.64\[.\]250") that was used by the suspected Russian-speaking threat actor to conduct automated mass scanning for vulnerable appliances.

CyberStrikeAI is an "open-source artificial intelligence (AI) offensive security tool (OST) developed by a China-based developer who we assess has some ties to the Chinese government," security researcher Will Thomas (aka [@BushidoToken](https://x.com/BushidoToken/status/2028521486844088336)) [said](https://www.team-cymru.com/post/tracking-cyberstrikeai-usage).

Details of the AI-powered activity came to light last month when Amazon Threat Intelligence [said](https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html) it detected the unknown attacker systematically targeting FortiGate devices using generative artificial intelligence (AI) services like Anthropic Claude and DeepSeek, compromising over 600 appliances in 55 countries.

According to the [description](https://github.com/Ed1s0nZ/CyberStrikeAI) in its GitHub repository, CyberStrikeAI is built in Go and integrates more than 100 security tools to enable vulnerability discovery, attack-chain analysis, knowledge retrieval, and result visualization. It's maintained by a Chinese developer who goes by the online alias Ed1s0nZ.


Team Cymru said it observed 21 unique IP addresses running CyberStrikeAI between January 20 and February 26, 2026, with servers primarily hosted in China, Singapore, and Hong Kong. Additional servers related to the tool have been detected in the U.S., Japan, and Switzerland.

The Ed1s0nZ account, besides hosting CyberStrikeAI, has published several other tools that demonstrate their interest in exploitation and jailbreaking AI models -

- watermark-tool, to add invisible digital watermarks to documents.
- banana\_blackmail, a Golang-based ransomware,
- PrivHunterAI, a Golang-based tool that uses Kimi, DeepSeek, and GPT models to detect privilege escalation vulnerabilities.
- ChatGPTJailbreak, which contains a README.md file with prompts to jailbreak OpenAI ChatGPT by tricking it into entering a Do Anything Now (DAN) mode or asking it to act as ChatGPT with Developer Mode enabled.
- InfiltrateX, a Golang-based scanner for detecting privilege escalation vulnerabilities.
- VigilantEye, a Golang-based tool that monitors the disclosure of sensitive information, such as phone numbers and ID card numbers, in databases. It's configured to send an alert via a WeChat Work bot if a potential data breach is detected.

"Further, Ed1s0nZ's GitHub activities indicate they interact with organisations that support potentially Chinese government state-sponsored cyber operations," Thomas said. "This includes Chinese private sector firms that have known ties to the Chinese Ministry of State Security (MSS)."

One such company the developer has [interacted](https://github.com/knownsec/404StarLink/issues/190) with is [Knownsec 404](https://nattothoughts.substack.com/p/knownsec-the-king-of-vulnerability), a Chinese security vendor that [suffered a major leak](https://www.resecurity.com/es/blog/article/knownsec-data-breach-a-trove-of-espionage-tradecraft-with-an-insider-narrative) of more than 12,000 internal documents late last year, exposing the firm's employee data, government clientele, hacking tools, large volumes of stolen data such as South Korean call logs and information related to Taiwan's critical infrastructure organizations, and the inner workings of ongoing cyber operations targeting other countries.

"Ostensibly, KnownSec appeared to be just another security company, but this is only a half truth," DomainTools [noted](https://dti.domaintools.com/the-knownsec-leak-yet-another-leak-of-chinas-contractor-driven-cyber-espionage-ecosystem/) in an analysis published this January, describing it as a "state-aligned cyber contractor" capable of supporting Chinese national security, intelligence, and military objectives.

"In reality, \[...\] it has a shadow organization that works for the PLA, MSS, and the organs of the Chinese security state. This leak exposes a company that operates far beyond the role of a typical cybersecurity vendor. Tools like ZoomEye and the Critical Infrastructure Target Library give China a global reconnaissance system that catalogs millions of foreign IPs, domains, and organizations mapped by sector, geography, and strategic value."

Ed1s0nZ has also been observed making active modifications to a README.md file located in an eponymous repository, [removing references](https://github.com/Ed1s0nZ/Ed1s0nZ/commit/5c806c2580fadd9b564b9d32b0db3364dfd0349e) to them having been honored with the Level 2 Contribution Award to the China National Vulnerability Database of Information Security (CNNVD). The developer has also claimed that "everything shared here is purely for research and learning."

According to [research](https://www.bitsight.com/blog/chinese-vulnerability-database-analysis-cnvd-cnnvd) published by Bitsight last month, China maintains two different vulnerability databases: CNNVD and the Chinese National Vulnerability Database (CNVD). While CNNVD is overseen by the Ministry of State Security, CNVD is controlled by CNCERT. Previous findings from Recorded Future have [revealed](https://www.recordedfuture.com/blog/chinese-mss-vulnerability-influence) that CNNVD takes longer to publish vulnerabilities with higher CVSS scores than vulnerabilities with lower ones.

"The developer's recent attempt to scrub references to the CNNVD from their GitHub profile points to an active effort to obscure these state ties, likely to protect the tool's operational viability as its popularity grows," Thomas said. "The adoption of CyberStrikeAI is poised to accelerate, representing a concerning evolution in the proliferation of AI-augmented offensive security tools."

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
