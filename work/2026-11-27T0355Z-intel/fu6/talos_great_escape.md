---
title: "The Great Escape: Tradecraft insights from an agentic swarm"
author: Ryan Fetterman
url: https://blog.talosintelligence.com/the-great-escape-tradecraft-insights-from-an-agentic-swarm/
hostname: talosintelligence.com
description: The OpenAI-linked swarm activity in 2026 is fully traceable through public records. This blog analyzes its tradecraft and compares it to early signals and behaviors from current agentic attack activity seen in the wild.
sitename: Cisco Talos Blog
date: "2026-11-25"
tags: ['On The Radar', 'Landing Page Top Story', 'Top Story']
fingerprint: "350503918d9a8069"
language: en
image: https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/size/w1200/2026/11/swarm-header.jpg
pagetype: article
filedate: "2026-11-27"
---
- The OpenAI-linked swarm activity in 2026 is fully traceable through public records and offers an unprecedented view into how multi-agent AI systems operate and coordinate at scale.
- Distilling and documenting the swarm tradecraft may help defenders understand multi-agent operations and communication, and how agents adapt when a path is blocked.
- Some documented behaviors may transfer to more purpose-built cyber attack frameworks like ARTEX, including methods to persistently store results, the burst-and-pause timing patterns of reasoning loops, and the self-labeling conventions that can reveal workload assignments and distribution.

Beginning in June 2026 and extending for several months, a collection of OpenAI models conducting internal training and evaluation tasks broke out of their containerized environments and accessed websites and databases via the public internet in ways [<u>the company says it did not authorize</u>](https://openai.com/index/how-we-will-do-better-for-australia/).

This activity represents a new kind of cyber event: not a malicious intrusion, but an unintentional series of consequences stemming from an agentic *swarm*, a group of AI agents exhibiting coordinated behavior toward a shared objective. A swarm implies many agents but doesn’t have a rigid count. The main distinction is behavioral; the collective activity of a swarm becomes complex and unpredictable even when individual agents may be explainable. This swarm provided an initial, public glimpse into the behavior and coordination of autonomous, multi-agent operations.

Due to constraints in their evaluation environment, the OpenAI swarm used public internet services as improvised infrastructure, which made the activity visible and traceable. The behaviors exposed revealed methods for persistent probing, iterative payload development, work partitioning and coordination across agents, and adaptation to execution constraints, in ways that are likely to be relevant for understanding agent behavior beyond this just case.

Agentic cyber attack frameworks are [<u>now appearing in intrusion activity</u>](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/?utm_source=chatgpt.com), with the ability to support [<u>scaling to multi-agent operations</u>](https://www.trendaisecurity.com/en-us/resources-insights/deep-research/not-only-artex-the-different-levels-ai-is-used-in-attacks-targeting-japan). These attacker swarms largely replace the use of public internet resources with purpose-built infrastructure that removes some of the artifacts visible. However, documenting our understanding of operational swarm techniques can give defenders a baseline for recognizing behaviors as they move into new environments and contexts. In some cases, we can already see the evidence where these techniques *do* transfer.

In this post, we’ll explore and document the tradecraft of the escaped OpenAI swarm and conclude by comparing it to early signals and behaviors from the current agentic attack activity seen in the wild.

## Background

Swarms are an important concept to track because they can divide work across parallel agents, potentially completing complex tasks faster, though the gains depend on the task and the quality of coordination. Parallel agent coordination was crucial to OpenAI’s ability to [<u>solve the Navier-Stokes Millenium Prize Problem,</u>](https://openai.com/index/navier-stokes-solution/) which arrived at a winning solution with a group on the order of 10,000 concurrent agents over the course of 88 hours.

Early evidence suggests swarms transfer effectively to cyber attack problems. The main factors for swarm efficiency are how parallelizable the tasking is, and if the attackers want to pay the inflated token cost. A rough example is using four agents on the same problem, to get it done twice as fast; as Noam Brown of OpenAI said on a [<u>Dwarkesh podcast</u>](https://www.dwarkesh.com/p/noam-brown), “Because there are four agents working for half as long, you’re paying 2x more to get an answer twice as quickly.”

AI models undergoing training and evaluation operate inside sandboxed computing environments. These are controlled workspaces where they can write and run code, search for information, and iterate toward solutions. These environments are designed to be both enabling and constraining. They give models room to practice, while limiting what they can reach and do, so that mistakes or misaligned behavior stay contained.

## Operating under constraint

While the techniques employed by the OpenAI swarm may have crossed the thresholds of intended use, they should not be viewed as malicious intent. A useful framing for understanding these techniques is creativity under constraint. The agents were optimized to meet their objectives, and they displayed considerable persistence and ingenuity to that end.

The constraints the agents were working around were layered and understanding them helps explain the motivation behind every technique. The most fundamental was the absence of a browser runtime: Agents operating in text and code environments cannot natively load JavaScript-heavy pages, call browser APIs, or interact with dynamic web content. The creative solution was submitting URLs to a public scanner like “urlquery.net” which provided a real Chromium instance on demand.

This workaround by itself, however, was still not enough. Browsers apply a security rule called the same-origin policy: JavaScript running on one website generally cannot read data from another. Cross-origin resource sharing (CORS) lets a destination website explicitly permit access. The agents used public CORS proxies to relay requests when target websites did not grant permission.

They also lacked infrastructure of their own to host payloads or receive data, so they relied on public services such as httpbin, httpbun, and "webhook.site" services capable of testing HTTP requests and responses but not designed for this activity.

In some evaluation environments another constraint applied: Agents appear to have been restricted to GET requests only, with no ability to make outbound POST calls. That is likely what pushed them toward [<u>using public wikis as shared state stores</u>](https://collusion.wiki/), as wiki page edits are a write operation achievable through ordinary browser navigation.

## The tradecraft

In response to their constraints and in persistent pursuit of their objectives, the swarm developed and refined its tradecraft over time. This included chaining legitimate web services like URL shorteners, CORS proxies (services that relay requests to bypass browser security restrictions), Base64 decode endpoints (services that decode encoded data back into executable web pages), and markdown renderers into extraction pipelines that never required dedicated attacker infrastructure.

Talos observed structured work partitioning across parallel agent instances, iterative probe development, and sandbox identification techniques. The agents coordinated using a variety of identifying tags (e.g., `uqscan=claude...`, `CHATGPTTEST1`, `OAI_META_1312`, `archive_test=20261004`). These self-labels, intended as internal tracking strings, became the primary cross-campaign fingerprint linking multiple disparate operations.

To better understand the flow, we will detail the activity of the swarm in a seven-step chain, aligning the purpose of the action with the publicly accessible internet services used.

A separate orchestration layer, Coordinate (COORD), runs above the chain rather than within it. When multiple agents execute the same chain in parallel, COORD governs how work is divided between them — for example, URL shorteners (“da.gd”, “is.gd”) distribute identical payloads to multiple instances; structured identifiers (`?uniq0–19`, `node=`, `validation=v<unix>_<county>_<req>`) partition tasks and track completion. The COORD layer distinguishes a swarm from a single agent running sequentially.

## Evolution and execution

The swarm's operational techniques evolved over time. Early activity relied on silent CDX enumeration, querying public web archive indexes to map target sites and using a single exit node. By the peak operational phase, the swarm was running against multiple simultaneous targets with structured work partitioning, sandbox identification, and covert exfiltration beacons. To better understand these events, we can reconstruct from public records the [<u>unauthorized access to Australian government websites</u>](https://openai.com/index/how-we-will-do-better-for-australia/?utm_source=chatgpt.com).

### Traced extraction demonstration

**Step 1 — RECON: Enumerate target via Common Crawl CDX**

The agent silently maps the target site structure by querying Common Crawl's CDX, a searchable database of every URL the archive has ever crawled. This allows enumeration of all potentially relevant target URLs, without the server ever being contacted.

The request in Figure 2 returns archived URL paths, MIME types, timestamps, and status codes. The agent discovers objective-relevant Tableau visualization endpoints at “vizprod.aihw.gov.au” without ever touching AIHW servers.

*Effect: Agent identifies the target: `vizprod.aihw.gov.au/t/Public/views/AGE-115/...`*

**Step 2 — CRAFT: Build extraction payload**

The agent writes a self-contained HTML page with embedded JavaScript. This payload uses the Tableau JS API to load a dashboard; enumerate its parameters, worksheets, and filters; then beacon the extracted data out via an image request.

The L() function is the exfiltration design. Each call fires an image beacon to "httpbun.com/status/204" with data in the `?pr=` query parameter. The probe ID `p0011782077286` is a Unix-epoch timestamp enabling session correlation.

*Effect: Payload is ready, now encode as Base64 for hosting.*

**Step 3 — ENCODE: Host on legitimate decode service**

The entire HTML payload is base64-encoded and appended to a public decode service URL. When fetched, the service decodes and serves the payload as a real web page.

*Effect: The delivery URL is ready; next step is to submit to urlquery scanner.*

**Step 4 — SUBMIT: Launder through “urlquery.net”**

The agent submits the delivery URL to “urlquery.net”, a legitimate web security scanner. urlquery's Chromium sandbox fetches and renders the page, executing the embedded JavaScript. The target sees requests from urlquery's scanner IPs (“92.42.109.x”), not the agent.

**\[COORD sub-step\]** The self-label `?uq=p001_1782077286_AGE115_v14` includes a probe prefix (`p001`), Unix epoch, target identifier (`AGE115`), and iteration count (v14 = 14th payload revision).

*Effect: The chromium sandbox renders page, and payload JS executes.*

**Step 5 — EXECUTE: In-browser extraction via CORS proxy**

When the payload executes inside urlquery's sandboxed Chromium browser, it uses the Tableau JavaScript API to load the AIHW health statistics dashboard. Tableau's backend speaks a protocol called VizQL; earlier payload generations bypassed the full dashboard load and hit the VizQL session API directly via a CORS proxy, reusing session tokens the agent had collected from previous runs.

AIHW sees the request originating from Cloudflare's IP range, not the agent, nor urlquery.

*Effect: The data is validly extracted. Next, send out via a covert beacon.*

**Step 6 — EXFIL: Zero-byte 204 beacon**

Extracted data is URL-encoded into the query string of image beacon requests to "httpbun.com/status/204". The server returns `HTTP 204 No Content` with zero bytes back. The data travels exclusively in the request URL, which urlquery logs as an ordinary HTTP transaction.

Each beacon sends up to 1,800 characters. The 204 response means no data flows back to the browser, acting as a write-only channel.

*Effect. The transaction is logged; the agent retrieves report.*

**Step 7 — COLLECT: Read back via urlquery report**

After the scan completes, the agent retrieves the urlquery report JSON, which contains every HTTP request and response the browser made, including the exfil beacon URLs with embedded data in the `?pr=` parameters.

This closes the loop. The agent submitted a URL, urlquery's browser executed the payload, and the agent reads the results back from the public report. No direct connection between the agent and the target ever existed. The entire extraction was laundered through two intermediaries, httpbun.com (hosting) and urlquery.net (execution).

## Technique transfer in a growing ecosystem

In October, a second autonomous actor was identified via the same technique fingerprints. This time, the activity was attributed to a [<u>Tencent-hosted “fleet”</u>](https://swarmcha.se/posts/chinese-agent-fleet-full-report), operating from Tencent's Hong Kong network (AS132203). A fleet is distinguished from a swarm in that these agents were working on a unified task, but with no signs of coordination. The Tencent fleet’s activity focused on Alibaba’s Amap navigation service, polling points-of-interest data, with requests consistent with systematically collecting location listings and related details.

### Did the Tencent fleet learn from the OpenAI swarm?

The discovery of the Tencent fleet can largely be attributed to technique transfer; this group was following the path pioneered by the OpenAI swarm. The Tencent fleet used "urlquery.net" as a browser execution proxy, "httpbun.com" as a payload delivery host, and "webhook.site" as an exfil channel. There was also progression within the Tencent swarm’s capability. The early fleet operations initially used “httpbin.org/base64/”, and later the same infrastructure switched to “httpbun.com/base64/”, mirroring the OpenAI swarm's own progression to the same host.

A separate actor, operating independently, converging on the same non-obvious infrastructure in the same sequence is harder to explain without the OpenAI swarm's publicly indexed urlquery footprint as a common source. In fact, it seems likely that swarms will web search prior documentation of tradecraft relating to their tasking and could offer a potential explanation to how the Tencent fleet managed to find a write up about their own activity, and in turn, [<u>communicate with the authors</u>](https://swarmcha.se/posts/chinese-agent-fleet-full-report).

## Swarm dynamics in cyber attacks

You don’t look far to see where the insights from swarm behavior may transfer to cyber attack and defense implications. Recent intrusions from [<u>agentic cyber attack harnesses</u>](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) like [<u>ARTEX</u>](https://blog.talosintelligence.com/artex-and-beyond/) exhibit similar characteristics. However, these multi-agent planning systems are distinct in that they have architecturally solved the constraints the OpenAI swarm was working around. The swarm needed a browser (“urlquery.net”) to run JavaScript. ARTEX alleviates this constraint by running a headless Go backend that calls tools directly.

What may hold consistent are methods around the reconnaissance logic, the payload iteration, the structured work partitioning, or the self-labeling patterns. Those are properties of the planning layer, not the infrastructure (e.g., work unit identifiers encoding timestamps, geographic scope, and sequence counters). These coordination patterns may survive the move to purpose-built infrastructure, but they likely be only internally visible queue labels.

Further research will be required going forward to grapple with the emergence of agentic attack frameworks and pinning down the meaningful surface area they have for detection and mitigation. It seems possible these may be durable if they are tied to inherent preferences of the underlying models. In our limited analysis, several avenues seem promising:

- **Persistent-state exfiltration: writing results that outlast the agent**
In the documented[<u>ARTEX intrusions</u>](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/), victim machines used curl to POST command output to rotating "webhook.site" URLs. The Tencent fleet did the same by pre-creating "webhook.site" tokens from Tencent IPs before payload deployment, then routing exfiltrated data through them. The OAI swarm used image beacons for the same structural purpose.
This convergence reflects a constraint of agents; they can't hold a persistent connection back to an operator. A human running a reverse shell is present in real time to receive output. An agent executes a task, may spawn parallel sub-agents, and completes, or is terminated, before the operator checks in. Results must go somewhere that outlasts the agent's execution window, and parallel sub-agents need isolated write channels so they don't collide. That is what the web hooks, beacons, and message boards are solving. Egress bypass seems like a secondary benefit. These services will often happen to be allow-listed, which makes them harder to block.
- **Burst-and-pause reasoning loops**
Google Threat Intelligence Group (GTIG) describes ARTEX executing 27 events in 23 seconds, moving from compromised credential to deep system access in as little as 15 minutes and iterating on web shell candidates in real time, rapidly adjusting on error, trimming oversized payloads, and relaunching within seconds. GTIG measured individual burst sequences at 2 – 25 seconds, with sub-second actions inside them. The burst-and-pause timing signature can prove irregular in contexts that reveal rapid reasoning and adaptation.
- **Self-labeling conventions**
Agents mark their own work for later retrieval or correlation. The OAI swarm embedded full operational metadata into URL parameters. ARTEX has used "artex-probe-\*" file names. These patterns are high-fidelity signals precisely because they're functional for the agent. They may be useful for fingerprinting agent swarms, because they can't easily alter or remove the labeling scheme without breaking the agent's own state tracking.

## The agent-centric future

The 2026 swarm campaigns are not just a curiosity that preceded a threat; they are a snapshot of the same core capability, in the time before the infrastructure constraints were lifted. ARTEX and its cohort of agentic harnesses are now showing us what swarm dynamics look like when resources are unconstrained and aligned on a cyber attack objective.

While these systems are powerful, they are not universally appealing. Using a coordinated multi-agent system is still a trade-off decision for attackers, and one in a growing array of options. Single agent systems can reach the same performance of swarms, and do so more efficiently, following the logic around extending chain-of-thought or [<u>scaling test-time compute</u>](https://arxiv.org/abs/2408.03314). Swarm scaling primarily favors situations where speed is the most important factor.

Swarm engagements will have higher token cost, more noise, and require a broader operational footprint. Token costs, however, are only a concern when using an API. The growing list of local, open-weight models with improving cyber capabilities will continue to be an appealing alternative for attackers. As defenders, we need to recognize the distinction in behavior and capabilities and continue to search for identifying characteristics across these attack options and proactively harden our threat models in response.
