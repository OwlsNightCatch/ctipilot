---
title: A Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats
author: The Hacker News
url: https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html
hostname: thehackernews.com
description: Researchers demonstrated Meta Muse flaws enabling conversation theft and cloud machine takeover; NebuSec says the issues are fixed.
sitename: The Hacker News
date: "2026-11-21"
categories: ['Article']
tags: ['AI Agents', 'artificial intelligence', 'Cloud security', 'Meta', 'Prompt Injection', 'Vulnerability']
fingerprint: cdcb099b69be8ed3
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYiVrbfn3FWfI_uNyjj8q9SZ38d2mHKu2ehdtYYKPwyg-05yKJBYUAPEaVxJq5KDGwU11X2tmEKNUKPIHQY9s67e1K9w_8NRdEOxVCDJqqMbQ6F27kfOj3GKjcQ3-0WHFNg7uYT6QeIU90qX1YW_Zvyn7WhZwpV41i5Pj6watQsF7Ti8NN1GIQLxw-jPc/s1700-nu-rw-lo-l85-e365/muse-ai.jpg
pagetype: article
filedate: "2026-11-25"
---
A malicious webpage could extract a **Meta Muse** user's private conversations and stored memories from the assistant without triggering any approval prompt, researchers have shown.

The same attack could be extended to reach the credentials Muse stores for the user's connected accounts.

The work was a laboratory demonstration, not an attack on real users, and it stayed inside the individual user's cloud machine. **NebuSec**, the security firm that published it yesterday, says Muse's team has since fixed every weakness it describes.

Muse is Meta's personal AI agent, launched on September 8, that works through the online accounts a user connects to it and can make purchases on their behalf. Each person's agent runs on its own cloud computer.

There, a monitoring layer called **Sentinel** is meant to be the single gate for anything the agent sends out, and the passwords and tokens for connected accounts are supposed to stay beyond the agent's reach.


Muse's team described the aim at launch: "So we designed the system to assume the agent may be under attack and limit the potential damage."

In the demonstration, a malicious page the agent opened could pull a user's conversation history and stored memories to an external server and alter them, with no prompt shown to the user, according to the firm's [research write-up](https://nebusec.ai/research/meta-muse-credential-exposure/).

From there, the researchers chained a flaw in Muse's built-in browser, which the assistant uses for tasks such as creating PDFs, to a Linux kernel flaw, thereby taking full control of the user's cloud machine. They set out that chain in a [technical breakdown](https://nebusec.ai/research/inside-meta-muse/).

That full control reached the credential store, the saved files, and Sentinel itself, the parts Muse's [security design](https://muse.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) keeps walled off from the agent.

The compromise went no further than that one machine. The researchers did not break out to the shared server beneath it or into other users' machines.

Muse was built to assume its own agent could be turned against the user and to box in any break-in. Each of those controls worked as designed, the firm said, yet the attack still ran the whole way through.

The firm says it reported the findings to Muse's team and that the exploits were all fixed before publication. Meta has not publicly confirmed the fixes or commented on the work, and the write-up does not say whether any user data was accessed before the patches went in.

The firm's Muse research broke into the cloud system behind the assistant, unlike an [earlier Muse flaw](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html) found in September, which only let malware already on a user's Mac hijack the assistant on the device.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
