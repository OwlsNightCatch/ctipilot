---
title: Barracuda XDR Integration Credentials
url: https://trust.barracuda.com/security/barracuda-xdr-integration-credentials
hostname: barracuda.com
sitename: Barracuda Networks
date: "2026-11-13"
fingerprint: "1c11d086cf87e58c"
---
# Barracuda XDR Integration Credentials

**Update: November 13, 2026, at 2:30 pm EST**

Barracuda’s investigation has confirmed how the attacker obtained initial access. The cloud access key used had been stored in a configuration file within the third party’s GitHub repository, which was exposed when the third party’s development environment was compromised. Other Barracuda credentials contained in the same file had already expired or have since been revoked.

Since this advisory was first published, Barracuda has continued extensive containment, remediation, and credential rotation activities across its cloud, data analytics, and source code environments. Barracuda has also retired two internal automation servers whose credentials were exposed, removed their access keys, and conducted a comprehensive review of access records on those systems. No evidence of attacker activity was identified. The investigation remains ongoing.

To provide additional transparency into the incident, Barracuda has published a detailed technical analysis, "[Forty-four hours: Anatomy of a machine-speed intrusion](https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion)," which outlines the incident timeline, root-cause findings, attacker activity, indicators of compromise, and response actions.

**Barracuda’s guidance to notified customers remains unchanged: revoke and recreate integration credentials and review activity within connected systems beginning November 1, 2026.**

## Additional Indicators

The attacker created cloud and Kubernetes resources with names beginning with the letter “i” followed by digits and no hyphen (for example, i31911, i28324probe, and i19engx1). Within GitHub, it used workflow files named i19ghci.yml and i19ci2.yml on branches beginning with i19ghci- and i19ci2-.

These naming conventions, the sequence of attacker activity, and the automated routines used to identify credentials and cryptocurrency wallets are consistent with publicly reported characteristics of ARTEX, an open-source AI-driven penetration-testing framework that security researchers have reported being used by both criminal and state-aligned threat actors since mid-2026.


**Published: November 10, 2026**

In early November 2026, Barracuda identified unauthorized activity within portions of its internal cloud environment. Barracuda acted immediately to contain the activity, terminate the attacker’s access, and rotate credentials and secrets across the environment.

One of the affected systems stores credentials used by Barracuda XDR to collect data from customers’ connected systems, such as Microsoft 365, Google Workspace, endpoint security platforms, and other integrated services. The attacker had access to this system between November 1 and November 2, 2026.

The investigation has found no direct evidence that customer integration credentials were viewed or accessed. Out of an abundance of caution, Barracuda has directly notified customers with potentially affected credentials. Those customers have been advised to revoke and recreate integration credentials and have received detailed [guidance](https://documentation.campus.barracuda.com/wiki/x/AYDGOg) to support those actions.

If an organization has not received a notification from Barracuda regarding this advisory, no action is required. This advisory applies only to organizations using an API integration for Barracuda Managed XDR Cloud or Monitored Endpoint. Organizations that do not use either integration are not affected and do not need to take any action.

## What Happened

- Activity window: November 1–2, 2026.
- Initial access: The attacker gained access through a third party that had been issued a cloud access key.
- What the attacker did: The attacker sought credentials stored across portions of the environment and used those credentials to move laterally.
- Evidence of financial motive: Commands executed by the attacker searched for cryptocurrency wallets and related assets, including:
  - Environment variables named WALLET, MNEMONIC, SEED, and PRIV
  - Ethereum keystore files
  - Extended private keys
  - Seed phrases
  - Kubernetes secrets with wallet-related names

  The activity is consistent with a financially motivated threat actor looking for cryptocurrency assets and reusable credentials.
- Who it resembles: The observed techniques are consistent with recently reported automated, AI-driven intrusion activity.

## What Barracuda Has Done

We have taken the following actions:

- Disabled the attacker’s known access and the compromised Barracuda credentials involved in the incident.
- Enhanced monitoring across XDR environments and customer-connected data sources for activity related to this incident.
- Increased threat hunting and investigation efforts across affected systems.

## Actions Barracuda is Continuing to Take

- Protecting integration credentials: We are moving them to a store that stays protected even if cluster administration is compromised.
- Logging: We have enabled full audit logging on the affected environments, and we are adding data-access logging where it was missing.
- Credential lifecycle: We are removing long-lived and over-privileged access keys, and expiring credentials held by vendors when their engagements end.
- Kubernetes hardening: We are restricting privileged workloads and limiting which services can read secrets. We have deployed runtime threat detection across our clusters.
- Continuing our investigation: Our investigation remains ongoing and we will continue to provide updates.

## Recommended Actions for Notified Customers

Customers who have been contacted by Barracuda should revoke and recreate their integration credentials and review connected system activity logs since November 1, 2026. Guidance for how to do this is available on [Barracuda Campus](https://documentation.campus.barracuda.com/wiki/x/AYDGOg). Customers and partners can also contact Barracuda at [SOC@Barracuda.com](mailto:SOC@Barracuda.com) with any questions.

## Indicators of Compromise

Organizations that wish to review their environments for activity potentially associated with this incident may look for the following indicators. The presence of these indicators does not by itself confirm malicious activity but may warrant further investigation.

- **IP addresses:**
  - 180.178.56.10
  - 52.128.238.126
  - 221.146.68.107
  - 2a09:bac1:7680:3d0::26b:5b
- **User agents:**
  - Boto3/1.43.122
  - curl/8.5.0
  - curl/7.81.0
  - Python-urllib/3.10
  - Mozilla/5.0 (compatible; read-only-audit)

## Don’t wait to get protected

Get a free consultation with a cybersecurity expert and see Barracuda's cybersecurity solutions in action.
