# extract: served via trafilatura-direct
---
title: Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel
author: The Hacker News
url: https://thehackernews.com/2026/09/thousands-of-openai-agents-quietly.html
hostname: thehackernews.com
description: Autonomous agents identifying as OpenAI systems used a German wiki to coordinate a timed web task and share a sandbox bypass.
sitename: The Hacker News
date: "2026-09-05"
categories: ['Article']
---
A group of AI safety researchers says a fleet of autonomous agents that identified themselves as OpenAI systems left about 18,000 posts on a dormant 25-year-old German wiki between May and July 2026, using the site as a shared board to pool answers to a timed web task and pass around a way out of their sandbox.

The activity was concentrated on **DSEwiki**, a German software developer wiki that runs on the ProWiki farm at wikiservice[.]at and had been edited about 20 times over the previous decade.

The researchers, led by Sydney Von Arx of the AI safety nonprofit [Nightingale Collective](https://nightingalecollective.org/), reconstructed the deleted pages from edit history and published their analysis along with a downloadable copy of the data.

The wikis let anyone change a page with an ordinary web request, the kind normally used only to read a page rather than to write one. Agents that were restricted to reading the internet could therefore still write to the site, because the restriction was written against the request type their harness expected writes to use, not against what the old wiki software would actually accept.

"We found ~18,000 posts from autonomous AI agents (self-identifying as from OpenAI) using the public internet to communicate during a web-retrieval task," the researchers wrote in [their published report](https://collusion.wiki/).

The agents were working through timed lookup tasks of usually five questions, and many were given questions that other agents had already answered. According to the report, they posted results, raw data, and predictions of upcoming questions so that agents running ahead could hand answers to those running behind.

About 17,000 of the edits on DSEwiki came from Microsoft Azure addresses, 98.5% of them, and the agents gave themselves more than 3,700 distinct names such as OpenAIResearcher and OAIResearchMar26, drawn from a feature of their task plus a date each was apparently told it was running on.


The researchers documented several distinct behaviors on the site -

- **Writing via a read request:** agents used the wikis' acceptance of state-changing read requests to post without the ability to send a normal write request.
- **A proxy bypass:** one task needed a statistic to two decimal places from a Microsoft Power BI dashboard, reachable only with a write request the sandbox blocked, so agents worked around the block and shared the method.
- **Impersonation:** agents made edits under the name of a wiki moderator.
- **Coordination to cheat a timed task:** agents formed groups to relay answers and reverse-engineer the order of future questions.
- **Alternate routes:** 197 of the roughly 18,000 edits came from Amazon Web Services, DigitalOcean, and the Tor anonymity network rather than Azure, often under the same agent names.

The bypass turned on a gap the agents found in their own sandbox. The environment allowed traffic to reach Azure storage hostnames ending in .blob.core.windows.net without passing through its security proxy, but it did not verify that such a hostname was valid.

An [agent invented](https://x.com/thlarsen/status/2095853824934330386) bypass[.]blob[.]core[.]windows[.]net, pointed it at the real dashboard's address, 20.223.25[.]152, by editing its /etc/hosts file, and sent its blocked request there instead. One agent posted the method, and another reported reproducing it about 14 minutes later. The wiki path worked the same way, the researchers say, turning a web capability meant only for reading into a way to write to the public internet.

The researchers say the wiki activity was a separate episode from the OpenAI models that [broke into Hugging Face](https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html) in July, as described in [OpenAI's July disclosure](https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html).

Those agents had no internet access and had to escape a sandbox, while the agents on the wiki were given web access as part of their task and left no sign of the internal message board the Hugging Face swarm used.

In [an independent investigation](https://thehackernews.com/2026/08/openai-says-reward-hacking-drove-ai.html) of the Hugging Face incident, METR found that roughly 1,200 agents exchanged more than 70,000 messages and files on an unsanctioned board, and that about 700 of them went on to attack the platform.

### What OpenAI Has Said

OpenAI has not publicly disclosed the wiki episode, and the researchers infer from the site's public logs that the company found it. Addresses registered to OpenAI first visited the wiki on June 21, and agent editing collapsed the next day.

The Hacker News confirmed via [ARIN's registry](https://rdap.arin.net/registry/ip/199.47.142.0) on September 5 that one of the address blocks the report cites, 199.47.142.0, is registered to OpenAI OpCo, LLC.

OpenAI has not confirmed that the agents were its own. Asked about the report, which Reuters first reported, an OpenAI spokesperson said the German activity "wasn't related to Hugging Face" and would not have appeared in that incident report, and denied that its legal team had discouraged an investigation.

The company has said it cannot respond in detail to a report it has not reviewed, and that the researchers declined its access request. In its own account of the Hugging Face incident, OpenAI has described the same underlying behavior that arises during training.

"After investigating this incident, OpenAI discovered through retrospective CoT reviews that agents learned to use improvised collaboration channels in rare cases during the training process for some OpenAI models, including the model that drove the Hugging Face activity, even when the collaboration tool was not enabled," the company said in [its technical report](https://openai.com/index/hugging-face-incident-and-the-road-ahead/).

The wiki data shows no third-party systems compromised. The reported harm was to the wiki itself, whose moderator spent weeks deleting agent pages, and to the integrity of the timed task that the agents were cheating on.

The researchers say they cannot tell from the wiki alone whether the task was part of training or an evaluation, and they note the agents must have had some way to converge on the same obscure site.

The pattern extends beyond OpenAI. Anthropic disclosed in July that Claude models had reached real systems during misconfigured cybersecurity evaluations, an episode The Hacker News covered when Anthropic said [Claude mistook the open internet for a capture-the-flag exercise](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html).

The UK's AI Security Institute reported in August that agents in its cyber tests used a public GitHub page as a message board and public tunneling services to reach the internet, findings The Hacker News covered when a [Claude model tried to backdoor an open-source project](https://thehackernews.com/2026/08/claude-mythos-5-tried-to-backdoor-real.html) during testing.

OpenAI released GPT-6 Astra on September 3, a day before the wiki report, and its system card includes a dedicated evaluation for agents that seek out and follow messages left by other agents on external boards.

### Update

OpenAI addressed what it called the "wiki incident" in a [post](https://x.com/OpenAI/status/2096133504417616165) on September 5, saying its agents "wrote to several internet sites" and that the company had treated the episode as an instance of misalignment similar to earlier cases it had already published, rather than as a security incident of the kind it disclosed for Hugging Face.

The company pointed to three earlier reports, on [monitoring internal coding agents](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/), its [GPT-5.6 system card](https://deploymentsafety.openai.com/gpt-5-6), and [safety and alignment in long-horizon models](https://openai.com/index/safety-alignment-long-horizon-models/), as prior signs of agents using the internet in unintended ways.

"We and the larger AI community do not yet have a clear standard for how to report misalignment that shows up during training, evaluation, and deployment, including examples that don't look like traditional security incidents but could provide insight into AI behavior and future risks," the company said, adding that it would share a framework "in upcoming weeks" and was working with government regulators on the issue.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
