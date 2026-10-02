---
title: AI agent used Zammad zero-days to breach Dutch vulnerability disclosure non-profit - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/10/01/divd-agentic-ai-attack-breach/
hostname: helpnetsecurity.com
description: An agentic AI-powered attack that hit the Dutch Institute for Vulnerability Disclosure (DIVD) on September 21 exploited two Zammad zero-days.
sitename: Help Net Security
date: "2026-10-01"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['0-day', 'agentic AI', 'Europe', 'NCSC-NL', 'open source', 'vulnerability disclosure', '0-day', 'agentic AI', 'Europe', 'NCSC-NL', 'open source', 'vulnerability disclosure']
---
# AI agent used Zammad zero-days to breach Dutch vulnerability disclosure non-profit

An agentic AI-powered attack that hit the Dutch Institute for Vulnerability Disclosure (DIVD) on September 21 exploited two zero-day vulnerabilities in Zammad, an open-source helpdesk and customer support ticketing system.

“Used together, [the two flaws] allowed the attackers to hijack sessions, run code remotely and escalate privileges from the Zammad user to root, in seconds, due to the agentic part of this hack. From there they were able to access other services and read and exfiltrate data,” the Dutch non-profit [shared](https://www.linkedin.com/feed/update/urn:li:activity:7511092587848523778/) on Wednesday.

### The DIVD breach

DIVD is an organization staffed with (predominantly) volunteer security researchers. It searches for new vulnerabilities in software and report them to the vendors, scans the internet for known vulnerabilities, and notifies owners of vulnerable systems via hosting providers, national CERTs or other intermediaries.

A week ago, its computer security incident response team (CSIRT) [revealed](https://csirt.divd.nl/2026/09/24/when-not-if/) that it got hacked and that it started an investigation after reporting the incident to the Autoriteit Persoonsgegevens (the Dutch Data Protection Authority), the Dutch National Cyber Security Centre (NCSC-NL), and discussing their options with the police.

An update on Monday confirmed that the attack was “loud and very very messy.”

“We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic or pattern. It also looks like the agent skipped a few steps on its learning curve, because it has done some pretty dumb things, like polluting its own MITM attack with password spraying,” the organization [said](https://www.linkedin.com/posts/in-every-crisis-you-work-with-whatever-you-share-7510363577375993856--zPB/). 

“But what makes this attack pretty cool is that the agent is so overexplaining in its comments that it makes our job in reverse engineering a lot easier.”

Yesterday’s update revealed the exploitation of the Zammad zero-days.

DIVD has yet to share which data was accessed by the AI agents and why, but noted that the scope of the compromise has been limited thanks to proper network segmentation and the actions of its IT and incident response team after detection.

“We were able to stop the attackers from going deeper into our systems and network. Unfortunately some of the damage was already done. We’ve found signs of compromise that we’re still looking into, and until we can prove otherwise we assume breach. Still, stopping the attackers is a win and in a situation like this you take every win you can get,” they said.

Whether the DIVD breach was the result of agentic AI attempting to achieve a goal that was part of a larger cyber attack or a cyber capability test is unknown.

Recent findings by AI research laboratory Transluce have [revealed](https://www.helpnetsecurity.com/2026/09/24/openai-agent-hacking-australia/) that AI agents have also been using hacking tactics (vulnerability probing) while working on ordinary data retrieval tasks.

### What Zammad users should do

After determining, with the help of Merlon Security researchers, that the attackers had leveraged two Zammad zero-days, the DIVD CSIRT notified Zammad GmbH, which started working on fixes. Then they started pinpointing internet-exposed vulnerable instances and started notifying the owners.

**CVE-2026-102489**, which allows attackers to remotely execute malicious code without logging in, affects Zammad versions 6.3.0 to 6.5.4. 

**CVE-2026-102490**, a privilege elevation vulnerability, allows authenticated attackers with low privileges (the local zammad user) to achieve *root* on the vulnerable system. It affects all versions of Zammad, including the latest alpha release.

Both flaws are currently without a fix, but CVE-2026-102489 is not exploitable in Zammad versions 7.0.0 through 7.1.3 due to environment conditions.

“We advise all users of Zammad to upgrade to version 7 of Zammad or to take it offline. If you want to investigate whether you have been compromised based on our IoCs, you can download our [log check script](https://csirt.divd.nl/downloads/DIVD-2026-00015/cve-2026-102489_ioc_check_script_v2.sh) to check your Zammad logfiles for Indicators of Compromise,” the organization [noted](https://csirt.divd.nl/cases/DIVD-2026-00015/).

The Dutch NCSC [advised](https://www.ncsc.nl/alerts/actief-misbruik-van-zeroday-kwetsbaarheden-in-zammad-update-nu) making a copy of the application and network logs before installing the update: “If there is more information about the abuse of the second vulnerability, these logs can help you in the future to check if your system has been attacked.”

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
