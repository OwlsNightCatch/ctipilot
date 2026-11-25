---
title: Radware report says an exposed Cloud WAF management API let an attacker reach customer cloud access keys
author: MLQ ai Newsroom
url: https://mlq.ai/news/radware-report-says-an-exposed-cloud-waf-management-api-let-an-attacker-reach-customer-cloud-access-keys/
hostname: mlq.ai
description: An unauthorized party reached an internal Radware Cloud WAF management API that was exposed to the internet without authentication on Nov. 19, according to a Radware root cause analysis report that B…
sitename: MLQ.ai
date: "2026-11-24"
categories: ['tech']
tags: ['Cloud', 'Cybersecurity', 'Radware']
fingerprint: "8d731a1a8e92234d"
language: en
image: https://mlq.ai/media/news_images/radware-report-says-an-exposed-cloud-waf-management-api-let-an-attacker-reac_zGjp4Oz.jpg
pagetype: article
filedate: "2026-11-25"
---
# Radware report says an exposed Cloud WAF management API let an attacker reach customer cloud access keys

- Radware says an internal-only Cloud WAF management API was "reachable from the Public Internet without requiring authentication" and was accessed on Nov. 19 <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.
- Exposed data included customer contact details and, for a subset of customers, credentials for exporting logs to AWS S3, Azure Blob Storage or SFTP <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.
- Radware has not issued a public statement or an SEC breach report, and did not immediately respond to BleepingComputer <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.

An attacker reached customer account details and cloud access keys at [Radware](https://mlq.ai/companies/radware-ltd/) through an internal Cloud WAF management API that was exposed to the internet, according to a Radware root cause analysis report shared with BleepingComputer by an anonymous source <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. The report says an unauthorized party accessed the internal-only API on Nov. 19 and that it was "reachable from the Public Internet without requiring authentication" <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.

Radware, an Israeli maker of application security and DDoS protection products listed on Nasdaq, says it serves more than 12,500 enterprise and telecom carrier customers, BleepingComputer reported <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. The report does not say how many customers were affected.

## What was exposed

According to the report, the attacker could see customer contact details and, for a subset of customers, "the credentials configured for log export" into storage the customers manage themselves: AWS S3 buckets, Azure Blob Storage or SFTP servers <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. Radware says WAF traffic inspection, certificates, end-user data, customer application traffic and its cloud DDoS services and data were not exposed, and that "WAF traffic inspection and protection have continued without interruption" <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.

Radware detected the intrusion on Thursday, about 10 hours after the first unauthorized access, blocked the source IP address and access to the internal API, and revoked and replaced all internal account credentials <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. It is still investigating whether the exposed keys were misused <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.

## What customers were told

Radware "strongly" advised affected AppSec (WAF and bot protection) customers to rotate their Cloud WAF log-export credentials, including Azure Blob keys or SAS tokens, AWS S3 access keys and SFTP credentials, and to review storage access logs for unexpected activity since at least Nov. 19 <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. Some customers told BleepingComputer they had received AWS alerts about an unfamiliar IP address trying to access their log-export buckets <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>.

Radware had not published a statement or filed a breach report with the SEC as of BleepingComputer's report on Nov. 24, and did not immediately respond to a request for comment <sup>[\[1\]](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)</sup>. Law enforcement involvement has not been disclosed.

## Companies mentioned

## Further sources

This article was produced by MLQ.ai's AI newsroom and checked against primary sources such as company filings, official releases and court documents. Reports from a single outlet are attributed. Editor: [Peter Foy](https://mlq.ai/about/peter-foy/). [How we work](https://mlq.ai/about/editorial-standards/) · Spotted an error? [Tell us](https://mlq.ai/contact/).

The stories that matter, in one email. Free — unsubscribe anytime.
