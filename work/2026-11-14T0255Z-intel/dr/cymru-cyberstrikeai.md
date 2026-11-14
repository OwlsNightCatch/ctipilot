---
title: "Tracking CyberStrikeAI: AI-Native Offensive Tools & MSS Ties | Team Cymru"
author: Will Thomas; Team Cymru
url: https://www.team-cymru.com/post/tracking-cyberstrikeai-usage
hostname: team-cymru.com
description: Discover how CyberStrikeAI is revolutionizing AI-augmented offensive security. Explore its ties to Chinese state-sponsored actors and learn to detect it with NetFlow.
sitename: Team Cymru
date: "2026-03-02"
fingerprint: fd5340d6852ed6a4
---
March 2, 2026

# Tracking CyberStrikeAI Usage

Team Cymru is continuously monitoring our global netflow visibility to uncover patterns of adversary activity, identify malicious operations, and gain actionable intelligence. In this post, we are diving into CyberStrikeAI, an open-source artificial intelligence (AI) offensive security tool (OST) developed by a China-based developer who we assess has some ties to the Chinese government.

## What is CyberStrikeAI?

In its own words from the GitHub repository (see [here](https://github.com/Ed1s0nZ/CyberStrikeAI)), ‚ÄúCyberStrikeAI is an AI-native security testing platform built in Go. It integrates 100+ security tools, an intelligent orchestration engine, role-based testing with predefined security roles, a skills system with specialized testing skills, and comprehensive lifecycle management capabilities.‚Äù

CyberStrikeAI comes with its own dashboard that helps users quickly understand the platform's core features and current state, as shown in Figure 1 below.

CyberStrikeAI was first brought to our attention following the Amazon CTI team‚Äôs [blog](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/) about AI-augmented threat actor infrastructure they had discovered. Amazon shared this related IP 212.11.64\[.\]250.

Analysis of that IP address in Team Cymru Scout‚Äôs open port scan data revealed that it had this ‚ÄúCyberStrikeAI‚Äù banner running on this service, as shown in Figure 2 below.

**Identifying Targeting with NetFlow**

Using Team Cymru Scout, we can find NetFlow communications between the IP shared by Amazon and its targets, such as the Fortinet FortiGate devices it was observed targeting, as shown in Figure 3 below.

## Researching Ed1s0nZ

While researching the GitHub profile (see [here](https://github.com/Ed1s0nZ)) of CyberStrikeAI‚Äôs developer, ‚ÄúEd1s0nZ‚Äù, several attributes about the individual caught our attention.

Firstly, Ed1s0nZ‚Äôs other GitHub repositories suggest interest in exploitation activity:

- **watermark-tool:** A secure and efficient invisible document watermarking solution that can add completely invisible digital watermarks to various documents, while supporting watermark extraction and verification. Developed in Go, it supports both web and CLI usage. The watermark uses steganography technology to ensure that the watermark is completely invisible and does not affect the reading experience and visual effects of the original document.
- **PrivHunterAI:** This tool uses a passive proxy approach and mainstream AI (such as Kimi, DeepSeek, GPT, etc.) to detect privilege escalation vulnerabilities. Its core detection function is built on the open APIs of the relevant AI engines and supports data transmission and interaction via HTTPS protocol.
- **InfiltrateX:** A useful privilege escalation scanning tool. While automated detection of privilege escalation vulnerabilities is difficult, prone to occur, and poses serious risks, it can still strive to automate the detection of some such vulnerabilities.

Further, Ed1s0nZ‚Äôs GitHub activities indicate they interact with organisations that support potentially Chinese government state-sponsored cyber operations. This includes Chinese private sector firms that have known ties to the Chinese Ministry of State Security (MSS).

A number of GitHub activities potentially link Ed1s0nZ to the Chinese state-sponsored cyber operations. On 19 December 2025, Ed1s0nZ [posted](https://github.com/knownsec/404StarLink/issues/190) CyberStrikeAI to Knownsec 404‚Äôs Starlink Project, as shown in Figure 4 below. Based on published [reporting](https://dti.domaintools.com/research/the-knownsec-leak-yet-another-leak-of-chinas-contractor-driven-cyber-espionage-ecosystem) by DomainTools and others, Knownsec does work for the MSS and the Chinese People‚Äôs Liberation Army (PLA).

Further, on 5 January 2026, Ed1s0nZ [added](https://github.com/Ed1s0nZ/Ed1s0nZ/commit/2b8a84e689e9fe2fdad517c7e196604ef33cf76b) to their GitHub profile ‚ÄúCNNVDÔºàÂõΩÂÆ∂‰ø°ÊÅØÂÆâÂÖ®ÊºèÊ¥ûÔºâ 2024 Âπ¥Â∫¶ÊºèÊ¥ûÂ•ñÂä±ËÆ°Âàí ¬∑ ‰∫åÁ∫ßË¥°ÁåÆÂ•ñÔºà‰∏™‰∫∫). Translation: CNNVD (Chinese National Vulnerability Database) 2024 Vulnerability Reward Program - Level 2 Contribution Award (Individual).‚Äù The CNNVD is run by CNITSEC and is also overseen by the MSS. Arguably, this program exists as a vehicle for the CCP to collect zero days before they are publicly disclosed, as [detailed](https://www.bitsight.com/blog/chinese-vulnerability-database-analysis-cnvd-cnnvd) by researchers at BitSight.

Interestingly, we noticed Ed1s0nZ [removed](https://github.com/Ed1s0nZ/Ed1s0nZ/commit/5c806c2580fadd9b564b9d32b0db3364dfd0349e) the reference to the CNNVD from their GitHub profile, potentially in effort to cover up these ties to one of these MSS-affiliated organisations.

## Number of IPs Over Time

While researching CyberStrikeAI, we noticed that the repository was first added on 8 November 2025, as shown in Figure 5 below.. We did not observe a lot of IPs running the platform around this date though.

However, from 20 January 2026 to the conclusion of this assessment on 26 February 2026, we observed 21 unique IP addresses running CyberStrikeAI, over differing periods of time, as shown in Figure 6 below.

## Where users hosted CyberStrikeAI

Many of the CyberStrikeAI servers were hosted in Chinese-speaking locals, namely China, Singapore, and Hong Kong. Which is to be expected for a tool developed by a Chinese-speaking coder.

## Outlook

Based on our analysis, the adoption of CyberStrikeAI is poised to accelerate, representing a concerning evolution in the proliferation of AI-augmented offensive security tools. While the GitHub repository was initially created in November 2025 with minimal active deployments, the rapid emergence of 21 unique IP addresses running the platform between January 20 and February 26 indicates a sharp increase in operational usage. Because the platform is heavily hosted in regions like China, Singapore, and Hong Kong, we anticipate that CyberStrikeAI will continue to see strong adoption among Chinese-speaking threat actors.

Furthermore, the developer‚Äôs (Ed1s0nZ) documented interactions with organizations affiliated with the MSS, specifically Knownsec and the CNNVD, suggest a high likelihood that this tool may be leveraged by Chinese state-sponsored advanced persistent threats (APTs). The developer's recent attempt to scrub references to the CNNVD from their GitHub profile points to an active effort to obscure these state ties, likely to protect the tool's operational viability as its popularity grows.

As adversaries increasingly embrace AI-native orchestration engines, we expect to see a rise in automated, AI-driven targeting of vulnerable edge devices, similar to the observed reconnaissance and targeting of Fortinet FortiGate appliances. In the near future, defenders must be prepared for an environment where tools like CyberStrikeAI, alongside the developer's other AI-assisted privilege escalation projects like PrivHunterAI and InfiltrateX, significantly lower the barrier to entry for complex network exploitation. Security teams should proactively monitor their environments using the provided IP indicators and prepare for the continued weaponization of AI in offensive cyber operations.

## Related IP addresses

Search, pivot, and act on internet infrastructure in one AI-assisted environment, built on visibility into 400B+ daily connections.

[Get an Analyst-Led Walkthrough →](https://www.team-cymru.com/lp/command-center-walkthrough)

Search, pivot, and act on internet infrastructure in one AI-assisted environment, built on visibility into 400B+ daily connections.

[Get an Analyst-Led Walkthrough →](https://www.team-cymru.com/lp/command-center-walkthrough)
