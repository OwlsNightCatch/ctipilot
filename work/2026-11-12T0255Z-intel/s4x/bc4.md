---
title: Notion says Fireworks breach exposed customer AI chat transcripts
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/notion-says-fireworks-breach-exposed-customer-ai-chat-transcripts/
hostname: bleepingcomputer.com
description: Notion, the digital workspace platform, disclosed that a security breach at its AI infrastructure provider, Fireworks AI, exposed Notion AI chat transcripts in a small number of workspaces.
sitename: BleepingComputer
date: "2026-11-11"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Artificial Intelligence, Customer Data, Data Breach, Fireworks, Notion, Third-Party Data Breach,virus removal, malware removal, computer help, technical support']
fingerprint: "3945189c189c258b"
---
Notion, the digital workspace platform, disclosed that a security breach at its AI infrastructure provider, Fireworks AI, exposed Notion AI chat transcripts in a small number of workspaces.

The disclosure comes shortly after [Fireworks AI confirmed](https://www.bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack/) that an attacker accessed its development environment via a third-party cloud provider on October 23 and compromised resource metadata, billing information, model weights, and datasets for some customers.

Fireworks AI experienced another breach in early October, when hackers accessed environment variables containing API keys and tokens stored as secrets for a limited number of accounts.

Notion learned about the exposed chat transcripts after receiving an alert from Fireworks on November 2 about an exposed dataset that contained only synthetic test data.

Notion responded by cutting off traffic to Fireworks, deleting all data from the vendor’s systems, and halting training runs by November 3.

However, Fireworks confirmed on November 8 that customer data had been accessed, [including that of Notion users](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor-nov9).

Notion is a cloud-based workspace used for note-taking, document creation, internal wikis, project management, and task tracking. It includes an AI assistant that can answer questions, summarize content, and help draft text.

Fireworks AI enables Notion to run some of the open-weight models available through Notion AI and analyze stored conversations for Insights, a feature that gives workspace administrators visibility into how their teams use AI.

The exposed transcripts came from the Insights dataset specifically, which has now been disabled.

“Upon analysis of the dataset Fireworks AI gave us on November 8, we discovered that it included Notion AI chat transcripts used for the Insights feature, which for the vast majority of impacted workspaces were unattributable,” [Notion stated in an update](https://www.notion.com/en-gb/security/advisories/security-incident-involving-a-third-party-ai-vendor).

"Unattributable means the chats weren't labeled with who wrote them or which workspace they came from, and the transcripts did not contain tool call results.”

Notion has also [published a FAQ page](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor) about the incident, highlighting that Fireworks had contractually committed to zero data retention for Notion data.

According to the company, less than 1% of its users are impacted by the incident. Potentially affected workspace owners should review the data through Security incident review in Notion’s desktop web interface and share a link with members that lets them download their own transcripts.

Notion advises affected users to rotate any passwords, API keys, or other credentials entered into affected chats.

If neither a user nor their workspace owner has received a notice, Notion says no action is needed for now, and they are most likely not part of the impacted subset.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
