---
title: Radware discloses breach exposing customer cloud access keys
author: Sergiu Gatlan
url: https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/
hostname: bleepingcomputer.com
description: Cybersecurity company Radware says attackers gained access to some of its customers' account details and cloud access keys through an unsecured internal Cloud WAF (Web Application Firewall) management API that was left exposed online.
sitename: BleepingComputer
date: "2026-11-24"
tags: ['computers', 'windows', 'linux', 'mac', 'support', 'tech support', 'spyware', 'malware', 'virus', 'security', 'API', 'Breach', 'Cloud', 'Credentials', 'Cybersecurity', 'Radware', 'Security Breach', 'WAF', 'Web Application Firewall', 'virus removal', 'malware removal', 'computer help', 'technical support']
fingerprint: ed738e1a8e1677cd
language: en
image: https://www.bleepstatic.com/content/hl-images/2026/11/24/Radware.jpg
pagetype: article
filedate: "2026-11-25"
---
Cybersecurity company Radware says attackers gained access to some of its customers' account details and cloud access keys through an unsecured internal Cloud WAF (Web Application Firewall) management API that was left exposed online.

Founded in 1996 and headquartered in Tel Aviv, Radware now provides application delivery and DDoS protection services to more than 12,500 enterprise and telecom carrier customers worldwide.

In a root cause analysis report shared by an anonymous source with BleepingComputer, Radware says it blocked the originating IP address and access to the internal management API. The company also revoked and replaced all internal account credentials after detecting the breach on Thursday, ten hours after the initial unauthorized API access.

"On 19 November 2026, an unauthorized party accessed an internal-only Cloud WAF management API that was reachable from the Public Internet without requiring authentication," Radware said.

"The confirmed information potentially accessed includes customer contact details, and for a subset of customers, the credentials configured for log export into their self-managed storage (AWS S3, Azure Blob Storage, or SFTP)."

The company added that the breach did not expose WAF traffic inspection, certificates, end-users’ data, customer application traffic, or cloud DDoS services and data.

## Customers advised to rotate exposed keys

It also "strongly" advised affected AppSec (WAF, BOT) customers to rotate Cloud WAF log export credentials (including Azure Blob Storage keys or SAS tokens, AWS S3 access keys, or SFTP credentials) as soon as possible and review access logs on their cloud storage accounts for unexpected access since at least November 19.

The company is still investigating the breach and whether any API keys or other customer information exposed in the incident were used without authorization, and said it has already received reports from customers about AWS alerts for an unfamiliar IP address attempting to access their log-export buckets.

"WAF traffic inspection and protection have continued without interruption, and we have not identified an impact on the availability or protection of customer applications and services," Radware added. "We have found no evidence to date of changes to customer security policies or of access to customer application traffic."

Radware has yet to issue a public statement regarding the incident or file a breach report with the US Securities and Exchange Commission.

BleepingComputer also reached out to a Radware spokesperson with questions about the incident, but a response was not immediately available.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
