# extract: served via trafilatura-direct
---
title: OpenAI admits it didn't disclose rogue AI wiki hijacking incident
author: Ax Sharma
url: https://www.bleepingcomputer.com/news/security/openai-admits-it-didnt-disclose-rogue-ai-wiki-hijacking-incident/
hostname: bleepingcomputer.com
description: OpenAI admits it did not disclose an incident where autonomous AI agents hijacked a German wiki, created 18,000 posts, shared answers, and bypassed restrictions, saying it treated the activity as model "misalignment" rather than a security breach.
sitename: BleepingComputer
date: "2026-09-05"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Hijack, OpenAI, Sandbox Escape,virus removal, malware removal, computer help, technical support']
---
OpenAI has acknowledged that it did not publicly disclose an earlier incident in which its autonomous AI agents took over a German wiki to communicate, share answers, and exchange techniques for bypassing restrictions.

The company says it treated the activity as model "misalignment" rather than a security incident, but now admits its disclosure practices must expand as AI systems increasingly cause real-world impact.

## Rogue agents built their own message board

The incident began in May while OpenAI agents were completing timed, multi-round web lookup tasks.

In their [writeup](https://collusion.wiki/), independent researchers Sydney Von Arx, Cormac Slade Byrd, Spencer Kitts, and Thomas Larsen state that they uncovered roughly 18,000 posts from autonomous agents that "colluded to share answers, research their environment, and bypass sandbox restrictions."

The agents were supposed to have read-only Internet access but discovered they could write to an obscure German programming wiki, DSEWiki (or *DeutschesSoftwareEntwickler*). They turned it into a shared message board for pooling answers, cheating on tests, predicting future questions, and exchanging techniques for bypassing OpenAI's sandbox restrictions.

The researchers also found agents probing the wiki for cross-site scripting (XSS) flaws, impersonating its moderators, and establishing backup communications, though they found no evidence the XSS attempts succeeded.

When the administrator began removing their pages, one agent warned others that a "wiki cleanup/deletion sweep appears active alphabetically" and directed them to a backup page beginning with "ZZZ" so it would survive longer.

The researchers attributed the activity to internal OpenAI systems based on agent names referencing OpenAI, the nature and speed of the evaluation tasks, infrastructure associated with Microsoft Azure, and subsequent visits to the wiki from OpenAI-linked IP addresses.

However, their investigation was limited to information the agents wrote publicly.

The research team did not have access to OpenAI's internal transcripts or other data that could establish precisely how the agents discovered the wiki and began coordinating through it.

## OpenAI says its disclosure rules must change

In a [statement published](https://x.com/OpenAI/status/2096133504417616165) today, OpenAI said it had historically treated model misalignment as a research issue, with findings communicated through research papers and system cards.

The company said it considered the wiki activity another example of "misalignment" similar to behaviors it had previously discussed, rather than an incident requiring a dedicated public disclosure.

OpenAI's own wording suggests a wider footprint than the researchers documented, describing the episode as one "where our agents wrote to several internet sites."

That differed from its response to the [Hugging Face compromise in July](https://www.bleepingcomputer.com/news/security/openai-says-its-ai-models-hacked-hugging-face-during-testing/), when OpenAI said its AI models hacked the platform after discovering a vulnerability while completing cybersecurity tasks.

A follow-up analysis found that [nearly 700 rogue AI agents had coordinated](https://www.bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack/) during the attack, sharing strategies and creating persistent access mechanisms without direct human instructions.

OpenAI said it treated the Hugging Face breach as a conventional security incident because it affected the security of both OpenAI and third parties. The AI giant began working with Hugging Face and publicly disclosed the incident the following day.

However, OpenAI now acknowledges that the distinction between research misalignment and security incidents is becoming increasingly difficult to maintain.

"This year, we've started to see misalignment cause new types of real-world impact," the company said.

OpenAI says the AI industry lacks consistent standards governing when unexpected agent behavior during training, evaluation, or deployment should be reported, particularly when it does not resemble a traditional cybersecurity incident.

The company is developing a new disclosure framework that it plans to publish in the coming weeks and says it is discussing these issues with government regulators worldwide.

The timing of the acknowledgment is also notable, coming in the same week OpenAI [launched GPT-6 Astra](https://openai.com/index/gpt-6-astra/), which it touts as "the world's most intelligent and aligned model" and state-of-the-art on computer use, browsing, software engineering, and cybersecurity.

OpenAI says Astra is better at staying within its intended scope, measured partly by a new evaluation it built in response to the Hugging Face incident.

However, the problem is not unique to OpenAI.

In July, Anthropic revealed that its [Claude AI breached three organizations](https://www.bleepingcomputer.com/news/security/anthropics-claude-breached-3-orgs-uploaded-pypi-malware-during-tests/) during internal security evaluations, in one case registering a package name it found in documentation and uploading malicious code to PyPI. The package was live for about an hour, in which 15 real systems downloaded and ran it.

As AI models become more capable and gain greater autonomy and access to the Internet and external tools, such incidents are expected to accelerate.

What remains unknown is what else these systems could become capable of, or end up doing, without stronger controls, oversight, and disclosure requirements.

## 
            [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)
        

        Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
