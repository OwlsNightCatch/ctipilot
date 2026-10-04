---
title: "Agents Gone Wild: An AI-Orchestrated Global Campaign Against PaperCut NG/MF"
author: GreyNoise September 9
url: https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
hostname: greynoise.io
description: "11 organizations compromised in 26 seconds. GreyNoise breaks down the AI-enabled campaign against PaperCut NG/MF that hit 440 instances across 48 countries."
sitename: greynoise.io
date: "2026-09-09"
---
GreyNoise observes adversary activity through our Global Observation Grid (GOG), a network of sensors that draws attacker scanning and exploitation onto infrastructure we control. This lets us study adversary infrastructure, tooling, and tradecraft directly, without waiting for a victim investigation. GreyNoise has been tracking malicious use of [45.142.193.132](https://viz.greynoise.io/ips/45.142.193.132) since early July 2026 due to its use for attacks against internet facing technologies and devices from Palo Alto, Ubiquiti, Citrix, SonicWall, and Proxmox VE.

On 31 August 2026, a likely Russian-speaking malicious cyber actor (MCA) used 45.142.193.132 and artificial intelligence (AI) to develop, test, and use exploits for PaperCut NG/MF ([CVE-2026-81578](https://viz.greynoise.io/tags/papercut-cve-2026-81578-authentication-bypass-attempt) and [CVE-2026-82078](https://viz.greynoise.io/tags/papercut-cve-2026-82078-unsafe-reflection-rce-attempt)). PaperCut is print management software that enables organizations to track, charge, and manage printing, copying, and scanning jobs for organizations. PaperCut offers cloud and self-hosted versions. PaperCut NG and MF are self-hosted Java web applications that by default run with SYSTEM-level privileges on Windows and are usually domain-joined and integrated with Active Directory. As part of the adversary’s exploit development and testing, they built and attacked a lab environment that included the vulnerable PaperCut software and an Active Directory server. In parallel workflows, the adversary built target lists using an internet scanning service Netlas.io using an identified API key.

Once the adversary achieved remote code execution (RCE) and credential harvesting in its self-hosted lab environment, they used hundreds of AI Agents powered by OpenAI’s Codex (harness), a DeepSeek model (not OpenAI models), and various publicly available offensive security tools to opportunistically compromise at least 440 instances of PaperCut MF/NG hosted by 395 identified victim organizations in 48 countries. There are other real victims that could not be attributed to a named organization. The adversary did explicitly attempt to avoid targeting entities in 28 identified countries; however, our observed victimology shows the attempted restraint failed in some instances.

It’s clear that large language models (LLM) are enabling adversaries to move at greater speed and scale. The adversary went from an empty workspace to first achieving RCE against a real victim in just under four hours, first domain admin in an additional two hours, and once the full campaign launched, compromised at least 11 organizations in 26 seconds. In one instance, the adversary went from initial access to full domain administrator in seven minutes against a high school in the United States. However, the adversary did not experience success evenly across all victims. GreyNoise observed the adversary achieved domain admin against only 12 victim organizations.

The adversary did not immediately follow-up with all compromised victims, so there were multiple-day delays between initial access and achievement of domain admin but only due to a lack of action by the adversary. Where domain admin was achieved, the adversary’s fastest time was five minutes and the longest time was 144 minutes. At GreyNoise’s time of last observation, the adversary had not achieved domain admin against the other victims. In at least one instance of targeting a perceived vulnerable PaperCut instance, Cloudflare’s Web Application Firewall (WAF) defeated the adversary. Fundamental hardening of environments still matters against AI-enabled threats.

It is unclear if this actor is solely focused on access development to be handed off to other affiliated actors or if they will directly leverage their accesses to achieve follow-on objectives such as data theft or ransomware deployment. In the past, other intrusions involving exploitation of PaperCut have led to extortion. GreyNoise partnered with industry leading incident response services organizations to conduct victim notifications around the clock.



## Key Takeaways

- Despite U.S. based frontier model guardrails, adversaries are using a variety of large language models to conduct intrusions globally
- AI enables fast and efficient complex orchestration of cyber operations; however, unless properly constrained, agentic operations can deviate from expected behavior and pose operational risk
- Organizations are not helpless against agentic attacks and traditional hardening does have a positive impact on the security posture of an organization


## Intrusion Attack Lifecycle

Where domain admin was achieved, GreyNoise observed three attack paths:

**Attack Path A.**

If the compromised PaperCut host was a domain member, the adversary harvested LSASS process memory and registry secrets to recover privileged credentials to pass-the-hash to the domain controller.

**Attack Path B.**

In instances where the victim had not patched for CVE-2021-42278 and CVE-2021-42287, the adversary used a [‘noPac’ attack.](https://www.sophos.com/en-us/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware)

**Attack Path C.** 

If the compromised PaperCut host was on the Domain Controller itself or running as a Domain-Admin service account, the adversary simply added its newly created account to Domain Admins.

In all Attack Paths, the adversary used DCSync to create a full NTDS.DIT dump to exfiltrate the organization’s credentials.



## Indicators of Compromise

Note that these IOCs are not exhaustive, the AI-enabled adversary continued to make necessary changes on the fly. GreyNoise will continue to add new IOCs on our [GitHub](https://github.com/GreyNoise-Intelligence/gn-research-supplemental-data).


## Adversary Tool Kit

The MCA had a library of publicly available offensive security tools used to expand access to the enterprise environment. Note that not all of these tools were observed in active use during this campaign.


## Targeting and Victimology

This campaign appears to be opportunistic. There is a high concentration of U.S. based targets in the education sector; however, it’s likely that is more attributable to the customer base of PaperCut NG/MF.

The adversary used a list of defined countries to avoid that existed from previous campaigns. It’s currently uncertain why the MCA’s agents deviated, but it is a good example of Agents Gone Wild. The countries to avoid in order were: Russia, China, Hong Kong, Thailand, Iran, Venezuela, Belarus, Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan, Armenia, Azerbaijan, Moldova, Ukraine, Brazil, Vietnam, Indonesia, Pakistan, Tanzania, Bangladesh, Afghanistan, Turkey, South Africa, Namibia, Nigeria, and Zimbabwe.


### Volume by Country


### Volume by Industry


GreyNoise will continue monitoring the situation and report updates as needed.

[Read the full report](https://www.greynoise.io)
