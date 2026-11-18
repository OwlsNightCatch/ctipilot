---
title: "Forty-four hours: Anatomy of a machine-speed intrusion"
author: Arve Kjoelen
url: https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion
hostname: barracuda.com
description: "Barracuda's account of a 44-hour, machine-speed intrusion: how it began, how we found it, what we did for customers, and what it means for cybersecurity."
sitename: Barracuda Blog
date: "2026-11-11"
tags: ['Attacks, Threat Actors, and Data Breaches']
fingerprint: "8c8311864f278505"
---
# Forty-four hours: Anatomy of a machine-speed intrusion

#### What we saw, how we found it, and what it means for cybersecurity

Earlier this month, Barracuda was the target of a fast-moving intrusion into parts of our cloud environment. We published a [Trust Center advisory](https://trust.barracuda.com/security/barracuda-xdr-integration-credentials) on November 10 with the customer-facing details, and we have contacted customers we believe could be affected. This post is the story behind that advisory: what the attacker did, how fast it moved, what it was looking for, and what we think it means for the industry.

## How it started

The attacker did not break down our door. It gained access using a valid cloud access key.

As part of a previous project, we provided a cloud access key to a third-party vendor. We did not retire the key when the vendor — a company working in AI — finished that work. That is on us.

In October, the vendor’s own development environment was compromised. That appears to be where the attacker found our key.

## What we observed and when

All times are UTC.

- **November 1, 04:33.** The attacker made its first call with the key. Within minutes, it was mapping what the key could reach. The attacker used the key to read stored secrets such as AWS access keys and Azure service principal secrets.
- **Over the next 24 hours.** The attacker used each secret it found to reach the next system:
  - From our cloud accounts to a data analytics system;
  - From there to a source-code access token;
  - From there to Kubernetes clusters.
- **November 2, early hours.** In just under four hours, the attacker pushed short-lived branches to a handful of repositories in order to trigger a build workflow written to print the build system’s secrets into the job log. The secrets were encoded so that the log’s usual secrets masking would not hide them.
- **November 2, 23:31.** The last activity we recorded.

In all, the attacker touched about 10 cloud accounts in roughly 44 hours. The work was methodical and tireless. It referred to resources with machine-style labels: the letter “i” followed by digits, with no human-readable words.

Those labels were fingerprints. The probe names, the other indicators we collected, the order in which the attacker worked through our systems, and its built-in routines for hunting credentials and wallets all match ARTEX.

ARTEX is an open-source, AI-driven penetration-testing framework released in July 2026. A “planner” AI agent decides the next step, and “worker” agents run common tools and add what they find to a shared map of the target. It was built for authorized security testing. Within weeks of its release, researchers at Wiz, Microsoft, Google, and CrowdStrike reported both criminal and state-aligned groups using it in real-world attacks, typically with a human steering it at key moments.

Because many groups use ARTEX, the match tells us how the attacker operated, not who it was.

## What the attacker was looking for

Two things stood out.

**Credentials and secrets. Everywhere.** The attacker read secret stores. It decrypted infrastructure-as-code state files, which often contain credentials. It pulled credentials from server metadata services and from Kubernetes service accounts. Every credential it found became a lead to follow.

**Cryptocurrency.** On a group of servers where it gained shell access, the commands searched explicitly for:

- Environment variables named WALLET, MNEMONIC, SEED, and PRIV
- Ethereum keystore files
- Extended private keys
- Seed phrase files
- Kubernetes secrets with wallet-related names

No wallet material exists on those systems. But the intent was clear.

A third motive cannot be ruled out. Some of the secrets in the attacker’s reach were credentials for AI services. The vendor the attacker came through is an AI company. As we explain below, we are not the only organization to see this pattern.

## The backdoor

Attackers who expect to be found leave a way back in. This one did.

Using access to one of our Kubernetes clusters, it deployed a container that mounted the underlying server’s file system. The container was restricted to read-only access, but that was sufficient to harvest that server’s credentials. It also tried to create a new administrative cloud identity for itself. That attempt was blocked.

We removed the container on the evening of November 4, Pacific time. Credential rotation followed across every system involved.

## How we found it

It started with an engineer and information from a partner.

On November 4, one of our engineers noticed unusual activity on their own account and reported it. We quickly traced it back through the chain described above.

That same day, the vendor contacted us about their own incident. They did not believe Barracuda had been affected, but they shared what they knew anyway. That information helped us connect the dots faster. We are grateful they did not wait until they were certain.

By the time the activity was reported, it had already stopped. The attacker had finished its run in less than two days. That gap is the most important lesson of this incident.

## An eerily similar attack

In October, attackers broke into Railway, a cloud application hosting platform. [Railway’s incident report](https://blog.railway.com/p/incident-report-october-security-incident) describes an attack chain much like ours:

- An initial foothold
- A copy of internal source code
- A misconfiguration
- A credential that unlocked customers’ stored secrets

The attackers then used stolen customer AI-service credentials to generate an estimated $740,000 in unauthorized compute costs. Railway believes the keys were resold for “distillation,” meaning querying commercial models at scale to train copies. Railway described the response as “a contest of agent speed,” against what Wiz characterized as a harness similar to ARTEX.

The Wall Street Journal recently reported on the same trend: [AI computing power has become a prized commodity for criminals](https://www.wsj.com/tech/ai/hackers-hunt-for-ais-most-valuable-commodity-computing-power-4c2054d5), and AI credentials now trade like currency. Railway works in AI infrastructure, just as our vendor does. Security researchers report that at least nine AI developer platforms disclosed incidents in October alone.

The observed activity was consistent with a financially motivated attacker seeking cryptocurrency assets and reusable credentials. Crypto wallets were clearly on its list. Given how many AI-adjacent companies are being hit in similar ways, it would be naïve to rule out that AI service credentials and the computing power behind them were part of the prize.

## What we did for customers

One of the systems the attacker reached stores the credentials that Barracuda XDR uses to collect data from customers’ connected systems. Our investigation found no direct evidence that the attacker viewed or accessed those credentials. However, logging in that environment was not detailed enough to rule it out.

So, we made a scoping assumption: assume the worst. We treated every credential within the attacker’s reach as potentially compromised and rotated credentials and secrets across the affected environment. For customers, we identified the potentially affected API integration credentials for Barracuda Managed XDR Cloud or Monitored Endpoint and contacted those customers directly. We asked them to revoke and recreate their integration credentials and provided step-by-step guidance. If you have not heard from us, no action is needed. The details are in our [Trust Center advisory](https://trust.barracuda.com/security/barracuda-xdr-integration-credentials).

We would rather ask some customers to rotate keys that were never touched than leave one exposed.

## What this means

Vulnerabilities and incidents are rising sharply, and attackers now move at machine speed. This attacker crossed five platforms in less than two days. Defenders who rely on spotting malicious activity and then responding to it will often arrive after the attacker has finished.

**1. Detect-and-respond, as the primary strategy, is dead.** The focus must move to prevent and recover. Detection still matters, but it cannot be the only plan. In practice:

- **Remove standing credentials.** Long-lived keys, especially those held by third parties, are pre-positioned access for an attacker. Short-lived, narrowly scoped credentials would have stopped this intrusion at its first step.
- **Shrink the blast radius.** No single credential should open the next door, and the one after that.
- **Assume compromise and be able to recover quickly.** That means rotating secrets at scale, rebuilding from known-good states, and making scoping decisions that assume the worst rather than hope for the best.

**2. Information sharing must be stronger and faster.** The most useful outside signal we received came from a company that did not think we were affected, and it arrived two days after the attack began. Both things need to change. Companies should share indicators and context early, even when unsure who is affected. That is difficult today because most sharing still depends on people writing emails and making phone calls. It will improve with increased automation as companies increase sharing with public threat feeds.

We are applying these lessons in our own environment, and we will keep sharing what we learn.

What MSP customers need next, from the backroom to the boardroom

Barracuda Research found that technical excellence remains essential, but future growth will be driven by AI expertise, cyber resilience, and the ability to communicate risk in business terms.

Subscribe to the Barracuda Blog.

Sign up to receive threat spotlights, industry commentary, and more.

Cybersecurity skills gap report: AI risk tops the list

Barracuda Research survey of 2,000 security leaders finds 94% report cybersecurity skills gaps, at the same time as AI reduces entry-level security roles that help develop future investigators.
