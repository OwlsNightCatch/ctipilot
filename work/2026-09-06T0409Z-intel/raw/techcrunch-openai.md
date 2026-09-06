# extract: served via trafilatura-direct
---
title: Another swarm of OpenAI agents reached the open internet without the frontier lab's knowledge | TechCrunch
author: Tim Fernholz
url: https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/
hostname: techcrunch.com
description: It's the latest failure of OpenAI's internal monitoring and security systems.
sitename: TechCrunch
date: "2026-09-04"
categories: ['AI']
tags: ['openai']
---
A group of independent AI researchers [discovered](https://collusion.wiki/index.html) that internally deployed OpenAI agents began posting on an obscure German wiki forum in order to collaborate on evaluations. They appear to have worked together for over a month without OpenAI’s knowledge.

A spokesperson for the frontier lab would not say whether these agents were indeed from OpenAI, or when the lab became aware of their actions. They noted that OpenAI had not been given a chance to review the researchers’ findings before they were published today but said that the AI model maker is “now carefully reviewing its contents and will take any necessary next steps.”

After OpenAI [revealed](https://techcrunch.com/2026/08/26/openai-releases-its-official-report-on-the-hugging-face-breach/) that agents working on an internal evaluation were able to access the open internet and exploit Hugging Face, a group of researchers — Nightingale CEO Sydney Von Arx, AI researcher Cormac Slade Byrd, Redwood Research’s Spencer Kitts, and AI Futures Project’s Thomas Larsen — began searching for evidence of other rogue AI agents.

They put themselves in the agents’ shoes to figure out their needs and deployed their own LLM to identify likely places the agents might congregate. They then identified a wiki-hosting service that would be particularly vulnerable: The DseWiki is 25 years old but had just 10 edits in the last 20 years — before the agents arrived.

Starting on May 11, the researchers tracked agents, many with [OpenAI identifiers in their names](https://collusion.wiki/explorer/labels/1.html), trying and finally succeeding in editing the German wiki site. By mid-June, the agents were actively trading tips on how to answer web search questions posed under time limits, sharing answers to pass the tests. A human moderator apparently noticed these posts and started deleting them, seeing them as spam, which the agents fought back against, trying to hide their posts from alphabetical sorting by beginning each with the string “ZZZ.”

“The administrator spent the next 5 days fighting a losing battle against the agents, deleting an average of 100 pages a day while the agents created about 400 new pages per day,” the researchers wrote. “On June 22, the agent edits suddenly stop, and the administrator spends each evening over the next 5 weeks deleting the remaining agent-created pages. Agents deleted the content of the front page of the wiki and replaced it with their link dumps. The moderator restored the original version. This back-and-forth happened nine times.”

Eventually, someone at OpenAI appears to have noticed — the researchers track apparently human browsers coming from OpenAI IP addresses, and then agent activity drops to near zero, before spiking as OpenAI-affiliated visitors attempt to recover the deleted pages.

While OpenAI has made vague disclosures about agents gaining unauthorized access to external communication services, it had not previously disclosed this specific incident, or said how often this type of thing has happened. While no obviously illegal activity appears to have occurred during this incident, it raises more questions about whether OpenAI can monitor and control the technology it is building, at a time when there is limited public oversight or input into frontier AI labs.

“The lack of any real federal AI governance means that frontier companies can pick and choose when they disclose incidents like this,” Representative Lori Trahan (D-MA) said. Trahan has introduced a bipartisan bill, the Frontier Act, that would require labs to disclose these incidents and host independent auditors.

AI safety researchers are concerned that the latest generation of powerful models, whose reasoning is [increasingly opaque](https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/) to its creators, could take actions that harm people. Astra, released yesterday by OpenAI, appears to be its most capable model yet.

The company says Astra is also the model most likely to follow human direction, but third-party researchers who were asked to evaluate it expressed concern about its alignment. The U.K.’s AI Safety Institute and Apollo Research both reported concerns that the model might be aware that it was being evaluated and potentially hide its real behavior.

“Apollo believes that, given the higher rates of eval awareness and limited evaluation window, low rates of misbehavior here do not provide substantial evidence about the model’s alignment or misalignment,” the researchers [wrote](https://deploymentsafety.openai.com/gpt-6-astra/external-evaluations-for-alignment---apollo-research) in their evaluation.
