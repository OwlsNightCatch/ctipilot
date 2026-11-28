---
title: SAP confirms security incident after suspicious activity on GitHub
author: Jens Jonkers
url: https://itdaily.com/news/security/sap-security-incident-github/
hostname: itdaily.com
description: "Security incident at SAP: the company confirms suspicious activity and took measures. Tokens may have been stolen."
sitename: ITdaily
date: "2026-11-27"
categories: ['Security']
tags: ['GitHub', 'SAP']
fingerprint: "2c227713de12574b"
language: en
image: https://itdaily.com/wp-content/uploads/SAP-Walldorf-3.jpg
pagetype: article
filedate: "2026-11-28"
---
**SAP has suffered a security incident: the company confirms suspicious activity and took urgent measures to protect customers. The attackers allegedly stole employee tokens to copy and modify source code on GitHub.**

SAP confirms to [BleepingComputer](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/) that it detected suspicious activity in its IT environment and immediately took the necessary measures to protect customers. [Der Spiegel](https://www.spiegel.de/netzwelt/sap-wird-opfer-von-hackerangriff-a-6648b5ce-5d74-48dc-86ea-9469705bb91d) already reported on Thursday, based on an internal memo, that the incident concerns the GitHub environment of the German software company.

According to the German magazine, attackers allegedly stole authentication tokens from SAP employees and used them to copy and modify source code on GitHub. Sources within SAP say the attackers may have used AI agents. SAP confirms none of these details.

## The security incident at SAP

The investigation has so far found no evidence of unauthorised access to business customer data, SAP says. A spokesperson declined to explain which environments are affected and whether customers who pull code from SAP’s GitHub repositories or receive updates from them need to take action, BleepingComputer learned. SAP restricted access to GitHub, paused automated development processes and replaced signing keys.

Internally, the incident is called Project Granite. It affected many development teams, the same sources say.

## Modified code as a risk

SAP publishes source code for products and open-source projects on GitHub. Modified code becomes a supply chain problem if it ends up in a build or release unnoticed. SAP has not said whether that happened. An attacker gaining access to source code via GitHub also happened in recent weeks at [1Password](https://itdaily.com/news/security/github-account-hijacked-1password/). There, an attacker hijacked an employee’s GitHub account.

SAP does not say whether customers need to take action and has not yet disclosed which repositories are affected. According to [SOCRadar](https://socradar.io/blog/sap-security-incident-github-tokens-source-code/), anyone who uses SAP packages from GitHub should pin exact versions for now, check the release history for unexpected versions and follow SAP’s security advisories.
