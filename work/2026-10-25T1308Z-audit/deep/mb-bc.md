# extract: served via trafilatura-direct
---
title: Metabase SQLi zero-day exploited in customer data-theft attacks
author: Mayank Parmar
url: https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/
hostname: bleepingcomputer.com
description: A critical Metabase SQL injection vulnerability was exploited in zero-day attacks to breach customer instances in data theft attacks, known to impact Framework and Tally.
sitename: BleepingComputer
date: "2026-08-07"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Actively Exploited, Data Theft, Framework, LexisNexis, Metabase, SQL Injection, Zero-Day,virus removal, malware removal, computer help, technical support']
fingerprint: "2495c9c39823a7ae"
---
A critical Metabase SQL injection vulnerability was exploited in zero-day attacks to breach customer instances in data theft attacks, known to impact Framework and Tally.

Metabase disclosed the attacks on Thursday, warning that its Metabase Cloud SaaS platform was compromised through a previously unknown vulnerability affecting versions 1.58 and above. The company warns that self-hosted installations are also vulnerable.

"We recently identified that Metabase Cloud was attacked by someone utilizing an unknown ("0-day") security vulnerability in versions 1.58 and above," Metabase CEO Sameer Al-Sakran warned in a [blog post](http://www.metabase.com/blog/security-update).

Metabase confirmed it blocked the endpoints used for the attack and immediately rolled out a fix for the vulnerability.

"The vulnerability is an unauthenticated SQL injection flaw in Metabase that can ultimately give a remote attacker administrator access to a customer's instance."

While Metabase has not assigned the vulnerability a CVE identifier, its security advisory rates it as Critical with a CVSS score of 10.0 and confirms that it has been actively exploited.

"This is a CRITICAL vulnerability that allows an unauthenticated remote attacker to inject arbitrary SQL into the Metabase application database, which can give them administrator access to the instance," reads an associated [security advisory](http://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf).

"From there, the attacker could change the application configuration, steal stored credentials for the connected databases, read any data accessible through those connections, and export data. Metabase has confirmed active exploitation of this vulnerability."

Metabase is available both as software that organizations can host themselves and through Metabase Cloud, the company's managed SaaS offering.

Metabase says its Cloud customers have already been upgraded and patched, while organizations running vulnerable self-hosted installations must update manually.

The SQLi vulnerability has been fixed in patched versions for all affected branches from 0.58 through 0.63, with the minimum safe releases being 0.58.24, 0.59.21, 0.60.17, 0.61.11, 0.62.9, and 0.63.5.

Organizations unable to upgrade immediately are advised to temporarily block access to the '`/api/session/reset_password`' endpoint until the update can be applied.

Metabase recommends that self-hosted customers immediately upgrade, revoke all active user sessions, review API keys and administrator accounts for unauthorized changes, rotate credentials for connected databases, and inspect logs and query history for signs of compromise.

The company says attacks can be identified by a POST request to `/api/session/reset_password` returning a 400 status code, followed by a successful GET request to `/api/user/current`.

Metabase warns that system logs showing these entries have likely been compromised.

## Customers disclose Metabase data theft attacks

Laptop maker **Framework** is one of the companies that has confirmed customer information was stolen after attackers compromised its Metabase instance.

In a breach notification sent to customers and shared with BleepingComputer, Framework said the incident allowed the attackers to steal customer information. The stolen data includes full names, email addresses, login IP addresses, billing and shipping address information, phone number, and company name.

For Framework for Business customers, the data may also include the company name, phone number, VAT, EIN, and billing email address.

Framework said Metabase notified the company on August 6 that its instance had been vulnerable to the zero-day and accessed by the attacker on August 3.

**Tally**, the popular online form builder, has also [notified users](https://news.ycombinator.com/item?id=49213500) that its Metabase analytics environment was compromised on August 3.

"Through that they reached your email address, and your password as a cryptographic hash. A hash is one-way, so it can't be turned back into your password. They didn't reach your forms, or the answers people submitted to them. Those are stored separately."

BleepingComputer asked Tally which password hashing algorithm was used and whether the exposed password hashes were salted, but had not received a response at the time of publication.

*Update 8/10/26:* This article previously mentioned that LexisNexis was impacted by a breach related to Metabase.

However, the company has told us that their disruption is unrelated to the Metabase zero-day attacks and due to [different third-party security incident](https://www.bleepingcomputer.com/news/security/lexisnexis-shuts-down-services-after-suspicious-activity-on-servers/).

## [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)

Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
