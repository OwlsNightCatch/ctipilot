---
title: What happens when a fake coding test reaches a security company?
author: About the Author
url: https://www.sophos.com/en-us/blog/fake-coding-test-reaches-security-company
hostname: sophos.com
description: Fake job interviews are an established way to target developers
sitename: SOPHOS
date: "2026-11-04"
fingerprint: "45a495f9c83546ac"
---
## An established technique

Developers are attractive targets. Their laptops and accounts often reach source code, build systems and production infrastructure, so attackers put real effort into getting onto them. Fake recruitment is one of the most established ways to do it: the attacker poses as an employer, runs a plausible interview process, then asks the candidate to download and run a coding assignment.

The technique is in the news this week after Binance's [$6.3 billion theft](https://www.coindesk.com/business/2026/11/03/binance-s-usd6-3-billion-hack-began-with-a-fake-job-interview-exchange-says), which began with a job interview. According to Binance, a software engineer was approached in September through a legitimate job platform and told to download a coding assignment onto his work computer. The FBI has attributed the attack to North Korea.

### Our close call

In September, an industry partner tipped us off through an intelligence-sharing channel: one of our employees' Macs had been compromised. The day before a similar lure reached one of our employees, and the employee had opened a GitHub "coding assignment" in VS Code. A command hidden in the workspace settings ran as soon as a terminal opened, and within two minutes the BeaverTail loader and InvisibleFerret backdoor were running. To be clear, we’re not suggesting this was necessarily the exact malware used at Binance. The broader concern is that employment-themed social engineering is used by multiple [North Korean threat groups.](https://www.sophos.com/en-us/threat-profiles?taxonomy_state_sponsored=North+Korea&page=1&pageSize=10&locale=en-us) So this isn’t an isolated trick associated with one campaign, but part of a wider and well-established playbook.

An external tip-off is a gift, but it's also very uncomfortable. By the time one arrives, most of your other controls have already failed. Ours failed for a mundane reason: the Mac's endpoint agent was broken. Unprotected assets are one of the most common and least glamorous failure points we see across our customer base. This time it impacted us.

We routinely publish root cause analysis for incidents like this one. See [INC-2026-002](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002) for more details on the attack and our corrective actions.

**A similar lure, a different attack**

Both attacks abused trusted developer tooling. Ours used a VS Code workspace feature and a handful of scripts. According to [Binance](https://www.binance.com/en/blog/community/3229153443759566763), its attacker swapped the legitimate pyenv component in the engineer's Homebrew installation for a malicious version, used it to contact an attacker-controlled server, and cleaned up traces as it went. Binance says its endpoint tools didn't detect that malware. Our endpoint protection already detected the payload used against us: SophosLabs confirmed that the first script dropped on the Mac was already detected as Troj/Dloadr-EJE. A working agent would have stopped the chain.

## What to do about it

We'd suggest three things.

**Find the endpoints that have gone quiet.** We already had device-compliance checks and endpoint coverage monitoring in place, but this incident showed a gap between them. Correlating identity sign-in data with endpoint telemetry closed it: a device that's still signing in but not reporting to your endpoint console is a coverage gap. Joining those views up surfaced devices that passed identity and device-management compliance but weren't reporting to our corporate console.

It's worth noting that we found a long tail of edge cases that stopped this data joining up cleanly (some unique to Sophos, such as the way we test beta versions of our endpoint internally). This complexity had thwarted previous reconciliation attempts, but this time, with the help of an AI agent, we were able to work through the messy bits far more efficiently. Tackling some of the historic complexity allowed us to tighten our device-management compliance checks to prevent a recurrence. The investigation informed a proposed detection for this kind of visibility gap.

**Treat North Korea's targeting of IT staff as one threat.** A year ago we published our [CISO playbook on North Korean IT workers](https://www.sophos.com/en-us/trust/ciso-playbooks/north-korean-it-workers). It includes a control matrix, an implementation guide and training slides, all built from our own hiring controls and CTU research. The playbook focuses on keeping fraudulent hires out. Fake interviews run the same scheme in reverse. Instead of posing as a candidate to get inside your company, the attacker poses as an employer to get onto your employee's laptop. The investigation also informed a proposed detection for this kind of visibility gap.

Many controls overlap: identity verification, least privilege, monitoring for unauthorized remote access tools, and endpoints that actually work. As the Binance incident highlights, defending against compromised developer devices is challenging but critical. At Sophos, one of our principal risks focuses on ensuring we have a strong "firebreak" between our corporate and product environments. Our threat model considers compromise of both privileged developer and IT sysadmin endpoints or identities.

**Scope what your AI tools can reach**. Binance’s attacker used an internal AI tool to move from one engineer to two others. Whether a tool is misused by prompt injection or by a compromised user, the defence is the same: assume the AI layer will be breached and contain what it can reach. We set out seven patterns for doing that in our [lethal trifecta blog](https://www.sophos.com/en-us/blog/inside-the-lethal-trifecta-blast-radius-reduction-in-ai-agent-deployments), including credential isolation, sealed tool endpoints and human approval for irreversible actions.

## A state-sponsored criminal enterprise

North Korea is an unusual state actor. Most state-sponsored groups steal secrets. North Korea also steals money, at scale, to fund the regime. Chainalysis estimates it stole [$2.02 billion in cryptocurrency in 2025](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/), most of it from the $1.5 billion Bybit heist. The Binance attack alone is roughly three times that figure.

It also innovates like a startup. Sophos Counter Threat Unit (CTU) researchers track several overlapping North Korean groups:

- [NICKEL ALLEY](https://www.sophos.com/en-us/blog/nickel-alley-strategy-fake-it-til-you-make-it) runs the Contagious Interview campaign: fake companies, fake recruiters and malicious code repositories, plus ClickFix lures and poisoned npm packages. The VS Code technique used against us matches its tradecraft.
- [NICKEL TAPESTRY](https://www.sophos.com/en-us/blog/nickel-tapestry-expands-fraudulent-worker-operations) runs the fraudulent IT worker scheme. It has been active since at least 2016, is expanding into Europe and Japan, uses generative AI to build fake CVs and has turned to data-theft extortion.
- [NICKEL GLADSTONE](https://www.sophos.com/en-us/threat-profiles/nickel-gladstone) is a financially focused subgroup that has targeted cryptocurrency exchanges since at least 2018, including through TraderTraitor, the name the FBI has linked to the Binance attack.

A [September joint advisory](https://www.mofa.go.jp/files/101089150.pdf) from Japan's National Police Agency, the FBI and partners puts the scale in perspective. Between December 2025 and July 2026, the Contagious Interview actors (which the advisory calls WaterPlum) compromised at least 30,000 devices in more than 100 countries and took funds or credentials from over 7,000 cryptocurrency wallets. The advisory also found that they and some North Korean IT workers sit under the same government bureau.

The common thread is the target: IT people. Developers, DevOps engineers and administrators hold the keys, and North Korea has learned that the job market is the easiest way to reach them. The attackers who hit Binance needed one engineer's laptop. So did the attackers who targeted us. The difference was what that laptop could reach, and how quickly someone noticed.
