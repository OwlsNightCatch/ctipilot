---
title: "Attackers Pick the Target, AI Does the Rest: Cyber Predictions for 2027"
author: Dick O'Brien Principal Intelligence Analyst; Threat Hunter Team
url: https://www.security.com/threat-intelligence/cyber-ai-predictions-2027
hostname: security.com
description: Attackers are handing more of their work to AI. Next year could bring the first major breach in which the victim’s own AI agents do most of the attacker’s work.
sitename: SECURITY.COM
date: "2026-11-17"
fingerprint: d7c119db8fa7f649
language: en
image: https://www.security.com/sites/default/files/styles/blogs_hero_tiny/public/2026-11/Hero%20Image_0.jpg.webp?h=d0c468d4&itok=SQNb0d20
pagetype: article
filedate: "2026-11-25"
---
# Attackers Pick the Target, AI Does the Rest: Cyber Predictions for 2027

## Attackers are handing more of their work to AI. Next year could bring the first major breach in which the victim’s own AI agents do most of the attacker’s work.

## Key points

- Humans will pick the target, but AI will run most of the attack.
- AI credentials will become the new cloud keys.
- Shadow AI agents will present a new challenge.
- Patching alone will not be enough to tackle modern threats.
- Ransomware will break another record, with data-theft waves on top.
- The line between spies and criminals will keep blurring.

As the AI juggernaut continues to roll on, in 2027 we may reach a point where cyber attackers need to do little more than pick a target and collect the money, information or access at the end. AI agents will increasingly handle reconnaissance, exploitation, credential theft and lateral movement, working at machine pace.

Last year, we predicted that [agentic AI would lower the barrier to entry for attackers](https://www.security.com/feature-stories/five-cyber-predictions-2026). Over the past 12 months we have watched that happen, and most of our predictions for 2027 extend what we are already seeing, while one or two go further. As organizations give AI agents standing access to their data, we would not be surprised to see a major breach in which the attacker brought almost no tools of their own, because the victim’s own agents did the work.

## Humans will pick the target, but AI will run most of the attack

Until recently, attackers used AI as an assistant, however, increasingly, they are putting it in charge. The [“Skynet” agent](https://www.security.com/threat-intelligence/ai-llmjacking-skynet) we reported on in October 2026 wired a large language model (LLM) into the center of an attack tool. The tool had around 74 callable functions covering reconnaissance, exploitation, credential theft and botnet control. Its operators described the unattended setting as “Skynet mode” and authorized it to run up to 100,000 steps without human approval.

This is not yet the norm. Most intrusions still have a human at the keyboard making the important decisions. But the direction is clear, and [Google’s threat analysts](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026) and others have described the same shift from chat-based assistance to agentic orchestration. An agent does not sleep, does not need to be paid and can run many intrusions at once. An operator who once handled one victim at a time could now supervise agents’ activity on dozens.

While agents deployed in most organizations today still run under constrained scopes or human-in-the-loop approvals, they are vulnerable to [prompt injection attacks or indirect tool abuse](https://www.ibm.com/think/topics/prompt-injection), which could place them under the control of attackers without them even needing to exploit a vulnerability to send the agent rogue. Prompt injection attacks involve the hackers feeding a malicious prompt directly into a LLM that they have gained access to, while an indirect attack involves hackers hiding their payloads or instructions in data consumed by the LLM – such as software tickets, code reviews or web pages that the LLM has been instructed to read. The attackers are essentially tricking the LLM, no vulnerabilities required.

[Model poisoning](https://www.huntress.com/generative-ai-guide/ai-data-poisoning) is another way that attackers can potentially interfere with AI agents’ operations. It involves tampering with the data, fine-tuning samples, or open-source weights that an AI uses to learn, so that the AI develops a deliberate blind spot or backdoor known only to the attacker. Security teams are generally so worried about protecting credentials and endpoints, they may not think about whether the intelligence inside the model itself has been compromised. These attacks are also often difficult to detect as the model appears to be functioning normally, and strange outputs may simply be put down to hallucinations.

In 2027 and beyond we expect the human role in many AI-driven cyber attacks to shrink towards choosing targets and collecting the money. Reconnaissance, exploitation, credential theft and lateral movement will increasingly be handled by agents working at machine pace, which means the gap between first access and damage will keep closing. Low-skilled attackers will benefit most: capabilities that once needed a team of specialists will be available to anyone who can point an agent at a list of targets. For defenders, the quality of attacker tradecraft will matter less than its volume.

Agents will also change what attackers use. Living off the land, where attackers use tools already present on the victim’s network, has been one of the defining tactics of the past decade. The next version may be living off the AI: attackers turning the victim’s own coding assistants and agents, and the permissions they hold, against the organization. [Gartner forecast](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) task-specific agents in around 40% of enterprise applications by the end of this year, and every one of them holds standing credentials and access to data. We would not be surprised to see the first major breach in which the attacker brought almost no tooling of their own, because the victim’s agents did the work.

## AI credentials will become the new cloud keys

Attackers learned long ago that cloud credentials were worth stealing, and AI credentials are their newest target. Our recent research on the [Aoki infostealer](https://www.security.com/threat-intelligence/aoki-infostealer-ai-targeting) found it harvesting credential and session files for Claude, Codex, Cursor, Gemini and other AI coding assistants. Skynet, for its part, scans for exposed AI endpoints and uses them to fund and conceal its operations, leaving the victim to pay for every step.

There is a market for what they steal. Google found that [underground prices for AI accounts more than doubled in 2026](https://securityledger.com/2026/09/google-llmjacking-powers-cybercriminals-use-of-ai/). Stolen AI access is useful in several ways: free computing power, a way around bans imposed on accounts that have been abused, and a way to strip safety controls from commercial models. Attackers can steal AI access in order to run AI-driven attacks.

In 2027, we expect AI keys to join browser cookies and crypto wallets as a standard target for infostealers, and for the resale of stolen AI access to mature into its own underground business, much as initial access brokers did for network access. Developers will be the main targets. A coding assistant’s configuration files can tie together API keys, source code repositories and cloud accounts, which makes a developer’s workstation one of the most valuable machines in the organization. Many victims will discover the theft through an unexpected bill, not an alert.

AI providers will respond with shorter-lived tokens and tighter controls, as the cloud providers did. Attackers will respond by stealing live sessions instead of static keys. If the history of cloud credentials is a guide, it will take organizations a couple of painful years to treat AI credentials with the same care as the rest.

## Shadow AI agents will present a new challenge

As the use of AI continues to become more commonplace across almost all organizations and workplaces, we may see a shift from the traditional issue of “shadow IT” where software, hardware, or other services are used without the knowledge or approval of the enterprise’s IT department, to “agent shadow IT”, where AI tools are being used without the knowledge or approval of organizations’ IT or security departments.

This could be employees using things like AI tools, local models, or unapproved plugins to get their work done faster, without telling their IT or security departments. This is likely to become a bigger issue and [has been observed already today](https://www.ncsc.gov.uk/blogs/the-hidden-risks-of-shadow-ai) where security teams cannot protect what they do not know exists. These unofficial AI helpers often have direct access to company data and code, which may get fed back to whoever is running the AI without restrictions or specialized agreements being in place instructing the AI not to leverage or use the data, leading to this becoming a leak or information disclosure issue.

This could also be a more pronounced issue in markets where the popular, Western AI coding assistants are not legitimately available, leading to those wanting to use them turning to rogue operators. A recent [Symantec Threat Hunter Team blog](https://www.security.com/threat-intelligence/openai-claude-unauthorized-relays) discussed how a grey market relay service was installing the genuine OpenAI Codex and Anthropic Claude Code CLIs on enterprise systems and then reconfiguring them to route every request through third-party infrastructure instead of the vendors' own servers. This activity was mostly impacting a variety of enterprises across mainland China where many Western AI coding assistants are not officially available.

Of note was that this operation also disabled the CLI's execution sandbox entirely, enabling network access for the write sandbox, replacing the user's real API credentials with relay-issued tokens, and disabling telemetry and error reporting. While there was no evidence found in this case that the relay operator had abused their level of access, a potential risk is that the configuration it installed would let the operator read every prompt, file, and secret passed through the agent and run commands with the user's full privileges. Given this was not a legitimate service, it’s unlikely any IT or security oversight for this product existed in the organizations where it was being used.

## Patching alone will not be enough to tackle modern threats

The [PHP2Shell vulnerabilities](https://www.security.com/threat-intelligence/php2shell-critical-vulns-cve-2026-109618-109619) (CVE-2026-109618 and CVE-2026-109619) show how short the patching window has become. Both flaws allow unauthenticated remote code execution. Technical details leaked on October 20, 2026, a day before the PHP project released fixes, and public proof-of-concept code followed. Attackers did not need to be clever. They just needed to be early.

Defenders are told to patch faster, but patching is a race against machines that defenders cannot win. Testing and deploying a critical patch takes days or weeks, and for some systems, like those older PHP versions, it never happens. AI is shrinking the patching window. It can increasingly read a patch, compare it with the old code and produce a working exploit in minutes, and it can scan open-source projects for flaws before the fixes ship.

Vulnerabilities are also only part of the problem. Attackers using AI are just as good at finding what has no CVE: misconfigurations, forgotten internet-facing systems, default or reused credentials and over-permissioned identities, and at chaining several low-severity weaknesses into a working attack path. In 2027 we expect more breaches in which no single vulnerability was to blame.

So, we expect the conversation to shift from how fast organizations patch to how fast they can make a threat irrelevant, whether or not a patch exists. Think of it as mean time to mitigate. The answer will lean on controls that do not depend on knowing the vulnerability: behavioral blocking, default-deny application control, tight segmentation and identity protections that stop an attacker using what they have stolen. Patching will still matter. It just may not be enough.

## Ransomware will break another record, with data-theft waves on top

Ransomware shows no sign of slowing. There were 3,126 claimed attacks in the third quarter of 2026, the highest quarterly total we have recorded, including the busiest single month, August, with 1,184. Across the first three quarters of 2026 there were 7,777 claimed attacks, 28% more than in the same period of 2025 and already close to the 8,498 recorded in the whole of last year.

The line-up behind those numbers keeps changing. Over the past 12 months, Qilin has been the busiest operation with 1,457 claimed attacks, followed by The Gentlemen with 870, a group that did not feature in our 2025 top 10. Akira (604), Inc (482) and DragonForce (391) follow behind. LockBit, which had struggled to rebuild after the disruption of its operation in 2024, is back with 365.

Data-theft-only extortion is less predictable. It surged in 2025, driven by a handful of mass campaigns, notably Cl0p’s attacks on Oracle E-Business Suite and the Salesforce-related attacks carried out by ShinyHunters, and it fell back in 2026, with 808 identified extortion-only attacks in the first three-quarters of 2026, against 1,187 a year earlier. One campaign against a vulnerability in a widely used enterprise product can add hundreds of victims of these kinds of attacks in a single quarter, making the likely volume of these kinds of attacks harder to predict.

We expect more of the same in 2027: encrypting ransomware as the steady baseline, with extortion-only waves arriving whenever an attacker finds a zero-day in widely used software. Encryption may keep its place partly because it pays better: [Coveware found](https://www.veeam.com/blog/cyber-extortion-payment-trends-q2-2026.html) victims paid in only around 15% of cases in the second quarter of 2026 where leaking data was the only threat.

## The line between spies and criminals will keep blurring

Many of the threat actors we track no longer fit neatly into a single category. Our research on [Jewelbug](https://www.security.com/blog-post/jewelbug-crypto-fraud-espionage) found a China-based group running espionage operations and a cryptocurrency fraud business from the same infrastructure and the same control panel. On one side it compromised government webmail in the Middle East. On the other, it ran an AI-generated network of fake exchange download pages to target Chinese-speaking crypto users. We assess that the fraud business most likely supplied access, infrastructure and delivery for the espionage.

Warlock, a ransomware operation we wrote about in our [Ransomware 2026 whitepaper](https://sed-cms.broadcom.com/sites/default/files/2026-01/RWN-2026-WP100_1.pdf) and [blogged about more recently in October 2026](https://www.security.com/threat-intelligence/warlock-ransomware-critical-infrastructure), fits the pattern too. Some of its tools trace back to earlier Chinese espionage activity, and ransomware may at times serve to obscure espionage.

We expect this to go further in 2027. Governments that want deniable capabilities have every incentive to let contractors fund themselves through e-crime, and criminals gain tooling, protection or simply tolerance in return. The result is groups whose motives change from one intrusion to the next: espionage on Monday, extortion on Friday.

We expect to see more high-profile incidents in which ransomware turns out to have been a cover for espionage or sabotage, and incident responders will have to start asking what the ransomware was hiding. Attribution will get harder, and the stakes will rise with it. Defenders may need to stop running separate playbooks for ransomware and espionage. Every ransomware incident should include a search for earlier access and for what was taken before anything was encrypted.

## What to do about it?

Several of the trends above share one answer: reduce what attackers can do once they are on a network. Behavioral protection, visibility across endpoints and cloud, and governing how AI is used inside your organization matter more than ever when exploits arrive faster than patches. For resource-strapped teams or complex enterprises looking to deepen visibility and correlate signals across their stack, solutions such as [Symantec CBX](https://www.security.com/cbx) can fill that gap.

## Learn more in our predictions webinar

Catch a live breakdown of what’s ahead in our *2027 Threat Predictions* webinar with Principal Intelligence Analyst Dick O'Brien and Threat Analyst Alan Neville on December 16, 2026. [**Register now to gain expert insights**](https://engage.broadcom.com/2027-threat-forecast) into the key AI, ransomware, and espionage trends to plan for in 2027.

## Join our 2027 Threat Predictions Webinar

[Find out what's ahead](https://engage.broadcom.com/2027-threat-forecast)
