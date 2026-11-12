---
title: Fireworks AI discloses new breach after cloud provider hack
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack/
hostname: bleepingcomputer.com
description: AI infrastructure startup Fireworks has disclosed a new security breach in which attackers accessed its development machines after breaching a third-party cloud provider.
sitename: BleepingComputer
date: "2026-11-10"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, AI, Artificial Intelligence, Breach, Data Breach, Fireworks, LLMjacking, Security Breach,virus removal, malware removal, computer help, technical support']
fingerprint: "4d128c934d94174b"
---
AI infrastructure startup Fireworks has disclosed a new security breach in which attackers accessed its development machines after breaching a third-party cloud provider.

FireWorks provides a high-performance inference platform for developers who want to deploy and run open-source artificial intelligence models (such as Mistral, Meta's Llama, or Google's Gemma) without worrying about hardware bottlenecks and complex infrastructure tasks.

The company notified law enforcement and customers of another security incident in early October after attackers accessed environment variables containing API keys and tokens stored as secrets for a limited number of accounts.

"The evidence indicates links to a cybercriminal threat actor group, which is financially motivated and aimed at selling tokens from unauthorized access to Large Language Models (LLMs) to illicit routing gateways, known as 'LLMJacking'," [Fireworks said](http://fireworks.ai/security/bulletins/october-2026-security-incident) at the time.

After revoking compromised internal credentials, affected Fireworks API keys, and keys created by the attackers, Fireworks discovered another security incident on October 23.

In the new breach, the threat actors accessed resource metadata (e.g., Fireworks resource identifiers, display names, descriptions, creation time), billing information (e.g., billing and shipping addresses, invoice and payment history, account balance, and credit usage), and incomplete model weights and datasets for some customers.

However, the company said the attackers couldn't access customer payment card numbers because Fireworks doesn't store them.

"A third-party cloud provider that hosted Fireworks R&D machines experienced a security incident on October 23. On October 24, the unauthorized third party used it to reach Fireworks development machines and then run an unauthorized workload that led to additional customer data impact," [Fireworks noted](https://fireworks.ai/security/bulletins/october-2026-security-incident-update) in a Monday advisory.

"We detected this activity on the same day, and followed our incident response processes to take immediate remediation measures and close known critical vulnerabilities. As of October 25, we have not detected further evidence of successful unauthorized access by the threat actor on the Fireworks platform customers use."

Since the attack, Fireworks revoked and replaced credentials and service accounts, restricted unauthorized network pathways, isolated affected systems, and tightened access to data storage and analytics systems to block public or unauthorized access to stored data.

The company is now working with Palo Alto Networks' Unit 42 incident response division to secure its systems against future attacks and further investigate the incident's full scope and impact.

One week ago, researchers at Google's Threat Intelligence Group (GTIG) and Mandiant reported that large language model hijacking attacks (also known as LLMjacking) are [driving record costs for compromised organizations](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/), with cloud AI charges reaching as high as $1 million due to fraudulent calls using stolen API keys.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
