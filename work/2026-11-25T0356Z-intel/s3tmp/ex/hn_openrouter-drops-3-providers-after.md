---
title: OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms
author: The Hacker News
url: https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html
hostname: thehackernews.com
description: Attackers stole AI prompts from three inference providers, prompting OpenRouter to remove 125 endpoints from Zero Data Retention eligibility.
sitename: The Hacker News
date: "2026-11-22"
categories: ['Article']
tags: ['artificial intelligence', 'Cloud security', 'Credential Theft', 'data breach', 'data privacy', 'OpenRouter']
fingerprint: "9c1fd389ac3607c7"
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEGP3P_elvK4C-QnSx5onZ67viDXCIgPCUYqtTF_RDNcLJfyQ4QMbegUmn8AJy5nEmnXfN4ACr6hHztG_DdqXlj54S21toacPQaZgRx2rgqZltN3lvREpZR2xlvgXF_iZ7zW0XT0b91mMiRDVaEB6TUvMFlWwaSa3_C7gwpxdKcNhLtIq15KqwaZrR3VI/s1700-nu-rw-lo-l85-e365/openrouter.png
pagetype: article
filedate: "2026-11-25"
---
Attackers stole data from inside three AI inference providers for months, and none of the three knew until researchers told them, the industrial cybersecurity company Dragos said this week.

Some of the stolen requests were flagged as **Zero Data Retention**, the setting that is supposed to mean a prompt is never stored.

**OpenRouter**, a gateway that routes customers' AI requests to a pool of third-party providers, said today that it has removed three providers from its platform, removed 125 endpoints from eligibility for Zero Data Retention, and notified all potentially affected customers. The findings showed no breach of OpenRouter itself, the company said.

The earliest of the three breaches began in mid-July. The planted prompts were bait, but they were processed alongside real customer requests, and those were almost certainly copied too, the firm said.

The finding comes from [canary token research](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) that seeded about two million prompts with unique web links and credentials between July and November, then watched for anyone using them. A planted secret can only be learned in one place, so any use of it means someone read the prompt that carried it.

The largest of the three breaches involved a couple hundred AWS keys that were planted, each sent in exactly one request to one provider during a few short windows in late October. Every request sent during those windows was stolen, and some came from requests the provider had rejected before a model ever ran, indicating the attacker was copying traffic at the first point of arrival rather than deeper in the inference stack.

The thief tested keys within hours in some cases, listed S3 buckets, searched Secrets Manager and Parameter Store, and tried to create Bedrock API keys and add IAM users to keep access, driving tens of thousands of AWS API calls.

One attacker appears to have compromised two of the providers at once, using secrets from both from a single rented server.

On November 1, the same attacker brought in ARTEX, an AI-driven penetration testing framework, and used it only to confirm that keys it already held were still live. Two of its user agents, artex-agent and artex-judge-r121, appear in no public indicator list the firm could find and are worth adding to detections.

"A privacy flag doesn't help when the attacker is already inside," wrote HD Moore, the firm's chief research officer.


The second finding needed no break-in. Sellers on an AI inference marketplace listed models at the lowest prices, enabled request logging, and collected what flowed through, the research found.

The people doing it looked like individuals on home internet connections. One, working from a Mac on home broadband in France, took passwords from two prompts and typed root SSH login attempts by hand, then used the same machine to test several planted AWS keys.

One of those keys had traveled through a different router that quietly forwarded some of its traffic to the marketplace, a hop that no customer was told about. That router has since told the firm it stopped, and route tracing across about 2,000 paths found several hundred unidentified systems, plus one seller that quietly adds about 1,000 hidden tokens to every prompt.

A Chinese AI lab, which the research does not name, fetched the secret links from more than half of the seeded prompts sent to its models between July and October, including about two-thirds of the requests marked no data collection or Zero Data Retention. Prompts sent to U.S. hosting providers that resell the lab's models triggered the same scraper, thereby flowing back to the lab.

A git client on another cloud later tried to clone private repositories referenced in the prompts, but only for that lab's models, and one large U.S. provider kept crawling a secret link more than two months after a single request to its search endpoint.

Twenty-four days after one prompt was sent, its secret link was posted into a chat on Feishu, the Chinese workplace app known as Lark elsewhere. The link was opened within two minutes from three desktops and three phones in Beijing and Shanghai.

The firm had disclosed only the first 8 characters of the provider's link, so whoever posted it was reading a cached copy of the full prompt.

In practice, Moore wrote, the flagged prompts were kept, passed to other companies, and read by human beings.

OpenRouter said in an [incident announcement](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) that the 125 endpoints removed from Zero Data Retention eligibility cover providers flagged by the researchers plus others cut as a precaution. Any endpoint removed during the review will require assurances and validation before its status is returned.

The gateway is adapting the researchers' testing approach so that the checks can run on an ongoing basis and is verifying network paths to identify where requests and responses may be forwarded to third parties.

The researchers are now working with about a dozen providers, and planted keys and secret links were still being accessed months after the first thefts, as of this week.

Railway, a platform company, said in October that an [intrusion it suffered](https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html) was likely part of a series of attacks built to target platform companies with the end goal of compromising AI inference providers.

Not all affected providers have posted publicly, the gateway said, and it has notified affected users either way. Three have posted.

### What the Providers Have Disclosed

An attacker took control of an inference server at Phala and could view request data while it was being processed, the provider said in a [preliminary incident report](https://phala.com/posts/phala-november-preliminary-incident-report) last week. The incident was contained on November 8, and the model service has been restored with added protections.

Requests to the DeepSeek V4 Flash 0731 model that reached Phala through the gateway between October 21 at 00:00 UTC and November 8 at 05:35 UTC should be treated as exposed, the report says, and every key, token, password, or other secret within them should be rotated.

A third-party researcher had been placing unique canary credentials in requests since July 1, and only the ones sent on October 21 and 22 were later misused. Those tests sampled traffic rather than monitoring every request, so the provider maintains the broader precautionary window.

At Together AI, an unauthorized party downloaded stored samples of customer prompts after an AI coding agent committed a credential to the company's public GitHub repository, the company said yesterday in a [security notice](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026). The samples had been collected for routine software testing and were generated by requests to the MiniMax M3, GLM-5.2, and Kimi K2.6 models in June and July.

The party searched the samples for credentials to other services and tested them, and five of the tested credentials were canaries from the researchers' experiment. The company said it has no reason to believe the data went further, understands it has been deleted, and has made zero data retention the default for new accounts.

Novita, another provider on the gateway, confirmed this week in a [privacy notice](https://x.com/novita_labs/status/2124196616358010992) that a routing configuration issue caused some MiniMax requests to be sent on to MiniMax's official API, beyond what was intended for those customers.

Dragos has not named the three breached providers, OpenRouter has not named the three it removed, and neither has said publicly whether they are the same three.

The provider behind the mid-July breach first blamed an internal misconfiguration, then a partner's data processing, before its own investigation found that attackers had compromised its internal credentials, the researchers said. It had still not disclosed the incident publicly as of this week.

### What Users Should Do

The researchers' advice starts from one limit: a privacy flag binds only the first hop, Moore wrote, and AI agents will send whatever they can read, credentials included. Where a prompt goes is a choice, he wrote, and a customer who does not choose hands the choice to the lowest price.

Self-hosting is the only option in which no third party reads a prompt, and going directly to a first-tier provider leaves one company, one contract, and one privacy policy to check.

Routers need more care: pick the upstream providers yourself instead of accepting the default pool, verify that privacy settings actually change where requests go, and stay away from reseller marketplaces, some of whose capacity runs on stolen keys.

A fake credential seeded into the context that agents and pipelines already send serves as a tripwire if any use of it is treated as an incident, and a free Thinkst Canarytoken is enough to get started. Settings that scrub known credential formats from prompts help too, though they miss sensitive data that is not shaped like a key.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
